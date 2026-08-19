# Quantitative Quality-Control Consistency Review — Workflow 1.5.1

## Pending Human Adjudication

All six candidate consistency issues in this report are **Pending Human Adjudication**. This is a quantitative reporting quality-control review, not a finding about author intent, study soundness, or paper-level conclusions.

## Executive Quality-Control Summary

Complete source coverage produced **6** stable quality-control candidates: C001, C002, C003, C004, C005, and C006. The candidates concern two matched confidence-interval differences, a quality-of-life direction-label conflict, a cross-document confidence-interval difference, a participant-total mismatch, and a protocol-to-final-report model-rule difference for concrete displayed syntheses.

Small preventable reporting defects can matter when values, intervals, denominators, directions, or model descriptions are extracted into downstream evidence products. This report does not establish that any item propagated, changed a conclusion, or caused serious harm.

## Package and Reused-Evidence Provenance

The supplied package contains three direct PDF sources and no supplied workbook, CSV, DOC, or DOCX source.

| Source ID | Direct source | Pages | SHA-256 |
|---|---|---:|---|
| DOC-001 | [jama_wilson_2020_oi_190154.pdf — PDF p. 1](<../jama_wilson_2020_oi_190154.pdf#page=1>) | 11 | `4786726a6b91df3e168d0f90afb52c3999f4aafe4283d767028ba364ec0cb0a2` |
| DOC-002 | [joi190154supp1_prod.pdf — PDF p. 1](<../joi190154supp1_prod.pdf#page=1>) | 15 | `04c91bf1e28f2e8948e128736028716a7f2c716ca288424f04176889f0bd228e` |
| DOC-003 | [joi190154supp2_prod.pdf — PDF p. 1](<../joi190154supp2_prod.pdf#page=1>) | 49 | `76c413481a77777146f9468094dde137e001b0cb3d9ef2e2020bd4d25074b001` |

Existing native-text derivatives covered 40 direct PDF pages (DOC-001 pp. 1-11 and DOC-003 pp. 17-45). The remaining 35 pages were mapped from fresh native/layout extraction; DOC-003 p. 8 also received direct visual confirmation because its text layer is sparse. Reused material served as a locator and transcription aid; the direct PDFs were the evidence authority. The source and 89 reused-artifact hash registers were unchanged at the evidence-quality audit.

## Scope, Complete Coverage, and Exclusions

| Source ID | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001 | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | 15 | 0 | 15 | 15 | COMPLETE |
| DOC-003 | 49 | 29 | 20 | 49 | COMPLETE |
| **Total** | **75** | **40** | **35** | **75** | **COMPLETE** |

The review mapped the complete, disjoint union of 75 direct-source PDF pages. It covered numeric, denominator, proportion, total, inferential-statistical, cross-document, effect-measure, direction, label, scale, and rate-versus-count relationships within the supplied package.

Excluded from candidate registration were broad methodology, clinical, raw-data, misconduct, and external-literature review; none was within this quality-control scope. Coherent display-zero P values would also be excluded. No printed P-value display zero was found; S056 is a non-P incidence display and is diagnostic-only. S002 is likewise diagnostic-only because the package lacks a compatible exact effect-test and interval rule; it has no candidate card.

## Quantitative and Statistical Relationship Coverage

The canonical relationship inventories contain **34 of 34** numeric/reporting relationships (N001-N034) and **71 of 71** inferential-statistical relationships (S001-S071). All were mapped and checked.

Statistical pass 1, conducted independently, recorded `PASS_1_COMPLETE` for all 71 S relationships. It found no point-estimate containment or interval-order failure and retained source-limited CI-to-P reconstruction as diagnostic only. Statistical pass 2 independently revisited all 71 S relationships against the complete current-run ledger and mechanical recheck; every relationship is `PASS_2_COMPLETE`. Pass 2 added no candidate. It specifically records the corrected Figure 4 orientation: negative values favor NIPPV and positive values favor no NIPPV; the group-subtraction order is not supplied and is not inferred.

## Candidate Index

| ID | Candidate title | Category |
|---|---|---|
| [C001](#c001--bpap-mortality-pooled-confidence-interval-lower-endpoint-differs-across-matched-main-article-displays) | BPAP mortality pooled confidence-interval lower endpoint differs across matched main-article displays | Cross-document numeric inconsistency |
| [C002](#c002--bpap-quality-of-life-pooled-confidence-interval-upper-endpoint-differs-across-matched-main-article-displays) | BPAP quality-of-life pooled confidence-interval upper endpoint differs across matched main-article displays | Cross-document numeric inconsistency |
| [C003](#c003--quality-of-life-direction-label-conflicts-with-the-stated-standardized-direction) | Quality-of-life direction label conflicts with the stated standardized direction | Measure, label, or scale inconsistency |
| [C004](#c004--high-versus-low-intensity-cat-confidence-interval-differs-between-the-main-article-and-supplement) | High-versus-low intensity CAT confidence interval differs between the main article and supplement | Cross-document numeric inconsistency |
| [C005](#c005--cheung-2010-participant-total-differs-between-matched-baseline-and-effectiveness-displays) | Cheung 2010 participant total differs between matched baseline and effectiveness displays | Denominator, proportion, or total inconsistency |
| [C006](#c006--final-report-meta-analysis-model-rule-differs-from-the-protocol-rule-for-syntheses-with-3-through-18-studies) | Final-report meta-analysis model rule differs from the protocol rule for syntheses with 3 through 18 studies | Statistical reporting inconsistency |

## Candidate Evidence Cards

## C001 — BPAP mortality pooled confidence-interval lower endpoint differs across matched main-article displays

**Candidate statement:** The matched BPAP-versus-no-device mortality result has lower 95% confidence-interval endpoints of 0.51 in the abstract and results narrative and 0.50 in Figure 1, while the point estimate, upper endpoint, study count, and patient total match.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 abstract — PDF p. 1](<../jama_wilson_2020_oi_190154.pdf#page=1>); [DOC-001 Figure 1 — PDF p. 4](<../jama_wilson_2020_oi_190154.pdf#page=4>); [DOC-001 results narrative — PDF p. 5](<../jama_wilson_2020_oi_190154.pdf#page=5>).

**Source evidence:** The abstract and p. 5 narrative print BPAP versus no-device mortality OR 0.66 (95% CI, 0.51-0.87), P=.003, 13 studies, and 1423 patients. Figure 1 prints OR 0.66 (95% CI, 0.50-0.87) with 13 BPAP study rows.

**Reported-versus-comparator:** Reported narrative/abstract lower endpoint: 0.51. Comparator Figure 1 lower endpoint: 0.50. Both print OR 0.66, upper endpoint 0.87, 13 studies, and 1423 patients.

**Reasoning procedure:** Match outcome, comparison, effect measure, point estimate, confidence level, study count, patient total, and displayed precision. With no stated population, time-point, model, or precision distinction, the matched rounded interval should repeat.

**Calculation:** `0.51 - 0.50 = 0.01`. The Figure 1 group denominators also reproduce the stated total: `744 + 679 = 1423`.

**Alternative source-grounded interpretations:** A common unrounded endpoint near a rounding boundary could have been formatted by different export routines, or one display could reflect a different unreported output version. The package does not identify either explanation.

**Mechanical evidence recheck:** All three cited locations were found in the direct PDF. Printed values and comparator matched; the consistency rule and calculation reproduced. Unrounded endpoint, pooled standard error, model output, and figure-versus-narrative display rule are unavailable. Direct observation is separated from the possible rounding/export explanation.

**Quality-control relevance:** The directly printed matched interval endpoints do not reconcile under the stated display context and require clarification of the intended value.

**Potential downstream evidence impact:** If confirmed, an extractor could copy different lower confidence limits for the same pooled mortality result into an evidence table. No actual propagation or conclusion change is asserted.

**Human verification steps:** Confirm the final pooled-analysis output and unrounded lower endpoint; compare the figure-generation and narrative-export settings; identify the intended two-decimal confidence interval.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — BPAP quality-of-life pooled confidence-interval upper endpoint differs across matched main-article displays

**Candidate statement:** The matched BPAP-versus-no-device quality-of-life synthesis has upper 95% confidence-interval endpoints of 0.39 in the abstract and narrative and 0.38 in Figure 4, while the point estimate, lower endpoint, study count, and patient total match.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 abstract — PDF p. 1](<../jama_wilson_2020_oi_190154.pdf#page=1>); [DOC-001 Figure 4 and narrative — PDF p. 5](<../jama_wilson_2020_oi_190154.pdf#page=5>).

**Source evidence:** Figure 4 prints BPAP versus no-device quality-of-life SMD 0.16 (95% CI, -0.06 to 0.38), with 9 study rows. The abstract and p. 5 narrative print SMD 0.16 (95% CI, -0.06 to 0.39), P=.15, 9 studies, and 833 patients.

**Reported-versus-comparator:** Reported abstract/narrative upper endpoint: 0.39. Comparator Figure 4 upper endpoint: 0.38. Both print SMD 0.16, lower endpoint -0.06, 9 studies, and 833 patients.

**Reasoning procedure:** Match comparison, outcome, measure, point estimate, lower endpoint, confidence level, study count, patient total, and precision. No separate population, time point, model, or confidence level is stated.

**Calculation:** `0.39 - 0.38 = 0.01`. Displayed Figure 4 group sizes reproduce `424 + 409 = 833` patients.

**Alternative source-grounded interpretations:** Independent formatting or export routines could round a common unprinted endpoint differently near a boundary; an unreported analysis or output version is also possible. The supplied sources state no such distinction.

**Mechanical evidence recheck:** The cited direct-PDF locations, printed values, comparator, matching rule, and arithmetic were reproduced. The unrounded upper endpoint, pooled standard error, final weights, analysis output, and display convention are unavailable.

**Quality-control relevance:** The matched printed interval has two upper endpoints without a supplied explanation of their distinct context.

**Potential downstream evidence impact:** If confirmed, a systematic-review or meta-analysis extractor could copy either upper confidence limit for the same quality-of-life synthesis. No actual propagation or conclusion change is asserted.

**Human verification steps:** Obtain the final pooled output and unrounded upper endpoint; check Figure 4 and narrative export settings; document the intended confidence interval.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Quality-of-life direction label conflicts with the stated standardized direction

**Candidate statement:** The methods state that standardized quality-of-life directions use higher scores for better outcomes, while Table 2 states that higher scores indicate worse quality of life; Figure 4 and the mixed native instrument directions require an explicit scale-context and sign-convention explanation.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-001 synthesis methods — PDF p. 3](<../jama_wilson_2020_oi_190154.pdf#page=3>); [DOC-001 Figure 4 — PDF p. 5](<../jama_wilson_2020_oi_190154.pdf#page=5>); [DOC-001 Table 2 footnote b — PDF p. 8](<../jama_wilson_2020_oi_190154.pdf#page=8>); [DOC-003 instrument directions — PDF p. 15](<../joi190154supp2_prod.pdf#page=15>).

**Source evidence:** DOC-001 p. 3 says measure directions were standardized and higher scores represent better outcomes. Table 2 footnote b says higher scores indicate worse quality of life. DOC-003 p. 15 shows mixed native directions. Figure 4 directly labels negative values “Favors NIPPV” and positive values “Favors No NIPPV.”

**Reported-versus-comparator:** The standardized higher-score statement maps higher standardized score to better outcome; the Table 2 footnote maps higher score to worse quality of life. Figure 4 supplies the stated negative/positive favor orientation, but the group-subtraction order is absent.

**Reasoning procedure:** Once mixed native scales are standardized to one stated direction, the standardized score direction, table footnote, and plotted favor labels require a stated coherent polarity or explicit distinction between standardized and native-scale contexts. Figure 4 alone does not establish group subtraction.

**Calculation:** `positive standardized score = higher standardized score`. Under p. 3 this maps to `better outcome`; under Table 2 footnote b it maps to `worse quality of life`. Figure 4 maps the negative side to NIPPV and the positive side to no NIPPV. These printed mappings require an unstated distinction; no intervention-minus-control or control-minus-intervention subtraction is inferred.

**Alternative source-grounded interpretations:** The Table 2 footnote may describe selected native instruments, and Figure 4 may use a control-minus-intervention orientation. The package lacks study-level extracted means, sign transformations, the group-subtraction rule, and a statement that the table reverts to native polarity.

**Mechanical evidence recheck:** Every cited source page and statement was found directly. The polarity comparison reproduced. The direct Figure 4 orientation is negative=favors NIPPV and positive=favors no NIPPV; the absent group-subtraction order remains the exact missing definition.

**Quality-control relevance:** Opposed higher-score statements can leave the scale context of standardized quality-of-life results unclear to a reader or data extractor.

**Potential downstream evidence impact:** If confirmed, a reviewer could reverse a quality-of-life direction or encode a Table 2 SMD under the wrong scale convention. No actual propagation or conclusion change is asserted.

**Human verification steps:** Provide each study’s sign transformation and group-subtraction convention; state whether Table 2 footnote b refers to native or standardized scales; confirm the intended Figure 4 favor labels.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — High-versus-low intensity CAT confidence interval differs between the main article and supplement

**Candidate statement:** The one-RCT, 14-patient high-versus-low intensity CAT comparison prints WMD 2.30 in both sources but prints different 95% confidence intervals.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [DOC-001 other-device-comparisons narrative — PDF p. 7](<../jama_wilson_2020_oi_190154.pdf#page=7>); [DOC-003 eTable 10 — PDF p. 43](<../joi190154supp2_prod.pdf#page=43>).

**Source evidence:** DOC-001 p. 7 prints WMD 2.30 (95% CI, -2.23 to 6.83), P=.32, for one RCT of 14 patients. DOC-003 p. 43 prints the same comparison, WMD 2.30 (95% CI, -2.35 to 6.95), one RCT, 14 patients; CAT is identified as higher=worse.

**Reported-versus-comparator:** Main article: -2.23 to 6.83. Supplement eTable 10: -2.35 to 6.95. Both retain WMD 2.30, the same comparison, outcome, study count, and total.

**Reasoning procedure:** Match comparison, outcome instrument, design, study count, patient count, point estimate, confidence level, and precision. No distinct analysis set, time point, or calculation is stated, so the rounded interval should be the same.

**Calculation:** Lower-endpoint difference: `-2.23 - (-2.35) = 0.12`; upper-endpoint difference: `6.95 - 6.83 = 0.12`. Both intervals are centered on 2.30: `(-2.23 + 6.83) / 2 = 2.30` and `(-2.35 + 6.95) / 2 = 2.30`.

**Alternative source-grounded interpretations:** The article and supplement may reflect different calculation or export versions, or an unstated standard-error calculation. Group summaries, exact standard error, confidence-interval construction, analysis output, and version history are unavailable.

**Mechanical evidence recheck:** Both direct-PDF locations, printed values, comparator, matching rule, and calculations were reproduced. The canonical relationship is N031. The recheck does not select either interval as intended.

**Quality-control relevance:** The same printed point estimate and matched comparison carry two interval widths without a supplied distinction.

**Potential downstream evidence impact:** If confirmed, an extractor could record different interval widths for the same 14-patient CAT result. No actual propagation or conclusion change is asserted.

**Human verification steps:** Inspect the underlying result output, standard-error and interval calculation, source version history, and the intended interval for the 14-patient comparison.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Cheung 2010 participant total differs between matched baseline and effectiveness displays

**Candidate statement:** The Cheung 2010 baseline row prints CPAP 24 and BPAP-ST 23 participants, totaling 47, while matched effectiveness displays print 49 patients without defining the population difference.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-003 eTable 6 — PDF p. 19](<../joi190154supp2_prod.pdf#page=19>); [DOC-003 eTable 10 — PDF p. 43](<../joi190154supp2_prod.pdf#page=43>); [DOC-001 BPAP-versus-CPAP narrative — PDF p. 6](<../jama_wilson_2020_oi_190154.pdf#page=6>).

**Source evidence:** The Cheung 2010 eTable 6 row lists CPAP 24 and BPAP-ST 23. eTable 10 identifies the matched BPAP-versus-CPAP result as one RCT with 49 patients. The main article likewise describes one RCT of 49 patients; both reference mappings identify Cheung 2010.

**Reported-versus-comparator:** Baseline display total: 47. Matched effectiveness display total: 49. The package does not state that these are enrolled, randomized, treated, baseline-characterized, or outcome-analysis populations.

**Reasoning procedure:** Match author/year, trial identity, design, intervention pair, and result. A baseline group total and effectiveness-display total should reconcile or explicitly identify different populations.

**Calculation:** `24 + 23 = 47`; `49 - 47 = 2`. As a diagnostic only, the eTable 10 rounded percentages are compatible with `7 / 23` and `14 / 26`, totaling 49; event counts are not printed, so this decomposition is not direct evidence.

**Alternative source-grounded interpretations:** The 47 may be baseline-characterized participants and 49 all randomized or analyzed participants, or two participants may be absent from the baseline display. The supplied sources do not state which explanation applies.

**Mechanical evidence recheck:** Cited locations, study identity, group counts, 49-patient comparator, arithmetic, and missing population definitions were reproduced directly. The recheck does not treat the diagnostic percentage decomposition as a printed event-count record.

**Quality-control relevance:** Matched participant totals are not reconciled by a supplied population definition.

**Potential downstream evidence impact:** If confirmed, an evidence extractor could record 47 or 49 as the trial total, affecting denominator or sample-size metadata. No actual propagation or conclusion change is asserted.

**Human verification steps:** Identify the population represented in each display; confirm enrollment, randomization, treatment, baseline, and outcome-analysis totals; document whether either count requires correction.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Final-report meta-analysis model rule differs from the protocol rule for syntheses with 3 through 18 studies

**Candidate statement:** The protocol assigns DerSimonian-Laird with Knapp-Hartung variance adjustment to the 3-through-18-study branch, while the final article describes DerSimonian-Laird random effects for `k >= 3` without reporting that adjustment; the overlap contains concrete displayed syntheses.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-002 Data Synthesis — PDF p. 11](<../joi190154supp1_prod.pdf#page=11>); [DOC-001 Data Synthesis and Analysis — PDF p. 3](<../jama_wilson_2020_oi_190154.pdf#page=3>); [DOC-001 Figures 1 and 2 — PDF p. 4](<../jama_wilson_2020_oi_190154.pdf#page=4>); [DOC-001 Figures 3 and 4 — PDF p. 5](<../jama_wilson_2020_oi_190154.pdf#page=5>).

**Source evidence:** The protocol specifies meta-analysis for more than two studies, DerSimonian-Laird random effects for more than 18 studies, and DerSimonian-Laird plus Knapp-Hartung otherwise. The final article states DerSimonian-Laird random effects except when fewer than three studies are included, when fixed-effect Mantel-Haenszel is used. Figures show concrete 3-, 5-, 6-, 9-, 13-, and 15-study syntheses.

**Reported-versus-comparator:** Protocol reporting rule for `3 <= k <= 18`: DerSimonian-Laird with Knapp-Hartung variance adjustment. Final-article reporting rule for `k >= 3`: DerSimonian-Laird random effects, without a stated Knapp-Hartung adjustment.

**Reasoning procedure:** Combine the protocol’s more-than-two-study eligibility threshold with its stated model branch, then compare that explicit branch with the final article’s rule for the same concrete study-count range. This is a comparison of printed model-rule reporting only.

**Calculation:** Protocol: `k > 18` uses the separately stated DerSimonian-Laird branch; `3 <= k <= 18` uses DerSimonian-Laird plus Knapp-Hartung. Final article: `k < 3` uses fixed-effect Mantel-Haenszel; `k >= 3` uses stated DerSimonian-Laird random effects. The intersection is `3 <= k <= 18`, including printed k=3, 5, 6, 9, 13, and 15 syntheses.

**Alternative source-grounded interpretations:** The final article may use a high-level label that retains Knapp-Hartung without naming it, or the plan may have been amended. The package provides no amendment, per-synthesis statistical command, output, degrees of freedom, or reconciliation.

**Mechanical evidence recheck:** Direct PDF locations, both written rules, the overlapping range, and the displayed study counts were found and reproduced. The recheck establishes a concrete model-rule reporting difference only; it does not infer the method actually used for any synthesis.

**Quality-control relevance:** The final report does not state whether the protocol’s named variance adjustment applies to displayed syntheses in the concrete overlapping range.

**Potential downstream evidence impact:** If confirmed, a reviewer, meta-analyst, or guideline evidence table could copy an incomplete or differing model description for these syntheses. No actual propagation, calculation change, or conclusion change is asserted.

**Human verification steps:** Review the analysis plan amendments, per-synthesis statistical commands and output, variance settings, and final methods wording; state whether Knapp-Hartung was used for each 3-through-18-study synthesis.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed, these items identify fields that downstream evidence work may need to verify before reuse: confidence-interval endpoints (C001, C002, C004), standardized direction conventions (C003), participant totals (C005), and synthesis-model descriptions (C006). Such fields can be copied into systematic reviews, meta-analyses, guideline evidence tables, or later summaries. The supplied package does not establish that copying occurred, that a quantitative synthesis changed, or that the paper’s conclusions changed.

## Limitations and Missing Definitions

The package has no raw participant data, source-study analysis files, meta-analysis code, or protocol amendment. It also lacks unrounded pooled endpoints, pooled standard errors, complete model output, figure-versus-narrative export rules, group-subtraction and sign-transformation documentation for quality-of-life SMDs, Cheung population definitions and event numerators, and per-synthesis model settings.

Exact CI-to-P or statistic compatibility could not be asserted because the sources do not provide a compatible result-specific test statistic, standard error, degrees of freedom, covariance, continuity correction, final weights, variance estimator, or CI construction. S002 remains diagnostic-only for that reason. `NR` and `NOS` cells remain source-reported missing entries rather than inferred values. These limitations constrain resolution of the six comparisons but do not leave a scientific-coverage gap.

## Human Adjudication Checklist

For each card, verify the direct PDF locations, obtain the missing source record identified in its mechanical recheck, determine the intended reported value or definition, document the basis for any action, and complete every human-adjudication field with initials and notes. Preserve the stable IDs C001-C006 when recording the outcome.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

The complete coverage and artifact map is recorded in [coverage_manifest.md](<review_1_5_1/coverage_manifest.md>). Source coverage is recorded in [source_coverage.md](<review_1_5_1/source_coverage.md>), direct hashes in [source_hashes_before.sha256](<review_1_5_1/source_hashes_before.sha256>), and reused-asset hashes in [reused_artifact_hashes_before.sha256](<review_1_5_1/reused_artifact_hashes_before.sha256>). Direct-source and reused-asset integrity checks were unchanged at the audit.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | /root | gpt-5.6-sol | high | CURRENT_SESSION | `run_state.md` |
| asset_curator | /root/reuse_asset_curator | gpt-5.6-terra | medium | FRESH_SPAWN | `evidence_asset_inventory.md` |
| main_evidence_mapper | /root/main_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/main_quantitative_evidence.md` |
| support_evidence_mapper | /root/support_quantitative_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/support_quantitative_evidence.md` |
| numeric_checks | /root/numeric_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/numeric_consistency.md` |
| cross_source_checks | /root/cross_source_consistency_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/cross_source_consistency.md` |
| statistics_pass_1 | /root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_1.md` |
| evidence_recheck | /root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | `verification/evidence_recheck.md` |
| statistics_pass_2 | /root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_2.md` |
| evidence_quality | /root/quality_control_auditor | gpt-5.6-sol | high | FRESH_SPAWN | `quality/evidence_quality_audit.md` |
| report_generation | /root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | `../final_report_1_5_1.md` |

### Reproducibility performance

- **Target basis:** Three PDFs totaling 75 pages, with reusable page text anticipated for 40 pages and 35 pages requiring fresh extraction; the two supplements contain protocol and results tables that increase relationship-mapping complexity despite the moderate page count.
- **Total source units:** 75
- **Fresh-source units:** 35
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-08-18T23:18:40Z
- **Finished UTC:** 2026-08-19T00:00:18Z
- **Observed elapsed minutes:** 41.6
- **Target status:** MET_TARGET
- **Exceedance causes:** None

These initialized performance values are to be finalized by the coordinator immediately after Markdown assembly.

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Input tokens | Output tokens | Total tokens | Token-only API-equivalent cost (USD) |
|---|---:|---:|---:|---:|
| gpt-5.6-sol | 0 known | 0 known | 0 known | 0.000000 known |
| gpt-5.6-terra | 0 known | 0 known | 0 known | 0.000000 known |

The runtime exposed no authoritative token counts for the coordinator or any of the 10 specialist agents, so all 11 response records are `UNAVAILABLE`; no text-length estimate was substituted. The zero values above are known subtotals only, not complete counts. Cached input and cache-write counts are input subsets, and reasoning tokens are an output subset; they are not added again to total tokens. Per-agent detail is recorded in [token_usage_summary.md](<review_1_5_1/token_usage_summary.md>). Any amount is a token-only API-equivalent estimate under the pricing snapshot dated 2026-08-18, not an invoice, and excludes non-token costs.
