## C001 — Protocolized temperature-management window

**Status:** Pending Human Adjudication

**Candidate statement:** The reported seven-day temperature-management window does not identify how it relates to final-plan 96-hour device/pyrexia instructions and contemporaneous seven-day instructions.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** REPORT DOC-001 pp.1,3 vs PLAN DOC-002 pp.77,89,101; PLAN final V9 sections compared

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-202

**Qualifying route:** Route B

**Classification rationale:** Confirmed. P_R takes precedence over the independent P_P component. These are intervention specifications in protocol material, and observed/published intervention descriptions in report material.

**Classification ambiguity:** The p.77 seven-day time origin and post-96-hour ordinary-care definition remain unspecified; role assignments are clear.

**Exact source locations:** Yes, at every registered location: REPORT [DOC-001 p.1, Interventions](../../../jama_cooper_2018_oi_180132.pdf#page=1) and [p.3, Rewarming and Normothermia](../../../jama_cooper_2018_oi_180132.pdf#page=3); PLAN [DOC-002 p.77, §12.11](../../../joi180132supp1_prod.pdf#page=77), [p.89, Appendix A events table](../../../joi180132supp1_prod.pdf#page=89), and [p.101, Appendix F infection/pyrexia instructions](../../../joi180132supp1_prod.pdf#page=101).

**Source evidence:** Yes. Abstract: temperature managed in both groups for seven days. Main p.3: after reaching 37°C, normothermic management using automated wraps if required for up to seven days postrandomization.

**Reported-versus-comparator:** Yes. Final V9 p.77: postrewarming normothermia with pads up to a maximum seven days or earlier ICU discharge; this sentence does not explicitly give the time origin. Control pyrexia prevention is up to 96 hours postrandomization, then unit protocol. Events table p.89 marks standard-care temperature-control device continuation through Day 7. Appendix p.101 gives normothermic pads for 96 hours postrandomization, then ward protocol, and pyrexia prevention in all patients up to 96 hours postrandomization, then unit protocol. These are distinct contemporaneous sections, rather than only historical versions.

**Reasoning procedure:** Yes. Focus D and Route B concern the assigned intervention/comparator duration. REPORT seven-day specification differs from PLAN 96-hour specification; PLAN event/detailed-section seven-day specifications differ from PLAN Appendix F 96-hour specification.

**Calculation:** Seven days = 168 hours. Conservatively allowing seven displayed days [6.5,7.5] gives [156,180] hours; 96 hours gives [95.5,96.5]. Gap 59.5 hours; relative discrepancy 59.5/96 = 0.61979. This is a comparison of specifications, not a claim about actual patient exposure. The seven-day hypothermia maximum itself reconciles and is context.

**Affected result or extracted value:** Assigned temperature-management/device-use duration for each randomized arm attached to the primary six-month favorable-GOSE comparison.

**Why context does not resolve it:** Optional pads, earlier ICU discharge and subsequent ward care do not define whether seven days and 96 hours describe the same arm-specific assigned management window. The final protocol retains both schedules without an explicit hierarchy.

**Alternative source-grounded interpretations:** Seven days may describe the full management window, with compulsory protocol measures ending at 96 hours and later measures supplied by routine care; pads are explicitly optional when required, and ICU discharge can shorten use. This does not define a common arm-specific device maximum across the compared statements.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. The direct PDFs retain seven-day and 96-hour specifications in the registered report and contemporaneous final-plan sections, separated beyond display precision. Necessary inputs: Yes for the textual/duration comparison. **Exact missing inputs or definitions:** Which section governed arm-specific device use, the seven-day time origin on p.77, and whether routine ward/unit management after 96 hours was intended to constitute the same assigned seven-day intervention. Actual device-use records are unavailable. Direct observation and inference: The competing printed schedules and events-table ticks are direct observations. A retained appendix from an earlier practice or a distinction between active device management and ordinary care is an unestablished explanation. No adherence consequence is inferred. See the complete durable [C001 source recheck](../verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, an extractor could record different assigned temperature-management durations for the randomized arms. Actual device exposure, adherence and outcome consequences are not established.

Checker provenance: Included finding F-ST1-202; duplicate findings F-XS-007. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

## C002 — Signed primary risk difference

**Status:** Pending Human Adjudication

**Candidate statement:** The abstract prints a positive primary risk difference of 0.4%, while the body and Table 2 print −0.4 percentage points for the same outcome, counts and confidence interval.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT DOC-001 abstract p.1 vs body p.5 and Table2 p.7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-001

**Qualifying route:** Route A, category 2

**Classification rationale:** Confirmed. Every conflicting copy is in one published report; this concerns a signed estimate, so statistical_results applies.

**Classification ambiguity:** None.

**Exact source locations:** Yes: REPORT [DOC-001 p.1, abstract Results](../../../jama_cooper_2018_oi_180132.pdf#page=1), [p.5, Primary Outcome](../../../jama_cooper_2018_oi_180132.pdf#page=5), and [p.7, Table 2 primary row](../../../jama_cooper_2018_oi_180132.pdf#page=7).

**Source evidence:** Yes. Abstract prints risk difference 0.4%, CI −9.4% to 8.7%, RR 0.99, P=.94, with favorable counts 117 and 111.

**Reported-versus-comparator:** Yes. Body and Table 2 print −0.4 percentage points, identical interval −9.4 to8.7, with counts 117/240 and 111/226.

**Reasoning procedure:** Yes: focus B, Route A category 2, opposite signed readings of the same primary absolute effect.

**Calculation:** H−N = 100(117/240−111/226) = −0.36504425 percentage points. Positive0.4 interval [0.35,0.45] versus negative −0.4 interval [−0.45,−0.35] leaves gap 0.70; relative discrepancy 0.70/0.4=1.75. Count-derived intervals are unnecessary to establish the separated printed copies.

**Affected result or extracted value:** Signed primary absolute risk difference for favorable six-month GOSE, hypothermia versus normothermia.

**Why context does not resolve it:** Route A, category 2 applies to opposite printed signs changing the extracted effect direction; reconstructing a sign from counts does not remove the candidate.

**Alternative source-grounded interpretations:** Reverse contrast or absolute magnitude could account for positive 0.4. The unchanged asymmetric CI and RR below1 accompany the original H-versus-N contrast and do not define such a switch.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. Fresh source renders show positive 0.4 in the abstract and negative −0.4 in both other copies, beyond precision. Necessary inputs: Yes. **Exact missing inputs or definitions:** Whether the abstract uses unsigned magnitude or an explicitly different contrast; neither is stated. Direct observation and inference: Three source signs, counts and intervals are direct observations. The origin of the sign difference is not established; no significance change is claimed. See the complete durable [C002 source recheck](../verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, an extractor could copy the positive abstract estimate or the negative body/table estimate as the signed primary effect. No significance or paper-level conclusion change is established.

Checker provenance: Included finding F-NUM-001; duplicate findings F-ST1-001, F-XS-001. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

## C003 — Cooling-duration anchor and late-cooling minimum

**Status:** Pending Human Adjudication

**Candidate statement:** The final protocol and report give different cooling-duration anchors, with further 72 hours after target attainment versus 72 hours after randomization and a conditional 48-hour late-cooling minimum.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** REPORT DOC-001 pp.3–4 vs PLAN DOC-002 pp.69,77,97,99; PLAN final V9 sections compared

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-201

**Qualifying route:** Route B

**Classification rationale:** Confirmed. Report-versus-plan and independent final-plan specification differences coexist, so P_R precedes P_P.

**Classification ambiguity:** Ideal-versus-operative wording and the conditional48-hour exception require interpretation; roles remain clear.

**Exact source locations:** Yes: REPORT [DOC-001 p.3, Maintenance/Rewarming](../../../jama_cooper_2018_oi_180132.pdf#page=3), [p.4, target-attainment results](../../../jama_cooper_2018_oi_180132.pdf#page=4); PLAN [DOC-002 p.69, §6.5](../../../joi180132supp1_prod.pdf#page=69), [p.77, §12.11](../../../joi180132supp1_prod.pdf#page=77), [p.97, §26.3.1](../../../joi180132supp1_prod.pdf#page=97), and [p.99, rewarming flowchart and late-start note](../../../joi180132supp1_prod.pdf#page=99).

**Source evidence:** Yes. Report maintains hypothermia for at least72 hours after randomization and assesses rewarming at 72 hours after randomization; maximum is seven days. Target attainment results show only 186 patients reached33°C and report injury-to33°C median10.1 hours; these are context, not individual duration arithmetic.

**Reported-versus-comparator:** Yes. Final synopsis p.69 reaches33°C then maintains for a further72 hours. Detailed p.77 assesses72 hours after randomization. Appendix p.97 says ideally72 hours after severe head injury. Flowchart p.99 uses72 hours postrandomization and requires at least48 hours of actual cooling before considering rewarming if cooling commenced late.

**Reasoning procedure:** Yes. Focus D, Route B: duration/time-origin specification for the randomized intervention. The synopsis's further72-hour target-temperature period differs from the detailed randomization-based rule plus late-start48-hour minimum. The latter minimum is conditional, so it is not asserted to apply to every patient.

**Calculation:** Nominal minima72 and 48 hours give intervals [71.5,72.5] and [47.5,48.5], gap 23 hours and relative 23/72=0.31944. Time origins differ logically even when the numeral72 matches. If target attainment occurs after randomization, attainment+72 and randomization+72 do not identify the same endpoint; source-level medians are not subtracted to estimate any individual's duration.

**Affected result or extracted value:** Assigned cooling dose, minimum duration and time origin for the primary favorable-GOSE comparison.

**Why context does not resolve it:** The final synopsis and operative flowchart do not specify how ideal target-temperature exposure, the randomization anchor and the conditional late-cooling rule are reconciled.

**Alternative source-grounded interpretations:** The synopsis may give an ideal target-temperature dose while the operational flowchart supplies clinically conditional implementation. That is possible, but it leaves the dose/time-origin extracted from the ordinary assigned intervention unspecified across final V9 and report.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. The final synopsis explicitly specifies a further72 hours after target attainment, while report/detailed plan and late-start flowchart explicitly use the other anchors/minimum. Necessary inputs: Yes for specifications. **Exact missing inputs or definitions:** Governing time origin, definition of actual cooling for the48-hour condition, and hierarchy among synopsis, detailed protocol and appendix. Patient-level target attainment, exceptions and exposure are unavailable. Direct observation and inference: Printed anchors,72-hour phrases and 48-hour note are direct. Actual shortening of individual cooling or its clinical consequences is not established. See the complete durable [C003 source recheck](../verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, an extractor could characterize the intervention using different cooling-duration anchors or minima. Individual exposure and neurological consequences are not established.

Checker provenance: Included finding F-ST1-201; duplicate findings F-XS-006. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

## C004 — Routine rewarming rate

**Status:** Pending Human Adjudication

**Candidate statement:** The report describes a routine rewarming target up to 0.25°C/h, while the final plan recommends an aim/maximum of approximately 0.17°C/h; the relationship between the ordinary specifications remains unclear.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT DOC-001 p.3 vs PLAN DOC-002 pp.77,99,100; PLAN p.21 historical context

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-203

**Qualifying route:** Route B

**Classification rationale:** Confirmed. This concerns an intervention specification. The superseded0.25 historical plan does not add P_P.

**Classification ambiguity:** Recommended aim versus broad reported ceiling is explicitly retained; no rigid ban or actual rate violation is inferred.

**Exact source locations:** Yes: REPORT [DOC-001 p.3, Rewarming](../../../jama_cooper_2018_oi_180132.pdf#page=3); PLAN [DOC-002 p.77, §12.11](../../../joi180132supp1_prod.pdf#page=77), [p.99, flowchart rate aim](../../../joi180132supp1_prod.pdf#page=99), [p.100, management and special considerations](../../../joi180132supp1_prod.pdf#page=100). Historical [PLAN p.21, V1 §12.11](../../../joi180132supp1_prod.pdf#page=21) was also found and read.

**Source evidence:** Yes. The report gives gradual controlled rewarming at a target rate up to0.25°C/h.

**Reported-versus-comparator:** Yes. Final p.77 gives gradual rewarming0.17°C/h, with a recommended maximum0.5°C every three hours. Flowchart p.99 says the rate aim is0.17°C/h. Management p.100 repeats0.17 and 0.5°C every three hours and permits faster rates in urgent situations under the intensivist. Historical p.21 gives0.25°C/h; that is disclosed version context, not an independent contemporaneous plan conflict.

**Reasoning procedure:** Yes, Route B and focus D, as a comparison of reported routine specification with final-plan recommended routine specification. It is not a comparison of actual patient rates and not a claim that a recommendation legally prohibits every higher rate.

**Calculation:** Intervals [0.165,0.175] and [0.245,0.255] have gap 0.070; relative 0.070/0.17=0.41176. The displayed0.5°C/3h rule is consistent with approximately0.1667°C/h and confirms the0.17 recommendation.

**Affected result or extracted value:** Routine assigned rewarming target/maximum used to characterize the randomized cooling intervention.

**Why context does not resolve it:** The immediate context does not specify whether the broader report ceiling represents a revised routine aim or contains the final-plan recommended aim. Emergency exceptions do not define the ordinary target.

**Alternative source-grounded interpretations:** A routine rate0.17 satisfies the report's broader up-to0.25 ceiling. The recommendation may remain operative within that ceiling, so actual adherence could reconcile. The registered issue is the different descriptions of the routine maximum/aim; emergency exceptions are expressly disclosed and do not identify a new routine aim.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. Direct sources confirm the reported up-to0.25 routine target and final-plan0.17 recommended aim/maximum descriptions, with separated numeric specification intervals. Necessary inputs: Yes for routine target/recommendation comparison. **Exact missing inputs or definitions:** Whether0.25 is merely a broad outer ceiling containing the recommended0.17 aim, whether a later operative update changed that aim, and the implemented routine-rate specification. Actual temperature traces cannot be inferred from these descriptions. Direct observation and inference: The rate phrases, recommendation and urgent exceptions are direct. An actual protocol departure or mechanism for the differing report statement is not established. See the complete durable [C004 source recheck](../verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, an extractor could record 0.25°C/h or approximately 0.17°C/h as the routine specification. Actual patient rates and adherence cannot be inferred.

Checker provenance: Included finding F-ST1-203; duplicate findings None. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

Audit finding F-QA-102 is SCREENED_OUT/DUPLICATE_OF_INCLUDED provenance, not an additional included Finding ID.

## C005 — Primary analysis-population definition

**Status:** Pending Human Adjudication

**Candidate statement:** The primary analysis-population definition differs between the report and final plan regarding the joint class of patients who were ineligible and never received the intervention.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT DOC-001 pp.3–4 and DOC-003 pp.12,17 vs PLAN DOC-002 pp.84,174–175

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-204

**Qualifying route:** Route B

**Classification rationale:** Confirmed. This is a planned-versus-reported primary analysis definition; the report sensitivity populations are contextual, not a separate S_C inconsistency.

**Classification ambiguity:** Realized equality of the two primary sets is unresolved; roles are clear.

**Exact source locations:** Yes: REPORT [DOC-001 p.3, a-priori analyses definition](../../../jama_cooper_2018_oi_180132.pdf#page=3), [p.4, Figure1 and evaluable population](../../../jama_cooper_2018_oi_180132.pdf#page=4), [DOC-003 p.12, per-protocol definition](../../../joi180132supp2_prod.pdf#page=12), [p.17, as-treated definition](../../../joi180132supp2_prod.pdf#page=17); PLAN [DOC-002 p.84, §15.2](../../../joi180132supp1_prod.pdf#page=84), [p.174, V8 modified-ITT amendment](../../../joi180132supp1_prod.pdf#page=174), and [p.175, amendment continuation](../../../joi180132supp1_prod.pdf#page=175).

**Source evidence:** Yes. All a-priori analyses use randomized assignment excluding consent withdrawals unless otherwise indicated. Report p.4 removes6+5=11 withdrawals from511, leaving500; primary outcome available for 240 and 226. Supplement defines broader eligibility and compliance exclusions for sensitivity populations.

**Reported-versus-comparator:** Yes. Final §15.2 excludes consent withdrawals and those not fulfilling inclusion criteria and never receiving the intervention. The V8 amendment specifically describes addition of modified intention-to-treat analysis to accommodate this joint class; p.175 continues its rationale, rather than supplying membership counts.

**Reasoning procedure:** Yes, focus D and Route B: differing primary-population membership specification. The conjunctive criterion requires both ineligibility and never receiving intervention; it must not be replaced by an exclusion of every ineligible patient.

**Calculation:** 511−(6+5)=500, and 240+226=466, reconcile. There is no reproduced numerical population-count difference; a precision discrepancy is zero for these count identities. The reproduced comparison is logical set definition: REPORT randomized minus consent withdrawals versus PLAN that set minus the joint exclusion class. The latter may be empty.

**Affected result or extracted value:** Primary analysis-set definition underlying favorable outcomes 117/240 versus 111/226.

**Why context does not resolve it:** The report does not state whether the planned joint exclusion was applied or had no members. Sensitivity-population definitions do not establish primary-set membership.

**Alternative source-grounded interpretations:** The joint class could contain nobody in the primary dataset; alternatively a later SAP may define implementation. Report sensitivity exclusions do not establish whether the same joint exclusion operated in the primary analysis.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. Final-plan joint exclusion and report consent-only definition remain different as printed; no count mismatch is asserted. Necessary inputs: Yes to compare definitions; no to calculate a changed population. **Exact missing inputs or definitions:** Patient-level membership of the joint class, which primary analyses applied the modified definition, and any operative SAP explanation underlying 'unless otherwise indicated.' Direct observation and inference: Differing explicit set definitions and printed500/466 totals are direct. Different realized membership, patient exclusions and any effect on117/240 versus 111/226 are unestablished. See the complete durable [C005 source recheck](../verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, an extractor could use different descriptions of the primary analysis set. A changed realized denominator or effect estimate is not established.

Checker provenance: Included finding F-ST1-204; duplicate findings F-XS-005. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

## C006 — Planned binary primary odds ratio not supplied

**Status:** Pending Human Adjudication

**Candidate statement:** The supplied final plan promises a binary primary GOSE odds ratio and 95% confidence interval that are absent from the matched supplied report outputs.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN DOC-002 p.84 vs REPORT DOC-001 pp.1,3,5,7 and DOC-003 pp.1–24

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004

**Qualifying route:** Route A, category 5

**Classification rationale:** Confirmed. It is planned-versus-reported primary output presence; no report-to-report conflict is asserted.

**Classification ambiguity:** External SAP amendments are not supplied.

**Exact source locations:** Yes: PLAN [DOC-002 p.84, §15.2](../../../joi180132supp1_prod.pdf#page=84); REPORT [DOC-001 p.1, abstract primary results](../../../jama_cooper_2018_oi_180132.pdf#page=1), [p.3, primary statistical method](../../../jama_cooper_2018_oi_180132.pdf#page=3), [p.5, primary and ordinal outcomes](../../../jama_cooper_2018_oi_180132.pdf#page=5), [p.7, Table2](../../../jama_cooper_2018_oi_180132.pdf#page=7), and [DOC-003 p.22, post-hoc OR results](../../../joi180132supp2_prod.pdf#page=22). Full source-native search/read covered DOC-003 physical pages1–24: [1](../../../joi180132supp2_prod.pdf#page=1), [2](../../../joi180132supp2_prod.pdf#page=2), [3](../../../joi180132supp2_prod.pdf#page=3), [4](../../../joi180132supp2_prod.pdf#page=4), [5](../../../joi180132supp2_prod.pdf#page=5), [6](../../../joi180132supp2_prod.pdf#page=6), [7](../../../joi180132supp2_prod.pdf#page=7), [8](../../../joi180132supp2_prod.pdf#page=8), [9](../../../joi180132supp2_prod.pdf#page=9), [10](../../../joi180132supp2_prod.pdf#page=10), [11](../../../joi180132supp2_prod.pdf#page=11), [12](../../../joi180132supp2_prod.pdf#page=12), [13](../../../joi180132supp2_prod.pdf#page=13), [14](../../../joi180132supp2_prod.pdf#page=14), [15](../../../joi180132supp2_prod.pdf#page=15), [16](../../../joi180132supp2_prod.pdf#page=16), [17](../../../joi180132supp2_prod.pdf#page=17), [18](../../../joi180132supp2_prod.pdf#page=18), [19](../../../joi180132supp2_prod.pdf#page=19), [20](../../../joi180132supp2_prod.pdf#page=20), [21](../../../joi180132supp2_prod.pdf#page=21), [22](../../../joi180132supp2_prod.pdf#page=22), [23](../../../joi180132supp2_prod.pdf#page=23), [24](../../../joi180132supp2_prod.pdf#page=24). [DOC-004 p.1](../../../joi180132supp3_prod.pdf#page=1) supplies data-sharing statements, not such an output.

**Source evidence:** Yes. Final §15.2 promises an unadjusted RR and 95% CI, RD and 95% CI, and OR and 95% CI for midpoint-dichotomized primary GOSE.

**Reported-versus-comparator:** Yes. Main primary binary results give RR/RD, while OR 0.97(0.71–1.34), P=.88 is explicitly for ordinal GOSE. The supplement's OR 0.91(0.59–1.41) and adjusted0.95 result are explicitly post-hoc adequate-cooling58/124 versus 111/226; they do not match primary117/240 versus 111/226. Per-protocol, as-treated and missingness outputs are labeled RR, and their populations differ. No matched primary binary OR/CI is supplied.

**Reasoning procedure:** Yes, focus D and Route A category 5: an explicitly promised primary analysis output is absent from matched supplied reports.

**Calculation:** This is an output-presence and result-identity comparison; numeric rounding cannot turn an ordinal OR or adequate-cooling OR into the planned primary binary output. The crude odds-ratio identity would use117/(240−117) divided by111/(226−111), but recomputing it cannot substitute for a reported planned OR/CI and is not used as a numeric discrepancy.

**Affected result or extracted value:** Availability of the planned primary midpoint-dichotomized GOSE OR and 95% CI for 117/240 versus 111/226.

**Why context does not resolve it:** Route A, category 5 concerns an explicitly planned primary output absent from matched supplied reporting. Ordinal and post hoc subset ORs have different outcomes/populations and do not provide that output.

**Alternative source-grounded interpretations:** The published RR/RD may have been selected as the primary reporting format by an external/later SAP. That document is not supplied, and the distinct reported ORs do not resolve the matched-output absence.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. Direct primary-report renders and complete supplementary output search confirm only unmatched ordinal/subset ORs, while the final plan explicitly promises the matched binary primary OR/CI. Necessary inputs: Yes to identify the planned output and distinguish all supplied OR results. **Exact missing inputs or definitions:** The primary binary OR/CI output or a supplied operative amendment withdrawing that planned output. External SAP references supply pointers only and were not accessed. Direct observation and inference: The promise, report effect-measure labels and absent matched output are direct supplied-source observations. A reason for omission or undocumented amendment is not inferred. See the complete durable [C006 source recheck](../verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, evidence extraction could identify a planned primary OR/CI as unavailable in the supplied reports or associate an unmatched OR with that planned output. No replacement estimate is proposed.

Checker provenance: Included finding F-XS-004; duplicate findings None. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

## C007 — Survival analysis window

**Status:** Pending Human Adjudication

**Candidate statement:** The survival method states six-month censoring, while the corresponding supplementary curve retains positive risk sets at 200 and 250 days.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT DOC-001 pp.2,4–5 vs REPORT DOC-003 p.5

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-003

**Qualifying route:** Route B

**Classification rationale:** Confirmed. The comparison concerns a survival method and corresponding results in two reports; contextual main-page copies do not add an independent S_W conflict.

**Classification ambiguity:** Whether corresponding Cox and Kaplan–Meier windows truly coincide is unresolved.

**Exact source locations:** Yes: REPORT [DOC-001 p.2, Data Collection](../../../jama_cooper_2018_oi_180132.pdf#page=2), [p.4, Statistical Analysis survival method](../../../jama_cooper_2018_oi_180132.pdf#page=4), [DOC-003 p.5, eFigure2 plot, risk table and caption](../../../joi180132supp2_prod.pdf#page=5). The repeated HR result was also confirmed at [DOC-001 p.5, Secondary Outcomes](../../../jama_cooper_2018_oi_180132.pdf#page=5).

**Source evidence:** Yes. Follow-up is to death or six months after randomization; Cox analysis is described as censored at six months or last-known-contact, with corresponding Kaplan–Meier curves/log-rank test.

**Reported-versus-comparator:** Yes. Figure2's time axis is survival days; at 200 days risk sets are91/88 and at 250days23/17, with later censor ticks. Caption describes probability/risk of death at six months and HR 1.13(0.76–1.69), P=.54; plot log-rank P=.5349. These P values are compatible as differently labeled tests/display precision and are not an additional issue.

**Reasoning procedure:** Yes, focus C and Route B: the named survival result's censoring window is compared with its corresponding plotted risk process.

**Calculation:** Even a conservative upper bound of186 days for six calendar months is below200 days. Universal administrative censoring by that bound implies zero at-risk subjects at 200/250 days. Half-unit risk-count intervals at 200 days [90.5,91.5] and [87.5,88.5], and at 250 days [22.5,23.5] and [16.5,17.5], remain positive. Their gaps from zero exceed precision; for printed23 the minimum relative discrepancy is22.5/23=0.97826. Exact survival records are not required to establish this literal-window mismatch.

**Affected result or extracted value:** Observation/censoring horizon associated with mortality HR 1.13 (95% CI 0.76–1.69), P = .54.

**Why context does not resolve it:** The method and caption do not identify different Cox and Kaplan–Meier windows or an extended assessment allowance; therefore the horizon of the named HR is not identifiable from immediate context.

**Alternative source-grounded interpretations:** Six-month assessment may allow delayed contact, or Cox and Kaplan–Meier presentations may use different windows. The stated corresponding-curve method and caption do not specify either distinction.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. Direct-source eFigure2 retains positive risk sets beyond any literal six-calendar-month cutoff while the main method states such a cutoff. Necessary inputs: Yes for rule-versus-plot comparison. **Exact missing inputs or definitions:** Actual administrative cutoff, definition of six-month assessment window, event/censor times, and whether Cox and plot used identical datasets/windows. Direct observation and inference: Printed censor rule, caption and positive risk sets are direct. A changed HR or significance conclusion is not inferred. See the complete durable [C007 source recheck](../verification/evidence_recheck.md).

**Potential downstream evidence impact:** If confirmed, an extractor could attach a six-month or longer observation horizon to the reported survival result. No revised HR or significance assessment is established.

Checker provenance: Included finding F-ST1-003; duplicate findings None. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

## C008 — Cooling-time equal-proportions test

**Status:** Pending Human Adjudication

**Candidate statement:** The registered count-to-P comparison for cooling-time categories is retained as a candidate reporting issue with not_reproduced evidence: permitted half-unit inputs reconcile with P = .09.

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Compared document roles:** REPORT DOC-001 pp.4–5 vs REPORT DOC-003 p.11; REPORT DOC-003 same-display counts and P

**Evidence state:** not_reproduced

**Inclusion audit:** QUESTIONED

The audit questions inclusion because half-unit inputs reproduce the printed .09 and no matched global estimate/interval/test establishes Route A category 1.

**Finding IDs:** F-ST1-004

**Qualifying route:** Route A, category 1

This is the historical registration route; the current recheck and audit do not establish its reproduction or category-1 linkage.

**Classification rationale:** Relationship/domain fields describe the registered comparisons and are retained. Evidence state records their precision reconciliation; stable identity is unchanged.

**Classification ambiguity:** The global table P's exact implementation is not identified; the claimed category 1 interval/test linkage is absent.

**Exact source locations:** Yes: REPORT [DOC-001 p.4, favorable outcome versus time-to33°C method](../../../jama_cooper_2018_oi_180132.pdf#page=4), [p.5, Additional Outcomes nonsignificance statement](../../../jama_cooper_2018_oi_180132.pdf#page=5), [DOC-003 p.11, eTable7 four categories and P value](../../../joi180132supp2_prod.pdf#page=11).

**Source evidence:** Yes. Main states an unadjusted chi-square test for equal proportions in cooled patients and nonsignificant results. Table labels four categories1–7h,8–13h,>13h,Never; totals 49,67,59,65; favorable counts 18,28,32,39; P=.09. Individual percentages36.7,41.8,54.2,60.0 have marginal95% CIs 22.8–50.7,29.6–53.9,41.2–67.3,47.8–72.2.

**Reported-versus-comparator:** Confirmed four-category totals 49, 67, 59, 65 and favorable counts 18, 28, 32, 39 versus printed P = .09. The main method names an equal-proportions chi-square test; the individual CIs are marginal proportion intervals.

**Reasoning procedure:** The count-based P recomputation is applicable, but the registered Route A category 1 exemption is not established. Its definition concerns a printed estimate/interval versus P/test conflict, a P/test unable to belong to a printed estimate/interval, or point-estimate containment. Here the printed intervals are marginal proportion intervals, not a global contrast CI; they overlap a common proportion, and there is no printed global test statistic or global effect interval contradicting P=.09. Recomputed exact-count significance alone is not such a printed interval/P conflict. The mandatory display rule therefore applies to this recomputation.

**Calculation:** Pool 117/240. Pearson statistic sum over groups of (a_i−n_i*117/240)^2/[n_i*(117/240)*(123/240)] =8.133762156, df 3; P=.04332664. Restricting to the three reaching-target categories gives3.658952, df 2, P=.16050, also a different exact-count result. Allowing every displayed count/denominator its required half-unit range, admissible numerators(18.5,28.5,31.5,38.5) with totals(48.5,66.5,59.5,65.5) give chi-square6.162765031, df 3, P=.10395436. Along the continuous path from printed centers to these permitted endpoints, the recomputed P interval includes [.04332664,.10395436], hence overlaps the printed [.085,.095] range. Gap0; relative discrepancy 0. This is an interval-arithmetic feasibility check, not a claim that fractional participants were observed. Printed percentages are outputs of the same display, not additional count inputs to this stated-count recomputation.

**Affected result or extracted value:** Association-test attribution for favorable primary GOSE across the four cooling-time categories; the registered numerical inconsistency does not survive the required precision check.

**Why context does not resolve it:** The historical Route A, category 1 justification is disputed: no printed matched global estimate/interval/test statistic establishes that category, and the count-to-P comparison reconciles under the prescribed half-unit rule. There is no current reproduced inconsistency to support that route.

**Alternative source-grounded interpretations:** A different subset or categorical implementation may generate.09; the main method and table do not distinguish it. The reported marginal CIs and nonsignificance statement reconcile with.09. No marginal-CI/global-test conflict is reproduced.

**Mechanical evidence recheck:** All listed source locations were found and the source/comparator readings matched. The recomputed P range overlaps [.085,.095], and no printed global estimate/CI or test statistic establishes a Route A category 1 exception. Thus the numerical comparison reconciles under the required display rule despite the exact-count diagnostic difference. Necessary inputs: Yes for the prescribed precision check. **Exact missing inputs or definitions:** Exact test implementation/group inclusion that generated.09 is absent, but no missing definition is needed to establish the mandatory interval overlap. Direct observation and inference: The exact-count diagnostic difference is observed computationally; the reported count-to-P inconsistency does not survive the normative half-unit rule. A different analysis or production mechanism is not established. See the complete durable [C008 source recheck](../verification/evidence_recheck.md).

**Potential downstream evidence impact:** The retained card records a questioned historical comparison and its precision reconciliation. It does not support copying an alternative P value or assuming a changed significance conclusion; exact test attribution remains unspecified.

Checker provenance: Included finding F-ST1-004; duplicate findings None. All duplicate source locations are retained in the consolidated source evidence below. The classification-table Finding IDs field records INCLUDE rows only; duplicate provenance is separately preserved.

