# Mechanical Evidence Recheck and Classification Confirmation

Status: COMPLETE. Assigned and covered stable IDs: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010. All ten IDs retain Pending Human Adjudication. This artifact records source-reading and comparison facts, not human dispositions. QUALITY_CONTROL_SCOPE.md, the review contract, performance profile, report specification, settings, tooling record, source inventory, complete current ledger and independent inclusion screen were read. No legacy conclusion, external source, raw data or unprinted model detail was used.

The supplied PDFs are final authority. Fresh exact-page native layout extraction confirmed textual locations; direct CPU page rendering confirmed Figure 3 and supplementary eFigures 2 and 3. No source-versus-transcription difference requiring a ledger value/location change was found. The existing screen's limitation about PLAN p.103 is preserved: it does not say after intubation.

| ID | Review domain | Relationship type | All relationships | Evidence state | Classification confirmation |
|---|---|---|---|---|---|
| C001 | report_internal_inconsistency | S_C | S_C, S_W | reproduced | Unchanged; PLAN p.103 corroborates only |
| C002 | statistical_results | S_W | S_W | reproduced | Unchanged |
| C003 | protocol_report | P_R | P_R | reproduced | Unchanged; oxygenation model replacement not independently established |
| C004 | protocol_report | P_R | P_R | reproduced | Unchanged |
| C005 | protocol_report | P_R | P_R | reproduced | Unchanged |
| C006 | protocol_report | P_R | P_R, S_W | reproduced | Unchanged; equality-at-9 membership unavailable |
| C007 | protocol_report | P_R | P_R | reproduced | Unchanged; effect-measure identity separate from C008 adjustment |
| C008 | protocol_report | P_R | P_R | reproduced | Unchanged; adjustment separate from C007 estimand |
| C009 | protocol_report | P_R | P_R | reproduced | Unchanged |
| C010 | protocol_report | P_R | P_R | reproduced | Unchanged; absence limited to supplied REPORT materials |

## C001 — Oxygenation result time and population attribution

**Cited locations found and source values/text matched:** Yes, at every registered location. REPORT [main abstract, PDF p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1) lists PaO2:FIO2 over the three days after intubation, then reports 150 versus 119 and difference 19.5 (95% CI 4.4 to 34.6). Its results sentence also places lower respiratory rate after six hours. REPORT [secondary results, PDF p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6) says PaO2:FIO2 was higher until day 4, prints the same 150/119 and mean difference 19.5 (4.4 to 34.6), and points to eFigure 2 and the eTable.

**Comparator matched:** Yes. REPORT [eTable, PDF p.2](../../../joi180109supp2_prod.pdf#page=2) explicitly titles oxygenation and ventilation six hours after randomization and labels the PaO2/FiO2 row six hours after randomization: medians 150 [104–230] and 119 [86–165]. REPORT [eFigure 2 panel B, PDF p.4](../../../joi180109supp2_prod.pdf#page=4) uses Randomization, H6 and Day 1 through Day 7 on its time axis. Its printed contributor rows were read; no plotted coordinate was converted into an exact estimate. Corroborating PLAN [secondary-endpoint definition, PDF p.103, lines 1694–1697](../../../joi180109supp1_prod.pdf#page=103) says PaO2/FiO2 from day 1 to day 3 and does not attach an after-intubation qualifier.

**Consistency rule applicable:** Yes, matched-result attribution under focus B/C: the same displayed descriptive pair and associated contrast require an identifiable time origin, window and population. This is not a median-minus-median versus mean-difference calculation.

**Comparison and display-precision check:** The 150/119 pair and 19.5 (4.4–34.6) tuple match exactly between the two main occurrences; the pair also matches the specifically six-hour supplementary table. Integer display ranges are [149.5,150.5) and [118.5,119.5); the mean-difference range is [19.45,19.55), with endpoint ranges [4.35,4.45) and [34.55,34.65). These shared ranges establish numerical matching but cannot make postintubation and randomization-based windows the same. No difference of the two medians is used to test 19.5.

**Necessary inputs available:** Exact textual definitions, numeric tuple, supplementary table labels and figure time axis. **Exact missing inputs or definitions:** The measurement population, time origin/window and fitted analysis yielding 19.5; whether that contrast is pointwise or longitudinal; an explicit connection to the abstract's postintubation endpoint. An intubated-only denominator is not supplied for this tuple.

**Source-grounded alternative interpretation:** The abstract's six-hour clause and the eTable support a six-hour randomized-arm descriptive comparison; the postintubation endpoint description could refer to another intended trajectory. The p.6 until-day-4 wording could refer to the broader trajectory. The sources do not explicitly assign the single mean contrast to one of these possibilities.

**Direct observation versus inferred explanation:** The different time labels and matching printed pair are observed. Attribution to a distinct postintubation analysis, or an explanation based on how the abstract was composed, would be inference and is not established.

**Document roles and classification:** Main pp.1,6 and results-supplement pp.2,4 are REPORT because they present published outcomes/results. Plan p.103 is PLAN because it specifies prospective endpoints. Relationship type S_C; all relationships S_C, S_W; review domain report_internal_inconsistency. S_C takes precedence over S_W. PLAN merely corroborates endpoint context and contributes no P_R relationship. No classification change is needed. **Classification ambiguity:** Exact oxygenation analysis and window remain unspecified.

**Evidence state:** reproduced. Determining fact: the directly read postintubation outcome description and the directly read six-hour/randomization labels remain different for the matched descriptive result.

**Exact remaining human question:** Which time origin, measurement window, population and analysis generated 150 versus 119 and mean difference 19.5 (4.4–34.6), and how does that result correspond to the abstract endpoint definition?

## C002 — Forest-plot HR reference and favor direction

**Cited locations found and source values/text matched:** Yes. REPORT [abstract, PDF p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1) and [Table 2/primary results, PDF p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5) print day-28 mortality HR 0.98 (0.77–1.24), with 138/388 HFNO and 140/388 standard oxygen. Table 2 and REPORT [secondary results, PDF p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6) print ventilation HR 0.85 (0.68–1.06), with 150/388 and 170/388. REPORT [subgroup methods, PDF p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4) describes HFNO versus standard effects as Cox HRs displayed in forests; it does not name a reversed reference in Figure 3.

**Comparator matched and all affected occurrences:** Yes. The direct render and native text of REPORT [Figure 3, PDF p.7](../../../jama_azoulay_2018_oi_180109.pdf#page=7) confirm both favor-label pairs: values below 1 sit under Favors High-Flow Nasal Oxygen Therapy; above 1 under Favors Standard Oxygen Therapy. Both all-patient rows and all 24 subgroup rows are enumerated below. Each row is at that same exact PDF page, in the named panel/subset; H and S mean the printed HFNO and standard columns. Affected subgroup direction interpretations share the unresolved reference convention; no independently printed comparator HR is claimed for each subgroup.

| Exact Figure 3 occurrence | H event/total | S event/total | Printed HR (95% CI) | Printed interaction P for pair |
|---|---:|---:|---|---|
| A mortality, ICU admission 0–1 days | 120/321 | 118/330 | 0.95 (0.74–1.22) | .15 |
| A mortality, ICU admission ≥2 days | 18/67 | 22/58 | 1.55 (0.83–2.90) | .15 |
| A mortality, PaO2:FIO2 <200 | 99/237 | 95/251 | 0.89 (0.68–1.19) | .52 |
| A mortality, PaO2:FIO2 ≥200 | 16/65 | 10/35 | 1.18 (0.54–2.60) | .52 |
| A mortality, oxygen flow ≤9 | 122/348 | 127/347 | 1.06 (0.83–1.36) | .39 |
| A mortality, oxygen flow >9 | 16/40 | 13/41 | 0.76 (0.36–1.57) | .39 |
| A mortality, catecholamines No | 121/355 | 126/349 | 1.08 (0.84–1.39) | .15 |
| A mortality, catecholamines Yes | 17/33 | 14/39 | 0.62 (0.31–1.26) | .15 |
| A mortality, unknown diagnosis No | 99/297 | 95/303 | 0.93 (0.70–1.23) | .12 |
| A mortality, unknown diagnosis Yes | 39/91 | 45/85 | 1.39 (0.90–2.13) | .12 |
| A mortality, hematologic malignancy No | 66/199 | 72/198 | 1.11 (0.79–1.55) | .5 |
| A mortality, hematologic malignancy Yes | 64/167 | 65/181 | 0.94 (0.67–1.33) | .5 |
| A mortality, All patients | 138/388 | 140/388 | 1.02 (0.81–1.29) | — |
| B IMV, ICU admission 0–1 days | 128/321 | 142/330 | 1.1 (0.87–1.40) | .17 |
| B IMV, ICU admission ≥2 days | 22/67 | 28/58 | 1.69 (0.96–2.95) | .17 |
| B IMV, PaO2:FIO2 <200 | 99/237 | 117/251 | 1.17 (0.90–1.53) | .44 |
| B IMV, PaO2:FIO2 ≥200 | 27/65 | 13/35 | 0.88 (0.46–1.71) | .44 |
| B IMV, oxygen flow ≤9 | 136/348 | 151/347 | 1.15 (0.91–1.45) | .65 |
| B IMV, oxygen flow >9 | 14/40 | 19/41 | 1.37 (0.68–2.72) | .65 |
| B IMV, catecholamines No | 137/355 | 154/349 | 1.18 (0.94–1.49) | .83 |
| B IMV, catecholamines Yes | 13/33 | 16/39 | 1.09 (0.52–2.26) | .83 |
| B IMV, unknown diagnosis No | 114/297 | 135/303 | 1.18 (0.92–1.52) | .9 |
| B IMV, unknown diagnosis Yes | 36/91 | 35/85 | 1.15 (0.72–1.82) | .9 |
| B IMV, hematologic malignancy No | 61/199 | 89/198 | 1.61 (1.16–2.23) | .01 |
| B IMV, hematologic malignancy Yes | 78/167 | 77/181 | 0.89 (0.65–1.22) | .01 |
| B IMV, All patients | 150/388 | 170/388 | 1.17 (0.94–1.46) | — |

**Consistency rule applicable:** Yes, matched model-based all-patient estimates should reconcile under their identified contrast, and the favor convention must identify which intervention has lower hazard. Event counts identify matched outcomes/populations; a crude count ratio is not the comparator.

**Comparison and display-precision check:** Mortality HR 0.98 allows [0.975,0.985), versus forest 1.02 allowing [1.015,1.025); these do not overlap. Ventilation HR 0.85 allows [0.845,0.855), versus forest 1.17 allowing [1.165,1.175); these do not overlap. Reciprocal diagnostics are 1/0.98 = 1.020408 and 1/0.85 = 1.176471. Allowing the table estimates' full rounding ranges gives inverse ranges approximately (1.015228,1.025641] and (1.169591,1.183432], which intersect the forest ranges. Thus reciprocal coding is compatible even though exact inversion of displayed 0.85 alone rounds to 1.18. This is a diagnostic, not confirmation of fitted-model reference coding. Reading every subgroup HR/CI and the shared favor labels confirms the scope of the reference question; no subgroup arithmetic contradiction is inferred from its crude events.

For every two-decimal subgroup HR/CI entry in the table above, the display interval is [x−.005,x+.005); the explicitly one-decimal HR 1.1 has [1.05,1.15). Two-decimal interaction P values use the same .005 half-unit; .5 and .9 use .05. These intervals preserve the printed quantities without inferring exact model output. For the nonhematologic IMV row, HR 1.61 allows [1.605,1.615) and its lower CI 1.16 allows [1.155,1.165), still above 1. That establishes the row's numerical side of the printed favor convention, not the unprinted model reference.

**Necessary inputs available:** Matched all-patient counts, HRs/intervals, model descriptions and rendered favor labels. **Exact missing inputs or definitions:** Figure 3 treatment/reference coding and model specification; explicit explanation of how its overall HRs relate to Table 2; unrounded fitted estimates and event times.

**Source-grounded alternative interpretation:** Figure 3 may use standard-versus-HFNO reference coding whereas Table 2 uses HFNO-versus-standard; different model construction is another possibility. The reciprocal ranges support the first possibility, but the caption/methods do not establish it or reconcile the favor labels.

**Direct observation versus inferred explanation:** The two nonoverlapping overall HR displays and both label placements are directly observed. Inversion of coding, reversal of all subgroup effects or a specific mechanism is inferred and remains unestablished.

**Document roles and classification:** Every compared location is REPORT in the same published article. Relationship type S_W; all relationships S_W; review domain statistical_results, because estimates and effect directions are compared. No plan/result-supplement conflict is introduced. No classification change is needed. **Classification ambiguity:** The forest model/reference coding is unprinted.

**Evidence state:** reproduced. Determining fact: matched overall rows carry HRs beyond display precision in opposite numerical orientations, with the same printed favor convention and no stated reference reconciliation.

**Exact remaining human question:** Which treatment/reference coding and favor direction apply to both Figure 3 panels and every subgroup HR, and how do the two overall HRs relate to Table 2?

## C003 — Planned longitudinal joint models and reported rank comparisons

**Cited locations found and source text matched:** Yes. PLAN [protocol, PDF p.55, lines 825–826](../../../joi180109supp1_prod.pdf#page=55), [original SAP, PDF p.82, lines 1314–1315](../../../joi180109supp1_prod.pdf#page=82) and [final SAP, PDF p.105, lines 1745–1747](../../../joi180109supp1_prod.pdf#page=105) all prescribe joint models accounting for right censoring for longitudinal oxygenation, dyspnea and comfort.

**Comparator matched and affected report locations:** Yes. REPORT [methods, PDF p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4) explicitly chooses Wilcoxon rank-sum for visual analog comfort/dyspnea scores. REPORT [abstract, PDF p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1) reports no difference in comfort/dyspnea; REPORT [secondary results, PDF p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6) says neither differs at any time. REPORT [eFigure 3 panels A/B, PDF p.5](../../../joi180109supp2_prod.pdf#page=5) displays comfort/dyspnea at Randomization, H6 and Day 1 through Day 7, with contributor rows. REPORT [eFigure 2 panels A/B, PDF p.4](../../../joi180109supp2_prod.pdf#page=4) supplies respiratory-rate/oxygenation context. Both supplementary pages were visually confirmed without reading exact estimates from coordinates.

**Consistency rule applicable:** Yes, focus D compares a prospective repeated-outcome analysis with the explicitly reported analysis supporting the abstract-reported comfort/dyspnea conclusion.

**Comparison and display-precision check:** Joint longitudinal models accounting for right censoring and rank-sum comparisons are different named analytical procedures. This is a textual method comparison, with no numeric half-unit input able to reconcile the two specifications. No exact graph effect, variance or test P was inferred. Absence of a reported oxygenation model does not positively establish replacement of its planned joint model.

**Necessary inputs available:** Three prospective method statements, explicit comfort/dyspnea report method, conclusion and longitudinal displays. **Exact missing inputs or definitions:** Actual fitted comfort/dyspnea joint-model results, if any; how censoring was implemented; whether rank-sum conclusions were pointwise, combined or supplementary to other analyses; actual reported oxygenation model.

**Source-grounded alternative interpretation:** Rank-sum comparisons could have replaced the planned models, or both analyses could have been performed with only rank-based conclusions identifiable in the supplied report.

**Direct observation versus inferred explanation:** The named method difference is observed for comfort and dyspnea. Replacement of oxygenation analysis, a specific censoring mechanism, or an explanation for changing contributors would be inference and is not asserted.

**Document roles and classification:** All three prospective locations are PLAN; main/result-supplement outcome locations are REPORT. Relationship type P_R; all relationships P_R; review domain protocol_report. The result supplement corroborates reported display context and creates no additional S_C inconsistency. No classification change is needed. **Classification ambiguity:** Oxygenation analysis is unreported; it remains context, not independent evidence of replacement.

**Evidence state:** reproduced. Determining fact: the final plan explicitly promises joint comfort/dyspnea models while the report explicitly names rank-sum comparisons for these outcomes.

**Exact remaining human question:** Which analyses generated the comfort/dyspnea conclusions, and how do the reported rank-sum comparisons relate to the planned joint models and their censoring provision?

## C004 — Infection competing-risk plan and reported proportion test

**Cited locations found and source text matched:** Yes. PLAN [original SAP, PDF p.82, lines 1305–1310](../../../joi180109supp1_prod.pdf#page=82) and [final SAP, PDF p.105, lines 1738–1742](../../../joi180109supp1_prod.pdf#page=105) explicitly include ICU-acquired infection among competing-risk endpoints, prescribe cumulative incidences with death or discharge alive from ICU competing, Gray comparison, and potential-confounder adjustment using cause-specific Cox models.

**Comparator matched and all affected report occurrences:** Yes. REPORT [methods, PDF p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4) explicitly compares infection proportions by chi-square. REPORT [Table 2, PDF p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5) prints 39/388 versus 41/388, 10.0% versus 10.6%, risk difference −0.6% (−4.6 to 4.1), cause-specific HR 1.01 (0.96–1.06) and P=.91. REPORT [abstract, PDF p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1) and [secondary results, PDF p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6) repeat the infection percentages/absolute difference and no-significant-difference conclusion. Table 2 footnote d explicitly labels the HR cause-specific.

**Consistency rule applicable:** Yes, focus D requires the estimator/test of the abstract-reported infection comparison to be identifiable against the final analytical specification.

**Comparison and display-precision check:** Planned cumulative-incidence/Gray comparison versus reported proportions/chi-square is a positive method difference. Display ranges for the contextual RD −0.6%, CI −4.6% to 4.1%, HR 1.01 and P=.91 are respectively [−0.65,−0.55), [−4.65,−4.55), [4.05,4.15), [1.005,1.015) and [.905,.915). Allowing every such range does not change the named procedures. No variance reconstruction from crude events, HR-versus-risk-ratio comparison or independent P-value contradiction is claimed.

**Necessary inputs available:** Prospective competing events/test, explicit report test, endpoint counts and estimate/test labels. **Exact missing inputs or definitions:** Event times, cumulative-incidence estimate and Gray result for infection, actual cause-specific HR model/adjustment and interval algorithm, and an explicit mapping of each reported effect/P to its analysis.

**Source-grounded alternative interpretation:** A proportion comparison could have replaced the planned competing-risk test; both could have been run but only the proportion comparison is identifiable. The printed cause-specific HR suggests an additional time-to-event component but does not identify a Gray comparison.

**Direct observation versus inferred explanation:** Named estimator/test specifications differ directly. Which unreported models were run, why the framework changed, or how the HR interval was generated remains inference.

**Document roles and classification:** SAP statements are PLAN; all main article occurrences are REPORT. Relationship type P_R; all relationships P_R; review domain protocol_report. Two plan versions agree, so there is no P_P; report repetitions agree, so no S_W is added. No classification change is needed. **Classification ambiguity:** The infection HR's implementation is unreported; it is not asserted to be univariable.

**Evidence state:** reproduced. Determining fact: explicit final-plan cumulative-incidence/Gray and explicit reported infection proportion/chi-square statements remain different.

**Exact remaining human question:** Which infection estimator, competing events and comparison test generated the reported RD, cause-specific HR and P=.91, and where is their relationship to the planned analysis specified?

## C005 — ICU-stay analysis specification

**Cited locations found and source text matched:** Yes. PLAN [original SAP, PDF p.82, lines 1311–1313](../../../joi180109supp1_prod.pdf#page=82) and [final SAP, PDF p.105, lines 1742–1745](../../../joi180109supp1_prod.pdf#page=105) prescribe ICU-stay analysis overall and separately in survivors/dead patients, using the former/latter Kaplan–Meier and competing-risk wording. That wording was preserved without assigning unprinted event coding.

**Comparator matched and all affected report occurrences:** Yes. REPORT [methods, PDF p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4) chooses Wilcoxon rank-sum for ICU length of stay. REPORT [Table 2, PDF p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5) presents both 388-person groups, medians 8 [4–14] versus 6 [4–13] days, mean difference 0.6 days (−1.0 to 2.2), P=.07; footnote b says quantitative-outcome differences are differences in means. REPORT [abstract, PDF p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1) and [secondary results, PDF p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6) repeat the 8/6-day summaries, 0.6-day contrast and lack of a significant difference. They identify no survivor/death-separated ICU-stay results.

**Consistency rule applicable:** Yes, focus D compares planned estimator/populations with the explicitly reported pooled rank-sum comparison for this abstract-reported outcome.

**Comparison and display-precision check:** Kaplan–Meier/competing-risk and overall plus survivor/death-separated analyses are not specified by the reported pooled rank-sum statement. Numeric ranges for medians 8 and 6 are [7.5,8.5) and [5.5,6.5); mean difference 0.6 allows [.55,.65), CI endpoints [−1.05,−.95) and [2.15,2.25), P=.07 allows [.065,.075). Medians and a difference in means are different summaries and were not equated. Their display precision cannot resolve the method/population specification difference.

**Necessary inputs available:** Explicit prospective procedures/population split, report procedure and summary labels. **Exact missing inputs or definitions:** Planned time/event coding, separately reported survivor/death ICU-stay populations and estimates, survival/competing-risk results, and a reconciliation of those procedures with the reported rank-sum result.

**Source-grounded alternative interpretation:** Pooled rank-sum may have replaced the planned analyses, or the planned analyses may have been performed additionally without identifiable reporting. The plan's former/latter wording does not fully specify how every event is coded.

**Direct observation versus inferred explanation:** Method names, intended population split and pooled reporting are directly observed. A numerical inconsistency between medians and means, the event coding, or analysis replacement mechanism is not inferred.

**Document roles and classification:** Both SAP locations are PLAN; all article comparisons are REPORT. Relationship type P_R; all relationships P_R; review domain protocol_report. Agreeing plan versions and agreeing report repetitions add no P_P or S_W. No classification change is needed. **Classification ambiguity:** Event coding and the plan's former/latter mapping are not fully resolved by its text.

**Evidence state:** reproduced. Determining fact: the prospective survival/competing-risk procedures and population split differ from the explicitly named report rank-sum comparison, with no supplied connecting statement.

**Exact remaining human question:** Which ICU-stay population and analytical procedure generated the mean difference 0.6 days and P=.07, and how do these correspond to the planned overall and survivor/death-separated analyses?

## C006 — Prospective and displayed subgroup boundaries

**Cited locations found and source text matched:** Yes. PLAN [PDF p.98, lines 1600–1601](../../../joi180109supp1_prod.pdf#page=98) and [PDF p.99, lines 1602–1604](../../../joi180109supp1_prod.pdf#page=99) define D0/D1/D2 versus ≥D3 and oxygen flow <9 versus ≥9 L/min, with interaction analyses on these strata. PLAN [final SAP, PDF p.104, lines 1721–1722](../../../joi180109supp1_prod.pdf#page=104) refers primary-endpoint treatment-by-covariate interactions to the subsets defined above.

**Comparator matched and all affected report occurrences:** Yes. REPORT [randomization, PDF p.2](../../../jama_azoulay_2018_oi_180109.pdf#page=2) says time since ICU admission ≤2 versus ≥3 days, and oxygen >9 versus ≤9 L/min. REPORT [subgroup methods/Table 1, PDF p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4) links subgroup HRs to stratification variables and prints D0 244/251, D1 77/79, D2 47/38, ≥D3 20/20 for HFNO/standard. REPORT [Figure 3, PDF p.7](../../../jama_azoulay_2018_oi_180109.pdf#page=7) labels time subgroups 0–1 and ≥2 days in both panels. Panel A rows are 120/321 versus 118/330, HR .95 (.74–1.22), and 18/67 versus 22/58, HR 1.55 (.83–2.90), interaction P=.15. Panel B rows are 128/321 versus 142/330, HR 1.1 (.87–1.40), and 22/67 versus 28/58, HR 1.69 (.96–2.95), interaction P=.17. The accompanying oxygen rows are ≤9/>9 in both panels: A 122/348 versus 127/347, HR 1.06 (.83–1.36), and 16/40 versus 13/41, HR .76 (.36–1.57), P=.39; B 136/348 versus 151/347, HR 1.15 (.91–1.45), and 14/40 versus 19/41, HR 1.37 (.68–2.72), P=.65. All row labels/counts were visually confirmed.

**Consistency rule applicable:** Yes, focus D compares predefined subgroup membership to prospective strata and report methods; the time-boundary difference demonstrably changes primary/key-secondary subgroup populations.

**Comparison and display-precision check:** HFNO 244+77=321 and 47+20=67; standard 251+79=330 and 38+20=58. These exactly reproduce Figure 3's 0–1 and ≥2 denominators. Planned/reported-randomization ≤2 totals are 368 and 368, leaving ≥3 denominators 20/20. Thus 47 HFNO and 38 standard day-2 participants move relative to those strata. Counts are exact integers, not continuous rounded inputs; the categorical inequality boundary is exact. P=.15 and .17 have display ranges [.145,.155) and [.165,.175), but no rounding of P or HR can change membership. For oxygen, <9/≥9 versus ≤9/>9 differs only for participants exactly at 9; that count is unavailable, so no changed oxygen membership or effect is calculated.

**Necessary inputs available:** Prospective strata, reported randomization/method statements, four Table 1 day counts per arm and both forest panels' denominators. **Exact missing inputs or definitions:** Prospective justification for a distinct 0–1/≥2 analysis rule, actual subgroup coding, and number of participants exactly at 9 L/min. A label difference alone is not used to infer the latter count.

**Source-grounded alternative interpretation:** A different subgroup cutpoint could have been prospectively intended independently of the randomization strata; the display may be describing different analysis bins. The supplied methods link the subgroups to strata and do not identify that distinct prospective rule.

**Direct observation versus inferred explanation:** Day-2 membership follows exactly from printed denominators and Table 1 counts. An effect of the oxygen equality boundary, a changed HR from recoding, or the reason for adopting these bins is not inferred.

**Document roles and classification:** Prospective strata/SAP are PLAN; main pp.2,4,7 are REPORT. Relationship type P_R; all relationships P_R, S_W; review domain protocol_report. PLAN-to-forest and report-method-to-forest comparisons both apply; P_R takes precedence over S_W. Plan versions do not create a P_P conflict. No classification change is needed. **Classification ambiguity:** Oxygen equality-at-9 membership is unavailable; it remains accompanying qualified context.

**Evidence state:** reproduced. Determining fact: exact printed day counts reproduce the forest's ≥2 population, whereas the prospective/report-randomization late stratum starts at ≥3.

**Exact remaining human question:** What were the prospectively specified mortality and ventilation subgroup boundaries, and which time and oxygen-flow populations do the displayed HRs and interaction tests represent?

## C007 — Primary relative-risk plan and reported hazard ratio

**Cited locations found and source text matched:** Yes. PLAN [original SAP, PDF p.82, lines 1297–1300](../../../joi180109supp1_prod.pdf#page=82) and [final SAP, PDF p.104, lines 1731–1734](../../../joi180109supp1_prod.pdf#page=104) describe a binary alive/dead endpoint at day 28 and an experimental/control relative risk with 95% CI. Their hospital-death wording was read in that immediate day-28 binary context; it is not used for a separate endpoint candidate.

**Comparator matched:** Yes. REPORT [primary methods, PDF p.3](../../../jama_azoulay_2018_oi_180109.pdf#page=3) describes Kaplan–Meier mortality estimation, risk difference and HR from univariable Cox models. REPORT [Table 2, PDF p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5) labels primary all-cause day-28 mortality HR .98 (.77–1.24). Its separate ICU/hospital mortality RR rows are distinct outcomes, not the planned primary RR. The report's redesign paragraph on p.3 explains an early noninferiority-to-superiority change; the final SAP being compared already specifies superiority.

**Consistency rule applicable:** Yes, focus D compares final planned primary estimand/model with the identifiable reported primary result. Effect-measure identity is independent of C008's covariate-adjustment comparison.

**Comparison and display-precision check:** A binary day-28 risk ratio and a Cox hazard ratio are distinct estimands regardless of numerical proximity. HR .98 allows [.975,.985); printed CI .77–1.24 allows [.765,.775) and [1.235,1.245). No value within these display ranges changes an HR into an RR. No crude RR was substituted for a model estimate, and the effect difference was not calculated from count ratios.

**Necessary inputs available:** Exact final and original estimand statements, report model and effect labels, primary endpoint definition. **Exact missing inputs or definitions:** Primary day-28 RR estimate/CI or an explicit explanation that the final primary estimand was changed to HR; event times and model output needed to reconstruct the HR.

**Source-grounded alternative interpretation:** The HR may intentionally replace the planned RR; a primary RR analysis may also have been performed but is not identifiable in the supplied report. Neither possibility is specified by the redesign paragraph.

**Direct observation versus inferred explanation:** PLAN RR and REPORT HR labels/models differ directly. A change of numerical results, the actual effect of substituting estimands, or a rationale for that substitution is not inferred.

**Document roles and classification:** SAP pp.82,104 are PLAN; main pp.3,5 are REPORT. Relationship type P_R; all relationships P_R; review domain protocol_report. Two agreeing SAP versions contribute no P_P. Adjustment is independently classified under C008 because an adjusted HR would still differ from the planned RR. No classification change is needed. **Classification ambiguity:** The primary RR is not identifiable; hospital wording is resolved in the immediate binary day-28 context.

**Evidence state:** reproduced. Determining fact: the final SAP identifies an RR for the binary day-28 endpoint, while the report explicitly identifies its primary treatment effect as a Cox HR.

**Exact remaining human question:** Which final primary estimand was intended, and where is the planned day-28 RR result or a reconciliation of that specification with the reported HR?

## C008 — Planned covariate adjustment and explicit univariable models

**Cited locations found and source text matched:** Yes. PLAN [original SAP, PDF p.82, lines 1300–1310](../../../joi180109supp1_prod.pdf#page=82) prescribes potential-confounder adjustment for the primary analysis and cause-specific Cox adjustment for competing-risk endpoints including intubation. PLAN [final SAP, PDF p.104, line 1734](../../../joi180109supp1_prod.pdf#page=104) repeats primary adjustment; PLAN [PDF p.105, lines 1738–1742](../../../joi180109supp1_prod.pdf#page=105) repeats competing-risk adjustment.

**Comparator matched and all affected report occurrences:** Yes. REPORT [primary methods, PDF p.3](../../../jama_azoulay_2018_oi_180109.pdf#page=3) explicitly identifies univariable Cox models; REPORT [ventilation methods, PDF p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4) explicitly identifies a univariable cause-specific Cox model. REPORT [Table 2, PDF p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5) supplies mortality HR .98 (.77–1.24) and ventilation HR .85 (.68–1.06), the affected treatment effects. REPORT [limitations, PDF p.8](../../../jama_azoulay_2018_oi_180109.pdf#page=8) acknowledges that treatment estimates were not adjusted on stratification factors.

**Consistency rule applicable:** Yes, focus D compares explicit planned covariate adjustment with explicit reported treatment-only/univariable analyses for primary mortality and key-secondary ventilation. This rule does not depend on whether the primary effect is an RR or HR.

**Comparison and display-precision check:** Potential-confounder-adjusted and univariable model specifications differ logically; numeric rounding cannot supply covariates. Mortality HR display range is [.975,.985), ventilation [.845,.855), and their printed CI endpoint ranges are [.765,.775)/[1.235,1.245) and [.675,.685)/[1.055,1.065). All such values could arise under either adjustment designation, so no estimate calculation is used as proof of adjustment. The explicit text is decisive.

**Necessary inputs available:** Positive planned adjustment statements and positive reported univariable statements for both outcomes. **Exact missing inputs or definitions:** Named potential confounders, final covariate/model specification, adjusted mortality and ventilation estimates or a supplied reconciliation of the change. Infection's fitted adjustment is not specified; it is not asserted to be univariable.

**Source-grounded alternative interpretation:** Univariable models could have replaced the prescribed adjusted analyses, or additional adjusted analyses may have been run without identifiable reporting. Absence of stratification adjustment in the limitations supports the report description but does not specify every potential confounder intended in the plan.

**Direct observation versus inferred explanation:** Adjusted versus univariable method text differs directly in the two named treatment effects. Particular omitted covariates, magnitude of any adjusted-result change, and an explanation for the selection are not inferred.

**Document roles and classification:** All SAP locations are PLAN; main pp.3,4,5,8 are REPORT. Relationship type P_R; all relationships P_R; review domain protocol_report. Report limitation corroborates the explicit method and is not a separate S_W conflict. The independent C007 estimand issue is not folded into this candidate: a treatment-only RR would still omit planned adjustment. No classification change is needed. **Classification ambiguity:** Potential confounders were not named; adjustment details of the infection HR remain unreported.

**Evidence state:** reproduced. Determining fact: directly read final adjustment prescriptions differ from directly read univariable mortality and ventilation model statements.

**Exact remaining human question:** Which final covariate-adjustment specifications applied to the primary mortality and ventilation treatment effects, and where are the planned adjusted results or a reconciliation with the reported univariable models?

## C009 — Comparator rescue-HFNO permission

**Cited locations found and source text matched:** Yes. PLAN [rationale, PDF p.95, lines 1544–1552](../../../joi180109supp1_prod.pdf#page=95) sets the comparative oxygen strategies; PLAN [PDF p.96, lines 1553–1554](../../../joi180109supp1_prod.pdf#page=96) says HFNO will not be used in the control group. PLAN [final intervention, PDF p.99, lines 1616–1625](../../../joi180109supp1_prod.pdf#page=99) repeats that categorical rule at line 1621.

**Comparator matched and all affected report occurrences:** Yes. REPORT [treatments, PDF p.3](../../../jama_azoulay_2018_oi_180109.pdf#page=3) permits HFNO only for standard-arm patients with do-not-intubate orders whose standard therapy failed. Figure 1 on the same page records 30 standard-arm HFNO recipients. REPORT [intervention results, PDF p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5) records these 30 patients (7.7%) and 14 deaths (46.7%).

**Consistency rule applicable:** Yes, focus D compares an explicit randomized comparator-intervention rule, which defines the strategy underlying primary mortality and ventilation results. Occurrence of a crossover or individual clinical appropriateness is not the rule under examination.

**Comparison and display-precision check:** The categorical PLAN no-HFNO rule and REPORT conditional permission remain different irrespective of counts. Contextual arithmetic reproduces 100×30/388 = 7.731959%, inside the displayed 7.7% interval [7.65,7.75); 100×14/30 = 46.666667%, inside [46.65,46.75). These percentages reconcile. Exact integer counts and allowed numeric intervals do not transform a prohibition into conditional permission.

**Necessary inputs available:** Explicit prospective restriction, explicit report permission and reported recipient counts. **Exact missing inputs or definitions:** A supplied prospective amendment or final-strategy specification reconciling the rescue permission with the final-plan restriction. Participant-level eligibility and individual reasons are neither required for this comparison nor inferred.

**Source-grounded alternative interpretation:** The intended final comparator may have included an additional rescue rule; individual departures from the categorical plan may instead have been reported as a general treatment description. The supplied evidence does not identify which applies.

**Direct observation versus inferred explanation:** Plan prohibition, report conditional permission and counts are directly observed. A protocol violation, justification of any individual crossover, or an effect on mortality is not inferred.

**Document roles and classification:** Rationale/intervention pp.95,96,99 are PLAN; article pp.3,5 are REPORT. Relationship type P_R; all relationships P_R; review domain protocol_report. The plan rationale and intervention agree; the report methods and recipient counts corroborate each other. No extra P_P or S_W is created. No classification change is needed. **Classification ambiguity:** No supplied amendment reconciles the final comparator permission.

**Evidence state:** reproduced. Determining fact: the final plan expressly excludes HFNO in controls whereas the report expressly permits conditional rescue HFNO.

**Exact remaining human question:** Was conditional rescue HFNO part of the intended final comparator strategy, and where is that permission reconciled with the supplied final-plan prohibition?

## C010 — Prespecified per-protocol primary result unavailable

**Cited location found and source text matched:** Yes. PLAN [final SAP, PDF p.104, lines 1717–1723](../../../joi180109supp1_prod.pdf#page=104) places the main ITT comparison and primary-endpoint interaction analyses in its methodology section and ends with an unconditional promise that a per-protocol analysis will be performed. The subsequent missing-value section is separate and does not make that sentence conditional.

**Comparator matched and complete absence scope:** REPORT [main methods/Figure 1, PDF p.3](../../../jama_azoulay_2018_oi_180109.pdf#page=3) describes ITT with only withdrawn-consent exclusions and includes 388 in each primary-analysis arm. REPORT [methods, PDF p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4), [Table 2/primary results, PDF p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5), [secondary results/primary survival figure, PDF p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6) and [subgroup forest, PDF p.7](../../../jama_azoulay_2018_oi_180109.pdf#page=7) contain no separately identified per-protocol population/result. Complete supplied-report inspection additionally covers [abstract p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1), [background/design p.2](../../../jama_azoulay_2018_oi_180109.pdf#page=2), [discussion/administrative p.8](../../../jama_azoulay_2018_oi_180109.pdf#page=8), [administrative/references p.9](../../../jama_azoulay_2018_oi_180109.pdf#page=9), results supplement [cover p.1](../../../joi180109supp2_prod.pdf#page=1), [eTable p.2](../../../joi180109supp2_prod.pdf#page=2), [ventilation figure p.3](../../../joi180109supp2_prod.pdf#page=3), [oxygenation figure p.4](../../../joi180109supp2_prod.pdf#page=4), [comfort/dyspnea figure p.5](../../../joi180109supp2_prod.pdf#page=5), and [data-sharing statement p.1](../../../joi180109supp3_prod.pdf#page=1). None identifies a primary per-protocol definition, denominator or mortality effect. The data-sharing page is administrative and has no analysis result.

**Consistency rule applicable:** Yes, the explicit focus-D provision covers a prespecified primary analysis not reported. The comparison is the promise of a distinct per-protocol primary analysis versus its identifiable availability in the supplied reporting package, not the absence of an arbitrary method detail.

**Comparison and display-precision check:** Full supplied-report reading and a case-insensitive per-protocol/analysis-population text search found no identifiable PP result. ITT denominators 388/388 are exact counts. No numeric half-unit interval can supply an unreported PP definition, denominator or result. The 12 intervention switches and 30 comparator HFNO recipients were not subtracted from ITT denominators; treatment changes do not establish a PP exclusion rule.

**Necessary inputs available:** Express final prospective promise, explicit report ITT definition, all supplied REPORT pages and their analysis displays. **Exact missing inputs or definitions:** Final PP eligibility/exclusion definition, PP participants/events, primary PP effect/interval/test, or a supplied statement explaining replacement/withdrawal of that prespecified analysis.

**Source-grounded alternative interpretation:** A PP analysis could have been performed but not included in the supplied reports, or the final analysis promise could have changed. The complete local package establishes neither which alternative applies nor that PP and ITT results differ.

**Direct observation versus inferred explanation:** The promise and absence of an identifiable PP result within the supplied REPORT package are directly observed. Never performing the analysis, any PP sample size, or the direction/magnitude of a PP effect would be inference and is not asserted.

**Document roles and classification:** Final SAP p.104 is PLAN. Main pp.1,2,3,4,5,6,7,8,9; results supplement pp.1,2,3,4,5; and data-sharing p.1 are REPORT by published report/result/administrative content. Relationship type P_R; all relationships P_R; review domain protocol_report. Agreement of report locations in identifying only ITT does not create S_C or S_W. No classification change is needed. **Classification ambiguity:** Absence is restricted to supplied reports; no claim is made about analyses held elsewhere or never performed.

**Evidence state:** reproduced. Determining fact: the final SAP unconditionally promises a PP analysis while every supplied REPORT page lacks an identifiable PP primary result/definition.

**Exact remaining human question:** What definition, population and mortality result implement the promised primary per-protocol analysis, or what supplied reconciliation explains its replacement or absence from the reports?

## Confirmation derivatives and engine record

All new derivatives are below `.ai_paper_validation/review_1_6_1/preprocessing/evidence_recheck_confirmation/`. Engine: direct Poppler pdftotext/pdftoppm 25.03.0, CPU only. `pdftotext -layout` generated native layout text; `pdftoppm -singlefile -png` generated source-page renders at the recorded resolution. The available direct tools listed in tooling_record.md were used; no OCR, fallback environment, Office tool, GPU, web access or source/reused-artifact modification was needed. JavaScript arithmetic evaluated only the displayed reciprocal and percentage diagnostics; it did not classify candidates.

| New derivative path relative to review_1_6_1 | Exact source units | Engine and method |
|---|---|---|
| preprocessing/evidence_recheck_confirmation/main-p001-p009.txt | Main PDF pp.1,2,3,4,5,6,7,8,9 | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/results-p001-p005.txt | Results PDF pp.1,2,3,4,5 | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/data-sharing-p001.txt | Data-sharing PDF p.1 | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/plan-p55.txt | Plan PDF p.55 | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/plan-p82.txt | Plan PDF p.82 | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/plan-p95.txt | Plan PDF p.95 | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/plan-p96.txt | Plan PDF p.96 | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/plan-p98.txt | Plan PDF p.98 | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/plan-p99.txt | Plan PDF p.99 | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/plan-p100.txt | Plan PDF p.100, intervention context | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/plan-p101.txt | Plan PDF p.101, intervention context | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/plan-p102.txt | Plan PDF p.102, endpoint context | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/plan-p103.txt | Plan PDF p.103 | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/plan-p104.txt | Plan PDF p.104 | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/plan-p105.txt | Plan PDF p.105 | Poppler pdftotext 25.03.0, native layout |
| preprocessing/evidence_recheck_confirmation/main-p007.png | Main PDF p.7 | Poppler pdftoppm 25.03.0, CPU PNG at 130 dpi |
| preprocessing/evidence_recheck_confirmation/results-p004.png | Results PDF p.4 | Poppler pdftoppm 25.03.0, CPU PNG at 100 dpi |
| preprocessing/evidence_recheck_confirmation/results-p005.png | Results PDF p.5 | Poppler pdftoppm 25.03.0, CPU PNG at 100 dpi |

Counts: 10 assigned IDs; 10 separately completed cards; evidence states reproduced 10, reproduced_after_transcription_correction 0, not_reproduced 0; classification changes 0. All registered source locations were found; all repeated-pattern occurrences were included. Remaining human questions concern analysis/reference/population definitions and the supplied-report absence of PP results, as stated individually. No source-location confirmation remains incomplete.
