# AMATERASU Trial: Quantitative Quality-Control Consistency Review

**Workflow 1.6.2 — Pending Human Adjudication**

Every candidate below remains **Pending Human Adjudication**. The classifications and evidence states describe the supplied reporting evidence; they are not adjudications of the authors' work.

## Executive Quality-Control Summary

Complete review of four supplied PDFs, comprising 96 pages, identified **seven stable candidates**: four in `protocol_report` and three in `statistical_results`. The candidates concern de novo cancer outcome status, planned survival-curve and risk-ratio analyses, an omitted prespecified subgroup, genotype denominators, a shared hazard-ratio direction statement, and an adjusted estimate/interval/P-value combination under an explicitly diagnostic reproducing calculation.

All seven passed independent inclusion screening, exact-source mechanical recheck and independent inclusion audit. Six evidence states are `reproduced`; one is `reproduced_after_transcription_correction`. The correction concerns a paragraph-specific amendment date in the registration, while the outcome-status comparison remains reproduced. No date-only candidate was registered.

The complete inventories contain 105 numeric relationships and 106 statistical relationships. Different fresh statistical agents completed both passes over all 106 statistical records. Pass 2 also revisited every initial checker exclusion and produced the seventh candidate, which received a different fresh inclusion screen and appended-ID recheck. No candidate count was assumed or imposed.

The candidates identify bounded questions for evidence extraction. They do not establish that a synthesis, clinical decision or trial conclusion changed. In particular, C007's printed interval and P value both indicate nominal significance; its discrepancy concerns their joint numerical construction under the stated diagnostic, whose identity with the actual author method is not established.

## Package and Reused-Evidence Provenance

Document roles were assigned by content. The protocol/SAP supplement is `PLAN`; the article, results supplement and data-sharing statement are `REPORT`.

| Source ID | Supplied filename | Role | Complete supplied scope |
|---|---|---|---|
| DOC001 | [jama_urashima_2019_oi_190023.pdf](../jama_urashima_2019_oi_190023.pdf#page=1) | REPORT | Main article, PDF pp.1–9 |
| DOC002 | [joi190023supp1_prod.pdf](../joi190023supp1_prod.pdf#page=1) | PLAN | 45 pages: contents p.1; initial version pp.2–16; final version pp.17–33; references pp.34–35; appendices pp.36–44; amendments p.45 |
| DOC003 | [joi190023supp2_prod.pdf](../joi190023supp2_prod.pdf#page=1) | REPORT | Results supplement, PDF pp.1–41 |
| DOC004 | [joi190023supp3_prod.pdf](../joi190023supp3_prod.pdf#page=1) | REPORT | Data-sharing statement, PDF p.1 |

The curator inventoried and hashed **381 eligible existing assets**: 274 usable, 98 duplicate, eight partial and one stale; none was unreadable. They include native/layout text, normalized text, OCR, rendered pages and extraction/identity metadata. Partial identity records and stale tooling metadata were not allowed to define review scope. Alternate page-specific native text supplied usable extraction for main-article p.9 despite its absence from one earlier derivative group.

Existing extraction was reused as a locator and transcription aid. Current agents rebuilt discovery, mapping, screening and classification from supplied evidence; earlier candidate sets, decisions and final reports were not scientific inputs. Exact supplied PDF pages controlled the mechanical rechecks. Available direct Poppler tools produced targeted current-source text and CPU rasters, including a 180-dpi amendment-page render to distinguish paragraph-specific dates. No new OCR or Office conversion was necessary.

Durable provenance is recorded in [source_inventory.md](review_1_6_2/source_inventory.md), [evidence_asset_inventory.md](review_1_6_2/evidence_asset_inventory.md), and the before-review [source](review_1_6_2/source_hashes_before.sha256) and [reused-asset](review_1_6_2/reused_artifact_hashes_before.sha256) hash manifests.

## Scope, Complete Coverage, and Exclusions

The review covers counts and denominators; estimate, interval and test logic; source-described statistical method logic; and planned-versus-reported statistical design. Administrative, reference and appendix pages were inspected and mapped even when no result-relevant relationship applied. The complete supplied package is the evidence boundary; no external literature, registry or participant-level data was used.

| Source | Total pages | Reusable-backed pages | Fresh-required pages | Mapped pages | Coverage |
|---|---:|---:|---:|---:|---|
| DOC001 | 9 | 9 | 0 | 9 | COMPLETE |
| DOC002 | 45 | 45 | 0 | 45 | COMPLETE |
| DOC003 | 41 | 41 | 0 | 41 | COMPLETE |
| DOC004 | 1 | 1 | 0 | 1 | COMPLETE |
| **Total** | **96** | **96** | **0** | **96** | **COMPLETE** |

Reusable and fresh-required counts partition all source pages. Zero fresh-required pages means that usable extraction already covered every page; it does not mean that fresh scientific mapping or direct-source confirmation was omitted. Optional rendered-image gaps were closed where needed by current targeted renders or usable source text. There is no scientific-coverage gap.

Main and support mapping proceeded over disjoint scopes, with two disjoint 20-page visual shards covering the results supplement's pp.2–41. Every shard and stage has one artifact path per row in [coverage_manifest.md](review_1_6_2/coverage_manifest.md). The source-level accounting is in [source_coverage.md](review_1_6_2/source_coverage.md).

Differences resolved by display precision, matching populations, stated model-versus-crude distinctions, immediately resolvable terminology or peripheral administrative comparisons were excluded under the normative scope. The review does not conduct a broad clinical, design, novelty, misconduct or raw-data assessment, and does not recommend a preferred analysis.

## Quantitative and Statistical Relationship Coverage

| Inventory or stage | Completed scope | Durable record |
|---|---|---|
| Numeric relationships | N001–N105: counts, denominators, totals, percentages, matched copies and effect-measure identity | [Numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md) |
| Statistical relationships | S001–S106: 78 distinct result relationships and 28 method/design relationships | [Statistical inventory](review_1_6_2/statistics/relationship_inventory.md) |
| Statistical pass 1 | All 106 records, individually marked PASS_1_COMPLETE | [Pass 1](review_1_6_2/checkers/statistical_pass_1.md) |
| Statistical pass 2 | All 106 records, individually marked PASS_2_COMPLETE; complete ledger, screen and recheck implications revisited | [Pass 2](review_1_6_2/checkers/statistical_pass_2.md) |
| Exclusion reconsideration | All 39 original checker exclusion rows reread; one raised as F-ST2-001, 38 retained | [Lossless original exclusion projection](review_1_6_2/checkers/all_excluded_observations.md) |
| Evidence-quality audit | All seven stable IDs, screening in both directions, original exclusions, source coverage, classifications and execution controls | [Quality audit](review_1_6_2/quality/evidence_quality_audit.md) |

Result coverage includes main effect estimates and laboratory comparisons, achieved-mean vitamin-D model estimates, imputed analyses, genotype panels and post hoc panels. Within-panel treatment estimates and interaction tests were checked separately. An interaction P value was not substituted for a within-subgroup P value. The 38 retained original exclusion rows consolidate to 28 distinct retained observations in pass 2; these are not additional finding-screen decisions.

Both passes checked endpoint order, estimate containment, null/test agreement, effect direction, analysis populations and planned specifications. Missing unrounded outputs or inferential constructions were named in the relationship records rather than inferred. The final-plan sample-size calculation reproduced its displayed approximately 120 events and 400 participants under the source-specified Freedman setup. No printed interval/P tuple reverses nominal significance; C007 concerns a narrower diagnostic incompatibility.

## Inclusion Screening Summary

A finding qualified when reproduced and either within an always-register category (Route A) or in focus, unresolved by immediate context and relevant to interpretation/extraction (Route B). Display rounding was assessed with half-unit intervals and the relative-discrepancy rule; the general 0.05 exemption does not apply to Route A category 1 interval-versus-P/test conflicts. Repeated instances of one pattern were consolidated.

| Screening stage | Findings screened | INCLUDE | SCREENED_OUT |
|---|---:|---:|---:|
| Initial | 12 | 6 | 6 |
| Pass 2 | 1 | 1 | 0 |
| **Total** | **13** | **7** | **6** |

| Decision | Reason code | Count |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 7 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 6 |
| **Total** | | **13** |

The six duplicate findings retain their provenance and affected locations within C001–C004 and C006. Every included finding maps to a stable candidate. No screened-out finding receives a separate evidence card. All other screened-out reason codes have zero finding-screen decisions; checker self-screened exclusions are separately accounted for above. The scientific audit confirmed all 13 decisions without adding an audit-stage finding or reversing a decision. See the single canonical table in [inclusion_screen.md](review_1_6_2/screening/inclusion_screen.md) and fresh [pass-2 working screen](review_1_6_2/screening/inclusion_screen_pass_2.md).

## Review-Domain Summary

| Review domain | Definition | Candidates |
|---|---|---:|
| statistical_results | Reported counts, estimates, intervals, tests or statistical methods | 3 |
| report_internal_inconsistency | Conflicting result attribution to outcome, time, population or comparison within report materials | 0 |
| protocol_report | Statistical design or analysis differences between REPORT and PLAN | 4 |
| plan_material | Statistical design inconsistency solely within PLAN | 0 |
| **Total** | | **7** |

| Primary relationship type | Candidates |
|---|---:|
| P_R | 4 |
| P_P | 0 |
| S_C | 0 |
| S_W | 3 |
| **Total** | **7** |

C001 additionally includes P_P; precedence selects P_R. Corroboration alone does not add a relationship. Consequently the seven primary-type counts reconcile to seven candidates, while C001's full relationship set preserves its plan-internal comparison.

| Evidence state | Candidates |
|---|---:|
| reproduced | 6 |
| reproduced_after_transcription_correction | 1 |
| not_reproduced | 0 |
| **Total** | **7** |

All seven inclusion audits are CONFIRMED. These are inclusion and evidence-record distinctions; every candidate remains Pending Human Adjudication.

## Candidate Index

| ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| C001 | De novo cancer outcome status | protocol_report | P_R | reproduced_after_transcription_correction | CONFIRMED |
| C002 | Planned Kaplan–Meier curve counterpart | protocol_report | P_R | reproduced | CONFIRMED |
| C003 | Planned relapse/safety RR evaluation counterpart | protocol_report | P_R | reproduced | CONFIRMED |
| C004 | Omitted prespecified high-baseline subgroup | protocol_report | P_R | reproduced | CONFIRMED |
| C005 | Genotype percentages and unstated denominators | statistical_results | S_W | reproduced | CONFIRMED |
| C006 | Shared Table 2 hazard-ratio direction statement | statistical_results | S_W | reproduced | CONFIRMED |
| C007 | Adjusted interval/P-value diagnostic compatibility | statistical_results | S_W | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — De novo cancer outcome status differs across final plan and report

**Pending Human Adjudication**

**Candidate statement:** The matched de novo cancer endpoint is tertiary in the final plan body and amendment, while the final synopsis and report retain adverse-event/safety status.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** REPORT main article pp.2–3 and8 vs PLAN final synopsis p19, body p25 and amendment p45; PLAN synopsis p19 vs body p25

**Evidence state:** reproduced_after_transcription_correction

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Qualifying route:** Route A, category 5

**Classification rationale:** REPORT versus final PLAN establishes P_R. Final PLAN synopsis versus body also establishes P_P. P_R takes precedence, assigning protocol_report. Initial synopsis content is historical corroboration.

**Classification ambiguity:** None for document roles or precedence; any unprovided subsequent hierarchy amendment remains a bounded evidence limitation.

**Exact source locations:** PLAN [initial synopsis, PDF p.4](../joi190023supp1_prod.pdf#page=4), [final synopsis, PDF p.19](../joi190023supp1_prod.pdf#page=19), [final body, PDF p.25](../joi190023supp1_prod.pdf#page=25) and [amendment, PDF p.45](../joi190023supp1_prod.pdf#page=45); REPORT [Outcomes beginning, PDF p.2](../jama_urashima_2019_oi_190023.pdf#page=2), [continuation and analysis populations, PDF p.3](../jama_urashima_2019_oi_190023.pdf#page=3) and [Table 3 de novo row and population footnotes, PDF p.8](../jama_urashima_2019_oi_190023.pdf#page=8).

**Source evidence:** The endpoint is cancer in organs other than the primary site after study medication begins. Final body p.25 calls it tertiary; amendment p.45 says it was separated from secondary and safety outcomes and inserted as tertiary. Final synopsis p.19 includes it as an adverse event, not an outcome. Main Outcomes and Table 3 call it safety. Initial synopsis p.4 corroborates the earlier adverse-event designation.

**Reported-versus-comparator:** Report safety designation and final-synopsis adverse-event designation versus final-body/amendment tertiary designation for the same endpoint. Duplicate F-ST1-004 is retained as checker provenance.

**Reasoning procedure:** Match organ restriction and timing before comparing hierarchy labels. Distinguish a status comparison from the explicitly different Table 3 analysis populations.

**Calculation:** Hierarchy is categorical; numerical rounding intervals are not applicable. Table 3's until-censoring per-protocol counts are 15/227 (6.6%) versus 8/147 (5.4%); one-year per-protocol counts are 16/243 (6.6%) versus 9/160 (5.6%); randomized counts are 16/251 (6.4%) versus 9/166 (5.4%). These are labeled different populations, not another count discrepancy.

**Affected result or extracted value:** De novo cancer outcome hierarchy and identification of the reported population/event count representing its analysis.

**Why context does not resolve it:** Route A category 5 covers a changed prespecified outcome status. Presentation in a safety table does not reconcile the explicit tertiary-versus-adverse-event statements.

**Alternative source-grounded interpretations:** The synopsis may retain earlier wording, or a tertiary outcome may have been presented with safety results. A subsequent hierarchy amendment is possible but not supplied. None is asserted as the observed explanation.

**Mechanical evidence recheck:** Every cited source location and endpoint label was matched to direct supplied-source text and rasters. A 180-dpi source render confirmed that the de novo and DBP paragraphs on plan p.45 print **2012.12.8**, while the version heading and subgroup paragraph print **2012.12.18**. Registration's de novo-date transcription was corrected to the paragraph-specific reading; the status comparison remained reproduced. This is not a separate date candidate. Roles, precedence and domain were confirmed.

**Potential downstream evidence impact:** If confirmed, an extractor could otherwise copy a different outcome-status code or select a different reported analysis-population column. No observed event reallocation, synthesis consequence or conclusion change is established.

## C002 — Planned Kaplan–Meier curves lack a reported counterpart among Nelson–Aalen displays

**Pending Human Adjudication**

**Candidate statement:** The supplied plans specify ITT Kaplan–Meier survival curves for primary relapse-free and key secondary overall survival; the report names Nelson–Aalen cumulative-hazard curves without a supplied reported Kaplan–Meier curve counterpart.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main article methods p3 and figures pp.6–7 vs PLAN initial SAP p14, final synopsis p19 and SAP p31

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002

**Qualifying route:** Route A, category 5

**Classification rationale:** Different named analysis displays in REPORT versus PLAN establish P_R and protocol_report. Agreeing initial/final plans do not create P_P.

**Classification ambiguity:** None.

**Exact source locations:** PLAN [initial SAP method 5c, PDF p.14](../joi190023supp1_prod.pdf#page=14), [final synopsis, PDF p.19](../joi190023supp1_prod.pdf#page=19), [final SAP method 5c, PDF p.31](../joi190023supp1_prod.pdf#page=31) and [amendment context, PDF p.45](../joi190023supp1_prod.pdf#page=45); REPORT [Methods, PDF p.3](../jama_urashima_2019_oi_190023.pdf#page=3), [Figure 2A/B and caption, PDF p.6](../jama_urashima_2019_oi_190023.pdf#page=6), [Figure 3 and caption, PDF p.7](../jama_urashima_2019_oi_190023.pdf#page=7), [abstract, PDF p.1](../jama_urashima_2019_oi_190023.pdf#page=1) and [survival summaries, PDF p.4](../jama_urashima_2019_oi_190023.pdf#page=4). Counterpart search covered the complete [results supplement, PDF pp.1–41](../joi190023supp2_prod.pdf#page=1) and [data-sharing statement, PDF p.1](../joi190023supp3_prod.pdf#page=1).

**Source evidence:** Both SAP versions prescribe Kaplan–Meier survival curves on ITT analysis, separately from Cox HR estimation. Main Methods and figure captions expressly name Nelson–Aalen cumulative-hazard curves. The complete supplied report mapping identifies no Kaplan–Meier curve counterpart or stated curve-method amendment.

**Reported-versus-comparator:** Named cumulative-hazard displays versus the planned survival-curve analysis. Five-year relapse-free survival is 77%/69% and overall survival 82%/81%; the report does not identify the estimator specifically producing these percentages. Duplicate F-ST1-002 is retained as provenance.

**Reasoning procedure:** Match endpoints and randomized analysis population, then compare the named curve methods and their displayed quantities. Keep Cox estimates, survival percentages and graphical estimators distinct.

**Calculation:** This specification comparison is categorical. No numerical rounding discrepancy is asserted for HR 0.76 (0.50–1.14), P=.18, HR 0.95 (0.57–1.57), P=.83, or the five-year survival percentages. No curve coordinates were reconstructed from pixels.

**Affected result or extracted value:** Planned primary/key-secondary curve-analysis status and estimator coding for the five-year survival summaries.

**Why context does not resolve it:** Route A category 5 covers a planned primary or key secondary analysis without a reported counterpart. A named Nelson–Aalen display does not document the separately planned Kaplan–Meier curve.

**Alternative source-grounded interpretations:** Kaplan–Meier may have generated the percentages while Nelson–Aalen supplied the plotted curves; an unsupplied amendment may have changed the display method. The evidence establishes counterpart absence within supplied reporting, not that Kaplan–Meier was never performed or that a particular estimator produced the percentages.

**Mechanical evidence recheck:** Exact plan statements, report Methods, axes and captions were matched against direct-source text and rasters. Complete report-supplement extraction and maps were checked for a counterpart. All roles, classification and the reproduced evidence state were confirmed.

**Potential downstream evidence impact:** An extractor could code the plotted analysis or percentage estimator without knowing how it relates to the prespecified curve analysis. No changed survival estimate or synthesis outcome is demonstrated.

## C003 — Planned relapse and safety risk-ratio evaluations lack reported counterparts

**Pending Human Adjudication**

**Candidate statement:** SAP method 5e specifies relapse and safety evaluation by risk ratio, while the report supplies post hoc relapse subdistribution HRs and descriptive safety cells without a named counterpart to the planned RR evaluations.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main article methods p3 and relapse/safety displays pp.6–8 vs PLAN initial SAP p14 and final SAP p31

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003

**Qualifying route:** Route B

**Classification rationale:** The conflict concerns REPORT versus PLAN analysis specification/status, assigning P_R and protocol_report. Both plan versions agree. A model-based estimate is not compared numerically with a crude ratio.

**Classification ambiguity:** None; Route B does not require asserting that every relapse/safety endpoint is key secondary.

**Exact source locations:** PLAN [initial SAP method 5e, PDF p.14](../joi190023supp1_prod.pdf#page=14) and [final SAP method 5e, PDF p.31](../joi190023supp1_prod.pdf#page=31); REPORT [post hoc competing-risk method, PDF p.3](../jama_urashima_2019_oi_190023.pdf#page=3), [Figure 2C and relapse narrative, PDF p.6](../jama_urashima_2019_oi_190023.pdf#page=6), [Table 2 relapse rows, PDF p.7](../jama_urashima_2019_oi_190023.pdf#page=7) and [all Table 3 safety rows and footnotes, PDF p.8](../jama_urashima_2019_oi_190023.pdf#page=8). Counterpart search covered the complete [results supplement](../joi190023supp2_prod.pdf#page=1) and [data-sharing statement](../joi190023supp3_prod.pdf#page=1).

**Source evidence:** Both SAPs explicitly specify RR evaluation. The report defines a post hoc competing-risk relapse analysis with subdistribution HRs; its safety display contains counts and percentages in three stated populations, with no RR or RR-interval column. Duplicate F-ST1-003 is retained as provenance.

**Reported-versus-comparator:** Total relapse subdistribution HR 0.75 (0.48–1.17), P=.21; low-baseline 1.18 (0.64–2.19), P=.59; middle-baseline 0.44 (0.21–0.89), P=.02. These retain their reported measure. The full safety pattern is:

| Safety outcome | Until-censoring per protocol, vitamin D/placebo 227/147 | One-year per protocol, 243/160 | Randomized, 251/166 |
|---|---|---|---|
| Fracture | 3 (1.3%) / 5 (3.4%) | 3 (1.2%) / 6 (3.8%) | 3 (1.2%) / 6 (3.6%) |
| Urinary stones | 2 (0.9%) / 0 (0.0%) | 4 (1.6%) / 2 (1.3%) | 4 (1.6%) / 4 (2.4%) |
| Severe adverse events | 19 (8.4%) / 9 (6.1%) | 20 (8.2%) / 13 (8.1%) | 21 (8.4%) / 15 (9.0%) |
| De novo cancer | 15 (6.6%) / 8 (5.4%) | 16 (6.6%) / 9 (5.6%) | 16 (6.4%) / 9 (5.4%) |

Table 3 defines adherence populations, randomization regardless of adherence, admission-related events, and other-organ post-medication cancer in its footnotes. These labeled populations are not treated as conflicting copies.

**Reasoning procedure:** Match endpoints, distinguish RR from subdistribution HR, and identify the planned evaluation's reporting status. The post hoc method explains the reported HR but does not identify a prespecified RR counterpart.

**Calculation:** Categorical measure/status comparison; numerical rounding intervals are not applicable. No crude RR is assigned as a substitute for a reported HR, and no numerical discrepancy in the three matched relapse estimates is asserted.

**Affected result or extracted value:** Relapse effect-measure coding and status of prespecified relapse/safety treatment comparisons.

**Why context does not resolve it:** B1: explicit analysis specification falls within focus area D. B2: post hoc competing-risk and descriptive safety reporting leave planned RR implementation/status unresolved. B3: that distinction bears on which treatment-comparison estimand and prespecification status an extractor records.

**Alternative source-grounded interpretations:** RRs may have been calculated but omitted, the reported analysis may be additional, or an unsupplied revision may have replaced them. Planned RR horizon and implementation population are not specified in method 5e. Deliberate descriptive safety reporting is possible. No preferred analysis is proposed.

**Mechanical evidence recheck:** Both SAP statements, all three relapse estimates, all safety rows/population columns and footnotes were matched against exact-source text and rasters. Complete supplied report maps contained no named RR counterpart. Roles, P_R/domain and reproduced state were confirmed.

**Potential downstream evidence impact:** An extractor could treat a subdistribution HR as the counterpart of a planned RR evaluation or code analysis status without its mapping being stated. No replacement measure or observed downstream consequence is assigned.

## C004 — Prespecified high-baseline vitamin-D subgroup analysis was omitted

**Pending Human Adjudication**

**Candidate statement:** The final SAP specifies the >40 ng/mL efficacy subgroup, while the report explicitly omits its analysis and limits interactions to low/middle groups because only five high-baseline participants were available.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main article high-baseline subgroup specification and omission pp.3–8 vs PLAN final SAP p31 and amendment p45

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004

**Qualifying route:** Route A, category 5

**Classification rationale:** REPORT versus PLAN analysis-scope specification establishes P_R and protocol_report. Amendment content corroborates the final SAP and adds no P_P conflict.

**Classification ambiguity:** None; the prespecified efficacy subgroup concerns primary/key-secondary endpoints.

**Exact source locations:** PLAN [final SAP subgroup/interaction specification, PDF p.31](../joi190023supp1_prod.pdf#page=31) and [subgroup amendment, PDF p.45](../joi190023supp1_prod.pdf#page=45); REPORT [Methods, PDF p.3](../jama_urashima_2019_oi_190023.pdf#page=3), [subgroup population and omission, PDF p.4](../jama_urashima_2019_oi_190023.pdf#page=4), [Table 1 high-group counts, PDF p.5](../jama_urashima_2019_oi_190023.pdf#page=5), [Figure 3 caption, PDF p.7](../jama_urashima_2019_oi_190023.pdf#page=7) and [limitations, PDF p.8](../jama_urashima_2019_oi_190023.pdf#page=8); [abstract, PDF p.1](../jama_urashima_2019_oi_190023.pdf#page=1) corroborates the reported two-group interaction context.

**Source evidence:** Final SAP lists low <20, middle 20–40 and high >40 ng/mL efficacy analyses. The report explicitly states that the high subgroup was not evaluated because of small numbers. The subgroup amendment paragraph prints 2012.12.18. Duplicate F-ST1-005 is retained as provenance.

**Reported-versus-comparator:** Planned three-group scope versus reported low/middle-only analyses. The reported interactions include relapse/death P=.04 and overall survival P=.13; no high-group estimate is inferred.

**Reasoning procedure:** Match baseline thresholds and efficacy endpoints. Preserve the disclosed small-n rationale while identifying the planned analysis lacking a reported counterpart. Look for a supplied minimum-size rule without inventing one.

**Calculation:** High-group counts reconcile: four vitamin D plus one placebo equals five. Low/middle/high totals 173+232+5=410 reconcile. The issue is categorical analysis scope, not a count discrepancy; rounding intervals do not apply.

**Affected result or extracted value:** Prespecified subgroup coverage and scope of the reported interaction tests.

**Why context does not resolve it:** Route A category 5 covers a planned primary/key-secondary analysis not reported. The openly disclosed small-sample rationale does not remove the reproduced scope difference.

**Alternative source-grounded interpretations:** A minimum-size condition or analysis amendment may have governed omission, but is not supplied. The observed practical rationale is retained. No analysis of five participants is recommended or preferred.

**Mechanical evidence recheck:** All specification, omission, count, caption and limitation locations were exact-source matched. The subgroup paragraph's 2012.12.18 date was confirmed separately from de novo/DBP paragraphs dated 2012.12.8. No date-only candidate follows. Roles, P_R/domain and reproduced state were confirmed.

**Potential downstream evidence impact:** An extractor could code prespecified subgroup completeness or interaction scope differently without the governing minimum-size/amendment definition. No unreported effect or changed treatment conclusion is inferred.

## C005 — Genotype percentages use unstated denominators differing from printed arm headers

**Pending Human Adjudication**

**Candidate statement:** Twenty-two genotype count/percentage cells do not reconcile with Table 1's printed 251/166 arm headers under display precision. Locus-category sums reconstruct plausible available-case denominators that the table does not state.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table1 p5 arm headers vs genotype count/percentage rows and footnotes

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-002

**Qualifying route:** Route A, category 3

**Classification rationale:** Headers, counts, percentages and footnotes conflict within one REPORT display, establishing S_W and statistical_results. Supplement category-count corroboration adds no S_C relationship.

**Classification ambiguity:** None; inferred available-case denominators remain an alternative interpretation.

**Exact source locations:** [Main article Table 1, PDF p.5](../jama_urashima_2019_oi_190023.pdf#page=5): both repeated arm headers; BsmI, Cdx2, ApaI, TaqI, DBP1 and DBP2 rows; footnotes a–c. Every affected cell is enumerated below.

**Source evidence:** Both table halves print vitamin D n=251 and placebo n=166 under counts/percentages. Footnote a addresses rounded percentage totals, b BMI and c pathology; none assigns a genotype denominator exception. The numerical relationship is also covered by statistical S104 and numeric N033–N038/N095.

**Reported-versus-comparator:** Printed integer percentages versus percentages recomputed from the same row's count and the explicit arm header, allowing half-unit intervals for each input.

**Reasoning procedure:** Read all six loci and table footnotes; assess all category cells, retaining only those with remaining relative gap >0.05; consolidate the shared denominator pattern as one candidate. Infer category-sum denominators only as a separate source-grounded alternative.

**Calculation:** For count c, denominator n and printed percentage p, the recomputed interval is `[100(c−0.5)/(n+0.5), 100(c+0.5)/(n−0.5)]`; compare with `[p−0.5,p+0.5]`. Remaining interval gap divided by p gives relative discrepancy. All 22 affected cells exceed 0.05:

| Locus / genotype | Arm and printed denominator | Printed count (%) | Recomputed interval, % | Printed percentage interval | Relative discrepancy |
|---|---|---|---|---|---|
| BsmI GG | Vitamin D,251 | 175 (76) | [69.383698,70.059880] | [75.5,76.5] | 0.071581 |
| BsmI GG | Placebo,166 | 119 (79) | [71.171171,72.205438] | [78.5,79.5] | 0.079678 |
| Cdx2 GG | Vitamin D,251 | 89 (39) | [35.188867,35.728543] | [38.5,39.5] | 0.071063 |
| Cdx2 GA | Vitamin D,251 | 103 (45) | [40.755467,41.317365] | [44.5,45.5] | 0.070725 |
| Cdx2 AA | Vitamin D,251 | 38 (17) | [14.910537,15.369261] | [16.5,17.5] | 0.066514 |
| Cdx2 GG | Placebo,166 | 49 (33) | [29.129129,29.909366] | [32.5,33.5] | 0.078504 |
| Cdx2 GA | Placebo,166 | 77 (51) | [45.945946,46.827795] | [50.5,51.5] | 0.072004 |
| ApaI GG | Vitamin D,251 | 96 (42) | [37.972167,38.522954] | [41.5,42.5] | 0.070882 |
| ApaI GT | Vitamin D,251 | 104 (45) | [41.153082,41.716567] | [44.5,45.5] | 0.061854 |
| ApaI GG | Placebo,166 | 69 (46) | [41.141141,41.993958] | [45.5,46.5] | 0.076218 |
| ApaI GT | Placebo,166 | 61 (40) | [36.336336,37.160121] | [39.5,40.5] | 0.058497 |
| TaqI TT | Vitamin D,251 | 172 (74) | [68.190855,68.862275] | [73.5,74.5] | 0.062672 |
| TaqI TT | Placebo,166 | 115 (77) | [68.768769,69.788520] | [76.5,77.5] | 0.087162 |
| TaqI TC | Placebo,166 | 31 (21) | [18.318318,19.033233] | [20.5,21.5] | 0.069846 |
| DBP1 TT | Vitamin D,251 | 134 (58) | [53.081511,53.692615] | [57.5,58.5] | 0.065645 |
| DBP1 TG | Vitamin D,251 | 87 (38) | [34.393638,34.930140] | [37.5,38.5] | 0.067628 |
| DBP1 TT | Placebo,166 | 82 (55) | [48.948949,49.848943] | [54.5,55.5] | 0.084565 |
| DBP1 TG | Placebo,166 | 57 (39) | [33.933934,34.743202] | [38.5,39.5] | 0.096328 |
| DBP2 CC | Vitamin D,251 | 115 (50) | [45.526839,46.107784] | [49.5,50.5] | 0.067844 |
| DBP2 CA | Vitamin D,251 | 91 (39) | [35.984095,36.526946] | [38.5,39.5] | 0.050591 |
| DBP2 CC | Placebo,166 | 81 (54) | [48.348348,49.244713] | [53.5,54.5] | 0.078802 |
| DBP2 CA | Placebo,166 | 58 (39) | [34.534535,35.347432] | [38.5,39.5] | 0.080835 |

The smallest retained relative gap is approximately 0.050591, rather than a value within the 0.05 exemption.

**Affected result or extracted value:** Baseline genotype proportions and locus-specific population denominators.

**Why context does not resolve it:** Route A category 3 covers count/denominator/percentage inconsistencies within one display. Recovering a plausible denominator from category sums does not make it a printed denominator instruction.

**Alternative source-grounded interpretations:** Available-case category sums reconstruct the following denominators and reconcile the printed percentages under the precision rule:

| Locus | Vitamin D category total | Placebo category total |
|---|---:|---:|
| BsmI | 231 | 150 |
| Cdx2 | 230 | 150 |
| ApaI | 231 | 150 |
| TaqI | 231 | 150 |
| DBP1 | 231 | 148 |
| DBP2 | 231 | 150 |

This supports a plausible missing-genotype/available-case explanation, without assigning replacement denominators or percentages. The separate DBP1 placebo 57/59 copy difference is below the workflow threshold and does not create another candidate.

**Mechanical evidence recheck:** Direct source text and Table 1 raster confirmed all headers, affected cells and footnotes. Independent screen, recheck and audit reproduced the full 22-cell calculations; alternative category sums were separately assessed. Roles, S_W/domain and reproduced state were confirmed.

**Potential downstream evidence impact:** An extractor could copy genotype percentages while attaching the printed arm totals as their denominators, or choose inferred available-case totals without a stated availability rule. No actual extraction consequence or replacement value is established.

## C006 — Table 2's shared hazard-ratio direction definition reverses the report interpretation

**Pending Human Adjudication**

**Candidate statement:** The shared Table 2 footnote assigns decreased outcome probability under vitamin D to HR values greater than 1, while the report interprets a matched below-1 adverse-outcome estimate as lower under vitamin D.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table2 p7 direction footnote vs its estimates and treatment interpretations pp.3–4 and6–7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Qualifying route:** Route A, category 2

**Classification rationale:** Both direction instructions and the matched estimates are within one REPORT. S_W and statistical_results apply; corroborating plan content would not create P_R.

**Classification ambiguity:** None.

**Exact source locations:** [Table 2 footnote a and every outcome/stratum row, PDF p.7](../jama_urashima_2019_oi_190023.pdf#page=7); [Statistical Analysis, PDF p.3](../jama_urashima_2019_oi_190023.pdf#page=3); [treatment-effect narrative, PDF p.4](../jama_urashima_2019_oi_190023.pdf#page=4); [matched middle relapse narrative and Figure 2C, PDF p.6](../jama_urashima_2019_oi_190023.pdf#page=6); and [Figure 3 treatment-direction corroboration, PDF p.7](../jama_urashima_2019_oi_190023.pdf#page=7).

**Source evidence:** Footnote a explicitly links HR>1 to decreased outcome probability under vitamin D. Main p.6 describes middle-baseline relapse subdistribution HR 0.44 (0.21–0.89), P=.02 as lower cumulative incidence in vitamin D than placebo. The table and narrative copies of 0.44 match numerically. Duplicate findings F-XS-005 and F-ST1-001 are retained as provenance.

**Reported-versus-comparator:** The single shared direction rule applies to all nine printed comparisons:

| Outcome | Stratum | Reported HR/subdistribution HR (95% CI) | P |
|---|---|---|---:|
| Relapse | Total | 0.75 (0.48–1.17) | .21 |
| Relapse | Low baseline | 1.18 (0.64–2.19) | .59 |
| Relapse | Middle baseline | 0.44 (0.21–0.89) | .02 |
| Cancer-specific death | Total | 1.09 (0.58–2.01) | .80 |
| Cancer-specific death | Low baseline | 1.45 (0.63–3.38) | .38 |
| Cancer-specific death | Middle baseline | 0.78 (0.29–2.10) | .63 |
| Noncancer death | Total | 0.70 (0.29–1.73) | .44 |
| Noncancer death | Low baseline | 1.11 (0.26–4.65) | .89 |
| Noncancer death | Middle baseline | 0.39 (0.11–1.39) | .15 |

**Reasoning procedure:** Match treatment contrast and adverse outcome, then compare the explicit above-null direction instruction with the report's interpretation of its identical below-null relapse result. Consolidate all rows governed by the shared footnote into one candidate.

**Calculation:** All nine point-estimate half-unit intervals retain their side of 1. For the matched 0.44 estimate, [0.435,0.445] stays below 1; its reciprocal-reference diagnostic [1/0.445,1/0.435]=[2.247191,2.298851] is disjoint. This diagnostic is not a replacement estimate. The matched numerical copies have gap zero; their direction statements conflict. No CI/P conflict is asserted for these nine rows.

**Affected result or extracted value:** Treatment reference and effect-direction coding of all nine Table 2 estimates.

**Why context does not resolve it:** Route A category 2 covers a direction/reference statement that reverses the printed reading. Adjacent narrative may permit reconstruction of an intended direction but does not remove the contrary printed table instruction.

**Alternative source-grounded interpretations:** The footnote may intend a reciprocal treatment reference or the opposite inequality. Neither is specified, and neither makes all printed statements agree without clarification. Composite relapse/death HR 0.76 and subgroup 0.46 corroborate direction only; they are not treated as numerically identical to relapse-only 0.44.

**Mechanical evidence recheck:** The shared footnote, all nine triples, matched narrative and treatment labels were exact-source matched. Independent calculations confirmed stable null sides and the reciprocal diagnostic. Roles, S_W/domain and reproduced state were confirmed.

**Potential downstream evidence impact:** Applying the printed footnote could reverse direction or reference coding when extracting a Table 2 effect. No actual propagation, replacement estimate or change in the overall trial conclusion is established.

## C007 — Adjusted interval and P value lack a joint solution under a same-page reproducing calculation

**Pending Human Adjudication**

**Candidate statement:** The age-quartile-adjusted relapse-free-survival HR 0.66, 95% CI 0.43–0.99 and P=.048 lack a joint rounded solution under an explicitly diagnostic symmetric log-Wald calculation that reproduces all five other complete same-page triples.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article p6 age-adjusted result vs p6 comparator displays and p3 method description

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST2-001

**Qualifying route:** Route A, category 1

**Classification rationale:** Target, comparator and method locations are within the same REPORT, assigning S_W and statistical_results. Nearby compatible results support a reproducing diagnostic, not an additional conflicting document.

**Classification ambiguity:** None for role/type/domain; the actual row-specific inferential construction is unprovided.

**Exact source locations:** [Main PDF p.6 age-adjusted relapse/death paragraph](../jama_urashima_2019_oi_190023.pdf#page=6); [p.6 adjacent adjusted-death sentence](../jama_urashima_2019_oi_190023.pdf#page=6); [p.6 Figure 2A](../jama_urashima_2019_oi_190023.pdf#page=6); [p.6 Figure 2B](../jama_urashima_2019_oi_190023.pdf#page=6); [p.6 Figure 2C and its relapse narrative copy](../jama_urashima_2019_oi_190023.pdf#page=6); [p.6 middle-baseline relapse paragraph](../jama_urashima_2019_oi_190023.pdf#page=6); and [p.3 Statistical Analysis/post hoc age adjustment](../jama_urashima_2019_oi_190023.pdf#page=3).

**Source evidence:** Target HR 0.66 (0.43–0.99), P=.048 is attributed to age-quartile-adjusted relapse/death. Methods specify Cox models, 95% CIs, age-quartile adjustment and two-sided P<.05, without identifying the target row's test or CI construction. Five other complete same-page tuples are shown below. S016 received both statistical passes; pass 2 reconsidered pass 1's conditional diagnostic exclusion under the always-register interval/test category, then received a fresh independent screen and recheck.

**Reported-versus-comparator:** Printed target P interval [.0475,.0485) versus diagnostic P bounds jointly constrained by the rounded HR and both CI limits. Supporting tuples are compatible with the same diagnostic after rounding; they are not five additional discrepancies.

**Reasoning procedure:** Label the calculation as diagnostic rather than attributing it to the actual author method. Impose log-symmetric confidence limits and all four display intervals simultaneously. Construct compatible unrounded examples for each neighboring tuple, and compare the complete target feasible range with its printed P interval. Keep nominal significance and numerical construction separate.

**Calculation:** Let b=ln(H), q=1.959963984540054, L=exp(b−q×SE), U=exp(b+q×SE), and two-sided P=2Φ(−abs(b)/SE). Joint symmetry requires H²=L×U. Target rounding intervals are H∈[.655,.665), L∈[.425,.435), U∈[.985,.995), and P∈[.0475,.0485). Conservative closed-bound joint extrema are:

| Extremum | H | L | U | SE | abs(b)/SE | Diagnostic P |
|---|---:|---:|---:|---:|---:|---:|
| Minimum | .655 | .435 | .986264367816 | .208824859934 | 2.026195748348 | .042744729167580 |
| Maximum | .655 | .431180904523 | .995 | .213324073718 | 1.983461294226 | .047315926395588 |

At fixed H, P increases with U. Feasibility imposes U≥H²/.435; at fixed U<1, P decreases with H, while on that lower-U feasibility boundary P increases with H. Both extrema therefore use H=.655, with L=.435 for the minimum and U=.995 for the maximum. Conservatively including rounding boundaries cannot enlarge the upper bound to .0475.

The diagnostic P range **[.042744729167580,.047315926395588]** remains below printed **[.0475,.0485)**. The minimum gap is **.000184073604412**; dividing by printed .048 gives **.003834866758583**. The general 0.05 relative-display exemption does not apply to Route A category 1. The five compatible constructive examples are:

| Relationship and printed H (L–U), P | Compatible H | Compatible L | Compatible U | Diagnostic P |
|---|---:|---:|---:|---:|
| S001: .76 (.50–1.14), .18 | .755025 | .502246867360 | 1.135025 | .176686709753 |
| S002: .95 (.57–1.57), .83 | .945025 | .570644079567 | 1.565025 | .826109001109 |
| S003: .75 (.48–1.17), .21 | .746525 | .475025209363 | 1.173200 | .205007266743 |
| S009: .44 (.21–.89), .02 | .435025 | .213832095845 | .885025 | .021617031427 |
| S017: .81 (.48–1.36), .42 | .805025 | .477888983574 | 1.356100 | .415003737171 |

All four rounding intervals are satisfied in each comparator example. They are constructive values, not recovered author outputs. S003/S009 retain subdistribution-HR labels. Numerical compatibility across Cox and competing-risk results does not prove a shared actual inferential method.

**Affected result or extracted value:** Mapping of adjusted primary relapse/death P=.048 to HR 0.66 and CI 0.43–0.99.

**Why context does not resolve it:** Route A category 1 applies to the reproduced diagnostic interval/test discrepancy. The source CI excludes 1 and source P<.05, so **nominal significance agrees**; no significance reversal is claimed. Immediate text does not identify the exact CI/test mapping.

**Alternative source-grounded interpretations:** A score or likelihood-ratio P paired with a Wald CI, another CI construction, or a separate test may explain the tuple. The actual unrounded coefficient/standard error, variance estimator, named test, statistic/degrees of freedom and row-specific interval construction are unprovided. Neither Stata use nor five compatible neighboring tuples identifies the actual method. No replacement P, interval or preferred method is assigned.

**Mechanical evidence recheck:** A fresh appended-ID rechecker independently matched all seven source-location groups, including Figure 2C and its narrative copy, using direct text and source rasters. Independent normal-tail integration reproduced the bounds and every comparator example. Refinement of the checker's normal approximation by about 4.4×10⁻⁹ preserved interval separation and required no source transcription correction. Roles, S_W/domain and reproduced state were confirmed; the independent audit reproduced the refined bounds.

**Potential downstream evidence impact:** An extractor could record the adjusted tuple without knowing whether its CI and P share a construction. The card preserves the printed values and their mapping question; it establishes no changed unadjusted primary conclusion, synthesis result or nominal significance decision.

## Downstream Evidence-Chain Considerations

Evidence extraction can carry forward outcome hierarchy, analysis status, population denominator, effect-measure identity and treatment direction as well as numerical estimates. The candidate cards identify which of those fields may require clarification from the supplied reporting. Preserving source links, population labels and diagnostic limits helps distinguish a reported quantity from an inferred explanation.

The report does not establish that any candidate has entered a systematic review, meta-analysis or guideline, or that a downstream decision changed. It assigns no replacement values. Each stable ID remains Pending Human Adjudication, including patterns that have a plausible source-grounded explanation.

## Limitations and Missing Definitions

Scientific coverage is complete for all supplied source pages; no required unit or candidate card is deferred. The available evidence consists of the supplied reports and plan material, not participant-level event/censoring data, full analysis code or unrounded statistical outputs. Direct-source confirmation establishes printed evidence and bounded comparisons rather than reconstruction of every actual analysis.

Missing definitions concern: the final de novo cancer hierarchy/population mapping; whether the planned Kaplan–Meier curves were performed and the survival-percentage estimator; planned RR implementation/status, time horizon and population; any governing minimum-size condition for the omitted subgroup; genotype availability rules and denominators; Table 2's intended reference/direction instruction; and C007's exact CI/test construction and unrounded inferential outputs. Unprovided amendments are possibilities, not evidence that they exist.

Other relationship-level limits include unreported interaction covariance/test construction, imputation pooling outputs, numerical proportional-hazards/stage-adjustment/interim outputs and precise unlabeled graphical coordinates. These limits were retained in the maps and inventories. No unknown details were invented to complete a check. Current direct tools were available, processing used CPU, and no fallback installation or GPU OCR was required. See [limitations.md](review_1_6_2/limitations.md).

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Routing, tooling and durable records

Routing preflight records PASS, default run model **gpt-6.1-sol**, coordinator/high, ordinary specialists/medium, and statistical/screening/recheck/audit specialists/high. All ten named presets were checked. Execution mode is INTERACTIVE_CLI and provider is CURRENT_SESSION. Mandatory stages used distinct fresh runtime agents; optional disjoint shards have their own runtime records. See [routing_preflight.md](review_1_6_2/routing_preflight.md) and [tooling_record.md](review_1_6_2/tooling_record.md).

Direct available tools include pdfinfo, pdftotext, pdftoppm, pdftocairo, tesseract, libreoffice and pandoc. Actual current extraction/raster confirmation used available Poppler tools on CPU; hashes use sha256sum. No temporary fallback environment was created. No supplied source or reused asset was edited. Earlier audit artifacts were preserved.

Final SHA-256 recomputation confirms that all four supplied sources and all381 reused assets remain unchanged. The [source after-hashes](review_1_6_2/source_hashes_after.sha256) and [reused-asset after-hashes](review_1_6_2/reused_artifact_hashes_after.sha256) match their before-review manifests exactly. Standalone HTML is rendered locally with embedded CSS and a table of contents; the final mechanical result is recorded in [review_validation.json](review_1_6_2/review_validation.json). Canonical [ledger](review_1_6_2/candidate_ledger.md), [recheck](review_1_6_2/verification/evidence_recheck.md) and [quality audit](review_1_6_2/quality/evidence_quality_audit.md) contain the same seven stable IDs as this report. Post-assembly comparison confirms that every report classification field matches the audited ledger literally.

### Agent execution

All 17 actual agents, including the coordinator, are recorded below. Specialist IDs encode the exact runtime canonical identifier with its leading slash removed; prefixing `/` recovers it. Each agent's primary artifact is relative to review_1_6_2; the complete artifact assignment is in the coverage manifest.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary artifact |
|---|---|---|---|---|---|
| coordinator | 01a1294f-634f-7bb3-a0ec-5f572bfe674e | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | root/curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_figures_a | root/support_figures_a | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_figures_a.md |
| support_quantitative_mapper_figures_b | root/support_figures_b | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_figures_b.md |
| numeric_consistency_reviewer | root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | root/statistics_pass_1 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | root/initial_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | root/evidence_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | root/statistics_pass_2 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| quality_control_coverage_auditor | root/coverage_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/coverage_audit.md |
| quality_control_auditor | root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| inclusion_screener_pass_2 | root/pass_2_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_pass_2 | root/pass_2_rechecker | gpt-6.1-sol | high | FRESH_SPAWN | verification/parts/evidence_recheck_pass_2.md |
| report_generator | root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

### Reproducibility performance

- **Target basis:** Four native-text PDFs with 96 unique pages and full reusable extraction, no Office conversion or mandatory fresh OCR; 40 supplement figure/table pages require visual reading in two parallel disjoint 20-page shards, initial/final protocol and SAP versions require matched statistical-design mapping, and mandatory mapping, checking, screening, recheck, second statistical pass, audit and report agent waves remain. Reuse reduces preprocessing while complete relationship review remains required.
- **Total source units:** 96
- **Fresh-source units:** 0
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-10-11T04:55:10Z
- **Finished UTC:** 2026-10-11T05:46:49Z
- **Observed elapsed minutes:** 51.65
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Complete106-relationship second-pass review raised one additional interval/test finding, requiring a different fresh inclusion screen and appended-ID source recheck; serial final inclusion audit and complete seven-card report assembly followed those released handoffs.
