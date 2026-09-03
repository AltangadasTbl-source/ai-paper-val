# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication

**Every candidate in this report is Pending Human Adjudication.** This review identifies supplied-source quantitative reporting consistency questions; it does not determine validity, importance, action, or any correction, and it does not claim that a study conclusion changed.

## Executive Quality-Control Summary

Complete supplied-source coverage identified **7** distinct quantitative reporting quality-control candidates (C001-C007). The review mapped all 170 direct PDF pages, checked 117 numeric/reporting relationships and 34 inferential-statistical relationships in each of two independent statistical passes, and mechanically rechecked every stable candidate against direct source pages. Small preventable reporting defects can matter when data are extracted for downstream evidence products; this report does not assert that any defect propagated or caused harm.

## Package and Reused-Evidence Provenance

The package contains three supplied PDFs: [jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf](<../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=1>) (DOC-001, 11 pages), [joi250084supp1_prod_1765403089.61351.pdf](<../joi250084supp1_prod_1765403089.61351.pdf#page=1>) (DOC-002, 90 pages), and [joi250084supp2_prod_1765403089.61751.pdf](<../joi250084supp2_prod_1765403089.61751.pdf#page=1>) (DOC-003, 69 pages). Source identities and before-run SHA-256 values are recorded in [source_inventory.md](<review_1_5_1/source_inventory.md>) and [source_hashes_before.sha256](<review_1_5_1/source_hashes_before.sha256>).

Existing source-linked page assets were used only as locators and transcription or visual aids. The reusable-asset inventory hashed 127 eligible artifacts; 42 unique source pages had usable reusable extraction and 128 required fresh direct mapping. See [evidence_asset_inventory.md](<review_1_5_1/evidence_asset_inventory.md>) and [reused_artifact_hashes_before.sha256](<review_1_5_1/reused_artifact_hashes_before.sha256>).

## Scope, Complete Coverage, and Exclusions

| Source | Total pages | Reusable | Fresh-required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 main article | 11 | 11 | 0 | 11 | Complete |
| DOC-002 protocol/SAP | 90 | 0 | 90 | 90 | Complete |
| DOC-003 results supplement | 69 | 31 | 38 | 69 | Complete |
| **Total** | **170** | **42** | **128** | **170** | **Complete** |

Coverage assignments and canonical artifacts are recorded in [coverage_manifest.md](<review_1_5_1/coverage_manifest.md>) and [source_coverage.md](<review_1_5_1/source_coverage.md>). The review is confined to supplied-package numeric, denominator/proportion/total, inferential-statistical, cross-document numeric, measure-label/scale, and rate-versus-count consistency. It excludes broad methodology, clinical, raw-data, and external-literature audits.

## Quantitative and Statistical Relationship Coverage

All numeric/reporting relationships **N001-N117** were mapped and checked; the canonical register is [numeric_relationship_inventory.md](<review_1_5_1/relationships/numeric_relationship_inventory.md>) and the complete check record is [numeric_consistency.md](<review_1_5_1/checkers/numeric_consistency.md>). Cross-source consistency covered N001-N117 and S001-S034 in [cross_source_consistency.md](<review_1_5_1/checkers/cross_source_consistency.md>).

Both independent statistical passes completed **S001-S034**. Pass 1 is recorded in [statistical_pass_1.md](<review_1_5_1/checkers/statistical_pass_1.md>) (`PASS_1_COMPLETE`); pass 2 is recorded in [statistical_pass_2.md](<review_1_5_1/checkers/statistical_pass_2.md>) (`PASS_2_COMPLETE`). One-sided 95% confidence intervals/bounds, including the protocol wording on [DOC-002 PDF p. 37](<../joi250084supp1_prod_1765403089.61351.pdf#page=37>), were treated as one-sided, not two-sided. No candidate was registered solely for a finite-precision display-zero P value.

## Candidate Index

| ID | Candidate | Category | Relationship provenance |
|---|---|---|---|
| C001 | Protocol and reported primary endpoint differ on diabetes-range A1C failure condition | Cross-document numeric inconsistency | N002, N038, N087; S001, S008-S010 |
| C002 | 312 listed 12-month A1C measurements versus 313 participants with A1C available | Denominator, proportion, or total inconsistency | N006, N069, N102 |
| C003 | Figure 3 labels BMI values in kg/m² as weight | Measure, label, or scale inconsistency | N025 |
| C004 | Repeated age P value has unresolved comparator scope | Cross-document numeric inconsistency | N098-N101; S022, S024-S026 |
| C005 | eTable 7 pairs no statistically significant with p<0.05 | Statistical reporting inconsistency | N101; S026 |
| C006 | eTable 10b labels one comparison as both chi-squared and Wilcoxon rank-sum | Statistical reporting inconsistency | N085, N104; S018, S028 |
| C007 | MICE pooled percentages and printed risk difference have incompatible signs | Statistical reporting inconsistency | N110; S019, S031 |

## Candidate Evidence Cards

## C001 — Protocol and reported primary endpoint differ on the diabetes-range A1C failure condition

**Candidate statement:** The protocol's success rule is at least one of three components, while the reported/supplement rule adds a diabetes-range A1C failure condition that can override all components.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-002 protocol — PDF p. 15](<../joi250084supp1_prod_1765403089.61351.pdf#page=15>); [DOC-001 main article — PDF p. 4](<../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4>); [DOC-003 supplement — PDF p. 30](<../joi250084supp2_prod_1765403089.61751.pdf#page=30>) (explicit global-failure clause); [DOC-003 supplement — PDF p. 56](<../joi250084supp2_prod_1765403089.61751.pdf#page=56>) (15-participant table).

**Source evidence:** The protocol defines success by at least one of three thresholds. The main report includes maintaining A1C below 6.5% throughout; the supplement explicitly says A1C at or above 6.5% at 6 and/or 12 months marked a participant as failing regardless of body-weight or physical-activity improvement, and lists 15 participants.

**Reported-versus-comparator:** Protocol rule `A or B or C` versus reported/supplement rule `(A or B or C) and D`, where D means no diabetes-range A1C at the defined visits.

**Reasoning procedure:** Matched population, 12-month endpoint role, three component thresholds, and contrast, then compared whether the added global condition changes the binary classification rule.

**Calculation:** A participant meeting A, B, or C while not meeting D is classified differently. The supplied table identifies 15 D-false instances, but does not show their component achievement; no affected count is calculated.

**Alternative source-grounded interpretations:** A dated protocol amendment or final SAP revision, not supplied, may have prospectively adopted the rule. The main-article grammar could be read narrowly, but the supplement's explicit global clause supports the broader reading.

**Mechanical evidence recheck:** Direct-source recheck confirmed all four locations and distinguishes the p. 30 global clause from the p. 56 participant table; see [evidence_recheck.md](<review_1_5_1/verification/evidence_recheck.md>).

**Quality-control relevance:** A binary endpoint definition should identify any global override condition.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an incomplete endpoint definition or classification rule; no propagation or conclusion change is asserted.

**Human verification steps:** Obtain the dated governing amendment/final SAP and determine whether any of the 15 participants otherwise met a component.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — 312 listed 12-month A1C measurements versus 313 participants with A1C available

**Candidate statement:** Listed follow-up A1C device counts total 312, while matched missingness and complete-outcome reporting identify 313 participants with A1C available.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-003 supplement — PDF p. 8](<../joi250084supp2_prod_1765403089.61751.pdf#page=8>); [DOC-001 main article — PDF p. 4](<../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4>); [DOC-001 main article — PDF p. 5](<../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=5>); [DOC-003 supplement — PDF p. 50](<../joi250084supp2_prod_1765403089.61751.pdf#page=50>).

**Source evidence:** The method rows list Afinion 282, A1CNow+ 30, and serum 0. The report states 313 complete outcomes; eTable 8c gives 26 and 29 missing A1C observations among 368 and states no missing A1C among completers.

**Reported-versus-comparator:** The follow-up device-method total versus the independently derived A1C-available/completer total in the same randomized arms and time point.

**Reasoning procedure:** Treated device rows as integer observations and evaluated their reconciliation conditional on the unresolved premise that the displayed method rows are exhaustive.

**Calculation:** `282 + 30 + 0 = 312`; `368 - (26 + 29) = 313`; difference = 1. Baseline rows total `334 + 33 + 1 = 368`, supporting but not proving exhaustiveness.

**Alternative source-grounded interpretations:** One result may use an unlisted method (the narrative names Siemens DCA Vantage), or the displayed table may omit an observation without changing availability.

**Mechanical evidence recheck:** Direct pages confirmed counts, arm-specific missingness, and the no-missing-among-completers statement; see [evidence_recheck.md](<review_1_5_1/verification/evidence_recheck.md>).

**Quality-control relevance:** Outcome-ascertainment and denominator tables should reconcile or disclose an exception.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an incorrect A1C availability total or incomplete method breakdown; no outcome-estimate change is asserted.

**Human verification steps:** Reconcile participant-level A1C/device logs and identify the method for the unmatched observation.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Figure 3 labels BMI values in kg/m² as “weight”

**Candidate statement:** Figure 3 calls values in kg/m² “weight,” although the identical values are labelled BMI in Table 1.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-001 main article — PDF p. 8](<../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=8>); [DOC-001 main article — PDF p. 6](<../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=6>); [DOC-003 supplement — PDF p. 53](<../joi250084supp2_prod_1765403089.61751.pdf#page=53>).

**Source evidence:** Figure 3 prints AI `32.2 (28.2-35.9)` and human `32.5 (29.3-37.7)` kg/m² as baseline weight. Table 1 prints the identical triplets in its BMI row.

**Reported-versus-comparator:** Figure label/unit versus Table 1 measure label and exact arm-specific baseline values.

**Reasoning procedure:** Matched arm, time point, values, IQRs, and unit; then assessed whether measure labels agree with kg/m².

**Calculation:** All six displayed median/IQR values match exactly. No rounding tolerance or derived calculation is needed.

**Alternative source-grounded interpretations:** “Weight” may be shorthand or a carried-over figure label, but no literal weight-in-kilograms summary supports that interpretation.

**Mechanical evidence recheck:** Direct pages confirmed the Figure 3 wording, kg/m² unit, exact Table 1 match, and package BMI usage; see [evidence_recheck.md](<review_1_5_1/verification/evidence_recheck.md>).

**Quality-control relevance:** Measure labels and units should identify the same quantity.

**Potential downstream evidence impact:** If confirmed, a figure-data extractor could record BMI as body weight or assign the wrong unit; no treatment-effect change is asserted.

**Human verification steps:** Review the figure-production source and confirm whether the intended descriptor was BMI.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — eTables 5-7 leave the comparator scope of a repeated age P value ambiguous

**Candidate statement:** The same `p = 0.014` age statement appears beneath tables with different displayed contrasts without a clear comparator label.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-003 supplement — PDF p. 39](<../joi250084supp2_prod_1765403089.61751.pdf#page=39>); [DOC-003 supplement — PDF p. 43](<../joi250084supp2_prod_1765403089.61751.pdf#page=43>); [DOC-003 supplement — PDF p. 45](<../joi250084supp2_prod_1765403089.61751.pdf#page=45>); [DOC-003 supplement — PDF p. 47](<../joi250084supp2_prod_1765403089.61751.pdf#page=47>); [DOC-001 main article — PDF p. 6](<../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=6>).

**Source evidence:** eTables 3, 5, 6, and 7 repeat “Age differed between study groups (p = 0.014).” eTables 5-7 display site, baseline-A1C, and completion-status contrasts; eTable 5 separately gives site-age `p = 0.017`. eTable 3 has an overall randomized-cohort column, not treatment-arm columns.

**Reported-versus-comparator:** Repeated P-value text versus the distinct displayed contrasts beneath which it appears. A treatment-arm attribution is supported by the matched main Table 1 `P = .01` at coarser precision, but is an inference rather than a direct eTable 3 observation.

**Reasoning procedure:** Compared exact repeated wording, column populations, table-specific P values, and the matched main-table context; did not recalculate unavailable rank-sum results.

**Calculation:** `p = 0.014` is repeated four times. The site table's separately printed age `p = 0.017` demonstrates a distinct table-specific contrast. Summary values cannot reproduce all relevant P values.

**Alternative source-grounded interpretations:** The note may intentionally restate a global randomized-arm fact, but placement does not state that scope; copied-footnote history is also possible.

**Mechanical evidence recheck:** Direct pages confirmed the repeated text, different columns, eTable 5 `p = 0.017`, and the main-table coarser `P = .01`; see [evidence_recheck.md](<review_1_5_1/verification/evidence_recheck.md>).

**Quality-control relevance:** A P value should identify its population, outcome, and comparator.

**Potential downstream evidence impact:** If confirmed, an extractor could attach `p = 0.014` to the wrong contrast; no recalculated P value or conclusion change is asserted.

**Human verification steps:** For every occurrence, identify the intended population and comparator from analysis output or table-production records.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — eTable 7 pairs “no statistically significant” with p<0.05

**Candidate statement:** eTable 7's no-significance statement is paired with `p<0.05`, while the same page uses `p>0.05` for similarity and `p=.014` for a difference.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-003 supplement — PDF p. 46](<../joi250084supp2_prod_1765403089.61751.pdf#page=46>); [DOC-003 supplement — PDF p. 47](<../joi250084supp2_prod_1765403089.61751.pdf#page=47>).

**Source evidence:** Footnote 1 says no baseline characteristics were statistically significantly different between groups `(p<0.05)`. Footnote 2 says age differed `(p = 0.014)` and all other characteristics were similar `(p > 0.05)`.

**Reported-versus-comparator:** The no-significance sentence and its parenthetical inequality versus the same page's stated inequality convention.

**Reasoning procedure:** Compared only printed language and inequalities; no unreported characteristic-specific test result was inferred.

**Calculation:** `0.014 < 0.05`; the page calls that a difference and uses `p > 0.05` for similarity.

**Alternative source-grounded interpretations:** The less-than sign or sentence may be a typographical carryover, or an unstated test family/qualifier may be intended.

**Mechanical evidence recheck:** Direct page review confirmed both footnotes and their inequality directions; see [evidence_recheck.md](<review_1_5_1/verification/evidence_recheck.md>).

**Quality-control relevance:** Significance wording and its inequality should not reverse the table's stated convention.

**Potential downstream evidence impact:** If confirmed, an extractor could reverse the table's significance summary or inequality; no specific characteristic difference is asserted.

**Human verification steps:** Obtain completion-status comparison outputs and confirm the intended inequality and scope for footnote 1.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — eTable 10b labels one comparison as both chi-squared and Wilcoxon rank-sum

**Candidate statement:** The same binary arm comparison is described as chi-squared in the eTable 10 method text and Wilcoxon rank-sum in eTable 10b.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-003 supplement — PDF p. 29](<../joi250084supp2_prod_1765403089.61751.pdf#page=29>); [DOC-003 supplement — PDF p. 52](<../joi250084supp2_prod_1765403089.61751.pdf#page=52>).

**Source evidence:** The method description specifies chi-squared for the between-group prohibited-medication proportion. eTable 10b prints AI `6/183 (3.3%)`, human `7/185 (3.8%)`, `P = .793`, with a Wilcoxon rank-sum footnote.

**Reported-versus-comparator:** The named-test label for the same randomized-arm binary proportion comparison in two supplement locations.

**Reasoning procedure:** Matched table, population, binary outcome, arm comparison, counts, and P-value cell while preserving uncertainty about the actual software procedure.

**Calculation:** `6/183 = 3.28%` and `7/185 = 3.78%`, consistent with displayed percentages. An ordinary uncorrected two-proportion/Pearson diagnostic is approximately compatible with `.793`, but cannot identify the generating procedure.

**Alternative source-grounded interpretations:** The p. 29 description may be general, the p. 52 footnote may be copied, or a rank-based analysis of a binary indicator may have been used.

**Mechanical evidence recheck:** Direct pages confirmed both test labels, counts, denominators, and P value; see [evidence_recheck.md](<review_1_5_1/verification/evidence_recheck.md>).

**Quality-control relevance:** A statistical-test label should identify the procedure used for a reported comparison.

**Potential downstream evidence impact:** If confirmed, an extractor could record the wrong test for `P = .793`; no claim is made that the P value itself is wrong.

**Human verification steps:** Inspect named software output, options, and table-generation records to determine which label describes the comparison.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — MICE pooled percentages and printed risk difference have incompatible signs

**Candidate statement:** eTable 16 prints AI 32.2% and human 31.9% but an AI-minus-human risk difference of -1.1 percentage points.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-003 supplement — PDF p. 30](<../joi250084supp2_prod_1765403089.61751.pdf#page=30>); [DOC-003 supplement — PDF p. 59](<../joi250084supp2_prod_1765403089.61751.pdf#page=59>).

**Source evidence:** The methods describe 20-set MICE with Rubin's rules. eTable 16 gives MI-pooled percentages 32.2% (AI) and 31.9% (human), a risk difference of -1.1 percentage points, and a one-sided 95% lower bound of -11.5.

**Reported-versus-comparator:** The AI-minus-human risk-difference cell versus the direct subtraction of the displayed AI and human marginal percentages.

**Reasoning procedure:** Matched analysis population, column order, percentage-point scale, MICE context, and contrast direction. Direct arithmetic was restricted to displayed values; the unreported pooling estimand was not inferred.

**Calculation:** `32.2 - 31.9 = +0.3` percentage points. Values rounding to 32.2% and 31.9% imply an underlying displayed-value difference of approximately **+0.2 to +0.4 percentage points**, so ordinary one-decimal rounding cannot directly yield -1.1.

**Alternative source-grounded interpretations:** The risk difference may be adjusted or standardized under an unstated estimand, separately pooled on a different scale, use a reversed contrast, or reflect a production error. Full model, covariance, and per-imputation output are absent.

**Mechanical evidence recheck:** Direct pages confirmed the MICE/Rubin context, column order, percentages, risk difference, and one-sided lower bound; see [evidence_recheck.md](<review_1_5_1/verification/evidence_recheck.md>).

**Quality-control relevance:** An effect estimate should clearly identify its estimand and agree in sign with directly comparable displayed marginals.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a risk-difference sign inconsistent with displayed arm percentages or copy an incorrect percentage; no noninferiority or conclusion change is asserted.

**Human verification steps:** Obtain the estimand, contrast coding, model, full-precision per-imputation estimates, covariance, and pooling calculation for the -1.1 percentage-point cell.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, these issues could affect what a systematic reviewer, meta-analyst, guideline developer, or structured-data extractor transcribes: endpoint definition (C001), outcome availability/method counts (C002), measure label/unit (C003), P-value comparator scope (C004), significance wording (C005), test label (C006), or effect-estimate sign (C007). This is a generic extraction-risk statement only. It does not state that any item was propagated, changed a conclusion, or caused harm.

## Limitations and Missing Definitions

The package lacks amendment/SAP history and participant-level component outcomes for C001; participant-level A1C/device logs for C002; original figure/table production records for C003-C006; and full imputation/model/pooling output for C007. Several planned or reported relationships lack formulas, variance/covariance information, degrees of freedom, exact test options, sidedness details, or adjusted-estimand definitions. DOC-002's glyph-encoded text required direct CPU-rendered page review. These are resolution or derivative limitations, not coverage gaps. Full details are in [limitations.md](<review_1_5_1/limitations.md>).

## Human Adjudication Checklist

- Confirm every cited direct-source location and its context.
- Obtain missing governing documents, analysis outputs, logs, or production records where identified.
- Decide validity, importance, and action for each stable ID independently.
- Record decisions only in the card templates; retain all stable IDs and source provenance.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Source integrity and execution

The before-run source and reused-artifact hashes are retained in [source_hashes_before.sha256](<review_1_5_1/source_hashes_before.sha256>) and [reused_artifact_hashes_before.sha256](<review_1_5_1/reused_artifact_hashes_before.sha256>). The execution manifest records every review agent:

| Stage | Agent ID | Model | Effort |
|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high |
| reuse_asset_curator | root/reuse_asset_curator | gpt-5.6-terra | medium |
| main_evidence_mapper_001 | root/main_mapper_001 | gpt-5.6-terra | medium |
| support_evidence_mapper_d2a/d2b/d2c | root/support_mapper_d2a; root/support_mapper_d2b; root/support_mapper_d2c | gpt-5.6-terra | medium |
| support_evidence_mapper_d3a/d3b/d3c | root/support_mapper_d3a; root/support_mapper_d3b; root/support_mapper_d3c | gpt-5.6-terra | medium |
| mapping_integrator | root/mapping_integrator | gpt-5.6-terra | medium |
| numeric_checks | root/numeric_reviewer | gpt-5.6-terra | medium |
| statistics_pass_1 | root/statistical_pass_1 | gpt-5.6-terra | high |
| cross_source_checks | root/cross_source_reviewer | gpt-5.6-terra | medium |
| evidence_recheck | root/evidence_rechecker | gpt-5.6-sol | high |
| statistics_pass_2 | root/statistical_pass_2 | gpt-5.6-terra | high |
| evidence_quality | root/quality_auditor | gpt-5.6-sol | high |
| report_generation | root/report_generator | gpt-5.6-terra | medium |

The complete runtime identifiers, start modes, and output artifacts are in [agent_execution_manifest.md](<review_1_5_1/agent_execution_manifest.md>).

### Reproducibility performance

- **Target basis:** Inventory found 170 PDF pages across one 11-page main article, one 90-page protocol/SAP, and one 69-page results supplement; 42 pages have usable source-linked reusable extraction while 128 require fresh direct mapping, including the entire glyph-encoded protocol, so seven bounded mapping shards plus complete checker, recheck, audit, and report waves are planned. This exceeds the 102-page/81-fresh-page calibration package in both source and fresh-mapping burden.
- **Total source units:** 170
- **Fresh-source units:** 128
- **Target elapsed minutes:** 65-100
- **Started UTC:** 2026-09-03T03:44:55Z
- **Finished UTC:** 2026-09-03T05:29:53Z
- **Observed elapsed minutes:** 105.0
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** The 90-page protocol's glyph-encoded text layer required full CPU page rendering and direct visual mapping; several durable artifact writes and reads experienced bounded local filesystem latency.

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Responses | Input tokens | Output tokens | Total tokens | Token-only API-equivalent estimate (USD) |
|---|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 3 unavailable records | 0 | 0 | 0 | 0.000000 known; complete estimate __ |
| gpt-5.6-terra | 14 unavailable records | 0 | 0 | 0 | 0.000000 known; complete estimate __ |

Amounts are token-only API-equivalent estimates under the dated price snapshot, not invoices. Cached input/cache-write tokens are input subsets and reasoning tokens are output subsets; they are not added again to total tokens. Per-agent accounting detail is in [token_usage_summary.md](<review_1_5_1/token_usage_summary.md>) after the accounting cutoff.
