# Quantitative Quality-Control Consistency Review: Graham et al. Package

## Pending Human Adjudication

**All three quality-control candidates are Pending Human Adjudication.** They identify printed quantitative, summary-label, or method-label inconsistencies for human review. They do not determine a correction or study conclusion.

## Executive Quality-Control Summary

Complete source coverage identified **3** stable quality-control candidates: C001, C002, and C003. The review mapped all 40 supplied PDF pages, checked 56 numeric/reporting relationships and 25 inferential-statistical relationships, and completed two independent statistical passes. Small preventable reporting defects can matter for downstream evidence extraction; this report does not claim that any defect propagated, changed a conclusion, or caused serious harm.

## Package and Reused-Evidence Provenance

The supplied package comprises the main article, study protocol, and results supplement. Direct-source evidence is authoritative; existing native/layout text, rendered pages, page manifests, source maps, and document records were used only to locate and transcribe evidence. The reused-evidence inventory recorded 52 eligible assets: 39 usable, 8 partial, 2 stale, and 3 duplicate. No OCR, workbook, CSV, DOC/DOCX, or structured-data source was supplied.

The complete direct-source inventory and provenance are recorded in [source_inventory.md](review_1_5_3/source_inventory.md) and [evidence_asset_inventory.md](review_1_5_3/evidence_asset_inventory.md). Pre-review source and reused-artifact hashes are retained in [source_hashes_before.sha256](review_1_5_3/source_hashes_before.sha256) and [reused_artifact_hashes_before.sha256](review_1_5_3/reused_artifact_hashes_before.sha256).

## Scope, Complete Coverage, and Exclusions

| Source | Supplied file | Total pages | Reusable-backed | Fresh-required | Mapped | Status |
|---|---|---:|---:|---:|---:|---|
| D001 | [jama_graham_2024_oi_240078_1739900423.19074.pdf — PDF p. 1](<../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=1>) | 9 | 9 | 0 | 9 | COMPLETE |
| D002 | [joi240078supp1_prod_1739900423.22574.pdf — PDF p. 1](<../joi240078supp1_prod_1739900423.22574.pdf#page=1>) | 15 | 0 | 15 | 15 | COMPLETE |
| D003 | [joi240078supp2_prod_1739900423.24574.pdf — PDF p. 1](<../joi240078supp2_prod_1739900423.24574.pdf#page=1>) | 16 | 13 | 3 | 16 | COMPLETE |
| **Package** | **Three supplied PDFs** | **40** | **22** | **18** | **40** | **COMPLETE** |

Every source page was mapped. D002 pp. 1-15 and D003 pp. 2-3 and 16 received fresh direct-source extraction; all remaining pages were reusable-backed and source-checked where needed. The review excluded web and external-literature searches, broad methodology or clinical audits, and unsupported reconstruction of unreported analyses. No candidate cap, review queue, top-N subset, or deferred-by-cap category was used.

## Quantitative and Statistical Relationship Coverage

The numeric relationship inventory contains N001-N056. Every item was assigned to the numeric-consistency review; N052 generated C002. The full descriptions and source locations are in [numeric_relationship_inventory.md](review_1_5_3/relationships/numeric_relationship_inventory.md) and [numeric_consistency.md](review_1_5_3/checkers/numeric_consistency.md).

| Numeric IDs | Coverage and provenance | Completion |
|---|---|---|
| N001-N010 | D001 population, design, outcomes, programme schedule, planning, and analysis definitions | COMPLETE |
| N011-N020 | D001 Table 1 baseline counts, denominators, percentages, scales, labels, and missingness | COMPLETE |
| N021-N031 | D001 flow, response, main cessation results, comparator, moderation, and CTP relationships | COMPLETE |
| N032-N040 | D001 Table 3, participant-flow, narrative, and result-label relationships | COMPLETE |
| N041-N045 | D002 protocol and D003 supplement definitions, planned/final mappings, and sensitivity context | COMPLETE |
| N046-N051 | D003 eAppendices/eTables 3 and 5 outcomes, arithmetic, denominators, and labels | COMPLETE |
| N052 | D003 eTable 4 summary-statistic label/display relationship; provenance for C002 | COMPLETE |
| N053-N056 | D003 eTable 4-6, response, moderator, and cross-source reporting relationships | COMPLETE |

The inferential inventory contains S001-S025. Statistical pass 1 and the independent pass 2 each marked every S ID complete. Pass 2 generated the subsequently rechecked C003 label observation; no P-value display-zero candidate was registered. The complete records are in [relationship_inventory.md](review_1_5_3/statistics/relationship_inventory.md), [statistical_pass_1.md](review_1_5_3/checkers/statistical_pass_1.md), and [statistical_pass_2.md](review_1_5_3/checkers/statistical_pass_2.md).

| Statistical IDs | Pass 1 | Pass 2 | Provenance |
|---|---|---|---|
| S001-S005 | PASS_1_COMPLETE | PASS_2_COMPLETE | Planning, analysis labels, follow-up, and primary/repeated PPA |
| S006-S010 | PASS_1_COMPLETE | PASS_2_COMPLETE | CCA/IPRW, moderation, and CTP/dual-abstinence results |
| S011-S015 | PASS_1_COMPLETE | PASS_2_COMPLETE | Subgroups, discussion, distinct protocol study, planned analysis, and missingness |
| S016-S020 | PASS_1_COMPLETE | PASS_2_COMPLETE | Mediation, MI, IPRW, and repeated outcome records |
| S021-S025 | PASS_1_COMPLETE | PASS_2_COMPLETE | Moderator definitions, MI grid, eTable 4-6 relationships |

## Candidate Index

| Stable ID | Candidate | Category | Status |
|---|---|---|---|
| [C001](#c001--quit-date-pre-message-duration-conflicts-between-the-main-article-and-both-support-documents) | Quit-date pre-message duration conflict | Cross-document numeric inconsistency | Pending Human Adjudication |
| [C002](#c002--etable-4-labels-motivation-and-confidence-as-median-iqr-but-prints-single-parenthetical-dispersion-values) | eTable 4 summary-label/display mismatch | Measure, label, or scale inconsistency | Pending Human Adjudication |
| [C003](#c003--eappendix-c-prints-ipwr-once-for-a-result-otherwise-defined-and-labelled-as-iprw) | `IPWR` versus `IPRW` method label | Measure, label, or scale inconsistency | Pending Human Adjudication |

## Candidate Evidence Cards

## C001 — Quit-date pre-message duration conflicts between the main article and both support documents

**Candidate statement:** The main article prints a 6-week pre-quit message period, whereas both supplied support documents print a 1-week pre-quit period for the same named intervention and quit-date subgroup. **Pending Human Adjudication.**

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_graham_2024_oi_240078_1739900423.19074.pdf — PDF p. 3](<../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=3>); [joi240078supp1_prod_1739900423.22574.pdf — PDF p. 2](<../joi240078supp1_prod_1739900423.22574.pdf#page=2>); [joi240078supp2_prod_1739900423.24574.pdf — PDF p. 2](<../joi240078supp2_prod_1739900423.24574.pdf#page=2>).

**Source evidence:** D001 states “6 weeks before and 8 weeks after”; D002 states “a week before and 8 weeks afterward”; D003 states “1 week preceding” and 8 weeks afterward.

**Reported-versus-comparator:** `6 weeks before` in D001 versus `1 week before` in D002 and D003, with the intervention name, quit-date subgroup, temporal anchor, and week unit matched. All three print an 8-week post-quit period.

**Reasoning procedure:** Matched descriptions of one intervention component require the same pre-quit duration unless a source supplies a version, effective-date, subgroup, or other scope qualifier.

**Calculation:** `6 weeks - 1 week = 5 weeks`; `6 weeks != 1 week`.

**Alternative source-grounded interpretations:** The texts may describe different programme versions, the support documents may be outdated, or one printed occurrence may be a production discrepancy. The supplied documents do not establish which explanation applies or which schedule trial participants received.

**Mechanical evidence recheck:** All three cited locations and printed durations were found and matched. Required comparison inputs are available; missing inputs are trial-period delivery specifications, delivery logs, version history, and editorial source files. Direct observation is the unequal printed duration; any version or production explanation remains inferred. See [evidence_recheck.md](review_1_5_3/verification/evidence_recheck.md).

**Quality-control relevance:** A reader or implementation reviewer could extract conflicting intervention exposure durations from the supplied documents.

**Potential downstream evidence impact:** If confirmed, a systematic-review extractor, intervention-description review, or guideline evidence table could copy the wrong pre-quit duration. This does not establish propagation or a changed trial conclusion.

**Human verification steps:** Inspect trial-period delivery specifications, version history, participant message logs, and editorial source files; determine whether documents describe different releases; then reconcile the duration or add version/effective-date qualifiers.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — eTable 4 labels motivation and confidence as median (IQR) but prints single parenthetical dispersion values

**Candidate statement:** eTable 4 labels the motivation and confidence rows `median (IQR)` but prints one parenthetical number in each affected cell, unlike its own endpoint-form IQR convention. **Pending Human Adjudication.**

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi240078supp2_prod_1739900423.24574.pdf — PDF p. 12](<../joi240078supp2_prod_1739900423.24574.pdf#page=12>), eTable 4; [joi240078supp2_prod_1739900423.24574.pdf — PDF p. 13](<../joi240078supp2_prod_1739900423.24574.pdf#page=13>), scale footnote; [jama_graham_2024_oi_240078_1739900423.19074.pdf — PDF p. 4](<../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4>), Table 1 comparator.

**Source evidence:** eTable 4 prints motivation as `4.1 (0.8)` in both groups and confidence as `3.2 (1.1)` and `3.5 (1.1)` under `median (IQR)`. The same table prints other median-IQR rows as endpoint pairs, including `30.0 (27.0-30.0)` and `4.0 (3.0-5.0)`.

**Reported-versus-comparator:** A `median (IQR)` label with one parenthetical value versus the same table's `median (IQR)` rows with two hyphen-separated endpoint values. D001 Table 1 also uses endpoint-form IQRs for the same measures.

**Reasoning procedure:** Under the source's own displayed convention, an IQR is shown as `Q1-Q3`; the affected cells contain a single value with no note defining a different convention.

**Calculation:** The comparator format has two values inside parentheses; each affected cell has one. Rounding cannot create two unprinted endpoints from one displayed value.

**Alternative source-grounded interpretations:** The cells may be means (SDs), scalar IQR widths under an unstated convention, or medians with omitted endpoints. The supplied package does not define the intended convention or provide analysis output to resolve it.

**Mechanical evidence recheck:** Cited cells, internal comparators, the Table 1 comparator, and the 1-to-5 scale footnote were found and matched. The comparison is reproducible from printed display arity. Missing inputs include Q1/Q3 values, participant-level data, table-production specifications, and any note defining scalar IQRs. See [evidence_recheck.md](review_1_5_3/verification/evidence_recheck.md).

**Quality-control relevance:** The label/display mismatch can cause a data extractor to encode the wrong summary-statistic type.

**Potential downstream evidence impact:** If confirmed, a meta-analysis table, systematic-review dataset, or guideline evidence profile could copy a median/IQR versus mean/SD classification incorrectly. This does not establish an error in treatment-effect estimates or a changed conclusion.

**Human verification steps:** Compare analysis output and the table-production file with the manuscript labels; establish the intended statistic, convention, and group values for the motivation and confidence rows.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — eAppendix C prints IPWR once for a result otherwise defined and labelled as IPRW

**Candidate statement:** eAppendix C prints `IPWR` once beside the repeated-PPA result even though the same source defines and otherwise uses `IPRW`, and the matched eTable labels the result `IPRW`. **Pending Human Adjudication.**

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi240078supp2_prod_1739900423.24574.pdf — PDF p. 5](<../joi240078supp2_prod_1739900423.24574.pdf#page=5>), eAppendix C; [joi240078supp2_prod_1739900423.24574.pdf — PDF p. 14](<../joi240078supp2_prod_1739900423.24574.pdf#page=14>), eTable 5; [jama_graham_2024_oi_240078_1739900423.19074.pdf — PDF p. 4](<../jama_graham_2024_oi_240078_1739900423.19074.pdf#page=4>), Statistical Methods.

**Source evidence:** D003 p. 5 defines `IPRW` as inverse probability of retention weighting and otherwise uses `IPRW`, but its repeated-PPA sentence prints `IPWR` with RR 2.21 (95% CI 1.67-2.93). D003 p. 14 and D001 p. 4 label the matching analysis `IPRW`.

**Reported-versus-comparator:** Undefined `IPWR` versus the defined and repeatedly printed `IPRW` for the same weighted repeated-PPA result; the RR and confidence interval match.

**Reasoning procedure:** A method abbreviation attached to a result should agree with its explicit expansion and the label for the same matched analysis elsewhere in the supplied package.

**Calculation:** `IPWR != IPRW`; the matched-result anchors are `RR 2.21 = 2.21` and `1.67-2.93 = 1.67-2.93`.

**Alternative source-grounded interpretations:** `IPWR` could be an unstated second abbreviation, but no supplied source defines it and the identical eTable result is labelled `IPRW`. A typographical transposition is plausible but is not asserted as a correction.

**Mechanical evidence recheck:** The occurrence, explicit `IPRW` expansion, repeated `IPRW` uses, and matched eTable result were found and matched. The package does not provide an analysis-output label, production source, or change history to establish the intended editorial mechanism. See [evidence_recheck.md](review_1_5_3/verification/evidence_recheck.md) and [evidence_recheck_C003.md](review_1_5_3/verification/evidence_recheck_C003.md).

**Quality-control relevance:** An undefined transposed abbreviation can create avoidable ambiguity about the weighted analysis used for the repeated-PPA result.

**Potential downstream evidence impact:** If confirmed, a methods summary, systematic-review extractor, or guideline evidence table could preserve an undefined method label. The numeric treatment-effect result is consistent across the supplied locations; this does not establish propagation or a changed conclusion.

**Human verification steps:** Compare the repeated-PPA analysis output and manuscript production file with eTable 5 and the defined method name; establish whether `IPWR` denotes the defined IPRW analysis or another documented analysis.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, the candidates could affect extraction of intervention duration, baseline summary-statistic type, or analysis-method naming. Such details are commonly copied into systematic reviews, meta-analyses, guidelines, and evidence tables. The supplied evidence does not show that copying occurred, that any conclusion changed, or that harm occurred.

## Limitations and Missing Definitions

The complete limitations record is in [limitations.md](review_1_5_3/limitations.md). The package lacks participant-level data, unrounded source values, intervention delivery logs, programme-version history, analysis-output labels, table-production files, and complete statistical test or variance definitions. These gaps prevent resolution of the three candidate explanations and limit exact inferential reconstruction, but do not prevent reproduction of the printed comparisons. Reusable assets are derivatives, not final authority; PDF source pages were used for candidate evidence. No web or external literature was used.

## Human Adjudication Checklist

1. Confirm the cited source text and comparator at every linked PDF page.
2. Obtain the missing primary documentation named in the relevant card.
3. Determine whether the differing text is version-specific, a defined alternative convention, or a reporting discrepancy.
4. Record decisions only in each card's five blank human adjudication fields.
5. If a correction is warranted, preserve the source, rationale, and version context; do not infer an effect on conclusions without supporting evidence.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

The routing preflight reports PASS, `INTERACTIVE_CLI`, coordinator inference PASS, and verification of all nine named role presets. Complete source coverage, source hashes, reused-artifact hashes, evidence maps, relationship inventories, checker outputs, rechecks, and the quality audit are preserved under [review_1_5_3](review_1_5_3/). Direct-source and reused-artifact hash comparisons were unchanged at the evidence-quality audit. The report itself has not altered any supplied source.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode |
|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN |
| main_quantitative_mapper | root/main_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN |
| support_quantitative_mapper | root/support_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN |
| numeric_consistency_reviewer | root/numeric_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN |
| cross_source_consistency_reviewer | root/cross_source_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN |
| statistics_pass_1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence_rechecker | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN |
| statistics_pass_2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence_recheck_append | root/evidence_recheck_c003 | gpt-5.6-sol | high | FRESH_SPAWN |
| quality_control_auditor | root/quality_control_auditor | gpt-5.6-sol | high | FRESH_SPAWN |
| report_generator | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN |

The authoritative execution manifest is [agent_execution_manifest.md](review_1_5_3/agent_execution_manifest.md).

### Performance

- **Target basis:** This package has three direct PDFs with 40 unique PDF-page units. Twenty-two units have readable, source-matched reusable native text, and 18 require fresh direct-source mapping (all 15 protocol pages plus results-supplement pages 2, 3, and 16). The package also has 13 rendered table/figure pages, 25 page-native-text files, two evidence maps, and document/page manifests; complete numeric and statistical mapping, two statistical passes, rechecking, and report generation remain required. These actual coverage, fresh-extraction, visual-table, and relationship-review burdens support the bounded target below.
- **Total source units:** 40
- **Fresh-source units:** 18
- **Target elapsed minutes:** 40-60
- **Started UTC:** 2026-08-19T04:35:22Z
- **Finished UTC:** 2026-08-19T05:05:14Z
- **Observed elapsed minutes:** 29.9
- **Target status:** MET_TARGET
- **Exceedance causes:** None

The four timing fields match [run_state.md](review_1_5_3/run_state.md); local rendering and validation occur outside the observed review duration.

### Token-Usage and Cost Metadata

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Cached input tokens | Cache-write tokens | Output tokens | Reasoning tokens | Total tokens | Known token cost (USD) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 |
| gpt-5.6-terra | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 |

Authoritative response-level runtime/API token counts were not exposed for any manifested agent in this interactive runtime, so the ledger records `UNAVAILABLE` with exact `__` token fields and the complete package count and price remain incomplete. The zero totals above are known subtotals, not estimates of actual usage. See [token_usage_summary.md](review_1_5_3/token_usage_summary.md) for per-agent detail. Cached input and cache-write counts are input subsets; reasoning is an output subset and is not added again to total tokens. Any available amount uses the bundled dated fixed-model rates and is a token-only estimate, not an invoice.
