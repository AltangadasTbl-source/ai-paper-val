# Quantitative Quality-Control Consistency Review: Vitamin D and Omega-3 Trial Paper Package

> **Pending Human Adjudication:** This source-grounded review identifies reporting-consistency candidates for human review. It does not determine validity, importance, correction, acceptance, exclusion, severity, scientific conclusions, or harm.

## Executive Quality-Control Summary

Fresh source-first processing and complete mapped coverage identified **7** distinct quantitative reporting quality-control candidates: two arm-specific contributor-count discrepancies, four participant-count-to-treatment-label discrepancies, and one plan-versus-implemented imputation-count difference. All seven are **Pending Human Adjudication**. The candidate set was produced from complete mapped coverage, not from a review queue, target count, ranking, or cap. No conclusion change or downstream propagation is asserted.

## Package and Fresh-Processing Provenance

The supplied package contains four direct PDFs: the 11-page main article (DOC-001), a 33-page protocol/analytic-plan supplement (DOC-002), a 19-page results supplement (DOC-003), and a one-page data-sharing statement (DOC-004). Fresh source processing used PDF metadata, native text, layout text, and targeted page rendering; no prior audit derivative was used as evidence. Native/layout text was usable for all pages, and targeted OCR was not required.

| Source | Role | Units | Fresh preparation |
|---|---|---:|---|
| [jama_de_boer_2019_oi_190122.pdf — PDF p. 1](<../jama_de_boer_2019_oi_190122.pdf#page=1>) | Main article | 11 PDF pages | Native/layout text; pp. 1-11 rendered |
| [joi190122supp1_prod.pdf — PDF p. 1](<../joi190122supp1_prod.pdf#page=1>) | Protocol and analytic-plan addendum | 33 PDF pages | Native/layout text; result-relevant pp. 11-20 and 31-33 rendered |
| [joi190122supp2_prod.pdf — PDF p. 1](<../joi190122supp2_prod.pdf#page=1>) | Results supplement | 19 PDF pages | Native/layout text; pp. 1-19 rendered |
| [joi190122supp3_prod.pdf — PDF p. 1](<../joi190122supp3_prod.pdf#page=1>) | Data-sharing statement | 1 PDF page | Native/layout text; p. 1 rendered |

## Scope, Complete Coverage, and Exclusions

All 64 direct-source PDF pages had zero reusable units, 64 fresh-required units, 64 mapped units, and `COMPLETE` status. The coverage manifest contains 19 disjoint stage rows with one artifact path per row. The review covered result-relevant numeric values, denominators, proportions, totals, estimates, intervals, P values, labels, scales, rates, counts, and matched cross-document occurrences.

Excluded from the candidate threshold were broad study-design, clinical, novelty, misconduct, raw-data, and conclusion-validity assessments. Analysis-unit or population matters were considered only where they created a concrete quantitative inconsistency. No literal display-zero P value occurred; no candidate is based on display precision.

## Quantitative and Statistical Relationship Coverage

The canonical relationship inventories contain 62 numeric/reporting relationships (`N001`-`N062`) and 39 statistical relationships (`S001`-`S039`). Numeric consistency checking covered all 62 N relationships; cross-source checking covered all 101 relationships. Statistical pass 1 and independent statistical pass 2 each recorded completion for every S relationship. Pass 2 also considered the full C001-C007 ledger and mechanical recheck and registered no new candidate.

Both statistical passes used fresh, distinct `gpt-5.6-terra` high-effort specialist executions. Checks included arithmetic and totals; denominators/proportions; interval, point-estimate, direction, and label compatibility where source-supported; rate-versus-count distinction; and matched-result agreement across the article and supplements.

## Candidate Index

| ID | Category | Candidate |
|---|---|---|
| C001 | Cross-document numeric inconsistency | Figure 2 omega-3 eGFR contributor counts conflict with Table 2 |
| C002 | Cross-document numeric inconsistency | Figure 2 omega-3 urine-ACR contributor counts conflict with eTable 6 |
| C003 | Measure, label, or scale inconsistency | Figure 3 assigns vitamin-D arm sizes to the opposite column labels |
| C004 | Measure, label, or scale inconsistency | Figure 4 assigns omega-3 arm sizes to the opposite column labels |
| C005 | Measure, label, or scale inconsistency | eFigure 2 places vitamin-D participant counts under the opposite headings |
| C006 | Measure, label, or scale inconsistency | eFigure 3 places omega-3 participant counts under the opposite headings |
| C007 | Cross-document numeric inconsistency | Imputation count differs between the analytic-plan addendum and article methods |

## Candidate Evidence Cards

## C001 — Figure 2 omega-3 eGFR contributor counts conflict with Table 2

**Candidate statement:** Figure 2 panel B and Table 2 print different omega-3 arm-specific eGFR contributor counts at each matched time point.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Figure 2 panel B — PDF p. 7](<../jama_de_boer_2019_oi_190122.pdf#page=7>); [Table 2 — PDF p. 8](<../jama_de_boer_2019_oi_190122.pdf#page=8>).

**Source evidence:** Figure 2 prints omega-3 placebo `607/459/438` and omega-3 active `701/531/496` at baseline/year 2/year 5. Table 2 prints placebo `651/491/462` and active `657/499/472` for the same outcome, contrast, and time points. Panel B exactly repeats panel A's vitamin-D count sequences.

**Reported-versus-comparator:** Figure 2 panel B versus Table 2; the source supplies no distinct panel-B population definition.

**Reasoning procedure:** Match outcome, factorial contrast, arm labels, and time points, then compare each arm-specific contributor count while retaining each time-point total as a separate check.

**Calculation:** Figure minus Table 2 is placebo `-44/-32/-24` and active `+44/+32/+24`; both locations total `1308/990/934` at baseline/year 2/year 5.

**Alternative source-grounded interpretations:** An unstated figure-specific subset could have been used, or panel B could retain copied count annotations; neither mechanism is stated in the package.

**Mechanical evidence recheck:** Cited locations and all six counts were re-read. The rule is applicable; a panel-B inclusion rule or production data is unavailable.

**Quality-control relevance:** The printed arm split does not reconcile across matched displays, although the time-specific totals do.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy incorrect arm-specific eGFR contributor counts from Figure 2; no propagation or conclusion change is asserted.

**Human verification steps:** Confirm the intended panel-B population and each omega-3 arm/time count from figure-production records or source data.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Figure 2 omega-3 urine-ACR contributor counts conflict with eTable 6

**Candidate statement:** Figure 2 panel D and eTable 6 print different omega-3 arm-specific urine-ACR contributor counts at all matched time points.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Figure 2 panel D — PDF p. 7](<../jama_de_boer_2019_oi_190122.pdf#page=7>); [eTable 6 — PDF p. 11](<../joi190122supp2_prod.pdf#page=11>).

**Source evidence:** Figure 2 prints omega-3 placebo `609/463/440` and active `702/529/505`; eTable 6 prints placebo `653/490/467` and active `658/502/478`. Panel D exactly repeats panel C's vitamin-D sequences.

**Reported-versus-comparator:** Figure 2 panel D versus eTable 6 for the same urine-ACR contrast and time points.

**Reasoning procedure:** Compare the arm-specific matched contributor counts and separately verify the time-specific combined totals.

**Calculation:** Figure minus eTable 6 is placebo `-44/-27/-27` and active `+44/+27/+27`; both locations total `1311/992/945`.

**Alternative source-grounded interpretations:** An unstated plotting subset is possible; copied panel-C count annotations are also possible but not source-established.

**Mechanical evidence recheck:** All six values, caption context, comparator values, and page locations were reproduced; no different population is defined.

**Quality-control relevance:** The displayed omega-3 arm split is inconsistent across matched result displays.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy incorrect omega-3 urine-ACR contributor counts; no propagation or conclusion change is asserted.

**Human verification steps:** Verify panel-D population rules and intended arm/time counts against figure-production records or source data.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Figure 3 assigns vitamin-D arm sizes to the opposite column labels

**Candidate statement:** Figure 3 places the randomized vitamin-D participant counts under the opposite treatment headings; this candidate is confined to participant-count columns.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Abstract — PDF p. 1](<../jama_de_boer_2019_oi_190122.pdf#page=1>); [Table 2 and Figure 3 — PDF p. 8](<../jama_de_boer_2019_oi_190122.pdf#page=8>).

**Source evidence:** Factorial allocations give active vitamin D `370+333=703` and vitamin-D placebo `289+320=609`. Figure 3 prints `N=703` under Placebo and `N=609` under Vitamin D, including the same opposite nested-count mapping.

**Reported-versus-comparator:** Figure 3 participant-count columns versus randomized factorial allocation identity and Table 2 treatment labels.

**Reasoning procedure:** Sum factorial cells by vitamin-D assignment and compare the totals and nested N values with the figure headings. Do not infer a reversal of mean changes or forest estimates.

**Calculation:** Active vitamin D: `370+333=703`; placebo: `289+320=609`. Figure 3 assigns 703 to Placebo and 609 to Vitamin D. Its first nested count column `333+370=703` is active vitamin D.

**Alternative source-grounded interpretations:** The participant-count columns may be transposed while headings, mean changes, and forest direction remain treatment-aligned. Figure 3's overall changes (`-13.1` placebo; `-12.3` vitamin D) agree with Table 2 at printed precision.

**Mechanical evidence recheck:** The allocation cells, Figure 3 headings, overall N values, and nested N values were reproduced. Figure-production metadata and cell-level comparators for every subgroup estimate are unavailable.

**Quality-control relevance:** This is a count-to-treatment-label mapping issue only; the supplied evidence does not establish reversal of means, changes, or forest estimates.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy a Figure 3 subgroup participant count under the wrong vitamin-D treatment label; no propagation or conclusion change is asserted.

**Human verification steps:** Verify the intended participant-count columns for every Figure 3 subgroup row and separately confirm whether any non-count display element requires change.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Figure 4 assigns omega-3 arm sizes to the opposite column labels

**Candidate statement:** Figure 4 places randomized omega-3 participant counts under opposite treatment headings; this candidate is confined to participant-count columns.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Abstract — PDF p. 1](<../jama_de_boer_2019_oi_190122.pdf#page=1>); [Table 2 — PDF p. 8](<../jama_de_boer_2019_oi_190122.pdf#page=8>); [Figure 4 — PDF p. 9](<../jama_de_boer_2019_oi_190122.pdf#page=9>).

**Source evidence:** Factorial allocations give active omega-3 `370+289=659` and omega-3 placebo `333+320=653`. Figure 4 prints `N=659` under Placebo and `N=653` under Omega-3 Fatty Acids.

**Reported-versus-comparator:** Figure 4 participant-count columns versus factorial allocation identities and Table 2 treatment labels.

**Reasoning procedure:** Sum the randomized factorial cells by omega-3 assignment and compare the resulting overall and nested N values to the figure headings, without extending the observation to means or estimates.

**Calculation:** Active omega-3: `370+289=659`; placebo: `333+320=653`. Figure 4 places 659 under Placebo and 653 under Omega-3 Fatty Acids; first nested column `289+370=659` is active omega-3.

**Alternative source-grounded interpretations:** N columns may be transposed while headings and mean-change values remain treatment-aligned. The overall Figure 4 changes (`-13.1` placebo; `-12.2` omega-3) match Table 2 at printed precision.

**Mechanical evidence recheck:** The factorial allocation, headings, N values, and Table 2 labels were reproduced. Production metadata and every cell-level subgroup comparator are unavailable.

**Quality-control relevance:** This is a participant-count identity issue only, not evidence that the figure's means or forest estimates are reversed.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy Figure 4 subgroup Ns under incorrect omega-3 treatment labels; no propagation or conclusion change is asserted.

**Human verification steps:** Check intended N columns for all Figure 4 subgroup rows and independently verify whether any non-count display must be remapped.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — eFigure 2 places vitamin-D participant counts under the opposite headings

**Candidate statement:** eFigure 2 maps vitamin-D participant counts to opposite headings while its overall geometric-change values remain aligned with the printed headings; this candidate is count-only.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Abstract — PDF p. 1](<../jama_de_boer_2019_oi_190122.pdf#page=1>); [eTable 6 — PDF p. 11](<../joi190122supp2_prod.pdf#page=11>); [eFigure 2 — PDF p. 18](<../joi190122supp2_prod.pdf#page=18>).

**Source evidence:** eFigure 2 prints Placebo `N=703`, ratio `3.02`, and Active intervention `N=609`, ratio `2.97`. eTable 6 identifies active vitamin D baseline `N=702`, year-5 ratio `2.97`, and placebo `N=609`, ratio `3.02`; randomized totals are 703 active and 609 placebo.

**Reported-versus-comparator:** eFigure 2 participant-count columns versus randomized factorial totals and eTable 6 arm-specific values.

**Reasoning procedure:** Compare N identities separately from geometric-change values and forest direction, using allocation sums to identify randomized arms.

**Calculation:** Active vitamin D is `370+333=703`; placebo is `289+320=609`. eFigure 2 places these Ns under opposite headings, while `3.02` placebo and `2.97` active agree with eTable 6. The 703-versus-702 difference is randomized total versus measured baseline availability.

**Alternative source-grounded interpretations:** Only the N columns may be transposed; the headings, change values, and forest direction may remain as printed. The source does not establish that any subgroup estimate requires remapping.

**Mechanical evidence recheck:** The eFigure, eTable, allocation identity, ratios, and count calculations were reproduced. Production metadata and an independent table for each subgroup estimate are absent.

**Quality-control relevance:** The observation is restricted to displayed participant-count identity; no value, ratio, or forest-direction inconsistency is claimed.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an eFigure 2 subgroup N under the wrong vitamin-D label; no propagation or conclusion change is asserted.

**Human verification steps:** Determine whether only N columns require exchange and verify the treatment identity of each displayed subgroup element.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — eFigure 3 places omega-3 participant counts under the opposite headings

**Candidate statement:** eFigure 3 maps omega-3 participant counts to opposite headings while overall geometric-change values remain aligned with their printed headings; this candidate is count-only.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Abstract — PDF p. 1](<../jama_de_boer_2019_oi_190122.pdf#page=1>); [eTable 6 — PDF p. 11](<../joi190122supp2_prod.pdf#page=11>); [eFigure 3 — PDF p. 19](<../joi190122supp2_prod.pdf#page=19>).

**Source evidence:** eFigure 3 prints Placebo `N=659`, ratio `3.05`, and Active intervention `N=653`, ratio `2.94`. eTable 6 identifies active omega-3 baseline `N=658`, year-5 ratio `2.94`, and placebo `N=653`, ratio `3.05`; randomized totals are 659 active and 653 placebo.

**Reported-versus-comparator:** eFigure 3 participant-count columns versus randomized factorial totals and eTable 6 arm-specific values.

**Reasoning procedure:** Evaluate N-to-treatment identity separately from values, ratios, and forest direction.

**Calculation:** Active omega-3 is `370+289=659`; placebo is `333+320=653`. eFigure 3 places those Ns under opposite headings, while `3.05` placebo and `2.94` active agree with eTable 6. The 659-versus-658 difference is randomized total versus measured baseline availability.

**Alternative source-grounded interpretations:** N columns may be transposed while headings, changes, and forest direction remain as printed. The supplied comparison does not establish a reversal of all values.

**Mechanical evidence recheck:** The eFigure, eTable, allocation identity, ratios, and N calculations were re-read; production metadata and a full cell-level comparator are not supplied.

**Quality-control relevance:** The observation is confined to participant-count columns; no ratio, change-value, or forest-direction discrepancy is claimed.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an eFigure 3 subgroup N under the wrong omega-3 label; no propagation or conclusion change is asserted.

**Human verification steps:** Verify whether N columns alone require exchange and confirm treatment identity for all displayed subgroup elements.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Imputation count differs between the analytic-plan addendum and article methods

**Candidate statement:** The analytic-plan addendum states 10 imputation data sets, whereas the article methods state implemented multiple imputation `M=20`.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [Analytic-plan addendum, Section 15c — PDF p. 32](<../joi190122supp1_prod.pdf#page=32>); [Article Data Analysis — PDF p. 3](<../jama_de_boer_2019_oi_190122.pdf#page=3>).

**Source evidence:** DOC-002 p. 32 states `10 imputation datasets` combined with Rubin's rules. DOC-001 p. 3 states multiple imputation `(M = 20)` and Rubin-rule combination.

**Reported-versus-comparator:** The prospective analytic-plan addendum versus the article's implemented-method description for related missing-outcome analyses.

**Reasoning procedure:** Compare the exact imputation counts and shared Rubin-rule context, while retaining the possibility that a final implemented method intentionally differed from a plan.

**Calculation:** `20 - 10 = 10`; the article reports twice the number of imputation data sets stated in the addendum.

**Alternative source-grounded interpretations:** The number of imputations may have been intentionally increased and the analytic scope broadened after the plan text was written. The package does not include a dated change record, rationale, or later governing amendment.

**Mechanical evidence recheck:** Both statements and their exact PDF locations were reproduced; the corrected plan location is DOC-002 p. 32. Intent, governance by this exact plan version, and documentation are not established.

**Quality-control relevance:** The package contains different exact counts for a plan and the reported implemented procedure; this does not itself establish an analysis error or a disclosure requirement.

**Potential downstream evidence impact:** If confirmed relevant after human review, a data extractor could copy a planned-versus-implemented imputation-count difference; no propagation or conclusion change is asserted.

**Human verification steps:** Identify any dated amendment or analysis record explaining 10 versus 20 and determine the governing planned procedure for the reported analysis.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If confirmed through human adjudication, small preventable reporting defects can matter when a systematic review, meta-analysis, guideline, or data extractor reuses the specific count, treatment label, or implemented-method value shown in a source. This review does not establish that any value has been reused, propagated, changed a conclusion, or caused harm.

## Limitations and Missing Definitions

- No participant-level data or figure-production files were supplied; the review cannot determine the mechanism of a display discrepancy or prescribe a correction.
- Unrounded model outputs, complete person-time denominators, every interaction-test coefficient/standard error/degrees of freedom, proportional-hazards diagnostics, and correlation test definitions were not supplied.
- C003-C006 are count-only observations. Their overall means or geometric-change ratios remain aligned with printed treatment headings; the package does not establish that subgroup estimates or forest directions require remapping.
- No later change-control record or rationale explains the C007 move from 10 planned to 20 implemented imputations.
- Candidates are not adjudications, severity ratings, corrections, or conclusion-impact claims.

## Human Adjudication Checklist

For each candidate, verify the cited source values and page locations; identify the governing population, treatment label, display-production record, or analytic amendment; determine whether the comparison is applicable; record a decision only in the five placeholder fields in the candidate card; and preserve the source distinction between direct observation and inferred explanation.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and Source Integrity

- **Target basis:** Four supplied PDFs contain 64 pages: an 11-page main article plus 33-page, 19-page, and 1-page support files. All 64 pages require fresh native and layout extraction; result-relevant pages may require targeted rendering, and complete main/support mapping plus two independent statistical passes is required. The scope is smaller than the 102-page calibration package but has no reusable units.
- **Total source units:** 64
- **Fresh-source units:** 64
- **Source integrity before preprocessing:** Recorded in `review_1_5_2/source_hashes_before.sha256`.
- **Source integrity after review:** VERIFIED_UNCHANGED; all four SHA-256 checks match `review_1_5_2/source_hashes_before.sha256` and `source_hashes_after.sha256`.
- **Source coverage:** DOC-001 11/11; DOC-002 33/33; DOC-003 19/19; DOC-004 1/1 mapped units, all `COMPLETE`.
- **Relationship coverage:** 62 N relationships and 39 S relationships; numeric, cross-source, and both statistical passes complete.

### Agent Execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | `run_state.md` |
| fresh-source preprocessing | root/fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN | `evidence_asset_inventory.md` |
| main quantitative mapping | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/main_quantitative_evidence.md` |
| support quantitative mapping | root/support_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/support_quantitative_evidence.md` |
| numeric consistency | root/numeric_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/numeric_consistency.md` |
| cross-source consistency | root/cross_source_reviewer | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/cross_source_consistency.md` |
| statistical pass 1 | root/statistical_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_1.md` |
| evidence recheck | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | `verification/evidence_recheck.md` |
| statistical pass 2 | root/statistical_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_2.md` |
| evidence quality | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | `quality/evidence_quality_audit.md` |
| report generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | `report_generation.md` |

### Performance

- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-08-24T01:53:43Z
- **Finished UTC:** 2026-08-24T02:34:32Z
- **Observed elapsed minutes:** 40.8
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token Accounting and Cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Requests | Input tokens | Output tokens | Total tokens | Token-only API-equivalent estimate (USD) |
|---|---:|---:|---:|---:|---:|
| gpt-5.6-sol | 3 unavailable records | 0 known | 0 known | 0 known | 0.000000 known |
| gpt-5.6-terra | 8 unavailable records | 0 known | 0 known | 0 known | 0.000000 known |

The runtime exposed no authoritative response token counts for the coordinator or any specialist, so the ledger uses one `UNAVAILABLE` row per manifested agent and does not estimate usage from text. The displayed zero is the known subtotal, not a complete token count. Cached input/cache-write counts are input subsets and reasoning counts are output subsets; they are not added again to total tokens. Amounts are token-only API-equivalent estimates under the 2026-08-18 pricing snapshot, not an invoice. The versioned token summary supplies per-agent detail.
