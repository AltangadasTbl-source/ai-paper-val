# Quantitative Quality-Control Consistency Review — Workflow 1.6.2

**Pending Human Adjudication.** All thirteen candidates below are reporting issues prepared for human adjudication. Evidence states and inclusion audits describe this review's records; they do not determine the authors' intended values or a final correction.

## Executive Quality-Control Summary

Complete review of the four supplied PDFs identified **13 stable candidates** from **25 independently screened findings**. Twenty-four findings were included and consolidated into the thirteen issues; one finding was screened out because its immediate quantitative context resolved it. Every candidate has a source-page mechanical recheck, a reproduced evidence state and a CONFIRMED inclusion audit.

The candidates concern signed estimates, comparator composition, primary outcome and analysis definitions, scoring and power specifications, modeled point contrasts and interval widths, treatment-specific safety reporting, and count/percentage consistency. Eight belong to statistical_results, four to protocol_report and one to plan_material. No candidate was assigned to report_internal_inconsistency. No paper-level conclusion change is inferred.

## Package and Reused-Evidence Provenance

The package concerns the randomized krill-oil trial reported by Laslett and colleagues. Documents are classified by content: the main article and results tables are REPORT material; the prospective protocol and statistical analysis plan (SAP) are PLAN material. One source unit is one physical PDF page, including covers, references and administrative material.

| Source ID | Supplied source and evidence locator | Role | Physical pages |
|---|---|---|---:|
| DOC-001 | [jama_laslett_2024_oi_240048_1727199125.7595.pdf](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=1), main article | REPORT | 10 |
| DOC-002 | [joi240048supp1_prod_1727199125.7845.pdf](../joi240048supp1_prod_1727199125.7845.pdf#page=1), protocol version 02, February 2016 | PLAN | 15 |
| DOC-003 | [joi240048supp2_prod_1727199125.8245.pdf](../joi240048supp2_prod_1727199125.8245.pdf#page=1), SAP excerpt | PLAN | 1 |
| DOC-004 | [joi240048supp3_prod_1727199125.83025.pdf](../joi240048supp3_prod_1727199125.83025.pdf#page=1), results supplement | REPORT | 15 |
| Total | Four supplied PDFs; no supplied Office, workbook or CSV source | — | 41 |

The curator inventoried and hashed 116 eligible existing evidence assets: 58 USABLE, 16 PARTIAL and 42 DUPLICATE; none were STALE or UNREADABLE. Assets include native/layout text, rendered pages and source/document maps. Partial and duplicate assets served only as eligible locators or provenance. No earlier candidate selection, screening judgment or report conclusion supplied the discovery scope.

Canonical source-matched reusable text covered the main article, SAP and results supplement, plus thirteen protocol pages. Exact native-text agreement alone did not cover the historical numeric figures on protocol pages 4–5; those two pages were freshly rendered and mapped on the CPU. Every page was scientifically reconstructed in this run. The [source inventory](review_1_6_2/source_inventory.md) and [evidence-asset inventory](review_1_6_2/evidence_asset_inventory.md) retain full identities, locations, fitness assessments and extraction-engine provenance.

## Scope, Complete Coverage, and Exclusions

The review covers counts and denominators; estimate, interval and test logic; statistical method logic; and planned versus reported statistical design. It uses only supplied package evidence. Discovery and classification were rebuilt, with reusable derivatives acting as locators and transcription aids. Exact supplied pages were the authority for mechanical candidate confirmation.

| Source | Total units | Reusable units | Fresh-required units | Mapped units | Coverage |
|---|---:|---:|---:|---:|---|
| DOC-001 | 10 | 10 | 0 | 10 | COMPLETE |
| DOC-002 | 15 | 13 | 2 | 15 | COMPLETE |
| DOC-003 | 1 | 1 | 0 | 1 | COMPLETE |
| DOC-004 | 15 | 15 | 0 | 15 | COMPLETE |
| Total | 41 | 39 | 2 | 41 | COMPLETE |

The main scope comprises all three tables, two figures, narrative repetitions and statistical definitions. Support scope comprises all eight eTables, the eFigure, complete protocol/SAP design statements and all eighteen planned secondary endpoint items. Cover, reference, administrative and historical units have explicit completion records. The [source-coverage ledger](review_1_6_2/source_coverage.md) and [coverage manifest](review_1_6_2/coverage_manifest.md) record the complete assignments and durable outputs. No scientific coverage gap remains.

The scope excludes broad clinical, study-design, novelty, misconduct and raw-data audits, and preferences for another analysis. Differences resolved by field context, display precision, notation or terminology are excluded. Model-based estimates are not required to equal crude differences or ratios. Peripheral copied descriptive values, time-specific contributor counts and administrative details are excluded unless they alter a primary or key secondary result, analysis-population size or planned decision rule. A tiny P value displayed as zero cannot alone qualify.

For numeric reproduction, each printed input and comparator receives its half-unit rounding interval. A residual relative gap at most 0.05 is treated as display precision; a greater gap, or a positive gap against printed zero, reproduces the discrepancy. Interval-versus-P/test conflicts are exempt from this rounding exclusion. Diagnostic normal-power and empirical interval-width calculations are expressly distinguished from unpublished fitted-model calculations.

## Quantitative and Statistical Relationship Coverage

The main mapper reconstructed 127 local evidence bundles across ten pages. The support mapper reconstructed all thirty-one support pages, including 65 supplementary inferential rows: three primary sensitivity rows and 62 eTable 4 endpoint/time rows. Its integral page transcriptions preserve all displayed cells and definitions.

The numeric inventory contains 197 relationships: N001–N099 and N101–N198, reviewed in disjoint main and support scopes and merged without loss. N100 is unused; it does not represent an uncovered relationship. The statistical inventory contains 104 relationships, S001–S104: 68 distinct current-result tuples, with matched repetitions, plus 36 method, design and historical records. Numeric and statistical identifiers track relationships rather than findings and therefore are not added to form a unique-result count.

Two different fresh gpt-6.1-sol/high statistical agents covered every S relationship. Each inventory row has PASS_1_COMPLETE and PASS_2_COMPLETE. Checks included containment, endpoint order, null/P agreement, direction and effect-measure identity, same-display reproducing methods, model/population matching, planned analyses and power specifications. No categorical interval-null/P significance conflict was established among the supplied result tuples.

Pass 2 revisited the complete ledger, screening and recheck facts, and all 49 upstream excluded-observation rows. It emitted one additional finding, F-ST2-001, concerning the WOMAC total-pain 24-week interval. A different fresh screener included it and consolidated its occurrences into C012's interval-width pattern; a different fresh rechecker confirmed the expanded card. The final auditor reviewed all 49 upstream rows and all 37 unique pass-2 excluded rows in both directions and established no additional finding. Excluded-observation bookkeeping is distinct from the canonical finding-decision counts below.

Full evidence is retained in the [main map](review_1_6_2/extraction/main_quantitative_evidence.md), [support map](review_1_6_2/extraction/support_quantitative_evidence.md), [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md), [statistical inventory](review_1_6_2/statistics/relationship_inventory.md), [first statistical pass](review_1_6_2/checkers/statistical_pass_1.md) and [second statistical pass](review_1_6_2/checkers/statistical_pass_2.md).

## Inclusion Screening Summary

Inclusion requires reproduction and either a Route A always-register category or all three Route B criteria: in focus, unresolved by immediate context and consequential to a named interpretation or extraction value. There is no expected number of candidates. Repeated occurrences remain within one issue when the same supported rule fails without an established separate cause.

| Screening stage | Findings | INCLUDE | SCREENED_OUT |
|---|---:|---:|---:|
| Initial numeric, cross-source and statistical-pass-1 screen | 24 | 23 | 1 |
| Independent statistical-pass-2 finding screen | 1 | 1 | 0 |
| Total | 25 | 24 | 1 |

| Decision | Reason code | Findings |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 24 |
| SCREENED_OUT | CONTEXT_RESOLVES | 1 |
| Total | — | 25 |

All other screened-out reason codes have zero canonical finding decisions. F-NUM-005 is the sole screened-out finding: the matching supplementary RR/log-binomial definition, binary proportions and ratio-shaped interval identify the main responder measure. No independent numeric or null/test contradiction remains. It has no candidate card. Multiple INCLUDE findings share a candidate when they describe the same issue; the 24 included findings map to thirteen stable IDs. The [canonical screening log](review_1_6_2/screening/inclusion_screen.md) contains exactly one decision per finding and preserves both independent screening stages.

## Review-Domain Summary

Review domains pre-fill human review. statistical_results covers counts, estimates, intervals, tests and statistical methods in REPORT material. report_internal_inconsistency covers conflicting result attribution within REPORT material. protocol_report covers statistical design or analysis differences between PLAN and REPORT. plan_material covers statistical-design inconsistencies confined to PLAN material.

| Review domain | Stable candidates |
|---|---:|
| statistical_results | 8 |
| report_internal_inconsistency | 0 |
| protocol_report | 4 |
| plan_material | 1 |
| Total | 13 |

| Primary relationship type | Meaning | Stable candidates |
|---|---|---:|
| S_C | Between different REPORT documents | 3 |
| S_W | Within a REPORT document | 5 |
| P_R | PLAN compared with REPORT | 4 |
| P_P | Within PLAN material | 1 |
| Total | — | 13 |

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 13 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| Total | 13 |

All thirteen inclusion audits are CONFIRMED; none are QUESTIONED. These labels are inclusion-record facts, not adjudications. C001 includes S_C and S_W, with S_C primary under the prescribed precedence P_R > P_P > S_C > S_W. Corroborating documents alone do not add a relationship.

## Candidate Index

| ID and candidate | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|
| [C001 — Primary signed contrast differs between report locations](#c001--primary-signed-contrast-differs-between-report-locations) | statistical_results | S_C | reproduced | CONFIRMED |
| [C002 — Placebo composition percentages differ by a decimal place](#c002--placebo-composition-percentages-differ-by-a-decimal-place) | statistical_results | S_W | reproduced | CONFIRMED |
| [C003 — Primary VAS recall periods differ between plan and report](#c003--primary-vas-recall-periods-differ-between-plan-and-report) | protocol_report | P_R | reproduced | CONFIRMED |
| [C004 — ICOAP item count does not identify the scoring denominator](#c004--icoap-item-count-does-not-identify-the-scoring-denominator) | statistical_results | S_W | reproduced | CONFIRMED |
| [C005 — Adopted power specifications differ between plan and report](#c005--adopted-power-specifications-differ-between-plan-and-report) | protocol_report | P_R | reproduced | CONFIRMED |
| [C006 — Reported primary model differs from the supplied planned model](#c006--reported-primary-model-differs-from-the-supplied-planned-model) | protocol_report | P_R | reproduced | CONFIRMED |
| [C007 — Planned per-protocol primary efficacy analysis is not reported](#c007--planned-per-protocol-primary-efficacy-analysis-is-not-reported) | protocol_report | P_R | reproduced | CONFIRMED |
| [C008 — Repeated modeled arm-change and point-contrast discrepancies](#c008--repeated-modeled-arm-change-and-point-contrast-discrepancies) | statistical_results | S_W | reproduced | CONFIRMED |
| [C009 — Selected adverse-event counts change treatment attribution](#c009--selected-adverse-event-counts-change-treatment-attribution) | statistical_results | S_C | reproduced | CONFIRMED |
| [C010 — Serious-event relatedness classifications do not reconcile](#c010--serious-event-relatedness-classifications-do-not-reconcile) | statistical_results | S_C | reproduced | CONFIRMED |
| [C011 — Planned effusion power does not reproduce from supplied inputs](#c011--planned-effusion-power-does-not-reproduce-from-supplied-inputs) | plan_material | P_P | reproduced | CONFIRMED |
| [C012 — Repeated contrast-interval widths differ from a reproducing display rule](#c012--repeated-contrast-interval-widths-differ-from-a-reproducing-display-rule) | statistical_results | S_W | reproduced | CONFIRMED |
| [C013 — WORMS smaller-one-unit percentages differ from their counts](#c013--worms-smaller-one-unit-percentages-differ-from-their-counts) | statistical_results | S_W | reproduced | CONFIRMED |

## Candidate Evidence Cards

In the cards, K denotes krill oil and P denotes placebo. Weeks identify follow-up; continuous comparisons use modeled changes rather than crude baseline-to-follow-up differences. Each card retains every affected occurrence and the diagnostic assumptions needed to reproduce its comparison.

## C001 — Primary signed contrast differs between report locations

Pending Human Adjudication.

**Candidate statement:** The primary 24-week VAS treatment contrast is printed positive in Key Points and negative in matched main and supplementary result copies.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main Key Points vs REPORT main abstract/Table 2/text and REPORT results original/VAS24 copies

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001, F-XS-001

**Qualifying route:** Route A, category 2

**Classification rationale:** Both within-main and cross-report values are compared; S_C takes precedence over S_W. No PLAN conflict is assigned.

**Classification ambiguity:** None; the rechecker confirmed the supplementary copies are directly conflicting comparators.

**Exact source locations:** DOC-001 [p1 abstract](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=1), [p2 Key Points](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2), [p6 Table 2](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), [p7 primary text](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7); DOC-004 [p2 original row](../joi240048supp3_prod_1727199125.83025.pdf#page=2), [p5 VAS24](../joi240048supp3_prod_1727199125.83025.pdf#page=5).

**Source evidence:** REPORT [main p2 Key Points](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2) prints mean difference 0.30, 95% CI −6.9 to 6.4, P=.94. REPORT [main p1 abstract](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=1), [p6 Table 2 primary row](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), and [p7 Primary Outcome](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7) each print −0.3 with that interval; Table 2/body give P=.94. REPORT [results p2 eTable 1 original-data row](../joi240048supp3_prod_1727199125.83025.pdf#page=2) prints −0.27 (−6.92 to 6.38), P=.94, and modeled changes −19.93/−20.21. REPORT [results p5 knee VAS week24](../joi240048supp3_prod_1727199125.83025.pdf#page=5) prints −0.3 (−6.9 to 6.4), P=.94. All concern primary knee VAS change at 24 weeks. Age-adjusted/imputed results are distinct rows and are not silently substituted.

**Reported-versus-comparator:** Key Points +0.30 versus main/result-supplement −0.3 and original-analysis −0.27, with matching outcome, follow-up and interval.

**Reasoning procedure:** Match the primary outcome, analysis and week across six locations, preserve the printed signs and compare their precision intervals; distinguish age/imputation sensitivity rows.

**Calculation:** Route A, category 2: direction-changing printed sign. Positive interval [.295,.305] versus main/results −.3 interval [−.35,−.25] leaves gap .545/.30=1.8167. Against the original −.27 interval [−.275,−.265], gap .560/.30=1.8667. Negative −.27 and −.3 copies overlap at their displayed precision. The ordinary displayed contrast −20.2−(−19.9)=−.3 supports the negative direction but does not identify the Key Points convention. Neither null exclusion nor significance differs.

**Affected result or extracted value:** Primary 24-week knee VAS signed mean-change contrast.

**Why context does not resolve it:** Route A, category 2: a printed sign changes the extracted direction. Reconstructing the negative contrast elsewhere does not remove the printed positive occurrence.

**Alternative source-grounded interpretations:** An opposite contrast or unsigned magnitude could be intended. Reversing the contrast also reverses the CI orientation to −6.4 to 6.9; the printed interval remains −6.9 to 6.4. Opposite signs are directly observed; their production mechanism is inferred and not assigned.

**Mechanical evidence recheck:** The independent rechecker found every cited source and comparator location, visually matched their printed values/text, confirmed the rule and reproduced the comparison with the stated precision allowances. Source roles and relationships were confirmed from content. reproduced. The positive printed Key Points value is present and does not reconcile with matched signed primary copies after display allowances. Exact remaining human question: Which signed treatment contrast and group order belong to the primary estimate and its printed interval in Key Points?

Inputs and bounded missing definitions: Exact values, matched endpoint/time/CI and treatment changes are available. The explicitly intended group order or absolute-magnitude convention for Key Points is not supplied.

**Potential downstream evidence impact:** If confirmed, an extractor could copy opposite signed primary estimates from different report locations. The printed intervals and nonsignificant interpretation are unchanged by this observation.

## C002 — Placebo composition percentages differ by a decimal place

Pending Human Adjudication.

**Candidate statement:** The same placebo mass-concentration bound is paired with percentages differing by one decimal place.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Methods vs REPORT main Discussion placebo percentages

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-002, F-XS-008

**Qualifying route:** Route A, category 2

**Classification rationale:** Conflicting percentages occur within the main REPORT; S_W.

**Classification ambiguity:** None.

**Exact source locations:** DOC-001 [p2 intervention last line](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2), [p3 continuation](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3), [p9 Discussion](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=9).

**Source evidence:** REPORT [main p2 Interventions last line](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2) prints less than 5 mg/g (0.5%), completed as other omega-3 content at REPORT [main p3 first continuation](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3). REPORT [main p9 Discussion](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=9) describes the same oil without EPA/DHA and less than 5 mg/g (0.05%) other omega-3.

**Reported-versus-comparator:** Methods <5 mg/g (0.5%) versus Discussion <5 mg/g (0.05%) for other omega-3 content.

**Reasoning procedure:** Match the randomized comparator description, convert the mass ratio to a percentage and compare both parenthetical values after precision allowances.

**Calculation:** Route A, category 2: magnitude-changing decimal. Percentage intervals [.45,.55]% and [.045,.055]% leave .395 percentage-point gap/.5=.79 (or /.05=7.9). Since 1 g=1000 mg, 5 mg/g corresponds to .5%; allowing 5±.5 mg/g yields [.45,.55]% and the same discrepancy against .05%. This compares parenthetical concentration bounds, not measured unreported oil concentrations.

**Affected result or extracted value:** Placebo other-omega-3 concentration bound and percentage.

**Why context does not resolve it:** Route A, category 2: the decimal changes the printed concentration magnitude. A possible actual concentration satisfying both inequalities does not reconcile their parenthetical conversions.

**Alternative source-grounded interpretations:** An actual concentration could satisfy both inequalities; that does not equate their printed parenthetical conversions. A differing intended bound or decimal-position substitution is possible. The tenfold printed percentage difference is observed; a mechanism is not established.

**Mechanical evidence recheck:** The independent rechecker found every cited source and comparator location, visually matched their printed values/text, confirmed the rule and reproduced the comparison with the stated precision allowances. Source roles and relationships were confirmed from content. Evidence state is reproduced, determined by the printed .5%/.05% separation. Exact remaining human question: Which mass-concentration bound and parenthetical percentage describe the randomized placebo's other omega-3 composition?

Inputs and bounded missing definitions: Both concentration/percentage copies and unit conversion are available. Actual concentration and whether a distinct upper bound was intended are absent.

**Potential downstream evidence impact:** If confirmed, comparator-composition extraction could retain a tenfold difference in the printed percentage bound. Actual composition or an efficacy mechanism is not inferred.

## C003 — Primary VAS recall periods differ between plan and report

Pending Human Adjudication.

**Candidate statement:** The supplied plan and report use distinct recall periods for the primary VAS pain endpoint.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol primary VAS definition vs REPORT main primary VAS definition and Table 1 footnote

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002, F-ST1-005

**Qualifying route:** Route B

**Classification rationale:** PLAN versus REPORT endpoint window; P_R and protocol_report.

**Classification ambiguity:** An unsupplied amended instrument could reconcile the windows.

**Exact source locations:** DOC-001 [p3 primary outcome](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3), [p5 Table 1 footnote b](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=5); DOC-002 [p6 primary definition](../joi240048supp1_prod_1727199125.7845.pdf#page=6), [p8 primary question](../joi240048supp1_prod_1727199125.7845.pdf#page=8).

**Source evidence:** PLAN [protocol p6 Primary outcome](../joi240048supp1_prod_1727199125.7845.pdf#page=6) identifies 24-week VAS knee-pain change; PLAN [protocol p8 Primary outcome: Pain](../joi240048supp1_prod_1727199125.7845.pdf#page=8) specifies a 100-mm VAS question asking pain today. REPORT [main p3 Primary Outcome](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3) defines 24-week change in VAS pain over the past 7 days; REPORT [main p5 Table 1 footnote b](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=5) repeats the past-7-days definition.

**Reported-versus-comparator:** Protocol pain today versus reported pain over the past seven days, both attached to the primary 24-week VAS change.

**Reasoning procedure:** Match primary status, index knee, scale and follow-up, then compare the categorical recall window; numerical rounding is inapplicable.

**Calculation:** Route B, focus D: the reference period is part of the primary endpoint definition. Today and past 7 days differ despite the matching scale/time of follow-up. Half-unit numerical precision is inapplicable to this categorical window comparison. The discrepancy affects definition extraction for the primary −.3 contrast.

**Affected result or extracted value:** Recall period defining the primary 24-week VAS pain estimate.

**Why context does not resolve it:** The common scale and follow-up do not identify one administered recall window. No supplied questionnaire version or amendment bridges today and the past seven days; this is an endpoint definition, not synonymous wording.

**Alternative source-grounded interpretations:** The instrument may have changed or both recall items may have been collected. Printed window difference is observed; which question generated the primary analysis is not directly observed.

**Mechanical evidence recheck:** The independent rechecker found every cited source and comparator location, visually matched their printed values/text, confirmed the rule and reproduced the comparison with the stated precision allowances. Source roles and relationships were confirmed from content. Evidence state is reproduced, determined by the two distinct printed primary reference periods. Exact remaining human question: Which recall period was administered for the analyzed primary VAS, and what dated instrument or amendment connects the supplied definitions?

Inputs and bounded missing definitions: Both endpoint passages and recall statements are available. The administered questionnaire, version/date, or amendment linking the windows is absent.

**Potential downstream evidence impact:** If confirmed, primary outcome extraction could attach different reference periods to the same reported effect. The administered question and any amendment remain unspecified.

## C004 — ICOAP item count does not identify the scoring denominator

Pending Human Adjudication.

**Candidate statement:** The printed ICOAP question count and scoring maxima do not jointly identify the intermittent and total normalization denominators.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main ICOAP scoring ranges vs REPORT main item-count/scoring definition

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-003

**Qualifying route:** Route B

**Classification rationale:** Quantitative scoring definition within one REPORT; S_W and statistical_results.

**Classification ambiguity:** A field-specific item convention is possible but no external definition is used.

**Exact source locations:** DOC-001 [p4 post hoc scoring](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p5 Table 1 footnote g](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=5), [p6 ICOAP rows/descriptions](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6).

**Source evidence:** REPORT [main p4 Post Hoc Outcomes](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4) gives item scoring 0–4, raw total 0–44, constant 0–20, intermittent 0–24, all rescaled to 0–100. REPORT [main p5 Table 1 footnote g](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=5) states five constant questions and eight on pain that comes and goes. REPORT [main p6 ICOAP rows and footnote d](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6) uses these descriptions for the reported rescaled outcomes.

**Reported-versus-comparator:** Eight intermittent questions scored 0–4 versus intermittent maximum 24; five constant questions imply maximum 20, while the printed total maximum is 44.

**Reasoning procedure:** Apply the source-supported additive scoring interpretation explicitly, allow conservative input precision and compare the intermittent maximum; retain branching, weighting or unscored-question conventions as alternatives.

**Calculation:** Route B, focus C: the printed numbers do not jointly specify an additive scoring denominator. Eight×four implies maximum 32, five×four=20, and their sum maximum is 52 rather than 44. Even conservative literal half-unit inputs [7.5,8.5]×[3.5,4.5]=[26.25,38.25] versus printed 24 interval [23.5,24.5] leave gap 1.75/24=.0729167. Integer scale definitions normally are exact; the broader rounding envelope still does not reconcile the intermittent maximum. The total discrepancy is consequential to the same scoring-definition issue.

**Affected result or extracted value:** ICOAP scored-item definition and raw-to-0–100 normalization denominators.

**Why context does not resolve it:** The source gives neither a scored-versus-unscored item distinction nor weights or branching rules connecting eight intermittent questions to maximum 24. A statistically literate reader cannot identify the denominator from the supplied passages alone.

**Alternative source-grounded interpretations:** Eight questions could include items omitted from the score, or a weighting/branching rule could produce maximum 24. The source does not supply such a bridge. Counts/ranges are observed; eight scored equal-weight items is an explicit diagnostic interpretation, not an externally imposed instrument version.

**Mechanical evidence recheck:** The independent rechecker found every cited source and comparator location, visually matched their printed values/text, confirmed the rule and reproduced the comparison with the stated precision allowances. Source roles and relationships were confirmed from content. Evidence state is reproduced, determined by the unresolved printed count/raw-maximum combination under the source-supported additive reading and its precision envelope. Exact remaining human question: Which of the eight intermittent questions contributed to the raw 0–24 score, and which denominators normalized the intermittent and total ICOAP outcomes?

Inputs and bounded missing definitions: Printed question counts, item maximum, subscale maxima and rescaling destination are available. Which questions contribute to the intermittent sum, any unscored branching questions/weights, and exact rescaling denominator are absent.

**Potential downstream evidence impact:** If confirmed, an extractor could use an unresolved item count or raw maximum when recording scale normalization. No change in an observed treatment effect is asserted.

## C005 — Adopted power specifications differ between plan and report

Pending Human Adjudication.

**Candidate statement:** The prospectively adopted power inputs in the protocol differ from those summarized in the report.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol adopted power inputs vs REPORT main power inputs

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005, F-ST1-004

**Qualifying route:** Route B

**Classification rationale:** PLAN versus REPORT adopted design inputs; P_R. The plan-internal reproduction is separately C011.

**Classification ambiguity:** An unsupplied prospective amendment or retrospective summary may explain the inputs.

**Exact source locations:** DOC-001 [p4 power](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4); DOC-002 [p2 effusion hypothesis](../joi240048supp1_prod_1727199125.7845.pdf#page=2), [p12 adopted power](../joi240048supp1_prod_1727199125.7845.pdf#page=12).

**Source evidence:** PLAN [protocol p12 Power calculations](../joi240048supp1_prod_1727199125.7845.pdf#page=12) prints pain difference 10 mm, change SD 25.5, 90% power, .05, 234 participants inflated to 260/130 per arm; effusion power 96% for 20% difference, mean 2.24 cm², change SD 1.35. PLAN [protocol p2 secondary hypothesis](../joi240048supp1_prod_1727199125.7845.pdf#page=2) gives 20% effusion reduction over 24 weeks. REPORT [main p4 Power Calculations](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4) gives 130/group, 90% power, VAS difference 10 points/change SD 23.8, effusion-volume difference 4.5 mL, alpha .05.

**Reported-versus-comparator:** Pain change SD 25.5 versus 23.8; effusion power 96% versus 90%; planned 20% area target versus reported 4.5-mL volume target.

**Reasoning procedure:** Separate adopted specifications from historical illustrative calculations, compare displayed numeric inputs with precision allowances and distinguish area from volume without inventing a conversion.

**Calculation:** Route B, focus D: compare adopted design inputs. SD intervals [25.45,25.55]/[23.75,23.85] leave 1.60/25.5=.0627451. Power intervals [95.5,96.5]/[89.5,90.5] leave 5/96=.0520833. Plan absolute area target .20×2.24=.448 cm² differs dimensionally from report volume 4.5 mL; no rounding operation converts area into volume. Same nominal sample size does not identify a shared design calculation.

**Affected result or extracted value:** Adopted pain dispersion and effusion detectable target/power specifications.

**Why context does not resolve it:** The common 130-per-arm sample does not reconcile the disjoint input intervals or dimensions. No dated adopted calculation or amendment connects the specifications.

**Alternative source-grounded interpretations:** Different cited source trials, an amended calculation or retrospective summary could explain the specifications. The differing inputs and dimensions are observed; their adoption history is not established. The historical n=54 WOMAC illustration explicitly regarded as optimistic is not substituted.

**Mechanical evidence recheck:** The independent rechecker found every cited source and comparator location, visually matched their printed values/text, confirmed the rule and reproduced the comparison with the stated precision allowances. Source roles and relationships were confirmed from content. Evidence state is reproduced, determined by the disjoint SD/power intervals and different effusion target dimensions. Exact remaining human question: Which dated calculation prospectively governed the trial's pain dispersion and effusion target/power, and what document explains the changed specifications?

Inputs and bounded missing definitions: All compared printed specifications are available. A dated adopted calculation/amendment, area-to-volume target link, and report effusion-volume dispersion input are absent.

**Potential downstream evidence impact:** If confirmed, design extraction could copy different dispersion, structural-effect and power inputs depending on document choice. Adoption history and a protocol violation are not inferred.

## C006 — Reported primary model differs from the supplied planned model

Pending Human Adjudication.

**Candidate statement:** The producing primary model in the report differs from the primary change-score regression stated in the supplied plans.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol/SAP primary model vs REPORT main primary producing model

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003, F-ST1-006

**Qualifying route:** Route A, category 5

**Classification rationale:** PLAN protocol/SAP versus REPORT model; P_R. Agreement between the two plan copies does not add P_P.

**Classification ambiguity:** An unsupplied model amendment or operational elaboration is possible.

**Exact source locations:** DOC-001 [p4 statistical methods](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p7 continuation](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7); DOC-002 [p12 Statistics](../joi240048supp1_prod_1727199125.7845.pdf#page=12); DOC-003 [p1 lines 5–7](../joi240048supp2_prod_1727199125.8245.pdf#page=1).

**Source evidence:** PLAN [protocol p12 Statistics](../joi240048supp1_prod_1727199125.7845.pdf#page=12) and PLAN [SAP p1 lines 5–7](../joi240048supp2_prod_1727199125.8245.pdf#page=1) prescribe between-group linear regression of changes in pain, maximal effusion size and function, with univariate/conditional multivariable modeling. REPORT [main p4 Statistical Analyses](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4) specifies longitudinal mixed model with treatment, month, interaction, participant/center random intercepts and month random slope; REPORT [main p7 continuation](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7) explains arm changes/contrasts as linear combinations of coefficients. The complete new report maps and direct current main/results extraction supply no separately identified original change-score regression primary estimate.

**Reported-versus-comparator:** Planned regression of changes versus reported longitudinal mixed model with treatment/month/interaction, participant and center random intercepts and a month random slope.

**Reasoning procedure:** Compare complete primary producing-model specifications and inspect supplied efficacy results for a separately identified original-model estimate; retain shared conditional baseline adjustment.

**Calculation:** Route A, category 5: planned primary analysis compared with producing reported model. The random-effects/time structure is materially more specific than the stated planned regression of changes, and no separate original-model result is identified. Categorical analysis-specification comparison; numerical precision does not apply. Conditional baseline adjustment is shared and is not claimed as a discrepancy.

**Affected result or extracted value:** Model specification attached to the primary VAS estimate.

**Why context does not resolve it:** Route A, category 5: the planned primary analysis is not separately reported alongside the stated producing model. Broad linearity does not supply the dated specification connecting the models.

**Alternative source-grounded interpretations:** Mixed modeling may be an approved amendment or elaboration of broad linear-regression intentions. Both choices can be coherent. Printed specification difference is observed; an unauthorized change is not inferred.

**Mechanical evidence recheck:** The independent rechecker found every cited source and comparator location, visually matched their printed values/text, confirmed the rule and reproduced the comparison with the stated precision allowances. Source roles and relationships were confirmed from content. Evidence state is reproduced, determined by the distinct supplied model specifications and absence of a separately identified original-model primary estimate. Exact remaining human question: Where is the dated specification connecting the supplied change-score regression to the reported longitudinal mixed model, or the planned-model primary result?

Inputs and bounded missing definitions: Both full producing/planned statements are available. The dated prespecification/amendment, operational elaboration of the original model, and original-model primary output are absent.

**Potential downstream evidence impact:** If confirmed, an extractor could attach a different prespecified model or amendment status to the primary effect. Both model choices may be coherent; no preferred analysis is proposed.

## C007 — Planned per-protocol primary efficacy analysis is not reported

Pending Human Adjudication.

**Candidate statement:** The unconditionally planned adherence-restricted primary efficacy analysis has no corresponding estimate in the supplied results.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol/SAP per-protocol primary analysis vs REPORT main/results supplied efficacy analyses

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004, F-ST1-007

**Qualifying route:** Route A, category 5

**Classification rationale:** Planned primary analysis versus its absence from REPORT efficacy material; P_R. Neither the agreement of plan copies nor adherence descriptives add another relationship.

**Classification ambiguity:** An unsupplied analysis or amendment could explain reporting status.

**Exact source locations:** DOC-002 [p12 Statistics](../joi240048supp1_prod_1727199125.7845.pdf#page=12); DOC-003 [p1 lines 8–9](../joi240048supp2_prod_1727199125.8245.pdf#page=1); DOC-001 [p4 methods](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p6 efficacy table](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), [p7 methods/results](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7); DOC-004 [p2 sensitivity table](../joi240048supp3_prod_1727199125.83025.pdf#page=2), [p3 adherence](../joi240048supp3_prod_1727199125.83025.pdf#page=3).

**Source evidence:** PLAN [protocol p12 Statistics](../joi240048supp1_prod_1727199125.7845.pdf#page=12) and PLAN [SAP p1 lines 8–9](../joi240048supp2_prod_1727199125.8245.pdf#page=1) unconditionally state analyses for participants consuming ≥80% capsules. REPORT [main p4 methods](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p7 methods/results](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7), and [p6 Table 2](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6) identify randomized longitudinal analyses. REPORT [results p2 eTable 1](../joi240048supp3_prod_1727199125.83025.pdf#page=2) gives original, age-adjusted and imputed primary rows. REPORT [results p3 eTable 2](../joi240048supp3_prod_1727199125.83025.pdf#page=3) gives ≥80%-adherence frequencies, limited to available pill-count/trial-completion data, without efficacy estimates.

**Reported-versus-comparator:** Protocol and SAP prescribe per-protocol analyses for ≥80% capsule consumption; report material supplies randomized efficacy, age/imputation sensitivities and adherence descriptives without that primary subset effect.

**Reasoning procedure:** Inspect the complete ten-page main article and fifteen-page results supplement through full maps and direct-source recheck, distinguishing descriptive adherence and other sensitivities from the planned restriction.

**Calculation:** Route A, category 5: absence of an unconditionally planned primary analysis in supplied results. Absence recheck covers complete main pp1–10 and results pp1–15 through the full new maps, fresh direct layout extraction and review of all result/table families, with exact visual confirmation of pertinent methods, efficacy and adherence pages. No primary effect/CI/P is identified as using the ≥80%-capsule population. This conclusion is bounded to supplied reporting, not whether an analysis was ever performed. A keyword search alone did not determine it. Numerical precision is inapplicable.

**Affected result or extracted value:** Availability and analysis population of the planned ≥80%-capsule primary per-protocol estimate.

**Why context does not resolve it:** Route A, category 5: a planned primary analysis is not reported. Adherence counts and differently defined sensitivities do not substitute for an adherence-restricted effect/interval.

**Alternative source-grounded interpretations:** It may have been performed but not supplied, amended, or prevented by incomplete pill data. Those are explanations; absence of an identified supplied result is observed.

**Mechanical evidence recheck:** The independent rechecker found every cited source and comparator location, visually matched their printed values/text, confirmed the rule and reproduced the comparison with the stated precision allowances. Source roles and relationships were confirmed from content. Evidence state is reproduced, determined by explicit planned analysis and no corresponding supplied primary estimate. Exact remaining human question: Where are the planned ≥80%-capsule primary per-protocol population definition, estimate and interval, or the dated amendment removing that analysis?

Inputs and bounded missing definitions: Prespecified restriction and complete supplied result units are available. Restricted population definition/size, efficacy output, or amendment removing the analysis are absent. Descriptive adherence counts do not supply those missing quantities.

**Potential downstream evidence impact:** If confirmed, evidence extraction could record the planned primary subset analysis as unavailable in the supplied report. This does not establish that it was never performed.

## C008 — Repeated modeled arm-change and point-contrast discrepancies

Pending Human Adjudication.

**Candidate statement:** Three modeled point contrasts do not reproduce under the placebo-minus-krill change rule supported by other rows.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main ICOAP within-display and REPORT results WOMAC/hsCRP within-display modeled contrasts

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-004, F-NUM-101, F-NUM-102, F-ST1-001

**Qualifying route:** Route A, category 4

**Classification rationale:** Each numeric contrast conflicts within its own REPORT display; S_W. Different-outcome patterns across documents and corroborating methods add no conflicting S_C relationship.

**Classification ambiguity:** Row-specific distinct models or marginalizations are not supplied.

**Exact source locations:** DOC-001 [p6 ICOAP total/intermittent](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6); DOC-004 [p5 weight-bearing/function week4](../joi240048supp3_prod_1727199125.83025.pdf#page=5), [p6 hsCRP12/24 and glucose12](../joi240048supp3_prod_1727199125.83025.pdf#page=6). Producing model corroboration: DOC-001 [p4](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p7](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7).

**Source evidence:** REPORT [main p6 Table 2 ICOAP total24/intermittent24](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), REPORT [results p5 WOMAC weight-bearing4/function4](../joi240048supp3_prod_1727199125.83025.pdf#page=5), and REPORT [results p6 hsCRP12/24 and glucose12](../joi240048supp3_prod_1727199125.83025.pdf#page=6) were visually read. Producing-model REPORT [main p4](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4) and [main p7](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7) describe modeled arm changes and linear-combination differences.

| Affected row | Krill modeled change (95% CI) | Placebo modeled change (95% CI) | Printed contrast (95% CI), P | Half-unit recomputation vs printed envelope | Gap/printed magnitude |
|---|---|---|---|---|---|
| ICOAP total24 | −9.9 (−13.3,−6.57) | −8.2 (−11.9,−4.5) | 2.05 (−2.64,6.74), .39 | P−K=1.7; [1.60,1.80] vs [2.045,2.055] | .245/2.05=.119512 |
| WOMAC weight-bearing4 | −84 (−122,−46) | −103 (−141,−65) | 3 (−10,16), .66 | P−K=−19; [−20,−18] vs [2.5,3.5] | 20.5/3=6.833333 |
| hsCRP12 | −.53 (−1.32,.26) | .24 (−.55,1.03) | .07 (−1.19,1.33), .92 | P−K=.77; [.760,.780] vs [.065,.075] | .685/.07=9.785714 |

**Reported-versus-comparator:** ICOAP total24: implied 1.7 versus 2.05; WOMAC weight-bearing4: implied −19 versus 3; hsCRP12: implied 0.77 versus 0.07.

**Reasoning procedure:** Compare displayed modeled arm changes with modeled contrasts, match endpoint/week and producing model, and apply the same subtraction rule to affected and witness rows with independent half-unit bounds.

**Calculation:** Route A, category 4, the same modeled P−K identity that reproduces other continuous rows. Witnesses: intermittent ICOAP −8.2−(−9.7)=1.5; function4 −103−(−84)=−19; hsCRP24 −.12−(−.76)=.64; primary VAS24 −20.2−(−19.9)=−.3. These witnesses reconcile under display precision. All three affected gaps exceed .05. This comparison uses displayed modeled changes, not crude final-minus-baseline means. CI/P significance agreement does not reconcile the conflicting point contrasts.

**Affected result or extracted value:** ICOAP total 24-week, WOMAC weight-bearing 4-week and hsCRP 12-week modeled point contrasts and associated result tuples.

**Why context does not resolve it:** Route A, category 4: a method that reproduces other rows does not reproduce these printed point contrasts beyond display precision. Unreported row-specific model distinctions remain questions rather than a crude-estimate substitution.

**Alternative source-grounded interpretations:** Distinct row-specific models or marginalization may underlie arm and contrast columns. Weight-bearing4 changes/CIs exactly repeat function4; ICOAP placebo total change/CI repeats intermittent; hsCRP12 contrast tuple repeats glucose12. These repetitions are observed; a copying or column-production mechanism is not established.

**Mechanical evidence recheck:** The independent rechecker found every cited source and comparator location, visually matched their printed values/text, confirmed the rule and reproduced the comparison with the stated precision allowances. Source roles and relationships were confirmed from content. Evidence state is reproduced, determined separately by each of the three disjoint contrast envelopes. Exact remaining human question: Which modeled arm changes and contrast belong to each affected endpoint/time row, and did the columns use a shared model, population and marginalization procedure?

Inputs and bounded missing definitions: Every displayed change, contrast, CI/P and model statement is available. Row-specific fitted output, marginalization, common model/population and exact contrast definition are absent.

**Potential downstream evidence impact:** If confirmed, extractors could copy conflicting point effects or attach a repeated result tuple to the named outcomes. No intended replacement value or package-wide effect change is assigned.

## C009 — Selected adverse-event counts change treatment attribution

Pending Human Adjudication.

**Candidate statement:** Selected adverse-event counts have different treatment attribution between the main and detailed results displays.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main adverse-event treatment counts vs REPORT results detailed adverse-event treatment counts

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-104, F-XS-006

**Qualifying route:** Route A, category 2

**Classification rationale:** Counts conflict across two REPORT documents; S_C and statistical_results.

**Classification ambiguity:** Different undisclosed coding or subsets remain possible.

**Exact source locations:** DOC-001 [p8 Table 3](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8); DOC-004 [p10 cough and treatment headers](../joi240048supp3_prod_1727199125.83025.pdf#page=10), [p11 gastrointestinal rows](../joi240048supp3_prod_1727199125.83025.pdf#page=11).

**Source evidence:** REPORT [main p8 Table 3](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8) labels columns krill n130/placebo n132; cough 2/0, reflux 1/3, abdominal discomfort 0/3. REPORT [results p10 eTable 7 headers and cough](../joi240048supp3_prod_1727199125.83025.pdf#page=10) has the same K/P order and cough blank/2. REPORT [results p11 continuation gastrointestinal rows](../joi240048supp3_prod_1727199125.83025.pdf#page=11) gives reflux 3/1 and abdominal discomfort 3/blank. Blank cells remain blank; no implicit zeros enter the calculations.

**Reported-versus-comparator:** Reflux krill/placebo 1/3 versus 3/1; krill abdominal discomfort 0 versus 3; placebo cough 0 versus 2.

**Reasoning procedure:** Match event labels and treatment headers; compare only explicit counts after precision allowances, retaining supplementary blanks as unreported.

**Calculation:** Route A, category 2: treatment-specific count attribution changes. Krill reflux 1[.5,1.5] vs 3[2.5,3.5] gap1/1=1; placebo reflux 3 vs1 gap1/3=.333333. Krill abdominal discomfort 0[−.5,.5] vs3[2.5,3.5] gap2; placebo cough 0[−.5,.5] vs2[1.5,2.5] gap1. Against printed zero any positive gap reproduces. Nonnegative truncation of zero's interval does not alter either gap. Main K cough2 and P abdominal3 have supplementary blanks, which document treatment attribution but are not independently quantified comparisons.

**Affected result or extracted value:** Treatment-specific reflux, abdominal-discomfort and cough event counts.

**Why context does not resolve it:** Route A, category 2: the explicit counts change treatment-specific readings. Blank cells are not converted to zero, and adjacent integer differences with touching precision intervals are excluded.

**Alternative source-grounded interpretations:** Different coding/subsets or treatment-column substitutions are possible. Conflicting explicit treatment counts are directly observed; their production mechanism is not established. Adjacent 1-vs2 copies with touching half-unit intervals are not part of this retained pattern.

**Mechanical evidence recheck:** The independent rechecker found every cited source and comparator location, visually matched their printed values/text, confirmed the rule and reproduced the comparison with the stated precision allowances. Source roles and relationships were confirmed from content. Evidence state is reproduced, determined by the four explicit matching arm/event comparisons above. Exact remaining human question: Which treatment-specific cough, reflux and abdominal-discomfort counts apply, and do both displays use the same event-count definitions and population?

Inputs and bounded missing definitions: Explicit counts, event names, treatment headers and study period are available. Any distinct coding, event/person unit, population subset or table-specific counting definition is absent.

**Potential downstream evidence impact:** If confirmed, selected treatment-specific safety counts copied into extraction could depend on which display is used. No pooled risk estimate or overall safety conclusion is inferred.

## C010 — Serious-event relatedness classifications do not reconcile

Pending Human Adjudication.

**Candidate statement:** The main all-unrelated serious-event summary does not reconcile with supplementary treatment-relatedness classifications.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main serious-event relatedness summary vs REPORT results serious-event relatedness classifications

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-007

**Qualifying route:** Route B

**Classification rationale:** Reported statistical safety classifications across two REPORT documents; S_C and statistical_results.

**Classification ambiguity:** An unsupplied final investigator assessment may reconcile preliminary labels.

**Exact source locations:** DOC-001 [p8 Table 3, footnote b, narrative](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8); DOC-004 [p14 eTable 8 relatedness entries](../joi240048supp3_prod_1727199125.83025.pdf#page=14).

**Source evidence:** REPORT [main p8 Table 3 final row, footnote b, safety narrative](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8) gives treatment-related SAE0/0, no related serious events identified by investigators, and all serious events considered unrelated. REPORT [results p14 eTable 8](../joi240048supp3_prod_1727199125.83025.pdf#page=14) explicitly labels parentheses as relationship with treatment. Its treatment order is placebo first, krill second. Krill transfusion-dependent anaemia is 1 (Probable); seven other krill entries and three placebo entries are Possible. Krill fracture fixation and placebo appendicitis are Unlikely; two placebo unknown entries are NA. All event entries total K9/P6 as in the main report.

**Reported-versus-comparator:** Main treatment-related SAE 0/0 and all-unrelated narrative versus supplementary krill anaemia Probable and other entries Possible, with matched total events.

**Reasoning procedure:** Match event totals and reversed supplementary treatment-column order, then compare categorical classifications and summary assertions without automatically counting every Possible as related.

**Calculation:** Route B, focus A/C: categorical relatedness-to-summary mapping is unresolved. The probable treatment relation is not reconciled by the main all-unrelated assertion or a supplied classification threshold. No conversion of every Possible to related is assumed. Numerical half-unit precision is inapplicable to the categorical comparison; no 0-vs1 argument is used to bypass touching integer intervals. The affected extracted result is final treatment-related SAE classification, particularly anaemia.

**Affected result or extracted value:** Final treatment-related SAE classification and summary, particularly the probable krill anaemia entry.

**Why context does not resolve it:** No final-assessment date, threshold or mapping connects Probable/Possible/Unlikely/NA to the main all-unrelated summary. This categorical comparison does not use a 0-versus-1 numeric argument to bypass display precision.

**Alternative source-grounded interpretations:** Main may summarize a later assessment while supplement retains earlier coding, or relatedness may have an unstated threshold. The printed classifications conflict as supplied; clinical causation or adjudication history is not inferred.

**Mechanical evidence recheck:** The independent rechecker found every cited source and comparator location, visually matched their printed values/text, confirmed the rule and reproduced the comparison with the stated precision allowances. Source roles and relationships were confirmed from content. Evidence state is reproduced, determined by Probable treatment-related coding versus the all-unrelated summary without a supplied bridge. Exact remaining human question: Which final assessment and mapping govern the related-SAE summary, and was the probable krill anaemia classification subsequently changed?

Inputs and bounded missing definitions: Event/treatment labels, relatedness entries, main assertions and total event alignment are available. The final investigator assessment date/version and mapping of Possible/Probable/Unlikely/NA into treatment-related status are absent.

**Potential downstream evidence impact:** If confirmed, an extractor could copy different final related-SAE classifications. Clinical causality and whether the trial caused a particular event are not adjudicated.

## C011 — Planned effusion power does not reproduce from supplied inputs

Pending Human Adjudication.

**Candidate statement:** The stated effusion power requires an additional assumption not identified by the supplied effect, variability and sample inputs.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol effusion power inputs vs PLAN protocol claimed power and statistical specification

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-003

**Qualifying route:** Route B

**Classification rationale:** Conflict lies within PLAN power inputs and claimed power; P_P and plan_material. The SAP corroborates the specification.

**Classification ambiguity:** Exact adopted power formula and efficiency assumptions are absent.

**Exact source locations:** DOC-002 [p2 effusion hypothesis](../joi240048supp1_prod_1727199125.7845.pdf#page=2), [p12 Power/Statistics](../joi240048supp1_prod_1727199125.7845.pdf#page=12); DOC-003 [p1 model and significance corroboration](../joi240048supp2_prod_1727199125.8245.pdf#page=1).

**Source evidence:** PLAN [protocol p12 Power calculations/Statistics](../joi240048supp1_prod_1727199125.7845.pdf#page=12) gives 234 participants before 10% loss, 260/130 per arm after allowance, and 96% effusion power for a 20% difference using mean2.24 cm²/change SD1.35. It specifies between-group regression and two-tailed .05. PLAN [protocol p2 hypothesis](../joi240048supp1_prod_1727199125.7845.pdf#page=2) confirms 20% effusion reduction over24 weeks; PLAN [SAP p1 lines5–10](../joi240048supp2_prod_1727199125.8245.pdf#page=1) corroborates model/significance.

**Reported-versus-comparator:** Plan 96% power for a 20% difference with mean 2.24 cm², change SD 1.35 and 117/130 per arm versus labelled normal two-arm diagnostic power.

**Reasoning procedure:** Use the supplied between-arm effect/change-SD specification for an expressly labelled diagnostic; examine both pre-loss and inflated samples, all relevant half-unit allowances and fixed two-sided alpha 0.05.

**Calculation:** Route B, focus C/D: stated power from explicit design inputs. A labelled equal-size two-arm normal mean-change diagnostic uses absolute effect .20×2.24=.448 cm² and SE=1.35×sqrt(2/n), with fixed designated two-sided alpha .05. n117/130 per arm gives normal power71.84438%/76.28552%. This diagnoses the supplied simple between-arm specification; it is not the authors' unpublished exact method. Input allowances20%[19.5,20.5],mean[2.235,2.245],SD[1.345,1.355] give fixed-n envelopes[69.15113%,74.44664%]/[73.67002%,78.77797%]. Compared with96%[95.5,96.5], best fixed-n gap16.72203/96=.1741878.

The recheck additionally broadens the derived n117 and printed n130 each by±.5, conservatively enclosing the half-unit total-derived sample range. The envelopes become[68.96565%,74.62587%]/[73.50681%,78.93133%]. Even this favorable n130.5 bound leaves gap16.56867/96=.1725903. This expands arithmetic allowances; no source transcription or location changed. Specified alpha is a decision rule rather than an uncertain input. The independent diagnostic is recorded with R4.5.2/base stats in review_1_6_2/preprocessing/evidence_rechecker/numeric-diagnostics.txt.

**Affected result or extracted value:** Stated planned power for the 20% effusion target and its supporting assumptions.

**Why context does not resolve it:** The stated two-arm design inputs do not identify the effect, variance or efficiency assumption needed to reproduce 96%. The source supplies no exact powering formula or covariance/adjustment efficiency bridge.

**Alternative source-grounded interpretations:** A different effective SD, endpoint contrast or adjustment efficiency could produce96%. The plan also anticipates natural effusion fluctuation in both arms, supporting a between-arm comparison rather than a single-arm change test. Stated inputs/claim are observed; the extra adopted assumption remains unknown. Historical n54 WOMAC illustration is not substituted.

**Mechanical evidence recheck:** The independent rechecker found every cited source and comparator location, visually matched their printed values/text, confirmed the rule and reproduced the comparison with the stated precision allowances. Source roles and relationships were confirmed from content. Evidence state is reproduced, determined by the large diagnostic gap under the supplied simple two-arm interpretation, still present after every specified numeric allowance above. Exact remaining human question: What adopted calculation and additional effect, variance or efficiency assumption produce96% power for the stated20% effusion target with these sample/mean/change-SD inputs?

Inputs and bounded missing definitions: Effect percentage, mean, change SD, nominal sample, loss allowance and significance/model statements are available. Exact powering formula/software, whether 234 or260 governs the effective sample, alternative effect/variance definition and any covariate-efficiency/correlation assumption are absent. Therefore the diagnostic reproduces the need for an additional unstated assumption, not a definitive recomputation of unpublished model power.

**Potential downstream evidence impact:** If confirmed, design extraction could retain 96% without the additional input required to reproduce its calculation. The diagnostic does not describe achieved power or prescribe another analysis.

## C012 — Repeated contrast-interval widths differ from a reproducing display rule

Pending Human Adjudication.

**Candidate statement:** Glucose12 and WOMAC total24 contrast intervals depart from an empirical width rule that reproduces neighboring rows within their own displays.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results glucose12 and REPORT main/results WOMAC total24 within-display contrast intervals vs arm intervals and reproducing rows

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-002, F-ST2-001

**Qualifying route:** Route A, category 4

**Classification rationale:** Each conflicting interval and its reproducing rule are compared within its own REPORT display; S_W. Main/results WOMAC copies agree, so no conflicting S_C relationship is added. Model-method corroboration adds no relationship.

**Classification ambiguity:** Exact row-specific covariance and CI methods are absent.

**Exact source locations:** DOC-004 [p6 glucose12/24, TG12, HDL12, LDL12, hsCRP12 and adjustment footnote](../joi240048supp3_prod_1727199125.83025.pdf#page=6), [p5 WOMAC total4/8/12/16/20/24](../joi240048supp3_prod_1727199125.83025.pdf#page=5); DOC-001 [p6 WOMAC total24 and glucose24 corroboration](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), [p4 model methods](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p7 model continuation](../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7).

**Source evidence:** Main WOMAC total pain24 prints krill change −87 (95% CI −110 to −63), placebo change −83 (−106 to −59), between-group change difference 3.0 (−24 to 31), P=.81. Results p5 prints the same arm changes and intervals and contrast 3 (−24 to 31), P=.81. Its observed follow-up contributors are krill106 and placebo111; the display headings identify randomized groups n=130/n=132. Main follow-up means identify n=129/n=130, but this candidate does not compare those contributor counts or substitute them into the modeled interval rule.

Results p6 fasting glucose12 prints krill change .09 (−.07 to .24), placebo change .15 (−.01 to .31), contrast .07 (−1.19 to 1.33), P=.92, contributors112/112. Glucose24 prints changes .07 (−.12 to .26)/.11 (−.08 to .29), contrast .04 (−.23 to .30), P=.79, contributors100/100. Main p6 corroborates this glucose24 interval. The entire glucose12 contrast .07 (−1.19 to 1.33), P=.92 also appears in the results p6 hsCRP12 row, whose arm changes are −.53 (−1.32 to .26)/.24 (−.55 to 1.03). This repeated tuple is a direct observation; a copying mechanism is not asserted.

The source states that primary and secondary outcomes were evaluated using a linear mixed model with treatment, month, treatment-by-month interaction and baseline outcome adjustment where baseline differences were present. Participant and center are random intercepts; month is a random slope. Main p7 states that within-group changes and between-group differences in changes were calculated using linear combinations of estimated coefficients. Main p6 and results p6 specify the baseline-adjustment threshold at P≤.10 and list hsCRP, back pain, WOMAC total pain and weight-bearing pain. No 24-week-specific WOMAC interval convention or glucose12-specific interval convention is disclosed at these locations. No values were imputed for the displayed analyses; the age sensitivity is separately identified. These model and adjustment statements support matching the displayed modeled changes and contrasts, without proving zero covariance.

Each witness was separately confirmed from the source image. K/P columns below contain modeled change intervals, not raw baseline/follow-up differences. RSS means the empirical root-sum-square rule applied to arm CI half-widths, with h=(upper−lower)/2. The rule is a diagnostic supported by the same display, not an assertion of the actual unpublished variance formula.

| Witness and source | K change CI | P change CI | Printed contrast CI | Nominal RSS half-width | RSS half-width envelope after each endpoint's own precision | Printed contrast half-width envelope | Result |
|---|---|---|---|---:|---|---|---|
| WOMAC total4; results p5 | −45 to−20 | −50 to−25 | −23 to13 |17.677670|[16.970563,18.384776]|[17.5,18.5]|Overlap|
| WOMAC total8; results p5 | −64 to−37 | −67 to−40 | −22 to16 |19.091883|[18.384776,19.798990]|[18.5,19.5]|Overlap|
| WOMAC total12; results p5 | −69 to−40 | −72 to−43 | −24 to18 |20.506097|[19.798990,21.213203]|[20.5,21.5]|Overlap|
| WOMAC total16; results p5 | −83 to−51 | −84 to−52 | −24 to22 |22.627417|[21.920310,23.334524]|[22.5,23.5]|Overlap|
| WOMAC total20; results p5 | −90 to−54 | −85 to−49 | −21 to30 |25.455844|[24.748737,26.162951]|[25,26]|Overlap|
| Glucose24; results p6, main p6 corroborates | −.12 to.26 | −.08 to.29 | −.23 to.30 |.265189|[.258118,.272259]|[.260,.270]|Overlap|
| Triglyceride12; results p6 | −.23 to.02 | .01 to.26 | .07 to.42 |.176777|[.169706,.183848]|[.170,.180]|Overlap|
| HDL12; results p6 | 0.0 to.08 | −.01 to.07 | −.07 to.05 |.056569|[.037165,.081125]|[.055,.065]|Overlap|
| LDL12; results p6 | −.01 to0.2 | −.15 to.06 | −.29 to.005 |.148492|[.126516,.172210]|[.144750,.150250]|Overlap|

Three additional same-main-display witnesses were visually confirmed on main p6: WOMAC weight-bearing24 arm CIs−61 to−42/−58 to−39, contrast CI−10 to16; WOMAC non-weight-bearing24 arm CIs−32 to−15/−29 to−13, contrast CI−10 to14; WOMAC function24 arm CIs−299 to−182/−247 to−132, contrast CI−31 to133. Their nominal RSS half-widths are13.435029,11.672618 and82.027435 respectively. Integer endpoint allowances give RSS envelopes[12.727922,14.142136], [10.965856,12.379418] and[81.320354,82.734515], each overlapping its printed half-width envelope[12.5,13.5], [11.5,12.5] and[81.5,82.5]. They support the rule within main Table 2 itself; the WOMAC24 main occurrence does not depend solely on a witness in another document.

Every witness has zero remaining width-interval gap after its actual display precision. The point and endpoint rounding allowances also permit centered intervals for these witnesses: for example WOMAC20's contrast5 permits a center4.5 and RSS width25.455844, yielding endpoints−20.955844/29.955844 inside the printed endpoint allowances. No nominal center/half-width difference caused solely by integer rounding is claimed. HDL12 prints 0.0, whose half-unit is .05; LDL12 prints 0.2, whose half-unit is .05, and its contrast upper .005 has half-unit .0005. The table respects these mixed precisions rather than silently giving all endpoints two decimal places. The broader allowances reinforce witness compatibility and do not alter either affected occurrence's mismatch.

**Reported-versus-comparator:** Glucose12 printed contrast half-width 1.26 versus empirical 0.21570–0.22984; WOMAC total24 printed 27.5 versus empirical 32.526912–33.941125.

**Reasoning procedure:** Confirm every affected and witness row; apply root-sum-square (RSS) to modeled arm-CI half-widths with each endpoint's actual precision, then compare reconstructed endpoint and printed intervals. Consolidate the shared empirical-width pattern while preserving both outcomes and model-specific alternatives.

**Calculation:** Route A, category 4 of QUALITY_CONTROL_SCOPE.md covers a printed interval that does not reproduce, beyond the display-precision rule, under a method that reproduces other rows of the same display. All five earlier time points of the same adjusted WOMAC total-pain outcome support the empirical RSS width rule. The same-page glucose24 and lipid rows support it for glucose12. The source does not establish that the model uses zero cross-arm covariance or common row-specific critical values, and none is assumed as a factual model property. Category 4 makes the missing producing method a human question rather than an automatic conditional exclusion. This is not a category1 interval-null/P conflict: both affected CIs contain0 and both printed P values exceed.05.

separately for both occurrences and both WOMAC copies.

For WOMAC24 both nominal arm CI half-widths are23.5. Allowing each integer arm endpoint ±.5 gives hK and hP in[23,24], and empirical RSS contrast half-width[32.5269119,33.9411255], nominal33.2340187. The printed contrast endpoints−24 and31 imply half-width27.5 with envelope[27,28]; the width gap is4.5269119, relative4.5269119/27.5=.1646150.

Main prints the contrast3.0, so its center allowance is[2.95,3.05]. Combining that allowance with the RSS envelope gives the lower endpoint envelope[−30.9911255,−29.4769119] and upper[35.4769119,36.9911255]. Printed lower−24 allows[−24.5,−23.5]; the nearest gap is4.9769119 and relative gap4.9769119/24=.2073713. Printed upper31 allows[30.5,31.5]; gap3.9769119 and relative gap3.9769119/31=.1282875. Both exceed.05.

Results prints contrast3, so its wider center allowance is[2.5,3.5]. The recomputed lower envelope becomes[−31.4411255,−29.0269119] and upper[35.0269119,37.4411255]. The respective gaps from the same printed endpoint allowances are4.5269119/24=.1886213 and3.5269119/31=.1137714. Thus the discrepancy remains beyond precision in each printed copy. Arm point subtraction−83−(−87)=4 permits[3,5]; that overlaps main3.0[2.95,3.05] and results3[2.5,3.5]. No point-estimate algebra discrepancy is added.

For glucose12, hK=.155/hP=.160 nominally and RSS=.222766694. Each arm endpoint is printed to .01, allowing ±.005; hK[.150,.160], hP[.155,.165] therefore give RSS[.215696546,.229836899]. The printed contrast .07 permits center[.065,.075], giving lower envelope[−.164836899,−.140696546] and upper[.280696546,.304836899]. Printed lower−1.19 permits[−1.195,−1.185], and upper1.33 permits[1.325,1.335]. Both gaps equal1.020163101, with relative gaps1.020163101/1.19=.857279917 and /1.33=.767039926. Nominal printed half-width1.26 is also disjoint from RSS. Arm point subtraction.15−.09=.06 permits[.05,.07], overlapping the printed contrast[.065,.075]; no point discrepancy is claimed.

**Affected result or extracted value:** Glucose 12-week and WOMAC total-pain 24-week between-arm confidence intervals, including both WOMAC report copies.

**Why context does not resolve it:** Route A, category 4: the same-display empirical rule reproduces the stated witnesses but not these printed intervals beyond display precision. Missing covariance, degrees of freedom or critical-value conventions are the producing-method question. Null inclusion and printed P significance agree.

**Alternative source-grounded interpretations:** The reported longitudinal model can share coefficients between arms, so nonzero arm-change covariance can change contrast variance. Marginal and contrast intervals could use different degrees of freedom, critical values or variance/marginalization conventions, especially if these depend on outcome and follow-up. A row-specific calculation could therefore explain either printed interval. WOMAC total pain is baseline-adjusted, whereas glucose is not listed among baseline-adjusted outcomes; consolidation does not assert these fits are identical. Neither a covariance convention nor an identified row-specific interval convention in the supplied methods explains the printed exceptions to the rule reproducing their own neighboring rows. The hsCRP/glucose repeated contrast tuple is compatible with a transcription-production explanation, but such an explanation is inferred and not adopted as a fact.

Direct: all printed rows, the agreeing report copies of WOMAC24, the repeated hsCRP/glucose12 tuple, the model/adjustment descriptions, and the disjoint recomputation intervals under the stated diagnostic. Inferred and unconfirmed: any copying mechanism, zero actual covariance, use of a common critical value, or a particular intended replacement interval. No preferred analysis or final correction is assigned.

**Mechanical evidence recheck:** A distinct fresh pass-2 rechecker visually confirmed all three affected occurrences, twelve same-display witness relationships plus the main glucose24 corroborating copy, and all five cited source pages. Source and comparator values matched; no source transcription correction was required. reproduced. Determining fact: the exact source values remain as transcribed, the same-display empirical rule reproduces the stated witness rows within actual half-unit intervals, and both affected occurrences remain separated from it by relative endpoint gaps above.05. No transcribed source value or source location required correction. Clarification of mixed witness endpoint precision broadens their compatibility envelopes but changes neither occurrence's evidence state.

Yes for the empirical rule and every display-precision comparison: exact arm endpoints, contrast point/endpoints, time points, outcomes, confidence-level labels, column bindings and same-display witness rows are available. Each relevant endpoint has its actual printed precision applied. Inputs are not taken from descriptive final means or from crude participant ratios. The printing of 95% CIs and the two-sided .05 test threshold is confirmed, but no exact P-value inversion is used.

Missing producing definitions: The fitted coefficient covariance matrix; covariance between the modeled arm changes; row-specific residual/variance estimates; degrees of freedom; critical values for the marginal-change and contrast intervals; exact contrast vectors and marginalization convention; and any distinct row-specific interval calculation. Raw fitted output is not supplied. These absences limit exact statistical regeneration. They do not prevent reproducing the empirical same-display discrepancy under category4.

Both occurrences fail the same empirical RSS arm-width rule supported by their own eTable4 neighboring rows; both require the same missing producing variance/critical-value definition. No separate production cause is established from the supplied evidence. Retaining glucose12 and WOMAC24 under expanded C012 is supported as one repeated display-width pattern, with the differing outcomes, baseline adjustments and possible row-specific explanations explicitly preserved. C008 instead concerns point-contrast algebra and remains a different rule. The consolidation preserves every new WOMAC occurrence and witness; it does not turn main-versus-supplement agreement into a cross-report inconsistency.

Remaining source-definition question: Which covariance, degrees-of-freedom, critical-value or interval/marginalization calculation produced the WOMAC total-pain24 contrast3.0(−24 to31) and fasting glucose12 contrast.07(−1.19 to1.33), and what row-specific convention explains their departure from the arm-CI-width rule that reproduces all five earlier WOMAC total-pain rows and the neighboring glucose/lipid rows? The question concerns producing definitions and extractable interval precision; both candidates' significance directions remain unchanged.

**Potential downstream evidence impact:** If confirmed, interval precision extracted for the two named outcomes could depend on unresolved producing conventions. No replacement interval or significance change is asserted.

## C013 — WORMS smaller-one-unit percentages differ from their counts

Pending Human Adjudication.

**Candidate statement:** The WORMS smaller-by-one-unit percentages do not reproduce from their count/total pairs in one table.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results WORMS smaller-one-unit counts vs percentages and totals in one display

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-103

**Qualifying route:** Route A, category 3

**Classification rationale:** Counts, percentages and denominators are in one REPORT display; S_W and statistical_results.

**Classification ambiguity:** None.

**Exact source locations:** DOC-004 [p8 eTable 5 smaller-one-unit and totals](../joi240048supp3_prod_1727199125.83025.pdf#page=8).

**Source evidence:** REPORT [results p8 eTable5 smaller−1-unit and totals](../joi240048supp3_prod_1727199125.83025.pdf#page=8) prints K10(12%) and P16(12%), totals107(100%)/109(100%). Other category counts K2,80,12,3 and P2,75,13,3 sum with these counts to107/109.

**Reported-versus-comparator:** Krill 10/107 and placebo 16/109 are both displayed as 12%, although their count-based percentages differ.

**Reasoning procedure:** Bind each arm's numerator, total and percentage within eTable 5, confirm the complete category sums and allow half-unit precision for every displayed input/output.

**Calculation:** Route A, category3: numerator/denominator/percentage within one display. K100×10/107=9.345794%; half-unit numerator/denominator bounds100×[9.5/107.5,10.5/106.5]=[8.837209%,9.859155%]. Printed12% interval[11.5,12.5] leaves gap1.640845/12=.1367371. P100×16/109=14.678899%; bounds100×[15.5/109.5,16.5/108.5]=[14.155251%,15.207373%], gap1.655251/12=.1379376. Both exceed .05; both retained occurrences reproduce independently. Counts are discrete, but even the broader mandated literal half-unit envelopes fail to reconcile.

**Affected result or extracted value:** Treatment-specific smaller-by-one-unit WORMS proportions at 24 weeks.

**Why context does not resolve it:** Route A, category 3: count, denominator and percentage fail to reconcile within one display beyond the precision rule. A different or weighted denominator is not supplied.

**Alternative source-grounded interpretations:** Another count/denominator could underlie each12%, or percentages may have been reused. The two count/percentage mismatches are observed; their mechanism is not established. Matching printed12% across arms does not identify a unique underlying input.

**Mechanical evidence recheck:** The independent rechecker found every cited source and comparator location, visually matched their printed values/text, confirmed the rule and reproduced the comparison with the stated precision allowances. Source roles and relationships were confirmed from content. Evidence state is reproduced, determined independently by the two separated percentage envelopes. Exact remaining human question: Which numerators and denominators produce the smaller-by-one-unit WORMS percentage in each treatment arm?

Inputs and bounded missing definitions: Explicit numerators, percentages, arm totals and complete count sums are available. Any different denominators or weighted percentage definition are absent; the source provides no such indication.

**Potential downstream evidence impact:** If confirmed, an extractor could copy 12% for either arm despite its unresolved numerator/denominator basis. No comparative risk effect or trial conclusion is inferred.

## Downstream Evidence-Chain Considerations

If a candidate is confirmed during human adjudication, evidence extraction could depend on which location, signed contrast, scale definition, interval, denominator, safety classification or plan specification is copied. The cards identify each affected quantity so that any later evidence-synthesis use can distinguish these alternatives. Counts, modeled effects, endpoint windows and analysis populations represent different quantities and require matched interpretation.

This package provides no evidence that an unresolved value has propagated into a meta-analysis, guideline or clinical decision. The review does not infer serious harm, a paper-level conclusion change or a replacement value. An unchanged null/P interpretation does not remove a reproduced reporting discrepancy, and a missing producing convention remains a bounded limitation rather than proof of a particular production mechanism.

## Limitations and Missing Definitions

All 41 supplied physical PDF pages were mapped; no scientific coverage gap remains. These limitations concern supplied content and exact regeneration.

- The package supplies no raw participant-level data, fitted model output, coefficient covariance matrices, row-specific degrees of freedom, CI critical values, exact contrast vectors or marginalization conventions. Empirical point/interval checks and normal-power calculations remain explicitly labelled diagnostics.
- The exact adopted effusion-power formula, effective variance/effect definition and any covariate-efficiency assumption are absent. Both pre-loss and inflated samples were examined without asserting achieved power.
- The administered primary questionnaire, its dated version and amendments connecting endpoint or model specifications are not supplied. A documented amendment remains a possible explanation for plan/report differences.
- ICOAP scored-versus-unscored items, branching, weights and raw normalization rules are not sufficiently specified to connect every printed count and maximum.
- The supplied report identifies no adherence-restricted primary efficacy estimate. This is an absence within supplied reporting, not proof that the analysis was never performed. Detailed imputation specifications are also absent.
- Treatment-specific safety coding, event/person linkage and table-specific counting bases are not fully supplied. A final investigator relatedness assessment and category-to-summary mapping are absent. Supplementary blanks remain unreported rather than assumed zero.
- Individual trajectories, quartiles and historical bar heights do not print exact numerical values. Their visual structure, axes, categories and printed statistics were mapped without invented digitization.
- Reusable protocol text on pages 4–5 omitted historical numeric figures; fresh CPU renders and mapping closed both units. Reusable assets are selective derivatives, not the final source authority. There were no tooling limitations; direct tools sufficed and no fallback environment was created.

Only supplied local evidence was used. The review does not infer production mechanisms, intended replacement values, clinical causality, protocol authorization history, evidence propagation or paper-level conclusion changes. Every stable candidate remains Pending Human Adjudication.


The standalone [limitations record](review_1_6_2/limitations.md) retains the same bounded supplied-content limits.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Source identity and integrity

Source identities and all 116 reusable assets were hashed before scientific work. The curator matched canonical legacy text to direct current-source layout extraction and verified physical pagination. The final independent audit repeated both before-hash checks successfully. Source and reused assets were preserved; fresh derivatives reside only under this run's versioned directory.

| Direct-source filename | SHA-256 before review |
|---|---|
| jama_laslett_2024_oi_240048_1727199125.7595.pdf | 2f57456533bfb7b4023bdb8b356a413fa086c42f1b16cdba12f6fe89ceb8d491 |
| joi240048supp1_prod_1727199125.7845.pdf | 317ff46a6f5ef0b298638dd6e447eefd462e0d3f7b35d0c9a6bdd014718d0bdb |
| joi240048supp2_prod_1727199125.8245.pdf | 57681138f96ff0b69619a409ec404118f442afbb2bba836f111d5fc893c5d430 |
| joi240048supp3_prod_1727199125.83025.pdf | 67e172cdd96b1897d5e06843f31565a5903ca0c4812bd692b0a4c900b8a9815e |

The complete integrity records are [source hashes before](review_1_6_2/source_hashes_before.sha256), [source hashes after](review_1_6_2/source_hashes_after.sha256), [reused-asset hashes before](review_1_6_2/reused_artifact_hashes_before.sha256) and [reused-asset hashes after](review_1_6_2/reused_artifact_hashes_after.sha256). The [mechanical validation record](review_1_6_2/review_validation.json) records final artifact, ID, coverage, classification, timing, link and integrity checks.

### Tooling and routing

Compute device: CPU. Direct tools sufficed: pdfinfo, pdftotext, pdftoppm/pdftocairo, sha256sum and Pandoc were available. Current-source extraction and rendering used Poppler 26.01.0. Tesseract 5.5.0/Leptonica 1.86.0 was available but new OCR was unnecessary. Labelled power/normal diagnostics used R 4.5.2 base stats; interval calculations also used explicitly transcribed inputs and JavaScript arithmetic. No GPU, global installation or temporary fallback environment was used. Fallback environment NOT_NEEDED; removal state NOT_CREATED; tooling limitations None. Derivative commands, engines and locations are recorded in originating stage artifacts and the [tooling record](review_1_6_2/tooling_record.md).

Routing preflight: PASS. Run model: gpt-6.1-sol; run model source DEFAULT. Coordinator inference: PASS. Execution mode: INTERACTIVE_CLI. Provider: CURRENT_SESSION. All ten named presets were verified against the fixed model/effort pairs in [routing preflight](review_1_6_2/routing_preflight.md). Every specialist stage used a distinct fresh runtime. No provider credential or substitute model is recorded.

### Agent execution

All fifteen actual agents, including the coordinator, numeric shard and expanded-C012 screen/recheck, appear exactly once below. Every role uses gpt-6.1-sol; ordinary roles use medium reasoning effort and statistical, screening, recheck and audit roles use high.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a129ab-bade-7253-b313-f5ed29533c7c | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a129ae-7eab-78d0-9d49-82bbb364e226 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a129b0-fc95-70f0-9813-251d72f97be6 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a129b1-1c9d-7bd2-a90b-b0403d8cb593 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | 01a129b4-c3f5-7492-bb6b-2461f3c7811e | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a129b4-ed97-7e21-94ff-d13c39bd4cee | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a129b5-1c4b-7ed3-955e-c6ca5e85d0b6 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| numeric_consistency_support_shard | 01a129b5-97cf-7843-9ca2-d5d4de552d64 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/parts/numeric_support_consistency.md |
| inclusion_screener | 01a129be-effc-76d0-a857-3dce2161cd4a | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a129c8-65ac-77a3-bd94-7df0e00a6fb0 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a129ce-662d-78e3-ae0a-28ba82dc65c9 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| inclusion_screener_pass_2 | 01a129d7-7723-7a51-85ed-fef5e15acf20 | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_pass_2 | 01a129d8-cbb2-7722-9cd1-850c8005a09c | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck_pass_2.md |
| quality_control_auditor | 01a129dc-bfaa-7f43-a2c8-6a41229edb68 | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | 01a129e6-b4ad-7a31-b78f-6e86f26a68a9 | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |


Artifact paths in this table are relative to review_1_6_2/. The [execution manifest](review_1_6_2/agent_execution_manifest.md) and [coverage manifest](review_1_6_2/coverage_manifest.md) retain primary and additional durable outputs.

### Reproducibility performance

The package-specific target combines source/reuse burden, PDF/table complexity, visual requirements, relationship volume and required fresh specialist waves. The planning range never limits scientific coverage or candidate inclusion. Review timing closes after complete Markdown assembly and is refreshed when a subsequent repair requires a model call. Local rendering and purely mechanical validation otherwise sit outside that review window.

- **Target basis:** Four PDF-only sources contain 41 unique physical pages, with 39 sufficiently covered by source-matched reusable evidence and two protocol pages requiring fresh visual mapping of historical numeric figures. The final audit refined the initial all-text-backed count without changing the 25–40 minute planning target. CPU direct rendering suffices; no OCR, Office conversion or workbook parsing is required. The main article and 15-page results supplement contain dense tables with retained visual pages; protocol and SAP add planned-versus-reported relationships. Parallel main/support mapping and parallel three-lane checks precede sequential screening, recheck, distinct statistical pass 2, audit and report waves. These combined factors support the selected target.
- **Total source units:** 41
- **Fresh-source units:** 2
- **Target elapsed minutes:** 25-40
- **Started UTC:** 2026-10-11T06:37:14Z
- **Finished UTC:** 2026-10-11T07:46:04Z
- **Observed elapsed minutes:** 68.83
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Complete review of 197 numeric relationships required an additional disjoint support checker shard; independent source confirmation consolidated 24 initial findings into thirteen complete evidence records; statistical pass 2 added an interval-width occurrence requiring a different fresh inclusion screener and expanded source rechecker; final audit reconciled two partial reusable pages and relocated evidence links before complete thirteen-card report assembly. Mandatory sequential screening, recheck, second-pass, audit and report waves were completed without omitting scope or findings. A final validator vocabulary check required one neutral audit-bookkeeping wording repair and refreshed timing before rerendering.

