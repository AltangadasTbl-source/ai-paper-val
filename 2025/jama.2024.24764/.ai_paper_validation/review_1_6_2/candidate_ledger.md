# Workflow 1.6.2 Stable Candidate Ledger

**Pending Human Adjudication**

Five issues were registered after an independent initial screen of all ten checker findings. Eight INCLUDE findings consolidate into five stable candidates. IDs follow first conflicting REPORT source location in DOC-001, then PLAN-only locations: quality-of-life summary p. 1, hospital-stay abstract p. 1, eligibility p. 2, covariance p. 4, and SAP p. 26. The source-order tie on p. 1 follows the abstract's no-difference summary before its displayed hospital-stay contrast. Assigned IDs are never removed. The mandatory exact-source recheck found all five evidence states reproduced and confirmed every classification. The independent inclusion and evidence-quality audit recorded CONFIRMED for all five candidates; every candidate remains Pending Human Adjudication.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_C | S_C | REPORT main article abstract p. 1 and secondary outcomes p. 6 vs REPORT results supplement eTable 3 p. 4 | reproduced | CONFIRMED | F-XS-005, F-ST1-005 |
| C002 | protocol_report | P_R | P_R | PLAN SAP pp. 15, 25, 42 and protocol pp. 24, 39 vs REPORT main article pp. 1, 4, 6, 8 | reproduced | CONFIRMED | F-XS-002, F-ST1-004 |
| C003 | protocol_report | P_R | P_R | REPORT main article eligibility p. 2 and mortality interpretation p. 10 vs PLAN protocol eligibility p. 17, summary p. 8, amendments p. 2 | reproduced | CONFIRMED | F-XS-001 |
| C004 | protocol_report | P_R | P_R | PLAN SAP analysis p. 26 vs REPORT main article analysis p. 4 and results p. 8, with REPORT results supplement pp. 3-4 affected outputs | reproduced | CONFIRMED | F-XS-003, F-ST1-002 |
| C005 | plan_material | P_P | P_P | PLAN SAP p. 26 fixed-parameter declaration vs PLAN SAP p. 26 baseline-adjusted time-specific contrast declaration | reproduced | CONFIRMED | F-ST1-003 |

## C001 — Quality-of-life conclusion versus the day-7 index test

**Candidate statement:** Quality-of-life conclusion versus the day-7 index test.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main article abstract p. 1 and secondary outcomes p. 6 vs REPORT results supplement eTable 3 p. 4

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-005, F-ST1-005

**Qualifying route:** Route A, category 1

**Classification rationale:** The conflicting narrative and day-specific test are in two REPORT documents. The SAP only corroborates the significance convention and does not introduce a P_R relationship.

**Classification ambiguity:** The intended narrative hypothesis is not stated; overall, interaction, final-time and clinical interpretations remain alternatives.

**Status:** Pending Human Adjudication


- **Finding IDs/provenance:** F-XS-005 (cross_source_consistency_reviewer), F-ST1-005 (statistics_pass_1).
- **Title:** Unqualified quality-of-life no-difference conclusion versus the day-7 EQ index test.
- **Route/focus:** Route A, category1; focus B.
- **Domain/type/all:** statistical_results / S_C / S_C.
- **Compared evidence:** REPORT [main abstract p1](../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=1), [Secondary Outcomes p6](../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=6), versus REPORT [eTable3 day7 and interaction, supplement p4](../../joi240145supp3_prod_1741627844.89412.pdf#page=4).
- **Exact values/statements:** Abstract says six of seven secondary outcomes show no significant difference, including QoL; body says no differences in QoL and cites eTables2–4. Day7 index MD−.057, CI exact string `(-0.104 -0.010)`, P=.02; interaction P=.10. Other index time-point P values .37/.49/.78.
- **Rule:** Day7 [.015,.025] P rounding range is entirely below .05; an interaction tests differing treatment effects across time and is a distinct null. The unqualified narrative's scope includes the cited time-specific result. CI separator typography is preserved; this issue rests on unambiguous P and narrative independently of endpoint-token parsing.
- **Affected extraction:** Whether day7 EQ index is a significant treatment contrast; which QoL conclusion is extracted from abstract/body versus table.
- **Alternatives/human question:** Could narrative mean an omnibus longitudinal hypothesis, interaction, final time point, or clinical importance? No such qualification/test attribution is printed. Ask which hypothesis/time/component supports the narrative and how it reconciles with day7 P=.02. No claim that an isolated test proves an overall longitudinal effect.
- **Corroboration only:** [SAP p12](../../joi240145supp1_prod_1741627844.87412.pdf#page=12) supplies two-sided95%/.05 and no multiplicity correction; it does not introduce P_R. Classification ambiguity: narrative's exact intended hypothesis is missing, but compared source roles/type are unambiguous.


## C002 — Planned hospital-stay differences versus reported geometric ratios

**Candidate statement:** Planned hospital-stay differences versus reported geometric ratios.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP pp. 15, 25, 42 and protocol pp. 24, 39 vs REPORT main article pp. 1, 4, 6, 8

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-002, F-ST1-004

**Qualifying route:** Route A, category 5

**Classification rationale:** The prospective UK hospital-stay difference specification is compared with the reported fitted contrast. Both plan documents are PLAN; the article is REPORT. Their alternative contingencies do not add an independent P_P conflict.

**Classification ambiguity:** A superseding analysis amendment is not supplied; the SAP transformation permission remains a source-grounded alternative.

**Status:** Pending Human Adjudication


- **Finding IDs/provenance:** F-XS-002 (cross_source_consistency_reviewer), F-ST1-004 (statistics_pass_1).
- **Title:** Planned key-secondary hospital-stay difference analysis versus reported geometric-mean ratios.
- **Route/focus:** Route A, category5; focus D.
- **Domain/type/all:** protocol_report / P_R / P_R.
- **PLAN evidence:** [SAP §9.2 p15](../../joi240145supp1_prod_1741627844.87412.pdf#page=15), [§9.6 p25](../../joi240145supp1_prod_1741627844.87412.pdf#page=25), [planned display p42](../../joi240145supp1_prod_1741627844.87412.pdf#page=42); [protocol UK-only definition p24](../../joi240145supp4_prod_1741627844.90412.pdf#page=24), [§14.2.2 p39](../../joi240145supp4_prod_1741627844.90412.pdf#page=39).
- **REPORT evidence:** [main abstract p1](../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=1), [Statistical Analysis p4](../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=4), [Secondary Outcomes p6](../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=6), [Table3/footnote c p8](../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8).
- **Printed specification/results:** SAP UK-only continuous mixed linear adjusted mean difference/95%CI; proposed primary method first, transformations/nonparametric methods through sensitivity analysis. Protocol adjusted mean difference or, if skewed, unadjusted difference in medians. Report skewed LOS log-transformed before fitting, effects exponentiated to adjusted geometric ratios; UK.91 [.82,1.02], P=.12 with9[7–15] vs11[7–16]days; pooled.96 [.88,1.06], P=.21 with8[6–14] vs9[6–14.5]days foregrounded in abstract.
- **Rule/affected extraction:** Neither planned difference estimand/interval is reported in the complete mapped results material; geometric ratio is a different estimand, not a mismatched crude subtraction. LOS is key secondary because reported in abstract. Display precision does not apply to model/estimand/population specifications.
- **Alternatives/human question:** SAP transformation permission could authorize log analysis as sensitivity, or an amended plan could replace the first analysis and expand the population; report explains skewness, but none supplies the planned difference result. Ask where the planned UK difference is reported or what amendment replaced it. The added pooled-country analysis belongs to this same presentation/replacement pattern; UK analysis is present. Do not create an independent plan-internal issue from protocol/SAP alternative contingencies.
- **Classification ambiguity:** Potential superseding analysis amendment is not supplied. Both supplied prospective versions remain PLAN and the published fitted analysis REPORT.


## C003 — Reported predicted-survival exclusion versus supplied eligibility criteria

**Candidate statement:** Reported predicted-survival exclusion versus supplied eligibility criteria.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT main article eligibility p. 2 and mortality interpretation p. 10 vs PLAN protocol eligibility p. 17, summary p. 8, amendments p. 2

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-001

**Qualifying route:** Route B

**Classification rationale:** The report's affirmative population restriction is compared with the prospective eligibility list. This is a REPORT-versus-PLAN population definition, without clinical appraisal or inferred exclusion counts.

**Classification ambiguity:** An unsupplied operational or amended criterion could reconcile the difference.

**Status:** Pending Human Adjudication


- **Finding ID/provenance:** F-XS-001 (cross_source_consistency_reviewer).
- **Title:** Reported predicted-30-day-survival exclusion absent from the supplied current eligibility plan.
- **Route/focus:** Route B; focus D. B1 is the positive planned/report analysis-population definition comparison; B2 is the formal exclusion absent from complete current criteria; B3 is the primary SSI result's population description.
- **Domain/type/all:** protocol_report / P_R / P_R.
- **REPORT evidence:** [main Eligibility Criteria p2](../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=2), [mortality interpretation p10](../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=10).
- **PLAN evidence:** [protocol §5.1–5.2 p17](../../joi240145supp4_prod_1741627844.90412.pdf#page=17), [summary p8](../../joi240145supp4_prod_1741627844.90412.pdf#page=8), [amendment context p2](../../joi240145supp4_prod_1741627844.90412.pdf#page=2).
- **Printed comparison:** Report excludes patients not expected to survive beyond30days and later invokes not including those unlikely to survive30days. Protocol lists only preceding3months abdominal surgery and expected reopening within30days as exclusions; inclusion willing/able day30 follow-up and capacity provisions does not state predicted survival. Current version4.0/amendment summary supplies no identifiable added survival threshold.
- **Rule/affected extraction:** Criterion presence-versus-absence, not clinical appropriateness or a count of affected individuals. The explicit population restriction accompanying SSI RR1.03 [0.83,1.28] and mortality interpretation differs from the supplied prospective criterion list. No arithmetic display-precision calculation is applicable.
- **Alternatives/human question:** A separate operational/amended criterion may exist; alternatively pragmatic recruitment selection may have been described as formal exclusion. Ask which prespecified document establishes the explicit predicted-survival criterion. Do not infer a realized exclusion count or challenge any observed death's eligibility.
- **Classification ambiguity:** An unsupplied operational/amended criterion could reconcile the discrepancy; content roles and relationship remain clear.


## C004 — Unstructured versus independent quality-of-life covariance

**Candidate statement:** Unstructured versus independent quality-of-life covariance.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP analysis p. 26 vs REPORT main article analysis p. 4 and results p. 8, with REPORT results supplement pp. 3-4 affected outputs

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-003, F-ST1-002

**Qualifying route:** Route B

**Classification rationale:** The conflicting covariance specifications are PLAN versus REPORT. Supplementary results identify affected outputs but do not create an independent S_C conflict.

**Classification ambiguity:** The working-covariance/model-level interpretation, variance estimator and possible amendment remain unresolved.

**Status:** Pending Human Adjudication


- **Finding IDs/provenance:** F-XS-003 (cross_source_consistency_reviewer), F-ST1-002 (statistics_pass_1).
- **Title:** SAP unstructured versus report independent covariance for repeated quality-of-life results.
- **Route/focus:** Route B; focus D. Positive covariance-specification conflict affects uncertainty in named QoL results and is not a missing-detail-only observation.
- **Domain/type/all:** protocol_report / P_R / P_R.
- **PLAN evidence:** [SAP §9.6 p26](../../joi240145supp1_prod_1741627844.87412.pdf#page=26).
- **REPORT evidence:** [main Statistical Analysis p4](../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=4), [Table3 SF12 p8](../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=8), [eTable2 p3](../../joi240145supp3_prod_1741627844.89412.pdf#page=3), [eTables3–4 p4](../../joi240145supp3_prod_1741627844.89412.pdf#page=4).
- **Printed comparison/rule:** SAP general unstructured repeated covariance plus robust sandwich standard errors, EQ same methods as SF12; report same longitudinal outcomes/treatment×time mixed linear analysis but independent covariance. Unstructured allows cross-time residual covariance; independence constrains it. Numeric display precision is inapplicable.
- **Affected extraction:** All adjusted day-specific PCS/MCS and EQ index/health contrasts, confidence limits/P values and treatment×time tests; e.g. day30 PCS−.861 [−2.829,1.106], MCS−1.904 [−4.276,.469].
- **Alternatives/human question:** Working covariance versus another model level, retained robust inference, revised fitting/convergence specification or an amended SAP could reconcile wording, but no supplied explanation identifies one. Ask which covariance/variance specification generated the printed estimates and how it relates to the plan. Missing report robust-SE statement is not a separate issue; no numerical effect or preferred covariance is claimed.
- **Classification ambiguity:** Model-level interpretation/amendment remains unresolved. Results supplement corroborates affected outputs; it does not add an independent S_C conflict.


## C005 — SAP fixed-participant parameterization and adjusted contrasts

**Candidate statement:** SAP fixed-participant parameterization and adjusted contrasts.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN SAP p. 26 fixed-parameter declaration vs PLAN SAP p. 26 baseline-adjusted time-specific contrast declaration

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-003

**Qualifying route:** Route B

**Classification rationale:** Both compared declarations are within the SAP. The issue concerns internal prospective parameter roles and adjustment, without an assertion that the fitted REPORT model used fixed participant indicators.

**Classification ambiguity:** Participant may denote an indicator, repeated-subject identifier or constrained parameterization; some fitted group-average contrasts can remain estimable.

**Status:** Pending Human Adjudication


- **Finding ID/provenance:** F-ST1-003 (statistics_pass_1); screened narrow claim differs from checker's broad absolute-contrast identification assertion.
- **Title:** SAP fixed-participant and fixed-treatment/baseline specification leaves the intended adjusted repeated-model parameterization unclear.
- **Route/focus:** Route B; focus C/D. B1 positive parameter-role/method specification; B2 explicit all-fixed parenthesis with treatment and baseline constant per participant; B3 interpretation of the planned adjusted QoL mean differences.
- **Domain/type/all:** plan_material / P_P / P_P.
- **Compared PLAN evidence:** [SAP p26 §9.6](../../joi240145supp1_prod_1741627844.87412.pdf#page=26), fixed-parameter declaration versus baseline-adjusted day-specific contrast declaration in the same paragraph; EQ methods inherit it. No REPORT location is a conflicting party.
- **Exact wording/rule:** Parameters allowing for participant, treatment group, baseline score, time and minimization variables, all fixed except center random; all assessment times including baseline; time×treatment; mean differences at relevant times. With literal perparticipant indicator columns I_i, T=Σtreated I_i and B=Σ B_i I_i, so separate treatment and baseline coefficients are not identified together with all participant effects absent a defined parameterization.
- **Essential limitation:** That column identity does not prove every absolute group-average difference is inestimable: fitted means/particular linear contrasts can remain estimable and invariant to redistributing coefficients. Do not carry a universal no-contrasts conclusion into registration. Narrow issue is which participant representation/constraint and baseline-adjusted contrast is intended by the positive specification.
- **Affected result/human question:** Planned adjusted day-specific PCS/MCS and EQ index/health contrasts. Does participant mean a fixed-indicator term, repeated-subject identifier, or another representation, and which parameterization/contrast implements the declared adjustment? No assertion about the actually fitted report model or preferred alternative analysis.
- **Classification ambiguity:** Parameterization meaning is unresolved; the conflict is internal prospective method logic, not report-plan noncompliance. Numeric display-precision calculation is inapplicable.
