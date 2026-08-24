# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication

This report records source-grounded quantitative reporting consistency candidates for human review. Every candidate below is **Pending Human Adjudication**. It makes no finding about validity, importance, correction, study quality, or the paper's conclusions.

## Executive Quality-Control Summary

Complete fresh source-first coverage identified **5** distinct candidate consistency issues (`C001`–`C005`). Two concern repeated adjusted estimates in the article, one concerns a supplement-table comparison label, and two concern planned-versus-reported definitions. Candidates were merged only when the printed values, comparator, and rule were the same. No top-N limit, queue, or early-stopping rule was used.

Small preventable reporting defects can matter when later data extractors, systematic reviews, meta-analyses, guidelines, or other evidence products copy a number or definition. The supplied package does not establish that any such reuse, propagation, conclusion change, or harm occurred.

## Package and Fresh-Processing Provenance

The direct package sources were four supplied, unencrypted PDFs: the 12-page main article, 32-page protocol, 9-page statistical analysis plan (SAP), and 27-page online supplement. All 80 direct PDF pages were fresh scientific mapping units; reusable direct-source units were zero. Fresh native and layout PDF text was produced for all four sources, with targeted source-page renderings for result displays.

The user-authorized existing OCR bundle was reused only for image-only Supplement 3 pages 3–16 after source-SHA matching. No CPU or GPU OCR was run. Native/layout text and source PDFs remained the principal evidence; renders and existing OCR were locator/inspection aids. Details are in [the evidence-asset inventory](review_1_5_2/evidence_asset_inventory.md) and [source coverage](review_1_5_2/source_coverage.md).

| Source | Direct units | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---|
| [Main article](../jama_huffman_2018_oi_170166.pdf#page=1) | 12 | 12 | 12 | COMPLETE |
| [Protocol](../joi170166supp1_prod.pdf#page=1) | 32 | 32 | 32 | COMPLETE |
| [SAP](../joi170166supp2_prod.pdf#page=1) | 9 | 9 | 9 | COMPLETE |
| [Online supplement](../joi170166supp3_prod.pdf#page=1) | 27 | 27 | 27 | COMPLETE |
| **Total** | **80** | **80** | **80** | **COMPLETE** |

## Scope, Complete Coverage, and Exclusions

The review covered result-relevant main and support content, including narrative results, tables, figures, captions, protocol/SAP definitions, eTables, and eFigures. It prioritized numerical, denominator, statistical, cross-document, measure-label/scale, and rate/count relationships. The complete allocation is recorded in [the coverage manifest](review_1_5_2/coverage_manifest.md).

Excluded from candidate discovery were broad methodology, clinical, novelty, misconduct, and raw-data audits. Analysis-unit or population questions qualified only where they generated a concrete reported-number, statistic, denominator, label, or interpretation inconsistency. Graphs without printed exact values were not reverse-engineered. No web or external literature was used.

## Quantitative and Statistical Relationship Coverage

The canonical numeric inventory contains 63 relationships: `N001`–`N035` and `N501`–`N528`. The canonical statistical inventory contains 63 relationships: `S001`–`S050` and `S501`–`S513`.

| Lane | Covered relationships | Completion |
|---|---:|---|
| Numeric/reporting checking | 63/63 N relationships | COMPLETE |
| Cross-source checking | 126/126 N/S relationships | COMPLETE |
| Independent statistical pass 1 | 63/63 S relationships | PASS_1_COMPLETE |
| Independent statistical pass 2 | 63/63 S relationships | PASS_2_COMPLETE |

Both statistical passes were separate fresh `gpt-5.6-terra` / high-effort executions. Pass 2 revisited all statistical relationships, the complete stable ledger, and the mechanical recheck; it added no distinct candidate. No supplied value was a `P = 0`/equivalent display-zero candidate; none of the five cards concerns display-zero notation.

## Candidate Index

| ID | Candidate | Category | Linked relationships |
|---|---|---|---|
| [C001](#c001--in-hospital-beta-blocker-adjusted-risk-difference-ci-endpoint-mismatch) | In-hospital beta-blocker adjusted-risk-difference CI endpoint mismatch | Cross-document numeric inconsistency | N024; S008 |
| [C002](#c002--discharge-beta-blocker-adjusted-point-estimates-mismatch) | Discharge beta-blocker adjusted point estimates mismatch | Cross-document numeric inconsistency | S021 |
| [C003](#c003--etable-1-difference-footnote-conflicts-with-the-displayed-comparison-groups) | eTable 1 difference footnote conflicts with the displayed comparison groups | Measure, label, or scale inconsistency | N517; S507 |
| [C004](#c004--sap-and-article-use-different-component-sets-under-the-same-outcome-name) | SAP and article use different component sets under the same outcome name | Measure, label, or scale inconsistency | N026; N027; S032 |
| [C005](#c005--published-prespecified-age-strata-do-not-match-the-supplied-sap) | Published prespecified age strata do not match the supplied SAP | Measure, label, or scale inconsistency | S505; S037–S039 |

## Candidate Evidence Cards

## C001 — In-hospital beta-blocker adjusted-risk-difference CI endpoint mismatch

**Candidate statement:** The main article prints two different upper 95% confidence-interval endpoints for the same in-hospital beta-blocker adjusted risk difference.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Main article Table 2 — PDF p. 6](../jama_huffman_2018_oi_170166.pdf#page=6); [main article Results narrative — PDF p. 7](../jama_huffman_2018_oi_170166.pdf#page=7).

**Source evidence:** Table 2 prints adjusted risk difference `6.25 (4.10 to 8.40)` and OR `1.46 (1.29-1.65)`. The matched narrative prints `6.25% [95% CI, 4.10%-8.10%]` and OR `1.46 [95% CI, 1.29-1.65]`.

**Reported-versus-comparator:** The same named in-hospital beta-blocker outcome, intervention-control contrast, adjusted risk-difference point estimate and lower endpoint, plus the same OR and OR interval, are paired with upper endpoints `8.40` and `8.10`.

**Reasoning procedure:** Directly compare the two printed occurrences after matching outcome, contrast, adjusted-result context, point estimate, lower endpoint, and OR. A difference in an upper endpoint at the printed two-decimal precision requires a source-identified distinct analysis to be treated as a separate result; neither location identifies one.

**Calculation:** `8.40 - 8.10 = 0.30` percentage points.

**Alternative source-grounded interpretations:** One occurrence may contain a transcription/typesetting error, or an unstated distinct analysis may exist. The supplied locations do not name a different population, adjustment set, time point, or estimand.

**Mechanical evidence recheck:** The exact locations and values were reproduced in [the mechanical recheck](review_1_5_2/verification/evidence_recheck.md). Direct observation is the two printed endpoints; any production explanation is inferred.

**Quality-control relevance:** This is a repeated adjusted-result consistency check (N024; S008), not a re-estimation of the model.

**Potential downstream evidence impact:** If confirmed, an extractor could copy either `8.40%` or `8.10%` as the upper confidence endpoint for the same result. The package does not show downstream reuse or a conclusion change.

**Human verification steps:** Consult finalized fitted-model output or a versioned analysis export and establish which upper endpoint applies to the intended in-hospital beta-blocker analysis.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Discharge beta-blocker adjusted point estimates mismatch

**Candidate statement:** The main article's Table 2 and matched narrative print different adjusted risk-difference and odds-ratio point estimates for discharge beta-blocker use while printing identical interval endpoints.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Main article Table 2 — PDF p. 6](../jama_huffman_2018_oi_170166.pdf#page=6); [main article Results narrative — PDF p. 7](../jama_huffman_2018_oi_170166.pdf#page=7).

**Source evidence:** Table 2 prints adjusted difference `6.69 (4.43 to 8.95)` and OR `1.48 (1.30-1.68)`. The narrative prints `6.63% [4.43%-8.95%]` and OR `1.47 [1.30-1.68]`.

**Reported-versus-comparator:** Matched outcome, contrast, adjusted analysis description, and both risk-difference and OR interval endpoints agree; the printed RD differs by `0.06` percentage points and the printed OR by `0.01`.

**Reasoning procedure:** Compare repeated adjusted point estimates under the same printed result identity. The intervals are unchanged and no distinct population, model, time point, or estimand is printed.

**Calculation:** `6.69 - 6.63 = 0.06` percentage points; `1.48 - 1.47 = 0.01`. The narrative's rounded raw rates (`67%` and `65%`) are compatible with Table 2's `66.8%` and `65.3%` and do not resolve the adjusted-point-estimate mismatch.

**Alternative source-grounded interpretations:** Transcription, different internal rounding, or distinct analysis runs are possible. The supplied sources do not designate which point estimates are final.

**Mechanical evidence recheck:** [The mechanical recheck](review_1_5_2/verification/evidence_recheck.md) reproduced both printed pairs and their identical interval endpoints. The mismatch is direct; possible causes are inferred.

**Quality-control relevance:** This is a cross-document repeated-result check (S021), not an assertion that either model is invalid.

**Potential downstream evidence impact:** If confirmed, an extractor could copy nonmatching adjusted RD or OR point estimates for the same reported analysis. No downstream reuse or conclusion change is established.

**Human verification steps:** Compare the final discharge beta-blocker model output with the table and narrative, and determine whether both locations were intended to report one analysis.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — eTable 1 difference footnote conflicts with the displayed comparison groups

**Candidate statement:** Supplement 3 eTable 1 displays complete-follow-up and missing-follow-up groups, while its difference footnote names intervention minus control.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Supplement 3 eTable 1 — PDF p. 17](../joi170166supp3_prod.pdf#page=17); [main article missing-follow-up narrative — PDF p. 6](../jama_huffman_2018_oi_170166.pdf#page=6).

**Source evidence:** eTable 1 columns are `Complete Follow Up n=21,079` and `Missing Follow Up n=295`; footnote a says `Difference = intervention minus control`. The article separately identifies `21 079` with complete follow-up and `295` with incomplete outcome data.

**Reported-versus-comparator:** The table headers/title identify complete versus missing follow-up, whereas the footnote names intervention versus control—distinct package-defined partitions.

**Reasoning procedure:** Directly assess whether the footnote comparator names the groups printed in the table, then check the displayed arithmetic direction against the displayed columns.

**Calculation:** The examples follow missing minus complete: age `60.0 - 60.6 = -0.6`; male `71.2 - 75.8 = -4.6` percentage points; tobacco use `42.4 - 30.8 = 11.6` percentage points.

**Alternative source-grounded interpretations:** The footnote may have been carried over from an intervention-control table; alternatively, a header could be wrong. The title, group totals, article narrative, and printed arithmetic support the complete/missing interpretation.

**Mechanical evidence recheck:** [The mechanical recheck](review_1_5_2/verification/evidence_recheck.md) reproduced the columns, footnote, and three calculations. The label conflict is direct; its production mechanism is not established.

**Quality-control relevance:** This check concerns the definition and direction of a displayed comparison (N517; S507), not reconstruction of the table's confidence intervals.

**Potential downstream evidence impact:** If confirmed, an extractor could assign displayed differences to intervention-control rather than missing-complete groups. The package does not establish actual propagation or a paper-level conclusion change.

**Human verification steps:** Verify the intended comparison order using the underlying table output; confirm whether footnote a should identify missing follow-up minus complete follow-up.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — SAP and article use different component sets under the same outcome name

**Candidate statement:** The supplied SAP and article use the name “optimal in-hospital medication use” for different printed component sets.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [SAP secondary endpoint — PDF p. 5](../joi170166supp2_prod.pdf#page=5); [main article outcome definition — PDF p. 3](../jama_huffman_2018_oi_170166.pdf#page=3); [main article Table 3 footnote — PDF p. 7](../jama_huffman_2018_oi_170166.pdf#page=7).

**Source evidence:** The SAP specifies aspirin, ADP-receptor antagonist, heparin, statin, and beta blocker. The article directly defines aspirin, ADP-receptor antagonist, anticoagulant, and beta blocker; it expressly says predefined in-hospital statin use was not collected. Table 3 reports `3122 (31.7)` control and `3878 (35.8)` intervention under the four-component definition.

**Reported-versus-comparator:** A five-component planned composite is compared with a four-component reported composite under the same outcome name. The component `heparin` is also expressed as `anticoagulant` in the article, without a supplied source defining whether they are operationally coextensive.

**Reasoning procedure:** Compare the printed SAP and article component sets directly. The article's four-component definition and statin-data disclosure are direct observations; the absence of a supplied amendment or change-control record leaves the planned-to-reported linkage unresolved.

**Calculation:** Set comparison: SAP includes `{aspirin, ADP-receptor antagonist, heparin, statin, beta blocker}`; article includes `{aspirin, ADP-receptor antagonist, anticoagulant, beta blocker}`. Statin is absent from the reported set, and the article states it was not collected. The reported counts/percentages cannot reconstruct the planned composite without statin data.

**Alternative source-grounded interpretations:** The article may intentionally report an operational four-component composite and may adequately disclose it. A nonsupplied amendment may authorize the change. No supplied amendment/change-control record resolves the same-name/different-component-set relationship.

**Mechanical evidence recheck:** [The mechanical recheck](review_1_5_2/verification/evidence_recheck.md) confirmed every component-set statement and the Table 3 result. This candidate preserves CP-04 provenance and its links to N026, N027, and S032; it does not create a second candidate.

**Quality-control relevance:** This is a planned-versus-reported measure-definition observation. It does not state that the article failed to disclose its four-component definition and does not determine whether an amendment was required.

**Potential downstream evidence impact:** If confirmed, an extractor could combine a five-component planned composite and a four-component reported composite under one label. The package does not establish propagation or a conclusion change.

**Human verification steps:** Review dated amendments/change-control records, the finalized analysis specification, and the operational definitions of heparin and anticoagulant; determine whether the publication definition adequately distinguishes the reported composite.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Published prespecified age strata do not match the supplied SAP

**Candidate statement:** The SAP's printed age subgroup categories do not map one-to-one to the article's age strata displayed under “Prespecified Subgroups.”

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [SAP subgroup analyses — PDF p. 7](../joi170166supp2_prod.pdf#page=7); [main article Methods — PDF p. 3](../jama_huffman_2018_oi_170166.pdf#page=3); [main article Figure 3 — PDF p. 9](../jama_huffman_2018_oi_170166.pdf#page=9).

**Source evidence:** The SAP specifies `<65 years and >65 years`. Article Methods calls age a prespecified subgroup, and Figure 3 displays `<50`, `50-69`, and `≥70` years under `Prespecified Subgroups`.

**Reported-versus-comparator:** The two SAP categories split at 65; the three published strata split at 50 and 70. The published `50-69` stratum spans the SAP boundary and includes age 65, which the SAP's literal `<65`/`>65` wording does not assign.

**Reasoning procedure:** Compare exact printed cutpoints and the article's prespecified label. No inference from outcome values is needed; a mapping source or amendment would be required to reconcile the category definitions.

**Calculation:** Two categories (`<65`, `>65`) cannot map one-to-one to three categories (`<50`, `50-69`, `≥70`); specifically, `50-69` crosses the 65-year boundary.

**Alternative source-grounded interpretations:** A later amendment or separate prespecification may define the 50/70-year cutpoints. The article may use “prespecified” for the age variable broadly rather than exact cutpoints, but the supplied package does not state that convention.

**Mechanical evidence recheck:** [The mechanical recheck](review_1_5_2/verification/evidence_recheck.md) confirmed the SAP cutpoints, Methods language, Figure 3 title, and three displayed strata. The mismatch is direct; any amendment or intent is not supplied.

**Quality-control relevance:** This is a planned-versus-published category-definition check (S505; S037–S039), not a conclusion about subgroup validity or clinical effect.

**Potential downstream evidence impact:** If confirmed, an extractor could record the 50/70-year strata as matching the supplied prespecified categories. The package does not show actual propagation or conclusion change.

**Human verification steps:** Obtain dated prespecification/amendment records, establish the intended treatment of age 65, and determine whether the article's displayed cutpoints were prespecified.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If a candidate is confirmed, a downstream user could copy the affected confidence-limit endpoint, adjusted point estimate, comparison label, composite definition, or subgroup definition into an evidence table or later evidence product. This is a bounded extraction concern only. The supplied sources do not document any downstream reuse, propagation, conclusion change, or harm.

## Limitations and Missing Definitions

- The package does not provide raw data, finalized model exports, unrounded effects, complete variance/test inputs, analysis code, or amendment/change-control records.
- No numerical values were inferred from graphs lacking printed point labels.
- The user required reuse of existing OCR rather than renewed OCR. The matched OCR aid was limited to Supplement 3 image-only toolkit pages and did not itself establish trial-result values.
- Fresh Poppler extraction used a locally extracted runtime because Poppler was absent from the base PATH; this was a tooling limitation, not a source change.
- This report is a consistency-review aid and does not adjudicate any candidate.

## Human Adjudication Checklist

For each candidate, retain the linked evidence, inspect the supplied PDF locations, obtain the named missing record where applicable, determine whether the printed comparison is intended, document the decision in the card's blank fields, and preserve the stable ID. Do not treat the report as a severity ranking or an automatic correction list.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

- **Profile:** 1.5.2
- **Target basis:** Four supplied PDFs totaling 80 pages: a 12-page main article, two text-rich support PDFs totaling 41 pages, and a 27-page support PDF with 14 source-hash-matched existing OCR pages. Fresh scientific mapping is required for all 80 pages; no new OCR is permitted by the user. Scope is smaller than the 102-page calibration package but includes multi-document tables and two independent statistical passes.
- **Total source units:** 80
- **Fresh-source units:** 80
- **Source-hash status:** Source hashes were recorded before fresh processing; final recomputation is recorded in the versioned review artifacts.
- **Source inventory:** [source_inventory.md](review_1_5_2/source_inventory.md)
- **Evidence assets:** [evidence_asset_inventory.md](review_1_5_2/evidence_asset_inventory.md)
- **Coverage manifest:** [coverage_manifest.md](review_1_5_2/coverage_manifest.md)
- **Final source-hash recomputation:** [source_hashes_after.sha256](review_1_5_2/source_hashes_after.sha256); all four hashes are unchanged from the pre-processing inventory.

### Agent execution

All actual review agents and their model, effort, start mode, and primary artifact are recorded in [agent_execution_manifest.md](review_1_5_2/agent_execution_manifest.md). This includes the coordinator; fresh preprocessing; main and support mapping; numeric and cross-source checking; independent statistical passes 1 and 2; evidence recheck; evidence-quality audit; and report generation.

| Stage | Runtime agent | Model | Effort | Start mode |
|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION |
| fresh_source_preprocessor | root/fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN |
| main_quantitative_mapper | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN |
| support_quantitative_mapper | root/support_mapper | gpt-5.6-terra | medium | FRESH_SPAWN |
| numeric_consistency | root/numeric_checker | gpt-5.6-terra | medium | FRESH_SPAWN |
| cross_source_consistency | root/cross_source_checker | gpt-5.6-terra | medium | FRESH_SPAWN |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence_recheck | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN |
| evidence_quality | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN |
| report_generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN |

### Reproducibility performance

- **Started UTC:** 2026-08-24T00:26:03Z
- **Finished UTC:** 2026-08-24T01:03:39Z
- **Observed elapsed minutes:** 37.6
- **Target elapsed minutes:** 30-45
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost metadata

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

Token amounts are token-only API-equivalent estimates under the dated price snapshot, not an invoice. Cached input and cache-write counts are input subsets; reasoning is an output subset and is not added again to total tokens. Per-agent accounting detail is in [token_usage_summary.md](review_1_5_2/token_usage_summary.md).

| Model | Known input tokens | Known output tokens | Known total tokens | Known token-only API-equivalent cost (USD) |
|---|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 |

These zeros are known subtotals only, not evidence of zero model usage. Authoritative response-level counts were unavailable for all 11 runtime agents, so the complete token count and complete token-only price remain unavailable.
