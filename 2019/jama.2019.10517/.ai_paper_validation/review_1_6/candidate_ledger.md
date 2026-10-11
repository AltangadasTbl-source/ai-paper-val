# Workflow 1.6 Stable Quality-Control Candidate Ledger

**Pending Human Adjudication.** Discovery restarted from supplied source-linked evidence, all 63 mapped pages, 400 numeric relationships, complete statistical pass 1, and 70 cross-source matching families. There is no candidate-count limit. Fifteen distinct candidates are registered below; every assigned ID is permanent. The fresh direct-source recheck is complete: fourteen recorded_candidate states map to retain; C009 is record_input_error and maps to discuss because its numerical comparison lacks an established scale/estimand alignment.

Duplicate merge rule: merge only the same printed inputs, comparator and consistency rule. HbA1c observations from numeric first/last, cross-source and statistical lanes become C005. SAS label observations become C009. Recruitment observations become C010. Historical completion observations become C013. The minimum-duration cross-source card becomes part of C014, whose numeric lane also records the permitted extension. DKEFS and UKU duplicate lane observations become C003 and C004. Separate total-cholesterol and LDL outcomes remain C007 and C008, with separate matched result identities. The statistical lane did not emit convention-only df, F/SD, P/CI, NNT or link-model complaints; those limitations remain in its coverage records.

Classification is confirmed by direct-source recheck. The role of each compared location is assigned by content, not filename; historical protocol data are PLAN. A corroborating plan is not a conflicting comparison. Table evidence/disposition fields below reproduce the fresh evidence rechecker facts; these are mechanical pre-fills and every candidate remains Pending Human Adjudication.

| ID | Primary category | Relationship type | All relationships | Compared document roles | Review domain | Evidence state | Suggested review disposition |
|---|---|---|---|---|---|---|---|
| C001 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main Table1 arm headers vs hyperlipidemia cells | statistical_results | recorded_candidate | retain |
| C002 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main Table1 placebo header vs living-arrangement categories | statistical_results | recorded_candidate | retain |
| C003 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main Table2 DKEFS row marker vs scale footnotes | report_internal_inconsistency | recorded_candidate | retain |
| C004 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main UKU item range vs adverse-effect criterion | report_internal_inconsistency | recorded_candidate | retain |
| C005 | Measure, label, or scale inconsistency | S_C | S_C, S_W | REPORT main HbA1c coefficient vs main Table4 and REPORT results eFigure8 units | report_internal_inconsistency | recorded_candidate | retain |
| C006 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main hospitalization count fraction vs printed percentage | statistical_results | recorded_candidate | retain |
| C007 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main Table5 total-cholesterol counts vs unadjusted difference | statistical_results | recorded_candidate | retain |
| C008 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main Table5 LDL counts vs unadjusted difference | statistical_results | recorded_candidate | retain |
| C009 | Measure, label, or scale inconsistency | S_C | S_C | REPORT main weekly SAS points label vs REPORT results eFigure9 score trajectories | report_internal_inconsistency | record_input_error | discuss |
| C010 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN recruitment paragraph vs PLAN Table4 and overall target | plan_material | recorded_candidate | retain |
| C011 | Measure, label, or scale inconsistency | P_P | P_P | PLAN MMSE threshold heading vs PLAN operational phase labels | plan_material | recorded_candidate | retain |
| C012 | Denominator, proportion, or total inconsistency | P_P | P_P | PLAN historical 35% fraction-of-relapses wording vs PLAN participant-risk framing | plan_material | recorded_candidate | retain |
| C013 | Denominator, proportion, or total inconsistency | P_P | P_P | PLAN historical Table5 race vs ethnicity Week6 completion partitions | plan_material | recorded_candidate | retain |
| C014 | Numeric or arithmetic inconsistency | P_P | P_P | PLAN pre-RCT exposure range vs PLAN phase durations and allowed extension | plan_material | recorded_candidate | retain |
| C015 | Measure, label, or scale inconsistency | P_R | P_R | REPORT relapse HDRS threshold vs PLAN threshold and five-point-rise qualifier | protocol_report | recorded_candidate | retain |

## C001 — Hyperlipidemia percentages do not reconcile with arm denominators

**Provenance:** RF-CAND-01, local RF072 (stable alias in relationships/numeric_id_map.tsv); numeric-report-first runtime 01a1286a-6645-7930-8d1b-45686ffab070.
**Exact source locations:** [Main PDF p.5, Table1](../../jama_flint_2019_oi_190079.pdf#page=5), REPORT column headers and hyperlipidemia row.
**Source evidence:** Olanzapine n=64, hyperlipidemia 18(29.0%); placebo n=62, 19(29.7%). No row-specific n or denominator footnote is supplied.
**Rule and calculation:** 100×18/64=28.125%→28.1%; 100×19/62=30.645161%→30.6%. Printed percentages lie outside the ±0.05 percentage-point nearest-rounding tolerance. Using opposite denominators yields 18/62→29.0% and 19/64→29.7%.
**Observation versus inference:** Printed counts, percentages and headers conflict under the stated column denominators. Opposite denominators reproduce the numbers diagnostically, without establishing a production mechanism.
**Alternatives and human question:** A reduced olanzapine denominator62 could explain one cell; placebo29.7% with count19 would require about64, exceeding its n62. Determine intended counts, arm placement and denominators. No correction is assigned.
**Classification rationale:** One REPORT table; S_W; denominator category derives statistical_results. **Classification ambiguity:** Unprinted row denominator or arm assignment.

## C002 — Placebo living-arrangement rows account for 60 of 62 participants

**Provenance:** RF-CAND-02, RF078; numeric-report-first runtime above.
**Exact source locations:** [Main PDF p.5, Table1](../../jama_flint_2019_oi_190079.pdf#page=5), REPORT placebo header and living-arrangement block.
**Source evidence:** Placebo n62; with others49(79.0%), alone10(16.1%), senior residence1(1.6%). No other/missing category or reduced n is printed. Olanzapine46+17+1=64 is a corroborating control.
**Rule and calculation:** 49+10+1=60; deficit62−60=2; displayed percentages sum96.7%. Two participants are 3.225806% of62. Individual percentages use62 correctly; displayed rounding cannot remove the integer deficit.
**Observation versus inference:** The listed category counts do not cover the header population. A complete partition is conditional because exhaustiveness and missingness are not explicitly defined.
**Alternatives and human question:** Are the two participants missing/unlisted, was a count misprinted, and is62 the intended percentage denominator? An intentionally incomplete category block could explain it, but needs a stated missingness definition.
**Classification rationale:** Internal REPORT total/missingness comparison; S_W; statistical_results. **Classification ambiguity:** Whether categories were intended as exhaustive.

## C003 — DKEFS color-word row carries a Barnes scale footnote

**Provenance:** RF-CAND-03 (RF087), CROSS-CAND-03; numeric-report-first and cross-source runtime 01a1286a-f59b-7f01-8800-04b775b11953.
**Exact source locations:** [Main PDF p.6, Table2](../../jama_flint_2019_oi_190079.pdf#page=6), REPORT DKEFS color-word row and footnotes h/i.
**Source evidence:** DKEFS color-word condition3 means8.6(2.9) and7.6(2.8), superscript i. Footnote i names Barnes global akathisia range0–5, higher worse. Footnote h defines both DKEFS tasks, scaled1–19, higher better. The Barnes row lacks i.
**Rule and calculation:** A row's measure/range must match its attached footnote. Means8.6 and7.6 exceed attached maximum5 by3.6 and2.6; rounding cannot explain it. Both are inside DKEFS1–19.
**Observation versus inference:** A printed marker-to-measure conflict, not proof the cognitive values are incorrect. A displaced marker is a possible explanation.
**Alternatives and human question:** Does h cover both DKEFS tasks, and is i intended for Barnes? Inspect original superscripts and intended scale associations.
**Classification rationale:** One REPORT table; S_W; measure category derives report_internal_inconsistency. **Classification ambiguity:** Intended marker placement.

## C004 — UKU criterion includes score 4 outside its stated range

**Provenance:** RF-CAND-04 (RF041), CROSS-CAND-04.
**Exact source locations:** [Main PDF p.4, tolerability paragraph](../../jama_flint_2019_oi_190079.pdf#page=4), REPORT item range and operational rule. [Protocol PDF p.15](../../joi190079supp1_prod.pdf#page=15) is PLAN corroboration only.
**Source evidence:** UKU range0–3 on each of48items; adverse effect requires a2-point increase or a score3or4 with an increase from baseline. The plan names score3.
**Rule and calculation:** Under declared integer codes {0,1,2,3}, criterion4 exceeds maximum3 by1. No disclosed recoding supplies4.
**Observation versus inference:** Internal scale/rule inconsistency. The extra unattainable branch may be operationally redundant, so adverse-event counts are not asserted wrong.
**Alternatives and human question:** Was there recoding to1–4, surplus wording, or a different intended criterion? Confirm implemented codes and threshold.
**Classification rationale:** Main range versus main rule is the discrepancy, S_W; corroborating PLAN does not create P_R. Domain report_internal_inconsistency. **Classification ambiguity:** Unprinted recoding.

## C005 — HbA1c model coefficient uses mg/dL while the outcome is percent

**Provenance:** RF-CAND-05 (RF018), RL-CAND-04 (RL028), CROSS-CAND-01, STAT1-CAND-01 (S016/S062). Numeric first/last, cross-source and statistical pass1 runtime 01a1286a-d824-7281-a62a-c73b450e930c; last numeric runtime 01a1286a-814f-7b12-a00b-e90ab6064dbe.
**Exact source locations:** REPORT [Main PDF p.1 abstract](../../jama_flint_2019_oi_190079.pdf#page=1), [p.7 secondary outcomes](../../jama_flint_2019_oi_190079.pdf#page=7), [p.8 Table4](../../jama_flint_2019_oi_190079.pdf#page=8); REPORT [Results supplement p.9, eFigure8](../../joi190079supp2_prod.pdf#page=9).
**Source evidence:** Daily HbA1c coefficient−0.0002mg/dL,95%CI−0.0021to0.0016, adjusted P=.99 in narrative; abstract repeats mg/dL. Table4 labels HbA1c,% and figure axis HbA1c(%), baseline around5.9.
**Rule and calculation:** A slope for a percentage response retains percentage-point/time units absent a stated response conversion; mass concentration mg/dL is a different dimension. No numeric conversion is prescribed. Matching raw means to model coefficients is unnecessary for this printed-unit comparison.
**Observation versus inference:** Exact printed units conflict; the response transformation, if any, is not supplied. Figure slopes are optional diagnostic corroboration only.
**Alternatives and human question:** Was a separate concentration-transformed response modeled, or what unit was intended for the daily estimate and CI? Raw change and model slope are different estimands but that alone does not explain a response-unit change.
**Classification rationale:** Substantive within-main S_W and main-to-results-report S_C unit comparisons; S_C precedence; report_internal_inconsistency. **Classification ambiguity:** Unprinted transformation.

## C006 — Eleven of 34 hospitalizations is printed as 32.3%

**Provenance:** RL-CAND-01 (RL009); cross-source X038 corroborates, without a separately emitted card.
**Exact source locations:** REPORT [Main PDF p.8, opening tolerability continuation](../../jama_flint_2019_oi_190079.pdf#page=8); [p.7 Table3](../../jama_flint_2019_oi_190079.pdf#page=7) corroborates numerator11.
**Source evidence:** Placebo11(32.3%) of34 required psychiatric hospitalization because of relapse; adjacent olanzapine6(46.2%) of13.
**Rule and calculation:** 100×11/34=32.352941%→32.4% under nearest one-decimal rounding. Printed32.3 differs0.052941 percentage point, beyond±0.05. 6/13=46.153846%→46.2%.
**Observation versus inference:** Explicit count fraction and percent differ under nearest rounding. Truncation could yield32.3 but is not stated and differs from the adjacent display convention.
**Alternatives and human question:** Determine whether truncation was intentional or which printed count/percent should reconcile. No clinical consequence is inferred.
**Classification rationale:** S_W within REPORT; denominator category derives statistical_results. **Classification ambiguity:** Unstated display convention.

## C007 — Total-cholesterol unadjusted risk difference does not match counts

**Provenance:** RL-CAND-02 (RL054); independently labeled total-cholesterol outcome.
**Exact source locations:** REPORT [Main PDF p.9, Table5 total-cholesterol row](../../jama_flint_2019_oi_190079.pdf#page=9), arm headers and unadjusted-difference label.
**Source evidence:** Olanzapine9(14.1%)/64, placebo6(9.7%)/62; absolute unadjusted difference4.3percentage points,95%CI−8to17.2. Qualifying threshold240mg/dL and above baseline.
**Rule and calculation:** 100×(9/64−6/62)=4.385080645percentage points→4.4. Printed4.3 lies0.085080645point away, beyond±0.05; printed14.1−9.7=4.4. No CI method is assumed.
**Observation versus inference:** Arithmetic from explicit unadjusted counts differs from printed point estimate; the separate CI is ordered and contains the estimate.
**Alternatives and human question:** Was there deliberate truncation, a different denominator or a different estimator despite the unadjusted label? Identify the denominator/rounding rule used for this outcome.
**Classification rationale:** One REPORT table, S_W; statistical_results. **Classification ambiguity:** Unprinted estimator/display rule. This remains distinct from LDL C008 because the outcome identity differs.

## C008 — LDL unadjusted risk difference does not match counts

**Provenance:** RL-CAND-03 (RL055); independently labeled LDL outcome.
**Exact source locations:** REPORT [Main PDF p.9, Table5 LDL row](../../jama_flint_2019_oi_190079.pdf#page=9), arm headers and unadjusted-difference label.
**Source evidence:** Olanzapine9(14.1%)/64, placebo6(9.7%)/62; difference4.3percentage points,95%CI−8to17.2; LDL threshold160mg/dL and above baseline.
**Rule and calculation:** 100×(9/64−6/62)=4.385080645percentage points→4.4, outside4.3±0.05. Printed group percentages subtract to4.4. Identical counts with cholesterol are plausible and not an independent duplication candidate.
**Observation versus inference:** This separately extractable LDL point estimate fails the same explicit count-difference rule; no participant identity or CI convention is inferred.
**Alternatives and human question:** Which LDL-specific denominators, estimator and rounding rule produced4.3 under the printed unadjusted heading?
**Classification rationale:** Internal REPORT arithmetic, S_W; statistical_results. **Classification ambiguity:** Unprinted estimator/display rule. Shared numerical inputs do not erase the different LDL result identity.

## C009 — Weekly SAS points label and plotted trajectories require an estimand mapping

**Provenance:** RL-CAND-05 (RL034), CROSS-CAND-02. Statistical pass1 records related diagnostics without independently emitting a candidate.
**Exact source locations:** REPORT [Main PDF p.7, extrapyramidal result](../../jama_flint_2019_oi_190079.pdf#page=7); REPORT [Results supplement p.10, eFigure9](../../joi190079supp2_prod.pdf#page=10). [Main PDF p.4, Poisson model](../../jama_flint_2019_oi_190079.pdf#page=4) continuing on [p.5](../../jama_flint_2019_oi_190079.pdf#page=5) is a model locator/supporting definition, not an independent conflicting coefficient.
**Source evidence:** Weekly SAS change contrast0.022points,95%CI0.009–0.036,adjustedP=.009; figure Week0–36, SAS Total Score. Approximate means O.56→.73, P.685→.40. Model Poisson with overdispersion; link/back-transformation unprinted.
**Rule and calculation:** Conditional additive-score diagnostic: [(0.73−0.56)−(0.40−0.685)]/36=.012639points/week;±.02 for each endpoint permits about.010417–.014861, separate from printed rounding interval.0215–.0225. Constant additive.022 over36weeks yields.792points versus approximate plotted difference-of-changes.455. Log diagnostic [ln(.73/.56)−ln(.40/.685)]/36≈.0223/week; it is not proof of a supplied link.
**Observation versus inference:** Exact points label and axes versus approximate graphical diagnostic. Direct-source recheck cannot establish identical estimand and additive interpretation; the registered numerical comparison therefore has evidence state record_input_error and suggested review disposition discuss. A residual label discrepancy cannot be settled from supplied definitions. No significance or clinical conclusion is recomputed.
**Alternatives and human question:** Is.022 a link-scale coefficient, a marginal derivative at a particular time, or another transformed contrast? Obtain exact plotted means/link/reference population to reconcile the points label. Do not infer a log link merely from Poisson convention.
**Classification rationale:** Main label versus separate REPORT result figure is S_C; main model wording only supports interpretation and adds no independently established S_W. Domain report_internal_inconsistency. **Classification ambiguity:** Approximate figure and unprinted link/estimand mapping.

## C010 — Protocol acute recruitment is 82 versus 98 per site

**Provenance:** PF-CAND-01 (PF099), CROSS-CAND-07.
**Exact source locations:** PLAN [Protocol PDF p.21, lines995–997](../../joi190079supp1_prod.pdf#page=21); [p.17 Table4](../../joi190079supp1_prod.pdf#page=17); [p.7 overview/Figure1](../../joi190079supp1_prod.pdf#page=7), with p.8 corroborating recruitment target.
**Source evidence:** Four sites each82patients; Table4 each98acute recruits and44randomized; overall392acute and176randomized.
**Rule and calculation:** 4×98=392;4×82=328; difference64total or16/site. Acute and randomized targets are not interchanged.
**Observation versus inference:** Two printed prospective acute targets conflict if the recruitment population is identical. No comparison to actual269/126 recruitment is made.
**Alternatives and human question:** Is82 a version-specific target or subgroup? Locate a supplied amendment/population qualifier that reconciles82 with98/392, if present.
**Classification rationale:** All discrepancies within one PLAN bundle, P_P; plan_material. **Classification ambiguity:** Possible embedded target revision without version boundary.

## C011 — Protocol MMSE threshold heading and paragraph name different phases

**Provenance:** PF-CAND-02 (PF034/PF058). Cross-source X043 notes a narrower interpretation but does not remove this independently emitted label candidate.
**Exact source locations:** PLAN [Protocol PDF p.9, line438 and lines439–444](../../joi190079supp1_prod.pdf#page=9), continuing line445 on [p.10](../../joi190079supp1_prod.pdf#page=10); [p.7 operational threshold](../../joi190079supp1_prod.pdf#page=7); [p.11 Table1 footnoteH](../../joi190079supp1_prod.pdf#page=11) corroborates assessment time.
**Source evidence:** Heading MMSE≥24 to enter Stabilization; paragraph MMSE<24 at end Stabilization excludes RCT, with case exceptions. Overview assigns≥24 to RCT entry. Standard Stabilization is8weeks.
**Rule and calculation:** Same numeric gate has different entry-phase labels; Stabilization entry and RCT entry are ordinarily8weeks apart. This is a concrete threshold label comparison, not an asserted difference in scores, eligibility counts or study-design quality.
**Alternatives and human question:** Is the cutoff for Stabilization entry, RCT entry or two separate gates? Which operational definition reconciles heading, paragraph and scheduled end-Stabilization MMSE?
**Classification rationale:** PLAN heading versus PLAN operational paragraph, P_P; plan_material. Main report agrees with the operational paragraph and is corroboration, not a P_R discrepancy. **Classification ambiguity:** Heading shorthand or an unprinted second gate.

## C012 — Historical 35% changes denominator between protocol passages

**Provenance:** PF-CAND-03 (PF008).
**Exact source locations:** PLAN [Protocol PDF p.4, lines175–177](../../joi190079supp1_prod.pdf#page=4); [p.15, lines728–732](../../joi190079supp1_prod.pdf#page=15).
**Source evidence:** Historical Aronson account says approximately35% of relapses occurred following antipsychotic discontinuation; power framing assumes35% participant relapse after discontinuation and calls it the same reported rate from that study. The planned35%−15%=20point contrast itself reconciles.
**Rule and calculation:** With D=relapses following discontinuation, R=all relapses and E=discontinuers at risk, the first wording is D/R≈.35 and the latter participant-risk identity is D/E≈.35. Different denominators cannot be treated as the same measure without a supplied mapping. No R/D/E counts are given and no historical risk is reconstructed.
**Observation versus inference:** Printed denominator/framing difference, with symbolic diagnostic. The package does not provide the underlying historical study's full data.
**Alternatives and human question:** Did the historical study report both quantities, did the first passage compress its denominator, or do R and E have an explicit identity? Clarify what35% represents in the supplied protocol account; no external literature is used.
**Classification rationale:** Historical/background content in one PLAN remains PLAN, P_P; plan_material. **Classification ambiguity:** Historical denominator or second distinct estimate unprinted.

## C013 — Historical Week6 completers differ between race and ethnicity partitions

**Provenance:** PL-CAND-01 (PL038/PL073/PL075/PL077/PL079/PL081/PL087/PL088), CROSS-CAND-08.
**Exact source locations:** PLAN [Protocol PDF p.29, Table5](../../joi190079supp1_prod.pdf#page=29), historical STOP-PD randomized n and Week6 completion columns.
**Source evidence:** Race Asian12/75.0%, Black29/75.9%, White218/74.8%; ethnicity Hispanic30/80.0%, non-Hispanic229/73.8%. Both denominator partitions sum259. Historical, not current continuation-trial results.
**Rule and calculation:** Nearest one-decimal intervals permit unique integer completers9,22,163 versus24,169; sums194 versus193. Row count interval width.001n≤.229 admits at most one integer. Difference1/259=.386100percentage point. Week12 counts6+15+121 and16+126 both sum142.
**Observation versus inference:** Denominators, percentages and common endpoint are printed; inferred integer numerators and totals are explicitly derived. Exhaustive/mutually exclusive matching of the two axes is supported by their totals, but raw flags are not supplied.
**Alternatives and human question:** Do both axes partition identical participants and use the printed n as completion denominator? Obtain raw completer counts and any missingness/definition difference; no single row is declared incorrect.
**Classification rationale:** Same historical table within PLAN, P_P; plan_material. **Classification ambiguity:** Unprinted alternative denominators or unmatched completion classification.

## C014 — Protocol exposure range omits the permitted extended path

**Provenance:** PL-CAND-02 (PL066/PL114), CROSS-CAND-06 for its lower-endpoint component; PF lane explicitly assigns p.41 comparison to the last-plan shard.
**Exact source locations:** PLAN [Protocol PDF p.41, lines2069–2070](../../joi190079supp1_prod.pdf#page=41); [p.10 Table1](../../joi190079supp1_prod.pdf#page=10); [p.11 footnotesA/D](../../joi190079supp1_prod.pdf#page=11); [p.7 lines326–332](../../joi190079supp1_prod.pdf#page=7); [p.40 stabilization dosing](../../joi190079supp1_prod.pdf#page=40). Pp.13–14 and25 corroborate ordinary duration/continuation.
**Source evidence:** Minimum10/max20weeks sertraline beforeRCT; acute4–12weeks after starting study medication; ordinary stabilization8weeks on treatment; p.7 allows two additional weekly stabilization visits for near-remitters not yet meeting final criteria.
**Rule and calculation:** Ordinary sequential course4–12+8=12–20weeks. If the explicitly permitted extension follows12acute weeks with continuous sertraline,12+8+2=22weeks, exceeding printed max20 by2. Minimum10 could be a conservative lower bound compatible with≥12, so that component is weaker and conditional.
**Observation versus inference:** Printed range, components and extension versus conditional arithmetic, not actual exposure data or a protocol violation.
**Alternatives and human question:** Does p.41 summarize only the ordinary course, excluding authorized extension, or use another medication clock? Where is the qualification stated? Is10 a loose lower bound or a permitted2-week acute course? Confirm continuous exposure along the extended path.
**Classification rationale:** All compared prospective statements within PLAN, P_P; plan_material. **Classification ambiguity:** Ordinary-course summary versus exception-inclusive range and medication clock.

## C015 — Report HDRS relapse threshold omits the plan's five-point qualifier

**Provenance:** CROSS-CAND-05 (X044); cross-source runtime above.
**Exact source locations:** REPORT [Main PDF p.4, primary outcome](../../jama_flint_2019_oi_190079.pdf#page=4); PLAN [Protocol PDF p.12, lines556–557](../../joi190079supp1_prod.pdf#page=12). [Main PDF p.6](../../jama_flint_2019_oi_190079.pdf#page=6) supplies13/64 and34/62 relapse results whose endpoint is defined, not differing counts.
**Source evidence:** Report relapse requires≥1 listed criterion, including17-itemHDRS≥18. Plan adds mean absolute increase5points on at leastone visit relative toRCT entry. Near-remission baseline may beHDRS11–15.
**Rule and calculation:** Score≥18 alone differs from score≥18 plus rise≥5 for baseline14–15. Illustrative15→18 rises3 and meets the report's printed threshold but not the plan qualifier; this is an example, not an observed participant. At baseline≤13,≥18 entails≥5rise.
**Observation versus inference:** Exact numeric endpoint definitions differ; whether applied rules or observed13/34 counts differ cannot be established from supplied aggregate data.
**Alternatives and human question:** Was the report compressed while the full plan rule was applied, was an amendment disclosed, or did the operative rule change? Determine the actual rule and whether any person met≥18 without≥5rise and without another relapse criterion. No violation or conclusion change is asserted.
**Classification rationale:** REPORT numeric endpoint label versus PLAN criterion, P_R; protocol_report. **Classification ambiguity:** Summary wording versus operative amended/full rule.

## Registration completion

All fifteen distinct discovered candidates have stable IDs. All are Pending Human Adjudication. The completed fresh recheck preserved every ID, confirmed content-based roles and primary/all relationships, and assigned exactly one allowed evidence state to each. Suggested review disposition is derived mechanically, never an AI adjudication. All ledger source links are truthful physical PDF locators. Missing definitions are candidate-specific limitations rather than source-coverage gaps.
