# Candidate Ledger

All candidates are Pending Human Adjudication. Ten stable IDs were registered only after the independent initial screen. Ordering follows the earliest cited REPORT page in source DOC-001; ties follow the screener's source-linked G-group order. This is source order, not a ranking. Duplicate finding IDs remain in provenance; the classification table's Finding IDs contains only INCLUDE findings. Mechanical recheck supplies reproduced for all ten; the final audit supplies CONFIRMED for nine and QUESTIONED for C001. These fields do not adjudicate any candidate.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | report_internal_inconsistency | S_C | S_C, S_W | REPORT main article pp.1,6 vs REPORT results supplement pp.2,4 | reproduced | QUESTIONED | F-XS-001 |
| C002 | statistical_results | S_W | S_W | REPORT main article pp.1,4,5,6 vs REPORT main article Figure3 p.7 | reproduced | CONFIRMED | F-XS-002 |
| C003 | protocol_report | P_R | P_R | PLAN protocol p.55 and SAP pp.82,105 vs REPORT main article pp.1,4,6 and results supplement pp.4,5 | reproduced | CONFIRMED | F-XS-004 |
| C004 | protocol_report | P_R | P_R | PLAN SAP pp.82,105 vs REPORT main article pp.1,4,5,6 | reproduced | CONFIRMED | F-XS-005 |
| C005 | protocol_report | P_R | P_R | PLAN SAP pp.82,105 vs REPORT main article pp.1,4,5,6 | reproduced | CONFIRMED | F-XS-006 |
| C006 | protocol_report | P_R | P_R, S_W | PLAN strata pp.98,99 and SAP p.104 vs REPORT main article pp.2,4,7 | reproduced | CONFIRMED | F-XS-008 |
| C007 | protocol_report | P_R | P_R | PLAN original/final SAP pp.82,104 vs REPORT main article pp.3,5 | reproduced | CONFIRMED | F-XS-003 |
| C008 | protocol_report | P_R | P_R | PLAN original/final SAP pp.82,104,105 vs REPORT main article pp.3,4,5,8 | reproduced | CONFIRMED | F-ST1-003 |
| C009 | protocol_report | P_R | P_R | PLAN rationale pp.95,96 and intervention p.99 vs REPORT main article pp.3,5 | reproduced | CONFIRMED | F-XS-007 |
| C010 | protocol_report | P_R | P_R | PLAN final SAP p.104 vs REPORT main article pp.1-9 and results supplement pp.1-5 | reproduced | CONFIRMED | F-ST1-005 |

## C001 — Oxygenation result time and population attribution

**Status:** Pending Human Adjudication
**Evidence state:** reproduced
**Finding IDs:** F-XS-001
**Checker provenance:** Cross-source G01; duplicate F-ST1-009. Statistical relationships S007, S032, S033.
**Candidate statement:** The abstract defines oxygenation over three days after intubation, while its descriptive result matches the six-hour-after-randomization table; the time/population of the associated mean contrast remains unclear.
**Exact source locations:** REPORT [main abstract p.1](../../jama_azoulay_2018_oi_180109.pdf#page=1), [secondary results p.6](../../jama_azoulay_2018_oi_180109.pdf#page=6); REPORT [results eTable p.2](../../joi180109supp2_prod.pdf#page=2), [eFigure2 p.4](../../joi180109supp2_prod.pdf#page=4). PLAN p.103 is corroboration only, and does not state after intubation.
**Source evidence:** Abstract outcome window says three days after intubation; report gives 150 versus119, mean difference19.5 (95% CI4.4–34.6). The eTable labels 150 [104–230] versus119 [86–165] as six hours after randomization; eFigure2 time axis is randomization-based.
**Reasoning procedure:** Match the descriptive pair before comparing the named window and population; do not equate medians with mean differences.
**Calculation:** Direct label comparison; descriptive pair150/119 matches exactly. No inferred model or postintubation subgroup denominator.
**Affected result or extracted value:** Time and population attribution of the abstract oxygenation result150/119 and19.5 (4.4–34.6).
**Why context does not resolve it:** Registration identified different explicit endpoint-definition and table windows. The final audit questions this criterion: the abstract's same coordinated results sentence places the higher oxygenation and lower respiratory-rate comparison after six hours, and the matching eTable expressly labels six hours after randomization. This immediate-context reading may resolve result attribution at once; unreported oxygenation-model details do not independently qualify.
**Alternative source-grounded interpretations:** Six-hour randomized-arm comparison or separately defined postintubation trajectory; source does not establish the latter for this tuple.
**Classification rationale:** Two REPORT documents conflict, with an additional within-main comparison; P_R is absent because PLAN does not conflict.
**Classification ambiguity:** Oxygenation contrast's precise measurement window and model remain unspecified; direct recheck must preserve this limitation.
**Human question:** Which time origin, population and measurement window apply to the reported oxygenation comparison?

## C002 — Forest-plot HR reference and favor direction

**Status:** Pending Human Adjudication
**Evidence state:** reproduced
**Finding IDs:** F-XS-002
**Checker provenance:** Cross-source G02; duplicate F-ST1-001. Statistical relationships S012, S018, S039 through S076.
**Candidate statement:** Identical overall event counts carry oppositely oriented HRs in Table2 and Figure3, while forest favor labels retain the same direction convention.
**Exact source locations:** REPORT [abstract p.1](../../jama_azoulay_2018_oi_180109.pdf#page=1), [subgroup methods p.4](../../jama_azoulay_2018_oi_180109.pdf#page=4), [Table2 p.5](../../jama_azoulay_2018_oi_180109.pdf#page=5), [results p.6](../../jama_azoulay_2018_oi_180109.pdf#page=6), [Figure3 p.7](../../jama_azoulay_2018_oi_180109.pdf#page=7). Affected pattern: both panels, both all-patient rows, all24 subgroup rows, and both favor-label pairs; every tuple retained in main map M084–M109 and S039–S064.
**Source evidence:** Table mortality138/388 versus140/388, HR0.98 (0.77–1.24); forest same counts, HR1.02 (0.81–1.29). Table ventilation150/388 versus170/388, HR0.85 (0.68–1.06); forest same counts, HR1.17 (0.94–1.46). Below1 favors HFNO and above1 favors standard in both forest panels.
**Reasoning procedure:** Compare matched model-based all-patient HRs and forest reference/favor labels; crude risk ratios are not the proof.
**Calculation:** Half-unit ranges mortality[.975,.985) vs[1.015,1.025), ventilation[.845,.855) vs[1.165,1.175) are disjoint. Reciprocal diagnostics1/.98=1.0204 and1/.85=1.1765 suggest contrast reversal; model coding is unprinted.
**Affected result or extracted value:** Mortality/ventilation HR reference group, including nonhematologic ventilation HR1.61 (1.16–2.23), and all forest-row favor interpretations.
**Why context does not resolve it:** Neither caption nor methods identifies a reversal explaining the simultaneous effect and favor conventions.
**Alternative source-grounded interpretations:** Reciprocal reference coding in forest or differently oriented analyses; source does not identify which applies.
**Classification rationale:** Conflicting effect and label locations are within one REPORT document; S_W/statistical_results.
**Classification ambiguity:** Exact fitted-model reference coding unavailable; no claim that every subgroup estimate is a crude ratio.
**Human question:** Which contrast and favor direction apply to each panel and its subgroup estimates?

## C003 — Planned longitudinal joint models and reported rank comparisons

**Status:** Pending Human Adjudication
**Evidence state:** reproduced
**Finding IDs:** F-XS-004
**Checker provenance:** Cross-source G05; duplicate F-ST1-004. Statistical relationships S034–S036.
**Candidate statement:** The plan prescribes joint longitudinal models accounting for right censoring, while the report explicitly specifies rank-sum comparisons for comfort and dyspnea.
**Exact source locations:** PLAN [protocol p.55 lines825–826](../../joi180109supp1_prod.pdf#page=55), [original SAP p.82 lines1314–1315](../../joi180109supp1_prod.pdf#page=82), [final SAP p.105 lines1745–1747](../../joi180109supp1_prod.pdf#page=105); REPORT [abstract p.1](../../jama_azoulay_2018_oi_180109.pdf#page=1), [methods p.4](../../jama_azoulay_2018_oi_180109.pdf#page=4), [results p.6](../../jama_azoulay_2018_oi_180109.pdf#page=6), [eFigure2 p.4](../../joi180109supp2_prod.pdf#page=4), [eFigure3 p.5](../../joi180109supp2_prod.pdf#page=5).
**Source evidence:** Joint models taking account of right censoring are planned for oxygenation, dyspnea and comfort; report names Wilcoxon rank-sum for comfort/dyspnea and no differences at any time.
**Reasoning procedure:** Compare explicitly named analytical methods and the secondary conclusions they support, preserving final-plan version context.
**Calculation:** Logical method comparison; no exact graphical effect or variance assumed.
**Affected result or extracted value:** Abstract-reported comfort/dyspnea treatment conclusions and their analytical basis.
**Why context does not resolve it:** The explicit rank-sum description does not explain the relationship to the final joint-model prescription.
**Alternative source-grounded interpretations:** Rank comparisons replaced the planned joint models or both were run with only rank results reported.
**Classification rationale:** PLAN versus REPORT model specification; P_R/protocol_report. Oxygenation is contextual because its actual reported model is not specified.
**Classification ambiguity:** No independent claim that an oxygenation joint model was replaced; pointwise contributor-count differences are excluded.
**Human question:** Which models generated the comfort/dyspnea conclusions, and how do they relate to the plan?

## C004 — Infection competing-risk plan and reported proportion test

**Status:** Pending Human Adjudication
**Evidence state:** reproduced
**Finding IDs:** F-XS-005
**Checker provenance:** Cross-source G06; duplicate F-ST1-007. Statistical relationships S022–S024.
**Candidate statement:** Planned infection cumulative-incidence/Gray analysis differs from the reported comparison of proportions by chi-square.
**Exact source locations:** PLAN [original SAP p.82 lines1305–1310](../../joi180109supp1_prod.pdf#page=82), [final SAP p.105 lines1738–1742](../../joi180109supp1_prod.pdf#page=105); REPORT [abstract p.1](../../jama_azoulay_2018_oi_180109.pdf#page=1), [methods p.4](../../jama_azoulay_2018_oi_180109.pdf#page=4), [Table2 p.5](../../jama_azoulay_2018_oi_180109.pdf#page=5), [results p.6](../../jama_azoulay_2018_oi_180109.pdf#page=6).
**Source evidence:** Plan death or alive ICU discharge competing with infection, Gray test and adjusted cause-specific Cox; report proportions/chi-square,39/388 vs41/388, RD−.6% (−4.6,4.1), cause-specific HR1.01 (.96,1.06), P=.91.
**Reasoning procedure:** Compare planned estimator/test to explicit reported test, without deriving a Cox interval from crude counts.
**Calculation:** Source-grounded method comparison. The numerical P can reconcile with a continuity-adjusted chi-square; its arithmetic is not the issue.
**Affected result or extracted value:** ICU-acquired infection treatment comparison and attribution of its RD, HR and P value.
**Why context does not resolve it:** The reported cause-specific HR does not identify the planned cumulative-incidence/Gray result or reconcile the explicit proportion-test description.
**Alternative source-grounded interpretations:** Proportion test replaced the planned framework, or additional competing-risk results are not identified.
**Classification rationale:** PLAN versus REPORT analytical specification; P_R/protocol_report.
**Classification ambiguity:** Infection model adjustment and HR interval algorithm are not established; no separate variance contradiction is claimed.
**Human question:** Which estimator, competing events and test generated the infection comparison?

## C005 — ICU-stay analysis specification

**Status:** Pending Human Adjudication
**Evidence state:** reproduced
**Finding IDs:** F-XS-006
**Checker provenance:** Cross-source G07; duplicate F-ST1-006. Statistical relationships S027, S029.
**Candidate statement:** Planned ICU-stay survival/competing-risk analyses and survivor/death-separated populations differ from the pooled rank-sum analysis reported.
**Exact source locations:** PLAN [original SAP p.82 lines1311–1313](../../joi180109supp1_prod.pdf#page=82), [final SAP p.105 lines1742–1745](../../joi180109supp1_prod.pdf#page=105); REPORT [abstract p.1](../../jama_azoulay_2018_oi_180109.pdf#page=1), [methods p.4](../../jama_azoulay_2018_oi_180109.pdf#page=4), [Table2 p.5](../../jama_azoulay_2018_oi_180109.pdf#page=5), [results p.6](../../jama_azoulay_2018_oi_180109.pdf#page=6).
**Source evidence:** Plan ICU stay overall and separately in survivors/dead using Kaplan–Meier/competing-risk estimators, preserving former/latter wording. Report Wilcoxon rank-sum, medians8 vs6days, mean difference.6days (−1.0,2.2), P=.07.
**Reasoning procedure:** Compare method and population specifications; median difference2days is not equated with mean difference.6days.
**Calculation:** Logical method/population comparison; no event coding or survival result inferred.
**Affected result or extracted value:** Abstract-reported ICU-stay contrast and the population/estimand associated with.6days and P=.07.
**Why context does not resolve it:** No supplied analysis-change explanation connects the explicit pooled rank-sum method to the final prospective estimators and population split.
**Alternative source-grounded interpretations:** Rank-sum replaced the prospective analyses, or both were run but only pooled results are identifiable.
**Classification rationale:** PLAN versus REPORT analytical specification; P_R/protocol_report.
**Classification ambiguity:** Plan former/latter phrase does not identify every event coding; preserve without choosing one.
**Human question:** Which ICU-stay method and population produced the reported comparison?

## C006 — Prospective and displayed subgroup boundaries

**Status:** Pending Human Adjudication
**Evidence state:** reproduced
**Finding IDs:** F-XS-008
**Checker provenance:** Cross-source G09; duplicate F-ST1-008. Statistical relationships S006, S038, S039, S040, S052, S053, S065, S071.
**Candidate statement:** The displayed predefined time subgroups include day2 in the late group, whereas planned/reported randomization strata include it in the early group.
**Exact source locations:** PLAN [strata pp.98](../../joi180109supp1_prod.pdf#page=98), [99 lines1600–1604](../../joi180109supp1_prod.pdf#page=99), [final SAP p.104 lines1721–1722](../../joi180109supp1_prod.pdf#page=104); REPORT [randomization p.2](../../jama_azoulay_2018_oi_180109.pdf#page=2), [subgroup methods/Table1 p.4](../../jama_azoulay_2018_oi_180109.pdf#page=4), [Figure3 p.7](../../jama_azoulay_2018_oi_180109.pdf#page=7), both time rows in each panel and accompanying oxygen-flow rows.
**Source evidence:** Plan D0,D1,D2 vs≥D3; report strata≤2 vs≥3days. Figure bins0–1 vs≥2days; early totals321/330, late67/58; Table1 day2 counts47/38,≥day3counts20/20. Mortality time-interaction P=.15; ventilation P=.17. Oxygen threshold plan<9/≥9 vs report≤9/>9 also retained as conditional context.
**Reasoning procedure:** Reconcile displayed membership with Table1 day counts, then compare the predefined-strata claim to its planned boundary.
**Calculation:** H early244+77=321, late47+20=67; C early251+79=330, late38+20=58. Planned late≥D3 is20/20. Equality-at9L/min membership is unprinted and is not inferred.
**Affected result or extracted value:** Time-subgroup mortality/ventilation HR populations and prospective attribution of interaction P=.15/.17.
**Why context does not resolve it:** No explanation identifies a prospective different binning, while explicit counts demonstrate moved day2 membership.
**Alternative source-grounded interpretations:** Intended different subgroup rule or display of the original strata; package does not identify which was prospective.
**Classification rationale:** Both PLAN/REPORT and within-REPORT comparisons apply; P_R has precedence over S_W, giving protocol_report.
**Classification ambiguity:** Oxygen equality boundary does not independently establish any changed membership/result; retain only as qualified context.
**Human question:** What were the prespecified analysis subgroup boundaries and which populations do the displayed HRs represent?

## C007 — Primary relative-risk plan and reported hazard ratio

**Status:** Pending Human Adjudication
**Evidence state:** reproduced
**Finding IDs:** F-XS-003
**Checker provenance:** Cross-source G03; duplicate F-ST1-002. Adjustment component of F-XS-003 belongs to C008. Statistical relationship S010.
**Candidate statement:** The plan specifies a binary day28 relative risk, while the report identifies a Cox hazard ratio as its primary relative effect, with no primary day28 RR reported.
**Exact source locations:** PLAN [original SAP p.82 lines1297–1300](../../joi180109supp1_prod.pdf#page=82), [final SAP p.104 lines1731–1734](../../joi180109supp1_prod.pdf#page=104); REPORT [primary methods p.3](../../jama_azoulay_2018_oi_180109.pdf#page=3), [Table2 p.5](../../jama_azoulay_2018_oi_180109.pdf#page=5). REPORT p.8 is adjustment context in C008.
**Source evidence:** Plan alive/dead by28days and experimental/control relative risk of hospital death with95%CI; report Kaplan–Meier, risk difference and univariable Cox HR0.98 (.77,1.24). ICU/hospital RRs are different endpoints.
**Reasoning procedure:** Compare supplied effect-measure/model specifications after final-plan version matching; isolate effect identity from covariate adjustment.
**Calculation:** Logical RR-versus-HR comparison; numerical closeness does not make the estimands identical.
**Affected result or extracted value:** Primary mortality effect-measure identity and availability of the planned primary RR result.
**Why context does not resolve it:** Disclosed grant-stage redesign does not explain this difference against the final superiority SAP.
**Alternative source-grounded interpretations:** Primary HR intentionally replaced RR, or the planned RR is not identifiable in supplied report content.
**Classification rationale:** PLAN versus REPORT primary estimand/model; P_R/protocol_report. Separate C008 applies the independent adjustment rule.
**Classification ambiguity:** Hospital-death wording in the immediate binaryday28 clause is context-resolved and not a separate endpoint issue.
**Human question:** Which final primary estimand was intended and how does the reported HR relate to the planned RR?

## C008 — Planned covariate adjustment and explicit univariable models

**Status:** Pending Human Adjudication
**Evidence state:** reproduced
**Finding IDs:** F-ST1-003
**Checker provenance:** Statistical G04; adjustment component of F-XS-003 retained without a second screening row. Statistical relationships S011, S021.
**Candidate statement:** Planned confounder adjustment for primary and ventilation effects differs from the report's explicitly univariable models.
**Exact source locations:** PLAN [original SAP p.82 lines1300–1310](../../joi180109supp1_prod.pdf#page=82), [final SAP p.104 line1734](../../joi180109supp1_prod.pdf#page=104), [p.105 line1742](../../joi180109supp1_prod.pdf#page=105); REPORT [methods p.3](../../jama_azoulay_2018_oi_180109.pdf#page=3), [methods p.4](../../jama_azoulay_2018_oi_180109.pdf#page=4), [Table2 p.5](../../jama_azoulay_2018_oi_180109.pdf#page=5), [limitations p.8](../../jama_azoulay_2018_oi_180109.pdf#page=8).
**Source evidence:** Plan primary potential-confounder adjustment and secondary adjusted cause-specific Cox. Report univariable mortality and ventilation Cox estimates; mortality HR.98 (.77,1.24), ventilation HR.85 (.68,1.06); p.8 acknowledges estimates not adjusted on stratification factors.
**Reasoning procedure:** Compare explicit adjustment specifications across the same primary and key secondary treatment effects. No specific unprinted confounder is assigned.
**Calculation:** Logical adjusted/univariable comparison, independent of RR/HR identity.
**Affected result or extracted value:** Adjustment designation and prospective analytical basis of the mortality/ventilation effects.
**Why context does not resolve it:** Acknowledging absent stratification adjustment does not identify the prescribed adjusted results or a reconciled final specification.
**Alternative source-grounded interpretations:** Univariable models replaced planned adjusted models, or adjusted results were additional but are not identifiable.
**Classification rationale:** PLAN versus REPORT model specification; P_R/protocol_report. One repeated adjustment pattern spans mortality and ventilation.
**Classification ambiguity:** Specific confounders unspecified; infection model is not asserted univariable.
**Human question:** Which final adjustment specification applied to these two treatment estimates?

## C009 — Comparator rescue-HFNO permission

**Status:** Pending Human Adjudication
**Evidence state:** reproduced
**Finding IDs:** F-XS-007
**Checker provenance:** Cross-source G08.
**Candidate statement:** The report expressly permits comparator-arm HFNO rescue that the final plan categorically excludes.
**Exact source locations:** PLAN [rationale p.95](../../joi180109supp1_prod.pdf#page=95), [p.96](../../joi180109supp1_prod.pdf#page=96), [intervention p.99 lines1616–1625](../../joi180109supp1_prod.pdf#page=99); REPORT [treatments/Figure1 p.3](../../jama_azoulay_2018_oi_180109.pdf#page=3), [interventions p.5](../../jama_azoulay_2018_oi_180109.pdf#page=5).
**Source evidence:** Plan HFNO not used in control; report allows rescue for do-not-intubate controls after standard failure;30(7.7%) received HFNO,14(46.7%) died; Figure1 records30 control HFNO recipients.
**Reasoning procedure:** Compare explicit comparator strategy rules, not individual clinical appropriateness or mere occurrence of crossover.
**Calculation:**30/388=7.732%,14/30=46.667%; descriptive arithmetic reconciles and is not the issue.
**Affected result or extracted value:** Comparator intervention definition underlying primary mortality and day28 ventilation effects.
**Why context does not resolve it:** Report explains the rescue condition but does not reconcile permission with final-plan prohibition.
**Alternative source-grounded interpretations:** Intentional final-strategy change or individual departures from the plan; no conclusion about either is assigned.
**Classification rationale:** PLAN versus REPORT randomized comparator rule; P_R/protocol_report.
**Classification ambiguity:** No supplied amendment identifies this rescue permission as a reconciled prospective change.
**Human question:** Was permitted rescue part of the intended final comparator strategy, and how is it reconciled with the supplied plan?

## C010 — Prespecified per-protocol primary result unavailable

**Status:** Pending Human Adjudication
**Evidence state:** reproduced
**Finding IDs:** F-ST1-005
**Checker provenance:** Statistical G10; cross-source exclusion of this observation was independently reconsidered by the screener. Statistical relationship S037.
**Candidate statement:** The final plan unconditionally promises a per-protocol analysis in the primary-analysis methodology, but supplied REPORT materials identify only the ITT primary result.
**Exact source locations:** PLAN [final SAP p.104 lines1717–1723](../../joi180109supp1_prod.pdf#page=104); REPORT [primary methods p.3](../../jama_azoulay_2018_oi_180109.pdf#page=3), [methods p.4](../../jama_azoulay_2018_oi_180109.pdf#page=4), [results p.5](../../jama_azoulay_2018_oi_180109.pdf#page=5), [p.6](../../jama_azoulay_2018_oi_180109.pdf#page=6), [p.7](../../jama_azoulay_2018_oi_180109.pdf#page=7); absence search covers REPORT main pp.1–9 and results supplement pp.1–5, with data-sharing statement p.1 administrative only.
**Source evidence:** Plan says per-protocol analysis will be performed. Report ITT excludes withdrawn consent only,388 perarm, with no PP definition, population or day28 mortality effect.
**Reasoning procedure:** Compare an express prospective primary-analysis promise with complete supplied-report coverage; focusD expressly includes a prespecified primary analysis not reported.
**Calculation:** No PP denominator inferred from12/30 treatment changes or other deviations.
**Affected result or extracted value:** Availability of prespecified primary per-protocol mortality population/result.
**Why context does not resolve it:** Conditional missingness and disclosed early design changes do not explain the unconditionally stated final primary sensitivity analysis.
**Alternative source-grounded interpretations:** PP was performed but not reported, or the final analysis promise changed; package does not establish which.
**Classification rationale:** PLAN versus REPORT primary sensitivity-result availability; P_R/protocol_report.
**Classification ambiguity:** Absence is limited to supplied report content; no claim that the analysis was never performed or that its result differs from ITT.
**Human question:** What population and result implement the promised per-protocol primary analysis, or what supplied reconciliation explains its replacement?
