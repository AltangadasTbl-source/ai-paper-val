# Quantitative Quality-Control Consistency Review — JAMA 2018.6496

**Pending Human Adjudication**

This report records reporting-consistency candidates for human review. Evidence states describe mechanical source checks; suggested review dispositions are mechanical pre-fills. Every candidate remains Pending Human Adjudication.

## Executive Quality-Control Summary

Complete review of the three supplied PDFs, comprising 49 physical pages, produced **10 stable candidates, C001–C010**. Nine have evidence state `recorded_candidate`; C008 has `record_input_error` because its proposed numerical comparison depended on an unsupported alignment of numerator and population. All ten receive full evidence cards.

The candidates concern two baseline percentage bases, a final-operator category total, a descending confidence interval, a historical percentage's direct rounding, duration and hypoxemia endpoint definitions, a primary missing-data endpoint label, a repeated resistance-result population label, and initial oxygen available-case denominators. Alternatives and missing definitions are stated individually. No numerical consequences are established for the endpoint-definition candidates.

Small preventable numeric or labeling defects can matter when evidence is extracted into systematic reviews, meta-analyses, guidelines or later publications. This review does not establish downstream propagation, conclusion change or serious harm.

Scientific source and relationship coverage is complete. Strict workflow validation has an execution-context limitation: the user's current-provider instruction and unavailable original-launch attestation conflict with four hard-coded routing literals in the unmodified validator. This report does not claim unconditional validator PASS; see the final [validation record](review_1_6/review_validation.json) after coordinator finalization.

## Package and Reused-Evidence Provenance

The package contains three scientific sources and no supplied Office, workbook or CSV files. Page numbers below are physical PDF pages, including covers. Roles follow content.

| Source ID | Actual supplied file | Pages | Content role |
|---|---|---:|---|
| DOC-001 | [jama_driver_2018_oi_180054.pdf — PDF p. 1](<../jama_driver_2018_oi_180054.pdf#page=1>) | 11 | REPORT main article |
| DOC-002 | [joi180054supp1_prod.pdf — PDF p. 1](<../joi180054supp1_prod.pdf#page=1>) | 25 | PLAN protocol, including historical background |
| DOC-003 | [joi180054supp2_prod.pdf — PDF p. 1](<../joi180054supp2_prod.pdf#page=1>) | 13 | Results pp.1–6 are REPORT, with quoted prospective rules classified by content; blank operational form pp.7–13 is PLAN |

A prospective-rule quotation in the interim appendix is PLAN content even within a REPORT results appendix. An operational form is PLAN, irrespective of supplement filename.

The curator reused **47 preprocessing assets** from `review_1_5_2/preprocessing/`: six whole-document native/layout text files and 41 PNG page renders. These overlap and cover 49 unique source pages; file counts are not source-unit counts. Old candidates, classifications, decisions and reports were not scientific inputs. Native files and the two support layout files match current direct Poppler extraction byte-for-byte. Main layout has a nonsemantic blank-line-position difference in the Figure 2 axis label. Text is readable and source-matched on every page.

Historical extraction/render engine metadata is UNKNOWN. Current-source agreement establishes fitness, not a historical engine attribution. The eight missing legacy PNGs are DOC-001 p.11 and DOC-002 pp.1–4,23–25; usable text covers each. Result-relevant graphical material was visually inspected during mapping, including the form's grade labels absent from text. The rechecker freshly rendered and visually inspected all 16 unique cited candidate pages using Poppler 25.03.0 at 125 dpi, with fresh layout text as a locator.

Complete provenance and page-level derivative paths are in the [source inventory](review_1_6/source_inventory.md), [evidence asset inventory](review_1_6/evidence_asset_inventory.md), [reuse hash baseline](review_1_6/reused_artifact_hashes_before.sha256) and [direct-source recheck](review_1_6/verification/evidence_recheck.md). Supplied PDFs remain the evidence authority.

## Scope, Complete Coverage, and Exclusions

Every physical source page received fresh scientific mapping, including covers, reference pages, prospective instructions and blank forms. Reusing extraction did not reuse candidate selection.

| Source ID | Unit type | Total | Reusable | Fresh-required | Mapped | Status |
|---|---|---:|---:|---:|---:|---|
| DOC-001 | PDF_PAGE | 11 | 11 | 0 | 11 | COMPLETE |
| DOC-002 | PDF_PAGE | 25 | 25 | 0 | 25 | COMPLETE |
| DOC-003 | PDF_PAGE | 13 | 13 | 0 | 13 | COMPLETE |
| Total | PDF_PAGE | 49 | 49 | 0 | 49 | COMPLETE |

Main and support assignments are disjoint and jointly exhaustive. Zero fresh-required pages means usable reusable extraction existed for every unit; targeted source rendering and fresh scientific review still occurred. The [source coverage ledger](review_1_6/source_coverage.md) and [coverage manifest](review_1_6/coverage_manifest.md) document each assignment and artifact.

The review prioritizes arithmetic, totals, denominators, proportions, inferential-statistical reporting, matched-source repetition, measure labels, scales and rate/count identity. Population or analysis-unit issues qualify through a concrete quantitative or label comparison. General methodology, study design, clinical interpretation, novelty, misconduct and raw-data audits are excluded. Only supplied package evidence was used; no external literature or web search was used.

Coherent display-zero P values alone are excluded under `DISPLAY_ZERO_NOT_CANDIDATE`. No source display-zero P was identified; P<.001 is a bound, and ICC<.001 is not a P value. None of the ten candidates is based on display precision alone.

## Quantitative and Statistical Relationship Coverage

The maps reconstruct 124 main and 67 support evidence groups. Main mapping includes all 94 table rows (27+34+17+6+10) and 30 narrative, definition, flow or figure groups. Support mapping covers protocol numerical background and plans, all six clustered eTable rows, both eFigures, interim analysis and every form question Q1–Q27.

| Review lane | Complete scope | Durable record |
|---|---|---|
| Numeric consistency | 191 relationships N001–N191, checked in disjoint groups of 100 and 91 | [Numeric inventory](review_1_6/relationships/numeric_relationship_inventory.md); [numeric checker](review_1_6/checkers/numeric_consistency.md) |
| Cross-source consistency | 67 matched comparison groups, with population/time/contrast/model identity checked | [Cross-source checker](review_1_6/checkers/cross_source_consistency.md) |
| Statistical pass 1 | All 93 S relationships, each PASS_1_COMPLETE | [Pass 1](review_1_6/checkers/statistical_pass_1.md) |
| Statistical pass 2 | All 93 S relationships, complete ten-ID ledger and all recheck facts, each PASS_2_COMPLETE; zero new candidates | [Pass 2](review_1_6/checkers/statistical_pass_2.md) |
| Direct-source recheck | C001, C002, C003, C004, C005, C006, C007, C008, C009, C010 | [Evidence recheck](review_1_6/verification/evidence_recheck.md) |
| Independent quality audit | All 49 pages, 191 N groups, 93 S groups and ten stable IDs | [Canonical quality audit](review_1_6/quality/evidence_quality_audit.md) |

The [statistical inventory](review_1_6/statistics/relationship_inventory.md) records both completed passes for every relationship. Fresh agents `task:/root/statistics_one` and `task:/root/statistics_two` executed the separate passes at gpt-6.1-sol/high. The pass-1 artifact's historical PASS_2_PENDING snapshot is superseded by the complete second-pass artifact and current inventory.

All 66 inferential table rows are covered: 34 main Table 2, 17 main Table 3, nine main Table 5 and six clustered eTable 1 rows. Checks cover group and difference intervals, P values, interactions, estimates, signs, natural scales, available cases, repeated values and model identity. Additional groups cover Cox hazard ratios, distinct log-rank tests, figures and risk arrays, ICC bounds, power, interim rules, endpoint definitions and reported analysis labels.

Disclosed clustered analyses are distinct from unclustered results. Hodges–Lehmann estimates need not equal marginal median subtraction; IQR/SD are not confidence intervals; interaction tests are distinct hypotheses from subgroup contrasts. Kaplan–Meier success curves and hazard ratios are not crude success proportions or person-time rates. Six P-value diagnostic differences remain explicitly documented as limitations because the selected reconstruction methods are not source-established author analyses.

## Document-Role Classification Summary

`P_R` compares PLAN with REPORT content; `P_P` is solely within PLAN content; `S_C` compares two different REPORT documents; `S_W` is within one REPORT document. Substantive mixed relationships would use precedence P_R > P_P > S_C > S_W. A corroborating document does not add a discrepancy relationship.

| Relationship type | Stable candidates |
|---|---:|
| P_R | 2 |
| P_P | 2 |
| S_C | 0 |
| S_W | 6 |
| Total | 10 |

| Review domain | Stable candidates |
|---|---:|
| protocol_report | 2 |
| plan_material | 2 |
| statistical_results | 5 |
| report_internal_inconsistency | 1 |
| Total | 10 |

| Evidence state | Stable candidates |
|---|---:|
| recorded_candidate | 9 |
| not_reproduced | 0 |
| repaired_residual | 0 |
| record_input_error | 1 |
| Total | 10 |

Mechanically derived suggested dispositions are `retain` for nine and `discuss` for one; `exclude` is zero. These are human-review pre-fills, not adjudications. Final classification values below are copied exactly from the [ledger classification table](review_1_6/candidate_ledger.md). C006 is P_R only after the form heading was distinguished from a stopwatch instruction; C008 preserves its ID and records the unsupported pooled/arm alignment.

## Candidate Index

| ID | Candidate | Category | Relationship type | Review domain | Evidence state |
|---|---|---|---|---|---|
| [C001](#c001) | Respiratory-indication percentages use a different denominator | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| [C002](#c002) | Other-medical percentages change the denominator | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| [C003](#c003) | Final-operator counts exceed the bougie arm total | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |
| [C004](#c004) | Duration confidence limits are printed in descending order | Statistical reporting inconsistency | S_W | statistical_results | recorded_candidate |
| [C005](#c005) | Historical rescue percentage differs from direct rounding | Denominator, proportion, or total inconsistency | P_P | plan_material | recorded_candidate |
| [C006](#c006) | Planned duration and reported duration use different stop events | Measure, label, or scale inconsistency | P_R | protocol_report | recorded_candidate |
| [C007](#c007) | Primary missing-data instruction names a secondary composite | Measure, label, or scale inconsistency | P_P | plan_material | recorded_candidate |
| [C008](#c008) | Resistance percentage changes its named population | Measure, label, or scale inconsistency | S_W | report_internal_inconsistency | record_input_error |
| [C009](#c009) | Hypoxemia window has a different end anchor | Measure, label, or scale inconsistency | P_R | protocol_report | recorded_candidate |
| [C010](#c010) | Initial oxygen missingness does not reproduce its denominators | Denominator, proportion, or total inconsistency | S_W | statistical_results | recorded_candidate |

## Candidate Evidence Cards

<a id="c001"></a>

## C001 — Respiratory-indication percentages use a different denominator

**Pending Human Adjudication**

**Candidate statement:** Table 1 respiratory-indication percentages do not reproduce the displayed arm denominators; medical-subset denominators reproduce them but are not consistently distinguished.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 1 respiratory-indication row vs REPORT main Table 1 headers and sibling rows

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The conflicting row, headers and sibling rows are REPORT content within the main article. No PLAN comparator is in conflict.

**Classification ambiguity:** None

**Exact source locations:** [jama_driver_2018_oi_180054.pdf — PDF p. 5](<../jama_driver_2018_oi_180054.pdf#page=5>), Table 1 asthma/COPD/heart failure/pneumonia row, No. (%) headers, Medical parent and altered-mental-status sibling rows; all REPORT.

**Source evidence:** Respiratory row 16 (5) and 23 (7); arm n=381 and 376; Medical counts 318 and 315. Altered mental status 185 (49) and 173 (46) matches whole-arm bases.

**Reported-versus-comparator:** Printed 5%/7% versus header-based rounded 4%/6%; medical-subset rounded 5%/7% is an alternative denominator interpretation.

**Reasoning procedure:** Compare exact numerator/denominator fractions with whole-percent displays using a ±0.5 percentage-point rounding allowance. Then evaluate the printed Medical parent as an alternative base. Printed values are direct observations; the denominator used in production is inferred. Checker provenance: NUM-A01; N044 with N039–N043 corroboration; independent numeric-main checker.

**Calculation:** 100×16/381=4.199475%→4%; 100×23/376=6.117021%→6%. Alternative 100×16/318=5.031447%→5%; 100×23/315=7.301587%→7%. Both header-based deviations exceed 0.5 percentage point.

**Alternative source-grounded interpretations:** Medical-subset percentages could be intended. Adjacent altered-mental-status percentages use whole-arm bases, so a row-specific convention needs clarification. Counts are not established as wrong.

**Mechanical evidence recheck:** Exact page, row, headers and comparators found and visually confirmed. Arithmetic reproduced; missing definition is the respiratory-row denominator. The unresolved header/subset alignment supports recorded_candidate. Independent audit agrees.

**Quality-control relevance:** A baseline proportion needs a stated population base to be reproducibly extracted.

**Potential downstream evidence impact:** If confirmed, an extractor could attach these subgroup percentages to the randomized-arm population. No downstream copying or conclusion change is established.

**Human verification steps:** Inspect Table 1 and confirm whether each respiratory percentage uses all randomized patients or only patients with medical indications; identify the intended denominator and corresponding row/header label.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

<a id="c002"></a>

## C002 — Other-medical percentages change the denominator

**Pending Human Adjudication**

**Candidate statement:** Table 1 Other-medical percentages reproduce the Medical subset, while the common arm headers and some sibling rows use whole-arm bases.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 1 other-medical row vs REPORT main Table 1 headers and sibling rows

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both sides are REPORT content in the same main-article table. This is a distinct numerator row from C001, even if the percentage convention has a shared explanation.

**Classification ambiguity:** None

**Exact source locations:** [jama_driver_2018_oi_180054.pdf — PDF p. 5](<../jama_driver_2018_oi_180054.pdf#page=5>), Table 1 Medical—Other row, headers, Medical totals and sibling rows; all REPORT.

**Source evidence:** Other-medical row 44 (14) and 41 (13); headers n=381/376; Medical totals 318/315. Medical subrow sums are 318 and 315.

**Reported-versus-comparator:** Printed 14%/13% versus whole-arm rounded 12%/11%; Medical-subset rounded 14%/13% reproduces the display.

**Reasoning procedure:** Apply whole-percent tolerance to both printed numerator/base pairs. Check the Medical parent and count sums before interpreting the issue as a proportion-base question. The production denominator is inferred from arithmetic. Checker provenance: NUM-A02; N045 with N039/N040/N046–N048 corroboration; independent numeric-main checker.

**Calculation:** 100×44/381=11.548556%→12%; 100×41/376=10.904255%→11%. Alternative 100×44/318=13.836478%→14%; 100×41/315=13.015873%→13%. Whole-arm deviations exceed ±0.5 percentage point; subrow counts add correctly.

**Alternative source-grounded interpretations:** The row could intentionally report Medical-subset percentages; that convention is not consistently stated or applied across sibling rows. No count change is established.

**Mechanical evidence recheck:** All source/comparator entries and count sums visually confirmed; calculation reproduced. Intended Other-row basis remains missing. recorded_candidate is retained and the independent audit agrees.

**Quality-control relevance:** A shared table header should allow readers to identify which population each percentage describes.

**Potential downstream evidence impact:** If confirmed, a baseline data extractor could record these two Other proportions on the wrong population base. Actual propagation is unknown.

**Human verification steps:** Confirm whether 14% and 13% are Medical-subset proportions, and identify the row/header convention intended for these and adjacent subrows.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

<a id="c003"></a>

## C003 — Final-operator counts exceed the bougie arm total

**Pending Human Adjudication**

**Candidate statement:** The three bougie operator-category counts total 383 against n=381 under the footnote defining the final intubating physician.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 2 operator rows vs REPORT main Table 2 header and final-physician footnote

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The conflicting counts, arm total and final-physician footnote are REPORT content within the main article. The PLAN form only corroborates category meanings and adds no P_R relationship.

**Classification ambiguity:** None

**Exact source locations:** [jama_driver_2018_oi_180054.pdf — PDF p. 6](<../jama_driver_2018_oi_180054.pdf#page=6>), Table 2 Operator rows, headers and footnote f, REPORT. [joi180054supp2_prod.pdf — PDF p. 7](<../joi180054supp2_prod.pdf#page=7>), operational form Q2, PLAN corroboration only.

**Source evidence:** Bougie senior resident/fellow 318, junior resident 57 and faculty 8; arm n=381. Comparator counts 334, 37 and 5; n=376. Footnote f specifies the final intubating physician and four physician changes per arm; form Q2 asks for one training level.

**Reported-versus-comparator:** 383 listed bougie-category entries versus 381 patients; comparator categories total 376 against 376 patients.

**Reasoning procedure:** Under one final physician per patient, mutually exclusive category totals cannot exceed the number of patients. Sum printed integers with zero rounding tolerance. Unknown episode-count or overlap rules cannot be assumed. Checker provenance: NUM-A03 and CROSS07; N076/N077/N078/N029 and X053; genuine duplicate comparisons merged before stable IDs.

**Calculation:** 318+57+8=383; 383−381=2. Comparator 334+37+5=376. Four physician changes do not explain extra final-only categories, and rounded percentages cannot alter the integer total.

**Alternative source-grounded interpretations:** Rows may count operator episodes or mix initial/final physicians, or a printed input may differ from the intended count. These mechanisms are unestablished; no particular row is selected for change.

**Mechanical evidence recheck:** Exact counts, totals, footnote and corroborating form confirmed visually. Integer sum reproduced and final-only rule applicable. Case-level counts or overlap/episode definitions are absent. recorded_candidate and S_W were independently audited.

**Quality-control relevance:** The stated counted unit must reconcile category totals with the denominator.

**Potential downstream evidence impact:** If confirmed, an extractor could copy an inconsistent distribution of operator training levels. No altered treatment estimate is established.

**Human verification steps:** Confirm the counted unit and category exclusivity, then reconcile the three bougie rows with 381 patients under footnote f using the original final-operator records.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

<a id="c004"></a>

## C004 — Duration confidence limits are printed in descending order

**Pending Human Adjudication**

**Candidate statement:** The all-patient duration-difference confidence interval is printed as 4 to −1 in a 95% CI column.

**Category:** Statistical reporting inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 3 all-patient duration interval vs REPORT main interval header and methods

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The mismatch is within the main REPORT between its interval and its header/range convention. The separate REPORT supplement corroborates plausible endpoint order under a disclosed different clustered analysis, adding no S_C discrepancy.

**Classification ambiguity:** None

**Exact source locations:** [jama_driver_2018_oi_180054.pdf — PDF p. 7](<../jama_driver_2018_oi_180054.pdf#page=7>), Table 3 all-patient duration row and Difference (95% CI) header; [jama_driver_2018_oi_180054.pdf — PDF p. 4](<../jama_driver_2018_oi_180054.pdf#page=4>), statistical methods, REPORT. [joi180054supp2_prod.pdf — PDF p. 2](<../joi180054supp2_prod.pdf#page=2>), eTable 1, and [joi180054supp2_prod.pdf — PDF p. 3](<../joi180054supp2_prod.pdf#page=3>), clustering note, REPORT corroboration/context.

**Source evidence:** Main medians 38/36 seconds; difference 1 (4 to −1), P=.24. Methods identify Hodges–Lehmann differences. Clustered supplement prints 1 (−1 to 4) seconds, P=.95 and discloses recalculated inferential columns.

**Reported-versus-comparator:** First interval endpoint 4 exceeds second −1, contrary to the lower-to-upper ordering used in other ranges. The clustered P value is a distinct analysis.

**Reasoning procedure:** Compare endpoint order directly, independently of the unknown variance/test implementation. Check estimate containment only diagnostically. Do not equate a Hodges–Lehmann estimate with subtraction of marginal medians. Checker provenance: NUM-A04, CROSS01 and STAT-A01; S040, N097 and X005/X064; identical interval/order comparisons merged.

**Calculation:** 4>−1. Sorting diagnostically gives [−1,4], containing 1; this does not determine the intended original limits. 38−36=2 need not equal the Hodges–Lehmann estimate 1.

**Alternative source-grounded interpretations:** The endpoints may have been transposed. The clustered supplement supports that possibility but cannot determine the main unclustered output. P=.24 versus .95 is not a matched-analysis contradiction.

**Mechanical evidence recheck:** Main printed endpoints, CI heading, methods and clustered-analysis context confirmed visually. Endpoint-order comparison reproduced. Original unclustered output remains unavailable for identifying intended limits; recorded_candidate is supported.

**Quality-control relevance:** A lower/upper interval field requires an unambiguous endpoint sequence.

**Potential downstream evidence impact:** If confirmed, extraction software could retain reversed lower and upper confidence-limit fields. No effect-estimate or conclusion change is demonstrated.

**Human verification steps:** Inspect the original unclustered Hodges–Lehmann output, confirm lower and upper limits and determine whether the printed sequence was intended.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

<a id="c005"></a>

## C005 — Historical rescue percentage differs from direct rounding

**Pending Human Adjudication**

**Candidate statement:** Protocol historical background gives 70 out of 88 as 79.6%, whereas the directly rounded fraction is 79.5% at one decimal.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol historical rescue counts vs PLAN same sentence percentage

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Counts and percentage occur in the same historical-background sentence inside the PLAN protocol. This is P_P plan material, with no conflicting trial REPORT result.

**Classification ambiguity:** None

**Exact source locations:** [joi180054supp1_prod.pdf — PDF p. 7](<../joi180054supp1_prod.pdf#page=7>), lines 198–199, with lines 196–203 as context; PLAN historical background.

**Source evidence:** Historical rescue background states 70 out of 88 (79.6%); nearby 20 out of 26 (76.9%) is coherent at one decimal.

**Reported-versus-comparator:** Printed 79.6% versus exact 79.5454545% and its direct one-decimal display 79.5%.

**Reasoning procedure:** Divide the printed counts and compare with the displayed one-decimal rounding interval. Qualify this rule as direct rounding; quoted historical precision or double rounding is not ruled out. Checker provenance: NUM-B01; N134/U010; independent support numeric checker.

**Calculation:** 100×70/88=79.5454545%. The 79.6% rounding interval [79.55,79.65) excludes the fraction by 0.0045455 percentage point. Printed-minus-exact is 0.0545455 point, above the 0.05 allowance. 100×20/26=76.9230769%→76.9%.

**Alternative source-grounded interpretations:** The protocol may preserve an externally quoted value or intermediate double rounding (79.545…→79.55→79.6). External articles were not accessed; supplied rounding provenance is absent.

**Mechanical evidence recheck:** Same-sentence counts, percentage and historical context confirmed visually; direct arithmetic reproduced. The unreported rounding/citation convention remains a human question. recorded_candidate and P_P were independently audited.

**Quality-control relevance:** Even a small display difference should retain a reproducible rounding basis for historical evidence extraction.

**Potential downstream evidence impact:** If confirmed, a reader could copy 79.6% as directly derived from 70/88. No dependence of this trial's conclusion on that difference is established.

**Human verification steps:** Determine whether 79.6% was intended as a directly rounded ratio, an intermediate-rounded figure or a preserved historical quotation, using the supplied sentence as the starting point.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

<a id="c006"></a>

## C006 — Planned duration and reported duration use different stop events

**Pending Human Adjudication**

**Candidate statement:** The planned first-attempt time-to-intubation measure ends at tracheal cuff inflation; the reported planned-secondary duration ends at blade removal.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol duration endpoint vs REPORT main and results-supplement duration endpoint

**Review domain:** protocol_report

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The discrepancy compares a PLAN protocol endpoint with agreeing REPORT definitions in the article and results supplement. The PLAN form heading defines an attempt, rather than the same stopwatch endpoint, so no independent P_P relationship is established. Agreeing REPORT locations add no S_C.

**Classification ambiguity:** Potentially distinct/amended secondary endpoint, without a supplied amendment resolving alignment.

**Exact source locations:** [joi180054supp1_prod.pdf — PDF p. 9](<../joi180054supp1_prod.pdf#page=9>), lines 315–317, and [joi180054supp1_prod.pdf — PDF p. 10](<../joi180054supp1_prod.pdf#page=10>), lines 346–347, PLAN. [jama_driver_2018_oi_180054.pdf — PDF p. 3](<../jama_driver_2018_oi_180054.pdf#page=3>), Trial Outcomes and Measurements; [jama_driver_2018_oi_180054.pdf — PDF p. 7](<../jama_driver_2018_oi_180054.pdf#page=7>), Table 3 duration rows/footnote c; [joi180054supp2_prod.pdf — PDF p. 2](<../joi180054supp2_prod.pdf#page=2>), duration rows, and [joi180054supp2_prod.pdf — PDF p. 3](<../joi180054supp2_prod.pdf#page=3>), dagger note, REPORT. [joi180054supp2_prod.pdf — PDF p. 10](<../joi180054supp2_prod.pdf#page=10>), attempt-definition heading preceding Q13, PLAN corroboration; Q13 itself is a device question.

**Source evidence:** Protocol time to intubation, first attempt only, runs from beginning of attempt to inflation of the ETT cuff in the trachea and is recorded with a stopwatch. Report duration runs from blade insertion to blade removal. Table 3 labels it a planned secondary outcome and prints 39/40 seconds for difficult airways and 38/36 seconds for all patients.

**Reported-versus-comparator:** PLAN cuff-inflation stop versus REPORT blade-removal stop for the named duration measure. The form attempt boundary does not independently specify the secondary stopwatch outcome.

**Reasoning procedure:** Compare endpoint identity and its planned-secondary label. Distinguish the named measure from the operational attempt definition. Different named events require a supplied equivalence, amendment or distinct-endpoint explanation; actual numerical divergence is not established. Checker provenance: NUM-B02, CROSS03 and STAT-A02; N140/N173/N184, X016 and S087; same duration-definition comparison merged.

**Calculation:** T_PLAN=t(cuff inflation)−t(attempt beginning); T_REPORT=t(blade removal)−t(blade insertion). If start events coincide, the difference is t(blade removal)−t(cuff inflation), which cannot be calculated from supplied aggregate summaries. No paired timestamps are available.

**Alternative source-grounded interpretations:** The reported measure could be distinct or deliberately amended; stop events might coincide operationally. The form may define attempt boundaries separately from successful-intubation stopwatch timing. No supplied amendment resolves the label alignment.

**Mechanical evidence recheck:** Both explicit definitions and planned-secondary label confirmed visually. Form locator clarified to the heading before Q13. Recheck corrects the provisional statistical P_P suggestion: final All relationships is P_R only. Missing paired timestamps, endpoint mapping and actual stopwatch instruction limit numerical interpretation; recorded_candidate is retained.

**Quality-control relevance:** Time outcomes require endpoint definitions before summaries or time models can be compared or combined.

**Potential downstream evidence impact:** If confirmed, a time-outcome extractor could combine seconds measured to different stop events under the same endpoint label. Changed durations, protocol violation and conclusion change are not demonstrated.

**Human verification steps:** Confirm which stop event generated the 39/40- and 38/36-second summaries and time analyses, including unsuccessful attempts, and identify any endpoint amendment or distinct-measure explanation.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

<a id="c007"></a>

## C007 — Primary missing-data instruction names a secondary composite

**Pending Human Adjudication**

**Candidate statement:** The protocol's primary missing-data clause instructs recovery of first-pass success without hypoxemia, while its primary definition is first-pass success alone.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol primary definition vs PLAN protocol primary missing-data endpoint wording

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The conflicting primary, secondary and missing-data definitions are all PLAN protocol content. Main REPORT primary wording is corroboration and adds no P_R discrepancy.

**Classification ambiguity:** None

**Exact source locations:** [joi180054supp1_prod.pdf — PDF p. 8](<../joi180054supp1_prod.pdf#page=8>), §2.1 lines 280–282; [joi180054supp1_prod.pdf — PDF p. 9](<../joi180054supp1_prod.pdf#page=9>), primary/secondary definitions, lines 284–295 and 304–312; [joi180054supp1_prod.pdf — PDF p. 20](<../joi180054supp1_prod.pdf#page=20>), §8.6.1 lines 719–720 continued at [joi180054supp1_prod.pdf — PDF p. 21](<../joi180054supp1_prod.pdf#page=21>), lines 721–722; all PLAN. [jama_driver_2018_oi_180054.pdf — PDF p. 3](<../jama_driver_2018_oi_180054.pdf#page=3>), primary wording, REPORT corroboration only.

**Source evidence:** Primary outcome: first-pass success. Secondary composite: first-pass success without hypoxemia. Paragraph beginning 'For the primary outcome' continues with video recovery to determine first-pass success without hypoxemia.

**Reported-versus-comparator:** Primary endpoint A versus missing-primary recovery label A∩B, where B is absence of hypoxemia.

**Reasoning procedure:** Compare endpoint names using the separately supplied definitions. A logical counterexample establishes different labels without establishing that any affected missing patient occurred. Checker provenance: NUM-B03, CROSS04 and STAT-A04; N136/N161, X024 and S089; identical endpoint-label comparisons merged.

**Calculation:** A successful first-attempt patient with hypoxemia satisfies A but not A∩B. Therefore A and A∩B are distinct endpoint definitions. No branch-use or affected-case count can be calculated from supplied material.

**Alternative source-grounded interpretations:** Secondary wording may have been copied into this clause; video review may have recovered both components independently while retaining primary A; the missing-data branch may have been unused.

**Mechanical evidence recheck:** Definitions and the two-page missing-primary instruction confirmed visually; logical comparison reproduced. Actual retrieval instruction, branch usage and coding logs are absent. P_P and recorded_candidate were confirmed and independently audited.

**Quality-control relevance:** The intended endpoint for a missing-data instruction must be distinguishable from a separately defined composite.

**Potential downstream evidence impact:** If confirmed, a plan extractor could attach a no-hypoxemia condition to the primary endpoint. No altered primary count or trial result is established.

**Human verification steps:** Determine whether the primary clause intended to recover first-pass success alone or the composite, and confirm what endpoint was coded if the video-recovery branch was used.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

<a id="c008"></a>

## C008 — Resistance percentage changes its named population

**Pending Human Adjudication**

**Candidate statement:** The discussion repeats a 7% resistance result under a bougie-group label, while the results describe all actual bougie use. An actual arm-specific numeric mismatch is not established.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main pooled bougie-use resistance result vs REPORT main discussion population label

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Both passages and group sizes are REPORT content within the main article, so the registered label comparison remains S_W. record_input_error records the unsupported alignment of pooled numerator 31 with randomized-arm denominator 381; it does not establish whether a residual label discrepancy exists.

**Classification ambiguity:** Identity of the repeated result and intended population label.

**Exact source locations:** [jama_driver_2018_oi_180054.pdf — PDF p. 5](<../jama_driver_2018_oi_180054.pdf#page=5>), Other Outcomes; [jama_driver_2018_oi_180054.pdf — PDF p. 7](<../jama_driver_2018_oi_180054.pdf#page=7>), continuation below Table 3; [jama_driver_2018_oi_180054.pdf — PDF p. 9](<../jama_driver_2018_oi_180054.pdf#page=9>), discussion; [jama_driver_2018_oi_180054.pdf — PDF p. 4](<../jama_driver_2018_oi_180054.pdf#page=4>), randomized group sizes; all REPORT.

**Source evidence:** Bougie use at any stage: 444 patients; resistance: 31 (7%), remedied in all but one. Discussion repeats 7% and the all-but-one remedy but refers to intubations in the bougie group. Randomized bougie arm n=381; its resistance numerator is not supplied.

**Reported-versus-comparator:** Pooled 31/444 reproduces 7%. Assigning the same 31 to 381 would yield 8%, but that assignment is unsupported and is not attributed to the authors' actual analysis.

**Reasoning procedure:** First establish population and numerator identity before comparing percentages. Repeated percentage/remedy wording suggests a shared result but does not prove it. Separate direct printed wording from conditional numerator reassignment. Checker provenance: CROSS02; X039 and N020 corroborating numeric scan. Numeric checker explicitly recognized the absent arm-specific numerator and did not emit a count candidate.

**Calculation:** 100×31/444=6.981982%→7%. Conditional 100×31/381=8.136483%→8%; this is unsupported conditional arithmetic, not a proven arm percentage. Possible arm counts 25–28 among 381 also round to 7%; they are not inferred actual counts.

**Alternative source-grounded interpretations:** Bougie group could informally mean all 444 actual bougie-use patients, or the discussion could describe a separately calculated randomized-arm proportion. The package does not settle the intended group or result identity.

**Mechanical evidence recheck:** Printed passages and arm total confirmed visually. Matched-result identity and the arm numerator are unavailable, so applicability is conditional only. The unsupported input alignment determines record_input_error and the mechanically derived discuss pre-fill. Independent audit preserves the stable ID and does not establish a numerical discrepancy.

**Quality-control relevance:** A repeated percentage needs an identifiable population before it can be reliably assigned to an analysis group.

**Potential downstream evidence impact:** If clarification establishes a label inconsistency, an extractor could attach a pooled proportion to the wrong population. Current evidence does not establish an arm event count or downstream error.

**Human verification steps:** Confirm whether discussion's bougie group means actual bougie-use patients or randomized assignment, and whether 7% repeats 31/444 or uses a separate arm-specific numerator and denominator.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

<a id="c009"></a>

## C009 — Hypoxemia window has a different end anchor

**Pending Human Adjudication**

**Candidate statement:** The planned hypoxemia observation window ends one minute after cuff inflation; REPORT definitions end one minute after first-attempt completion, whose duration ends at blade removal.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol hypoxemia observation window vs REPORT main and results-supplement observation window

**Review domain:** protocol_report

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** PLAN protocol definitions are compared with agreeing REPORT definitions in the article and results supplement. This is P_R only: REPORT repetition corroborates and creates no S_C; PLAN definitions do not conflict internally.

**Classification ambiguity:** Possible operational equivalence or amendment without paired timestamps or explicit supplied clarification.

**Exact source locations:** [joi180054supp1_prod.pdf — PDF p. 9](<../joi180054supp1_prod.pdf#page=9>), lines 304–312, and [joi180054supp1_prod.pdf — PDF p. 10](<../joi180054supp1_prod.pdf#page=10>), lines 340–354, PLAN. [jama_driver_2018_oi_180054.pdf — PDF p. 3](<../jama_driver_2018_oi_180054.pdf#page=3>), Measurements and Trial Outcomes; [jama_driver_2018_oi_180054.pdf — PDF p. 7](<../jama_driver_2018_oi_180054.pdf#page=7>), Table 3 footnotes b/c; [jama_driver_2018_oi_180054.pdf — PDF p. 9](<../jama_driver_2018_oi_180054.pdf#page=9>), Table 5 hypoxemia row/footnote b; [joi180054supp2_prod.pdf — PDF p. 3](<../joi180054supp2_prod.pdf#page=3>), asterisk/dagger notes, REPORT.

**Source evidence:** PLAN hypoxemia threshold is saturation <90%, or >10% drop if starting below 90%, through one minute after ETT cuff inflation. REPORT uses the same threshold but the window runs during or within one minute after completion of the attempt; reported attempt duration ends at blade removal. Reported hypoxemia fractions are 47/371 and 50/364; composites 156/191 versus 123/177 and 317/371 versus 282/366.

**Reported-versus-comparator:** PLAN cuff-inflation-plus-one-minute anchor versus REPORT attempt-completion-plus-one-minute anchor. Matching saturation thresholds do not establish matching observation windows.

**Reasoning procedure:** Compare the explicitly named time anchors separately from the saturation threshold. Keep event fractions as context; without timestamps and saturation trajectories, different printed definitions cannot be converted into changed event counts. Checker provenance: NUM-B04, CROSS05 and STAT-A03; N139/N143/N172, X017 and S088; same window rule merged, distinct from C006 continuous duration.

**Calculation:** End_PLAN=t(cuff inflation)+60 s; End_REPORT=t(first-attempt completion)+60 s. The report defines attempt duration by blade removal. Window offset and affected events cannot be calculated from aggregate fractions.

**Alternative source-grounded interpretations:** Cuff inflation and blade removal may coincide; observation may have been deliberately amended to attempt completion; completion might have an incompletely stated operational meaning. None of these is resolved by supplied data.

**Mechanical evidence recheck:** Thresholds, window definitions and reported fractions confirmed visually. Named-anchor comparison reproduced. Paired timestamps, saturation trajectories, failed-attempt/rescue rule and any explicit amendment/equivalence are missing. recorded_candidate and P_R were independently audited.

**Quality-control relevance:** An event proportion's ascertainment window forms part of its definition.

**Potential downstream evidence impact:** If confirmed, an extractor could attach a different observation window to reported hypoxemia/composite risks. Changed events, direction, magnitude and conclusion impact are not established.

**Human verification steps:** Confirm whether reported fractions used cuff inflation or first-attempt completion/blade removal as the end anchor, especially for failures and rescues, and identify any amendment or equivalence definition.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

<a id="c010"></a>

## C010 — Initial oxygen missingness does not reproduce its denominators

**Pending Human Adjudication**

**Candidate statement:** Table 1 initial oxygen threshold denominators do not equal arm totals minus the oxygen missingness assigned in footnote b, unless additional threshold exclusions apply.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 1 initial oxygen denominators vs REPORT same table missingness footnote

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The conflicting rows, headers and missingness footnote are REPORT content in one main-article table. Later start-of-attempt oxygen measurements have a different time point and are not conflicting comparators.

**Classification ambiguity:** None

**Exact source locations:** [jama_driver_2018_oi_180054.pdf — PDF p. 5](<../jama_driver_2018_oi_180054.pdf#page=5>), Table 1 initial oxygen median/threshold rows, headers and footnote b; all REPORT.

**Source evidence:** Arm n=381/376. Initial saturation <90%: 44/352 (13), 40/344 (12); <80%: 21/352 (6), 11/344 (3). Footnote b assigns oxygen missingness 43, split 19/24, using respectively. Heart-rate missingness is separately 61, split 29/32.

**Reported-versus-comparator:** Footnote-derived available counts 362/352 versus threshold denominators 352/344; printed denominators imply missingness 61 rather than 43.

**Reasoning procedure:** Under one initial oxygen measure, compute available cases as arm n minus missing values. Evaluate the possibility of additional threshold exclusions explicitly; do not infer a replacement from another vital sign or a later time point. Checker provenance: CROSS06; X048 and N028/N037/N038; two threshold rows share the same available-base comparison.

**Calculation:** 381−19=362; 376−24=352. Printed bases imply 381−352=29 and 376−344=32 missing, total 61; 61−43=18. Differences in available counts are 10 and 8. 19+24=43 is coherent, and displayed fractions correctly round using their printed bases.

**Alternative source-grounded interpretations:** Median and thresholds could use different availability rules with extra exclusions. Equality of implied threshold missingness to heart-rate missingness suggests a possible transcription mechanism, but does not establish it. No extra exclusion rule is supplied.

**Mechanical evidence recheck:** Rows, footnote's respectively assignment and initial-timepoint definition confirmed visually. Available-case arithmetic reproduced; additional threshold-only rules and median-contributing counts are unavailable. Same-measure applicability is conditional; unresolved alignment supports recorded_candidate.

**Quality-control relevance:** Available-case denominators should reconcile with the corresponding missingness definition.

**Potential downstream evidence impact:** If confirmed, an extractor could retain incompatible missing and available totals for the same initial saturation measure. No corrected denominator or treatment effect is established.

**Human verification steps:** Confirm whether initial saturation median and thresholds use the same eligible readings, and identify the missingness or threshold-exclusion rule reconciling arm totals, missing 19/24 and bases 352/344.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## Downstream Evidence-Chain Considerations

A downstream evidence product depends on accurate numerators, denominators, units, endpoint definitions and uncertainty fields. If a candidate is confirmed, even a small preventable reporting defect could be copied during structured extraction or synthesis. Relevant fields here include baseline proportions, operator categories, confidence limits, background percentages, time endpoints, event windows, missing-data labels, population labels and available-case totals.

These are bounded possibilities. The supplied evidence establishes no actual propagation, altered conclusion or serious harm. Endpoint-definition differences do not quantify changed seconds or events. An unsupported input alignment such as C008 requires population clarification before any arm-specific quantity can be attributed to the article.

## Limitations and Missing Definitions

All 49 source units and every registered relationship were covered. Remaining limits concern unavailable definitions, event-level inputs and execution context rather than omitted scientific source units. The complete maintained record is [limitations.md](review_1_6/limitations.md).

Only the three supplied PDFs are scientific evidence; raw data and external publications were outside scope. Historical extraction/render engines are UNKNOWN. Eight missing legacy PNGs are derivative gaps closed for scientific purposes by usable source-matched text and available direct rendering. OCR and Office conversion tools are absent; all sources are readable text-bearing PDFs, so no installation or fallback environment was needed. DOC-003 combines results with a prospective operational form, requiring content-based roles.

Exact chi-square implementation/continuity correction, analytic count-table definitions, binary interval formulas, interaction link/contrast/variance, continuous observations and rank/tie corrections, cluster sizes/covariance/algorithm, and Cox event times/test output are unavailable. Source-defined broad test classes do not establish all inferential constructions or test/interval inversion. No exact difficult-subgroup interim calculation can be reconstructed from the supplied interim summary.

Candidate-specific missing inputs include paired cuff-inflation/blade-removal timestamps and endpoint amendments (C006/C009), saturation trajectories and failed/rescue-attempt window rules (C009), primary missing-data retrieval/implementation logs (C007), an arm-specific resistance numerator and matched-result identity (C008), additional initial-saturation exclusion rules (C010), final-operator episode records (C003), and historical rounding provenance (C005). Intended row denominator conventions remain unresolved for C001/C002; original unclustered confidence limits are needed for C004.

### Six diagnostic P-value comparison limits

Both statistical passes retain these differences. Pearson and Yates values are **DIAGNOSTIC_APPROXIMATION**, independently recalculated from printed counts, with normal-tail approximation error about 1.5×10^-7. They are not identified author test outputs. The broad chi-square methods are stated on [jama_driver_2018_oi_180054.pdf — PDF p. 4](<../jama_driver_2018_oi_180054.pdf#page=4>); exact implementation, statistic and analytic table are unavailable.

| S ID / result | Source location (REPORT) | Printed inputs; P | Pearson diagnostic | Yates diagnostic | Exact human question |
|---|---|---|---|---|---|
| S007 etomidate | [jama_driver_2018_oi_180054.pdf — PDF p. 6](<../jama_driver_2018_oi_180054.pdf#page=6>), Table 2 | 332/381 vs 333/376; .54 | .548618 → .55 | .625129 → .63 | Which precise chi-square implementation, statistic and analytic count table generated .54? |
| S029 grade 2 view | [jama_driver_2018_oi_180054.pdf — PDF p. 6](<../jama_driver_2018_oi_180054.pdf#page=6>), Table 2 | 74/373 vs 62/359; .39 | .371672 → .37 | .424697 → .42 | Which exact implementation, statistic and analytic count table generated grade-2 .39? |
| S054 pneumothorax | [jama_driver_2018_oi_180054.pdf — PDF p. 9](<../jama_driver_2018_oi_180054.pdf#page=9>), Table 5 | 9/381 vs 9/376; .99 | .977373 → .98 | 1.000000 → 1.00 | Which exact implementation, statistic and analytic count table generated .99? |
| S021 faculty operator | [jama_driver_2018_oi_180054.pdf — PDF p. 6](<../jama_driver_2018_oi_180054.pdf#page=6>), Table 2 | 8/381 vs 5/376; .42 | .414910 → .41 | .592294 → .59 | Which analytic row inputs and exact test generated .42, given unresolved final-operator counts in C003? Do not change a count to force agreement. |
| S034 no device | [jama_driver_2018_oi_180054.pdf — PDF p. 6](<../jama_driver_2018_oi_180054.pdf#page=6>), Table 2 | 5/381 vs 6/376; .75 | .744575 → .74 | .982394 → .98 | Which implementation, statistic and analytic count table generated .75? |
| S052 any complication | [jama_driver_2018_oi_180054.pdf — PDF p. 9](<../jama_driver_2018_oi_180054.pdf#page=9>), Table 5 | 66/381 vs 63/376; .83 | .835511 → .84 | .911640 → .91 | Which implementation, statistic and analytic count table generated .83? |

These checks remain human questions rather than stable candidates because no supplied-source-compatible contradiction is established under the exact author analysis. They do not establish the printed P values as correct, and no unexplained difference is silently attributed to rounding. All six remain in the durable inventory and completed second-pass record.

S025 illustrates the implementation boundary: 218/377 versus 182/372 has printed P=.02, Pearson diagnostic .014630 and Yates diagnostic .017877, with Yates reproducing the printed precision. S049 grade-4 success (3/3 versus 2/5), difference 60 (17–100), P=.09 has Pearson diagnostic .089686; the source does not establish inferential inversion between its difference interval and chi-square test. Neither yields a separate candidate. Clustered duration inference cannot be reconstructed from median/IQR or identical rounded interval endpoints alone.

### Execution-context limitation

The user explicitly requested the current provider even where workflow controls name OpenRouter. That instruction was honored. The original session launch command and coordinator runtime model cannot be independently attested through the available interface. The configured coordinator contract and all nine exposed named presets match gpt-6.1-sol and their required efforts.

The truthful [routing preflight](review_1_6/routing_preflight.md) records PASS_WITH_USER_OVERRIDE, CURRENT_SESSION_PROVIDER and CURRENT_INTERACTIVE_SESSION, and does not fabricate the original launch. The unmodified validator requires Status PASS, Provider openrouter, Execution mode INTERACTIVE_CLI and Launch command codex --approve-for-me. These four strict execution-context requirements cannot pass under the current record. Scientific coverage completion is separately supported; the actual [validation JSON](review_1_6/review_validation.json) is produced after coordinator rendering and final checks. No unconditional strict PASS is asserted.

## Human Adjudication Checklist

For each stable ID, inspect the linked physical source page, verify numerator/denominator or endpoint identity, reproduce the stated arithmetic/logical rule and resolve the named alternative or missing definition. Preserve differences between direct printed observations and conditional diagnostics.

Record the human decisions only in the five blank fields on that card. Determine validity, importance and any action, then add initials and notes. All ten candidates remain Pending Human Adjudication until that human review occurs. Mechanical evidence states and suggested dispositions do not supply those decisions.

Before using a candidate in evidence extraction, confirm its population, time point, estimator, analysis adjustment and unit. For C008, establish the actual numerator/population identity before interpreting a numeric mismatch. For C006/C009, do not infer changed times or events without the missing source inputs. No final correction is assigned by this report.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Canonical review artifacts

The complete current review is reconstructible from the [source inventory](review_1_6/source_inventory.md), [asset inventory](review_1_6/evidence_asset_inventory.md), [source coverage](review_1_6/source_coverage.md), [coverage manifest](review_1_6/coverage_manifest.md), [main map](review_1_6/extraction/main_quantitative_evidence.md), [support map](review_1_6/extraction/support_quantitative_evidence.md), [numeric inventory](review_1_6/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_6/statistics/relationship_inventory.md), [numeric review](review_1_6/checkers/numeric_consistency.md), [cross-source review](review_1_6/checkers/cross_source_consistency.md), [statistical pass 1](review_1_6/checkers/statistical_pass_1.md), [statistical pass 2](review_1_6/checkers/statistical_pass_2.md), [candidate ledger](review_1_6/candidate_ledger.md), [recheck](review_1_6/verification/evidence_recheck.md) and [independent audit](review_1_6/quality/evidence_quality_audit.md). All ten stable IDs are represented here without a count-based omission.

### Source integrity and tooling

| Source file | Baseline SHA-256 |
|---|---|
| jama_driver_2018_oi_180054.pdf | `684db2edf58f16d1d24e8ddb6a463429b027450314c923e06700acdd0167e7d2` |
| joi180054supp1_prod.pdf | `38c1822278c238d2e9f217cd626c307b9d7ad8152f93f3281a03f58990e6108c` |
| joi180054supp2_prod.pdf | `b8b7e9731b69407ff10ffc262eb42477965333e3697461e848d8fe50e13b4b31` |

The independent coverage audit checked all three source hashes and all 47 reused-asset hashes against their before snapshots with no differences. The coordinator recomputes final after snapshots during finalization. Baselines: [source hashes](review_1_6/source_hashes_before.sha256) and [reused hashes](review_1_6/reused_artifact_hashes_before.sha256). Final snapshots: [source hashes after](review_1_6/source_hashes_after.sha256) and [reused hashes after](review_1_6/reused_artifact_hashes_after.sha256). Supplied sources and all pre-existing audit assets were preserved.

The local CPU tooling record reports Linux, direct pdfinfo/pdftotext/pdftoppm/pdftocairo available (Poppler 25.03.0), Pandoc 3.1.11.1, GNU sha256sum 9.7 and Python 3.13.5 for allowed auxiliary helpers. Tesseract and LibreOffice are unavailable. Fallback environment: NOT_NEEDED; packages/capabilities: None; environment removed: NOT_CREATED. No global installation, OCR or GPU operation was needed. The user's temporary-folder environment preference remains applicable if future installation becomes necessary. Complete probe and derivative engines appear in [tooling_record.md](review_1_6/tooling_record.md).

### Agent execution

All actual agents, including the coordinator and two optional bounded support shards, appear below. Mandatory specialist stages used fresh, distinct spawns. Runtime identifiers use `task:` plus the exact canonical task name exposed by the collaboration tool; opaque numerical runtime IDs are not exposed. The model column records the package coordinator contract and the tool-defined named specialist presets. Independent runtime coordinator-model attestation is unavailable; current-provider authorization is preserved.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | task:/root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | task:/root/asset_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | task:/root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | task:/root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | task:/root/numeric_main | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| numeric_consistency_support_shard | task:/root/numeric_support | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support.md |
| statistics_pass_1 | task:/root/statistics_one | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| cross_source_consistency_reviewer | task:/root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| evidence_rechecker | task:/root/rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | task:/root/statistics_two | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| coverage_quality_support | task:/root/coverage_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_audit.md |
| quality_control_auditor | task:/root/final_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | task:/root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Artifact paths in the table are relative to `review_1_6/`. The report generator additionally owns this complete Markdown report. The [execution manifest](review_1_6/agent_execution_manifest.md) is the authoritative roster. Both statistical passes used distinct fresh gpt-6.1-sol/high agents; mapping, numeric, cross-source and report roles used medium effort; recheck and quality audit used high effort.

### Reproducibility performance

- **Target basis:** Three PDFs with 49 pages, all covered by usable reusable native/layout text and 41 rendered pages; 0 fresh-required pages; mixed PLAN and REPORT supplemental content, numerical tables and figures, no Office conversion or OCR expected, ten mandatory specialist stages in sequential and parallel waves, two independent statistical passes, and direct-source rechecks.
- **Total source units:** 49
- **Fresh-source units:** 0
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T00:43:54Z
- **Finished UTC:** 2026-10-11T01:18:05Z
- **Observed elapsed minutes:** 34.18
- **Target status:** MET_TARGET
- **Exceedance causes:** None

These exact field values are copied from [run_state.md](review_1_6/run_state.md). The coordinator fills Finished UTC, observed elapsed time and target status immediately after complete Markdown assembly, and updates bounded exceedance causes if needed. The target considers reuse fitness, mixed PLAN/REPORT content, numerical tables/figures, agent waves and direct rechecks rather than page count alone. Local HTML rendering and mechanical validation are outside the scientific review timing window; later model-based repair requires updated finish and timing values.

