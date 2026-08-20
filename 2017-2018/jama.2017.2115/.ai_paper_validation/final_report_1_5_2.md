# Quantitative Quality-Control Consistency Review: Lappe et al. 2017 Paper Package

> **Pending Human Adjudication:** This report records quality-control candidates from supplied-source consistency checks. It makes no validity, importance, action, correction, severity, or scientific-disposition decision.

## 1. Executive Quality-Control Summary

Fresh source-first processing of three supplied PDFs (28/28 pages) mapped 69 numeric relationships and 38 inferential-statistical relationships. Six distinct quantitative reporting quality-control candidates were registered and mechanically rechecked. Each remains **Pending Human Adjudication**. The review found no displayed-zero P value and did not create any candidate on that basis.

The candidates concern one participant-count contradiction, two protocol label/unit conflicts, two conditional statistical-reporting questions, and one figure-versus-narrative discontinuation mismatch. Small preventable reporting defects can matter when values, confidence intervals, units, or definitions are copied into later evidence extraction; this report does not assert that propagation, conclusion change, or harm occurred.

## 2. Package and Fresh-Processing Provenance

Only the three supplied direct PDFs were used as evidence: [jama_lappe_2017_oi_170019.pdf — PDF p. 1](<../jama_lappe_2017_oi_170019.pdf#page=1>), [joi170019supp1_prod.pdf — PDF p. 1](<../joi170019supp1_prod.pdf#page=1>), and [joi170019supp2_prod.pdf — PDF p. 1](<../joi170019supp2_prod.pdf#page=1>). Their before-run SHA-256 hashes are recorded in [source_hashes_before.sha256](<review_1_5_2/source_hashes_before.sha256>) and fresh source inventory in [source_inventory.md](<review_1_5_2/source_inventory.md>).

Fresh native and layout text was generated for all pages; result-relevant pages were rendered. Targeted CPU OCR was used only for DOC-003 PDF p. 6 heading-glyph corruption, while its usable body text and rendering remained the basis for reading. No old audit derivative, web source, Office conversion, GPU, or unsupplied source was used.

## 3. Scope, Complete Coverage, and Exclusions

The review covers numeric, denominator/proportion/total, inferential-statistical, cross-document, measure/label/scale, and rate-versus-count relationships in the supplied package. It does not conduct a broad clinical, methodology, novelty, misconduct, raw-data, or final-correction audit.

| Direct source | Role | Fresh mapped units |
|---|---|---:|
| `jama_lappe_2017_oi_170019.pdf` | Main article | 10/10 PDF pages |
| `joi170019supp1_prod.pdf` | Supporting protocol/design document | 12/12 PDF pages |
| `joi170019supp2_prod.pdf` | Supplementary figures/statistical material | 6/6 PDF pages |

All 28/28 direct-source pages were freshly mapped; reusable units were 0 and fresh-required units were 28. Reference/index-only pages were classified rather than treated as omitted result material. Full stage assignments are in [coverage_manifest.md](<review_1_5_2/coverage_manifest.md>).

## 4. Quantitative and Statistical Relationship Coverage

- Numeric relationship inventory: 69/69 (`N001`–`N069`) mapped and checked; see [numeric_relationship_inventory.md](<review_1_5_2/relationships/numeric_relationship_inventory.md>) and [numeric_consistency.md](<review_1_5_2/checkers/numeric_consistency.md>).
- Statistical relationship inventory: 38/38 (`S001`–`S038`) mapped; see [relationship_inventory.md](<review_1_5_2/statistics/relationship_inventory.md>).
- Statistical pass 1: 38/38 completed by a fresh independent high-effort specialist; see [statistical_pass_1.md](<review_1_5_2/checkers/statistical_pass_1.md>).
- Statistical pass 2: 38/38 completed by a different fresh independent high-effort specialist, including all six ledger records and recheck facts; see [statistical_pass_2.md](<review_1_5_2/checkers/statistical_pass_2.md>).
- Cross-source review: all 69 numeric and 38 statistical relationships plus 24 match clusters checked; see [cross_source_consistency.md](<review_1_5_2/checkers/cross_source_consistency.md>).

There was no review queue, count cap, or deferred subset.

## 5. Candidate Index

| ID | Category | Candidate statement | Status |
|---|---|---|---|
| C001 | Denominator, proportion, or total inconsistency | Table 2 placebo calcium `N=1994` exceeds the randomized placebo cohort. | Pending Human Adjudication |
| C002 | Measure, label, or scale inconsistency | The protocol’s ≥70-year vitamin-D “limit” reverses inequality direction. | Pending Human Adjudication |
| C003 | Measure, label, or scale inconsistency | The protocol changes the calcium target from 1200 mg/day to 1200 g/day. | Pending Human Adjudication |
| C004 | Statistical reporting inconsistency | A death-difference CI is discordant with counts under a labelled diagnostic calculation. | Pending Human Adjudication |
| C005 | Statistical reporting inconsistency | An outside-study vitamin-D difference CI includes zero while printed P=.002. | Pending Human Adjudication |
| C006 | Cross-document numeric inconsistency | Figure 1 discontinuation counts conflict with a p.7 total and percentages. | Pending Human Adjudication |

## 6. Candidate Evidence Cards

## C001 — Table 2 placebo calcium `N=1994` exceeds the randomized placebo cohort

**Candidate statement:** The Table 2 placebo calcium participant count is larger than the entire reported randomized placebo cohort under the printed participant-count label. Status: Pending Human Adjudication.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_lappe_2017_oi_170019.pdf — PDF p. 5](<../jama_lappe_2017_oi_170019.pdf#page=5>), Table 2, outside-study calcium row; [PDF p. 1](<../jama_lappe_2017_oi_170019.pdf#page=1>) abstract and [PDF p. 4](<../jama_lappe_2017_oi_170019.pdf#page=4>) Figure 1 for placebo randomization.

**Source evidence:** Table 2 prints placebo `N=1994`, mean 512 (489 to 536) mg/d, versus treatment `N=1099`, mean 500 (475 to 525) mg/d. The paper prints 1147 randomized placebo participants; the adjacent placebo outside-study vitamin-D row prints `N=1094`.

**Reported-versus-comparator:** Reported placebo calcium `N=1994` versus reported placebo randomized total `N=1147`, a difference of 847.

**Reasoning procedure:** A cell headed “No. of Participants” for a participant-level placebo-group mean cannot exceed the reported placebo cohort absent a supplied different-unit definition.

**Calculation:** `1994 − 1147 = 847`; separately, `500 − 512 = −12.0` mg/d, which reproduces the printed mean difference but does not resolve the count mismatch.

**Alternative source-grounded interpretations:** The value may be a transposition, with adjacent `1094` one possible numerical explanation, or it may intentionally count another unit despite the header. The supplied PDFs establish neither explanation.

**Mechanical evidence recheck:** [evidence_recheck.md](<review_1_5_2/verification/evidence_recheck.md>) found the cited cell, comparator, header, adjacent row, and arithmetic at the direct-PDF pages.

**Quality-control relevance:** A participant count is a core denominator/label field for descriptive-table interpretation and extraction.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy an incorrect participant count or its implied analysis population into a systematic-review evidence table; no propagation is asserted.

**Human verification steps:** Check the Table 2 production proof or source data, determine whether the cell counts unique participants, and verify the intended placebo calcium count.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Protocol’s ≥70-year vitamin-D “limit” has the opposite inequality direction

**Candidate statement:** The protocol’s coordinated vitamin-D limiting instruction uses an upper bound for age <70 and a lower bound for age ≥70. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi170019supp1_prod.pdf — PDF p. 7](<../joi170019supp1_prod.pdf#page=7>), section 5, “Intervention.”

**Source evidence:** The sentence asks participants to “limit” outside vitamin D to “no more than 400 IU/day” if age <70 and “to more than 600 IU/day” if age ≥70.

**Reported-versus-comparator:** The reported ≥70 phrase `more than 600 IU/day` versus the paired limiting phrase `no more than 400 IU/day` and governing word “limit.”

**Reasoning procedure:** “No more than” defines an upper bound; “more than” defines a lower bound. Coordinated limits require an explicit different purpose to reverse direction.

**Calculation:** Age <70: outside vitamin D `≤400 IU/day`; age ≥70: outside vitamin D `>600 IU/day`. This is a direct inequality-direction comparison, not a rounding calculation.

**Alternative source-grounded interpretations:** “No more than 600 IU/day” may have been intended, or the older-group clause may intentionally state a distinct minimum. The supplied PDFs do not resolve the purpose or intended limit.

**Mechanical evidence recheck:** [evidence_recheck.md](<review_1_5_2/verification/evidence_recheck.md>) matched both clauses and the governing sentence at PDF p. 7.

**Quality-control relevance:** Directional symbols and limiting language define intervention/exposure instructions and their extractable dose constraints.

**Potential downstream evidence impact:** If confirmed, a protocol extractor could copy the wrong permitted vitamin-D direction or threshold into an intervention description; no downstream use is asserted.

**Human verification steps:** Consult the protocol source or trial operations documentation to establish whether the older-age clause is an upper limit, a distinct minimum, or a production error.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Protocol changes the calcium target unit from 1200 mg/day to 1200 g/day

**Candidate statement:** The same protocol paragraph presents 1200 mg/day as the regimen and 1200 g/day as the purported matching supplementation level. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi170019supp1_prod.pdf — PDF p. 7](<../joi170019supp1_prod.pdf#page=7>), section 5, “Intervention.”

**Source evidence:** The page specifies calcium `1200 mg/d` and two `600 mg` caplets daily, then states recommended intake was “1,200 g/day ... the level of supplementation that we are including.”

**Reported-versus-comparator:** Reported `1,200 g/day` versus the stated regimen of `600 mg × 2/day = 1200 mg/day = 1.2 g/day`.

**Reasoning procedure:** Exact mass-unit conversion compares the purported matching intake with the daily caplet regimen.

**Calculation:** `600 mg × 2/day = 1200 mg/day = 1.2 g/day`; `1200 g/day = 1,200,000 mg/day`, 1000-fold larger than 1200 mg/day.

**Alternative source-grounded interpretations:** The latter text may have intended `1,200 mg/day` or `1.2 g/day`; the supplied PDFs do not establish a correction.

**Mechanical evidence recheck:** [evidence_recheck.md](<review_1_5_2/verification/evidence_recheck.md>) matched the regimen, two unit strings, and conversion inputs at PDF p. 7.

**Quality-control relevance:** Dose units are central to intervention labeling, comparison, and evidence extraction.

**Potential downstream evidence impact:** If confirmed, an evidence table or protocol summary could copy a materially wrong calcium unit or dose scale; no propagation is asserted.

**Human verification steps:** Check the protocol production source and dosing records to determine the intended unit in the recommended-intake sentence.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Death-difference confidence interval is discordant with printed flow counts under a labelled diagnostic calculation

**Candidate statement:** The printed death-difference CI upper endpoint appears discordant with the printed flow counts under an explicitly labelled ordinary unpooled-binomial Wald diagnostic. Status: Pending Human Adjudication.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [jama_lappe_2017_oi_170019.pdf — PDF p. 4](<../jama_lappe_2017_oi_170019.pdf#page=4>), Figure 1 and adjacent results narrative.

**Source evidence:** The page prints 7 treatment and 9 placebo deaths among 1156 and 1147 randomized participants, death difference `.002`, and 95% CI `−.006 to .037`.

**Reported-versus-comparator:** Reported CI `−.006 to .037` versus the printed counts evaluated under the labelled diagnostic; the point difference itself is compatible with the counts.

**Reasoning procedure:** Reproduce placebo minus treatment and use an ordinary unpooled-binomial Wald interval only as a diagnostic; it is not claimed to be the paper’s reported CI method.

**Calculation:** `9/1147 − 7/1156 = .001791`, compatible with `.002`. Diagnostic `SE = .003463`; nominal 95% interval is approximately `−.0050 to .0086`, while the reported upper endpoint is `.037`.

**Alternative source-grounded interpretations:** `.037` may be a transcription/typesetting endpoint, or the reported interval may use a nonstandard method, population, or contrast orientation not supplied in the package. No correction is established.

**Mechanical evidence recheck:** [evidence_recheck.md](<review_1_5_2/verification/evidence_recheck.md>) matched counts, denominators, point difference, CI, and reproduced the labelled diagnostic.

**Quality-control relevance:** Confidence intervals and their accompanying event counts are routinely extracted statistical fields; this candidate is conditional on the absent reported CI method.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a discordant death CI or use it in a quantitative summary; no conclusion change or propagation is asserted.

**Human verification steps:** Recompute the death-proportion CI from the analysis dataset using the reported method, population, and contrast orientation; then compare the production endpoint.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Outside-study vitamin-D difference CI includes zero while printed P=.002

**Candidate statement:** One Table 2 contrast prints a two-sided P=.002 while its reported 95% CI includes zero; compatibility is conditional on the CI and P referring to the same contrast and procedures. Status: Pending Human Adjudication.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [jama_lappe_2017_oi_170019.pdf — PDF p. 5](<../jama_lappe_2017_oi_170019.pdf#page=5>), Table 2, outside-study vitamin D3 intake (visits 2–9) row.

**Source evidence:** Treatment `N=1099`, 740 (691 to 789) IU/d; placebo `N=1094`, 869 (803 to 934) IU/d; between-group difference `−128.1` with 95% CI `−209.5 to 46.6`, `P=.002`.

**Reported-versus-comparator:** Reported CI `−209.5 to 46.6`, which includes zero, versus reported two-sided `P=.002` in the same contrast row.

**Reasoning procedure:** A corresponding same-contrast two-sided 95% CI and two-sided null test ordinarily cannot pair null inclusion with P=.002. The source does not supply the Table 2 CI/test/variance mapping, so the premise remains conditional.

**Calculation:** `740 − 869 = −129`, compatible with `−128.1`. The ordered interval contains both `−128.1` and zero. Changing only the upper sign to `−46.6` gives a normal diagnostic near `.002`, but that explanatory observation is not a correction.

**Alternative source-grounded interpretations:** A missing minus sign is plausible, or the CI and P may be non-corresponding under an unreported method. The supplied package does not choose between them.

**Mechanical evidence recheck:** [evidence_recheck.md](<review_1_5_2/verification/evidence_recheck.md>) visually and textually confirmed that the printed upper endpoint has no minus sign, and matched the same-row P value.

**Quality-control relevance:** Paired effect, CI, and P-value fields can be extracted together; their interpretive compatibility depends on documented methods.

**Potential downstream evidence impact:** If confirmed, a reviewer could copy an internally discordant CI/P pair into a quantitative evidence table or meta-analytic data check; no use or conclusion change is asserted.

**Human verification steps:** Inspect the Table 2 analysis output and production proof, identify the CI/test construction and sidedness, and verify the printed upper endpoint.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Figure 1 discontinuation counts conflict with p.7 vitamin-D/placebo discontinuation total and percentages

**Candidate statement:** Figure 1 reports 484 intervention discontinuations while a later narrative reports 304 participants stopping vitamin D or placebo; the construct match remains conditional because the figure label is not defined. Status: Pending Human Adjudication.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_lappe_2017_oi_170019.pdf — PDF p. 4](<../jama_lappe_2017_oi_170019.pdf#page=4>), Figure 1; [PDF p. 7](<../jama_lappe_2017_oi_170019.pdf#page=7>), discontinuation narrative.

**Source evidence:** Figure 1 prints 238 and 246 “Discontinued intervention” participants with components 11+93+134 and 16+76+154. Page 7 prints 304 participants (13.2%; 12.4% treatment and 14.0% placebo) stopped vitamin D or placebo.

**Reported-versus-comparator:** Figure total `238 + 246 = 484` versus narrative total `304` with stated arm percentages.

**Reasoning procedure:** Compare matched trial, arm, and follow-up statements while retaining the unresolved possibility that Figure 1 uses a broader intervention-discontinuation event definition.

**Calculation:** `11+93+134=238`; `16+76+154=246`; `238+246=484`. The narrative percentages are compatible with about `143/1156=12.4%` and `161/1147=14.0%`; `143+161=304`. Rounding cannot reconcile 484 and 304.

**Alternative source-grounded interpretations:** Figure 1 may include stopping either study component, a different time window, or another status rule; alternatively, one display may be erroneous. The supplied PDFs do not define the difference.

**Mechanical evidence recheck:** [evidence_recheck.md](<review_1_5_2/verification/evidence_recheck.md>) matched figure components, narrative total/percentages, denominators, and the 484-versus-304 arithmetic.

**Quality-control relevance:** Discontinuation counts and definitions affect exposure/adherence descriptions and may be compared across figures and narratives.

**Potential downstream evidence impact:** If confirmed, an extractor could copy a discontinuation count or definition that is not comparable across displays; no propagation or effect on conclusions is asserted.

**Human verification steps:** Obtain the Figure 1 event-definition and source counts, compare its supplement components, time window, and counting rule with the p.7 endpoint, and verify which values describe each construct.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## 7. Downstream Evidence-Chain Considerations

If confirmed after human review, the identified fields could affect what a systematic review, meta-analysis, guideline evidence table, or data extractor records: a participant denominator, intervention limit, dose unit, confidence interval/P-value pair, or discontinuation definition. This is a generic extraction-risk statement only. The supplied package does not show that any field propagated, that a meta-analysis used it, or that a study conclusion changed.

## 8. Limitations and Missing Definitions

The complete bounded limitations record is in [limitations.md](<review_1_5_2/limitations.md>). In particular, raw data and production files are absent; Table 2 CI/test mappings, the death-CI construction, and the Figure 1 discontinuation definition are not supplied. These absences prevent adjudication or correction but do not remove the registered candidates.

## 9. Human Adjudication Checklist

For each candidate, a qualified human reviewer should: confirm direct-PDF location and transcription; retrieve the applicable production, protocol, or analysis source; verify population, unit, time window, contrast, and method; determine whether an alternative source-grounded definition resolves the mismatch; document any action outside this report; and complete the five blank fields in that card. All six records remain Pending Human Adjudication until that process occurs.

## 10. Reproducibility, Source-Integrity, and Agent-Execution Metadata

### Reproducibility and source integrity

Fresh processing is documented in [evidence_asset_inventory.md](<review_1_5_2/evidence_asset_inventory.md>), complete unit coverage in [source_coverage.md](<review_1_5_2/source_coverage.md>), and pre-run hashes in [source_hashes_before.sha256](<review_1_5_2/source_hashes_before.sha256>). The three direct PDFs had SHA-256 values: DOC-001 `af73f4f45ba4d330b06c21d0ac4a54c9069641578aa7a5f8063f4160af49c34d`; DOC-002 `a2782a096e4690f29d9fefa4522d19745b42dc047da7ae00c142f6bad6736d69`; DOC-003 `4c6200e596fdd764522785ef39e620cc6fb0ea725877a9339edbc829bf32fab2`. Final direct recomputation matched all three pre-run hashes, so source integrity was unchanged.

### Agent execution

The execution manifest is [agent_execution_manifest.md](<review_1_5_2/agent_execution_manifest.md>). It records `root` (gpt-5.6-sol, high); `root/fresh_preprocessing`, `root/main_mapper`, `root/support_mapper`, `root/numeric_checker`, `root/cross_source_checker`, and `root/report_generator` (gpt-5.6-terra, medium); `root/statistics_pass_1` and `root/statistics_pass_2` (distinct gpt-5.6-terra, high, fresh-spawn statistical passes); and `root/evidence_rechecker` and `root/quality_auditor` (gpt-5.6-sol, high).

## 11. Performance Metadata

- **Target basis:** Three direct PDF sources comprising one 10-page main article and two support documents of 12 and 6 pages; all 28 unique PDF pages require fresh native and layout extraction, result-relevant visual inspection/rendering, complete main/support quantitative mapping, three parallel first-line consistency lanes, two fresh high-effort statistical passes, full candidate recheck, evidence-quality audit, and complete report generation. No Office conversion is required and all direct tools are locally available.
- **Total source units:** 28
- **Fresh-source units:** 28
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-08-20T16:53:39Z
- **Finished UTC:** 2026-08-20T17:28:23Z
- **Observed elapsed minutes:** 34.7
- **Target status:** MET_TARGET
- **Exceedance causes:** None

## 12. Token-Usage and Cost Metadata

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Agents | Input tokens | Output tokens | Total tokens | Known token-only API-equivalent estimate (USD) | Status |
|---|---:|---:|---:|---:|---:|---|
| gpt-5.6-sol | 3 | 0 | 0 | 0 | 0.000000 | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| gpt-5.6-terra | 8 | 0 | 0 | 0 | 0.000000 | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

The finalized [token_usage_summary.md](<review_1_5_2/token_usage_summary.md>) provides per-agent detail. The runtime exposed no authoritative response-level token counts for the coordinator or specialists, so each manifested agent has an `UNAVAILABLE` row and the known token count of 0 is not a complete package count. No count was inferred from text length. Cached input and cache-write counts are input subsets, and reasoning is an output subset, not additional total tokens. Amounts are token-only API-equivalent estimates under the 2026-08-18 pricing snapshot, not invoices.
