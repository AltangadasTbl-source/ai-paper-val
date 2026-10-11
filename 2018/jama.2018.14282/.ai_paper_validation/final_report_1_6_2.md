# Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.2

> **Pending Human Adjudication.** All 16 candidates remain pending human adjudication. Evidence reproduction and inclusion audits are quality-control records, not human decisions.

## Executive Quality-Control Summary

Complete review of the four supplied PDFs identified **16 stable candidate reporting issues**, C001–C016. Exact-source evidence recheck reproduced all 16, and independent quality review recorded 16 CONFIRMED inclusion audits. The candidates concern statistical results, result attribution, and planned-versus-reported statistical design. The review assigns no severity or final disposition and makes no claim that a candidate changed the trial conclusion or propagated into evidence synthesis.

The initial independent screen considered 32 checker findings: 16 were included and 16 were consolidated as duplicates of included issues. Every supplied page was mapped anew using reusable source-linked evidence assets; there is no scientific-coverage gap. Both fresh statistical passes reviewed the complete set of 99 statistical relationships. The report preserves every stable ID, repeated affected location, source-grounded alternative and reconstruction limit.

## Package and Reused-Evidence Provenance

The package concerns the HIGH randomized trial of high-flow versus standard oxygen therapy in immunocompromised patients with acute respiratory failure. The main article reports 778 randomized participants and 776 analyzed participants, 388 per arm. Document roles are assigned from content: the prospective protocol/SAP bundle is PLAN, and the article, results supplement and retrospective data-sharing statement are REPORT.

| Stable source ID | Actual supplied filename and entry page | Content role | Complete physical page scope |
|---|---|---|---|
| DOC-001 | [jama_azoulay_2018_oi_180109.pdf](<../jama_azoulay_2018_oi_180109.pdf#page=1>) | REPORT | 1–9 |
| DOC-002 | [joi180109supp1_prod.pdf](<../joi180109supp1_prod.pdf#page=1>) | PLAN | 1–129 |
| DOC-003 | [joi180109supp2_prod.pdf](<../joi180109supp2_prod.pdf#page=1>) | REPORT | 1–5 |
| DOC-004 | [joi180109supp3_prod.pdf](<../joi180109supp3_prod.pdf#page=1>) | REPORT | 1 |

The protocol/SAP bundle contains earlier and final prospective versions, including an initial noninferiority design and a revised superiority design. Version evolution is interpreted with the article's disclosed redesign; it is not itself treated as a plan-internal inconsistency.

The curator inventoried and hashed **432 reusable assets**: 381 USABLE, 15 PARTIAL and 36 DUPLICATE; none STALE or UNREADABLE. These comprise 332 text files, 97 PNGs and 3 page/location manifests. Assets are preserved under earlier preprocessing directories. No separate OCR, structured-table, workbook or Office extraction asset exists. Native/layout streams contain the tables, and complementary rendered pages support graphical reading. Reuse provides locators and transcription aids; exact supplied PDFs remain the evidence authority.

Original reusable extraction/render engine versions are not recorded. Current fitness checks and targeted confirmations use Poppler 25.03.0; full-document native extraction matches current source extraction for three documents and differs only in word-preserving line ordering on plan page 11. Existing graphical layout text is supplemented by page images. Earlier candidate sets, screening decisions and final reports were not scientific discovery inputs. Detailed provenance is recorded in [source_inventory.md](review_1_6_2/source_inventory.md) and [evidence_asset_inventory.md](review_1_6_2/evidence_asset_inventory.md).

## Scope, Complete Coverage, and Exclusions

The review covers counts and denominators, estimate/interval/test logic, statistical method logic, and planned-versus-reported statistical design. Cross-location comparisons concern matching results and their analysis identity; plan comparisons concern primary or key-secondary analyses, endpoint status and randomized intervention specifications. The review does not perform a raw-data, broad clinical, novelty or misconduct audit and does not propose a preferred analysis.

| Source | Total units | Reusable units | Fresh-required units | Mapped units | Coverage |
|---|---:|---:|---:|---:|---|
| DOC-001 | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-002 | 129 | 129 | 0 | 129 | COMPLETE |
| DOC-003 | 5 | 5 | 0 | 5 | COMPLETE |
| DOC-004 | 1 | 1 | 0 | 1 | COMPLETE |
| **Total** | **144** | **144** | **0** | **144** | **COMPLETE** |

Units are unique physical PDF pages, including covers, administrative pages, references and near-empty pages. Reusable plus fresh-required units partition each source total; mapped units equal every total. Fresh-required refers to extraction gaps, not scientific review: every page received a new mapping assignment. The main mapper covered DOC-001; four disjoint support scopes covered plan pages 1–32, 33–64, 65–94 and 95–129, with the last also covering all results and data-sharing pages. Pages without applicable quantitative content remain explicitly mapped.

Display-precision comparisons allow every printed input and comparator its half-unit rounding interval. A nonoverlap gap relative to the printed reference at most 0.05 is screened out, except that interval-versus-P/test conflicts always follow Route A category 1. Standalone display-zero P values, immediately resolvable notation or terminology, modeled estimates compared with crude ratios, conditional observations, peripheral administrative comparisons and out-of-focus observations are excluded under the scope rules. Missing fitted inputs limit reconstruction, rather than allowing omission of a reviewed relationship.

Complete coverage and stage allocation are recorded in [source_coverage.md](review_1_6_2/source_coverage.md) and [coverage_manifest.md](review_1_6_2/coverage_manifest.md).

## Quantitative and Statistical Relationship Coverage

| Reviewed relationship set | Complete count | Completion evidence |
|---|---:|---|
| Numeric relationships N001–N104 | 104 | [numeric_relationship_inventory.md](review_1_6_2/relationships/numeric_relationship_inventory.md) |
| Statistical relationships S001–S099, pass 1 | 99 | Individual PASS_1_COMPLETE records in [relationship_inventory.md](review_1_6_2/statistics/relationship_inventory.md) |
| Statistical relationships S001–S099, pass 2 | 99 | Individual PASS_2_COMPLETE records in the same inventory and [statistical_pass_2.md](review_1_6_2/checkers/statistical_pass_2.md) |
| Matched cross-source/location groups | 72 | [cross_source_consistency.md](review_1_6_2/checkers/cross_source_consistency.md) |
| Initial checker excluded-observation rows revisited | 37 | 10 numeric, 14 statistical-pass-1 and 13 cross-source rows |

The statistical passes used distinct fresh gpt-6.1-sol/high agents. Pass 1 reviewed all 99 relationships. Pass 2 reviewed the complete ledger, screening and recheck facts and revisited all 99 relationships in disjoint 60/39-record shards. The combined input exceeded the 200000-normalized-character context bound, so the additional fresh high-effort shard preserved coverage. Each relationship has both completion records, including relationships that yield no finding or require an unavailable definition.

Pass 2 reconsidered every checker excluded-observation row against the always-register categories and display-precision rule. It emitted no new findings. The independent quality audit also reconsidered exclusions and screening in both directions and emitted no new findings or screening changes. A second inclusion screen was therefore not triggered. Counts of excluded observations describe checker-stage self-screening and are distinct from the 32 finding rows in the independent inclusion log.

## Inclusion Screening Summary

A candidate requires reproduction and either an always-register Route A category or all three Route B criteria: in focus, unresolved by immediate context, and relevant to interpretation or extraction of a named result. The independent screen used the exact cited supplied-source locations. Repeated occurrences were consolidated as one issue while preserving every affected location and checker provenance.

| Decision | Reason code | Findings |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 16 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 16 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONTEXT_RESOLVES | 0 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| **Total screened** | | **32** |

| Source checker | Findings screened | INCLUDE | SCREENED_OUT |
|---|---:|---:|---:|
| Numeric consistency reviewer | 4 | 4 | 0 |
| Cross-source consistency reviewer | 14 | 11 | 3 |
| Statistical pass 1 | 14 | 1 | 13 |
| **Total** | **32** | **16** | **16** |

These counts reconcile to the single table in [inclusion_screen.md](review_1_6_2/screening/inclusion_screen.md). All 16 included representatives map to 16 stable IDs. The duplicate rows map to those same preserved IDs and receive no separate cards. Seven candidates qualify through Route A category 5, two through category 3, one through category 2, one through category 4, and five through Route B.

## Review-Domain Summary

The four review domains are quantitative reporting categories. Statistical results covers counts, estimates, intervals, tests and statistical methods within REPORT materials. Report internal inconsistency covers conflicting result attribution to a population, outcome, time or comparison. Protocol report covers PLAN-versus-REPORT statistical design and analysis specifications. Plan material covers conflicting statistical design elements solely within PLAN materials.

| Review domain | Stable candidates |
|---|---:|
| statistical_results | 6 |
| report_internal_inconsistency | 1 |
| protocol_report | 9 |
| plan_material | 0 |
| **Total** | **16** |

| Primary relationship type | Meaning | Stable candidates |
|---|---|---:|
| P_R | PLAN versus REPORT | 9 |
| P_P | Within/between PLAN material | 0 |
| S_C | Between different REPORT documents | 2 |
| S_W | Within one REPORT document | 5 |
| **Total** | | **16** |

Primary relationships follow P_R > P_P > S_C > S_W precedence. C001 also has S_W, and C002 also has S_W; their primary relationships remain S_C and P_R respectively. Corroborating documents do not create additional conflict relationships.

| Evidence state | Stable candidates |
|---|---:|
| reproduced | 16 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| **Total** | **16** |

Inclusion audits are CONFIRMED for 16 and QUESTIONED for 0. Every card remains Pending Human Adjudication. Each summary independently reconciles to the 16-candidate ledger.

## Candidate Index

| Stable ID and candidate | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|
| [C001 — Oxygenation result assigned to different time origins](#c001) | report_internal_inconsistency | S_C | reproduced | CONFIRMED |
| [C002 — Stratum and subgroup cutpoints change across specifications](#c002) | protocol_report | P_R | reproduced | CONFIRMED |
| [C003 — Control-group HFNO prohibition versus reported rescue allowance](#c003) | protocol_report | P_R | reproduced | CONFIRMED |
| [C004 — Final-plan measurement components have no supplied outcome results](#c004) | protocol_report | P_R | reproduced | CONFIRMED |
| [C005 — Final-plan primary analyses are replaced or not identified](#c005) | protocol_report | P_R | reproduced | CONFIRMED |
| [C006 — Final-plan competing-risk secondary analyses differ from the report](#c006) | protocol_report | P_R | reproduced | CONFIRMED |
| [C007 — IMV cumulative-incidence P value assigned two test names](#c007) | statistical_results | S_C | reproduced | CONFIRMED |
| [C008 — Four Table 1 count/percentage pairs do not reconcile](#c008) | statistical_results | S_W | reproduced | CONFIRMED |
| [C009 — Planned joint longitudinal analyses are not identified](#c009) | protocol_report | P_R | reproduced | CONFIRMED |
| [C010 — Planned ICU-stay estimators and populations are not identified](#c010) | protocol_report | P_R | reproduced | CONFIRMED |
| [C011 — Initially secondary intubated mortality receives post hoc status](#c011) | protocol_report | P_R | reproduced | CONFIRMED |
| [C012 — Figure 3 hazard-ratio direction and favors headings](#c012) | statistical_results | S_W | reproduced | CONFIRMED |
| [C013 — Infection HR interval differs from a same-display reproducing construction](#c013) | statistical_results | S_W | reproduced | CONFIRMED |
| [C014 — Therapy counts use pooled percentages but arm-specific attribution](#c014) | statistical_results | S_W | reproduced | CONFIRMED |
| [C015 — Figure 3 subgroup population accounting is not supplied](#c015) | statistical_results | S_W | reproduced | CONFIRMED |
| [C016 — Two analyses called predefined have no supplied prospective specification](#c016) | protocol_report | P_R | reproduced | CONFIRMED |

## Candidate Evidence Cards

H denotes high-flow oxygen therapy; C denotes standard oxygen therapy. All PDF locations are physical pages. Each card repeats the final ledger classification exactly. Duplicate checker finding IDs are preserved as provenance in the ledger and screening records; the Finding IDs field below contains the INCLUDE representative recorded in the ledger classification table.

<a id="c001"></a>

## C001 — Oxygenation result assigned to different time origins

**Pending Human Adjudication.**

**Candidate statement:** The key-secondary oxygenation effect is associated with an after-intubation window in the abstract and with an after-randomization origin in the matching supplementary display.

**Review domain:** report_internal_inconsistency

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT main pp.1/6 vs REPORT results supplement pp.2/4

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Qualifying route:** Route B

**Classification rationale:** Every location is REPORT by content: published trial results and results eTable/eFigure. Primary S_C; all relationships S_C, S_W; domain report_internal_inconsistency because the issue is which time/population the result belongs to. S_C has precedence over S_W. No PLAN comparison is involved.

**Classification ambiguity:** The unsupplied additional-analysis alternative concerns result mapping, not document role.

**Exact source locations:** [jama_azoulay_2018_oi_180109.pdf — Main page 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>), Main Outcomes and Measures and Results; [jama_azoulay_2018_oi_180109.pdf — main page 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>), Secondary Outcomes; [joi180109supp2_prod.pdf — results supplement page 2](<../joi180109supp2_prod.pdf#page=2>), eTable title and PaO2/FIO2 row; [joi180109supp2_prod.pdf — results supplement page 4](<../joi180109supp2_prod.pdf#page=4>), eFigure 2B axis. All four cited locations were found in direct page extraction.

**Source evidence:** The abstract defines PaO2:FIO2 over three days after intubation and reports 150 versus 119 with difference 19.5, 95% CI 4.4–34.6. The body repeats 150/119 and that effect while describing higher oxygenation until day 4.

**Reported-versus-comparator:** The eTable explicitly says six hours after randomization and prints 150 [104–230] versus 119 [86–165]. The graph starts at Randomization, then H6 and days 1–7. Its origin and H6 location agree with the eTable.

**Reasoning procedure:** Route B, focus B/C, compares a key-secondary result's outcome time origin and population attribution. These are distinct analysis definitions, not immediately interchangeable terms. The affected extracted result is the oxygenation effect 19.5 (4.4–34.6). Directly observed: different printed origins attached to the matching oxygenation result. Inferred: the medians likely identify the same result and the abstract attribution may reflect a wording substitution; neither a production mechanism nor an additional analysis is established.

**Calculation:** The matching 150/119 values locate the report result but the abstract's after-intubation window does not map to the eTable's after-randomization window. Copied median intervals are [149.5,150.5] and [118.5,119.5] in both locations, gap 0; the body/abstract difference intervals [19.45,19.55], [4.35,4.45], [34.55,34.65] also overlap exactly. This is an attribution comparison, not a numeric discrepancy.

**Affected result or extracted value:** Oxygenation effect 19.5 (95% CI 4.4–34.6), its analyzed population, time origin and measurement window.

**Why context does not resolve it:** B1: result attribution is in focus. B2: intubation and randomization are different origins and can imply different populations; matching medians do not identify which window produced the mean effect. B3: an extractor could assign 19.5 (4.4–34.6) to different populations or times.

**Alternative source-grounded interpretations:** The abstract may intend randomization, or may refer to an additional intubated analysis with matching values; the supplied report does not identify which applies.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. The printed medians, effect, interval and explicit time labels suffice for that comparison. Exact missing inputs/definitions: The analysis population and time origin/window for the 19.5 contrast, and whether a separate intubated-only analysis exists, are not supplied together. reproduced. Determining recheck fact: Current source pages preserve the after-intubation versus after-randomization labels alongside the matching oxygenation values. Remaining question: Which population, time origin and measurement window apply to the reported oxygenation effect 19.5 (95% CI 4.4–34.6)?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: Oxygenation effect 19.5 (95% CI 4.4–34.6), its analyzed population, time origin and measurement window. The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c002"></a>

## C002 — Stratum and subgroup cutpoints change across specifications

**Pending Human Adjudication.**

**Candidate statement:** The oxygen-flow boundary differs between final plan and report, and the ICU-day boundary differs between reported randomization and forest analysis, changing subgroup membership definitions.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_W

**Compared document roles:** PLAN pp.98/99 vs REPORT main pp.2/7; REPORT main pp.2/4/5 vs REPORT main p.7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-012

**Qualifying route:** Route B

**Classification rationale:** Main pages are REPORT results/methods; plan pages are PLAN prospective randomization/interaction specifications. Primary P_R; all relationships P_R, S_W; domain protocol_report. Oxygen creates P_R; the independent report ICU-time comparison creates S_W. The plan's time rule merely corroborates report randomization and is not an extra relationship. P_R has precedence.

**Classification ambiguity:** A possible disclosed or unsupplied amendment may explain the oxygen difference; roles remain unambiguous.

**Exact source locations:** [jama_azoulay_2018_oi_180109.pdf — Main page 2](<../jama_azoulay_2018_oi_180109.pdf#page=2>), Randomization; [jama_azoulay_2018_oi_180109.pdf — main page 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), subgroup methods and all four ICU timing rows in Table 1; [jama_azoulay_2018_oi_180109.pdf — main page 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), primary-outcome statement about three predefined subgroups; [jama_azoulay_2018_oi_180109.pdf — main page 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>), both Figure 3 panels' ICU-time and oxygen-flow rows; [joi180109supp1_prod.pdf — plan page 98](<../joi180109supp1_prod.pdf#page=98>), lines 1600–1601; [joi180109supp1_prod.pdf — plan page 99](<../joi180109supp1_prod.pdf#page=99>), lines 1602–1604. Each was found; both panel boundaries were also read visually.

- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A ICU-time 0–1/≥2 rows](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B ICU-time 0–1/≥2 rows](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A oxygen-flow ≤9/>9 rows](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B oxygen-flow ≤9/>9 rows](<../jama_azoulay_2018_oi_180109.pdf#page=7>)

**Source evidence:** Final plan oxygen flow <9 versus ≥9 L/min; ICU days D0,D1,D2 versus ≥D3. Report randomization uses >9 versus ≤9 L/min and ≤2 versus ≥3 days. Main methods describe forest subgroups as defined by stratification variables.

**Reported-versus-comparator:** Both forest panels use oxygen ≤9/>9, with H/C denominators 348/347 and 40/41; both use ICU time 0–1/≥2, with denominators 321/330 and 67/58. Table 1's day 0,1,2,≥3 counts are H 244,77,47,20 and C 251,79,38,20. The interaction P values for time are .15/.17 and for flow .39/.65 in mortality/IMV.

**Reasoning procedure:** Route B, focus D and A/C. Equality at 9 L/min changes plan/report stratum membership; day 2 changes reported randomization/forest membership. Primary-mortality and IMV subgroup populations and interactions are affected. The differing cutpoints and bin reconstruction are direct facts. Deliberate regrouping or amendment is an inferred explanation, not demonstrated implementation history.

**Calculation:** Forest low-time H 244+77=321 and C 251+79=330; high-time H 47+20=67 and C 38+20=58. The sums' ±1 intervals overlap the corresponding forest ±.5 intervals. The randomization low-time bins sum to 368 per arm; three count inputs yield [366.5,369.5]. Forest low-bin intervals [320.5,321.5] and [329.5,330.5] leave gaps 45 and 36, relative to 368 of .122283 and .097826. No numeric rounding can reverse the placement of exact boundary categories 9 L/min or day 2.

**Affected result or extracted value:** Primary-mortality and IMV subgroup population definitions and interactions: ICU-time P=.15/.17 and oxygen-flow P=.39/.65.

**Why context does not resolve it:** B1: randomization and subgroup definitions are in focus. B2: exactly 9 L/min and ICU day 2 enter different explicitly defined bins; the immediate methods/figure context does not identify a changed analysis rule. B3: primary-mortality and IMV subgroup memberships and interaction interpretations depend on those definitions.

**Alternative source-grounded interpretations:** Separate analysis bins may have been deliberately used; an amended oxygen boundary may account for the report definition. Neither a changed definition nor its timing is identified for these specific comparisons.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. Explicit plan/report boundaries, Table 1 counts and both forest panels suffice. Exact missing inputs/definitions: Counts exactly at oxygen flow 9 L/min, allocation-list boundary implementation, any amendment changing it, and the reason for day-2 regrouping are unavailable. reproduced. Determining recheck fact: Direct plan/report inequalities differ at 9 L/min, and the report's day-2 forest regrouping is independently reconstructed from Table 1. Remaining question: Which exact oxygen-flow and ICU-day cutpoints governed randomization and each forest analysis, and where are the corresponding analysis-specific definitions or changes recorded?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: Primary-mortality and IMV subgroup population definitions and interactions: ICU-time P=.15/.17 and oxygen-flow P=.39/.65. The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c003"></a>

## C003 — Control-group HFNO prohibition versus reported rescue allowance

**Pending Human Adjudication.**

**Candidate statement:** The final plan prohibits high-flow oxygen in controls while the report permits and records rescue high-flow oxygen for controls with do-not-intubate orders after standard-oxygen failure.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN p.99 vs REPORT main pp.3/5

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-011

**Qualifying route:** Route B

**Classification rationale:** The prospective control intervention is PLAN; report treatment and implementation descriptions are REPORT. Primary P_R; all relationships P_R; domain protocol_report.

**Classification ambiguity:** Possible amendment history, not document role. No within-report contradiction is asserted.

**Exact source locations:** [joi180109supp1_prod.pdf — Plan page 99](<../joi180109supp1_prod.pdf#page=99>), lines 1617–1623, especially 1621; [jama_azoulay_2018_oi_180109.pdf — main page 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>), control-treatment paragraph; [jama_azoulay_2018_oi_180109.pdf — main page 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), Interventions. All locations were found directly.

**Source evidence:** Final plan prohibits HFNO in the control group while allowing NIV only under stated conditions.

**Reported-versus-comparator:** Article expressly allows high-flow oxygen for control patients with do-not-intubate orders after standard-oxygen failure, then reports 30 (7.7%) switched and 14 (46.7%) died.

**Reasoning procedure:** Route B, focus D: permitted intervention in the implemented comparator differs from the supplied final-plan prohibition and bears on primary mortality and IMV treatment-strategy interpretation. This is a specification comparison, not a judgment about clinical rescue. Directly observed: categorical final-plan prohibition, article permission and 30 implemented switches. Inferred: an operational or ethical amendment may bridge them; no such specific amendment was identified.

**Calculation:** Prohibition and stated permission differ. The accompanying counts reconcile: 30/388=7.731959%; half-unit interval [7.593308,7.870968]% overlaps printed [7.65,7.75]%. The 14/30 proportion has interval [44.262295,49.152542]% overlapping printed [46.65,46.75]%. Arithmetic is not the candidate basis.

**Affected result or extracted value:** Comparator-treatment strategy for day-28 mortality and IMV, including rescue high-flow oxygen in 30 controls.

**Why context does not resolve it:** B1: the randomized comparator specification is in focus. B2: the reported rescue explanation does not identify authorization under the final-plan prohibition. B3: the treatment-policy interpretation of primary mortality and IMV depends on whether rescue HFNO was part of the planned comparator.

**Alternative source-grounded interpretations:** A rescue amendment or allocation-based ITT crossover framework could explain the implemented exception.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. Final treatment sentence, rescue sentence and implementation counts suffice. Exact missing inputs/definitions: Any intervention amendment, its approval/timing, and whether the rescue exception was prospectively authorized are not supplied. reproduced. Determining recheck fact: The supplied final plan and report retain conflicting prohibition/permission language for the same control intervention. Remaining question: What final intervention specification and amendment timing govern the control-group do-not-intubate rescue allowance?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: Comparator-treatment strategy for day-28 mortality and IMV, including rescue high-flow oxygen in 30 controls. The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c004"></a>

## C004 — Final-plan measurement components have no supplied outcome results

**Pending Human Adjudication.**

**Candidate statement:** Final-plan Borg dyspnea and lowest-SpO2 oxygenation measurement components have no identified outcome results in the supplied report materials.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN pp.38/46/90/103 vs REPORT main pp.1/3/4/6 and REPORT results supplement pp.2/4/5

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-009

**Qualifying route:** Route A, category 5

**Classification rationale:** All cited prospective objectives/endpoints/summaries are PLAN; article and results graphics are REPORT. Primary P_R; all relationships P_R; domain protocol_report. Earlier/final plan copies corroborate the retained components; they do not establish P_P.

**Classification ambiguity:** Possible later specification change is unavailable.

**Exact source locations:** [joi180109supp1_prod.pdf — Plan page 38](<../joi180109supp1_prod.pdf#page=38>), lines 548–550; [joi180109supp1_prod.pdf — page 46](<../joi180109supp1_prod.pdf#page=46>), lines 688–691; [joi180109supp1_prod.pdf — page 90](<../joi180109supp1_prod.pdf#page=90>), secondary-outcome summary; [joi180109supp1_prod.pdf — page 103](<../joi180109supp1_prod.pdf#page=103>), lines 1694–1697. REPORT locations found: [jama_azoulay_2018_oi_180109.pdf — main page 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>), abstract; [jama_azoulay_2018_oi_180109.pdf — page 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>), Study Outcomes; [jama_azoulay_2018_oi_180109.pdf — page 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), VAS method; [jama_azoulay_2018_oi_180109.pdf — page 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>), Secondary Outcomes; [joi180109supp2_prod.pdf — results supplement page 2](<../joi180109supp2_prod.pdf#page=2>), eTable; [joi180109supp2_prod.pdf — page 4](<../joi180109supp2_prod.pdf#page=4>), eFigure 2B; [joi180109supp2_prod.pdf — page 5](<../joi180109supp2_prod.pdf#page=5>), eFigure 3B.

**Source evidence:** Earlier plan specifies VAS and Borg dyspnea and lowest SpO2 plus PaO2/FIO2 oxygenation; final page 103 retains VAS and Borg and lowest SpO2 plus PaO2/FIO2 days 1–3. Final summary page 90 retains dyspnea and oxygenation as secondary outcomes.

**Reported-versus-comparator:** Article describes dyspnea on a 0–10 scale and VAS comparisons; supplement panel explicitly labels dyspnea VAS. Oxygenation results and eTable/graph use PaO2/FIO2. These outcomes are abstract reported. No Borg outcome or lowest-SpO2 outcome result is identified in the complete supplied article/results supplement.

**Reasoning procedure:** Route A, category 5, focus D: positively retained key-secondary measurement components lack identified result counterparts. Borg and VAS are different named measurements; lowest SpO2 and PaO2/FIO2 are different oxygenation quantities. This is independent of C009's longitudinal modeling comparison. Directly observed: retained named commitments and no identified report counterparts. Inferred: narrowing, noncollection or unpublished analysis; the source does not establish which occurred.

**Calculation:** Final named components remain in the plan but have no mapped supplied outcome results. SpO2 treatment targets and background discussion do not provide a lowest-SpO2 outcome analysis. Numeric half-unit intervals cannot resolve absent analysis/component identities; precision is inapplicable.

**Affected result or extracted value:** Measurement coverage of key-secondary dyspnea and oxygenation: Borg score and lowest SpO2 outcomes.

**Why context does not resolve it:** Route A, category 5 is an always-register category. The reproduced planned-versus-reported outcome/analysis mapping remains eligible even when an explanatory alternative is available; the specific alternative and missing definition are retained below.

**Alternative source-grounded interpretations:** Components may have been narrowed after planning or collected/analyzed without inclusion in the supplied report.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. Retained endpoint list, reported measurement definitions and full supplied report coverage suffice for a bounded report-mapping check. Exact missing inputs/definitions: Borg results, lowest-SpO2 results, or dated specification changes removing those components are absent. reproduced. Determining recheck fact: Both named components remain in the final endpoint list while the supplied reported measurement results identify only VAS and PaO2/FIO2. Remaining question: Which supplied results or specification changes apply to Borg dyspnea and lowest-SpO2 oxygenation?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: Measurement coverage of key-secondary dyspnea and oxygenation: Borg score and lowest SpO2 outcomes. The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c005"></a>

## C005 — Final-plan primary analyses are replaced or not identified

**Pending Human Adjudication.**

**Candidate statement:** Three retained final-plan primary-analysis commitments—day-28 relative risk, confounder adjustment and per-protocol analysis—have no identified supplied primary-result counterparts.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN pp.53/54/82/104 vs REPORT main pp.3/4/5/6/7/8 and REPORT results supplement pp.1/2/3/4/5

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004

**Qualifying route:** Route A, category 5

**Classification rationale:** Prospective analysis specifications are PLAN; published results/methods/limitations and results supplement are REPORT. Primary P_R; all relationships P_R; domain protocol_report. Earlier copies corroborate final commitments, not P_P.

**Classification ambiguity:** Possible unrecorded replacement history; document roles are clear.

**Exact source locations:** PLAN [joi180109supp1_prod.pdf — page 53](<../joi180109supp1_prod.pdf#page=53>), lines 786–787; [joi180109supp1_prod.pdf — page 54](<../joi180109supp1_prod.pdf#page=54>), 808–814; [joi180109supp1_prod.pdf — page 82](<../joi180109supp1_prod.pdf#page=82>), 1297–1302; [joi180109supp1_prod.pdf — page 104](<../joi180109supp1_prod.pdf#page=104>), 1723 and 1730–1736. REPORT [jama_azoulay_2018_oi_180109.pdf — main page 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>), primary method/ITT/redesign; [jama_azoulay_2018_oi_180109.pdf — page 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), methods; [jama_azoulay_2018_oi_180109.pdf — page 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), Table 2/Primary Outcome; [jama_azoulay_2018_oi_180109.pdf — page 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>), Post Hoc Outcomes; [jama_azoulay_2018_oi_180109.pdf — page 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>), Figure 3; [jama_azoulay_2018_oi_180109.pdf — page 8](<../jama_azoulay_2018_oi_180109.pdf#page=8>), unadjusted-treatment-effect limitation. Complete results supplement pages [joi180109supp2_prod.pdf — 1](<../joi180109supp2_prod.pdf#page=1>), [joi180109supp2_prod.pdf — 2](<../joi180109supp2_prod.pdf#page=2>), [joi180109supp2_prod.pdf — 3](<../joi180109supp2_prod.pdf#page=3>), [joi180109supp2_prod.pdf — 4](<../joi180109supp2_prod.pdf#page=4>), [joi180109supp2_prod.pdf — 5](<../joi180109supp2_prod.pdf#page=5>) were directly read. Every registered location was found.

**Source evidence:** Final plan explicitly retains PP analysis at line 1723, day-28 alive/dead classification with relative risk and 95% CI at 1731–1734, and analyses adjusted for potential confounders at 1734. Earlier plan copies show the same analysis pattern.

**Reported-versus-comparator:** Report identifies allocation-based ITT, 388 per arm, Kaplan–Meier, absolute risk difference and univariable Cox HR .98 (.77–1.24). It explicitly states estimates were not adjusted on stratification factors. Its center-frailty analysis is labeled post hoc; secondary ICU/hospital mortality RRs are labeled for those outcomes. Neither supplies the planned primary RR, adjusted or PP result. No counterpart is identified in the supplied results supplement.

**Reasoning procedure:** Route A, category 5, focus D: three explicit final-plan primary-analysis commitments lack identified results or replacements. RR and HR are separate estimands; no modeled estimate is compared with a crude ratio. Directly observed: requirements remain in the final plan and supplied named primary analyses do not identify their results. Inferred: supersession/template/unpublished execution; none is proven.

**Calculation:** Primary RR, adjusted and PP commitments persist in the final superiority plan and do not map to the named univariable Cox/ITT result. The plan phrase hospital death immediately follows binary alive/dead day-28 classification; that context is retained without a separate horizon candidate. Numeric precision is inapplicable to estimator/population identity; the HR is not recalculated as a primary RR.

**Affected result or extracted value:** Primary day-28 mortality estimand, adjusted analysis and per-protocol population, versus the reported ITT/univariable HR .98 (.77–1.24).

**Why context does not resolve it:** Route A, category 5 is an always-register category. The reproduced planned-versus-reported outcome/analysis mapping remains eligible even when an explanatory alternative is available; the specific alternative and missing definition are retained below.

**Alternative source-grounded interpretations:** Requirements may have been superseded, retained as template language, or implemented outside the supplied report. The grant-stage redesign is disclosed, but the analyzed final-plan page still contains these requirements.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. Final positive requirements and the report's affirmative model/population statements suffice. Exact missing inputs/definitions: The planned primary RR result, adjusted primary result, PP result, PP eligibility/deviation rules, adjustment covariate list and dated replacements are unavailable. reproduced. Determining recheck fact: Direct final-plan lines 1723 and 1731–1734 retain the PP/RR/adjustment requirements while supplied primary output is expressly ITT/univariable Cox without those identified counterparts. Remaining question: Were the primary RR, adjusted and PP analyses performed, and which results or dated plan changes identify their replacement?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: Primary day-28 mortality estimand, adjusted analysis and per-protocol population, versus the reported ITT/univariable HR .98 (.77–1.24). The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c006"></a>

## C006 — Final-plan competing-risk secondary analyses differ from the report

**Pending Human Adjudication.**

**Candidate statement:** Retained final-plan adjusted competing-risk analyses for IMV and infection do not map to the reported univariable IMV and infection-proportion procedures.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN pp.54/82/105 vs REPORT main pp.3/4/5/6

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-006

**Qualifying route:** Route A, category 5

**Classification rationale:** All prospective framework pages are PLAN; article methods/results are REPORT. Primary P_R; all relationships P_R; domain protocol_report. Earlier plan copies corroborate the final framework.

**Classification ambiguity:** Possible method amendment or abbreviated description remains a human mapping question.

**Exact source locations:** PLAN [joi180109supp1_prod.pdf — page 54](<../joi180109supp1_prod.pdf#page=54>), 816–821; [joi180109supp1_prod.pdf — page 82](<../joi180109supp1_prod.pdf#page=82>), 1305–1310; [joi180109supp1_prod.pdf — page 105](<../joi180109supp1_prod.pdf#page=105>), 1738–1742. REPORT [jama_azoulay_2018_oi_180109.pdf — main page 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>), IMV competing risk; [jama_azoulay_2018_oi_180109.pdf — page 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), tests/models; [jama_azoulay_2018_oi_180109.pdf — page 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), Table 2 and footnote d; [jama_azoulay_2018_oi_180109.pdf — page 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>), Secondary Outcomes. Every registered location was found.

**Source evidence:** Final plan requires cumulative incidence for IMV/infection, death or live ICU discharge as competitors, Gray comparison and cause-specific Cox adjustment for potential confounders.

**Reported-versus-comparator:** Report defines death without IMV as a competitor, describes nonparametric IMV incidence/Gray comparison and univariable cause-specific Cox, and compares infection proportions using chi-square. Table 2 prints IMV HR .85 (.68–1.06), P=.17 and infection HR 1.01 (.96–1.06), P=.91 with cause-specific-HR footnote d.

**Reasoning procedure:** Route A, category 5, focus D: explicit adjusted competing-risk analyses of key-secondary outcomes are replaced or unidentified in the report. The IMV discharge handling and infection incidence/Gray mapping are specific supplied-plan elements. Directly observed: distinct method statements and no supplied identified adjusted counterparts. Inferred: omitted description or analytic replacement; execution details cannot be recovered from aggregate outputs.

**Calculation:** Univariable IMV Cox does not identify the promised confounder adjustment; infection proportions/chi-square do not identify the promised cumulative-incidence/Gray analysis. Death-without-IMV alone does not specify the planned live-discharge handling. No numeric HR/crude or interval/P conflict is inferred here. Display precision is inapplicable to method identity.

**Affected result or extracted value:** Key-secondary IMV HR .85 (.68–1.06), P=.17 and infection HR 1.01 (.96–1.06), P=.91, and their competitor/adjustment/test definitions.

**Why context does not resolve it:** Route A, category 5 is an always-register category. The reproduced planned-versus-reported outcome/analysis mapping remains eligible even when an explanatory alternative is available; the specific alternative and missing definition are retained below.

**Alternative source-grounded interpretations:** The report may abbreviate discharge handling, and separate proportion/incidence models may coexist; an amended method may have replaced adjustment.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. Positive prospective framework, affirmative reported methods and output identities suffice. Exact missing inputs/definitions: Infection event-time/risk-set analysis, live-discharge censor/competition rule, covariates, adjusted model results and mapping of incidence versus proportion tests are unavailable. reproduced. Determining recheck fact: The final plan explicitly retains adjustment and incidence/competition specifications that the affirmative reported univariable/proportion methods do not identify. Remaining question: Which competitors, live-discharge rule, adjustment covariates and tests produced the reported IMV/infection numbers, and which supplied results or plan changes map the planned analyses to them?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: Key-secondary IMV HR .85 (.68–1.06), P=.17 and infection HR 1.01 (.96–1.06), P=.91, and their competitor/adjustment/test definitions. The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c007"></a>

## C007 — IMV cumulative-incidence P value assigned two test names

**Pending Human Adjudication.**

**Candidate statement:** The article and supplementary cumulative-incidence figure assign the same IMV P=.17 comparison to Gray and log-rank tests without identifying separate analyses.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main pp.3/4/5/6 vs REPORT results supplement p.3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003

**Qualifying route:** Route B

**Classification rationale:** Main methods/results and the supplied graph are REPORT by content. Primary S_C; all relationships S_C; domain statistical_results. Any plan confirmation of Gray's test only corroborates one side and creates no P_R relationship.

**Classification ambiguity:** Possible distinct supplementary analysis, not role ambiguity.

**Exact source locations:** [jama_azoulay_2018_oi_180109.pdf — Main page 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>), competitor definition; [jama_azoulay_2018_oi_180109.pdf — page 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), Gray method; [jama_azoulay_2018_oi_180109.pdf — page 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), Table 2 IMV P; [jama_azoulay_2018_oi_180109.pdf — page 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>), cumulative-incidence statement/eFigure pointer; [joi180109supp2_prod.pdf — results supplement page 3](<../joi180109supp2_prod.pdf#page=3>), eFigure 1 title and P label. All were found; the current-source graph label was also read visually.

**Source evidence:** Main article states that IMV cumulative incidence is compared using Gray's test and prints P=.17 for IMV.

**Reported-versus-comparator:** The pointed-to cumulative-incidence figure explicitly labels P (log Rank test)=0.17, without identifying it as a separate supplementary analysis.

**Reasoning procedure:** Route B, focus C: two distinct named statistical procedures are attributed to the same key-secondary comparison without an analysis mapping. Directly observed: test labels differ for the mapped display. Inferred: supplementary analysis or abbreviated label; neither is established.

**Calculation:** Gray and log-rank are separate procedure labels. Both printed P copies have interval [.165,.175], gap 0; their equal rounded values do not establish equal methods. This does not assert an interval/P conflict or reconstruct an unknown fitted variance.

**Affected result or extracted value:** Test identity and competing-event/risk-set interpretation of the key-secondary IMV cumulative-incidence P=.17.

**Why context does not resolve it:** B1: statistical procedure identity is in focus. B2: Gray and log-rank are distinct named tests, with no separate-analysis attribution in the mapped figure. B3: the extracted test identity and competing-event interpretation of IMV P=.17 remain unresolved.

**Alternative source-grounded interpretations:** The figure may show an additional log-rank comparison, or its label may refer to the main Gray comparison without specifying that distinction.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. Main procedure statement, shared endpoint/time/figure mapping and figure label suffice. Exact missing inputs/definitions: The actual procedure, risk-set/competitor handling and whether a second analysis was performed are unavailable. reproduced. Determining recheck fact: The directly rendered figure preserves the log-rank label while the article's cumulative-incidence method states Gray. Remaining question: Which test and competing-event/risk-set rules generated the plotted IMV P=.17, and does it represent the main Gray comparison or a separate log-rank analysis?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: Test identity and competing-event/risk-set interpretation of the key-secondary IMV cumulative-incidence P=.17. The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c008"></a>

## C008 — Four Table 1 count/percentage pairs do not reconcile

**Pending Human Adjudication.**

**Candidate statement:** Four Table 1 count/percentage pairs do not reconcile with the displayed arm denominator of 388 after half-unit rounding allowances.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main p.4 Table 1 cells vs REPORT main p.4 arm denominators

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Qualifying route:** Route A, category 3

**Classification rationale:** Every compared location is REPORT within the same baseline table. Primary S_W; all relationships S_W; domain statistical_results.

**Classification ambiguity:** None for roles or relationship; unknown row denominators remain the substantive question.

**Exact source locations:** [jama_azoulay_2018_oi_180109.pdf — Main page 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), Table 1 both n=388 column headers, H chronic liver cell, C chronic kidney cell, both postextubation cells, and all table footnotes. All four affected cells and denominator context were found directly and read in the current-source render.

- [jama_azoulay_2018_oi_180109.pdf — p.4, Table 1 high-flow chronic liver 45 (13.3%)](<../jama_azoulay_2018_oi_180109.pdf#page=4>)
- [jama_azoulay_2018_oi_180109.pdf — p.4, Table 1 control chronic kidney 69 (20.4%)](<../jama_azoulay_2018_oi_180109.pdf#page=4>)
- [jama_azoulay_2018_oi_180109.pdf — p.4, Table 1 high-flow postextubation 14 (4.1%)](<../jama_azoulay_2018_oi_180109.pdf#page=4>)
- [jama_azoulay_2018_oi_180109.pdf — p.4, Table 1 control postextubation 18 (5.3%)](<../jama_azoulay_2018_oi_180109.pdf#page=4>)

**Source evidence:** H liver 45 (13.3%); C kidney 69 (20.4%); postextubation H 14 (4.1%) and C 18 (5.3%).

**Reported-versus-comparator:** Both arm headers say n=388. Neither cells nor footnotes provide an alternate denominator for these rows. Other rows explicitly provide denominators such as 221/294 and 26/167, so the source distinguishes those exceptions.

**Reasoning procedure:** Route A, category 3, focus A: numerator, printed denominator and percentage within one table do not reconcile above the display rule. Baseline location does not remove a within-display count comparison. Directly observed: four count/percentage pairs do not reconcile under the displayed denominator after half-unit precision. Inferred: alternate denominator usage or transcription mechanism; neither is established.

**Calculation:** For percentage use [100(n−.5)/(388+.5),100(n+.5)/(388−.5)].

| Affected cell | Recomputed percentage interval | Printed percentage interval | Gap | Relative gap |
|---|---:|---:|---:|---:|
| H liver 45 (13.3) | [11.454311,11.741935] | [13.25,13.35] | 1.508065 | .113388 |
| C kidney 69 (20.4) | [17.631918,17.935484] | [20.35,20.45] | 2.414516 | .118359 |
| H postextubation 14 (4.1) | [3.474903,3.741935] | [4.05,4.15] | .308065 | .075138 |
| C postextubation 18 (5.3) | [4.504505,4.774194] | [5.25,5.35] | .475806 | .089775 |

**Affected result or extracted value:** High-flow chronic-liver prevalence 45 (13.3%), control chronic-kidney prevalence 69 (20.4%), and postextubation proportions 14 (4.1%)/18 (5.3%).

**Why context does not resolve it:** Route A, category 3 is an always-register category. The reproduced within-display count/denominator/percentage inconsistency remains eligible even when an explanatory alternative is available; the specific alternative and missing definition are retained below.

**Alternative source-grounded interpretations:** Smaller available-case denominators could account for the percentages, but are not identified for these rows.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. Each printed count, percentage and n=388 denominator suffice; all four relative gaps exceed .05. Exact missing inputs/definitions: Any row-specific available-case denominator or distinct population for each cell is unavailable. reproduced. Determining recheck fact: All four numbers and the n=388 headers match the current PDF, and each independently repeated interval gap exceeds 5%. Remaining question: Which count/percentage pair and row-specific denominator apply to each of the four Table 1 cells?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: High-flow chronic-liver prevalence 45 (13.3%), control chronic-kidney prevalence 69 (20.4%), and postextubation proportions 14 (4.1%)/18 (5.3%). The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c009"></a>

## C009 — Planned joint longitudinal analyses are not identified

**Pending Human Adjudication.**

**Candidate statement:** Final-plan joint longitudinal models for oxygenation, comfort and dyspnea accounting for right censoring have no identified supplied results.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN pp.55/82/105 vs REPORT main pp.1/4/6 and REPORT results supplement pp.4/5

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-007

**Qualifying route:** Route A, category 5

**Classification rationale:** Prospective statistical strategy is PLAN; article and result series are REPORT. Primary P_R; all relationships P_R; domain protocol_report. Repeated earlier/final plan statements are corroboration rather than P_P.

**Classification ambiguity:** Model/result mapping is unknown; roles are clear.

**Exact source locations:** PLAN [joi180109supp1_prod.pdf — page 55](<../joi180109supp1_prod.pdf#page=55>), 825–826; [joi180109supp1_prod.pdf — page 82](<../joi180109supp1_prod.pdf#page=82>), 1314–1315; [joi180109supp1_prod.pdf — page 105](<../joi180109supp1_prod.pdf#page=105>), 1745–1747. REPORT [jama_azoulay_2018_oi_180109.pdf — main page 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>), key-secondary abstract results; [jama_azoulay_2018_oi_180109.pdf — page 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), Wilcoxon symptom methods; [jama_azoulay_2018_oi_180109.pdf — page 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>), oxygenation/comfort/dyspnea results; [joi180109supp2_prod.pdf — results supplement page 4](<../joi180109supp2_prod.pdf#page=4>), eFigure 2; [joi180109supp2_prod.pdf — page 5](<../joi180109supp2_prod.pdf#page=5>), eFigure 3. All locations were found.

**Source evidence:** Final plan states that longitudinal oxygenation, dyspnea and patient comfort analyses will use joint models accounting for right censoring, matching the earlier copies.

**Reported-versus-comparator:** Article specifies Wilcoxon rank-sum symptom comparisons, oxygenation difference 19.5 (4.4–34.6), and no comfort/dyspnea difference at any time. The supplement displays time-specific series. Complete supplied results identify no joint-model output for any of these three outcomes.

**Reasoning procedure:** Route A, category 5, focus D: explicit planned analyses of abstract-reported key-secondary outcomes have no identified supplied counterpart. Directly observed: joint models are positively planned, yet no report output identifies one. Inferred: unlabeled implementation or replacement; neither is established.

**Calculation:** None of the named time-specific tests, series or oxygenation contrast is identified as the planned joint model. No figure point/dispersion convention is inferred. Precision is inapplicable to model identity; identical numeric contrasts would not identify a censoring model by themselves.

**Affected result or extracted value:** Analysis basis of oxygenation difference 19.5 (4.4–34.6) and the reported time-specific comfort/dyspnea comparisons.

**Why context does not resolve it:** Route A, category 5 is an always-register category. The reproduced planned-versus-reported outcome/analysis mapping remains eligible even when an explanatory alternative is available; the specific alternative and missing definition are retained below.

**Alternative source-grounded interpretations:** A joint model might underlie an unlabeled contrast, or time-specific tests might replace it without a supplied mapping.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. Positive final-plan model requirement and complete supplied reported methods/results suffice for a bounded mapping check. Exact missing inputs/definitions: Joint-model formulas, outcome/time/survival submodels, right-censoring linkage, estimates/results, or replacement specification are unavailable. reproduced. Determining recheck fact: Current final-plan lines 1745–1747 retain the joint-model commitment and complete supplied report output does not identify its results. Remaining question: Which reported result identifies each planned oxygenation, dyspnea and comfort joint model, or its documented replacement?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: Analysis basis of oxygenation difference 19.5 (4.4–34.6) and the reported time-specific comfort/dyspnea comparisons. The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c010"></a>

## C010 — Planned ICU-stay estimators and populations are not identified

**Pending Human Adjudication.**

**Candidate statement:** Final-plan overall and separate survivor/decedent ICU-stay analyses with survival/competing-risk estimators have no identified counterparts alongside the pooled Wilcoxon result.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN pp.54/82/105 vs REPORT main pp.1/4/5/6

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-008

**Qualifying route:** Route A, category 5

**Classification rationale:** Prospective estimator/population statements are PLAN; abstract/methods/Table 2/results are REPORT. Primary P_R; all relationships P_R; domain protocol_report. No P_P conflict is inferred from plan wording.

**Classification ambiguity:** Estimator allocation is itself unclear, but does not change roles.

**Exact source locations:** PLAN [joi180109supp1_prod.pdf — page 54](<../joi180109supp1_prod.pdf#page=54>), 822–824; [joi180109supp1_prod.pdf — page 82](<../joi180109supp1_prod.pdf#page=82>), 1311–1313; [joi180109supp1_prod.pdf — page 105](<../joi180109supp1_prod.pdf#page=105>), 1742–1745. REPORT [jama_azoulay_2018_oi_180109.pdf — main page 1](<../jama_azoulay_2018_oi_180109.pdf#page=1>), abstract ICU stay; [jama_azoulay_2018_oi_180109.pdf — page 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), Wilcoxon method; [jama_azoulay_2018_oi_180109.pdf — page 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), Table 2 ICU stay/footnote e; [jama_azoulay_2018_oi_180109.pdf — page 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>), Secondary Outcomes. All were found; Table 2 was visually read.

**Source evidence:** Final plan requires ICU stay analyzed overall and separately in survivors/deceased using Kaplan–Meier and competing-risk estimators, matching earlier copies.

**Reported-versus-comparator:** Report supplies pooled medians 8 (4–14) and 6 (4–13), mean difference .6 (−1.0,2.2), P=.07, Wilcoxon method and the footnote that stay effects cannot be expressed by HRs. No supplied result identifies separate survivor/decedent analyses or the planned estimators.

**Reasoning procedure:** Route A, category 5, focus D: planned analyses for an abstract-reported key-secondary outcome are absent or replaced without an identified mapping. Directly observed: affirmative planned estimators/populations do not have supplied identified report counterparts. Inferred: analysis replacement or unpublished outputs; no execution history is established.

**Calculation:** A pooled Wilcoxon comparison and mean-difference result do not identify the planned survival estimators or separate populations. Mean difference is not forced to equal the median difference. Precision is inapplicable to population/estimator identity; numerical rounding cannot identify absent analyses.

**Affected result or extracted value:** ICU-stay medians 8 (4–14)/6 (4–13), mean difference .6 (−1.0 to 2.2), P=.07 and their estimator/population interpretation.

**Why context does not resolve it:** Route A, category 5 is an always-register category. The reproduced planned-versus-reported outcome/analysis mapping remains eligible even when an explanatory alternative is available; the specific alternative and missing definition are retained below.

**Alternative source-grounded interpretations:** The plan's former/latter wording is ambiguous about estimator allocation; rank tests could replace or supplement the planned analyses, which might have been performed outside this report.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. The explicit plan commitment and reported test/population summary suffice. Exact missing inputs/definitions: Assignment of the plan's former/latter estimators, survival-event/competing-event definitions, survivor/decedent analysis populations, outputs and replacement rationale are unavailable. reproduced. Determining recheck fact: The final plan retains overall and survivor/decedent analyses, while supplied report identifies only pooled results and Wilcoxon. Remaining question: Where are the planned overall and survivor/decedent ICU-stay analyses, what estimator applies to each, or which documented replacement produced the supplied pooled result?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: ICU-stay medians 8 (4–14)/6 (4–13), mean difference .6 (−1.0 to 2.2), P=.07 and their estimator/population interpretation. The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c011"></a>

## C011 — Initially secondary intubated mortality receives post hoc status

**Pending Human Adjudication.**

**Candidate statement:** An earlier planned secondary intubated-mortality analysis is reported as post hoc, with the disclosed superiority redesign and its omission from the final list retained as explanatory context.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN pp.6/7/38/45/47/103 vs REPORT main pp.3/4/6/8

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-010

**Qualifying route:** Route A, category 5

**Classification rationale:** All prospective versions/summaries are PLAN, including the earlier summary in another language; report methods/results/disclosure are REPORT. Primary P_R; all relationships P_R; domain protocol_report. No P_P is registered: version evolution itself is not framed as a plan-internal contradiction.

**Classification ambiguity:** Disclosed redesign is a substantial explanatory alternative and the candidate's prespecification history remains unresolved.

**Exact source locations:** PLAN [joi180109supp1_prod.pdf — page 6](<../joi180109supp1_prod.pdf#page=6>), 97–100; [joi180109supp1_prod.pdf — page 7](<../joi180109supp1_prod.pdf#page=7>), 142–146; [joi180109supp1_prod.pdf — page 38](<../joi180109supp1_prod.pdf#page=38>), 557–558; [joi180109supp1_prod.pdf — page 45](<../joi180109supp1_prod.pdf#page=45>), 675–676; [joi180109supp1_prod.pdf — page 47](<../joi180109supp1_prod.pdf#page=47>), 699–700; [joi180109supp1_prod.pdf — page 103](<../joi180109supp1_prod.pdf#page=103>), final secondary list. REPORT [jama_azoulay_2018_oi_180109.pdf — main page 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>), disclosed redesign; [jama_azoulay_2018_oi_180109.pdf — page 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), post hoc subset methods; [jama_azoulay_2018_oi_180109.pdf — page 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>), Post Hoc Outcomes; [jama_azoulay_2018_oi_180109.pdf — page 8](<../jama_azoulay_2018_oi_180109.pdf#page=8>), secondary exploratory caution. Each location was found; page 7's summary content was read and is described here in English.

**Source evidence:** Early summaries and endpoint lists identify mortality after HFNO failure/intubation as secondary; page 45 explicitly prespecifies day-28 mortality in patients intubated in the two groups. The final secondary list omits intubated mortality.

**Reported-versus-comparator:** Report methods call subset analyses in intubated patients post hoc; results under Post Hoc Outcomes print mortality 55.3% versus 52.3%, difference +3% (−8.5,14.5), P=.65.

**Reasoning procedure:** Route A, category 5, focus D: the supplied material demonstrates a changed outcome/analysis status. The article's general exploratory caution about multiplicity is not treated as an additional status discrepancy. Directly observed: early prospective secondary analysis, final omission, disclosed overall redesign and reported post hoc status. Inferred: this particular outcome was removed during that redesign and later reintroduced; the supplied materials do not establish the complete individual-outcome chronology.

**Calculation:** Earlier positive secondary/prespecified labels differ from the reported post hoc label. The final-list omission and disclosed redesign are retained as context; the comparison is not a claim that the overall redesign was undisclosed. The reported difference arithmetic is compatible: percentage input ranges [55.25,55.35] and [52.25,52.35] give [2.90,3.10] points, overlapping integer +3 interval [2.5,3.5]. Precision does not apply to status.

**Affected result or extracted value:** Prespecification status of intubated-subset mortality 55.3%/52.3%, RD +3% (−8.5 to 14.5), P=.65.

**Why context does not resolve it:** Route A, category 5 is an always-register category. The reproduced planned-versus-reported outcome/analysis mapping remains eligible even when an explanatory alternative is available; the specific alternative and missing definition are retained below.

**Alternative source-grounded interpretations:** Main page 3 expressly says the grant proposal was noninferiority with a 9% margin and different secondary endpoints; the grant jury requested a superiority trial before the revised institutional-review-board protocol. Together with omission from the final list, this could explain removal during redesign and later post hoc analysis.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. Earlier positive specification, final endpoint list, reported post hoc label and redesign disclosure suffice. Exact missing inputs/definitions: The dated amendment/status history specifically removing or retaining intubated mortality, and whether it was subsequently reintroduced, are unavailable. reproduced. Determining recheck fact: The earlier plan explicitly names this secondary intubated-mortality analysis and the article explicitly labels the corresponding subset analysis post hoc; the final omission and redesign disclosure remain in the evidence record. Remaining question: Was the reported intubated-mortality contrast retained from the earlier secondary analysis, or removed during redesign and later reintroduced as post hoc, and what dated specification records that history?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: Prespecification status of intubated-subset mortality 55.3%/52.3%, RD +3% (−8.5 to 14.5), P=.65. The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c012"></a>

## C012 — Figure 3 hazard-ratio direction and favors headings

**Pending Human Adjudication.**

**Candidate statement:** The all-patient IMV HR is 0.85 in Table 2 and 1.17 in Figure 3 with unchanged favors headings; the common figure contrast definition affects the reading of all 26 forest rows.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main pp.4/5/6 vs REPORT main p.7 Figure 3A/B

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-004

**Qualifying route:** Route A, category 2

**Classification rationale:** All locations are REPORT in the same article. Primary S_W; all relationships S_W; domain statistical_results.

**Classification ambiguity:** Figure contrast/model ambiguity, not role ambiguity.

**Exact source locations:** [jama_azoulay_2018_oi_180109.pdf — Main page 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), high-flow versus standard Cox treatment-effect statement; [jama_azoulay_2018_oi_180109.pdf — page 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), mortality/IMV Table 2 rows; [jama_azoulay_2018_oi_180109.pdf — page 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>), IMV narrative; [jama_azoulay_2018_oi_180109.pdf — page 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>), every HR row of both Figure 3 panels, favors headings, axes and caption. Current-source visual rendering confirmed the printed positions and all 26 rows, enumerated below.

Each of the 26 affected forest rows has its own locator; the shared headings, axes and caption apply to both panels.

- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — ICU time 0–1](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — ICU time ≥2](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — PaO2:FIO2 <200](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — PaO2:FIO2 ≥200](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — Oxygen flow ≤9](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — Oxygen flow >9](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — Catecholamines No](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — Catecholamines Yes](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — Unknown diagnosis No](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — Unknown diagnosis Yes](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — Hematologic malignancy No](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — Hematologic malignancy Yes](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — All patients](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — ICU time 0–1](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — ICU time ≥2](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — PaO2:FIO2 <200](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — PaO2:FIO2 ≥200](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — Oxygen flow ≤9](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — Oxygen flow >9](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — Catecholamines No](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — Catecholamines Yes](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — Unknown diagnosis No](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — Unknown diagnosis Yes](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — Hematologic malignancy No](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — Hematologic malignancy Yes](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — All patients](<../jama_azoulay_2018_oi_180109.pdf#page=7>)

**Source evidence:** Table 2 and narrative give H 150/388 versus C 170/388 and IMV cause-specific HR .85 (.68–1.06). Method defines high-flow versus standard treatment effects. Mortality Table 2 gives .98 (.77–1.24).

**Reported-versus-comparator:** Figure 3B gives identical all-patient counts with HR 1.17 (.94–1.46); A gives 1.02 (.81–1.29). Both panels place favors high-flow below 1 and favors standard above 1. All affected printed HR rows are retained:

| Figure 3 row, main page 7 | Panel A mortality HR (95% CI) | Panel B IMV HR (95% CI) |
|---|---|---|
| ICU time 0–1 | .95 (.74–1.22) | 1.1 (.87–1.40) |
| ICU time ≥2 | 1.55 (.83–2.90) | 1.69 (.96–2.95) |
| PaO2:FIO2 <200 | .89 (.68–1.19) | 1.17 (.90–1.53) |
| PaO2:FIO2 ≥200 | 1.18 (.54–2.60) | .88 (.46–1.71) |
| Oxygen flow ≤9 | 1.06 (.83–1.36) | 1.15 (.91–1.45) |
| Oxygen flow >9 | .76 (.36–1.57) | 1.37 (.68–2.72) |
| Catecholamines No | 1.08 (.84–1.39) | 1.18 (.94–1.49) |
| Catecholamines Yes | .62 (.31–1.26) | 1.09 (.52–2.26) |
| Unknown diagnosis No | .93 (.70–1.23) | 1.18 (.92–1.52) |
| Unknown diagnosis Yes | 1.39 (.90–2.13) | 1.15 (.72–1.82) |
| Hematologic malignancy No | 1.11 (.79–1.55) | 1.61 (1.16–2.23) |
| Hematologic malignancy Yes | .94 (.67–1.33) | .89 (.65–1.22) |
| All patients | 1.02 (.81–1.29) | 1.17 (.94–1.46) |

**Reasoning procedure:** Route A, category 2, focus B/C: the overall IMV quantity/reference-direction reading differs substantially within one report. The shared figure reference definition affects all 26 rows; subgroup estimates are not individually forced to equal crude ratios. Directly observed: all-patient HR copies differ beyond precision and direction relative to 1; headings retain the low-HR favors-high-flow reading. Inferred: reversed contrast throughout the figure. No independent reversal of every subgroup HR is established solely from counts.

**Calculation:** Table/figure point intervals [.845,.855] versus [1.165,1.175] yield gap .310/.85=.364706. Lower-limit intervals [.675,.685] versus [.935,.945] yield gap .250/.68=.367647; upper intervals [1.055,1.065] versus [1.455,1.465] yield gap .390/1.06=.367925. The diagnostic reciprocal point interval [1/.855,1/.845]=[1.169591,1.183432] overlaps the forest point; reciprocal CI endpoint intervals [1/1.065,1/1.055]=[.938967,.947867] and [1/.685,1/.675]=[1.459854,1.481481] overlap the forest endpoints. Mortality's point-copy gap is .030/.98=.030612, below .05, so it is corroborative rather than a separate numeric discrepancy.

**Affected result or extracted value:** All-patient IMV effect direction and reference group: .85 (.68–1.06) versus 1.17 (.94–1.46); common reference interpretation for all 26 Figure 3 rows.

**Why context does not resolve it:** Route A, category 2 is an always-register category. The reproduced quantity/reference-direction reading remains eligible even when an explanatory alternative is available; the specific alternative and missing definition are retained below.

**Alternative source-grounded interpretations:** The forest may intentionally show standard/high-flow or another model; the reciprocal diagnostic supports that possibility but the unchanged favors headings require a defined contrast.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. Matched all-patient counts, explicit treatment contrast, HRs/CIs and displayed favors labels suffice. Exact missing inputs/definitions: Figure numerator/reference treatment, model/competitor definitions and any explanation for reversing the contrast are unavailable. Raw subgroup event times and covariances are unavailable and are not needed to observe the overall copy conflict. reproduced. Determining recheck fact: Direct table and forest show .85 versus 1.17 for the same all-patient IMV counts, and interval arithmetic exceeds 5% for the point and both endpoints. Remaining question: What numerator/reference treatment and event model apply to both forest panels and their favors labels, and which direction should be extracted for all-patient IMV?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: All-patient IMV effect direction and reference group: .85 (.68–1.06) versus 1.17 (.94–1.46); common reference interpretation for all 26 Figure 3 rows. The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c013"></a>

## C013 — Infection HR interval differs from a same-display reproducing construction

**Pending Human Adjudication.**

**Candidate statement:** The infection HR interval does not reproduce under a diagnostic event-count interval construction that reproduces the other two HR rows of the same table, beyond display precision.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main p.5 infection HR row vs REPORT main p.5 mortality/IMV HR rows; REPORT main p.4 methods

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-011

**Qualifying route:** Route A, category 4

**Classification rationale:** Methods and all compared HR rows are REPORT in one article. Primary S_W; all relationships S_W; domain statistical_results.

**Classification ambiguity:** Actual interval construction is missing; it does not change document roles or the same-display comparison.

**Exact source locations:** [jama_azoulay_2018_oi_180109.pdf — Main page 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), infection-proportion chi-square comparison; [jama_azoulay_2018_oi_180109.pdf — main page 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), Table 2 all three HR rows, n=388 headers and cause-specific-HR footnote d. All were found and Table 2 was read in a current-source render.

**Source evidence:** Infection events H 39/C 41; HR 1.01 (.96–1.06), P=.91 and cause-specific-HR footnote. Report methods associate infection-proportion comparison with chi-square.

**Reported-versus-comparator:** Same display mortality events 138/140, HR .98 (.77–1.24); IMV events 150/170, HR .85 (.68–1.06). Confidence level is 95%.

**Reasoning procedure:** Route A, category 4, focus B/C: a same-display construction reproducing other HR interval rows does not reproduce the printed infection endpoints beyond 5%. It is a diagnostic construction, not a fitted Cox refit, preferred analysis, or proposed replacement interval. Infection P and its HR CI are not assumed to arise from the same test. Directly observed: the printed counts/HRs/CIs and the reproducible difference under the construction supported by other display rows. Inferred: a distinct method or precision basis explains the infection interval. No raw-data analysis was performed or claimed.

**Calculation:** Diagnostic limits are h exp[±1.95996 sqrt(1/eH+1/eC)]. Mortality central limits [.774676,1.239744] and IMV [.682442,1.058699] overlap their respective printed half-unit endpoint intervals. Allowing events ±.5 and HR ±.005 gives mortality lower [.770397,.778957], upper [1.232898,1.246597], and IMV lower [.678192,.686693], upper [1.052108,1.065295]; all overlap corresponding printed intervals. Infection central limits are [.651520,1.565723]. Its lower recomputed interval [.646502,.656527] versus printed [.955,.965] leaves .298473/.96=.310909; upper [1.553743,1.577838] versus printed [1.055,1.065] leaves .488743/1.06=.461079.

**Affected result or extracted value:** Infection HR 1.01 with reported 95% CI .96–1.06, especially the interval precision a data extractor may take.

**Why context does not resolve it:** Route A, category 4 is an always-register category. The reproduced same-display supported-method discrepancy remains eligible even when an explanatory alternative is available; the specific alternative and missing definition are retained below.

**Alternative source-grounded interpretations:** The infection row may use a different analysis unit, event definition, model variance or interval construction from the other HR rows.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. Printed HRs, confidence level and event counts suffice for this supported same-display diagnostic. Exact missing inputs/definitions: The actual fitted infection event definition/unit, Cox variance/covariance, CI construction, risk sets and event times are unavailable; the diagnostic cannot determine the fitted interval. reproduced. Determining recheck fact: The direct PDF infection endpoints .96/1.06 match registration, and independently repeated same-display interval arithmetic yields endpoint gaps .310909 and .461079 relative to the printed endpoints. Remaining question: What supplied analysis definition, variance and CI construction account for the infection HR interval relative to the construction reproducing the other Table 2 HR rows?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: Infection HR 1.01 with reported 95% CI .96–1.06, especially the interval precision a data extractor may take. The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c014"></a>

## C014 — Therapy counts use pooled percentages but arm-specific attribution

**Pending Human Adjudication.**

**Candidate statement:** Arm-attributed therapy counts and percentages in one paragraph reproduce with the pooled denominator, while they do not reconcile with either reported arm denominator.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main p.6 therapy paragraph vs REPORT main pp.3/5 arm and pooled denominators

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-002

**Qualifying route:** Route A, category 3

**Classification rationale:** Paragraph and denominator displays are REPORT in one article. Primary S_W; all relationships S_W; domain statistical_results.

**Classification ambiguity:** Therapy/population mapping is unresolved; roles are clear.

**Exact source locations:** [jama_azoulay_2018_oi_180109.pdf — Main page 6](<../jama_azoulay_2018_oi_180109.pdf#page=6>), first Post Hoc Outcomes paragraph; [jama_azoulay_2018_oi_180109.pdf — main page 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>), Figure 1 randomized/analyzed totals; [jama_azoulay_2018_oi_180109.pdf — main page 5](<../jama_azoulay_2018_oi_180109.pdf#page=5>), Patients. All were found directly.

**Source evidence:** Paragraph starts with the overall population, then states vasopressors and renal replacement were needed in 153 (19.7%) randomized to high-flow and 31 (4%) randomized to standard, with no statistical difference.

**Reported-versus-comparator:** Analyzed arms are 388 each, pooled 776; randomized arms are 389 each. The paragraph attaches the printed counts to separate arms despite the overall-population introduction.

**Reasoning procedure:** Route A, category 3, focus A: the arm-attributed count/percentage/denominator reading in one paragraph does not reconcile. Recovering a pooled denominator does not identify which therapies/populations those counts describe. Directly observed: printed percentages reproduce with pooled n=776 but not arm n=388 or 389. Inferred: pooled-therapy attribution or denominator usage. No reconstructed therapy cross-tabulation or test is claimed.

**Calculation:** 153/388=39.432990%; interval [39.253539,39.612903]% versus [19.65,19.75]% yields gap 19.503539/19.7=.990027. 31/388=7.989691%; interval [7.850708,8.129032]% versus integer 4% interval [3.5,4.5]% yields gap 3.350708/4=.837677. Using randomized denominator 389 instead yields [39.152760,39.510940]% and [7.830552,8.108108]%, still above 5%. Pooled 153/776=19.716495%, interval [19.639408,19.793681]%, and 31/776=3.994845%, interval [3.927882,4.061896]%, overlap the respective printed percentages, gaps 0.

**Affected result or extracted value:** Therapy-specific numerators 153/31, percentages 19.7%/4%, their treatment attribution and applicable arm or pooled denominators.

**Why context does not resolve it:** Route A, category 3 is an always-register category. The reproduced within-display count/denominator/percentage inconsistency remains eligible even when an explanatory alternative is available; the specific alternative and missing definition are retained below.

**Alternative source-grounded interpretations:** The two counts may denote pooled counts for separate therapies with arm language attached, or actual arm counts with pooled percentages. The paragraph does not select between these readings.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. Counts, percentages, arm attribution and analyzed/randomized totals suffice. Exact missing inputs/definitions: Therapy-specific counts by arm, whether 153/31 are pooled counts for two therapies, actual denominators and the test/cross-tabulation behind the no-difference statement are unavailable. reproduced. Determining recheck fact: Direct paragraph arm attribution and independently repeated percentage intervals remain incompatible under both arm denominators. Remaining question: Do 153 and 31 describe pooled vasopressor/renal-replacement counts or separate arm counts, and what arm-by-therapy numerators and denominators apply?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: Therapy-specific numerators 153/31, percentages 19.7%/4%, their treatment attribution and applicable arm or pooled denominators. The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c015"></a>

## C015 — Figure 3 subgroup population accounting is not supplied

**Pending Human Adjudication.**

**Candidate statement:** Smaller primary-mortality and IMV subgroup populations have no supplied mapping to available-covariate or restricted populations alongside the broad no-exclusion analysis statement.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main p.7 subgroup populations vs REPORT main p.7 All patients and REPORT main pp.3/4 population context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-003

**Qualifying route:** Route B

**Classification rationale:** Every compared location is REPORT in the same article. Primary S_W; all relationships S_W; domain statistical_results because the issue concerns analysis populations/counts/method mapping.

**Classification ambiguity:** Whether the subgroup analysis is available-covariate or full-set is the substantive ambiguity; roles and relationship are clear.

**Exact source locations:** [jama_azoulay_2018_oi_180109.pdf — Main page 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>), both panels' PaO2:FIO2, hematologic-malignancy and All patients rows and caption; [jama_azoulay_2018_oi_180109.pdf — main page 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), Table 1 malignancy/oxygenation context; [jama_azoulay_2018_oi_180109.pdf — main page 3](<../jama_azoulay_2018_oi_180109.pdf#page=3>), no missing/incomplete-data exclusion statement. Every cited row was found in direct extraction and the page 7 render.

- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — PaO2:FIO2 <200](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — PaO2:FIO2 ≥200](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — Hematologic malignancy No](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — Hematologic malignancy Yes](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — All patients](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — PaO2:FIO2 <200](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — PaO2:FIO2 ≥200](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — Hematologic malignancy No](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — Hematologic malignancy Yes](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — All patients](<../jama_azoulay_2018_oi_180109.pdf#page=7>)

**Source evidence:** All patients H/C n=388/388, mortality 138/140 and IMV 150/170. PaO2 low/high H/C n=237+65 and 251+35; deaths 99+16 and 95+10; IMV 99+27 and 117+13. Hematologic No/Yes n H 199+167 and C 198+181; deaths H 66+64 and C 72+65; IMV H 61+78 and C 89+77.

**Reported-versus-comparator:** Table 1 baseline hematologic malignancy is H 167/C 181 among 388 each, matching the Figure 3 Yes rows. Article positively states that no participants were excluded from analyses because of missing/incomplete data. Figure 3 identifies no missing-covariate group, availability restriction or subgroup-specific analysis population.

**Reasoning procedure:** Route B, focus A/C: observed smaller primary-mortality/IMV subgroup populations and broad affirmative no-exclusion statement leave the applicable subgroup population/handling unclear. This is not an assertion that every binary covariate must be completely observed or that every row must partition the full cohort. Directly observed: the tabulated sums are smaller, several differences exceed display precision, and the subgroup population/rule is not defined alongside the broad no-exclusion statement. Inferred: missing covariates, restricted definitions or exclusion from individual subgroup analyses. No complete-population arithmetic obligation is established without the missing definition.

**Calculation:** Two displayed counts give each sum an interval sum±1; full totals have interval total±.5. Complete affected comparisons are:

| Subgroup partition/arm | n sum versus full | Mortality sum versus full | IMV sum versus full |
|---|---|---|---|
| PaO2 H | 302 vs 388; intervals [301,303]/[387.5,388.5]; gap 84.5/388=.217784 | 115 vs 138; [114,116]/[137.5,138.5]; gap 21.5/138=.155797 | 126 vs 150; [125,127]/[149.5,150.5]; gap 22.5/150=.150000 |
| PaO2 C | 286 vs 388; [285,287]/[387.5,388.5]; gap 100.5/388=.259021 | 105 vs 140; [104,106]/[139.5,140.5]; gap 33.5/140=.239286 | 130 vs 170; [129,131]/[169.5,170.5]; gap 38.5/170=.226471 |
| Hematologic H | 366 vs 388; [365,367]/[387.5,388.5]; gap 20.5/388=.052835 | 130 vs 138; [129,131]/[137.5,138.5]; gap 6.5/138=.047101 | 139 vs 150; [138,140]/[149.5,150.5]; gap 9.5/150=.063333 |
| Hematologic C | 379 vs 388; [378,380]/[387.5,388.5]; gap 7.5/388=.019330 | 137 vs 140; [136,138]/[139.5,140.5]; gap 1.5/140=.010714 | 166 vs 170; [165,167]/[169.5,170.5]; gap 2.5/170=.014706 |

**Affected result or extracted value:** Population and covariate-handling interpretation of PaO2:FIO2 and hematologic-malignancy mortality/IMV subgroup HRs and interactions.

**Why context does not resolve it:** B1: these are primary-mortality/IMV analysis populations, not peripheral time-point contributor counts. B2: no available-covariate or restricted-population rule maps the smaller sets to the affirmative no-exclusion statement. B3: the applicable population and covariate handling of the subgroup HRs and interactions cannot be identified from immediate context. No exhaustive binary partition is assumed.

**Alternative source-grounded interpretations:** Available-covariate populations or a restricted hematologic definition may explain these sums; the ITT/no-exclusion sentence may describe only the full analysis set. This alternative is retained and complete binary partitions are not assumed.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. Counts, matched full totals, caption and no-exclusion statement suffice to reproduce population-size differences and the absent subgroup-specific mapping. H hematologic deaths and all C hematologic deficits stay within 5% and are not independently asserted as numeric discrepancies. Exact missing inputs/definitions: Covariate completeness, subgroup eligibility/restriction definitions, missing-covariate handling, and whether the broad no-exclusion statement applies to each subgroup are unavailable. reproduced. Determining recheck fact: Direct PDF counts reproduce the specified smaller populations and no subgroup restriction maps them to the affirmative analysis statement. This state records the printed accounting/mapping issue; it does not infer exhaustive subgroup partitions. Remaining question: Which populations and covariate-handling rules govern these primary-mortality and IMV subgroup rows, and how do they map to the article's no-exclusion statement?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: Population and covariate-handling interpretation of PaO2:FIO2 and hematologic-malignancy mortality/IMV subgroup HRs and interactions. The supplied package does not establish propagation into a synthesis or a changed conclusion.

<a id="c016"></a>

## C016 — Two analyses called predefined have no supplied prospective specification

**Pending Human Adjudication.**

**Candidate statement:** Unknown-diagnosis and hematologic-malignancy interactions are called predefined in the figure but have no named prospective specification in the supplied plan.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main pp.4/7 vs PLAN pp.45/46/53/82/98/99/104

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-014

**Qualifying route:** Route A, category 5

**Classification rationale:** Article method/title/forest results are REPORT; all prospective protocol/SAP/version passages are PLAN even though physically in a supplement. Primary P_R; all relationships P_R; domain protocol_report. No P_P is inferred from evolving subgroup lists.

**Classification ambiguity:** An unsupplied dated specification could change the mapping, not the document roles.

**Exact source locations:** REPORT [jama_azoulay_2018_oi_180109.pdf — main page 7](<../jama_azoulay_2018_oi_180109.pdf#page=7>), Figure 3 title and unknown-diagnosis/hematologic-malignancy rows in both panels; [jama_azoulay_2018_oi_180109.pdf — main page 4](<../jama_azoulay_2018_oi_180109.pdf#page=4>), subgroup methods. PLAN [joi180109supp1_prod.pdf — page 45](<../joi180109supp1_prod.pdf#page=45>), 666–677; [joi180109supp1_prod.pdf — page 46](<../joi180109supp1_prod.pdf#page=46>), 678–680; [joi180109supp1_prod.pdf — page 53](<../joi180109supp1_prod.pdf#page=53>), 784–787; [joi180109supp1_prod.pdf — page 82](<../joi180109supp1_prod.pdf#page=82>), interaction strategy; [joi180109supp1_prod.pdf — page 98](<../joi180109supp1_prod.pdf#page=98>), stratification list; [joi180109supp1_prod.pdf — page 99](<../joi180109supp1_prod.pdf#page=99>), continuation/interaction intention; [joi180109supp1_prod.pdf — page 104](<../joi180109supp1_prod.pdf#page=104>), 1721–1723 and 1735–1736. Every registered location was found directly; the figure's predefined title and both sets of rows were also read visually.

- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — Unknown diagnosis No](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — Unknown diagnosis Yes](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — Hematologic malignancy No](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3A mortality — Hematologic malignancy Yes](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — Unknown diagnosis No](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — Unknown diagnosis Yes](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — Hematologic malignancy No](<../jama_azoulay_2018_oi_180109.pdf#page=7>)
- [jama_azoulay_2018_oi_180109.pdf — p.7, Figure 3B IMV — Hematologic malignancy Yes](<../jama_azoulay_2018_oi_180109.pdf#page=7>)

**Source evidence:** Figure title positively calls the forest analyses predefined. Unknown-diagnosis interactions are P=.12 mortality and .9 IMV; hematologic interactions .5 mortality and .01 IMV. IMV hematologic No HR 1.61 (1.16–2.23), Yes .89 (.65–1.22).

**Reported-versus-comparator:** Initial plan specifies hypoxemia/other organ dysfunction and intubation, postextubation, intubated-mortality and DNI groups; final plan specifies ICU time, oxygen flow and shock strata with treatment-by-subset interactions according to those subsets. No cited prospective list specifies unknown-diagnosis or hematologic-malignancy treatment interactions.

**Reasoning procedure:** Route A, category 5, focus D: a positive prespecification claim cannot be mapped to the supplied prospective named analysis specifications. The affected interpretation is prespecification of these interactions, especially the reported hematologic IMV P=.01. Directly observed: positive predefined claim and no named mapping in the supplied plan. Inferred: another plan or mixed subgroup statuses. Neither the timing of analytic decisions nor an unprovided specification is established.

**Calculation:** Independently searched the newly extracted whole supplied plan for diagnosis/diagnostic, malignancy, hematology variants and subgroup/subset/interaction language, then read the prospective passages at the exact pages above. Other matching content is eligibility, background, prognostic or bibliographic material rather than these named prospective treatment interactions. Initial PaO2 subgroup support is present and is not counted as absent. No supplied additional specification was identified. Numeric display precision is inapplicable to prespecification status; the P values are locators/affected results, not recalculated tests.

**Affected result or extracted value:** Supplied prespecification status of diagnosis interactions .12/.9 and malignancy interactions .5/.01, including IMV malignancy No HR 1.61 (1.16–2.23) versus Yes .89 (.65–1.22).

**Why context does not resolve it:** Route A, category 5 is an always-register category. The reproduced planned-versus-reported outcome/analysis mapping remains eligible even when an explanatory alternative is available; the specific alternative and missing definition are retained below.

**Alternative source-grounded interpretations:** Another unsupplied prospective specification may contain them, or the shared predefined title may encompass both planned and added groups.

**Mechanical evidence recheck:** All cited locations were found and source/comparator readings matched the exact supplied pages. The applicable rule and calculation or logical comparison were independently reproduced; document roles and classifications were confirmed without transcription revision. Positive figure title, named rows and complete supplied prospective analysis lists suffice for this bounded mapping check. Exact missing inputs/definitions: A dated prospective specification naming these two interactions, or subgroup-specific planned/post hoc status, is unavailable. No unsupplied plan is presumed nonexistent. reproduced. Determining recheck fact: The directly rendered figure claims predefined status for both named analyses, and independent current-source plan search plus exact prospective passage reads identify no specification for them. Remaining question: Where were the unknown-diagnosis and hematologic-malignancy treatment interactions prospectively specified, or what subgroup-specific status applies to each?

**Potential downstream evidence impact:** If confirmed, this candidate could affect which result, definition or analysis attribute an evidence extractor records: Supplied prespecification status of diagnosis interactions .12/.9 and malignancy interactions .5/.01, including IMV malignancy No HR 1.61 (1.16–2.23) versus Yes .89 (.65–1.22). The supplied package does not establish propagation into a synthesis or a changed conclusion.

## Downstream Evidence-Chain Considerations

An evidence extractor may copy an effect estimate, interval, count, denominator, time window, analysis population, comparison direction, test identity or prespecification label from a report display. If a candidate is confirmed, resolving its specific reporting issue could affect one or more of those extracted fields. Repeated displays can also be copied separately unless their shared result or reference definition is recognized.

The cards identify that potential relevance for each named result. They do not establish that any value was propagated into a systematic review, meta-analysis or guideline, or that any external conclusion changed. Planned-versus-reported comparisons identify supplied specification/result mappings; P_R does not imply a protocol violation. Missing raw inputs and amendment history constrain explanations and quantitative impact estimates.

## Limitations and Missing Definitions

Complete coverage does not provide complete analytic reconstruction. Only supplied package evidence was used. Unavailable raw event times, risk sets, fitted covariances, model objects and code prevent exact refitting of named models and identification of every interval construction. C013's supported same-display calculation is diagnostic, not a substitute fitted confidence interval or a proposed model refit.

Dated prospective amendments and outcome/subgroup-specific specification history are unavailable. The article's disclosed initial 9% noninferiority-to-superiority redesign and omission of intubated mortality from the final secondary list remain substantial alternatives for C011. Final retained analysis commitments remain compared with identified supplied results; absence of a counterpart does not establish that analyses were never performed elsewhere.

Unidentified planned outputs include primary RR/adjusted/PP analyses, Borg and lowest-SpO2 outcomes, joint longitudinal analyses and separate ICU-stay survival estimators/populations. PP definitions and adjustment covariates are not invented. Exact competitor/discharge rules, test mappings, forest reference definitions and subgroup-covariate completeness are missing. C015 explicitly permits available-covariate or restricted-population explanations and does not assume every binary category partitions all participants.

Supplementary point, dispersion-bar and star definitions are unsupplied and were not treated as stated confidence intervals or significance thresholds. Historical plan-table right edges on [joi180109supp1_prod.pdf — p.127](<../joi180109supp1_prod.pdf#page=127>) and [p.128](<../joi180109supp1_prod.pdf#page=128>) are clipped in the source. Visible content was mapped; missing continuations were not completed by inference.

Original reusable extraction/render engine versions are unrecorded. Current source checks establish usable content fitness without certifying those original versions. Partial derivatives and text-only page-image gaps have complementary usable extraction; no scientific source-coverage gap remains. Tesseract and LibreOffice are unavailable, but OCR and Office conversion are unnecessary for these supplied PDFs. Full limitations are retained in [limitations.md](review_1_6_2/limitations.md).

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

The reproducibility record is contained in [routing_preflight.md](review_1_6_2/routing_preflight.md), [tooling_record.md](review_1_6_2/tooling_record.md), [run_state.md](review_1_6_2/run_state.md), [agent_execution_manifest.md](review_1_6_2/agent_execution_manifest.md), [candidate_ledger.md](review_1_6_2/candidate_ledger.md), [evidence_recheck.md](review_1_6_2/verification/evidence_recheck.md) and [evidence_quality_audit.md](review_1_6_2/quality/evidence_quality_audit.md). Discovery was rebuilt from source-linked evidence assets and complete mapping rather than earlier candidate decisions.

Routing preflight is PASS: default run model gpt-6.1-sol; model source DEFAULT; Provider CURRENT_SESSION; execution mode INTERACTIVE_CLI; coordinator inference PASS; all ten named presets verified. The coordinator uses high effort, ordinary specialists medium effort, and statistical/screening/recheck/audit specialists high effort. All 16 specialists are fresh runtime agents; the coordinator is recorded once.

### Source integrity and local tooling

The four direct sources and 432 reused assets were hashed before scientific work and again after review. Both after inventories are byte-identical to their before inventories. The recorded source and reused-asset checks therefore show unchanged inputs. Detailed hash records are [source_hashes_before.sha256](review_1_6_2/source_hashes_before.sha256), [source_hashes_after.sha256](review_1_6_2/source_hashes_after.sha256), [reused_artifact_hashes_before.sha256](review_1_6_2/reused_artifact_hashes_before.sha256) and [reused_artifact_hashes_after.sha256](review_1_6_2/reused_artifact_hashes_after.sha256).

| Supplied source | SHA-256 |
|---|---|
| jama_azoulay_2018_oi_180109.pdf | 515e58637dd5489fa605d597e7d637c52297a954616e3924f6fc14fa46d1f0b6 |
| joi180109supp1_prod.pdf | 8036657a65b8d2de9f209729822652f95ba1436079ce8e524d6538b64f7f87c3 |
| joi180109supp2_prod.pdf | 13c31ed5f073920f8c5fcd98965e4ed6a19411480939559d4eb87a792276a868 |
| joi180109supp3_prod.pdf | 2fdd033524cf8076b380c2a1e9fe1bf12d2ad6b91e40781f50e3f2873442e528 |

Processing used CPU. Current direct confirmation/render engines are Poppler 25.03.0; file checks use file 5.46 and hashing uses GNU coreutils 9.7. Native/layout extraction and targeted visual confirmation sufficed; no new OCR, Office conversion, GPU or fallback environment was required. Fallback status is NOT_NEEDED/NOT_CREATED. The coordinator performs local standalone HTML rendering with Pandoc 3.1.11.1 and final mechanical validation after Markdown assembly.

### Agent execution

All 17 actual agents, including the coordinator and additional bounded support shards, are recorded below. Artifact paths in this table are relative to review_1_6_2/.

| Stage | Agent ID | Model | Reasoning effort | Start mode | Artifact |
|---|---|---|---|---|---|
| coordinator | 01a129af-68b6-7e42-a754-cf9af7ad7441 | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | 01a129b0-e282-71e3-a1f6-409da964d142 | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | 01a129b4-3791-7603-a1a4-8c610dfdecaf | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | 01a129b4-5b29-7571-a033-f4edc42e6311 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| support_quantitative_mapper_shard_1 | 01a129b4-7c84-7f70-89f1-d9e06894b991 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_001_032.md |
| support_quantitative_mapper_shard_2 | 01a129b4-9407-7911-8acb-78005de23e07 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_033_064.md |
| support_quantitative_mapper_shard_3 | 01a129b4-ab4c-7ca2-8493-423476e266b5 | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/parts/support_plan_065_094.md |
| numeric_consistency_reviewer | 01a129b8-e16e-7732-8986-717ce7785e24 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | 01a129b9-0d28-70a3-a6a4-0dc8194fcb34 | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | 01a129b9-3c75-7c50-8787-4de976dc68d0 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| inclusion_screener | 01a129ca-c991-7a90-b0ad-3686288f164b | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | 01a129d3-409c-71e2-ad6d-92edf3038cd4 | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | 01a129db-13d2-7fe1-a704-4db0b539bac8 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_shard_support | 01a129db-42fe-7702-a208-6cf2e0d12816 | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_s061_s099.md |
| quality_control_auditor | 01a129e2-d0f7-7da1-8dc5-7c2d0b2ec94b | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| quality_control_auditor_shard_support | 01a129e3-1015-7543-8dd4-18036273576e | gpt-6.1-sol | high | FRESH_SPAWN | quality/parts/evidence_quality_c009_c016.md |
| report_generator | 01a129ec-e15a-73b1-98b8-a4d29010abef | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

The two statistical passes use different fresh runtime IDs. Support mapping, pass-2 and audit shards preserve complete disjoint coverage; none selects candidates by count. There is no pass-2 inclusion-screener runtime because pass 2 emitted no findings.

### Reproducibility performance

- **Target basis:** Four PDF sources with 144 pages; reusable native/layout text and rendered pages have usable coverage on every page. No Office conversion; available CPU PDF tools. Protocol/SAP mapping uses four disjoint shards, followed by concurrent numeric/cross-source/statistical checks and independent screening, recheck, second statistical pass, audit and report waves. Target allows visual result-table mapping and full plan-version comparison; zero fresh extraction units required.
- **Total source units:** 144
- **Fresh-source units:** 0
- **Target elapsed minutes:** 35-55
- **Started UTC:** 2026-10-11T06:39:59Z
- **Finished UTC:** 2026-10-11T07:52:04Z
- **Observed elapsed minutes:** 72.08
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Complete source-confirmation and evidence-card review waves; initial statistical link and readability repairs; context-bound second-pass and audit sharding

These are the finalized performance fields copied exactly from run_state.md immediately after Markdown assembly. The selected 55-minute upper bound has been exceeded; the bounded causes are recorded above. Local HTML rendering and mechanical validation remain outside observed review duration. A model-based validation repair requires an updated finish record.

