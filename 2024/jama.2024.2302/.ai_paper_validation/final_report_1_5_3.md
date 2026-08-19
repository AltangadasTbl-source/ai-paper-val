# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.5.3

## Pending Human Adjudication

Every candidate in this report is **Pending Human Adjudication**. This is a quantitative reporting quality-control review, not a determination about authors, validity of the paper, or the paper’s conclusions.

## Executive Quality-Control Summary

Complete uncapped coverage registered five stable reporting-consistency candidates: `C001` through `C005`. They concern endpoint thresholds, planned design values, prior descriptions, subgroup-boundary labels, and outcome-window terminology. Small preventable reporting defects can matter for downstream evidence extraction; the supplied package does not establish propagation, a conclusion change, or serious harm.

## Package and Reused-Evidence Provenance

The package comprises five direct sources: the main article (10 PDF pages), protocol (25 PDF pages), statistical analysis plan (10 PDF pages), results supplement (8 PDF pages), and a 237-paragraph auxiliary DOCX. Direct-source hashes and reused-asset hashes were recorded before review in [source_hashes_before.sha256](review_1_5_3/source_hashes_before.sha256) and [reused_artifact_hashes_before.sha256](review_1_5_3/reused_artifact_hashes_before.sha256). Reused native text and renders were location/transcription aids only; the supplied PDFs remained authoritative.

## Scope, Complete Coverage, and Exclusions

| Source | Total | Reusable | Fresh required | Mapped | Status |
|---|---:|---:|---:|---:|---|
| Main article PDF | 10 | 10 | 0 | 10 | Complete |
| Protocol PDF | 25 | 0 | 25 | 25 | Complete |
| Statistical analysis plan PDF | 10 | 0 | 10 | 10 | Complete |
| Results supplement PDF | 8 | 4 | 4 | 8 | Complete |
| Auxiliary DOCX paragraphs | 237 | 0 | 237 | 237 | Complete structural coverage; legacy assertions excluded from discovery |
| **Total** | **290** | **14** | **276** | **290** | **Complete** |

All mapped units are supported by the complete main/support scientific maps, including explicit no-applicable units and the required DOCX structural exclusion. Candidate discovery was uncapped and did not use older candidate content or external sources. A coherent display-zero P value was not a candidate; no mapped relationship used `P = 0`, `p = 0.000`, or equivalent notation.

## Quantitative and Statistical Relationship Coverage

- Numeric/reporting relationships: `N001`-`N041` (41 complete relationships).
- Statistical relationships: `S001`-`S020` (20 complete relationships).
- Cross-source review: 19 matched result/definition families across the four scientific PDFs.
- Statistical pass 1: fresh `gpt-5.6-terra` high-effort review of `S001`-`S020`; complete.
- Statistical pass 2: distinct fresh `gpt-5.6-terra` high-effort review of `S001`-`S020`, the complete ledger, and recheck facts; complete with no new candidate.

The relationship inventories and pass records are available in [numeric relationship inventory](review_1_5_3/relationships/numeric_relationship_inventory.md), [statistical relationship inventory](review_1_5_3/statistics/relationship_inventory.md), [statistical pass 1](review_1_5_3/checkers/statistical_pass_1.md), and [statistical pass 2](review_1_5_3/checkers/statistical_pass_2.md).

## Candidate Index

| ID | Category | Candidate |
|---|---|---|
| [C001](#c001--primary-sae-endpoint-threshold-label) | Measure, label, or scale inconsistency | `>1` versus `≥1`/“any” SAE threshold |
| [C002](#c002--planned-hospital-day-medians) | Cross-document numeric inconsistency | planned median hospital-day values |
| [C003](#c003--bayesian-intervention-priors) | Statistical reporting inconsistency | article/SAP intervention-prior ranges |
| [C004](#c004--gestational-age-boundary) | Measure, label, or scale inconsistency | `≥28` versus `>28` gestational-age boundary |
| [C005](#c005--primary-outcome-time-origin) | Measure, label, or scale inconsistency | enrollment versus randomization time origin |

## Candidate Evidence Cards

## C001 — Primary SAE endpoint threshold label

**Status:** Pending Human Adjudication

**Candidate statement:** Matched primary SAE results are labeled `≥1`/“any” in the main article and SAP but `>1` in the protocol and eTable.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [main article — PDF p. 6](<../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6>), Table 2; [results supplement — PDF p. 5](<../joi240020supp3_prod_1710443209.75411.pdf#page=5>), eTable 2; [protocol — PDF p. 2](<../joi240020supp1_prod_1710443209.74911.pdf#page=2>); [SAP — PDF p. 4](<../joi240020supp2_prod_1710443209.75411.pdf#page=4>).

**Source evidence:** Table 2 reports 44/159 and 27/149 as “Had ≥1 serious adverse event”; eTable 2 uses the same counts, percentages, and denominators under “Infant had > 1 SAE.”

**Reported-versus-comparator:** `≥1`, “at least 1,” and “any” include exactly one SAE; `>1` means at least two SAEs.

**Reasoning procedure:** Compare the printed threshold operators after matching population, arms, denominators, and results.

**Calculation:** `44/159 = 27.67%` (28%) and `27/149 = 18.12%` (18%). The differing sets are `{k: k ≥ 1}` and `{k: k > 1}`.

**Alternative source-grounded interpretations:** Repeated “any,” “at least one,” and `≥1` wording supports the possibility that `>1` was used informally for more than zero. The number with exactly one SAE is not supplied.

**Mechanical evidence recheck:** Direct-page recheck confirmed both operators and the matched counts; see [evidence recheck](review_1_5_3/verification/evidence_recheck.md#c001--primary-sae-endpoint-is-labeled-1-and-1any-for-matched-results).

**Quality-control relevance:** The endpoint label should identify the estimand associated with the reported counts.

**Potential downstream evidence impact:** If confirmed, a data extractor could copy the wrong SAE threshold alongside 44/159 and 27/149; no propagation or conclusion change is asserted.

**Human verification steps:** Determine the executable endpoint rule and whether any location requires correction, clarification, or version qualification.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Planned hospital-day medians

**Status:** Pending Human Adjudication

**Candidate statement:** Protocol/SAP locations print incompatible arm-specific planned median hospital-day values.

**Category:** Cross-document numeric inconsistency

**Exact source locations:** [protocol — PDF p. 3](<../joi240020supp1_prod_1710443209.74911.pdf#page=3>); [protocol — PDF p. 12](<../joi240020supp1_prod_1710443209.74911.pdf#page=12>); [SAP — PDF p. 3](<../joi240020supp2_prod_1710443209.75411.pdf#page=3>).

**Source evidence:** Protocol p. 3 gives planned medians 18 early/15 late; p. 12 gives medians 8/5 and means 18/13. The SAP explicitly calls the p. 3 18/15 medians incorrect and identifies 8/5 as intended.

**Reported-versus-comparator:** Planned median pairs 18/15 versus 8/5 days for the same early/late contrast.

**Reasoning procedure:** Compare the same planned measure, scale, contrast, and arm assignments; retain the SAP clarification as direct source evidence.

**Calculation:** `18−15=3`, `8−5=3`, `18−8=10`, and `15−5=10` days.

**Alternative source-grounded interpretations:** The page-12 mean/median distinction and the SAP’s explicit 8/5 clarification are supported. Amendment or drafting history is not supplied.

**Mechanical evidence recheck:** Direct-page recheck confirmed both median pairs, the means, and the SAP clarification; see [evidence recheck](review_1_5_3/verification/evidence_recheck.md#c002--planned-median-hospital-day-values-conflict-across-protocolsap-locations).

**Quality-control relevance:** Arm-specific planning values should be internally traceable even when the stated contrast is preserved.

**Potential downstream evidence impact:** If confirmed, an evidence extractor or replication reviewer could copy incorrect arm-specific planning medians; no effect on observed results or conclusions is asserted.

**Human verification steps:** Verify final design inputs and version history, then determine whether any location requires correction, clarification, or version qualification.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Bayesian intervention priors

**Status:** Pending Human Adjudication

**Candidate statement:** The article’s common intervention-prior range differs from the SAP’s class-specific prior descriptions.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [main article — PDF p. 4](<../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4>); [SAP — PDF p. 8](<../joi240020supp2_prod_1710443209.75411.pdf#page=8>).

**Source evidence:** The article states 0.33-3.0 for categorical and count intervention effects. The SAP gives categorical OR 0.2-4 with `Normal(0, SD=0.7)` on log-OR scale, and count RR 0.33-3.3.

**Reported-versus-comparator:** A common 0.33-3.0 range versus categorical 0.2-4 and count 0.33-3.3 ranges.

**Reasoning procedure:** Compare printed prior endpoints by outcome class and stated effect scale without inferring final model code.

**Calculation:** Categorical endpoint differences: `0.33−0.20=0.13` and `4.0−3.0=1.0`; count upper-endpoint difference: `3.3−3.0=0.3`.

**Alternative source-grounded interpretations:** The supplied documents do not select which stated range governed each final model. Amendment, simplification, and implementation history are not supplied.

**Mechanical evidence recheck:** Direct-page recheck confirmed the article and SAP descriptions; see [evidence recheck](review_1_5_3/verification/evidence_recheck.md#c003--bayesian-intervention-prior-ranges-differ-between-the-article-and-sap).

**Quality-control relevance:** Statistical-prior descriptions should allow a reader to identify the stated model specification.

**Potential downstream evidence impact:** If confirmed, a replication or evidence-synthesis reader could copy an incorrect stated prior; no estimate, conclusion, or propagation effect is asserted.

**Human verification steps:** Inspect final outcome-specific model specifications and determine how the article and SAP descriptions should be reconciled.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Gestational-age boundary

**Status:** Pending Human Adjudication

**Candidate statement:** The actual-result subgroup label `≥28` weeks differs from planned SAP wording `>28` weeks.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [main article — PDF p. 8](<../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8>), Figure 3; [SAP — PDF p. 3](<../joi240020supp2_prod_1710443209.75411.pdf#page=3>); [SAP — PDF p. 8](<../joi240020supp2_prod_1710443209.75411.pdf#page=8>); [SAP — PDF p. 9](<../joi240020supp2_prod_1710443209.75411.pdf#page=9>).

**Source evidence:** Figure 3 reports `<28 wk` and `≥28 wk`. SAP pp. 3 and 9 use `<28`/`>28`; SAP p. 8 itself uses `<28`/`≥28`.

**Reported-versus-comparator:** `≥28` includes exactly 28 weeks; `>28` excludes it.

**Reasoning procedure:** Compare the stated partitions and retain only source-supported context about their internal wording.

**Calculation:** At exactly 28 weeks, `GA≥28` is true and `GA>28` is false. The Figure 3 subgroup denominators partition the analysis populations: `102+57=159` and `99+50=149`.

**Alternative source-grounded interpretations:** SAP p. 8 and the article’s complete displayed partition support a possible inconsistent `>28` label. Exact gestational-age coding and exactly-28-week assignment are not supplied.

**Mechanical evidence recheck:** Direct-page recheck confirmed the competing operators and subgroup partition; see [evidence recheck](review_1_5_3/verification/evidence_recheck.md#c004--gestational-age-subgroup-boundary-is-printed-as-28-and-28-weeks).

**Quality-control relevance:** A subgroup boundary should identify which infants belong to each reported effect stratum.

**Potential downstream evidence impact:** If confirmed, an extractor could copy the wrong subgroup boundary with reported subgroup effects; no reassignment, propagation, or conclusion change is asserted.

**Human verification steps:** Verify cut point, representation/rounding convention, and assignment of exactly-28-week records.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — Primary-outcome time origin

**Status:** Pending Human Adjudication

**Candidate statement:** Primary SAE ascertainment is labeled from enrollment in protocol text and from randomization in SAP/main-article text.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [protocol — PDF p. 3](<../joi240020supp1_prod_1710443209.74911.pdf#page=3>); [protocol — PDF p. 11](<../joi240020supp1_prod_1710443209.74911.pdf#page=11>); [SAP — PDF p. 7](<../joi240020supp2_prod_1710443209.75411.pdf#page=7>); [main article — PDF p. 3](<../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3>). [Main article — PDF p. 6](<../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6>) footnote g is secondary-outcome context only, as it attaches to the hospital-stay row.

**Source evidence:** Protocol text defines SAE ascertainment from enrollment through 10 months after enrollment; the SAP and main article state primary-outcome collection for 10 months after randomization.

**Reported-versus-comparator:** `[enrollment, enrollment + 10 months]` versus `[randomization, randomization + 10 months]`.

**Reasoning procedure:** Compare named time origins without assuming that enrollment and randomization were simultaneous.

**Calculation:** The two windows have the same duration but different named origins unless enrollment equals randomization; the supplied package does not define that equality.

**Alternative source-grounded interpretations:** The protocol’s mixed terminology supports possible interchangeable usage. Operational simultaneity and any event-count difference are not supplied.

**Mechanical evidence recheck:** Direct-page recheck confirmed the competing time-origin wording and footnote attachment; see [evidence recheck](review_1_5_3/verification/evidence_recheck.md#c005--primary-outcome-time-origin-is-labeled-enrollment-and-randomization).

**Quality-control relevance:** The reported primary-outcome window should state its time origin consistently.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an incorrect observation window; no event-count change, propagation, or conclusion change is asserted.

**Human verification steps:** Verify enrollment/randomization timestamps and the final SAE extraction boundary rule.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If a candidate is confirmed, the relevant risk is that a systematic review, meta-analysis, guideline, replication record, or data extractor could copy a threshold, planning value, prior description, subgroup boundary, or observation-window label that is not the intended one. This report does not assert that such copying occurred or that any conclusion changed.

## Limitations and Missing Definitions

See the durable [limitations artifact](review_1_5_3/limitations.md). The supplied package lacks raw data, final code, key endpoint and timestamp definitions, exact gestational-age coding, and amendment/version history. These limitations bound the human questions; they do not resolve or suppress candidates.

## Human Adjudication Checklist

For each card, verify the cited source pages, obtain the named missing definition or record where available, decide the appropriate documentation outcome, and record all decisions only in the card’s human-adjudication fields.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Reproducibility and source integrity

- Routing preflight: PASS; interactive coordinator inference and all nine required role presets passed.
- Source coverage: 290/290 mapped units; 14 reusable plus 276 fresh-required units.
- Source and reused-artifact pre-review hash ledgers: [source hashes](review_1_5_3/source_hashes_before.sha256) and [reused artifact hashes](review_1_5_3/reused_artifact_hashes_before.sha256).
- Canonical evidence and review artifacts: [coverage manifest](review_1_5_3/coverage_manifest.md), [candidate ledger](review_1_5_3/candidate_ledger.md), [mechanical recheck](review_1_5_3/verification/evidence_recheck.md), and [quality audit](review_1_5_3/quality/evidence_quality_audit.md).

### Agent execution

All manifested stages used their recorded model, effort, and fresh-start status; the two statistical passes have distinct runtime IDs. The authoritative full list is [agent_execution_manifest.md](review_1_5_3/agent_execution_manifest.md).

### Performance

- **Target basis:** Five direct sources contain 53 PDF pages and 237 DOCX paragraph units, with 276 of 290 units requiring fresh direct-source mapping; the package includes a protocol, a statistical analysis plan, a results supplement with visually confirmed table pages, and a legacy auxiliary DOCX that requires structural exclusion handling. The resulting relationship volume, fresh extraction burden, and required independent agent waves support this bounded package-specific target.
- **Total source units:** 290
- **Fresh-source units:** 276
- **Target elapsed minutes:** 55-80
- **Started UTC:** 2026-08-19T04:31:57Z
- **Finished UTC:** 2026-08-19T04:56:08Z
- **Observed elapsed minutes:** 24.2
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

The interactive and collaboration runtimes exposed no authoritative response-level token counts, so
all 11 manifested agents have explicit `UNAVAILABLE` rows in the
[token usage ledger](review_1_5_3/token_usage_ledger.csv). The reported zero is the known subtotal,
not a complete package count. Cached-input/cache-write values are input subsets and reasoning values
are output subsets; they are not added again to total tokens. Any available amount uses the bundled
2026-08-18 fixed-model pricing snapshot and is a token-only estimate, not an invoice. Per-agent detail
is available in [token_usage_summary.md](review_1_5_3/token_usage_summary.md).
