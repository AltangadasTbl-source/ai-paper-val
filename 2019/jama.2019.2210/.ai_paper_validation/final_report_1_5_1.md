# Quantitative Quality-Control Consistency Review — Workflow 1.5.1

## Pending Human Adjudication

Every candidate in this report is **Pending Human Adjudication**. This is a quantitative reporting quality-control review, not a finding of invalidity or a conclusion about the study. Small preventable defects can matter for downstream evidence extraction; this report does not claim that any defect propagated, changed a conclusion, or caused serious harm.

## Executive Quality-Control Summary

Complete direct-source mapping identified **9** distinct candidate consistency issues (C001–C009). They concern denominators, a figure-caption contradiction, protocol thresholds and endpoint labels, a subgroup boundary label, a cross-document locus label, survival-origin terminology, and a hazard-ratio direction footnote. There is no review queue, top-N subset, or deferred-by-cap section.

## Package and Reused-Evidence Provenance

The supplied package contains four direct PDF sources: [main article](<../jama_urashima_2019_oi_190023.pdf#page=1>), [Supplement 1 protocol/SAP](<../joi190023supp1_prod.pdf#page=1>), [Supplement 2](<../joi190023supp2_prod.pdf#page=1>), and [Supplement 3](<../joi190023supp3_prod.pdf#page=1>). Reused native text and related derivatives were used only as locators and transcription aids; cited direct PDFs are the evidence authority. Source and reused-artifact inventories and before-work hashes are recorded in [the review artifacts](<review_1_5_1/>).

## Scope, Complete Coverage, and Exclusions

All 96 direct PDF pages were mapped: 49 through fit reusable extraction and 47 through fresh direct-source extraction. The source rows are complete: main article 9/9 pages, Supplement 1 45/45, Supplement 2 41/41, and Supplement 3 1/1. The review covers supplied-package quantitative reporting consistency only. It excludes a broad study-design, clinical, misconduct, novelty, raw-data, or external-literature audit. Coherent display-zero P values alone were excluded; none of the nine candidates depends on one.

## Quantitative and Statistical Relationship Coverage

The complete inventory contains **89 numeric/reporting relationships** (N001–N089) and **83 inferential-statistical relationships** (S001–S083). A distinct fresh Terra/high statistical pass 1 and a different fresh Terra/high statistical pass 2 each covered S001–S083. Both passes are complete; pass 2 added no distinct candidate.

## Candidate Index

| ID | Candidate | Category |
|---|---|---|
| [C001](#c001--table-1-snp-percentages-use-unlabelled-variable-available-case-denominators) | SNP available-case denominators | Denominator, proportion, or total inconsistency |
| [C002](#c002--figure-3-caption-says-panel-c-risk-numbers-are-absent-although-the-panel-prints-them) | Figure 3 panel-C risk rows | Numeric or arithmetic inconsistency |
| [C003](#c003--final-protocol-gives-different-accrual-stopping-thresholds) | Accrual stopping threshold | Denominator, proportion, or total inconsistency |
| [C004](#c004--final-protocol-assigns-de-novo-cancer-incompatible-endpoint-labels) | De novo cancer endpoint label | Measure, label, or scale inconsistency |
| [C005](#c005--one-final-protocol-high-25ohd-stratum-label-omits-the-boundary-operator) | High-25(OH)D boundary | Measure, label, or scale inconsistency |
| [C006](#c006--supplement-labels-cdx2-genotype-panels-as-cdk2) | Cdx2/CDK2 label | Measure, label, or scale inconsistency |
| [C007](#c007--table-1-bmi-categories-use-smaller-unlabelled-denominators-than-the-arm-headers) | BMI available-case denominators | Denominator, proportion, or total inconsistency |
| [C008](#c008--report-and-protocol-use-different-time-origin-labels-despite-a-same-visit-equivalence-statement) | Survival time-origin labels | Measure, label, or scale inconsistency |
| [C009](#c009--table-2-hazard-ratio-direction-footnote-is-opposite-the-displayed-outcome-direction) | HR direction footnote | Measure, label, or scale inconsistency |

## Candidate Evidence Cards

## C001 — Table 1 SNP percentages use unlabelled, variable available-case denominators

**Status:** Pending Human Adjudication

**Candidate statement:** Table 1 percentages use SNP-specific denominators smaller than the printed arm headers without an available-case or missingness label.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [main article — PDF p. 5](<../jama_urashima_2019_oi_190023.pdf#page=5>); [Supplement 2 — PDF p. 7](<../joi190023supp2_prod.pdf#page=7>), [p. 13](<../joi190023supp2_prod.pdf#page=13>), and [p. 27](<../joi190023supp2_prod.pdf#page=27>).

**Source evidence:** Table 1 heads the arms vitamin D `n=251` and placebo `n=166`; its Cdx2 counts are `89/103/38` and `49/77/24`, while the footnote addresses only percentage rounding. Supplement figures repeat the genotype-specific time-zero counts.

**Reported-versus-comparator:** The arm headers are `251/166`; Cdx2 triplets total `230/150`, and other SNP totals vary from `230–245` and `148–157`.

**Reasoning procedure:** Sum mutually exclusive genotype categories and compare the resulting available counts with each arm header and printed percentage basis.

**Calculation:** Cdx2: `89+103+38=230`, `49+77+24=150`; `89/230=38.70%`, `103/230=44.78%`, and `38/230=16.52%`, matching printed rounded percentages. The respective deficits from headers are `21` and `16`.

**Alternative source-grounded interpretations:** SNP-specific assay availability could legitimately yield variable denominators, but neither the table nor its footnote states that explanation.

**Mechanical evidence recheck:** Location, headings, all relevant counts, comparator figures, arithmetic, and the missing denominator definition were confirmed against direct PDFs. Direct observations are separated from possible assay-failure explanations.

**Quality-control relevance:** A table should identify a denominator when its percentages do not use the displayed arm total.

**Potential downstream evidence impact:** If confirmed, an extractor could copy arm totals rather than SNP-specific available-case denominators when recording genotype distributions.

**Human verification steps:** Check assay-call logs or the analysis dataset; identify the per-SNP, per-arm denominator and missing count; confirm intended Table 1 footnote wording.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C002 — Figure 3 caption says panel-C risk numbers are absent although the panel prints them

**Status:** Pending Human Adjudication

**Candidate statement:** Figure 3 panel C visibly prints risk rows while its caption says that panel-C numbers at risk are not given.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [main article — PDF p. 7](<../jama_urashima_2019_oi_190023.pdf#page=7>).

**Source evidence:** Panel C prints placebo `90, 88, 70, 51, 34, 22, 11` and vitamin D `142, 139, 115, 88, 61, 41, 20` under `No. at risk`.

**Reported-versus-comparator:** The caption states, `Numbers at risk for panel C are not given because of weighting.`

**Reasoning procedure:** Compare the literal caption statement with the displayed panel element.

**Calculation:** Seven placebo plus seven vitamin-D entries yield `14` displayed panel-C risk values, not zero.

**Alternative source-grounded interpretations:** The caption may mean weighted or effective numbers are unavailable while the panel shows raw counts; the source does not define that distinction.

**Mechanical evidence recheck:** The panel, 14 entries, and caption were directly confirmed. A stale caption, misplaced rows, or raw-versus-weighted distinction remains an inference.

**Quality-control relevance:** Caption and figure should not give incompatible instructions about whether a displayed quantity is present.

**Potential downstream evidence impact:** If confirmed, a data extractor could omit, misclassify, or incorrectly interpret the panel-C risk rows.

**Human verification steps:** Confirm the weighting method and intended meaning of the rows; compare the production figure and caption source; revise whichever element is not intended.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C003 — Final protocol gives different accrual stopping thresholds

**Status:** Pending Human Adjudication

**Candidate statement:** Two final-protocol passages state different literal enrollment stopping thresholds.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [Supplement 1 — PDF p. 18](<../joi190023supp1_prod.pdf#page=18>) and [Supplement 1 — PDF p. 31](<../joi190023supp1_prod.pdf#page=31>).

**Source evidence:** Page 18 says entry stops if randomized enrollment reaches `>400`; it also gives `240+160=400` as the target allocation.

**Reported-versus-comparator:** Page 31 says, `After enrolling 400 patients, enrollment will finish.`

**Reasoning procedure:** Apply the printed inequality to an integer enrollment count and compare it with the stated finishing count.

**Calculation:** `240+160=400`; the smallest integer satisfying `n>400` is `401`, whereas `after enrolling 400` identifies 400.

**Alternative source-grounded interpretations:** Either statement could be shorthand for a near-400 operational target or a completed randomization block, but no cited passage says so.

**Mechanical evidence recheck:** Both passages, allocation, inequality logic, and missing operative-rule definition were directly rechecked.

**Quality-control relevance:** A stopping threshold should be expressed consistently where it defines enrollment totals.

**Potential downstream evidence impact:** If confirmed, an extractor could record an incorrect planned enrollment cap or target.

**Human verification steps:** Review the operative protocol/version history and randomization-block rules; establish which threshold governed accrual.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C004 — Final protocol assigns de novo cancer incompatible endpoint labels

**Status:** Pending Human Adjudication

**Candidate statement:** The same de novo-cancer event is labelled `not as an outcome`, `Tertiary outcome`, and is reported in a safety-outcome table without a stated reconciliation.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Supplement 1 — PDF p. 19](<../joi190023supp1_prod.pdf#page=19>), [p. 25](<../joi190023supp1_prod.pdf#page=25>), [p. 26](<../joi190023supp1_prod.pdf#page=26>), and [p. 45](<../joi190023supp1_prod.pdf#page=45>); [main article — PDF p. 8](<../jama_urashima_2019_oi_190023.pdf#page=8>).

**Source evidence:** The synopsis says cancer appearing de novo will be an adverse event, `not as an outcome`; the final body lists it as a tertiary outcome, and the change summary says it was inserted as a tertiary outcome.

**Reported-versus-comparator:** The main article places `Cancer de novo` in Table 3, `Safety Outcomes`, including randomization-group counts `16/251` and `9/166`.

**Reasoning procedure:** Compare classifications of the same named event and ascertainment period; a dual role needs an explicit definition.

**Calculation:** The logical comparison reproduces three labels: adverse event/not outcome; tertiary outcome; and Safety Outcomes. The reported counts establish that this is a quantitative reporting item.

**Alternative source-grounded interpretations:** Clinical monitoring could use an adverse-event role while the statistical hierarchy uses a tertiary-outcome role, but the supplied text does not define those roles separately.

**Mechanical evidence recheck:** Event wording, three labels, change summary, table placement, counts, and missing hierarchy definition were confirmed against direct PDFs.

**Quality-control relevance:** Endpoint hierarchy and safety presentation should use defined, reconcilable labels.

**Potential downstream evidence impact:** If confirmed, an extractor could classify de novo cancer differently across outcome and safety evidence tables.

**Human verification steps:** Identify the final endpoint hierarchy and analysis plan; determine whether distinct adverse-event and tertiary-outcome roles were intended; align Table 3 terminology.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C005 — One final-protocol high-25(OH)D stratum label omits the boundary operator

**Status:** Pending Human Adjudication

**Candidate statement:** One protocol page gives high 25(OH)D as `(40 ng/mL)` without an operator, unlike later explicit `>40 ng/mL` definitions.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [Supplement 1 — PDF p. 23](<../joi190023supp1_prod.pdf#page=23>) and [p. 31](<../joi190023supp1_prod.pdf#page=31>); [main article — PDF p. 3](<../jama_urashima_2019_oi_190023.pdf#page=3>).

**Source evidence:** Page 23 defines low `(<20)`, middle `(>=20 to <=40)`, and high `(40 ng/mL)`.

**Reported-versus-comparator:** Page 31 and the article explicitly give high as `>40 ng/mL`.

**Reasoning procedure:** Test the boundary value against the explicit nonoverlapping category definitions.

**Calculation:** At `40`, `20<=40<=40` places the value in middle; `40` is not `>40`. The page-23 text leaves whether high means `=40`, `>=40`, or `>40` unspecified.

**Alternative source-grounded interpretations:** Page 23 may use `40 ng/mL` as informal shorthand for the cutoff; the later sources make `>40` the likely intended explicit rule.

**Mechanical evidence recheck:** All three printed label sets, the boundary logic, and the unavailable intended operator were confirmed.

**Quality-control relevance:** Prespecified strata need an explicit boundary to avoid overlap or ambiguity.

**Potential downstream evidence impact:** If confirmed, an extractor could assign the cutoff group or subgroup definition inconsistently.

**Human verification steps:** Check the implemented subgroup-programming rule and source version; confirm the intended page-23 operator and whether any value exactly 40 required assignment.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C006 — Supplement labels Cdx2 genotype panels as CDK2

**Status:** Pending Human Adjudication

**Candidate statement:** Supplement 2 labels matched Cdx2 subgroup panels as `CDK2` although the article and protocol identify `Cdx2/CDX2 rs11568820`.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [main article — PDF p. 5](<../jama_urashima_2019_oi_190023.pdf#page=5>); [Supplement 1 — PDF p. 27](<../joi190023supp1_prod.pdf#page=27>); [Supplement 2 — PDF p. 13](<../joi190023supp2_prod.pdf#page=13>), [p. 14](<../joi190023supp2_prod.pdf#page=14>), and [p. 15](<../joi190023supp2_prod.pdf#page=15>).

**Source evidence:** Table 1 gives Cdx2 GG/GA/AA vitamin-D counts `89,103,38` and placebo counts `49,77,24`; the protocol lists `CDX2, rs11568820`.

**Reported-versus-comparator:** Supplement panels are titled `CDK2 GG`, `CDK2 GA`, and `CDK2 AA` and show corresponding placebo/vitamin-D counts `49/89`, `77/103`, and `24/38`.

**Reasoning procedure:** Match subgroup identity through all six arm-by-genotype risk counts, then compare the locus label.

**Calculation:** `49=49`, `89=89`, `77=77`, `103=103`, `24=24`, and `38=38`; labels differ at the third character after `CD`: `X` versus `K`.

**Alternative source-grounded interpretations:** Matching counts and absence of CDK2 from the protocol list support a possible typesetting substitution; a distinct analysis with coincident counts is not defined in the package.

**Mechanical evidence recheck:** Labels, counts, protocol locus identifier, exact page anchors, and lack of source mapping statement were rechecked against direct PDFs.

**Quality-control relevance:** A matched genetic subgroup should retain its locus label across report components.

**Potential downstream evidence impact:** If confirmed, an extractor could copy the wrong locus name or attribute subgroup estimates to a different marker.

**Human verification steps:** Check genotype dataset and figure-generation code; confirm whether eFigures 3G–3I are rs11568820 and correct titles/captions if needed.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C007 — Table 1 BMI categories use smaller, unlabelled denominators than the arm headers

**Status:** Pending Human Adjudication

**Candidate statement:** Table 1 BMI quartiles and complementary supplement subgroups total fewer participants than the printed arm headers without a missingness or available-case label.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [main article — PDF p. 5](<../jama_urashima_2019_oi_190023.pdf#page=5>); [Supplement 2 — PDF p. 32](<../joi190023supp2_prod.pdf#page=32>) and [p. 33](<../joi190023supp2_prod.pdf#page=33>).

**Source evidence:** Under vitamin D `n=251` and placebo `n=166`, Table 1 gives BMI quartile counts `63,62,59,65` and `36,43,45,41`.

**Reported-versus-comparator:** Supplement 2 complementary BMI risks total vitamin D `208+41` and placebo `144+21`.

**Reasoning procedure:** Sum exhaustive BMI categories, compare with arm headers, and independently compare with complementary subgroup counts.

**Calculation:** `63+62+59+65=249` and `36+43+45+41=165`, deficits of `2` and `1`; Supplement 2 repeats `208+41=249` and `144+21=165`. Percentages also round from the smaller denominators.

**Alternative source-grounded interpretations:** BMI may be unavailable for exactly two vitamin-D and one placebo participant; a count transcription issue is another possibility. Neither explanation is stated.

**Mechanical evidence recheck:** Headers, quartiles, percentages, replicated supplement totals, arithmetic, and missing denominator statement were directly confirmed.

**Quality-control relevance:** Baseline-category percentages and subgroup results should disclose an available-case denominator when it differs from arm enrollment.

**Potential downstream evidence impact:** If confirmed, an extractor could use `251/166` instead of `249/165` for BMI proportions or subgroup sample sizes.

**Human verification steps:** Inspect baseline data and missingness handling; identify exclusions or unavailable BMI values; add the intended denominator/missingness statement.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C008 — Report and protocol use different time-origin labels despite a same-visit equivalence statement

**Status:** Pending Human Adjudication

**Candidate statement:** The report labels survival time from randomization while the final protocol labels it from starting supplementation; the article explicitly describes these as the same visit and treats them as equivalent, so no actual date difference is claimed.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [main article — PDF p. 2](<../jama_urashima_2019_oi_190023.pdf#page=2>) and [p. 6](<../jama_urashima_2019_oi_190023.pdf#page=6>); [Supplement 1 — PDF p. 25](<../joi190023supp1_prod.pdf#page=25>) and [p. 29](<../joi190023supp1_prod.pdf#page=29>); [Supplement 2 — PDF p. 2](<../joi190023supp2_prod.pdf#page=2>) and [p. 3](<../joi190023supp2_prod.pdf#page=3>).

**Source evidence:** The article defines RFS/OS from randomization, parenthetically as time from starting study medication, and plots years after randomization. It says participants were randomized and started supplementation at the first outpatient visit.

**Reported-versus-comparator:** The protocol defines RFS/OS and survival duration from starting supplementation or the supplement start day; Supplement 2 axes use randomization.

**Reasoning procedure:** Compare the printed time-origin labels while preserving the article’s same-visit and explicit equivalence context.

**Calculation:** No numeric estimate is recalculated. The wording comparison is `randomization date` versus `supplement start day`; participant-level date fields and survival-analysis code are not supplied to establish identity in every record.

**Alternative source-grounded interpretations:** The article itself supports different labels for the same operational date, rather than different numeric origins; universal participant-level identity remains unconfirmed.

**Mechanical evidence recheck:** Outcome definitions, axes, same-visit statement, parenthetical equivalence, and the absent date-variable/code evidence were directly confirmed. No claim is made that actual time origins differed.

**Quality-control relevance:** Time-to-event reporting should name a consistently defined time origin or explicitly document operational equivalence.

**Potential downstream evidence impact:** If confirmed, an extractor could record different time-origin labels unless the operational equivalence and analysis variable are clarified.

**Human verification steps:** Inspect analysis code and participant-level randomization/first-dose dates; identify the stored time-zero variable and document whether the dates were identical for every analyzed participant.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C009 — Table 2 hazard-ratio direction footnote is opposite the displayed outcome direction

**Status:** Pending Human Adjudication

**Candidate statement:** Table 2 says HR values greater than 1 indicate decreased outcome probability with vitamin D, whereas displayed outcome directions pair lower vitamin-D incidence with HRs below 1.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [main article — PDF p. 4](<../jama_urashima_2019_oi_190023.pdf#page=4>), [p. 6](<../jama_urashima_2019_oi_190023.pdf#page=6>), and [p. 7](<../jama_urashima_2019_oi_190023.pdf#page=7>).

**Source evidence:** Table 2 reports relapse HR `0.75 (0.48–1.17)`, cancer-specific-death HR `1.09 (0.58–2.01)`, noncancer-death HR `0.70 (0.29–1.73)`, and the footnote assigning decreased outcome probability to HR `>1`.

**Reported-versus-comparator:** Page 4 gives vitamin D/placebo relapse `41/251` versus `36/166`, cancer-specific death `27/251` versus `16/166`, and noncancer death `10/251` versus `9/166`; Figure 2C shows the vitamin-D relapse curve below placebo and prints HR `0.75`.

**Reasoning procedure:** Compare footnote direction with counts, curve/narrative direction, and HR sign without reconstructing the time-to-event models.

**Calculation:** Diagnostic crude proportions are relapse `16.33%` versus `21.69%`, noncancer death `3.98%` versus `5.42%`, and cancer-specific death `10.76%` versus `9.64%`. Lower vitamin-D incidence corresponds to HRs below 1 for relapse and noncancer death; higher incidence corresponds to HR above 1 for cancer-specific death. These are diagnostics, not reproduced HR estimators.

**Alternative source-grounded interpretations:** A placebo-relative contrast could make the footnote coherent, but the plotted/narrated relapse direction and HR below 1 indicate the opposite orientation for displayed relapse results; a table-only reversed contrast is not stated.

**Mechanical evidence recheck:** Counts, curve order, narrative, HRs, footnote, diagnostic arithmetic, and unavailable event-time/censoring/model inputs were rechecked against the direct PDF.

**Quality-control relevance:** A direction footnote should agree with the displayed treatment contrast so effect interpretation is reproducible.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an incorrect HR direction or treatment-reference interpretation.

**Human verification steps:** Inspect model specifications and reference coding for each Table 2 row; confirm the footnote orientation and revise the table text if required.

**Human adjudication fields:**
- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

If any candidate is confirmed, it could affect how a systematic review, meta-analysis, guideline, or structured data extractor transcribes a denominator, endpoint class, subgroup label, time-origin description, or effect-direction label. This is a bounded possibility only; the supplied package does not establish propagation, conclusion change, or harm.

## Limitations and Missing Definitions

Current direct-PDF mapping closes all scientific-coverage gaps, but some historical derivatives have stale provenance and were not relied on as authority. Individual-level dates, event/censoring times, genotype assay-call logs, figure source files, analysis code, and raw structured data are unavailable. Several subgroup figures omit complete model, adjustment, CI-construction, sidedness, and reference-orientation details; checks therefore do not invent those definitions. This review is limited to reporting consistency in the supplied package.

## Human Adjudication Checklist

For each card: confirm the cited source text and comparator; inspect the named primary record or analysis artifact; decide whether the stated alternative explains the observation; document any correction or no-change rationale; complete all five human-adjudication fields with initials.

## Reproducibility, Source-Integrity, Agent-Execution, Performance, Token-Usage, and Cost Metadata

### Source integrity and execution

Source and reused-artifact SHA-256 baselines are recorded before review; direct sources and reused assets were not modified. The manifest records the coordinator, curator, four mapping agents, numeric and cross-source agents, two distinct statistical agents, evidence rechecker, quality auditor, and this report generator. Candidate-ledger, recheck, quality-audit, and report ID sets are identical: C001–C009.

### Reproducibility performance

- **Target basis:** Four PDF sources contain 96 page units; 49 pages have fit reusable native text, 47 pages require fresh direct extraction, there are no Office/workbook sources, and complete review still requires four disjoint mapping shards plus numeric, cross-source, and two statistical passes.
- **Total source units:** 96
- **Fresh-source units:** 47
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-08-18T22:12:12Z
- **Finished UTC:** 2026-08-18T22:50:50Z
- **Observed elapsed minutes:** 38.6
- **Target status:** MET_TARGET
- **Exceedance causes:** None

### Token accounting and cost

- **Token accounting status:** INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE
- **Total-token count status:** INCOMPLETE
- **Total tokens:** 0
- **Known token cost (USD):** 0.000000
- **Estimated complete token cost (USD):** __

| Model | Total tokens | Known token cost (USD) | Complete-cost status |
|---|---:|---:|---|
| `gpt-5.6-sol` | 0 | 0.000000 | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |
| `gpt-5.6-terra` | 0 | 0.000000 | INCOMPLETE_RUNTIME_USAGE_UNAVAILABLE |

Coordinator replacement must use authoritative response-level runtime/API usage through Finished UTC and the dated price snapshot. Amounts are token-only API-equivalent estimates, not invoices; cached/cache-write input and reasoning output are subsets and must not be added again. Per-agent detail belongs in the versioned token-usage summary artifact.
