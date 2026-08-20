# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication

All eight candidate consistency issues in this report are **Pending Human Adjudication**. This is a quantitative reporting quality-control review, not a finding that any candidate is valid, that a correction is required, or that the paper's conclusions changed.

## Executive Quality-Control Summary

Complete uncapped review of the supplied package registered **8** stable candidates: C001, C002, C003, C004, C005, C006, C007, and C008. The review covered numeric, denominator, statistical, cross-document, and measure/scale relationships. Small preventable reporting defects can matter for downstream evidence extraction if confirmed; this review does not claim that any defect propagated, changed a conclusion, or caused harm.

## Package and Reused-Evidence Provenance

The package contains six direct PDF sources: the main article, three result-relevant supplements, a collaborator roster, and a data-sharing statement. Direct-source identity and pre-review hashes are recorded in [source inventory](review_1_5_3/source_inventory.md) and [source hashes](review_1_5_3/source_hashes_before.sha256). Reused native text, page maps, rendered pages, and related derivatives were inventoried and hashed before use in [evidence asset inventory](review_1_5_3/evidence_asset_inventory.md) and [reused-artifact hashes](review_1_5_3/reused_artifact_hashes_before.sha256).

Reusable artifacts were used only to locate and transcribe evidence. Candidate evidence was checked against the cited direct source pages.

## Scope, Complete Coverage, and Exclusions

The complete direct-source scope was 404 physical PDF pages: 38 reusable-backed and 366 fresh-required pages, with 404 mapped pages. Each source row closes in [source coverage](review_1_5_3/source_coverage.md): DOC-001 12/12, DOC-002 229/229, DOC-003 130/130, DOC-004 26/26, DOC-005 6/6, and DOC-006 1/1. The assignment and artifact partition are recorded in [coverage manifest](review_1_5_3/coverage_manifest.md).

The review was limited to reproducible quantitative reporting consistency: displayed counts, denominators, arithmetic, estimates, intervals, P values where compatible rules were supplied, labels, scales, rates, and matched cross-document values. It did not perform a broad clinical, methodological, novelty, misconduct, raw-data, or external-literature audit. Coherent display-zero P values were not registered as candidates; no card here concerns such a value.

## Quantitative and Statistical Relationship Coverage

The quantitative inventory contains N001–N056 (56 relationships); numeric and cross-source checks covered their complete mapped scope. The statistical inventory contains S001–S065 (65 relationships). Statistical pass 1 and the independent statistical pass 2 both recorded every S relationship as complete, including relationships without a candidate. The pass-2 reconciliation retained C001–C008 and added no candidate. See [numeric relationship inventory](review_1_5_3/relationships/numeric_relationship_inventory.md), [statistical relationship inventory](review_1_5_3/statistics/relationship_inventory.md), [statistical pass 1](review_1_5_3/checkers/statistical_pass_1.md), and [statistical pass 2](review_1_5_3/checkers/statistical_pass_2.md).

## Candidate Index

| ID | Candidate statement | Category |
|---|---|---|
| C001 | Shared-placebo race missingness does not reconcile with the printed denominator | Denominator, proportion, or total inconsistency |
| C002 | SVC values have incompatible monthly-rate and 24-week-change labels | Measure, label, or scale inconsistency |
| C003 | Shared-placebo ALSFRS-R credible-interval endpoints differ for the cited primary model | Cross-document numeric inconsistency |
| C004 | Pooled-active ALSFRS-R credible-interval endpoints differ for the cited primary model | Cross-document numeric inconsistency |
| C005 | Bayesian mortality event rates differ between article text and cited eTable 2 | Cross-document numeric inconsistency |
| C006 | Plasma NfL confidence intervals differ across Figure 3, narrative, and eTable 3B | Cross-document numeric inconsistency |
| C007 | Serum NfL regimen-only values and contrast differ across displays | Cross-document numeric inconsistency |
| C008 | Discussion total of 13 events conflicts with the 14 events displayed in Table 2 | Denominator, proportion, or total inconsistency |

## Candidate Evidence Cards

## C001 — Shared-placebo race missingness does not reconcile with the printed denominator

**Status:** Pending Human Adjudication

**Candidate statement:** The displayed shared-placebo race accounting has a one-participant mismatch.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_berry_2025_oi_240158_1742927563.7361.pdf — Table 1 and footnote b, PDF p. 6](<../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=6>)

**Source evidence:** Shared placebo is `n=164`; the race rows are Asian `2/160`, Black or African American `6/160`, White `151/160`, and multiple races `1/160`. Footnote b says race was unknown or unreported for 3 participants.

**Reported-versus-comparator:** The printed group total is 164 and the printed race denominator/category sum is 160, whereas the footnote reports 3 unknown or unreported participants.

**Reasoning procedure:** Compare the displayed group total, the common race denominator, the exhaustive displayed race-row numerator sum, and the footnote count without applying a rounding tolerance to counts.

**Calculation:** `2 + 6 + 151 + 1 = 160`; `164 - 160 = 4`; `4 - 3 = 1`.

**Alternative source-grounded interpretations:** The denominator may be a complete-case subset excluding one additional status, or a numerator, denominator, or footnote may be printed incorrectly; the table gives no separate subset definition.

**Mechanical evidence recheck:** Location and printed values were found and matched; the accounting calculation reproduced. Necessary values are present. The missing definition is whether an additional race status was deliberately excluded. Direct observation is the one-person mismatch; its cause is not inferred.

**Quality-control relevance:** This is a displayed baseline denominator/missingness accounting observation requiring human resolution.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy a baseline race denominator or missingness count inconsistently; no propagation or conclusion change is asserted.

**Human verification steps:** Check the participant-level race classification or table-production source, and determine whether a fourth unclassified status exists or whether one printed value requires correction.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — SVC values have incompatible monthly-rate and 24-week-change labels

**Status:** Pending Human Adjudication

**Candidate statement:** Identical SVC values are labelled as monthly rates in the article and as 24-week change estimates in eTable 3A.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [jama_berry_2025_oi_240158_1742927563.7361.pdf — Secondary Efficacy Outcomes, PDF p. 4](<../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>); [joi240158supp3_prod_1742927563.7911.pdf — eTable 3A, PDF p. 16](<../joi240158supp3_prod_1742927563.7911.pdf#page=16>)

**Source evidence:** The article calls `-9.32`, `-8.53`, and `-0.78` PPN per month over 24 weeks. eTable 3A presents the same values under `24-week Change Estimate` for SVC (% predicted).

**Reported-versus-comparator:** A monthly rate is printed in the article; a cumulative 24-week change label is printed for the same values in the cited table.

**Reasoning procedure:** Match population, endpoint, values, contrast, interval, and cited table; then compare the printed time-scale labels. No month-length conversion is used as evidence.

**Calculation:** The identical numeric triplet is `-9.32`, `-8.53`, and `-0.78` in both locations; the printed labels describe different scales and the supplied sources give no conversion or estimand definition that reconciles them.

**Alternative source-grounded interpretations:** `Per month` may be an editorial unit label, or the eTable heading may omit a rate convention. The supplied package does not select either interpretation.

**Mechanical evidence recheck:** Both locations and all values matched. The same population, outcome, contrast, and interval identify the comparison. The missing inputs are the fitted estimand and any time-scale convention. Direct observation is the conflicting label; intended usage is not inferred.

**Quality-control relevance:** Effect-scale labels guide quantitative extraction and should identify whether a value is a rate or a cumulative change.

**Potential downstream evidence impact:** If confirmed, a systematic review or data extractor could classify the same SVC result as a rate or as a 24-week change; no propagation or conclusion change is asserted.

**Human verification steps:** Review the model-output definition and table source to establish the intended SVC estimand and the label that should govern both displays.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Shared-placebo ALSFRS-R credible-interval endpoints differ for the cited primary model

**Status:** Pending Human Adjudication

**Candidate statement:** The shared-placebo ALSFRS-R interval endpoints differ between the article and its cited eTable 2.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_berry_2025_oi_240158_1742927563.7361.pdf — Primary Efficacy Outcome, PDF p. 4](<../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>); [joi240158supp3_prod_1742927563.7911.pdf — eTable 2, PDF p. 15](<../joi240158supp3_prod_1742927563.7911.pdf#page=15>)

**Source evidence:** The article gives shared-placebo slope `-1.03` with 95% CrI `-1.176 to -0.892`; eTable 2 gives `-1.03` with 95% CrI `(-1.181, -0.894)`.

**Reported-versus-comparator:** Matched Bayesian shared-parameter-model, group, endpoint, and unit labels accompany different three-decimal interval endpoints.

**Reasoning procedure:** Compare the two explicitly matched primary-model displays at their printed precision.

**Calculation:** Lower endpoints differ by `0.005`; upper endpoints differ by `0.002`; the point estimate is `-1.03` in both locations.

**Alternative source-grounded interpretations:** Different posterior runs, data locks, or production versions could exist, but neither source labels one.

**Mechanical evidence recheck:** Both locations, interval pairs, point estimate, group, unit, and model labels matched. The endpoint comparison reproduced. Missing inputs include posterior draws, unrounded quantiles, data-lock date, and model-run identifier. The difference is directly observed; its cause is not inferred.

**Quality-control relevance:** Repeated uncertainty endpoints for a named primary-model component should be traceable to one identified output.

**Potential downstream evidence impact:** If confirmed, an extractor could copy alternative credible-interval bounds for this component; no altered inference or conclusion is asserted.

**Human verification steps:** Compare the authoritative posterior output and production history to identify the intended interval and any labelled distinct run.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Pooled-active ALSFRS-R credible-interval endpoints differ for the cited primary model

**Status:** Pending Human Adjudication

**Candidate statement:** The pooled-active ALSFRS-R interval endpoints differ between the article and cited eTable 2.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_berry_2025_oi_240158_1742927563.7361.pdf — Primary Efficacy Outcome, PDF p. 4](<../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>); [joi240158supp3_prod_1742927563.7911.pdf — eTable 2, PDF p. 15](<../joi240158supp3_prod_1742927563.7911.pdf#page=15>)

**Source evidence:** The article gives pooled-active slope `-1.00` with 95% CrI `-1.153 to -0.858`; eTable 2 gives `-1.00` with 95% CrI `(-1.143, -0.847)`.

**Reported-versus-comparator:** The point estimate and named model match, while both printed interval endpoints differ.

**Reasoning procedure:** Compare matched primary-model component values at the displayed three-decimal precision.

**Calculation:** Lower endpoints differ by `0.010`; upper endpoints differ by `0.011`.

**Alternative source-grounded interpretations:** Separate posterior outputs or production versions may exist but are not identified on either supplied page.

**Mechanical evidence recheck:** The pages, values, component labels, and model match were confirmed and the comparison reproduced. Posterior run, data-lock, unrounded quantiles, and production history are missing. The printed mismatch is observed; no cause is assigned.

**Quality-control relevance:** A repeated model component needs an identifiable, reproducible uncertainty interval.

**Potential downstream evidence impact:** If confirmed, an extractor could copy different uncertainty endpoints for the pooled-active slope; no altered inference or conclusion is asserted.

**Human verification steps:** Check the primary-model posterior output and production record for the intended pooled-active interval.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Bayesian mortality event rates differ between article text and cited eTable 2

**Status:** Pending Human Adjudication

**Candidate statement:** Article and eTable 2 event rates differ for the matched Bayesian shared-parameter-model components.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_berry_2025_oi_240158_1742927563.7361.pdf — Primary Efficacy Outcome, PDF p. 4](<../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=4>); [joi240158supp3_prod_1742927563.7911.pdf — eTable 2, PDF p. 15](<../joi240158supp3_prod_1742927563.7911.pdf#page=15>)

**Source evidence:** The article gives shared placebo `0.007` and pooled active `0.006` events/month. eTable 2 gives `0.010` and `0.009` events/month for the same named model.

**Reported-versus-comparator:** Each matched group has a different three-decimal displayed mortality event rate.

**Reasoning procedure:** Compare group-specific values for the explicitly matched model, outcome unit, and components.

**Calculation:** `0.010 - 0.007 = 0.003` events/month for shared placebo; `0.009 - 0.006 = 0.003` events/month for pooled active. Values differing by `0.003` cannot be the same value rounded to three decimals.

**Alternative source-grounded interpretations:** One display may use an unlabelled event definition, posterior summary, or model run.

**Mechanical evidence recheck:** Both values and model labels were confirmed; the differences reproduced. The exact event variable, posterior summary, run identifier, and mapping to any death/PAV definition are missing. The value differences are direct observations; an explanation is not assigned.

**Quality-control relevance:** Event-rate values and their units should be consistent across matched model displays.

**Potential downstream evidence impact:** If confirmed, a reviewer could extract alternative mortality event rates; no conclusion change or downstream use is asserted.

**Human verification steps:** Inspect the model-output tables and event-definition metadata to determine whether these are distinct analyses and which rates are intended.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Plasma NfL confidence intervals differ across Figure 3, narrative, and eTable 3B

**Status:** Pending Human Adjudication

**Candidate statement:** The repeated plasma-NfL result has differing printed confidence-interval endpoints across three displays.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_berry_2025_oi_240158_1742927563.7361.pdf — Figure 3 and Biomarker Analyses, PDF p. 8](<../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>); [joi240158supp3_prod_1742927563.7911.pdf — eTable 3B, PDF p. 17](<../joi240158supp3_prod_1742927563.7911.pdf#page=17>)

**Source evidence:** Figure 3 gives `-9.5%` with CI `-17.8% to -0.5%`; nearby narrative gives `-17.8% to -0.4%`; eTable 3B gives `-18.0% to 0`. All print `-9.5%` and `P=.04`.

**Reported-versus-comparator:** The matched point estimate and P value are repeated with different printed interval endpoints.

**Reasoning procedure:** Match outcome, comparison, point estimate, and P value, then compare the printed interval bounds without reconstructing unrounded values or a null relation.

**Calculation:** Figure and narrative upper endpoints differ by `0.1` percentage point. eTable 3B prints a distinct endpoint pair, `-18.0% to 0`; its unrounded upper endpoint and rounding rule are unavailable.

**Alternative source-grounded interpretations:** Independent rounding from unprinted higher precision or an unlabelled model/output version may explain the displays.

**Mechanical evidence recheck:** Figure, narrative, and table were found and matched. The printed endpoint differences reproduced. Unrounded limits, interval method, table-specific rounding rule, and output version are absent. The printed mismatch is direct observation; no unrounded null relation is inferred.

**Quality-control relevance:** Repeated uncertainty bounds should remain traceable across figure, narrative, and table outputs.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy different confidence bounds for the plasma-NfL result; no changed significance determination, conclusion change, or propagation is asserted.

**Human verification steps:** Retrieve the authoritative unrounded interval output and document whether any display uses a separately labelled analysis or rounding rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Serum NfL regimen-only values and contrast differ across displays

**Status:** Pending Human Adjudication

**Candidate statement:** Matched article and eTable 3B serum-NfL displays report different placebo changes, contrasts, and interval endpoints.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_berry_2025_oi_240158_1742927563.7361.pdf — Figure 3 and Biomarker Analyses, PDF p. 8](<../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=8>); [joi240158supp3_prod_1742927563.7911.pdf — eTable 3B, PDF p. 17](<../joi240158supp3_prod_1742927563.7911.pdf#page=17>)

**Source evidence:** Article: placebo `+30.8%`, active `+0.4%`, difference `-23.2%` (95% CI `-39.5% to -2.5%`; `P=.03`). eTable: placebo `+26.8%`, active `+0.4%`, difference `-26.4%` (95% CI `-50.3% to -2.6%`; `P=.03`).

**Reported-versus-comparator:** The active change and P value agree, but placebo changes differ by 4.0 percentage points, treatment contrasts differ by 3.2 points, and both interval endpoints differ.

**Reasoning procedure:** Compare the matched regimen-placebo, pooled-active serum-NfL values across displays. Do not impose crude subtraction on a fitted back-transformed geometric-mean-ratio contrast.

**Calculation:** `30.8 - 26.8 = 4.0`; `|-23.2 - (-26.4)| = 3.2`. The article's contrast is compatible with the displayed-value diagnostic `[(1.004 / 1.308) - 1] x 100 = -23.24%`, so this is not an internal crude-subtraction claim.

**Alternative source-grounded interpretations:** An unlabelled ERO model, population, plate rule, data cut, or fitted-contrast definition could differ between displays.

**Mechanical evidence recheck:** Both pages and all displayed values matched; cross-display differences reproduced. The sources state log-scale modelling/back transformation but do not supply the exact fitted-contrast definition, model run, or population mapping. Differences are direct observations; their cause is not inferred.

**Quality-control relevance:** Matched biomarker arm changes, contrasts, and intervals should identify the same model output or a clearly labelled distinct analysis.

**Potential downstream evidence impact:** If confirmed, a systematic review or data extractor could copy different serum-NfL effect and interval values; no paper-level conclusion change or propagation is asserted.

**Human verification steps:** Compare the ERO model output, participant set, plate handling, and back-transformed contrast definition to determine whether the displays are intentionally distinct.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Discussion total of 13 events conflicts with the 14 events displayed in Table 2

**Status:** Pending Human Adjudication

**Candidate statement:** The Discussion's 13-event total does not match the 14 events obtained from the cited Table 2 group numerators if the endpoint and cutoff are the same.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_berry_2025_oi_240158_1742927563.7361.pdf — Table 2, PDF p. 7](<../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=7>); [jama_berry_2025_oi_240158_1742927563.7361.pdf — Discussion, PDF p. 9](<../jama_berry_2025_oi_240158_1742927563.7361.pdf#page=9>)

**Source evidence:** Table 2 reports `5/120` pooled-active and `9/162` shared-placebo death/PAV events. The Discussion reports 13 RCT-period events in those groups.

**Reported-versus-comparator:** Table 2's two printed numerators total 14, while the Discussion prints 13.

**Reasoning procedure:** Add the displayed Table 2 event numerators, conditional on the Discussion using the same event definition and cutoff.

**Calculation:** `5 + 9 = 14`, not 13.

**Alternative source-grounded interpretations:** The Discussion may use a narrower event definition, a different cutoff, or an unstated exclusion rather than Table 2's death-or-PAV endpoint.

**Mechanical evidence recheck:** The Table 2 and Discussion locations, values, and arithmetic were confirmed. The needed unresolved input is whether `events` in the Discussion means the same death/PAV endpoint and cutoff. The one-event difference is direct observation conditional on that match; its cause is not inferred.

**Quality-control relevance:** Event totals should identify their endpoint and cutoff sufficiently to reconcile with the supporting table.

**Potential downstream evidence impact:** If confirmed as the same endpoint and cutoff, an extractor could copy a total differing by one event; no conclusion change or propagation is asserted.

**Human verification steps:** Verify the RCT-period event list, endpoint definition, and cutoff for the Discussion sentence against Table 2.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, the observations could affect which denominator, time scale, uncertainty interval, rate, biomarker estimate, or event total a downstream data extractor records. Systematic reviews, meta-analyses, and guidelines should use their usual source verification and adjudication procedures. This review does not claim that any value was propagated, that any evidence synthesis was affected, or that the study's conclusions changed.

## Limitations and Missing Definitions

See the durable [limitations record](review_1_5_3/limitations.md). The package lacks participant-level data and several analysis-output definitions needed to resolve the candidate questions, including model-run identifiers, unrounded outputs, and some endpoint/estimand mappings. These limitations do not reduce the completed 404-unit source coverage or the direct-page confirmation of the printed values.

## Human Adjudication Checklist

1. Confirm every cited printed value against the direct PDF page.
2. Obtain authoritative source outputs or production records for the relevant model, table, and figure displays.
3. Resolve each stated missing definition before selecting an explanation or corrective action.
4. Record validity, importance, action, initials, and notes in each card's blank fields.
5. Preserve the stable IDs when documenting any later human decision.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

- **Routing preflight:** PASS; see [routing preflight](review_1_5_3/routing_preflight.md).
- **Coordinator inference:** PASS
- **Execution mode:** INTERACTIVE_CLI
- **Direct-source units:** 404
- **Reusable-backed units:** 38
- **Fresh-required units:** 366
- **Mapped units:** 404
- **Source integrity:** Before/after source and reused-artifact hashes are retained in the versioned review artifacts; coordinator finalization verifies equality.

### Agent execution

The current execution manifest is [agent_execution_manifest.md](review_1_5_3/agent_execution_manifest.md). It records the coordinator and each fresh specialist stage, including distinct Terra/high statistical passes and Sol/high evidence recheck and quality audit. The coordinator appends this report-generator runtime entry and completes the manifest after this report is assembled.

### Performance

- **Target basis:** Six supplied PDFs contain 404 stable PDF-page units. Only 38 pages have usable source-matched reusable native text, leaving 366 pages for fresh direct-source mapping across a 229-page protocol, a 130-page statistical analysis plan, and two administrative supplements. There are no Office/workbook/CSV sources; 16 retained renders reduce visual-table confirmation work for the main article and results supplement. The required main/support mapping, three first-pass checker lanes, a separate second statistical pass, recheck, quality audit, and report assembly set a bounded package-specific target.
- **Total source units:** 404
- **Fresh-source units:** 366
- **Target elapsed minutes:** 105-165
- **Started UTC:** 2026-08-19T05:21:29Z
- **Finished UTC:** 2026-08-19T05:51:19Z
- **Observed elapsed minutes:** 29.8
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Known token cost (USD) |
|---|---:|---:|---:|---:|
| gpt-5.6-sol | 0 | 0 | 0 | 0.000000 |
| gpt-5.6-terra | 0 | 0 | 0 | 0.000000 |

The runtime exposed no authoritative response-level token counts for any of the 17 manifested agents through the finished-UTC cutoff, so all ledger rows are explicitly `UNAVAILABLE`; the displayed zero tokens and zero known cost are the known subtotal only, not a complete package total. See [token_usage_summary.md](review_1_5_3/token_usage_summary.md) for per-agent detail. Cached-input and cache-write counts are input subsets and reasoning tokens are an output subset; they are not added again to total tokens. Any available amount uses the bundled pricing snapshot dated 2026-08-18 and is a token-only API-equivalent estimate, not an invoice.
