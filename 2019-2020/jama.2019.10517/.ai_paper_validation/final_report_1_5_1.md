# 1. Quantitative Quality-Control Consistency Review — JAMA 2019.10517 (Workflow 1.5.1)

# 2. Pending Human Adjudication Notice

> **Pending Human Adjudication**
>
> This report records source-grounded quantitative reporting quality-control candidates. Every candidate remains **Pending Human Adjudication**. It makes no severity assignment, final correction, validity decision, or conclusion about the paper's overall findings.

# 3. Executive Quality-Control Summary

Complete review of the supplied package identified **3** stable candidate consistency issues: C001, C002, and C003. The review covered all 63 direct-source PDF pages and did not use a review queue, a top-N subset, a candidate cap, or a deferred-by-cap category.

The candidates concern (1) an absolute difference that does not reproduce from displayed counts under ordinary nearest rounding, (2) an HbA1c unit/scale label conflict across matched displays, and (3) conflicting protocol recruitment targets. These are bounded reporting observations requiring human verification. They do not establish that a paper-level conclusion changed or that any downstream use has occurred.

# 4. Package and Reused-Evidence Provenance

The supplied package contains four direct PDFs: the main article, protocol/data analytic plan, results supplement, and data-sharing statement. Direct-source evidence has precedence throughout. Reused native text, normalized text, rendered pages, OCR text, OCR metadata, and document maps were used as locators and transcription aids only; cited candidate facts were confirmed against the direct PDFs.

| Source ID | Direct source | Content class | Pages | Reused page-level assets |
|---|---|---|---:|---:|
| DOC-001 | [jama_flint_2019_oi_190079.pdf — PDF p. 1](<../jama_flint_2019_oi_190079.pdf#page=1>) | Main article | 10 | 10 |
| DOC-002 | [joi190079supp1_prod.pdf — PDF p. 1](<../joi190079supp1_prod.pdf#page=1>) | Protocol and data analytic plan | 42 | 0 |
| DOC-003 | [joi190079supp2_prod.pdf — PDF p. 1](<../joi190079supp2_prod.pdf#page=1>) | Results supplement (eFigures 1-9) | 10 | 10 |
| DOC-004 | [joi190079supp3_prod.pdf — PDF p. 1](<../joi190079supp3_prod.pdf#page=1>) | Data-sharing statement | 1 | 0 |

Ninety-four designated reusable artifacts were source-matched and inventoried. DOC-002 and DOC-004 had only inventory-level reusable records, so all 43 of their pages were mapped directly. The direct-source and reused-artifact hashes were recorded before review and rechecked unchanged after scientific report assembly.

# 5. Scope, Complete Coverage, and Exclusions

The review was limited to quantitative reporting consistency: numeric/arithmetic, denominator/proportion/total, statistical reporting, cross-document numeric, measure/label/scale, and rate-versus-count relationships. It was not a broad clinical, methodological, misconduct, raw-data, or external-literature audit.

| Coverage measure | Count |
|---|---:|
| Total direct source units | 63 |
| Reusable units | 20 |
| Fresh-required units | 43 |
| Mapped units | 63 |

Every source row is complete: DOC-001 10/10 mapped, DOC-002 42/42 mapped, DOC-003 10/10 mapped, and DOC-004 1/1 mapped. Thus, 20 reusable plus 43 fresh-required units equals 63 total units, and 63 mapped units equals 63 total units.

Excluded as candidates were ordinary incomplete methodological detail without a concrete reported inconsistency, planned-versus-final statements that were not matched in population/time/model, and coherent display-zero P-value notation. No assigned relationship displayed `P = 0`, `p = 0.000`, or an equivalent; no candidate was created from P-value display precision.

# 6. Quantitative and Statistical Relationship Coverage

The numeric inventory is complete at **N001-N060** (60 relationships), spanning direct article tables/figures, protocol/SAP quantities, results-supplement figures, and the data-sharing statement. N060 is an explicit no-applicable quantitative unit. Detailed relationship mapping is retained in [numeric_relationship_inventory.md](<review_1_5_1/relationships/numeric_relationship_inventory.md>).

The statistical inventory is complete at **S001-S048** (48 relationships). A distinct fresh `gpt-5.6-terra` high-effort reviewer completed pass 1 for every S ID, and a different fresh `gpt-5.6-terra` high-effort reviewer completed pass 2 for the same complete ID set. Every statistical relationship is recorded as `PASS_1_COMPLETE` and `PASS_2_COMPLETE`; pass 2 reconciled C001, C002, and C003 and found no new source-grounded candidate. Detailed records are retained in [relationship_inventory.md](<review_1_5_1/statistics/relationship_inventory.md>), [statistical_pass_1.md](<review_1_5_1/checkers/statistical_pass_1.md>), and [statistical_pass_2.md](<review_1_5_1/checkers/statistical_pass_2.md>).

Numeric and cross-source review covered the complete N and S inventories. Statistical compatibility was assessed only where compatible source definitions were supplied; rounded-value diagnostics were not treated as reconstructions of reported analyses.

# 7. Candidate Index

| Stable ID | Candidate consistency issue | Category | Status |
|---|---|---|---|
| [C001](#c001--table-5-absolute-difference-does-not-reproduce-from-the-displayed-counts) | Table 5 absolute difference does not reproduce from displayed counts | Numeric or arithmetic inconsistency | Pending Human Adjudication |
| [C002](#c002--hba1c-interaction-is-labelled-with-a-concentration-unit-while-matched-displays-use-percent) | HbA1c interaction uses `mg/dL` while matched displays use percent | Measure, label, or scale inconsistency | Pending Human Adjudication |
| [C003](#c003--protocol-recruitment-target-conflicts-between-82-and-98-participants-per-site) | Protocol recruitment target conflicts between 82 and 98 participants per site | Denominator, proportion, or total inconsistency | Pending Human Adjudication |

# 8. Candidate Evidence Cards

## C001 — Table 5 absolute difference does not reproduce from the displayed counts

**Candidate statement:** Table 5 prints an absolute unadjusted difference of 4.3% for two rows whose displayed counts and percentages yield approximately 4.4 percentage points under the ordinary raw-proportion calculation and nearest one-decimal rounding. **Pending Human Adjudication**.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [jama_flint_2019_oi_190079.pdf — PDF p. 9](<../jama_flint_2019_oi_190079.pdf#page=9>), Table 5, total-cholesterol and LDL rows.

**Source evidence:** Each cited row prints 9/64 (14.1%) for sertraline plus olanzapine and 6/62 (9.7%) for sertraline plus placebo. Each prints `4.3 (-8 to 17.2)` in the “Absolute Unadjusted Difference Between Groups, % (95% CI)” column.

**Reported-versus-comparator:** Reported point value: 4.3%. Comparator: the first displayed raw proportion minus the second, `(9/64 − 6/62) × 100`, and independently `14.1 − 9.7` percentage points.

**Reasoning procedure:** Under the table's “absolute unadjusted difference” label, compare the printed point value with the raw difference calculated from the displayed event counts and group-size headers. The source does not specify a different point estimator, denominator, or rounding convention.

**Calculation:** `9/64 = 14.0625%` and `6/62 = 9.677419%`; `(9/64 − 6/62) × 100 = 4.38508065` percentage points, which is 4.4 to one decimal under nearest rounding. The displayed rounded percentages also give `14.1 − 9.7 = 4.4`. The gap from the printed 4.3 is about 0.085 percentage point, exceeding a half-unit one-decimal rounding interval of 0.05.

**Alternative source-grounded interpretations:** The source may have used truncation, undocumented row-specific denominators, a different estimator, or unprinted analysis-population inputs. The cited table does not identify any such basis. The repeated value could also be an intentional reuse of one result, but that does not establish how 4.3 was obtained.

**Mechanical evidence recheck:** Direct PDF inspection found the cited table, counts, percentages, group sizes, repeated 4.3 point value, and interval. The raw calculation reproduced. Available inputs are sufficient for the ordinary raw difference; missing inputs are the estimator, rounding convention, and any row-specific denominators. Direct observation is separated from possible production explanations in [evidence_recheck.md](<review_1_5_1/verification/evidence_recheck.md>).

**Quality-control relevance:** A printed absolute difference that does not reproduce under the displayed raw-proportion rule is a preventable reporting-consistency issue worth human verification.

**Potential downstream evidence impact:** If confirmed, a data extractor, systematic reviewer, or meta-analyst could copy the displayed absolute difference rather than a value reproducible from the table's stated counts. This report does not assert that this has happened or that it changes any conclusion.

**Human verification steps:** Inspect the production table or analysis output; determine whether the point value used truncation, a row-specific denominator, or a defined non-raw estimator; then document the intended display rule without assuming a replacement value.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — HbA1c interaction is labelled with a concentration unit while matched displays use percent

**Candidate statement:** The same HbA1c daily treatment-by-time estimate is labelled `mg/dL` in two main-article locations, whereas matched table and longitudinal figure displays label HbA1c as percent. **Pending Human Adjudication**.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [jama_flint_2019_oi_190079.pdf — PDF p. 1](<../jama_flint_2019_oi_190079.pdf#page=1>), abstract Results; [jama_flint_2019_oi_190079.pdf — PDF p. 7](<../jama_flint_2019_oi_190079.pdf#page=7>), Secondary Outcomes; [jama_flint_2019_oi_190079.pdf — PDF p. 8](<../jama_flint_2019_oi_190079.pdf#page=8>), Table 4; and [joi190079supp2_prod.pdf — PDF p. 9](<../joi190079supp2_prod.pdf#page=9>), eFigure 8.

**Source evidence:** Main-article pages 1 and 7 print the HbA1c daily treatment-by-linear-time result as `−0.0002 mg/dL` (95% CI, `−0.0021 to 0.0016`); page 7 reports adjusted `P = .99`. Table 4 labels the outcome `HbA1c, %`, and eFigure 8 labels its axis `HbA1c (%)` for the matched mixed-model display.

**Reported-versus-comparator:** Reported label: `mg/dL` for the repeated interaction coefficient and interval. Comparator labels: `%` in Table 4 and `HbA1c (%)` in eFigure 8 for the same named outcome.

**Reasoning procedure:** Compare unit/scale labels across matched appearances of the named HbA1c outcome, treatment comparison, and longitudinal time scale. A compatible alternative would require a source-defined transformation or a distinct concentration-scale outcome.

**Calculation:** This is a label comparison, not a numeric conversion. The coefficient and interval match exactly across pages 1 and 7. No conversion between `mg/dL` and `%`, or definition of a distinct transformed HbA1c variable, is supplied.

**Alternative source-grounded interpretations:** The repeated `mg/dL` label could be a production carryover from surrounding metabolic measures. Alternatively, the model may have used a transformed outcome whose unit was not defined. The supplied sources do not distinguish these possibilities or establish an intended replacement label.

**Mechanical evidence recheck:** Direct PDF inspection confirmed the repeated main-text label and estimate, Table 4 percent label, and eFigure 8 percent axis. The logical comparison reproduced; necessary labels are available, while the coefficient's intended dimensional unit and any transformation/conversion are missing. See [evidence_recheck.md](<review_1_5_1/verification/evidence_recheck.md>).

**Quality-control relevance:** Conflicting measure labels can cause a quantitative effect to be classified on the wrong scale during evidence extraction.

**Potential downstream evidence impact:** If confirmed, an extractor, systematic review, meta-analysis, or guideline evidence table could copy or classify the HbA1c effect using an incompatible unit. This report does not assert that the model result, inference, or paper-level conclusion is wrong or that any downstream use occurred.

**Human verification steps:** Inspect the analysis-variable definition and production source; confirm whether the interaction used percent-scale HbA1c or a separately transformed variable; record its intended unit and transformation, if any, without inferring one from this report.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Protocol recruitment target conflicts between 82 and 98 participants per site

**Candidate statement:** Within the protocol/SAP, four sites recruiting 98 acute participants each reconcile with an acute total of 392, while another statement says each of four sites will recruit 82 patients without a stated population, phase, or version distinction. **Pending Human Adjudication**.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [joi190079supp1_prod.pdf — PDF p. 7](<../joi190079supp1_prod.pdf#page=7>), Figure 1 and Section 3.9.1; [joi190079supp1_prod.pdf — PDF p. 17](<../joi190079supp1_prod.pdf#page=17>), Table 4; and [joi190079supp1_prod.pdf — PDF p. 21](<../joi190079supp1_prod.pdf#page=21>), Section 4.2.1.

**Source evidence:** Page 7 prints `Acute Phase (N=392)` and enrollment across four sites. Page 17 states that each site will recruit 98 acutely ill participants and randomize 44 remitted participants. Page 21 states that four research sites will each recruit 82 patients with the stated psychotic-depression population.

**Reported-versus-comparator:** Reported statement: 82 patients per site. Comparator: 98 acutely ill participants per site and total acute `N=392`, all within the same supplied protocol/SAP.

**Reasoning procedure:** For a common four-site acute recruitment plan, multiply each per-site target by four and compare with the stated total. Applicability is conditional on the statements referring to the same population, phase, and protocol version.

**Calculation:** `98 × 4 = 392`, reproducing the acute total. `82 × 4 = 328`, 64 below 392. The per-site values differ by `98 − 82 = 16`. The separate randomized target, `44 × 4 = 176`, agrees with the planned discontinuation RCT total and does not resolve the acute-recruitment mismatch.

**Alternative source-grounded interpretations:** The 82/site statement may describe an earlier or amended target, a human-subjects subset, or another denominator; 98/site may represent all acutely ill participants. None of the cited passages labels a distinct version, subset, phase, or time basis that resolves the difference.

**Mechanical evidence recheck:** Direct PDF inspection confirmed the four-site, 392-total, 98/site, 82/site, and 44/site statements. The arithmetic reproduced. Necessary numerical inputs are available; the missing inputs are a version history and an explicit population/phase/subset definition. See [evidence_recheck.md](<review_1_5_1/verification/evidence_recheck.md>).

**Quality-control relevance:** Conflicting planned recruitment totals can affect accurate reporting and extraction of a protocol's denominators or per-site recruitment target.

**Potential downstream evidence impact:** If confirmed, an extractor or evidence synthesis could copy an inconsistent planned recruitment denominator or site target. This report does not imply a defect in observed participant flow, final randomized analysis, paper-level conclusion, or any actual downstream propagation.

**Human verification steps:** Review protocol version control, amendments, and the recruitment-population definitions for pages 7, 17, and 21; establish whether the counts refer to different targets and, if not, identify the intended common target.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

# 9. Downstream Evidence-Chain Considerations

Small preventable reporting defects can matter to downstream evidence extraction when a reviewer, meta-analyst, guideline developer, or data curator copies a number, denominator, unit, or recruitment target. The potential is bounded to what could be copied if a candidate is confirmed. No claim is made that copying, propagation, conclusion change, or serious harm occurred.

# 10. Limitations and Missing Definitions

The full limitation record is retained in [limitations.md](<review_1_5_1/limitations.md>). In brief, scientific source coverage is complete, but C001 lacks a stated point-estimator/rounding/row-denominator definition; C002 lacks an intended unit or transformation definition; and C003 lacks a version, phase, time, or subset definition. Statistical records frequently lack exact SEs, test statistics, sidedness, interval construction, variance/covariance detail, multiplicity step positions, figure-band definitions, and simulation inputs. These absences limit deeper reconstruction but do not turn ordinary omissions into candidates.

# 11. Human Adjudication Checklist

1. Confirm the cited direct-PDF text and locations for each stable candidate.
2. Determine whether the stated comparator concerns the same population, time frame, model, and definition.
3. Review the missing definition or source record identified in each card.
4. Record validity, importance, action, initials, and notes only in the blank fields in that candidate's card.
5. Preserve the distinction between direct observation and a possible explanation; do not treat this quality-control report as a final correction.

# 12. Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

## Reproducibility and source integrity

The direct-source inventory, source hashes, reused-artifact hashes, source coverage ledger, coverage manifest, relationship inventories, checker records, candidate ledger, recheck, and quality audit are retained below [review_1_5_1](<review_1_5_1/>). Source evidence links in the candidate cards point to the supplied direct PDFs and end in truthful PDF page fragments. Direct-source and designated reused-artifact hash verification is finalized after Markdown assembly.

## Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | `run_state.md` |
| reuse_asset_curation | root/reuse_asset_curation | gpt-5.6-terra | medium | FRESH_SPAWN | `evidence_asset_inventory.md` |
| main_evidence_mapping | root/main_mapping | gpt-5.6-terra | medium | FRESH_SPAWN | `extraction/main_quantitative_evidence.md` |
| support_evidence_mapping | root/support_mapping_001 | gpt-5.6-terra | medium | FRESH_SPAWN | `parts/support_001_quantitative_evidence.md` |
| support_evidence_mapping | root/support_mapping_002 | gpt-5.6-terra | medium | FRESH_SPAWN | `parts/support_002_quantitative_evidence.md` |
| numeric_checks | root/numeric_review | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/numeric_consistency.md` |
| cross_source_checks | root/cross_source_review | gpt-5.6-terra | medium | FRESH_SPAWN | `checkers/cross_source_consistency.md` |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_1.md` |
| evidence_recheck | root/evidence_recheck | gpt-5.6-sol | high | FRESH_SPAWN | `verification/evidence_recheck.md` |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | `checkers/statistical_pass_2.md` |
| evidence_quality | root/quality_audit | gpt-5.6-sol | high | FRESH_SPAWN | `quality/evidence_quality_audit.md` |
| report_generation | root/report_generation | gpt-5.6-terra | medium | FRESH_SPAWN | `limitations.md` |

## Performance profile

- **Target basis:** Four supplied PDFs totaling 63 pages; 20 pages have reusable page-level extraction while 43 pages require fresh direct-source mapping, including one 42-page supplement with tables/figures. The package is smaller than the 102-page calibration package and has a lower fresh-extraction burden, but still requires four-source cross-document and two-pass statistical review.
- **Total source units:** 63
- **Fresh-source units:** 43
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-08-18T22:15:04Z
- **Finished UTC:** 2026-08-18T22:50:37Z
- **Observed elapsed minutes:** 35.6
- **Target status:** MET_TARGET
- **Exceedance causes:** None

## Token accounting and cost

Accounting uses authoritative response-level runtime/API usage through `Finished UTC`. This collaboration runtime exposed no authoritative token counts for the coordinator or any of the 11 specialists, so each manifested agent has an `UNAVAILABLE` ledger row with exact token fields left `__`; no text-length or tokenizer estimate was substituted. The 0 below is the known subtotal from available records, not a claim that the run consumed zero tokens. Cached input and cache-write counts are input subsets; reasoning tokens are an output subset and are not added again to total tokens. Amounts are token-only API-equivalent estimates under the pricing snapshot dated 2026-08-18, not invoices.

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Agents | Unavailable records | Input tokens | Cached input tokens | Cache-write tokens | Output tokens | Reasoning tokens | Total tokens | Known token cost (USD) | Estimated complete token cost (USD) | Status |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| gpt-5.6-sol | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| gpt-5.6-terra | 9 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0.000000 | __ | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

Per-agent details are retained in [token_usage_summary.md](<review_1_5_1/token_usage_summary.md>).
