# Workflow 1.6.2 Candidate Ledger

Pending Human Adjudication

The independent initial screen included 19 findings consolidated into 11 issues. Stable IDs are assigned in the screener's source order, with earliest conflicting source/page first. All compared locations and checker provenance are preserved below. The fresh rechecker reproduced all eleven issues, and the independent auditor confirmed inclusion for each. Classification and evidence fields are final for this review; all assigned IDs remain pending human adjudication.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | REPORT main article pp. 1-2 and results supplement p. 4 vs PLAN protocol pp. 8, 18, 20, 23 | reproduced | CONFIRMED | F-NUM-002, F-XS-002 |
| C002 | protocol_report | P_R | P_R, P_P | PLAN protocol p. 43 vs PLAN SAP pp. 2-4 and REPORT main article pp. 1, 4, 6, 8 | reproduced | CONFIRMED | F-XS-005, F-ST1-004 |
| C003 | statistical_results | S_C | S_C, S_W | REPORT main article pp. 1-3 vs REPORT results supplement p. 3 | reproduced | CONFIRMED | F-XS-001 |
| C004 | statistical_results | S_W | S_W | REPORT main article p. 4 sample-size total vs four factorial cell counts in the same paragraph | reproduced | CONFIRMED | F-NUM-001, F-ST1-001 |
| C005 | protocol_report | P_R | P_R | REPORT main article p. 4 vs PLAN protocol pp. 16-17 | reproduced | CONFIRMED | F-XS-003, F-ST1-002 |
| C006 | protocol_report | P_R | P_R, P_P | PLAN protocol pp. 8-9, 28, 43 vs PLAN SAP p. 2 and REPORT main article pp. 4, 8 | reproduced | CONFIRMED | F-XS-004, F-ST1-003 |
| C007 | protocol_report | P_R | P_R, S_W | PLAN protocol pp. 43-44 and SAP pp. 4-5 vs REPORT main article pp. 4, 6-8 and results supplement pp. 18-20 | reproduced | CONFIRMED | F-XS-006, F-XS-007, F-ST1-005 |
| C008 | protocol_report | P_R | P_R | PLAN SAP p. 4 vs REPORT main article pp. 4, 6-7 and results supplement pp. 18-22 | reproduced | CONFIRMED | F-XS-008, F-ST1-006 |
| C009 | protocol_report | P_R | P_R | PLAN SAP p. 5 vs REPORT main article pp. 4, 6, 8 and results supplement pp. 21-22 | reproduced | CONFIRMED | F-ST1-010 |
| C010 | statistical_results | S_C | S_C, S_W | REPORT main article pp. 6, 8 vs REPORT results supplement pp. 15-16, 22 | reproduced | CONFIRMED | F-ST1-007 |
| C011 | statistical_results | S_W | S_W | REPORT results supplement p. 19 Table B site rows vs its other six nonreference rows | reproduced | CONFIRMED | F-ST1-008 |

## C001 — Planned and reported daily EPA+DHA dose does not reconcile

**Candidate statement:** Planned and reported daily EPA+DHA dose does not reconcile.

**Registration key:** OMEGA_DOSE

**OMEGA_DOSE — F-NUM-002, F-XS-002.** Domain `protocol_report`; primary/all relationships `P_R`; route B. Earliest conflicting source DOC-001 p1. REPORT [main p1 abstract](../../jama_bot_2019_oi_190007.pdf#page=1), [p2 interventions](../../jama_bot_2019_oi_190007.pdf#page=2), and [results supplement p4 eAppendix 2](../../joi190007supp3_prod.pdf#page=4) all state the reported 1412 mg daily dose; PLAN [protocol p8 summary](../../joi190007supp1_prod.pdf#page=8), [p18 intervention box](../../joi190007supp1_prod.pdf#page=18), [p20 manufacturing allowance](../../joi190007supp1_prod.pdf#page=20), and [p23 explicit EPA+DHA 1.0 g/day](../../joi190007supp1_prod.pdf#page=23) establish the planned side. The concordant REPORT occurrences do not create an S_C conflict. Conservative recomputed PLAN interval is [950,1050] mg versus REPORT [1411.5,1412.5] mg, gap 361.5/1412 = 0.256020; even generously applying the rounded maximum allowance 1.255 gives 1317.75 mg, residual 93.75/1412 = 0.066395. Exposure dose for the primary MDD results is the affected value; a dose amendment or a different composition basis remains a human question.

**Classification rationale:** Prospective protocol dose specifications differ from retrospective article and results-supplement exposure descriptions; the concordant report copies are corroboration, so only P_R applies.

**Classification ambiguity:** None

**Status:** Pending Human Adjudication

## C002 — Planned primary analysis suite is replaced or not reported as specified

**Candidate statement:** Planned primary analysis suite is replaced or not reported as specified.

**Registration key:** PRIMARY_ANALYSIS_SUITE

**PRIMARY_ANALYSIS_SUITE — F-XS-005, F-ST1-004.** Domain `protocol_report`; primary relationship `P_R`; all relationships `P_R, P_P`; route A, category 5. PLAN [protocol p43 sections 10.1–10.2](../../joi190007supp1_prod.pdf#page=43), [SAP p2 primary outcome](../../joi190007supp2_prod.pdf#page=2), [p3 fourth analysis](../../joi190007supp2_prod.pdf#page=3), and [p4 secondary Cox](../../joi190007supp2_prod.pdf#page=4), compared with REPORT [main p1 model](../../jama_bot_2019_oi_190007.pdf#page=1), [p4 methods](../../jama_bot_2019_oi_190007.pdf#page=4), [p6 Table 2](../../jama_bot_2019_oi_190007.pdf#page=6), and [p8 Table 3](../../jama_bot_2019_oi_190007.pdf#page=8). The protocol-designated Kaplan–Meier/log-rank/four-way and repeated-MDD models are not supplied as such; logistic cumulative MDD replaces the specified primary survival suite and GEE/robust-linear symptom inference replaces the protocol primary mixed-model IDS specification, although the SAP allows mixed models or GEE. No claim is made that site adjustment cannot implement country adjustment or that GEE itself conflicts with the SAP. The governing prespecified primary analysis is the affected interpretation; Cox status itself belongs to PLANNED_POST_HOC.

**Classification rationale:** The prospective protocol and SAP specify different primary analysis suites, and the retrospective report differs from the protocol suite; P_R takes precedence over the additional P_P relationship.

**Classification ambiguity:** The governing sequence of the supplied protocol and undated SAP is not established; content-based document roles are clear.

**Status:** Pending Human Adjudication

## C003 — Online-screening BMI cutoff differs between report locations

**Candidate statement:** Online-screening BMI cutoff differs between report locations.

**Registration key:** BMI_FLOW

**BMI_FLOW — F-XS-001.** Domain `statistical_results`; primary relationship `S_C`; all relationships `S_C, S_W`; route A, category 2. Earliest conflicting source DOC-001 p3, with the population range corroborated in DOC-001 pp1–2. REPORT [main p3 Figure 1](../../jama_bot_2019_oi_190007.pdf#page=3) prints BMI <15 or >40 for 1451 online exclusions, versus REPORT [results supplement p3 online inclusion criteria](../../joi190007supp3_prod.pdf#page=3) explicitly assigning BMI 25–40 to the online-screening tool and REPORT [main p2 eligibility](../../jama_bot_2019_oi_190007.pdf#page=2)/[p1 abstract](../../jama_bot_2019_oi_190007.pdf#page=1) defining BMI 25–40. The half-unit interval gap [14.5,15.5] versus [24.5,25.5] is 9/25 = 0.36. The PLAN [protocol p16](../../joi190007supp1_prod.pdf#page=16) merely corroborates 25 and does not create P_R. The same-stage statement in the results appendix establishes reproduction; an intentional looser initial screen followed by 18 BMI <25 telephone exclusions remains an alternative but would itself need reconciliation with that explicit same-stage description. This is a printed numeric cutoff changing the represented participant-flow count, distinct from general recruitment eligibility differences in F-XS-009.

**Classification rationale:** The participant-flow cutoff conflicts across two REPORT documents and within the article; S_C takes precedence over S_W. The concordant protocol cutoff merely corroborates one side.

**Classification ambiguity:** None

**Status:** Pending Human Adjudication

## C004 — Sample-size total does not reconcile with four stated cell sizes

**Candidate statement:** Sample-size total does not reconcile with four stated cell sizes.

**Registration key:** COUNT_TOTAL

**COUNT_TOTAL — F-NUM-001, F-ST1-001.** Domain `statistical_results`; primary/all relationships `S_W`; route A, category 3, with category 2 as additional support. REPORT [main p4 Sample Size](../../jama_bot_2019_oi_190007.pdf#page=4) contains both sides. Four cells at 196 yield [782,786] versus printed total [391.5,392.5], gap 389.5/392 = 0.993622. The 22% attrition/250-per-cell continuation supports a possible factor-level interpretation of 392 but does not remove a printed count conflict. The required total underlying primary-MDD power is the affected extracted value; no replacement total is assigned.

**Classification rationale:** The total and four cell counts occur in one paragraph of one REPORT document, establishing S_W and a counts-focused statistical_results domain.

**Classification ambiguity:** None

**Status:** Pending Human Adjudication

## C005 — Primary power assumptions differ between the protocol and report

**Candidate statement:** Primary power assumptions differ between the protocol and report.

**Registration key:** POWER_INPUTS

**POWER_INPUTS — F-XS-003, F-ST1-002.** Domain `protocol_report`; primary/all relationships `P_R`; route B. REPORT [main p4 Sample Size](../../jama_bot_2019_oi_190007.pdf#page=4) versus PLAN [protocol p16 calculation](../../joi190007supp1_prod.pdf#page=16) and [p17 continuation](../../joi190007supp1_prod.pdf#page=17). Active MDD incidence 15% PLAN versus 20% REPORT leaves [14.5,15.5]% versus [19.5,20.5]%, gap 4/20 = 0.20; 180 versus 196 per-group counts leave gap 15/196 = 0.076531 (also 15/180 = 0.083333). The 20% versus 22% attrition difference alone is not a reproduced quantitative discrepancy under the display rule and must not become a separate claim. The protocol's separate 25% wording and factorial/additive context remain alternatives requiring the operative power specification; diagnostic two-proportion calculations are not evidence of a particular algorithm. This issue concerns planned versus reported primary-MDD effect and sample assumptions, distinct from the internal four-cell total identity.

**Classification rationale:** The prospective protocol and retrospective article give different primary power inputs, establishing P_R and protocol_report.

**Classification ambiguity:** None

**Status:** Pending Human Adjudication

## C006 — Prespecified outcome hierarchy differs across plan and report materials

**Candidate statement:** Prespecified outcome hierarchy differs across plan and report materials.

**Registration key:** OUTCOME_HIERARCHY

**OUTCOME_HIERARCHY — F-XS-004, F-ST1-003.** Domain `protocol_report`; primary relationship `P_R`; all relationships `P_R, P_P`; route A, category 5. REPORT [main p4 outcome hierarchy](../../jama_bot_2019_oi_190007.pdf#page=4) and [p8 Table 3](../../jama_bot_2019_oi_190007.pdf#page=8) versus PLAN [protocol p8–9 main parameters](../../joi190007supp1_prod.pdf#page=9), [p28 sections 8.1.1–8.1.2](../../joi190007supp1_prod.pdf#page=28), [p43 primary parameter analyses](../../joi190007supp1_prod.pdf#page=43), and [SAP p2 Outcomes](../../joi190007supp2_prod.pdf#page=2). IDS main/primary versus secondary is explicit and independently sufficient; GAD/utility SAP Other versus protocol/report secondary is retained with the alternative that Other is organizational wording. Categorical outcome status has no rounding calculation. No separate issue is created from the report's multiplicity-related advice to interpret secondary inference as exploratory.

**Classification rationale:** Outcome status conflicts between PLAN and REPORT and between the protocol and SAP; P_R takes precedence over P_P.

**Classification ambiguity:** The governing hierarchy across the supplied protocol and undated SAP is not established; content-based document roles are clear.

**Status:** Pending Human Adjudication

## C007 — Planned Cox and site/history analyses receive post hoc report designations

**Candidate statement:** Planned Cox and site/history analyses receive post hoc report designations.

**Registration key:** PLANNED_POST_HOC

**PLANNED_POST_HOC — F-XS-006, F-XS-007, F-ST1-005.** Domain `protocol_report`; primary relationship `P_R`; all relationships `P_R, S_W`; route A, category 5. One repeated reporting-status pattern covers PLAN [protocol p43 survival analysis](../../joi190007supp1_prod.pdf#page=43), [p44 country interactions](../../joi190007supp1_prod.pdf#page=44), [SAP p4 Cox and history/center specification](../../joi190007supp2_prod.pdf#page=4), [p5 interaction reporting](../../joi190007supp2_prod.pdf#page=5), versus REPORT [main p4 Outcomes/Methods](../../jama_bot_2019_oi_190007.pdf#page=4), [p6 Post Hoc Outcome](../../jama_bot_2019_oi_190007.pdf#page=6), [p7 Cox results](../../jama_bot_2019_oi_190007.pdf#page=7), [p8 collective post hoc moderation label](../../jama_bot_2019_oi_190007.pdf#page=8), and [supplement p18 moderation results](../../joi190007supp3_prod.pdf#page=18), [p19 GAD model](../../joi190007supp3_prod.pdf#page=19), [p20 utility-site model](../../joi190007supp3_prod.pdf#page=20). The main Methods distinguishes planned site/history from post hoc baseline severity while the Results collectively calls all three post hoc, yielding the additional S_W relationship. Baseline-severity analyses are not alleged to have been planned. The supplied undated SAP chronology and the intended scope of the collective post hoc wording remain alternatives; all Cox/site/history occurrences stay in one issue because the same prespecified-versus-post-hoc rule and reported designation recur.

**Classification rationale:** Prospective PLAN analyses receive post hoc REPORT labels, and the article Methods and Results differ internally about that status; P_R takes precedence over S_W.

**Classification ambiguity:** The supplied SAP chronology is not established; the intended scope of the collective post hoc label is retained as an alternative.

**Status:** Pending Human Adjudication

## C008 — Planned additive primary-outcome interaction result is not reported

**Candidate statement:** Planned additive primary-outcome interaction result is not reported.

**Registration key:** RERI_ABSENT

**RERI_ABSENT — F-XS-008, F-ST1-006.** Domain `protocol_report`; primary/all relationships `P_R`; route A, category 5. PLAN [SAP p4 Interaction of intervention strategies](../../joi190007supp2_prod.pdf#page=4), compared with REPORT [main p4 analysis](../../jama_bot_2019_oi_190007.pdf#page=4), [p6 primary interaction](../../jama_bot_2019_oi_190007.pdf#page=6), [p7 narrative](../../jama_bot_2019_oi_190007.pdf#page=7), [supplement pp18–20 moderation](../../joi190007supp3_prod.pdf#page=18), [p21 sensitivity](../../joi190007supp3_prod.pdf#page=21), and [p22 CACE](../../joi190007supp3_prod.pdf#page=22). Full REPORT search/reread covers DOC-001 pp1–11, DOC-004 pp1–25 and DOC-005 p1. No RERI/additive primary-interaction result is supplied. The explicitly planned primary-outcome additive sensitivity is independent of the protocol survival suite and the primary missingness sensitivity; no crude additive estimate is invented.

**Classification rationale:** A prospective SAP primary-interaction commitment lacks its matching result in the complete supplied retrospective REPORT set, establishing P_R.

**Classification ambiguity:** None

**Status:** Pending Human Adjudication

## C009 — Planned primary-outcome missingness sensitivity is not reported

**Candidate statement:** Planned primary-outcome missingness sensitivity is not reported.

**Registration key:** PRIMARY_MISSINGNESS

**PRIMARY_MISSINGNESS — F-ST1-010.** Domain `protocol_report`; primary/all relationships `P_R`; route A, category 5. PLAN [SAP p5 Missing data and drop-out](../../joi190007supp2_prod.pdf#page=5) promises sensitivity after its primary-outcome 100-MI/MAR/Rubin specification, compared with REPORT [main p4 MI and sensitivity](../../jama_bot_2019_oi_190007.pdf#page=4), [p6 primary estimates](../../jama_bot_2019_oi_190007.pdf#page=6), [p8 sensitivity results](../../jama_bot_2019_oi_190007.pdf#page=8), [supplement p21 continuous-secondary no-MI sensitivity](../../joi190007supp3_prod.pdf#page=21), and [p22 MI-CACE](../../joi190007supp3_prod.pdf#page=22). Full REPORT search finds no primary-MDD missingness sensitivity result. The exact primary sensitivity model is not specified, and the possibility that the promise was intended only for secondary outcomes is retained as the human clarification; the printed promise is connected directly to primary imputation, so this is an absent planned primary analysis rather than merely an unreported optional model detail. No alternative missing-data analysis is recommended.

**Classification rationale:** A prospective SAP primary-imputation-context sensitivity commitment lacks its matching primary result in the complete supplied REPORT set, establishing P_R.

**Classification ambiguity:** None

**Status:** Pending Human Adjudication

## C010 — CACE explanation does not identify the mapping to the printed MDD estimates

**Candidate statement:** CACE explanation does not identify the mapping to the printed MDD estimates.

**Registration key:** CACE_MAPPING

**CACE_MAPPING — F-ST1-007.** Domain `statistical_results`; primary relationship `S_C`; all relationships `S_C, S_W`; route B. REPORT [main p6 original MDD ORs](../../jama_bot_2019_oi_190007.pdf#page=6), [p8 CACE narrative](../../jama_bot_2019_oi_190007.pdf#page=8), [supplement p15 ratio explanation](../../joi190007supp3_prod.pdf#page=15), [p16 therapy adherence](../../joi190007supp3_prod.pdf#page=16), and [p22 logistic CACE estimates and coding](../../joi190007supp3_prod.pdf#page=22). The explicitly printed original-effect/complier-proportion explanation fails to identify the mapping from the published MDD estimates to the CACE ORs: an ITT supplement OR in [1.055,1.065] cannot produce a CACE OR in [.835,.845] by dividing that OR or its positive log by a positive compliance proportion. The gap from the smallest original OR to largest CACE OR is .210/.84 = .25. The therapy log-OR/compliance diagnostic gives approximately [.89635,.91010] against printed [.775,.785], gap .11135/.78 = .1428; it is a diagnostic of the supplied explanation, not proof of the fitted SEM coefficient or compliance probability. The ratio may be a linear-outcome illustration rather than the logistic implementation, and CACE may use a different fitted numerator/model; those alternatives need a source-grounded mapping to explain the named ORs, so the retained human question concerns their method and scale rather than asserting the CACE values cannot arise from any model.

**Classification rationale:** The original-effect and CACE comparison crosses two REPORT documents, while the supplement explanation and table also require the same mapping; S_C takes precedence over S_W.

**Classification ambiguity:** None

**Status:** Pending Human Adjudication

## C011 — Three site coefficient and interval tuples do not reproduce the same-table relationship

**Candidate statement:** Three site coefficient and interval tuples do not reproduce the same-table relationship.

**Registration key:** SITE_CI_PATTERN

**SITE_CI_PATTERN — F-ST1-008.** Domain `statistical_results`; primary/all relationships `S_W`; route A, category 4. REPORT [results supplement p19 Table B](../../joi190007supp3_prod.pdf#page=19), three site coefficient/CI rows versus the six remaining nonreference rows in that same table. Spain printed B [.1065,.1075] versus midpoint [.0475,.0485] leaves gap .0580/.107 = .542056; UK [.1165,.1175] versus [.1330,.1340] leaves gap .0155/.117 = .132479; Germany [.0575,.0585] versus [.1020,.1030] leaves gap .0435/.058 = .750000. The centered relationship reproduces supplements, therapy, history, baseline GAD and both baseline interactions allowing each input its printed precision, including the coarser .17/.52 limits. All three site estimates lie inside their CIs and all their null decisions agree with P, but that does not remove the category-4 same-display calculation mismatch. An asymmetric or different-model interval construction remains the human question; no universal symmetry assumption or corrected endpoint is imposed. The peripheral-comparison exception does not remove a reproduced always-register within-display pattern.

**Classification rationale:** All compared coefficient and interval rows occur within one table in one REPORT document, establishing S_W and statistical_results.

**Classification ambiguity:** None

**Status:** Pending Human Adjudication
