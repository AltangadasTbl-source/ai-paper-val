# Quantitative Quality-Control Consistency Review

## Pending Human Adjudication

Every listed item remains **Pending Human Adjudication**. This is a neutral quantitative reporting quality-control review; it assigns no severity, validity decision, correction, acceptance, rejection, or exclusion.

## Executive Quality-Control Summary

Fresh source-first review of all three supplied PDFs identified **8** distinct, mechanically rechecked candidates, C001–C008. They concern a direction word, unit label, arithmetic/rounding, interval scale, proportion/count alignment, cross-document centre count, and endpoint-definition alignment. This report does not state that any result, conclusion, or downstream product changed.

## Package and Fresh-Processing Provenance

Direct sources were [jama_jabre_2018_oi_180004.pdf — PDF p. 1](<../jama_jabre_2018_oi_180004.pdf#page=1>) (DOC-001; 9 pages; SHA-256 `114e922542bbb1f8369ca9b5c19be65d93856e16cf4ff295c483439e4e208839`), [joi180004supp1_prod.pdf — PDF p. 1](<../joi180004supp1_prod.pdf#page=1>) (DOC-002; 134 pages; SHA-256 `70106d31b08e3a9d7eaac8a0e035bbf8d92a43b51f2483b634d7349b0c5f6913`), and [joi180004supp2_prod.pdf — PDF p. 1](<../joi180004supp2_prod.pdf#page=1>) (DOC-003; 3 pages; SHA-256 `937e18794fc87074907b1e9ab792f9a35d2f2d895d586dd27e7cbf44d5ed8d46`). All evidence was freshly processed from supplied PDFs. Fresh CPU OCR was restricted to DOC-002 pages 52 and 103; no legacy OCR or audit derivative was evidence.

## Scope, Complete Coverage, and Exclusions

All **3/3** sources and **146/146** PDF pages were fresh-required and mapped: DOC-001 9/9, DOC-002 134/134, DOC-003 3/3; reusable units were zero. Blank/result-irrelevant DOC-002 pages 108–109 and 126–134 remain counted and mapped. The review covers quantitative/statistical consistency only and excludes broad clinical, conduct, design, misconduct, raw-data, and external-literature audit.

## Quantitative and Statistical Relationship Coverage

The numeric inventory covers **N001–N051 (51/51)**. The statistical inventory covers **S001–S038 (38/38)**; independent statistical pass 1 and pass 2 each completed every relationship, and pass 2 revisited C001–C008 plus recheck facts. No `P = 0` or equivalent display occurred; `P<.001` is an inequality display, not a display-zero candidate.

## Candidate Index

| ID | Candidate | Category |
|---|---|---|
| C001 | Noninferiority narrative reverses displayed bound direction | Statistical reporting inconsistency |
| C002 | Centre-5 pause contrast mixes count outcome with seconds | Measure, label, or scale inconsistency |
| C003 | PP survival difference does not round from printed inputs | Numeric or arithmetic inconsistency |
| C004 | PP survival CI has unresolved scale/precision inconsistency | Statistical reporting inconsistency |
| C005 | PP ROSC ETI percentage conflicts with count and difference | Denominator, proportion, or total inconsistency |
| C006 | Main article and eTable have different contributing-centre counts | Cross-document numeric inconsistency |
| C007 | Published endpoint description omits amended qualification | Measure, label, or scale inconsistency |
| C008 | Protocol technique-failure definition conditionally conflicts with article row | Measure, label, or scale inconsistency |

## Candidate Evidence Cards

## C001 — Noninferiority narrative reverses the displayed bound direction

**Candidate statement:** The narrative calls a lower CI limit greater than the threshold although the displayed lower limit is below it; the printed conclusion remains compatible with the displayed values.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [jama_jabre_2018_oi_180004.pdf — PDF p. 3](<../jama_jabre_2018_oi_180004.pdf#page=3>) (rule); [jama_jabre_2018_oi_180004.pdf — PDF p. 4](<../jama_jabre_2018_oi_180004.pdf#page=4>) (result/narrative).

**Source evidence:** Noninferiority requires a BMV-minus-ETI lower endpoint greater than `-1.00%`; the result prints `-1.64%` and says it was “greater than the threshold,” then says noninferiority was not demonstrated.

**Reported-versus-comparator:** Reported “greater”; comparator `-1.64%` versus `-1.00%` under the stated strict rule.

**Reasoning procedure:** Compare the printed endpoint and threshold separately from the printed conclusion.

**Calculation:** `-1.64% < -1.00%`; difference `-0.64` percentage points.

**Alternative source-grounded interpretations:** A direction word may be reversed or omitted; intended replacement wording is not supplied, while the conclusion is source-consistent.

**Mechanical evidence recheck:** The rule, endpoint, word, and conclusion were found at the cited pages; no additional input is required.

**Quality-control relevance:** Direction wording beside a noninferiority decision rule can misstate the CI-margin comparison.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an incorrect directional explanation; no propagation or conclusion change is asserted.

**Human verification steps:** Confirm intended wording against the publication record while retaining or reassessing the printed conclusion.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Centre-5 pause contrast mixes a count outcome with seconds

**Candidate statement:** A contrast for the number of qualifying pauses is labelled in seconds.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [jama_jabre_2018_oi_180004.pdf — PDF p. 3](<../jama_jabre_2018_oi_180004.pdf#page=3>) (definition); [jama_jabre_2018_oi_180004.pdf — PDF p. 4](<../jama_jabre_2018_oi_180004.pdf#page=4>) (contrast).

**Source evidence:** The outcome is the “number of pauses” lasting more than 2 seconds; BMV is `27`, ETI `16`, and the difference is printed as `11 seconds` (95% CI `7 to 15`).

**Reported-versus-comparator:** Reported `11 seconds`; comparator is a difference in the stated number of qualifying pauses.

**Reasoning procedure:** Preserve the outcome wording and subtract the printed group values without inferring a summary type.

**Calculation:** `27 - 16 = 11` qualifying pauses under the printed wording.

**Alternative source-grounded interpretations:** The source does not say whether values are totals, means, medians, or another summary; a time interpretation conflicts with “number of pauses.”

**Mechanical evidence recheck:** Definition, values, interval, and seconds label were confirmed; summary type and interval method remain missing.

**Quality-control relevance:** A count-versus-duration label changes a subgroup contrast’s meaning.

**Potential downstream evidence impact:** If confirmed, an extractor could record a duration effect where a count outcome is named; no downstream use is claimed.

**Human verification steps:** Determine the summary type and intended unit for the contrast and interval.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — PP day-28 survival point difference does not round from the printed inputs

**Candidate statement:** The PP survival difference `0.1` percentage points does not ordinarily round from the displayed counts and denominators.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [jama_jabre_2018_oi_180004.pdf — PDF p. 6](<../jama_jabre_2018_oi_180004.pdf#page=6>) (Table 2); [joi180004supp1_prod.pdf — PDF p. 123](<../joi180004supp1_prod.pdf#page=123>) (rounding rule).

**Source evidence:** BMV is `54/995 (5.4%)`, ETI `51/943 (5.4%)`, and BMV-minus-ETI is `0.1` percentage points.

**Reported-versus-comparator:** Reported `0.1`; comparator from printed inputs is `0.0189` percentage points, ordinarily `0.0` to one decimal.

**Reasoning procedure:** Calculate the conditional unadjusted point difference and apply the supplied one-decimal convention.

**Calculation:** `100 × (54/995 - 51/943) = 0.0189` percentage points, rounding to `0.0`.

**Alternative source-grounded interpretations:** An unstated retained estimator, denominator, adjustment, weighting, or rounding procedure could explain the display; no correction is adjudicated.

**Mechanical evidence recheck:** Counts, denominators, displayed values, and support rounding statement were confirmed.

**Quality-control relevance:** A point difference not reproduced from its displayed inputs can affect extraction.

**Potential downstream evidence impact:** If confirmed, a reviewer could copy the displayed difference rather than a count-derived comparison; no propagation is asserted.

**Human verification steps:** Identify the row-level estimator and inputs producing `0.1`, or determine whether the display requires amendment.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — PP day-28 survival confidence interval has an unresolved scale/precision inconsistency

**Candidate statement:** The PP survival interval in a percentage-point column has a scale/precision appearance unresolved by supplied row-level methods or inputs.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [jama_jabre_2018_oi_180004.pdf — PDF p. 3](<../jama_jabre_2018_oi_180004.pdf#page=3>) (rule); [PDF p. 6](<../jama_jabre_2018_oi_180004.pdf#page=6>) (Table 2); [joi180004supp1_prod.pdf — PDF p. 124](<../joi180004supp1_prod.pdf#page=124>) (CI rule).

**Source evidence:** The column prints difference `0.1`, 95% CI `-10 to 9.7`, and `P=.99` for `54/995` versus `51/943`.

**Reported-versus-comparator:** Reported interval `-10 to 9.7` percentage points; diagnostic ordinary unpooled-binomial comparator is about `-2.00 to 2.04` points.

**Reasoning procedure:** Use printed counts only for a labelled diagnostic scale comparison; do not reconstruct an unspecified source interval.

**Calculation:** Diagnostic SE `1.028756` points; with difference `0.018864`, Wald 95% interval `-1.997498 to 2.035226` points.

**Alternative source-grounded interpretations:** Nonstandard method, retained data, adjustment, correction, or decimal production issue may explain the display; exact construction is absent.

**Mechanical evidence recheck:** Recheck visually confirmed `-10`, not `-1.0`, and confirmed the stated rules; the diagnostic is not a replacement analysis.

**Quality-control relevance:** An interval scale/precision issue can alter recorded uncertainty.

**Potential downstream evidence impact:** If confirmed, an evidence product could copy the printed interval scale; no observed reuse or conclusion change is asserted.

**Human verification steps:** Obtain generated endpoints, units, method, precision process, and retained inputs.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — PP ROSC ETI percentage conflicts with its count, denominator, and signed difference

**Candidate statement:** The ETI PP ROSC percentage conflicts with its numerator/denominator and signed BMV-minus-ETI contrast.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [jama_jabre_2018_oi_180004.pdf — PDF p. 6](<../jama_jabre_2018_oi_180004.pdf#page=6>) (Table 2 PP ROSC row).

**Source evidence:** BMV `342/995 (34.4%)`, ETI `377/943 (30.0%)`, and BMV-minus-ETI `-5.6` points are printed.

**Reported-versus-comparator:** Reported ETI `30.0%`; `377/943 = 39.979%` (rounds `40.0%`), and count-derived contrast is negative while displayed percentages imply positive.

**Reasoning procedure:** Independently calculate ETI rate and BMV-minus-ETI contrast from displayed counts/denominators.

**Calculation:** `100 × 377/943 = 39.979%`; `100 × (342/995 - 377/943) = -5.607` points, matching `-5.6`; printed percentages give `+4.4` points.

**Alternative source-grounded interpretations:** The source does not establish which printed value or retained estimator was intended; no correction is adjudicated.

**Mechanical evidence recheck:** All row values and arithmetic/sign comparison were confirmed.

**Quality-control relevance:** A proportion inconsistent with count, denominator, and direction can misstate group rate and effect direction.

**Potential downstream evidence impact:** If confirmed, extractors could copy an erroneous rate or direction; no observed downstream use is asserted.

**Human verification steps:** Verify retained analysis output and identify intended numerator, denominator, percentage, and contrast.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Main article and eTable report different contributing-centre counts

**Candidate statement:** The article reports 20 EMS centres whereas eTable 1 shows 21 contributing investigator-centre rows.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [jama_jabre_2018_oi_180004.pdf — PDF p. 2](<../jama_jabre_2018_oi_180004.pdf#page=2>); [joi180004supp2_prod.pdf — PDF p. 2](<../joi180004supp2_prod.pdf#page=2>) (eTable 1).

**Source evidence:** Methods state 20 EMS centres (15 France, 5 Belgium); eTable 1 has 21 nonempty investigator-centre rows, whose arm totals reconcile to 1018 and 1022.

**Reported-versus-comparator:** Reported count `20`; comparator `21` displayed rows.

**Reasoning procedure:** Add country counts and count nonempty eTable rows without assuming a one-to-one mapping.

**Calculation:** `15 + 5 = 20`; eTable rows = `21`.

**Alternative source-grounded interpretations:** One EMS centre may map to multiple investigator-centre records; no crosswalk is supplied.

**Mechanical evidence recheck:** Main count, 21 rows, and eTable arm-total reconciliation were confirmed.

**Quality-control relevance:** Cross-document count units can be noncomparable.

**Potential downstream evidence impact:** If confirmed, an evidence product could copy an unmatched centre count; no propagation or conclusion effect is asserted.

**Human verification steps:** Obtain the centre-to-investigator-centre mapping and intended counting units.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Published primary-endpoint description omits the amended baseline-disability qualification

**Candidate statement:** The article’s CPC-1-or-2 endpoint description omits the amendment’s qualification for survivors with baseline neurologic disability.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [jama_jabre_2018_oi_180004.pdf — PDF p. 1](<../jama_jabre_2018_oi_180004.pdf#page=1>) and [PDF p. 3](<../jama_jabre_2018_oi_180004.pdf#page=3>); [joi180004supp1_prod.pdf — PDF p. 110](<../joi180004supp1_prod.pdf#page=110>).

**Source evidence:** Article: favourable outcome CPC 1 or 2. Amendment: a baseline-disabled survivor is favourable if survival retains the same disability degree.

**Reported-versus-comparator:** Reported CPC-1-or-2 description; comparator is the additional amendment qualification.

**Reasoning procedure:** Compare printed definitions and limit inference to potential classification difference.

**Calculation:** No aggregate calculation: a survivor can satisfy the amendment qualification without a literal CPC-1-or-2-only classification.

**Alternative source-grounded interpretations:** Article wording may be abbreviated or no participant may require the qualification; final coding and affected count are absent.

**Mechanical evidence recheck:** Both definitions were confirmed; no participant-level change was inferred.

**Quality-control relevance:** Omitted operative endpoint wording can affect outcome extraction.

**Potential downstream evidence impact:** If confirmed, reviewers could extract a narrower endpoint definition; no downstream use or conclusion change is asserted.

**Human verification steps:** Confirm final coding algorithm and whether any participant used the qualification.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Protocol composite technique-failure definition cannot reconcile with the article’s smaller ETI failure count if they are the same endpoint

**Candidate statement:** If the protocol composite and article Table 3 row denote the same endpoint and aligned population, aggregate displays cannot reconcile.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [joi180004supp1_prod.pdf — PDF p. 110](<../joi180004supp1_prod.pdf#page=110>); [jama_jabre_2018_oi_180004.pdf — PDF p. 1](<../jama_jabre_2018_oi_180004.pdf#page=1>), [PDF p. 4](<../jama_jabre_2018_oi_180004.pdf#page=4>), and [PDF p. 6](<../jama_jabre_2018_oi_180004.pdf#page=6>).

**Source evidence:** Amended protocol technique failure includes 28-day mortality, regurgitation, or failure to ventilate/intubate. Article prints ETI failure `21/996 (2.1%)` and ITT ETI deaths `54/1022`.

**Reported-versus-comparator:** Reported `21/996`; conditional conservative comparator is at least 27 before other composite components.

**Reasoning procedure:** Preserve conditional population/endpoint alignment and allow the maximum displayed exclusions before comparison.

**Calculation:** `54 - 24 - 3 = 27`, and `27 > 21`.

**Alternative source-grounded interpretations:** Article row may be narrower, use another final definition, or use actual-treatment population; aggregate displays do not establish participant alignment.

**Mechanical evidence recheck:** Definition, death total, flow values, and Table 3 row were confirmed; population/definition crosswalk remains missing.

**Quality-control relevance:** Undefined or mismatched outcome labels impede consistent cross-document comparison.

**Potential downstream evidence impact:** If confirmed, an extractor could treat nonaligned failure definitions as the same outcome; no observed propagation or conclusion change is asserted.

**Human verification steps:** Determine Table 3 definition, analysis population, and overlap with death, regurgitation, and procedural failure.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

Small preventable reporting defects can matter when systematic reviews, meta-analyses, guidelines, or other evidence products extract values, units, definitions, intervals, or centre counts. The report identifies only what could be copied if confirmed; it does not claim propagation, harm, or conclusion change.

## Limitations and Missing Definitions

Only supplied local PDFs and fresh assets were used. Aggregate evidence does not provide every row-level estimator, CI method, retained denominator, adjustment, participant classification, centre crosswalk, editorial history, or Table 3 failure-population definition. C004 is diagnostic only and C008 conditional. OCR is a transcription aid, while supplied PDFs/renderings are authoritative.

## Human Adjudication Checklist

- Check every card against its linked source pages and comparator.
- Resolve missing definitions or retained outputs before any action.
- Record human decisions only in each card’s `__` fields.
- Preserve stable IDs C001–C008 and distinguish a correction from this neutral review.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

Before/after source hashes are recorded in the fresh review directory. Inventory and coverage establish 3 direct PDFs, 146 total/fresh/mapped units, and zero reusable units; source-page assignments are in the coverage manifest.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | COORDINATOR-CURRENT-SESSION | gpt-5.6-sol | high | CURRENT_SESSION | run_state.md |
| fresh_source_preprocessing | root/fresh_preprocessing | gpt-5.6-terra | medium | FRESH_SPAWN | evidence_asset_inventory.md |
| main_quantitative_mapping | root/main_mapper | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapping_a | root/support_mapper_a | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_a_quantitative_evidence.md |
| support_quantitative_mapping_b | root/support_mapper_b | gpt-5.6-terra | medium | FRESH_SPAWN | extraction/parts/support_b_quantitative_evidence.md |
| numeric_checks | root/numeric_checker | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_checks | root/cross_source_checker | gpt-5.6-terra | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| evidence_recheck | root/evidence_rechecker | gpt-5.6-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-5.6-terra | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| evidence_quality | root/quality_auditor | gpt-5.6-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| evidence_quality_repair | root/quality_audit_repair | gpt-5.6-sol | high | FRESH_SPAWN | limitations.md |
| report_generation | root/report_generator | gpt-5.6-terra | medium | FRESH_SPAWN | report_generation.md |
| evidence_quality_repair | /root/quality_audit_repair | gpt-5.6-sol | high | FRESH_SPAWN | limitations.md |

### Performance

- **Target basis:** Three supplied PDFs totaling 146 pages: a 9-page main article, a 134-page support document with extensive tabular/protocol content, and a 3-page support document. All units require fresh extraction and mapping, the long support source may require targeted visual checks, and complete dual statistical passes plus mechanical recheck and quality audit are required.
- **Total source units:** 146
- **Fresh-source units:** 146
- **Target elapsed minutes:** 70-105
- **Started UTC:** 2026-08-24T01:55:18Z
- **Finished UTC:** 2026-08-24T03:03:02Z
- **Observed elapsed minutes:** 67.7
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

The coordinator will finalize these fields from [`token_usage_summary.md`](<review_1_5_2/token_usage_summary.md>) after capturing this report response. That artifact contains per-agent detail; cached/cache-write counts are input subsets and reasoning is an output subset. Final figures are token-only API-equivalent estimates under the dated price snapshot, not an invoice.

| Model | Agents | Input | Output | Total | Known token cost (USD) | Status |
|---|---:|---:|---:|---:|---:|---|
| gpt-5.6-sol | 4 | 0 | 0 | 0 | 0.000000 | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| gpt-5.6-terra | 9 | 0 | 0 | 0 | 0.000000 | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
