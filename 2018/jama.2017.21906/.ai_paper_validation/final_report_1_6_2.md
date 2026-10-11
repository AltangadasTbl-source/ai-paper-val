# ACS QUIK Quantitative Reporting Quality-Control Consistency Review — Workflow 1.6.2

**Pending Human Adjudication**

This report records candidate reporting issues for later human adjudication. Evidence states and inclusion-audit results describe the review record; they do not decide a candidate's final disposition.

## Executive Quality-Control Summary

Complete quantitative quality control of the supplied ACS QUIK package identified **7 stable candidates**, supported by 10 independently screened findings. Four concern planned versus reported outcomes or analyses; three concern the interpretation or reproduction of reported statistical results. Every candidate has evidence state reproduced and inclusion audit CONFIRMED, and every candidate remains Pending Human Adjudication.

All 80 physical PDF pages across four sources were mapped, comprising 69 reusable-backed pages and 11 fresh-required pages. The review reconstructed 30 numeric relationships and 163 statistical relationships. Both independent statistical passes completed all 163 relationships. The numeric lane checked 228 count/percentage pairs and 20 participant-flow blocks without registering a numeric finding. Recheck and audit retained source-grounded alternatives and missing definitions rather than treating an unprovided generating procedure as established.

The seven issues concern the medication composite's statin component, expanded-MACE status and identity, the primary-MACE subgroup specification, the mapping of two adjusted time-effect columns, residual direction, the LDL confidence interval in a follow-up descriptive table, and identification of a planned complete-case primary-MACE sensitivity analysis. Potential extraction implications are conditional on subsequent adjudication; this review does not establish downstream propagation or a change to trial conclusions.

## Package and Reused-Evidence Provenance

The package contains four supplied PDFs and no direct Office document, workbook or CSV source. Source IDs and physical PDF pages are stable locators. Document roles follow content, including the mixed operational/results supplement.

| Source ID | Supplied source and page locator | Content-based role | Physical pages | SHA-256 |
|---|---|---|---:|---|
| DOC-001 | [jama_huffman_2018_oi_170166.pdf — p.1](../jama_huffman_2018_oi_170166.pdf#page=1) | REPORT, pp.1–12: main trial article | 12 | 11311a6bb5c7a4be734ed60776b308f525ad101671ccc8d34bab18735aaca5f5 |
| DOC-002 | [joi170166supp1_prod.pdf — p.1](../joi170166supp1_prod.pdf#page=1) | PLAN, pp.1–32: protocol, version 22 September 2014 | 32 | 0e13bdfc6e5e3c8b86e187f54f0a3d7d0217fc0614be9fbdbbb7839dbab9004a |
| DOC-003 | [joi170166supp2_prod.pdf — p.1](../joi170166supp2_prod.pdf#page=1) | PLAN, pp.1–9: SAP, revised 17 June 2015 | 9 | d49019c3cf6ee0766fb319f254f27f87751a73bfec66c34d38bae16a956bb1c6 |
| DOC-004 | [joi170166supp3_prod.pdf — p.1](../joi170166supp3_prod.pdf#page=1) | REPORT index p.1; PLAN operational toolkit pp.2–16; REPORT eTables/eFigures pp.17–27 | 27 | 511f4a907e4c48d920f1c6b89d444fe76c7c91e11bbae84cdee834fa0393f3ec |

The curator inventoried and hashed 82 preserved evidence assets: 67 USABLE and 15 PARTIAL, with zero STALE, DUPLICATE or UNREADABLE assets. These comprise native/layout text, PDF information, page images, OCR text and its provenance records. Overlapping derivatives were counted as assets, not additional source pages. Historical OCR for the scanned toolkit used recorded rapidocr engines, including a historical GPU record; this review used CPU processing and no GPU OCR. Current native-text correspondence, source hashes and page-image fitness checks determined reuse eligibility. Old review conclusions were not scientific discovery inputs.

The main layout gaps on pp.4 and 8 were covered by matching native text and images; the protocol's embedded schedule on p.14 had a reusable image. Toolkit pp.3–16 had source-matched OCR and images despite minimal native text. Results-supplement pp.17–27 received fresh current-source image mapping because earlier and current renders differed in bytes. Direct source pages remain the authority for all candidate comparisons. See the [source inventory](review_1_6_2/source_inventory.md), [evidence-asset inventory](review_1_6_2/evidence_asset_inventory.md), [source hash baseline](review_1_6_2/source_hashes_before.sha256), and [reused-asset hash baseline](review_1_6_2/reused_artifact_hashes_before.sha256).

## Scope, Complete Coverage, and Exclusions

The scope comprises counts and denominators; estimate, interval and test logic; source-grounded statistical-method logic; and planned versus reported statistical design. Every direct-source page was assigned and mapped. Reuse accelerated extraction without limiting discovery.

| Source | Total units | Reusable units | Fresh-required units | Mapped units | Status |
|---|---:|---:|---:|---:|---|
| DOC-001, main article | 12 | 12 | 0 | 12 | COMPLETE |
| DOC-002, protocol | 32 | 32 | 0 | 32 | COMPLETE |
| DOC-003, SAP | 9 | 9 | 0 | 9 | COMPLETE |
| DOC-004, operational/results supplement | 27 | 16 | 11 | 27 | COMPLETE |
| **Total** | **80** | **69** | **11** | **80** | **COMPLETE** |

The main map covers 12 pages. Disjoint support maps cover 57 plan/index/toolkit pages and 11 result pages, totaling all 68 support pages. The [source-coverage ledger](review_1_6_2/source_coverage.md) and [coverage manifest](review_1_6_2/coverage_manifest.md) document the full assignments and artifact paths.

The review excludes broad clinical, study-design, novelty, misconduct and raw-data judgments and does not propose a preferred analysis. Peripheral descriptive copies, administrative details and operational examples are considered under the supplied scope's narrower comparison rule. Obvious notation or terminology, model-based estimates compared with crude recomputations, unsupported conditional assumptions, and discrepancies at most 5% after half-unit display-precision intervals do not independently qualify. Exact unprinted graph values, model internals and patient-level quantities were not manufactured.

## Quantitative and Statistical Relationship Coverage

The [numeric inventory](review_1_6_2/relationships/numeric_relationship_inventory.md) contains 30 relationships: 13 main and 17 support relationships. It retains count, total, numerator/denominator, percentage, baseline, flow and graphical relationships. The [statistical inventory](review_1_6_2/statistics/relationship_inventory.md) contains 163 relationships: 92 main and 71 support relationships. Grouped table relationships preserve every displayed cell and model, and graphical relationships retain all panels, axes, contrasts and available confidence-interval information.

| Stage | Completed scope | Findings or outcome |
|---|---|---|
| Numeric consistency review | All 30 numeric relationships and numeric fields of all 163 statistical relationships; 228 count/percentage pairs; 20 flow blocks | 0 findings; 12 excluded-observation rows |
| Cross-source consistency review | Matched results and protected plan/report comparisons across all four sources | 3 findings; 11 excluded-observation rows |
| Statistical pass 1 | All 163 statistical relationships; fresh main/support agents; explicit PASS_1_COMPLETE records | 6 findings; 9 main and 13 support excluded-observation rows |
| Statistical pass 2 | All 163 statistical relationships; different fresh main/support agents; explicit PASS_2_COMPLETE records; all 45 initial excluded observations revisited | 1 additional finding, F-ST2-501; separately screened and rechecked as C007 |
| Independent quality-control audit | All 80 pages, 30 numeric and 163 statistical relationships; every candidate, screening decision, classification and excluded observation | 7 CONFIRMED; 0 QUESTIONED; 0 new findings or classification changes |

The passes checked containment, endpoint order, null/direction agreement, supplied estimate/test compatibility, statistical-method logic, matched-result identity, decision rules, and planned-versus-reported analyses. Diagnostic calculations were kept separate from established producing methods. Complete records are in [numeric review](review_1_6_2/checkers/numeric_consistency.md), [cross-source review](review_1_6_2/checkers/cross_source_consistency.md), [statistical pass 1](review_1_6_2/checkers/statistical_pass_1.md), [statistical pass 2](review_1_6_2/checkers/statistical_pass_2.md), and the [quality audit](review_1_6_2/quality/evidence_quality_audit.md).

## Inclusion Screening Summary

A finding qualifies only when reproduced and meeting either an always-register Route A category or all three Route B criteria: in focus, not immediately resolved by context, and plausibly relevant to a specific result's interpretation or extraction. Display-precision comparisons allow each input and printed output its half-unit interval; a surviving relative discrepancy above 0.05 qualifies. The interval-versus-P/test category is not treated as rounding.

The [canonical screening log](review_1_6_2/screening/inclusion_screen.md) contains 10 rows, each with exactly one decision. The initial screen included 9 findings, consolidated into 6 issues. A different fresh pass-2 screener included 1 additional finding, appended as C007. Three pairs of independent checker findings refer to C001, C002 and C003 respectively. Consolidation retained every affected location.

| Screening stage | Findings screened | INCLUDE | SCREENED_OUT | Distinct newly registered issues |
|---|---:|---:|---:|---:|
| Initial | 9 | 9 | 0 | 6 |
| Pass 2 | 1 | 1 | 0 | 1 |
| Audit additions | 0 | 0 | 0 | 0 |
| **Total** | **10** | **10** | **0** | **7** |

| Decision | Reason code | Count |
|---|---|---:|
| INCLUDE | MEETS_THRESHOLD | 10 |
| SCREENED_OUT | NOT_REPRODUCED | 0 |
| SCREENED_OUT | ROUNDING_OR_DISPLAY_PRECISION | 0 |
| SCREENED_OUT | NOTATION_OR_TYPOGRAPHY | 0 |
| SCREENED_OUT | TERMINOLOGY_OR_WORDING | 0 |
| SCREENED_OUT | MODEL_VERSUS_CRUDE | 0 |
| SCREENED_OUT | CONTEXT_RESOLVES | 0 |
| SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | 0 |
| SCREENED_OUT | PERIPHERAL_COMPARISON | 0 |
| SCREENED_OUT | OUT_OF_FOCUS | 0 |
| SCREENED_OUT | DUPLICATE_OF_INCLUDED | 0 |

Checker self-screening tables contained 45 initial observations without finding IDs: 12 numeric, 11 cross-source, 9 main-statistical and 13 support-statistical. Those are not formal screened findings and do not inflate the 10-row screening denominator. Their initial reason-code counts were 9 display-precision, 3 model-versus-crude, 11 terminology, 5 notation, 10 conditional/unreported, 4 peripheral, 2 out-of-focus and 1 context-resolves. Pass 2 and audit retained 43 as exclusions, recognized one as already represented by C005, and promoted one concrete planned-primary-sensitivity observation to F-ST2-501/C007. All 45 received reassessment, including checks for always-register categories. No screened-out observation receives a candidate card.

## Review-Domain Summary

The four domains distinguish statistical-result logic, report-internal result attribution, plan/report statistical design, and plan-internal statistical design. Domains and relationship types describe the evidence comparison and are not adjudications. P_R compares PLAN with REPORT; P_P is within PLAN; S_C crosses REPORT documents; S_W is within one REPORT document. Primary-type precedence is P_R > P_P > S_C > S_W, and corroboration alone adds no conflicting relationship.

| Review domain | Definition | Candidates |
|---|---|---:|
| statistical_results | Counts, estimates, intervals, tests or statistical methods in REPORT materials | 3 |
| report_internal_inconsistency | REPORT conflict about the outcome, time, population or comparison to which a result belongs | 0 |
| protocol_report | Planned versus reported statistical-design or analysis element | 4 |
| plan_material | Inconsistent statistical-design element solely within PLAN material | 0 |
| **Total** | | **7** |

| Primary relationship type | Candidates |
|---|---:|
| P_R | 4 |
| P_P | 0 |
| S_C | 0 |
| S_W | 3 |
| **Total** | **7** |

Every candidate's all-relationships field contains only its primary type; therefore the relationship-membership totals are also P_R 4, P_P 0, S_C 0 and S_W 3.

| Evidence state | Candidates |
|---|---:|
| reproduced | 7 |
| reproduced_after_transcription_correction | 0 |
| not_reproduced | 0 |
| **Total** | **7** |

Inclusion audit: CONFIRMED 7; QUESTIONED 0. Qualifying routes: Route A category 5, four candidates; Route A category 2, one; Route A category 4, one; Route B, one. Each summary reconciles to the seven stable IDs.

## Candidate Index

| Stable ID | Candidate reporting issue | Review domain | Relationship type | Evidence state | Inclusion audit |
|---|---|---|---|---|---|
| [C001](#c001--planned-statin-component-versus-reported-medication-composite) | In-hospital medication composite omits the planned statin component | protocol_report | P_R | reproduced | CONFIRMED |
| [C002](#c002--planned-expanded-mace-objective-versus-reported-post-hoc-status) | Expanded-MACE prospective status and reported identity | protocol_report | P_R | reproduced | CONFIRMED |
| [C003](#c003--planned-primary-mace-subgroups-versus-reported-prespecified-set) | Primary-MACE subgroup specification | protocol_report | P_R | reproduced | CONFIRMED |
| [C004](#c004--distinct-adjusted-time-contrasts-lack-an-estimand-mapping) | Adjusted time-effect columns lack distinct mapping | statistical_results | S_W | reproduced | CONFIRMED |
| [C005](#c005--opposing-directional-readings-of-the-hospital-residual-display) | Residual definition and caption assign opposing direction | statistical_results | S_W | reproduced | CONFIRMED |
| [C006](#c006--ldl-interval-versus-the-same-display-reproducing-calculation) | LDL interval differs from a same-display reproducing calculation | statistical_results | S_W | reproduced | CONFIRMED |
| [C007](#c007--planned-complete-case-primary-mace-sensitivity-result-is-not-identified) | Planned complete-case primary-MACE sensitivity lacks identified counterpart | protocol_report | P_R | reproduced | CONFIRMED |

## Candidate Evidence Cards

## C001 — Planned statin component versus reported medication composite

**Pending Human Adjudication**

**Candidate statement:** The supplied SAP defines optimal in-hospital medication using five components including statin, while the report's associated composite and results use four components and expressly disclose that the predefined in-hospital statin data were not collected.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP p.5 vs REPORT main pp.3,7 and results supplement pp.21,22

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001, F-ST1-502

**Qualifying route:** Route A, category 5

**Classification rationale:** The substantive comparison is a prospective PLAN component list versus REPORT endpoint definitions. The REPORT occurrences agree with one another and add no S_C or S_W; no plan-internal conflict adds P_P. P_R maps to protocol_report.

**Classification ambiguity:** None

**Exact source locations:** PLAN [joi170166supp2_prod.pdf — p.5, §6.1.2, lines 1149–1151](../joi170166supp2_prod.pdf#page=5); REPORT [jama_huffman_2018_oi_170166.pdf — p.3, Outcomes](../jama_huffman_2018_oi_170166.pdf#page=3); REPORT [jama_huffman_2018_oi_170166.pdf — p.7, Table 3 medication row and footnote c](../jama_huffman_2018_oi_170166.pdf#page=7); REPORT [joi170166supp3_prod.pdf — p.21, eTable 5 medication row and footnote c](../joi170166supp3_prod.pdf#page=21); REPORT [joi170166supp3_prod.pdf — p.22, eTable 6 medication row and footnote b](../joi170166supp3_prod.pdf#page=22).

**Source evidence:** SAP lists aspirin, ADP receptor antagonist, heparin, statin and beta blocker. Main Outcomes lists aspirin, ADP antagonist, anticoagulant and β-blocker and discloses statin noncollection. Table 3 and both sensitivity displays omit statin. The discharge-medication composite is a separate endpoint and retains statin; it is not substituted for this comparison.

**Reported-versus-comparator:** Reported four-component optimal in-hospital use is control 3122 (31.7%) versus intervention 3878 (35.8%). Its primary adjusted difference is 6.00 percentage points (95% CI 3.90–8.11), OR 1.45 (1.28–1.64); cluster-adjusted difference 8.61 (6.98–10.23), OR 1.70 (1.57–1.85). eTable 5 ORs are GRACE 2.19 (1.83–2.62), transfer 1.47 (1.29–1.66), insurance 1.45 (1.28–1.64), and prehospital aspirin 1.47 (1.30–1.66); eTable 6 OR is 0.87 (0.70–1.07). The comparator is the planned five-component conjunction, not a reconstructed numerical treatment effect.

**Reasoning procedure:** Match the in-hospital endpoint across definitions and result rows, distinguish it from discharge medication, and compare component membership. Treat heparin/anticoagulant wording separately; the registered issue is statin membership.

**Calculation:** Planned set has five components; every reported set has four and excludes statin. This is categorical: half-unit numerical intervals and relative discrepancy are inapplicable. The associated four-component results cannot reconstruct a five-component count or effect from the supplied aggregates.

**Affected result or extracted value:** Definition, eligibility and interpretation of the optimal in-hospital medication composite and all listed treatment-effect and sensitivity results.

**Why context does not resolve it:** Route A, category 5 covers a changed prespecified composite definition. Disclosure of noncollection establishes the component change; it does not supply a prospectively revised definition or a five-component result.

**Alternative source-grounded interpretations:** An intentional disclosed adaptation to noncollection may explain the four-component result, or a later approved amendment may establish it. No dated amendment, statin observations, five-component outcome count or five-component eligibility set is supplied. Any eligibility consequence remains unestablished.

**Mechanical evidence recheck:** The fresh rechecker found and visually reread every listed source location, matched all printed components and numerical rows, and reproduced the component-set comparison. No transcription or location amendment was needed. PLAN/REPORT roles, P_R and protocol_report were confirmed; the independent audit confirmed inclusion. Direct observations are the lists and disclosure; amendment timing and patient-level consequences remain alternatives. See [combined recheck, C001](review_1_6_2/verification/evidence_recheck.md#c001--statin-component-absent-from-the-reported-in-hospital-composite).

**Potential downstream evidence impact:** If confirmed, an extractor could copy the four-component medication effect while interpreting it as the supplied SAP's five-component endpoint. Definition and eligibility clarification could distinguish these results; no downstream use or conclusion change is established.

## C002 — Planned expanded-MACE objective versus reported post-hoc status

**Pending Human Adjudication**

**Candidate statement:** The protocol and SAP prospectively name expanded MACE as a secondary objective, whereas the specifically expanded result in the report is repeatedly described as post hoc. Its equivalence to the planned expanded endpoint remains undefined.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol p.9 and SAP pp.2,3 vs REPORT main pp.3,8,9 and results supplement pp.1,23

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003, F-ST1-503

**Qualifying route:** Route A, category 5

**Classification rationale:** Both prospective PLAN documents agree about the named secondary objective, and REPORT locations agree about the reported expansion. The substantive status/identity comparison crosses PLAN and REPORT, giving P_R and protocol_report; corroboration adds no P_P, S_C or S_W.

**Classification ambiguity:** The prospective expanded-MACE component set is not supplied, leaving equivalence to the reported seven-component outcome unresolved; document roles and the PLAN/REPORT relationship are clear.

**Exact source locations:** PLAN [joi170166supp1_prod.pdf — p.9, §2.2.3, lines 259–263](../joi170166supp1_prod.pdf#page=9); PLAN [joi170166supp2_prod.pdf — p.2, §2.1.2, lines 1071–1072](../joi170166supp2_prod.pdf#page=2); PLAN [joi170166supp2_prod.pdf — p.3, continuation, lines 1073–1074](../joi170166supp2_prod.pdf#page=3); REPORT [jama_huffman_2018_oi_170166.pdf — p.3, Outcomes and Statistical Analysis](../jama_huffman_2018_oi_170166.pdf#page=3); REPORT [jama_huffman_2018_oi_170166.pdf — p.8, Secondary and Post Hoc Analyses](../jama_huffman_2018_oi_170166.pdf#page=8); REPORT [jama_huffman_2018_oi_170166.pdf — p.9, result continuation and Discussion](../jama_huffman_2018_oi_170166.pdf#page=9); REPORT [joi170166supp3_prod.pdf — p.1, eTable 7 index entry](../joi170166supp3_prod.pdf#page=1); REPORT [joi170166supp3_prod.pdf — p.23, eTable 7 title, expanded row and footnotes](../joi170166supp3_prod.pdf#page=23).

**Source evidence:** Both plans list in-hospital and 30-day expanded MACE under secondary objectives without enumerating the additional components. The report calls the expansion adding incident in-hospital heart failure, cardiogenic shock and cardiac arrest post hoc in methods, results and discussion; the supplement titles the display exploratory.

**Reported-versus-comparator:** Reported expanded MACE is control 919 (9.1%) versus intervention 795 (7.0%). Cluster-adjusted difference is −0.86 percentage points (95% CI −1.72 to −0.01), OR 0.89 (0.80–1.00); primary adjusted difference −1.34 (−2.72 to 0.04), OR 0.84 (0.70–1.00). These specifically defined reported results are compared with the prospectively named secondary expanded-MACE objective and its status.

**Reasoning procedure:** Read the prospective objective with its page-spanning SAP continuation, then match the expanded report components, repeated explicit post-hoc statements and eTable 7. Distinguish a specific post-hoc characterization from general exploratory caution due to unadjusted multiplicity.

**Calculation:** Planned status is secondary; the specifically reported expansion is post hoc. Component identity cannot be calculated because the prospective added-component list is absent. This categorical comparison has no half-unit interval or relative discrepancy. No P value is inferred from an OR limit printed as 1.00.

**Affected result or extracted value:** Prospective versus post-hoc status and endpoint identity attached to the expanded-MACE counts, adjusted differences and ORs listed above.

**Why context does not resolve it:** Route A, category 5 covers changed prespecified outcome status or composite definition. The explicit post-hoc statements establish the status contrast, while the unnamed prospective expansion prevents resolving whether these are the same endpoint.

**Alternative source-grounded interpretations:** The planned broad expansion could be distinct from the later heart-failure/shock/arrest expansion, or the reported seven-component outcome could implement the planned objective. The prospective expansion's exact components, analysis specification and any later dated amendment are missing. Neither alternative is adopted as established.

**Mechanical evidence recheck:** All eight cited locations were found and source-confirmed, including both SAP pages and every reported value. The comparison was reproduced without transcription adjustment; roles and P_R/protocol_report classification were confirmed. The independent audit retained the component-identity uncertainty and confirmed inclusion. See [combined recheck, C002](review_1_6_2/verification/evidence_recheck.md#c002--planned-secondary-expanded-mace-versus-reported-post-hoc-expansion).

**Potential downstream evidence impact:** If confirmed, a review could attach a prospective-secondary or post-hoc status to a different expanded endpoint, or combine results under an insufficiently matched composite definition. The issue concerns identity and extraction status; no clinical-conclusion reversal is established.

## C003 — Planned primary-MACE subgroups versus reported prespecified set

**Pending Human Adjudication**

**Candidate statement:** The reported primary-MACE subgroup set labeled prespecified changes the planned age partition, adds hospital type without a located supplied prospective specification, and does not identify the planned toolkit-use primary-outcome subgroup result.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP pp.5,7 vs REPORT main pp.3,9,10

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002, F-ST1-504

**Qualifying route:** Route A, category 5

**Classification rationale:** The prospective SAP subgroup specification is PLAN; the reported methods, Figure 3 and discussion are REPORT. Their substantive difference gives P_R and protocol_report. Agreeing reported prespecified claims and supporting SAP context add no other relationship.

**Classification ambiguity:** None

**Exact source locations:** PLAN [joi170166supp2_prod.pdf — p.5, §6.1.3, lines 1156–1165](../joi170166supp2_prod.pdf#page=5); PLAN [joi170166supp2_prod.pdf — p.7, §7.5.2, lines 1243–1254](../joi170166supp2_prod.pdf#page=7); REPORT [jama_huffman_2018_oi_170166.pdf — p.3, Statistical Analysis and separate process-evaluation statement](../jama_huffman_2018_oi_170166.pdf#page=3); REPORT [jama_huffman_2018_oi_170166.pdf — p.9, Figure 3 age/hospital-type rows, title and narrative](../jama_huffman_2018_oi_170166.pdf#page=9); REPORT [jama_huffman_2018_oi_170166.pdf — p.10, opening Discussion](../jama_huffman_2018_oi_170166.pdf#page=10).

**Source evidence:** SAP's a priori primary-endpoint subgroups are hospital size, toolkit-component use, age <65/>65, sex and STEMI/NSTEMI. The report labels age <50/50–69/≥70 and government/nonprofit/private hospital-type analyses prespecified. Its complete 14-row display has no toolkit-use row. Complete supplied-plan searches located no specification for those revised age groups or hospital type; complete supplied-report searches located no primary-MACE toolkit-use result.

**Reported-versus-comparator:** The comparison is the printed prespecified subgroup set against the supplied prospective list. The six affected Figure 3 rows retain the following source results, with intervention then control counts and percentage-point adjusted differences:

| Subgroup | Intervention events/total (%) | Control events/total (%) | Adjusted difference (95% CI) | Adjusted OR (95% CI) |
|---|---|---|---|---|
| Age <50 | 58/2079 (2.8) | 68/2045 (3.3) | 1.42 (−0.71 to 3.54) | 1.53 (0.83–2.79) |
| Age 50–69 | 297/6606 (4.5) | 326/5863 (5.6) | −0.57 (−2.02 to 0.88) | 0.89 (0.67–1.19) |
| Age ≥70 | 247/2623 (9.4) | 251/2158 (11.6) | −0.23 (−3.32 to 2.85) | 0.98 (0.71–1.35) |
| Government, 9 hospitals | 158/3036 (5.2) | 275/4097 (6.7) | −0.55 (−2.56 to 1.47) | 0.90 (0.61–1.33) |
| Nonprofit, 12 hospitals | 186/2964 (6.3) | 193/2785 (6.9) | −0.62 (−3.43 to 2.20) | 0.91 (0.59–1.40) |
| Private, 42 hospitals | 258/5308 (4.9) | 177/3184 (5.6) | 0.89 (−1.19 to 2.97) | 1.16 (0.82–1.64) |

**Reasoning procedure:** Match the primary endpoint and subgroup-analysis purpose, compare the prospective and reported partitions, and inspect every repeated prespecified claim. Treat the revised age bands, added hospital type and unreported toolkit-use analysis as one related specification pattern. Hospital size and type are distinct characteristics; the age-65 equality boundary is not separately registered.

**Calculation:** The prospective two-band age partition and reported three-band partition differ categorically; hospital type is added, and toolkit-use analysis has no located reported counterpart. Display-precision intervals are inapplicable. Published subgroup counts reconcile to the full arm totals; adjusted effects are not equated with crude ratios.

**Affected result or extracted value:** Prespecification and grouping of the primary-MACE age/hospital-type heterogeneity results, and availability of planned age-at-65 and toolkit-use primary-outcome analyses.

**Why context does not resolve it:** Route A, category 5 covers analyses described as prespecified but absent from the supplied plan and planned primary analyses without identified reported results. A separate process-evaluation promise does not identify the planned primary-MACE toolkit-use analysis.

**Alternative source-grounded interpretations:** A later dated specification may have revised age groups, added hospital type and replaced or deferred toolkit analysis. The promised separate process evaluation may address implementation, but its content is not supplied. The relevant amendment/specification and primary-MACE toolkit-use result or documented mapping are missing.

**Mechanical evidence recheck:** Every listed page, prospective item, reported claim and all six quantitative rows were visually matched; complete supplied-document searches supported the bounded absence statements. The categorical comparison was reproduced with no transcription adjustment. P_R/protocol_report was confirmed, and independent audit confirmed inclusion. See [combined recheck, C003](review_1_6_2/verification/evidence_recheck.md#c003--reported-prespecified-primary-mace-subgroup-set-differs-from-the-supplied-plan).

**Potential downstream evidence impact:** If confirmed, an extractor could attribute prespecified status to the displayed groups or assume availability of a planned subgroup analysis without a supplied counterpart. Clarification could improve subgroup definition and status extraction; no effect on the overall trial conclusion is established.

## C004 — Distinct adjusted time contrasts lack an estimand mapping

**Pending Human Adjudication**

**Candidate statement:** Table 2 prints two materially distinct adjusted effects for each of two time outcomes under shared method context, without separately mapping the columns to their estimands, models or contributing populations.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main Table 2 p.6 effect columns and method context p.3

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-001

**Qualifying route:** Route B

**Classification rationale:** Both adjusted-effect columns and their method context are REPORT content within one main article, giving S_W. The issue concerns estimates and statistical-method mapping, so the domain is statistical_results. A general prospective model description is not an additional conflicting comparator.

**Classification ambiguity:** None

**Exact source locations:** REPORT [jama_huffman_2018_oi_170166.pdf — p.6, Table 2 title, door-to-balloon and door-to-needle rows, both adjusted headings and footnotes b/c](../jama_huffman_2018_oi_170166.pdf#page=6); REPORT [jama_huffman_2018_oi_170166.pdf — p.3, Statistical Analysis](../jama_huffman_2018_oi_170166.pdf#page=3).

**Source evidence:** Both headings cite footnote b, describing intervention-versus-control effects and intervention-minus-control marginal effects from mixed logistic/quantile models with hospital and time adjustment. Footnote c identifies β coefficients but does not separately define the Difference column's time estimand. Main methods provide no row-specific mapping. Row units are minutes; the readily resolved percent-sign heading is separate from this candidate.

**Reported-versus-comparator:** For door-to-balloon time, control median is 65 (IQR 53–105), n=4022, and intervention median 77 (55–118), n=3639; Difference is 6.18 (95% CI −4.78 to 17.14), β is 13.00 (3.64–22.36). For door-to-needle time, control median is 44 (30–67), n=1455, and intervention median 45 (27–75), n=1433; Difference is 0.40 (−5.23 to 6.03), β is 5.00 (−5.20 to 15.20). The comparators are the two adjusted columns and their common description, not crude median differences.

**Reasoning procedure:** Identify the same row, adjustment context, model-family statement and column footnotes; establish that the numbers differ beyond display precision; determine whether the source maps each to a distinct analysis. Legitimate distinct estimands need not be equal, but their interpretation for extraction requires a supplied distinction. No P value or test is printed, so this is not a CI-versus-P/test conflict.

**Calculation:** Door-to-balloon point intervals [6.175,6.185] and [12.995,13.005] have gap 6.810, relative gap 6.810/6.18=1.10194175. Door-to-needle intervals [0.395,0.405] and [4.995,5.005] have gap 4.590, relative gap 4.590/0.40=11.475. Both exceed 0.05. Endpoint half-unit intervals remain:

| Row/column | Lower-limit interval | Upper-limit interval | Null inclusion throughout rounding intervals |
|---|---|---|---|
| Door-to-balloon Difference | [−4.785,−4.775] | [17.135,17.145] | Includes 0 |
| Door-to-balloon β | [3.635,3.645] | [22.355,22.365] | Excludes 0 |
| Door-to-needle Difference | [−5.235,−5.225] | [6.025,6.035] | Includes 0 |
| Door-to-needle β | [−5.205,−5.195] | [15.195,15.205] | Includes 0 |

All points remain inside their own ordered intervals. These calculations establish distinct published summaries, without imposing equal estimands or inferring covariance or degrees of freedom.

**Affected result or extracted value:** Which adjusted time contrast to extract, its magnitude and interval; for door-to-balloon, whether that extracted interval includes zero.

**Why context does not resolve it:** Route B1 is met by in-focus estimate/method logic. B2 is met because the shared footnote and β label do not map the distinct adjusted time estimands; minutes resolve units but not analyses. B3 is met because choosing a column changes the extracted effect and door-to-balloon null inclusion. The source does not identify the intended distinction at once.

**Alternative source-grounded interpretations:** Difference may represent a marginal time effect and β a conditional quantile coefficient; distinct quantiles, transformations, adjustment models or populations could also produce legitimate distinct summaries. The exact row/column estimand, quantile, scale, model, marginalization procedure and population are not supplied. No alternative is presumed to be the producing analysis.

**Mechanical evidence recheck:** Both pages, all row values, headings and footnotes were visually found and matched. The precision gaps and endpoint null inclusion reproduced without transcription amendment; S_W/statistical_results was confirmed. Independent audit confirmed Route B inclusion and preserved the absence of a printed test. See [combined recheck, C004](review_1_6_2/verification/evidence_recheck.md#c004--distinct-adjusted-time-contrasts-lack-an-estimand-mapping).

**Potential downstream evidence impact:** If confirmed, an extractor could select different adjusted time effects or attach a column's interval interpretation to an insufficiently defined contrast. Clarifying each producing analysis could make those two outcome extractions distinguishable; no trial-wide conclusion change is established.

## C005 — Opposing directional readings of the hospital residual display

**Pending Human Adjudication**

**Candidate statement:** The index defines the named eFigure 1A residual as Expected minus Observed, while its signed plot and caption associate positive departures with higher hospital MACE and negative departures with lower MACE relative to the mean.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement p.1 index vs same REPORT p.24 eFigure 1A caption

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-505

**Qualifying route:** Route A, category 2

**Classification rationale:** The index defines a reported result and the figure presents that result in the same REPORT supplement, giving S_W/statistical_results. The main article corroborates the caption's reading and adds no S_C relationship. The label changes quantitative direction, rather than merely locating a figure.

**Classification ambiguity:** Document roles and relationship are clear; the exact residual reference, formula and scale are undefined, leaving a bounded interpretive ambiguity.

**Exact source locations:** REPORT [joi170166supp3_prod.pdf — p.1, eFigure 1A index entry](../joi170166supp3_prod.pdf#page=1); REPORT [joi170166supp3_prod.pdf — p.24, eFigure 1A signed axis, points and complete caption](../joi170166supp3_prod.pdf#page=24). Supporting REPORT context: [jama_huffman_2018_oi_170166.pdf — p.9, site heterogeneity narrative](../jama_huffman_2018_oi_170166.pdf#page=9).

**Source evidence:** Index wording assigns Expected–Observed to the residual of 30-day MACE by hospital. The graph has clearly negative left-side and positive right-side values, axis ticks −3, −2, −1, 0, 1, 2 and a hospital-rank x-axis. Caption describes modeled hospital departures from mean MACE, residual zero as reference, left lower/right higher than mean, and intervals excluding zero as differing from mean at 5%. Main p.9 describes site event rate relative to the trial mean.

**Reported-versus-comparator:** The index subtraction order and caption sign-to-hospital-rate interpretation give opposing readings under a common expected/reference quantity and scale. Exact individual hospital coefficients, expected/observed pairs and confidence limits are not printed.

**Reasoning procedure:** Match the exact named primary-outcome figure, read its signed axis and caption, and apply the index's literal subtraction order. Assess the protected quantity-changing-label comparison before treating an index entry as peripheral. Separate the observed printed definitions from the assumption that expected equals the caption's mean on the same scale.

**Calculation:** For r=E−O, O>E gives r<0 and O<E gives r>0. The caption associates positive r with above-mean MACE and negative r with below-mean MACE. This is a logical direction comparison; no pixel-derived decimal hospital estimate is used. Half-unit intervals and a relative magnitude discrepancy cannot be formed truthfully without exact printed ordinates or paired values.

**Affected result or extracted value:** Whether positive/negative hospital residuals indicate MACE above/below the expected/reference rate, including interpretation of hospital intervals excluding zero. The trial-wide intervention OR is not reversed by this observation.

**Why context does not resolve it:** Route A, category 2 covers quantity-defining direction/reference statements reversing a displayed reading. Choosing the caption does not reconcile the competing index definition; this is more than a pointer or interchangeable wording.

**Alternative source-grounded interpretations:** The plotted result could be a hospital random effect or predicted departure on a model scale, while the index describes a distinct expected-minus-observed residual. Expected could differ from the trial-mean reference. The caption's mixed-logistic predicted-rate context supports these alternatives, but no exact formula, subtraction order, reference definition, probability/log-odds scale or hospital-specific values is supplied to distinguish them.

**Mechanical evidence recheck:** The source-confirmed index, caption and graph signs reproduce the competing directional descriptions; main p.9 corroborates one side. No hospital ID, value or event count was digitized, and no transcription adjustment was required. S_W/statistical_results was confirmed. Audit recognized the initial cross-source excluded observation as already represented by this candidate and confirmed inclusion. See [combined recheck, C005](review_1_6_2/verification/evidence_recheck.md#c005--opposing-directional-readings-of-the-named-hospital-residual-display).

**Potential downstream evidence impact:** If confirmed, an extractor or reader could interpret the same hospital departure as above or below its reference according to the chosen printed definition. Formula/reference clarification could support direction extraction from this plot; no change to the overall intervention effect or downstream decision is established.

## C006 — LDL interval versus the same-display reproducing calculation

**Pending Human Adjudication**

**Candidate statement:** The LDL confidence limits in eTable 1 do not reproduce, beyond display precision, under a pooled mean-difference calculation that reproduces the five other same-display mean/SD rows. LDL-specific contributor counts and its actual interval procedure are not supplied.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement p.17 eTable 1 LDL row vs same-display mean/SD rows

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-501

**Qualifying route:** Route A, category 4

**Classification rationale:** The substantive numbers and comparator rows are in the same REPORT table, giving S_W/statistical_results. This is a within-display reproducing-method check, rather than a peripheral cross-document baseline-copy comparison or adjusted-versus-crude treatment-effect comparison.

**Classification ambiguity:** None

**Exact source locations:** REPORT [joi170166supp3_prod.pdf — p.17, eTable 1 complete/missing follow-up headers, LDL row, age, weight, systolic-pressure, heart-rate and hemoglobin rows](../joi170166supp3_prod.pdf#page=17).

**Source evidence:** Table headers give complete follow-up n=21,079 and missing follow-up n=295. LDL means/SDs are 122.4 (40.8) and 131.4 (46.0) mg/dL, with missing-minus-complete difference 9.0 and 95% CI 3.2–14.8. Actual LDL assay contributors and the CI procedure are absent. These groups are follow-up groups, not randomized arms.

**Reported-versus-comparator:** The printed LDL interval is compared with the explicitly stated same-display calculation below. Its five supporting mean/SD rows are preserved:

| Characteristic | Complete mean (SD) | Missing mean (SD) | Printed difference (95% CI) |
|---|---|---|---|
| Age, years | 60.6 (12.1) | 60.0 (11.6) | −0.6 (−2.0 to 0.8) |
| Weight, kg | 63.5 (9.7) | 62.6 (9.3) | −0.9 (−2.0 to 0.2) |
| Systolic pressure, mmHg | 138.5 (28.9) | 138.9 (32.5) | 0.4 (−2.9 to 3.7) |
| Heart rate, bpm | 79.9 (18.9) | 82.9 (19.1) | 3.0 (0.8 to 5.2) |
| Hemoglobin, source label mg/dl | 13.2 (2.0) | 13.2 (2.1) | 0.0 (−0.3 to 0.2) |
| LDL, mg/dl | 122.4 (40.8) | 131.4 (46.0) | 9.0 (3.2 to 14.8) |

**Reasoning procedure:** Use the printed complete/missing group totals provisionally, set d=meanMissing−meanComplete, and evaluate pooled variance v=((nC−1)sC²+(nM−1)sM²)/(nC+nM−2), standard error SE=√[v(1/nC+1/nM)], endpoints d±1.96SE. This normal-approximation calculation is a diagnostic supported by reproduction of the other same-display rows, not a claim about the actual LDL-generating method or a preferred analysis. Then allow all displayed inputs and limits their half-unit rounding intervals.

**Calculation:** At printed LDL inputs, d=9.0, SE=2.3964893360, endpoints 4.3028809014–13.6971190986. The point difference reconciles: input difference range [8.90,9.10] overlaps printed 9.0's [8.95,9.05]. Means and SDs take ±0.05, while group headers conservatively take ±0.5: nC∈[21078.5,21079.5], nM∈[294.5,295.5]; LDL mean/SD intervals are [122.35,122.45], [40.75,40.85], [131.35,131.45], [45.95,46.05]. The recheck evaluated all 64 six-input corners; monotonicity of d and SE on these ranges supports their endpoint bounds. Fractional count intervals are conservative rather than asserted patient counts.

| Characteristic | Endpoints at printed inputs | Full lower-limit range | Full upper-limit range | Printed lower-limit interval | Printed upper-limit interval |
|---|---|---|---|---|---|
| Age | −1.98965319, 0.78965319 | [−2.09656791,−1.88275104] | [0.68275104,0.89656791] | [−2.05,−1.95] | [0.75,0.85] |
| Weight | −2.01402075, 0.21402075 | [−2.12070452,−1.90734897] | [0.10734897,0.32070452] | [−2.05,−1.95] | [0.15,0.25] |
| Systolic pressure | −2.92697797, 3.72697797 | [−3.03550242,−2.81847022] | [3.61847022,3.83550242] | [−2.95,−2.85] | [3.65,3.75] |
| Heart rate | 0.82785750, 5.17214250 | [0.72028958,0.93541117] | [5.06458883,5.27971042] | [0.75,0.85] | [5.15,5.25] |
| Hemoglobin | −0.22998469, 0.22998469 | [−0.33592720,−0.12405228] | [0.12405228,0.33592720] | [−0.35,−0.25] | [0.15,0.25] |
| LDL | 4.30288090, 13.69711910 | [4.19321414,4.41252805] | [13.58747195,13.80678586] | [3.15,3.25] | [14.75,14.85] |

Age, weight, systolic pressure and heart-rate endpoints reproduce at printed inputs. Hemoglobin permits a jointly feasible mean difference −0.05 within its displayed means and point interval, giving endpoints approximately −0.27998469 and 0.17998469 that match both printed-limit intervals. All five comparator rows have zero gap after precision. LDL's closest lower gap is 4.1932141427−3.25=0.9432141427, relative discrepancy 0.9432141427/3.2=0.2947544196. Its upper gap is 14.75−13.8067858573=0.9432141427, relative discrepancy 0.9432141427/14.8=0.0637306853. Both exceed 0.05; restricting counts to exact integers does not bridge these conservative gaps.

**Affected result or extracted value:** The baseline LDL missing-minus-complete 95% CI of 3.2–14.8 mg/dL. The point estimate, interval containment and endpoint order reconcile.

**Why context does not resolve it:** Route A, category 4 covers a printed result not reproduced beyond display precision by a method reproducing other rows of the same display. The unprovided producing counts/method remain the substantive missing definition rather than making this a conditional method preference.

**Alternative source-grounded interpretations:** Fewer LDL assay contributors than the group headers could widen the interval; a distinct interval procedure, variance estimator or degrees of freedom could also account for it. The table supplies no variable-specific assay counts or generating procedure, and does not say that every participant contributed LDL. The displayed Ns are reproduction inputs, not established assay Ns. No replacement interval is proposed.

**Mechanical evidence recheck:** The full table, all six mean/SD rows and printed limits were visually matched. Independent calculation reproduced the five comparator rows and conservative LDL precision gaps without a transcription amendment. S_W/statistical_results was confirmed; audit independently repeated the interval calculation and confirmed inclusion. See [combined recheck, C006](review_1_6_2/verification/evidence_recheck.md#c006--ldl-interval-differs-from-the-same-display-reproducing-calculation).

**Potential downstream evidence impact:** If confirmed, an extractor could copy the LDL follow-up-group interval without its necessary contributor-count or interval-method context. Clarification could support descriptive interval extraction; this does not establish an effect on trial treatment-effect conclusions.

## C007 — Planned complete-case primary-MACE sensitivity result is not identified

**Pending Human Adjudication**

**Candidate statement:** The SAP explicitly prescribes a complete-case sensitivity analysis for missing primary-outcome data, but the supplied REPORT materials do not identify its primary 30-day MACE result or map an existing reported analysis to it. Whether it was performed is not established by this reporting comparison.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP pp.6,7 vs REPORT main pp.3,6,7 and results supplement pp.17,21,22,23

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST2-501

**Qualifying route:** Route A, category 5

**Classification rationale:** The comparison is the prospective PLAN complete-case primary-outcome specification versus the identifiable REPORT analyses. Multiple REPORT documents jointly establish that side without conflicting with one another, adding no S_C or S_W; SAP context adds no P_P. P_R therefore gives protocol_report.

**Classification ambiguity:** None

**Exact source locations:** PLAN [joi170166supp2_prod.pdf — p.6, §7.1 lines 1190–1198 and §7.2 lines 1205–1210](../joi170166supp2_prod.pdf#page=6); PLAN [joi170166supp2_prod.pdf — p.7, §7.5 lines 1229–1238](../joi170166supp2_prod.pdf#page=7); REPORT [jama_huffman_2018_oi_170166.pdf — p.3, Outcomes and Statistical Analysis](../jama_huffman_2018_oi_170166.pdf#page=3); REPORT [jama_huffman_2018_oi_170166.pdf — p.6, follow-up paragraph](../jama_huffman_2018_oi_170166.pdf#page=6); REPORT [jama_huffman_2018_oi_170166.pdf — p.7, Table 3 primary row, footnote a and Primary Analysis](../jama_huffman_2018_oi_170166.pdf#page=7); REPORT [joi170166supp3_prod.pdf — p.17, eTable 1](../joi170166supp3_prod.pdf#page=17); REPORT [joi170166supp3_prod.pdf — p.21, eTable 5 primary row and analysis labels](../joi170166supp3_prod.pdf#page=21); REPORT [joi170166supp3_prod.pdf — p.22, eTable 6 primary row and analysis labels](../joi170166supp3_prod.pdf#page=22); REPORT [joi170166supp3_prod.pdf — p.23, eTable 7 title, rows and footnotes](../joi170166supp3_prod.pdf#page=23). Additional supporting context: REPORT [jama_huffman_2018_oi_170166.pdf — p.4, Figure 1 caption](../jama_huffman_2018_oi_170166.pdf#page=4).

**Source evidence:** SAP §7.1 applies missing-data methods to primary/secondary endpoints; §7.2 explicitly names complete-case and multiple-imputation sensitivity analyses. SAP p.7 identifies primary 30-day MACE and the hospital/time mixed-logistic model. The report describes intention-to-treat results, missing follow-up, multiple imputation and hypothetical missing-event scenarios, without identifying a complete-case primary-MACE result. Figure 1 says lost-follow-up participants were included in analysis, but does not specify missing-outcome coding or populations for individual models.

**Reported-versus-comparator:** Primary MACE is control 645 (6.4%) versus intervention 602 (5.3%), with arm headers 10,066 and 11,308. Primary OR is 0.98 (95% CI 0.80–1.21), difference −0.09 percentage points (−1.32 to 1.14). Main p.7 reports similar results after multiple imputation and a broader range of plausible hypothetical-scenario results. eTable 1 describes complete/missing follow-up (21,079/295), not a treatment effect. eTable 5 labels four covariate sensitivities, primary ORs 1.06 (0.77–1.44), 0.98 (0.80–1.21), 0.97 (0.79–1.20), 0.99 (0.80–1.22). eTable 6 labels an exposure-time interaction, OR 1.14 (0.76–1.70). eTable 7 labels an expanded composite, OR 0.84 (0.70–1.00), difference −1.34 (−2.72 to 0.04). None names or supplies a definition mapping its result to the planned complete-case primary sensitivity.

**Reasoning procedure:** Link the SAP's missing-data provision to the primary endpoint, then inspect all supplied REPORT text and every results display for a matching result-to-method identity. Complete main and results-supplement searches considered complete-case/available-case/observed-case, case deletion, missing, imputation, sensitivity, hypothetical and lost-follow-up language. The supplement's REPORT index and pp.17–27 were source-inspected; its operational PLAN pp.2–16 cannot identify a completed trial sensitivity result. Absence is bounded to this supplied package.

**Calculation:** The categorical method set in the SAP is {complete-case, multiple imputation}; report sensitivity text names imputation and hypothetical event scenarios without a complete-case designation or mapping. No complete-case numerical estimate exists for a half-unit or relative-discrepancy comparison. Contextual integer identities reconcile: 215+80=295 missing outcomes; 21,079+295=21,374; 10,066+11,308=21,374. These identities do not identify arm-specific complete-case denominators, outcome availability, model inclusion or a complete-case effect; none is reconstructed.

**Affected result or extracted value:** Availability, identity and contributing population of the planned complete-case sensitivity for the primary 30-day MACE intervention effect, alongside the printed primary OR and difference.

**Why context does not resolve it:** Route A, category 5 covers a planned primary or key-secondary analysis without an identified reported counterpart. Intention-to-treat wording, full-cohort headers, baseline follow-up summaries and similar-imputation language do not establish the planned complete-case result-to-method mapping.

**Alternative source-grounded interpretations:** The primary model may already implement complete-case analysis while descriptive cohort statements retain the full cohort; an unspecified hypothetical scenario may implement it; or the analysis may have been replaced or deferred. Missing definitions are the designated result, completeness rule, contributing population, primary-model missing-outcome coding, hypothetical-scenario definitions, mapping to an existing result, and any documentation of replacement/deferral. None of these alternatives is established, and the reporting observation does not assert that the analysis was unperformed or that its estimate would differ.

**Mechanical evidence recheck:** A different fresh appended rechecker visually reread all nine registered pages and the additional flow caption, matched source statements and quantitative context, and independently searched complete supplied REPORT text. The missing result/mapping comparison reproduced with no transcription amendment; P_R/protocol_report was retained. The audit confirmed the specific Route A category 5 issue while retaining general unreported implementation details as exclusions. See [appended recheck](review_1_6_2/verification/evidence_recheck_appended.md) and the lossless [combined recheck](review_1_6_2/verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, an extractor could omit a planned primary missing-data sensitivity or attribute an existing estimate to complete-case analysis without a supplied mapping. Identifying its result/population could support assessment of sensitivity evidence; no numerical shift, conclusion change or downstream decision is established.

## Downstream Evidence-Chain Considerations

Quantitative extraction connects a reported number with an outcome definition, population, time, model, scale, direction and prospective status. If a candidate is confirmed, the associated ambiguity or discrepancy could affect which number is copied or which meaning is attached to it in a systematic review, meta-analysis, guideline evidence table or other synthesis. The cards identify the specific bounded extraction implication rather than assuming an evidence-chain consequence has occurred.

The package establishes neither actual downstream copying nor a change to a synthesis, guideline or trial conclusion. The medication, expanded-MACE and subgroup issues concern endpoint/analysis definitions and status; the time/residual issues concern quantity mapping and direction; the LDL issue concerns a descriptive interval; and the complete-case issue concerns identifiable sensitivity evidence. These distinct implications should remain connected to their source definitions and alternatives.

## Limitations and Missing Definitions

Every direct-source page and registered relationship was covered. Remaining limitations concern the supplied evidence's granularity and definitions rather than scientific coverage. The [limitations artifact](review_1_6_2/limitations.md) records these in full.

| Candidate or scope | Missing definition or bounded limitation |
|---|---|
| C001 | Dated medication-composite amendment, statin observations, five-component eligibility set, counts and result are absent. |
| C002 | Prospective expanded-MACE component identity, analysis specification and any later amendment are absent. |
| C003 | Dated specification for revised age groups/hospital type and toolkit-use primary-MACE result or replacement/deferral mapping are absent. |
| C004 | Column-specific time estimand, quantile, scale, model, adjustment/marginalization and population mapping are absent. |
| C005 | Residual formula, subtraction order, expected-versus-mean reference, scale and exact hospital values are absent. |
| C006 | LDL assay contributor counts, row-specific missingness and generating interval/variance/degree-of-freedom procedure are absent. |
| C007 | Complete-case primary result, completeness/inclusion rule, contributing population, missing-outcome coding and mapping to primary or hypothetical-scenario results are absent. |
| Graphs | Exact hospital identifiers, rates, endpoints, events and denominators are unprinted; visual checks did not create decimal values from pixels. |
| Other reproduction | Exact restricted medication/smoker denominators, anticipated cluster-period power inputs and unreported model internals constrain reconstruction without independently establishing a candidate. |
| Tooling | Direct OCR and Office conversion were unavailable; all sources are PDFs and source-matched OCR/native text plus CPU visual inspection covered every page. No new OCR, Office conversion or fallback installation was needed. |

The review used only supplied package evidence. It did not inspect external publications, code or raw data; unsupplied amendments and separate process-evaluation reports cannot resolve a candidate here. Diagnostic calculations retain their stated assumptions and do not identify an unprovided producing analysis. Reproduction and CONFIRMED inclusion remain distinct from final human adjudication.

## Reproducibility, Source-Integrity, Agent-Execution, and Performance Metadata

### Reproducibility and source integrity

The [routing preflight](review_1_6_2/routing_preflight.md) records PASS, run model gpt-6.1-sol with DEFAULT source, INTERACTIVE_CLI, CURRENT_SESSION provider and verified ten named role presets. All specialists were fresh distinct runtimes; high-effort statistical passes used separate main/support runtime pairs. Every actual runtime, including coordinator and this report generator, is recorded once below and in the [execution manifest](review_1_6_2/agent_execution_manifest.md).

Direct local tooling used file, pdfinfo, pdftotext and pdftoppm/pdftocairo with Poppler 25.03.0, SHA-256 tools, and supplied source-matched reusable OCR. Current extraction and rendering ran on CPU; historical derivative engine/device metadata remains separately recorded in the [evidence-asset inventory](review_1_6_2/evidence_asset_inventory.md). No temporary fallback environment was created. The [tooling record](review_1_6_2/tooling_record.md) documents available tools and coverage of missing capabilities.

Final after-review SHA-256 recomputation matches all four source baselines and all 82 reused-asset baselines byte for byte. The [source after-hash record](review_1_6_2/source_hashes_after.sha256) and [reused-asset after-hash record](review_1_6_2/reused_artifact_hashes_after.sha256) preserve the comparisons. The standalone HTML uses embedded CSS and a table of contents. No fallback environment was created; final cleanup confirmation is recorded in the tooling record. The mechanical validator outcome is recorded in [review_validation.json](review_1_6_2/review_validation.json).

Durable evidence maps are the [main map](review_1_6_2/extraction/main_quantitative_evidence.md), [canonical support map](review_1_6_2/extraction/support_quantitative_evidence.md), and its disjoint [plan part](review_1_6_2/extraction/support_plan_evidence.md) and [results part](review_1_6_2/extraction/support_results_evidence.md). Stable candidate provenance and classifications are in the [ledger](review_1_6_2/candidate_ledger.md), [screening log](review_1_6_2/screening/inclusion_screen.md), [combined recheck](review_1_6_2/verification/evidence_recheck.md), and [quality audit](review_1_6_2/quality/evidence_quality_audit.md). Every source-PDF evidence link uses an actual filename and physical page anchor.

### Agent execution

| Stage | Agent ID | Model | Reasoning effort | Start mode | Primary durable artifact |
|---|---|---|---|---|---|
| coordinator | task:/root | gpt-6.1-sol | high | CURRENT_SESSION | run_state.md |
| reuse_asset_curator | task:/root/reuse_curator | gpt-6.1-sol | medium | FRESH_SPAWN | source_inventory.md |
| main_quantitative_mapper | task:/root/main_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/main_quantitative_evidence.md |
| support_quantitative_mapper | task:/root/support_mapper | gpt-6.1-sol | medium | FRESH_SPAWN | extraction/support_quantitative_evidence.md |
| numeric_consistency_reviewer | task:/root/numeric_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/numeric_consistency.md |
| cross_source_consistency_reviewer | task:/root/cross_checker | gpt-6.1-sol | medium | FRESH_SPAWN | checkers/cross_source_consistency.md |
| statistics_pass_1 | task:/root/stat1_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_1.md |
| statistics_pass_1_support_shard | task:/root/stat1_support | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_1_support.md |
| inclusion_screener | task:/root/initial_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen.md |
| evidence_rechecker | task:/root/evidence_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck.md |
| statistics_pass_2 | task:/root/stat2_main | gpt-6.1-sol | high | FRESH_SPAWN | checkers/statistical_pass_2.md |
| statistics_pass_2_support_shard | task:/root/stat2_support | gpt-6.1-sol | high | FRESH_SPAWN | checkers/parts/statistical_pass_2_support.md |
| inclusion_screener_pass_2 | task:/root/pass2_screener | gpt-6.1-sol | high | FRESH_SPAWN | screening/inclusion_screen_pass_2.md |
| evidence_rechecker_appended | task:/root/appended_recheck | gpt-6.1-sol | high | FRESH_SPAWN | verification/evidence_recheck_appended.md |
| quality_control_auditor | task:/root/quality_auditor | gpt-6.1-sol | high | FRESH_SPAWN | quality/evidence_quality_audit.md |
| report_generator | task:/root/report_generator | gpt-6.1-sol | medium | FRESH_SPAWN | limitations.md |

Artifact paths in this table are relative to review_1_6_2/. The API exposes canonical runtime task names; task: identifies that transport namespace. All 16 returned canonical names are distinct, with exactly one row per actual runtime. The main/support statistical shards are disjoint and jointly complete at each pass. Model and reasoning-effort values are copied from the execution manifest.

### Reproducibility performance

- **Target basis:** Four PDF sources with 80 pages, 69 reusable-backed and 11 requiring fresh visual mapping after current-source fitness checks, no Office conversion or new OCR expected; mixed plan and result content plus numerous main and supplementary tables require parallel mapping, concurrent checks, two independent statistical passes, screening, recheck, audit and report waves. Native plus reusable OCR input fits two mapping lanes.
- **Total source units:** 80
- **Fresh-source units:** 11
- **Target elapsed minutes:** 30-45
- **Started UTC:** 2026-10-11T06:39:56Z
- **Finished UTC:** 2026-10-11T07:51:20Z
- **Observed elapsed minutes:** 71.40
- **Target status:** EXCEEDED_TARGET
- **Exceedance causes:** Pass 2 identified an additional planned primary-outcome sensitivity analysis without an identified reported counterpart, requiring a different fresh inclusion screen and appended evidence recheck; complete fresh audit and report stages followed without reducing source or relationship coverage.

These exact finalized performance fields match the [run state](review_1_6_2/run_state.md). Finished UTC was recorded immediately after complete Markdown assembly. Local rendering and mechanical validation are outside that observed review window; any model-based repair after that time requires updated timing.
