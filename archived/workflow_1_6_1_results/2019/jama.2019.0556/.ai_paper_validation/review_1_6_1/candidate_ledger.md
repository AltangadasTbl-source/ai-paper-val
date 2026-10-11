# Workflow 1.6.1 Candidate Ledger

All candidates are Pending Human Adjudication. Five stable IDs are assigned only after independent inclusion screening. IDs follow the earliest substantive main-article anchor and paragraph order, as documented in screening/initial_working_notes.md. This is source order, not a ranking. Complete independent evidence and every affected occurrence are retained in that artifact and the cited checker records. The fresh direct-source recheck reproduced all five candidates and confirmed their classifications; the fresh audit recorded CONFIRMED for C001-C003 and QUESTIONED for C004-C005, with every stable ID retained.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | PLAN protocol pp.8,18,20,23 vs REPORT main pp.1,2 and results supplement pp.4,5 | reproduced | CONFIRMED | F-XS-002 |
| C002 | protocol_report | P_R | P_R, P_P | PLAN protocol p.43 vs PLAN SAP pp.3,4 and REPORT main pp.1,2,4,6,7 | reproduced | CONFIRMED | F-XS-003, F-ST1-002 |
| C003 | protocol_report | P_R | P_R | PLAN SAP p.4 vs REPORT main pp.1,4,6,7,8 and results supplement pp.21,22, with complete REPORT coverage | reproduced | CONFIRMED | F-XS-005 |
| C004 | protocol_report | P_R | P_R, P_P | PLAN protocol pp.9,28,43 vs PLAN SAP p.2 and REPORT main pp.4,8 | reproduced | QUESTIONED | F-XS-004, F-ST1-003 |
| C005 | protocol_report | P_R | P_R | PLAN protocol pp.16,17 vs REPORT main pp.4,9 | reproduced | QUESTIONED | F-XS-001, F-ST1-001 |

## C001 — Planned and reported daily EPA+DHA dose

Finding provenance: F-XS-002, cross_source_consistency_reviewer; independent initial screen INCLUDE.

The protocol explicitly specifies EPA+DHA 1.0 g/day; the main article and results supplement specify 1412 mg/day for the same one-year randomized supplement intervention. The difference is 412 mg/day (41.2%). The protocol's 125% upper manufacturing tolerance applied to 1000 mg yields 1250 mg, below 1412 mg. Other nutrients fall within the planned ranges.

Exact locations: DOC-002 joi190007supp1_prod.pdf pp.8 summary,18 treatment,20 tolerance,23 intended dose; DOC-001 jama_bot_2019_oi_190007.pdf pp.1 interventions,2 supplement intervention; DOC-004 joi190007supp3_prod.pdf pp.4 composition,5 testing. DOC-002 p.1 establishes the final-amendment protocol context.

Affected value: intervention-dose extraction attached to the multinutrient primary MDD OR 1.06 (0.87–1.29). The explicit EPA+DHA mass definition prevents immediate resolution as total capsule oil or ordinary tolerance. A revised formulation or retained earlier protocol wording could explain it, but no supplied amendment reconciles the daily masses. Laboratory FAME proportions are not used to reconstruct daily dose. REPORT occurrences agree; the conflict is P_R only. Classification ambiguity: amendment chronology is unavailable. Human question: what documented formulation change reconciles 1.0 g/day with 1.412 g/day?

## C002 — Primary MDD model priority and Cox prespecification

Finding provenance: F-XS-003, cross_source_consistency_reviewer; F-ST1-002, statistics_pass_1; both independent initial screen INCLUDE, consolidated as one issue.

Protocol primary-study-parameter analysis specifies Kaplan–Meier/log-rank/Cox time-to-event and mixed regression of MDD/IDS. SAP specifies primary cumulative-MDD logistic regression and secondary time-to-onset Cox regression. The article reports logistic regression as primary and repeatedly labels Cox post hoc. The reported model producing each number is clear; the prospective hierarchy/status does not reconcile across supplied specifications.

Exact locations: DOC-002 protocol p.43 §10.1; DOC-003 joi190007supp2_prod.pdf pp.3 primary logistic specification,4 secondary Cox specification; DOC-001 main pp.1 primary analysis,2 design links to protocol/SAP,4 outcomes/statistical methods,6 Table 2,7 onset narrative.

Affected results: primary ORs 1.06/0.93/0.93 and Cox HRs 1.05 (0.86–1.27),0.91 (0.75–1.10),0.91 (0.75–1.11), especially their planned supporting versus post hoc status. SAP may supersede protocol, but that does not itself explain why its explicit Cox analysis is called post hoc. A narrower later implementation may be intended but is not identified. Protocol/SAP model priority is P_P; protocol/report priority and SAP/report Cox status are P_R; P_R takes precedence. Classification ambiguity: SAP operative date/version and amendment chronology are absent. Human question: which primary-model specification operated prospectively, and what reconciles the planned secondary Cox analysis with its post hoc designation?

## C003 — Planned additive-interaction sensitivity not reported

Finding provenance: F-XS-005, cross_source_consistency_reviewer; independent initial screen INCLUDE.

SAP unconditionally commits to an additive-interaction sensitivity for primary MDD using RERI from a linear odds-ratio model and a likelihood-based 95% CI. Supplied REPORT materials contain multiplicative logistic interaction OR 0.93 (0.76–1.14), P=.48, Cox interaction HR 0.91 (0.75–1.11), P=.36, no-imputation secondary sensitivity and CACE. Complete REPORT mapping and source searches locate no RERI/additive estimate, CI, or reconciliation statement. Multiplicative interaction does not supply the planned additive estimand.

Exact locations: DOC-003 SAP p.4 primary-outcome interaction section; DOC-001 main pp.1 combination result,4 methods,6 Table 2,7 MDD narrative,8 sensitivity; DOC-004 results pp.21 no-imputation sensitivity,22 CACE. Absence scope covers DOC-001 pp.1–11, DOC-004 pp.1–25, DOC-005 joi190007supp4_prod.pdf p.1.

Affected result: completeness and interpretation of the reported absence of combined-intervention benefit for primary MDD and the unavailable prespecified additive estimate/CI. This qualifies as explicitly planned primary-outcome analysis not reported, rather than a desired additional detail. It does not assert that the analysis was never conducted or that its result would change a conclusion. Analysis may have been omitted, replaced or deferred; none is documented. Relationship P_R only. Classification ambiguity: actual execution is outside supplied evidence. Human question: where is the planned additive estimate/CI or its documented reconciliation?

## C004 — IDS endpoint hierarchy across protocol, SAP and report

**Inclusion audit:** QUESTIONED. The auditor found that protocol p.14 includes depressive symptom scores within secondary objectives, while the contrasting main/primary-study-parameter headings do not establish formal co-primary or key status. This supports a broad-terminology reading resolved by the explicit SAP/report secondary hierarchy. Under the scope's doubt rule, the reproduced source contrast may not meet inclusion. The stable ID and evidence remain available for human adjudication.

Finding provenance: F-XS-004, cross_source_consistency_reviewer; F-ST1-003, statistics_pass_1; both independent initial screen INCLUDE, consolidated as one issue.

Protocol includes IDS in its main-endpoint list and primary-study-parameter analysis subsection, separately from its secondary-parameter subsection. SAP and article classify IDS as secondary; the article treats secondary findings as exploratory because of multiple comparisons. The same IDS measure and follow-up windows are compared. This is a hierarchy issue; the coefficient 0.60 and adjusted mean difference 1.20 reconcile by stated effect coding and precision.

Exact locations: DOC-002 protocol pp.9 main-endpoint summary,28 §§8.1.1/8.1.2,43 §§10.1/10.2; DOC-003 SAP p.2 outcomes; DOC-001 main pp.4 secondary outcomes/exploratory interpretation,8 Table 3 and narrative. Additional audit context: DOC-002 protocol p.14 Secondary Objective explicitly includes depressive symptom scores; retain this page in the report's source locations and context assessment.

Affected result: prospective hierarchy attached to the IDS supplement overall coefficient 0.60 (0.15–1.05), P=.01, or full adjusted mean difference 1.20 (0.29–2.10), P=.01. SAP may refine protocol terminology or prospectively revise hierarchy, but the separate primary/secondary sections prevent identifying the intended reconciliation at once. No proven formal co-primary status or unprinted multiplicity rule is asserted. Protocol/SAP is P_P; protocol/report is P_R, with P_R precedence. Classification ambiguity: formal co-primary status and amendment chronology are not established. Human question: what operative IDS hierarchy reconciles its protocol main/primary placement with SAP/report secondary status?

## C005 — Primary MDD power assumptions and contrasts

**Inclusion audit:** QUESTIONED. The protocol explicitly powers an interaction-oriented contrast and the report explicitly powers marginal main effects; their different risk assumptions can coexist with a common 250-per-cell target. Missing operational mapping alone does not establish contradictory assumptions for the same matched contrast. The auditor applies the context/conditional exclusion boundary; the reproduced source contrast and stable ID are retained for human adjudication.

Finding provenance: F-XS-001, cross_source_consistency_reviewer; F-ST1-001, statistics_pass_1; both independent initial screen INCLUDE, consolidated as one issue.

Protocol specifies control 30%, intervention 15%, 90% power, two-sided alpha .05, 180/group, 20% dropout and 250/arm, with additive-interaction interest and 80% synergy comparison. Article specifies control 30%, active 20%, 33% relative/10 percentage-point absolute decrease, 90% power, two-sided alpha .05, 196/factorial cell, 22% attrition and 250/cell for main effects. The distinctly stated powering contrasts are retained; no equality between their sample-size algorithms is required.

Exact locations: DOC-002 protocol pp.16 §4.4,17 continuation,1 final-amendment version; DOC-001 main pp.4 Sample Size,9 power discussion/limitations.

Affected extraction: primary-design assumed incidence/effect/dropout inputs and the power basis accompanying the null primary MDD result. Active-risk rounding ranges 14.5–15.5% and 19.5–20.5% do not overlap; assumptions differ by 5 percentage points, and dropout by 2. Report 392/196 grouping and protocol introductory 25% wording are context-resolved and excluded as bases for this candidate. Different interaction-oriented and main-effect calculations may coexist, but neither text maps their materially different assumptions to the operative recruitment basis; matching 250/cell does not resolve that mapping. No arithmetic failure or demonstrably identical marginal populations are asserted. P_R only; SAP supplies no power comparator. Classification ambiguity: powering contrasts differ and revision chronology is absent. Human question: how do the two assumption/contrast specifications jointly define or revise the operative primary-design power basis?
