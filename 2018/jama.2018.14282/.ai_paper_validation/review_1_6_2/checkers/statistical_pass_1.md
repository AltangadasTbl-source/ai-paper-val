# Statistical consistency review — pass 1

Runtime ID: 01a129b9-3c75-7c50-8787-4de976dc68d0. Model gpt-6.1-sol; high reasoning; FRESH_SPAWN. QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md read completely. All 99 canonical S relationships were reviewed and recorded PASS_1_COMPLETE in statistics/relationship_inventory.md. Scope includes the complete main inferential map, all supplied protocol/SAP methods, every subgroup HR/CI/interaction and every results-supplement panel across 144 mapped source pages. Direct source reads used Poppler 25.03.0 on CPU; reusable text/images served as locators. No web or earlier scientific conclusions used. No assigned source coverage gap.

All displayed estimate/interval containment, endpoint order, null/P direction and stated conclusions were checked. No printed test statistic or standard error is supplied. Exact fitted-statistic reconstruction is limited by absent event times, covariance, fitted variance/CI definitions, and full model outputs. Missing details alone are not findings. Diagnostic approximations are labeled. Every emitted observation below was self-screened against the threshold; an independent screener must decide registration. No candidate IDs or adjudications are assigned here.

## Findings

### F-ST1-001

**Observation:** Figure 3 hazard-ratio direction differs from the report contrast.

- **Exact locations and document roles:** REPORT main article p.4 treatment-effect method (HFNO versus standard oxygen); p.5 Table 2 primary and IMV rows; p.6 IMV narrative; p.7 Figure 3A and 3B, all 26 HR rows and the left/right favors labels.
- **Source links:** [REPORT main p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5); [REPORT main p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6); [REPORT main p.7](../../../jama_azoulay_2018_oi_180109.pdf#page=7).
- **Printed values/statements:** Table 2: mortality HR 0.98 (0.77–1.24), IMV cause-specific HR 0.85 (0.68–1.06). Figure 3 all-patient rows: mortality 1.02 (0.81–1.29), IMV 1.17 (0.94–1.46). Both figure panels label values below 1 'Favors High-Flow Nasal Oxygen Therapy' and above 1 'Favors Standard Oxygen Therapy'.
- **Rule and calculation:** For an event HR stated as HFNO versus standard oxygen, HR below 1 favors HFNO. Inverting the reported IMV HR gives 1/0.85=1.17647, and reversing its interval gives [1/1.06,1/0.68]=[0.94340,1.47059], close to the figure 1.17 [0.94,1.46] within display precision. Mortality reciprocal 1/0.98=1.02041 likewise matches the figure. This indicates a reversed contrast with the original favors labels. The point-estimate half-unit intervals for the two IMV readings, [0.845,0.855] and [1.165,1.175], have gap 0.310; relative gap 0.310/0.85=0.36471>0.05. Direction mismatch, rather than the small mortality reciprocal difference, is the finding. No subgroup HR is equated to its crude risk ratio.
- **Focus area:** B.
- **Proposed review domain:** statistical_results.
- **Proposed relationships:** S_W.
- **Qualifying route:** Route A, category 2.
- **Affected result or extracted value:** Figure 3 treatment direction and all-patient/subgroup HRs for death and IMV, especially IMV HR 1.17 versus 0.85.
- **Why context does not resolve it:** The reproduced reversal of the HR/reference-group reading is category 2; reconstructing the reciprocal does not remove the printed direction a reader could extract.
- **Alternatives and missing definition:** The figure may have fitted standard oxygen versus HFNO while retaining HFNO-versus-standard favors labels; alternatively the relative HR values or labels use an unreported contrast. Event-time differences do not explain reciprocal all-patient values paired with the same event counts. The missing definition is the figure numerator/reference group.
- **Exact human question:** What is the numerator/reference treatment for every Figure 3 HR, and which favors labels apply to that contrast?

### F-ST1-002

**Observation:** Planned primary relative-risk and adjusted analyses are not identified in the report.

- **Exact locations and document roles:** PLAN bundle p.54 lines 809–813; p.82 lines 1297–1300; p.104 lines 1731–1734. REPORT main article p.3 Statistical Analysis; p.5 Table 2 and Primary Outcome; p.8 discussion of no stratification adjustment.
- **Source links:** [REPORT main p.3](../../../jama_azoulay_2018_oi_180109.pdf#page=3); [REPORT main p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5); [REPORT main p.8](../../../jama_azoulay_2018_oi_180109.pdf#page=8); [PLAN bundle p.54](../../../joi180109supp1_prod.pdf#page=54); [PLAN bundle p.82](../../../joi180109supp1_prod.pdf#page=82); [PLAN bundle p.104](../../../joi180109supp1_prod.pdf#page=104).
- **Printed values/statements:** PLAN: binary alive/dead at day 28, relative risk of hospital death experimental versus control with 95% CI, and 'Analyses adjusted on potential confounders will be performed.' REPORT: Kaplan–Meier mortality, absolute RD, and HR from univariable Cox regression; Table 2 primary HR 0.98 (0.77–1.24), RD−0.5 (−7.3,6.3). No primary RR or confounder-adjusted primary result is identified.
- **Rule and calculation:** Compare the explicitly named planned primary estimand/adjustment with the supplied result methods. A risk ratio is not a time-to-event hazard ratio, and an explicitly univariable model is not the specified additional confounder-adjusted analysis. All supplied results have been searched through the complete mapped main and results supplement; no planned primary RR/adjusted result is identified. No model or covariate list is invented. Arithmetic/display rounding does not apply to this method replacement.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** The prespecified primary day 28 mortality treatment-effect measure and adjusted analysis, alongside the reported HR 0.98.
- **Why context does not resolve it:** Category 5 applies to a planned primary analysis that is replaced or not reported. The disclosed grant-stage superiority redesign does not explain the same RR/adjustment commitment retained in the original SAP and final published plan.
- **Alternatives and missing definition:** The published RR description may have been retained template text, or the analysis may have been amended or performed without a reported result. The supplied sources do not name that amendment or map a primary adjusted RR to any displayed estimate.
- **Exact human question:** Was the planned primary day 28 relative-risk and confounder-adjusted analysis performed, and where is its result or the specification replacing it?

### F-ST1-003

**Observation:** Retained final-plan primary per-protocol analysis is not reported.

- **Exact locations and document roles:** PLAN bundle p.53 lines 786–787 (initial requirement); p.104 line 1723 (final published analysis). REPORT main article pp.3–8 methods/results, and REPORT results supplement pp.1–5.
- **Source links:** [REPORT main p.3](../../../jama_azoulay_2018_oi_180109.pdf#page=3); [REPORT main p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5); [REPORT main p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6); [REPORT main p.7](../../../jama_azoulay_2018_oi_180109.pdf#page=7); [REPORT main p.8](../../../jama_azoulay_2018_oi_180109.pdf#page=8); [PLAN bundle p.53](../../../joi180109supp1_prod.pdf#page=53); [PLAN bundle p.104](../../../joi180109supp1_prod.pdf#page=104); [REPORT supplement 2 p.1](../../../joi180109supp2_prod.pdf#page=1); [REPORT supplement 2 p.2](../../../joi180109supp2_prod.pdf#page=2); [REPORT supplement 2 p.3](../../../joi180109supp2_prod.pdf#page=3); [REPORT supplement 2 p.4](../../../joi180109supp2_prod.pdf#page=4); [REPORT supplement 2 p.5](../../../joi180109supp2_prod.pdf#page=5).
- **Printed values/statements:** Initial PLAN requires both ITT and PP for noninferiority. Final PLAN retains 'Finally, a per-protocol analysis will be performed.' REPORT identifies ITT with 388/arm and post hoc analyses; no primary PP population or result appears.
- **Rule and calculation:** The final positive analysis commitment remains after conversion to superiority. Complete supplied results do not contain the planned primary PP estimate, denominator, interval, or test. The observation is the missing committed primary analysis, not merely the absence of a PP membership detail. Display precision is not applicable.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** The primary day 28 mortality sensitivity analysis on a planned per-protocol population.
- **Why context does not resolve it:** Category 5: a planned primary analysis is not reported. Original noninferiority rationale is an alternative explanation but does not remove the retained final-plan sentence.
- **Alternatives and missing definition:** The analysis may have been dropped with a later analysis amendment, or performed without a supplied result. No final PP membership rule or replacement instruction is available.
- **Exact human question:** Was the final-plan primary per-protocol analysis performed, and where are its population and result or the plan change removing it?

### F-ST1-004

**Observation:** Planned competing-risk and adjusted secondary framework differs from reported methods.

- **Exact locations and document roles:** PLAN bundle p.54 lines 817–821; p.82 lines 1305–1310; p.105 lines 1738–1742. REPORT main article pp.3–4 Statistical Analysis and p.5 Table 2 IMV/infection rows.
- **Source links:** [REPORT main p.3](../../../jama_azoulay_2018_oi_180109.pdf#page=3); [REPORT main p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5); [PLAN bundle p.54](../../../joi180109supp1_prod.pdf#page=54); [PLAN bundle p.82](../../../joi180109supp1_prod.pdf#page=82); [PLAN bundle p.105](../../../joi180109supp1_prod.pdf#page=105).
- **Printed values/statements:** PLAN: intubation/infection cumulative incidence with death or live ICU discharge competing; Gray comparison and confounder adjustment by cause-specific Cox. REPORT: IMV death without IMV as competitor, Gray test, univariable cause-specific Cox; infection proportions by chi-square. Table 2 prints IMV HR 0.85 (0.68–1.06),P=.17; infection HR 1.01 (0.96–1.06),P=.91.
- **Rule and calculation:** The planned competitor set includes ICU discharge alive; the reported IMV description names death without IMV and does not map discharge to an event/censoring rule. Planned infection Gray comparison is replaced by an explicitly named chi-square comparison of proportions. Planned adjusted Cox analyses are not identified; IMV is explicitly univariable. These are source-grounded analysis specifications, not a preference for one competing-risk method. Display precision is not applicable.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Abstract-reported/key secondary IMV and infection comparisons and their event-risk populations and treatment effects.
- **Why context does not resolve it:** Category 5 applies to planned key secondary analyses replaced or not reported. The final plan repeats the specifications after the grant-stage redesign.
- **Alternatives and missing definition:** Discharge handling may be abbreviated in the report, or the final methods may have changed; infection may have separate incidence and proportional analyses. None of the supplied sources maps the planned discharge competitor/adjusted Gray-Cox framework to the displayed numbers.
- **Exact human question:** Which competing events, discharge handling, comparison test and adjustment produced the reported IMV and infection results, and what replaced the corresponding final-plan analyses?

### F-ST1-005

**Observation:** Planned longitudinal joint-model analyses are not identified.

- **Exact locations and document roles:** PLAN bundle p.55 lines 825–826; p.82 lines 1314–1315; p.105 lines 1745–1747. REPORT main article p.4 Statistical Analysis; pp.1,6 repeated oxygenation/comfort/dyspnea results; REPORT results supplement pp.4–5.
- **Source links:** [REPORT main p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1); [REPORT main p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6); [PLAN bundle p.55](../../../joi180109supp1_prod.pdf#page=55); [PLAN bundle p.82](../../../joi180109supp1_prod.pdf#page=82); [PLAN bundle p.105](../../../joi180109supp1_prod.pdf#page=105); [REPORT supplement 2 p.4](../../../joi180109supp2_prod.pdf#page=4); [REPORT supplement 2 p.5](../../../joi180109supp2_prod.pdf#page=5).
- **Printed values/statements:** PLAN: oxygenation, dyspnea and comfort analyzed with joint models accounting for right censoring. REPORT p.4 names Wilcoxon rank-sum for comfort/dyspnea; results report oxygenation difference 19.5 (4.4–34.6) and nonsignificant comfort/dyspnea over time. Figures provide no model/point/bar definition identifying a joint-model result.
- **Rule and calculation:** The joint-model commitment is explicit in the original SAP and final plan. The report names a different procedure for symptoms and never identifies the planned censoring-aware joint model or which reported longitudinal value it produced. This is not a proposed preferred model; it compares supplied descriptions. Rounding does not apply to the analysis mapping.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Abstract-reported/key secondary oxygenation, comfort and dyspnea longitudinal analyses.
- **Why context does not resolve it:** Category 5: planned key secondary joint-model analyses are replaced or not reported; the final plan retains them.
- **Alternatives and missing definition:** A joint model may have been fitted in addition to rank tests or used for a displayed mean contrast without being named. The supplied material does not define its longitudinal/survival components or identify its output.
- **Exact human question:** Were the planned joint models for oxygenation, comfort and dyspnea fitted, and which reported result corresponds to each model or to a stated replacement?

### F-ST1-006

**Observation:** Planned ICU length-of-stay survival analyses are not reported as specified.

- **Exact locations and document roles:** PLAN bundle p.54 lines 822–824; p.82 lines 1311–1313; p.105 lines 1742–1745. REPORT main article p.4 methods; p.5 Table 2 ICU stay; pp.1,6 ICU stay narrative.
- **Source links:** [REPORT main p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1); [REPORT main p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5); [REPORT main p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6); [PLAN bundle p.54](../../../joi180109supp1_prod.pdf#page=54); [PLAN bundle p.82](../../../joi180109supp1_prod.pdf#page=82); [PLAN bundle p.105](../../../joi180109supp1_prod.pdf#page=105).
- **Printed values/statements:** PLAN: ICU stay overall and separately in survivors and deceased, using Kaplan–Meier and competing-risk estimators as printed. REPORT: Wilcoxon rank-sum for ICU stay; medians 8 versus 6 days, mean difference 0.6 (−1.0,2.2),P=.07. No separate survivor/decedent survival-estimator result is supplied.
- **Rule and calculation:** The named planned estimators/populations differ from the reported rank comparison and quantitative mean difference. The planned survivor/decedent analyses are not supplied. Ambiguous 'former/latter' estimator attribution is preserved; it does not remove the positive planned analyses. Display precision does not apply to this specification comparison.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** The abstract-reported ICU length-of-stay analysis, overall and in planned survivor/decedent populations.
- **Why context does not resolve it:** Category 5: planned key secondary LOS analyses are replaced or not reported.
- **Alternatives and missing definition:** The rank test may have been an additional analysis or the plan may have been changed. No supplied result identifies the planned survival/competing-risk estimator or separate populations.
- **Exact human question:** Which reported ICU length-of-stay result corresponds to the planned overall and survivor/decedent survival analyses, or what analysis specification replaced them?

### F-ST1-007

**Observation:** Planned and displayed subgroup boundaries differ.

- **Exact locations and document roles:** PLAN bundle p.98 lines 1600–1601 and p.99 lines 1602–1604. REPORT main article p.2 Randomization; p.4 subgroup method; p.7 Figure 3A/B time and oxygen-flow rows.
- **Source links:** [REPORT main p.2](../../../jama_azoulay_2018_oi_180109.pdf#page=2); [REPORT main p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.7](../../../jama_azoulay_2018_oi_180109.pdf#page=7); [PLAN bundle p.98](../../../joi180109supp1_prod.pdf#page=98); [PLAN bundle p.99](../../../joi180109supp1_prod.pdf#page=99).
- **Printed values/statements:** Final PLAN: time D0/D1/D2 versus≥D3 and oxygen flow<9 versus≥9L/min. REPORT randomization: time≤2 versus≥3 days, oxygen flow≤9 versus>9L/min. Figure 3: time 0–1 versus≥2 days (321/330 and 67/58), oxygen≤9/>9 (348/347 and 40/41). Report method calls these stratification-defined subgroups.
- **Rule and calculation:** At exactly 9L/min, PLAN and REPORT assign different strata. At day 2, the REPORT randomization rule and Figure 3 time bins assign different subgroups. These are discrete membership changes, not rounded endpoints or stylistic inequality symbols: denominators and HRs are attached to those cutpoints. The time totals 321+67=388 and 330+58=388 establish a complete different partition, not a partial missing-data bin. No alternative strata are inferred.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationships:** P_R, S_W.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Planned treatment-by-stratum analyses and the Figure 3 time/flow subgroup denominators, HRs and interaction P values.
- **Why context does not resolve it:** Category 5: analyses described as stratification-defined do not use the supplied planned/stated boundary definitions. These inequalities change membership at actual values; they are not a symbol-only slip.
- **Alternatives and missing definition:** Separate subgroup bins may have been selected for analysis while randomization retained the planned strata, or one source may abbreviate its bins. The report does not distinguish that alternative or identify an amended flow threshold.
- **Exact human question:** What exact time-since-ICU-admission and oxygen-flow cutpoints were used for randomization and for each Figure 3 interaction/subgroup estimate, and were the analysis bins changed from the plan?

### F-ST1-008

**Observation:** Intubated mortality is reported as post hoc despite prospective secondary status.

- **Exact locations and document roles:** PLAN bundle p.6 lines 97–100; p.7 lines 142–146; p.38 secondary objectives; p.45 lines 675–676; p.47 lines 699–700. REPORT main article p.4 post hoc analysis description and p.6 Post Hoc Outcomes.
- **Source links:** [REPORT main p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6); [PLAN bundle p.6](../../../joi180109supp1_prod.pdf#page=6); [PLAN bundle p.7](../../../joi180109supp1_prod.pdf#page=7); [PLAN bundle p.38](../../../joi180109supp1_prod.pdf#page=38); [PLAN bundle p.45](../../../joi180109supp1_prod.pdf#page=45); [PLAN bundle p.47](../../../joi180109supp1_prod.pdf#page=47).
- **Printed values/statements:** Initial PLAN lists mortality after HFNO failure/intubation as secondary and prospectively names intubated-in-either-arm day 28 mortality. REPORT calls subset analyses in intubated patients post hoc and reports 55.3% versus 52.3%,RD+3 (−8.5,14.5),P=.65 there.
- **Rule and calculation:** The same post-intubation mortality subset/result is explicitly prospective secondary in the supplied initial plan but retrospectively labeled post hoc in REPORT. The final plan has a shorter secondary list, and REPORT p.3 discloses different secondary endpoints after redesign; these are source-grounded alternatives, not grounds to discard a reproduced outcome-status change. Display precision does not apply.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** The prespecification/outcome status of the reported intubated mortality contrast 55.3% versus 52.3%.
- **Why context does not resolve it:** Category 5 always registers a prespecified outcome whose status changes. The disclosed redesign is recorded as an alternative explanation.
- **Alternatives and missing definition:** The prospective analysis may have been removed with the grant-stage redesign and later reintroduced as post hoc, or only an additional intubated subset analysis may have been meant. The supplied report does not distinguish those analyses or date that status change.
- **Exact human question:** Was the reported intubated mortality contrast the prospectively listed secondary analysis, or was that analysis removed before the reported post hoc analysis, and where is the status change specified?

### F-ST1-009

**Observation:** Oxygenation outcome is attributed to a different window in the abstract.

- **Exact locations and document roles:** REPORT main article p.1 Main Outcomes and Measures/Results and p.6 Secondary Outcomes; REPORT results supplement p.2 e Table heading and PaO2/FiO2 row, p.4 e Figure 2B time axis.
- **Source links:** [REPORT main p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1); [REPORT main p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6); [REPORT supplement 2 p.2](../../../joi180109supp2_prod.pdf#page=2); [REPORT supplement 2 p.4](../../../joi180109supp2_prod.pdf#page=4).
- **Printed values/statements:** Abstract defines PaO2:FIO2 over 3 days after intubation and reports 150 versus 119, difference 19.5 (4.4–34.6). Supplement e Table labels 150[104–230] versus 119[86–165] as 6 hours after randomization. Figure axis starts at randomization/H6 then D1–D7; body says higher until day 4.
- **Rule and calculation:** The same oxygenation medians 150/119 are attached to the six-hour randomized time point in the results supplement, while the abstract outcome definition attaches oxygenation to days after intubation. These windows have different population/time origin; they are not immediately exchangeable. No exact mean is reconstructed from medians. Display precision is not relevant to the attribution mismatch.
- **Focus area:** B, D.
- **Proposed review domain:** report_internal_inconsistency.
- **Proposed relationships:** S_W, S_C.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** The time point and analysis population to extract for PaO2:FIO2 150 versus 119 and mean difference 19.5 (4.4–34.6).
- **Why context does not resolve it:** The abstract names intubation as the time origin while matching values occur in the randomized six-hour table. A reader cannot identify whether the abstract outcome/result concerns all randomized patients or an intubated subset without choosing between the printed windows.
- **Alternatives and missing definition:** The abstract may intend randomization rather than intubation, or its secondary outcome definition may refer to an additional post-intubation analysis. The source does not identify the latter result or map 19.5 to it.
- **Exact human question:** What population and time origin apply to the abstract PaO2:FIO2 result 150 versus 119 and difference 19.5, and how does it relate to the six-hour-after-randomization e Table?

### F-ST1-010

**Observation:** The cumulative ventilation figure names a different test.

- **Exact locations and document roles:** REPORT main article pp.3–4 IMV statistical method and p.6 cumulative incidence/e Figure pointer; REPORT results supplement p.3 e Figure 1.
- **Source links:** [REPORT main p.3](../../../jama_azoulay_2018_oi_180109.pdf#page=3); [REPORT main p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6); [REPORT supplement 2 p.3](../../../joi180109supp2_prod.pdf#page=3).
- **Printed values/statements:** Main method compares nonparametric IMV cumulative incidences by Gray test. e Figure 1 prints 'P (log Rank test) = 0.17'; main IMV result also prints P=.17.
- **Rule and calculation:** A Gray comparison of cumulative incidence and a log-rank comparison are distinct test definitions; the supplied report associates the same cumulative-incidence display with both names without mapping separate analyses. Equal rounded P values do not establish that they are the same procedure. This is a test-method identity observation, not an interval-versus-P significance conflict; display precision does not resolve method identity.
- **Focus area:** C.
- **Proposed review domain:** statistical_results.
- **Proposed relationships:** S_C.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** The comparison test to extract for the reported cumulative incidence of mechanical ventilation/P=.17.
- **Why context does not resolve it:** The main text and figure explicitly name distinct statistical procedures for the same outcome display, with no footnote distinguishing them.
- **Alternatives and missing definition:** The e Figure label may name an additional cause-specific survival comparison or use a generic label for the Gray comparison. The exact method and risk-set/competing-event treatment behind the plotted P are not supplied.
- **Exact human question:** Which comparison test generated P=.17 in e Figure 1, and how does that test relate to the Gray cumulative-incidence analysis described in the main article?

### F-ST1-011

**Observation:** The infection HR interval does not reproduce under the same-display interval diagnostic.

- **Exact locations and document roles:** REPORT main article p.5 Table 2 all three HR rows and footnote d; p.4 infection comparison method.
- **Source links:** [REPORT main p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5).
- **Printed values/statements:** Mortality:138/140 events,HR.98 (.77–1.24); IMV:150/170 events,HR.85 (.68–1.06); infection:39/41 events,HR 1.01 (.96–1.06), cause-specific HR per footnote. All 95% CIs.
- **Rule and calculation:** Diagnostic log-event-count interval H×exp(±1.95996×sqrt(1/e_H+1/e_C)) reproduces the mortality CI [0.77467,1.23975] and IMV CI [0.68244,1.05870] within printed half-unit intervals. Applied to the infection row it gives [0.65151,1.56574]. Allowing each count±0.5 and HR±0.005, lower endpoint range[0.64650,0.65653], upper[1.55374,1.57784]. Printed lower[0.955,0.965] has gap 0.29847/0.96=0.31091; printed upper[1.055,1.065] has gap 0.48874/1.06=0.46108. Both exceed 0.05. This is a diagnostic method supported by reproducing the other HR rows, not a claim that it is the exact fitted Cox covariance. No standard error or interval construction is supplied for the infection HR.
- **Focus area:** B, C.
- **Proposed review domain:** statistical_results.
- **Proposed relationships:** S_W.
- **Qualifying route:** Route A, category 4.
- **Affected result or extracted value:** The infection cause-specific HR95% CI0.96–1.06 and its precision for evidence extraction.
- **Why context does not resolve it:** Category 4: a printed interval does not reproduce under a method that reproduces the other rows of the same display. The missing model/variance/interval definition becomes the human question rather than making the observation conditional.
- **Alternatives and missing definition:** The infection HR interval may use a different analysis unit, event definition, variance or CI construction; the proportions chi-square P=.91 may belong to a separate comparison. These possibilities are not specified, and the diagnostic does not identify a final alternative interval.
- **Exact human question:** What event definition, analysis unit, model, variance estimator and confidence-interval construction produced the infection HR 1.01 (0.96–1.06), and why does its interval differ from the construction reproducing the other HR rows?

### F-ST1-012

**Observation:** The final planned Borg dyspnea measure is not reported.

- **Exact locations and document roles:** PLAN bundle p.103 lines 1695–1696; corroborating initial PLAN p.38 dyspnea objective and p.90 secondary list. REPORT main article pp.1,3–4,6 and REPORT results supplement p.5 e Figure 3B.
- **Source links:** [REPORT main p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1); [REPORT main p.3](../../../jama_azoulay_2018_oi_180109.pdf#page=3); [REPORT main p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6); [PLAN bundle p.38](../../../joi180109supp1_prod.pdf#page=38); [PLAN bundle p.90](../../../joi180109supp1_prod.pdf#page=90); [PLAN bundle p.103](../../../joi180109supp1_prod.pdf#page=103); [REPORT supplement 2 p.5](../../../joi180109supp2_prod.pdf#page=5).
- **Printed values/statements:** Final PLAN specifies dyspnea by VAS and Borg scale. REPORT lists dyspnea as a secondary outcome in the abstract, defines a0–10 dyspnea score, describes VAS rank comparisons and supplies only a VAS dyspnea panel; no Borg result appears.
- **Rule and calculation:** The final planned two-measure dyspnea outcome is key secondary because dyspnea is reported in the abstract. One measurement component is supplied and the separately named Borg component is absent from all supplied results. No Borg result is inferred from a VAS value; these are explicitly distinct scales in PLAN. Display precision does not apply.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** The planned Borg-scale component of the key secondary dyspnea outcome.
- **Why context does not resolve it:** Category 5: a planned key secondary outcome analysis/measurement component is not reported. Immediate VAS wording cannot identify a Borg result.
- **Alternatives and missing definition:** Borg measurement may have been omitted, considered redundant, or collected without a reported analysis; a later plan may have narrowed dyspnea to VAS. No supplied amendment or result establishes which applies.
- **Exact human question:** Was the final-plan Borg dyspnea measure collected and analyzed, and where is its result or the specification removing it from the key secondary dyspnea analysis?

### F-ST1-013

**Observation:** Final planned control oxygen strategy differs from the reported HFNO exception.

- **Exact locations and document roles:** PLAN bundle p.99 lines 1617–1623; REPORT main article p.3 standard oxygen treatment paragraph and p.5 Interventions.
- **Source links:** [REPORT main p.3](../../../jama_azoulay_2018_oi_180109.pdf#page=3); [REPORT main p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5); [PLAN bundle p.99](../../../joi180109supp1_prod.pdf#page=99).
- **Printed values/statements:** Final PLAN states 'HFNO will not be used in the control group.' REPORT permits HFNO only for do-not-intubate control patients after standard oxygen failure, and reports 30 controls (7.7%) switched,14(46.7%) died.
- **Rule and calculation:** The positive final-plan prohibition differs from a predefined reported exception used in 30/388=7.73196% of controls. Percentage/counts reconcile; the issue is the planned-versus-reported randomized intervention exposure, not a numerical count discrepancy or critique of clinical crossover. Display rounding does not apply to the allowed-treatment specification.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** The comparator oxygenation strategy and crossover allowance for the primary day 28 mortality/IMV treatment contrast.
- **Why context does not resolve it:** The exception changes actual randomized-comparator exposure for 30 participants; the report does not identify where the final prohibition was amended to permit it.
- **Alternatives and missing definition:** The exception may be rescue care introduced for DNI patients after protocol submission or may represent a disclosed operational rule omitted from the published plan. The supplied plan/report does not document the timing or replacement rule.
- **Exact human question:** When was rescue HFNO for control patients with do-not-intubate orders permitted, and what final intervention specification replaced the plan's prohibition?

### F-ST1-014

**Observation:** Figure 3 describes diagnosis and malignancy subgroup analyses as predefined, but the supplied plans do not contain them.

- **Exact locations and document roles:** REPORT main article p.7 Figure 3 title and unknown-diagnosis/hematologic-malignancy rows in panels A/B; p.4 subgroup methods. PLAN bundle pp.45–46, lines 666–680, initial subgroup list; pp.98–99, lines 1600–1604, final strata; p.104, lines 1721–1723 and 1735–1736, planned subset interaction strategy.
- **Source links:** [REPORT main p.7](../../../jama_azoulay_2018_oi_180109.pdf#page=7); [REPORT main p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4); [PLAN p.45](../../../joi180109supp1_prod.pdf#page=45); [PLAN p.46](../../../joi180109supp1_prod.pdf#page=46); [PLAN p.98](../../../joi180109supp1_prod.pdf#page=98); [PLAN p.99](../../../joi180109supp1_prod.pdf#page=99); [PLAN p.104](../../../joi180109supp1_prod.pdf#page=104).
- **Printed values/statements:** Figure 3 title says overall and in “Predefined Subgroups.” Unknown-diagnosis interactions are P=.12 for mortality and P=.9 for IMV. Hematologic-malignancy interactions are P=.5 for mortality and P=.01 for IMV; the IMV no-malignancy HR is 1.61 (1.16–2.23), and the malignancy HR is .89 (.65–1.22). Final PLAN names time since ICU admission, oxygen flow and shock strata; original PLAN adds oxygenation/organ-dysfunction and procedural/intubated/DNI subsets, but neither supplies unknown-diagnosis or hematologic-malignancy interaction analyses.
- **Rule and calculation:** Compare the report's positive predefined-analysis description with all supplied prospective subgroup specifications. The two diagnosis/disease subgroup analyses are absent from the complete supplied plan map. Eligibility definitions involving malignancy and historical associations involving unidentified ARF are not prospective treatment-interaction specifications. This is a prespecification mapping observation; display precision does not apply.
- **Focus area:** D.
- **Proposed review domain:** protocol_report.
- **Proposed relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Prespecification status of the unknown-diagnosis and hematologic-malignancy treatment interactions, including the IMV malignancy interaction P=.01 and subgroup HRs.
- **Why context does not resolve it:** Category 5 applies to an analysis described as prespecified that the supplied plan does not contain. The exploratory multiple-testing caution does not establish whether these particular subgroup analyses were prospectively defined.
- **Alternatives and missing definition:** These subgroups may have been prospectively added in another analysis document, or the figure title may collectively describe a mixture of planned and exploratory subgroups. No supplied amendment or subgroup-specific status distinguishes those possibilities.
- **Exact human question:** Where were the unknown-diagnosis and hematologic-malignancy subgroup interaction analyses prospectively specified, or which Figure 3 subgroups should be read as exploratory additions?

## Excluded observations

Only apparent issues not emitted are listed here; checks that reconcile are in the S records. One reason code per observation. The superseded initial noninferiority illustration is not an interval-versus-test finding on a reported estimate.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p.3 sample size versus PLAN p.103 | Total 779 versus 2×389=778; displayed half-unit intervals meet, and even an exact integer one-person gap is at most 0.05 relative. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main pp.1,6 respiratory-rate upper CI endpoint | −0.2 versus−0.3 has half-unit intervals meeting at−0.25; gapzero. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN pp.52,104 primary hypothesis | 'NIV' in otherwise explicitly HFNO-versus-oxygen strategy is immediately resolved by the surrounding intervention description. | TERMINOLOGY_OR_WORDING |
| PLAN pp.50,99 randomization sentence | 'Centre' randomization unit wording is resolved by the same patient allocation, parallel groups and central randomization-list paragraph; no cluster assignment is described. | TERMINOLOGY_OR_WORDING |
| PLAN pp.54,82,104 primary endpoint | 'Hospital death' immediately follows binary alive/dead classification atday 28; no distinct primary hospital horizon is numerically presented in PLAN. | TERMINOLOGY_OR_WORDING |
| PLAN pp.39–42 initial noninferiority illustration/rule | Generic efficacy-bound figure and literal lower-bound-less-than 9% prose are inside the explicitly superseded NI design; no reported superiority result relies on this rule. | OUT_OF_FOCUS |
| REPORT main p.7 sample-size assumptions statement | 'Assumptions ... met' does not define whether it means enrollment, operational assumptions or anticipated event rates; no separate realized power is printed. Wording uncertainty is screened out. | TERMINOLOGY_OR_WORDING |
| REPORT Supplement 2 pp.4–5 | Missing graph summary/bar confidence definitions and star legend alone do not reproduce a numeric/statistical conflict; bars are not assumed 95% CIs. | CONDITIONAL_OR_UNREPORTED |
| REPORT main Table 2 primary HR/P and Figure 2 | A diagnostic HR-Wald P around.87 differs from Table 2 .94, but no supplied text assigns Table 2 P to that HR-Wald test; log-rank .85 and PH residual .72 test separately named hypotheses. No same-analysis interval/P conflict is reproduced. | NOT_REPRODUCED |
| REPORT main pp.1,5–6 mean differences versus paired medians | A mean difference need not equal a difference of separately displayed medians; source footnote explicitly distinguishes means and descriptive medians. | CONTEXT_RESOLVES |
| PLAN p.100 line 1637 intervention exception | The continuous-HFNO paragraph immediately identifies standard oxygen as the intolerance/Venturi exception, despite the 'except ... will be used' wording. | TERMINOLOGY_OR_WORDING |
| PLAN pp.53,61 initial interim statements | No efficacy interim versus scheduled DSMB adverse-event reviews can denote distinct activities; later revised plan positively specifies efficacy interim and is followed. | CONTEXT_RESOLVES |
| REPORT main p.6 versus Supplement 2 p.4 oxygenation stars | 'Until day 4' versus stars on H6/D1–3 cannot be turned into conflicting significance without a supplied symbol/threshold definition. | TERMINOLOGY_OR_WORDING |
| PLAN pp.6–7,51 initial NI power/sample size | A diagnostic equal-event-rate normal NI formula assumes an unreported alternative event rate and exact test, so it cannot reproduce a defined source computation; formula details alone are not a finding. | CONDITIONAL_OR_UNREPORTED |

## Accounting and limits

Pass 1 complete:99 canonical relationships (S001–S099),14 findings (F-ST1-001–F-ST1-014),14 excluded observations. Direct scope: DOC-001 pp.1–9, DOC-002 pp.1–129, DOC-003 pp.1–5, DOC-004 p.1; scientific relationship coverage complete. Source-independent gaps: none. Exact Cox/joint-model/power refits cannot be made without the named source-dependent inputs. Historical Table 4 pp.127–128 has source-clipped right-edge text, and supplement plot points/bars have no exact numerical annotation/definition; readable content is fully mapped and no hidden values are inferred. All source and pre-existing assets remain preserved. Pass 2 must use a different fresh statistical runtime agent.


## Complete individual statistical-pass-1 record index

This index transcribes the original pass-1 completion facts preserved in the canonical statistical inventory. It supplements the checker summary with every canonical relationship ID; no new scientific finding or screening decision is introduced. Source locations and mapper provenance remain in statistics/relationship_inventory.md.

### S001

- **PASS_1_COMPLETE:** The report explicitly discloses the grant-stage noninferiority-to-superiority transition. Final PLAN pp.71–72,95,97 states superiority and mortality day 28. The report makes no noninferiority conclusion; the obsolete 9% margin is not applied to its superiority result. Outcome-status consequences are tracked at S070.

### S002

- **PASS_1_COMPLETE:** The final PLAN pp.90–91,103 prints 778=2×389; report p.3 prints 779 with 389 each. A one-person total discrepancy has relative display gap zero after half-unit intervals or less than 0.05. Diagnostic independent-proportions normal power formula with p C=.30,p H=.20,z(.975)=1.95996,z(.90)=1.28155 gives about 392/arm, close to 389; allowing printed integer percentage half-units includes 389. Exact design formula/continuity adjustment/interim adjustment are not supplied; no exact formula inferred. Report p.7 'assumptions ... met' is examined in excluded observations.

### S003

- **PASS_1_COMPLETE:** Observed interim P=.94 exceeds Haybittle–Peto .001; continuation follows the printed boundary. Final PLAN pp.102–103 agrees. Bayesian posterior rates/log OR and uniform prior are described without a numerical decision threshold, so no posterior threshold is inferred. Initial PLAN p.53 no interim differs from revised design; report explicitly discloses redesign. Safety DSMB interim wording at initial p.61 can be periodic safety review rather than the efficacy test.

### S004

- **PASS_1_COMPLETE:** 389 randomized per arm minus one consent withdrawal per arm gives 388; 2×388=776 analyzed. Report says no exclusions for missing data, not that every longitudinal measurement is observed. PLAN consent pp.74,79 permits data-use decisions on withdrawal. Final all-randomized ITT wording and source consent exclusions do not identify a conflicting analyzable count. Missing measurement denominators do not imply deletion from primary analysis.

### S005

- **PASS_1_COMPLETE:** REPORT p.3 gives Kaplan–Meier mortality, absolute RD and univariable Cox HR; PLAN pp.54,82,104 instead specifies binary day-28 RR and confounder-adjusted analyses. F-ST1-002 records the primary-analysis departure. Weighted-residual PH P=.72 is not significant; no numerical residual/test statistic, df or covariance is supplied, so exact reproduction is unavailable.

### S006

- **PASS_1_COMPLETE:** REPORT pp.3–4 gives death without IMV as competitor, nonparametric cumulative incidence, Gray comparison and univariable cause-specific Cox HR. PLAN pp.54,82,105 includes live ICU discharge as additional competitor and confounder adjustment. F-ST1-004 records that changed framework. Supplement e Figure 1 test label is independently tracked at S079.

### S007

- **PASS_1_COMPLETE:** REPORT p.4 names chi-square comparison for infection proportions; P=.91 is compatible diagnostically with continuity-corrected chi-square for 39/388 versus 41/388 (about.906). Continuity correction is not stated and is not assigned as the definitive test. Final PLAN p.105 instead describes Gray comparison/cause-specific Cox adjustment, tracked in F-ST1-004.

### S008

- **PASS_1_COMPLETE:** REPORT Wilcoxon rank-sum is internally coherent for independent randomized groups and quantitative available observations; it is not compared numerically to a mean-difference CI as if the same statistic were tested. PLAN survival/competing-risk LOS analyses and survivor/decedent analyses differ; F-ST1-006. Joint models separately S062.

### S009

- **PASS_1_COMPLETE:** Each printed interaction P belongs to a paired subgroup comparison, not the P for an individual HR. All interaction P values are ≥.05 except IMV hematologic-malignancy P=.01. The statement of no interaction applies to the three named stratification subgroups, whose printed P=.15,.39,.15 (mortality) and .17,.65,.83 (IMV) are nonsignificant. No df, variance or full Gail–Simon statistic is supplied. Changed subgroup boundaries tracked at S067/F-ST1-007; Figure 3 explicitly calls all displayed subgroups predefined; the unknown-diagnosis and hematologic-malignancy analyses are absent from the supplied prospective subgroup specifications, F-ST1-014.

### S010

- **PASS_1_COMPLETE:** Exploratory secondary status and absence of multiplicity correction are explicitly stated. No multiplicity-controlled superiority claim is printed. The .01 malignancy interaction is treated as exploratory. Post hoc frailty/site and intubated-subset labels examined against supplied plans, with the latter tracked F-ST1-008.

### S011

- **PASS_1_COMPLETE:** All REPORT P values are two-sided and alpha=.05. All displayed CIs are 95%. No test statistics or standard errors are directly printed. SAS/R in PLAN and R3.1.0 in REPORT are compatible, not a result-changing discrepancy.

### S012

- **PASS_1_COMPLETE:** RD −.5 is within[−7.3,6.3], HR .98 within[.77,1.24]; both intervals include null and P=.94>.05; direction and nonsignificant conclusion agree. Exact P from HR CI is not asserted without a specified HR test. Same primary occurrences are preserved at S013,S029.

### S013

- **PASS_1_COMPLETE:** 138/388=35.567% and 140/388=36.082%; difference−.51546pp, printed−.5. RD and HR CIs ordered/contain estimates and include null; P=.94 nonsignificant. Abstract/body agree. Figure 3 contrast differs (F-ST1-001). Diagnostic log-HR interval based on sqrt(1/138+1/140) reproduces its displayed endpoints within half-units; not an exact Cox refit.

### S014

- **PASS_1_COMPLETE:** RD−5.1 within[−12.3,2.0]; zero included; abstract conclusion nonsignificant agrees with paired main result P=.17. Risks match Table 2 under rounding.

### S015

- **PASS_1_COMPLETE:** 150/388=38.660%,170/388=43.814%,RD−5.15464pp. RD and cause-specific HR .85 [.68,1.06] are contained, ordered, include null and agree with P=.17 and narrative. Diagnostic log-event interval with sqrt(1/150+1/170) gives[.68244,1.05870], matching display. Full risk sets/competing-event times and fitted covariance are unavailable.

### S016

- **PASS_1_COMPLETE:** 39/388=10.052%,41/388=10.567%; RD−.51546pp. RD−.6 and HR 1.01 each contained in ordered intervals; both nulls included; P=.91 nonsignificant. Main abstract/body match. The HR interval [.96,1.06] does not reproduce under the event-count diagnostic that reproduces the other HR rows in this same display; F-ST1-011. The source-specific infection HR variance/interval construction is the human question.

### S017

- **PASS_1_COMPLETE:** 123/388=31.701%,122/388=31.443%;RD+.25773pp and RR123/122=1.00820, matching+.3 and 1.01 under half-units. Ordered CIs contain estimates/null, P=.64>.05. No stated secondary mortality test beyond effect measure permits exact P reconstruction.

### S018

- **PASS_1_COMPLETE:** 160/388=41.237%,162/388=41.753%;RD−.51546pp and RR160/162=.98765, matching−.5/.99. Ordered CIs contain estimates/null, P=.77>.05. Test mapping unspecified; exact P not inferred.

### S019

- **PASS_1_COMPLETE:** ICU medians 8/6 and their IQRs are ordered. Mean difference+.6 in[−1.0,2.2] and Wilcoxon P=.07 both nonsignificant. A difference of medians 2 is not the stated mean difference. Planned LOS methods examined in S008.

### S020

- **PASS_1_COMPLETE:** Hospital medians 24/27 and IQRs ordered; mean difference−2 within[−7.3,3.3], null included, P=.60>.05. The difference of medians−3 is not equated to the mean difference. Hospital-stay test/CI estimator not further specified.

### S021

- **PASS_1_COMPLETE:** Mean difference−1.8 contained in[−3.2,−.2], both endpoints<0 and significant claim agrees. Body upper endpoint−.3 differs; comparing half-unit intervals [−.25,−.15] and[−.35,−.25] yields zero gap, so rounding. Median 25/26 is not equated to mean difference.

### S022

- **PASS_1_COMPLETE:** Mean difference−1.8 contained in[−3.2,−.3], excluding 0; significant narrative agrees. e Table medians 25/26 and graph approximate means are separate summaries. No P/statistic printed for precise reproduction.

### S023

- **PASS_1_COMPLETE:** Mean difference 19.5 in[4.4,34.6], interval ordered/excludes 0; higher-oxygenation conclusion agrees. Median 150/119 is not equated to a mean difference 19.5. Abstract outcome window '3 days after intubation' differs from supplement 6h after randomization and repeated randomization-day figure; F-ST1-009. PLAN day 1–3 oxygenation/joint-model analyses separately S062,S070.

### S024

- **PASS_1_COMPLETE:** Comfort/dyspnea nonsignificance has no printed individual P or 95% between-group CI in REPORT. Supplement bars have no definition; they are not assumed confidence intervals or used to reverse significance. Planned joint models and Borg measure examined S062,S070.

### S025

- **PASS_1_COMPLETE:** Mean time difference−.5 lies within ordered[−1.2,.1], includes 0 and agrees with nonsignificance. IQR0–2 contains median 1. Individual timings/variance and test not supplied.

### S026

- **PASS_1_COMPLETE:** 55.3−52.3=3.0pp; estimate+3 within[−8.5,14.5], includes 0, P=.65>.05 agrees. Denominators are intubated subsets 150/170, not whole arms. Prespecified post-intubation mortality in initial PLAN versus REPORT post hoc status is F-ST1-008.

### S027

- **PASS_1_COMPLETE:** Difference+1.8 in ordered[−10.8,14.3], includes 0, P=.50>.05 agrees. This is the cancer versus no-cancer comparison described in narrative, not the treatment-by-hematologic-malignancy interaction in Figure 3. Arm/cancer risks and test not supplied.

### S028

- **PASS_1_COMPLETE:** Mortality site P=.33 and IMV site P=.07 are both>.05, consistent with nonsignificance. Mortality frailty analysis explicitly post hoc; no statistic/covariance/df supplied. No exact reconstruction attempted.

### S029

- **PASS_1_COMPLETE:** Figure 2 log-rank P=.85>.05 agrees with mortality-null CIs and nonsignificance. Table 2 P=.94 versus figure log-rank .85 need not be the same named test; the source does not assign Table 2 P specifically to log-rank. PH residual test P=.72 is a third, distinct hypothesis. At-risk counts are tracking, not additive deaths. No median survival is claimed.

### S030

- **PASS_1_COMPLETE:** Footnote explicitly defines binary absolute RD and quantitative difference of means despite common header. No HR claimed for LOS. All Table 2 estimates contained and endpoint orders checked. HR footnote labels IMV/infection as cause-specific, and both are examined with their corresponding method/text.

### S031

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S032

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S033

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S034

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S035

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S036

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S037

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S038

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S039

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.

### S040

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.

### S041

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.

### S042

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.

### S043

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S044

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S045

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S046

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S047

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S048

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S049

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S050

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S051

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S052

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.

### S053

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.

### S054

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval[1.16,2.23] excludes 1; no individual subgroup P is printed, so no interval/P conflict can be assessed. The paired hematologic-malignancy interaction P=.01 is significant and is a different hypothesis. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.

### S055

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs. The figure's predefined status for this clinical subgroup is F-ST1-014.

### S056

- **PASS_1_COMPLETE:** The printed HR lies within its ordered 95% interval. Interval includes 1; no individual subgroup P is printed. Paired interaction P is a different hypothesis and is tracked S009. All corresponding event counts are≤subgroup denominators; subgroup partitions/incomplete measurements are cross-referenced to numeric mapping. No source-supplied event times or covariance permit an exact Cox/interaction reconstruction. The Figure 3 H/C orientation versus printed HRs is part of F-ST1-001; crude ratios are not treated as model HRs.

### S057

- **PASS_1_COMPLETE:** REPORT Figure 3 left favors H/right favors C requires H/C event HR. IMV all-row HR 1.17 with that orientation conflicts with Table 2 H/C .85 and its lower-event direction; inverse .85≈1.176. F-ST1-001 consolidates the 26 row pattern and both panels. Individual model HRs are not expected to equal crude risk ratios.

### S058

- **PASS_1_COMPLETE:** Key Points/abstract/conclusion all assert no statistically significant day 28 mortality reduction; RD and HR null-containing intervals and P=.94/.85 support that reading. This does not assert equivalence or noninferiority.

### S059

- **PASS_1_COMPLETE:** No significant vasopressor/renal-replacement or discharge difference asserted, but no paired P/CI available. Printed count attribution tracked numerically through main N059; no inferred denominator/test. Different treatment populations/time windows are not reconstructed.

### S060

- **PASS_1_COMPLETE:** Treatment limitation count 170, deaths 135 gives 79.4118%, matching 79.4. Day 90 risks 46.9/48.2 labeled nonsignificant with no counts,P,CI or test; lack of precision alone is not a finding. It is a separate post hoc horizon, not D28 primary.

### S061

- **PASS_1_COMPLETE:** 816=2×408. The alternative-arm event rate and exact calculation routine are absent. A diagnostic equal-rate normal approximation gives about 294 per arm but assumes an unreported alternative, so no finding rests on it. The report discloses redesign; S002 covers the final superiority calculation.

### S062

- **PASS_1_COMPLETE:** A positive planned joint-model commitment is not identified in supplied results, while a different symptom procedure is named. F-ST1-005 records this planned-versus-reported analysis comparison. No preferred model is proposed; exact joint-model components and covariance are absent.

### S063

- **PASS_1_COMPLETE:** Final numeric eligibility thresholds substantially agree with the report. Initial definitions belong to the disclosed redesign. HIV/AIDs wording alone does not establish a changed analyzable count; no unsupported population count is inferred.

### S064

- **PASS_1_COMPLETE:** Final dose and weaning match the report. F-ST1-013 records the final control prohibition versus the reported rescue exception used in 30/388 controls. The p.100 line 1637 exception wording is immediately resolved by its paragraph and is excluded; no clinical treatment preference is proposed.

### S065

- **PASS_1_COMPLETE:** The final operational definition matches the reported result. The initial bilingual time-origin difference does not identify a conflicting reported primary value after redesign. SAP 'hospital death' follows classification as alive/dead at day 28; terminology is recorded in the excluded table.

### S066

- **PASS_1_COMPLETE:** The literal criterion differs from the signed generic illustration. It belongs to the expressly superseded NI design and is not applied to a reported superiority result; excluded OUT_OF_FOCUS. No NI conclusion is inferred from the report's superiority confidence intervals.

### S067

- **PASS_1_COMPLETE:** Patient allocation resolves the centre wording; no cluster model is inferred. Three binary strata produce 2^3=8 lists. Final-plan/report oxygen boundaries and report-internal time boundaries change subgroup membership: F-ST1-007.

### S068

- **PASS_1_COMPLETE:** The positive retained final primary-analysis commitment is absent from the results: F-ST1-003. Missing PP membership rules alone are not a separate finding. Superiority redesign does not remove the retained final-plan sentence.

### S069

- **PASS_1_COMPLETE:** Zero loss leaves the primary missing-data contingency untriggered. Predictor imputation models, imputation count and the named competing event are absent; missing detail alone is not a finding. Available secondary measurements are not equated to the primary population.

### S070

- **PASS_1_COMPLETE:** The prospective-secondary versus reported-post-hoc status is F-ST1-008, with redesign preserved as an alternative. The final Borg measure is absent: F-ST1-012. Removed initial non-key measures are not assumed to retain operational status after redesign.

### S071

- **PASS_1_COMPLETE:** Participation is not randomized oxygen exposure. A day 28 primary endpoint can coexist with longer follow-up. Consent/data-use permissions reconcile S004 exclusions; no additional conflicting count is derived.

### S072

- **PASS_1_COMPLETE:** Operational ascertainment and safety rules contain no reported conflicting efficacy test or number. Administrative timelines are outside statistical-design focus. All units remain mapped without inventing a primary/key safety analysis.

### S073

- **PASS_1_COMPLETE:** The intended intervention is immediately identifiable from the same paragraphs. Excluded TERMINOLOGY_OR_WORDING; no separate randomized NIV arm or changed numerical effect is inferred.

### S074

- **PASS_1_COMPLETE:** Initial subgroup definitions remain preserved. Intubated-result status is F-ST1-008. Conditional inferential subset analyses do not forbid descriptive forest rows. Exact interaction statistics and covariance are absent; no preferred test is proposed.

### S075

- **PASS_1_COMPLETE:** No different explicit report definition is supplied. An omitted repeated definition alone is not a discrepancy. Test framework and HR interval are examined at S007/S016.

### S076

- **PASS_1_COMPLETE:** Hospital-stay collection does not by itself designate a separate key analysis. Undefined point summaries/bars are not assumed means, standard errors or confidence intervals. Repeated displays are checked at S080–S083.

### S077

- **PASS_1_COMPLETE:** An exploratory intention without a primary/key model specification is not treated as an unreported primary/key analysis. No conflicting claim of prespecified predictor analysis appears. Missing optional exploratory output alone is not emitted.

### S078

- **PASS_1_COMPLETE:** 349=388−39 and 342=388−46; the 100% is 349/349 in the explicitly conditional non-intubated row. IQRs contain medians. Main medians match without equating their differences to mean contrasts. No P/CI printed here; window attribution is F-ST1-009.

### S079

- **PASS_1_COMPLETE:** The named procedures differ even when rounded P values agree. F-ST1-010 asks which generated the figure comparison. No interval/P significance conflict is asserted. Approximate curves and risk sets do not supply fitted event-time inputs.

### S080

- **PASS_1_COMPLETE:** Lower H6 HFNO direction matches the main negative confidence interval and significant statement. Undefined bars/star conventions prevent exact reconstruction; absence alone is not a finding. Counts need not equal primary N; planned joint models are S062.

### S081

- **PASS_1_COMPLETE:** Approximate higher HFNO oxygenation through day 4 matches the main positive interval. No bar confidence level or symbol threshold is supplied. 'Until day 4' versus star placement is not a reproduced numeric/test conflict without a symbol convention.

### S082

- **PASS_1_COMPLETE:** Approximate scores remain within 0–10. Different daily directions do not contradict reported nonsignificance. Undefined bars are not 95% between-group intervals. Joint models are S062; causes of lower observation counts are not inferred.

### S083

- **PASS_1_COMPLETE:** Scores remain within 0–10; no P or between-group interval permits exact significance reconstruction. No Borg panel/result is supplied, F-ST1-012. Joint models are S062.

### S084

- **PASS_1_COMPLETE:** Grant-stage revision explains initial/final design occurrences. Amendment wording may refer to formal post-approval changes; wording alone is not emitted. Explicit retained primary/key analysis commitments remain checked at S005,S062,S068,S070.

### S085

- **PASS_1_COMPLETE:** Directions agree with narrative. No arm sizes, CI, standard errors or identified test/sidedness allow exact reproduction. Historical rationale is not a HIGH result; clipped later text adds no complete independent value.

### S086

- **PASS_1_COMPLETE:** Count percentages round correctly. A significant three-arm comparison can coexist with a nonsignificant pair; exact test mapping/intervals are absent. No HIGH comparison is substituted.

### S087

- **PASS_1_COMPLETE:** Printed count relationships reconcile. Other directions lack CI/test inputs. Historical definitions are not applied to HIGH; right-edge clipping remains a source limitation.

### S088

- **PASS_1_COMPLETE:** No margin, CI or computational method is supplied for the historical NI conclusion. It cannot be reproduced from the summary and is not an operational HIGH rule. Missing historical detail alone is not a finding.

### S089

- **PASS_1_COMPLETE:** No test identity, CI, standard error or paired covariance is supplied. P=.44 does not conflict with a descriptive difference without those inputs. Historical clinical/eligibility wording does not identify a reported HIGH discrepancy.

### S090

- **PASS_1_COMPLETE:** 15+30=45 and printed percentages round correctly. Failure-group mortality direction agrees. No hospital-effect CI/test is supplied; not a HIGH randomized result.

### S091

- **PASS_1_COMPLETE:** 132/183=72.131%;41+44+15=100%. Category counts and effect intervals are absent; no integer events are invented from rounded percentages.

### S092

- **PASS_1_COMPLETE:** No changes, CIs, P values or standard errors are supplied. These verbal historical observations do not establish a conflicting current model or result.

### S093

- **PASS_1_COMPLETE:** Diagnostic reciprocals 1/.298=3.356 and 1/.29=3.448 lie in NNT3 half-unit interval[2.5,3.5]. ARR-copy relative gap.25/29.8=.00839≤.05. No reproduced result-changing gap.

### S094

- **PASS_1_COMPLETE:** Approximate population fraction does not provide exact events or intervals. Background response is not a HIGH treatment effect. No subgroup count/test is inferred.

### S095

- **PASS_1_COMPLETE:** Counts total 178 and percentages round. Unadjusted and separate adjusted directions may differ; no adjusted coefficient/CI reproduces a conflict. Historical wording is peripheral to a reported HIGH result.

### S096

- **PASS_1_COMPLETE:** Arms total 374; event fractions round, including 155/374=41.4%. Groups total 374 and HFNO groups 28+53+18+42=141. P values agree with verbal nonsignificance; exact tests/covariance absent. Bar heights are not exact events.

### S097

- **PASS_1_COMPLETE:** 60+55=115;30+25=55; percentages round. Higher NIV risks agree with narrative and significant P values. No adjusted coefficient/CI is supplied; no modeled effect is equated to crude risk.

### S098

- **PASS_1_COMPLETE:** Generic capacities are not HIGH assigned doses. Relevant measurement definitions link to S064/S076. No additional HIGH inferential result or operational decision rule is supplied.

### S099

- **PASS_1_COMPLETE:** No additional effect, test, primary/key analysis or prospective statistical decision rule is supplied. All inspected units remain covered. The data-sharing statement is REPORT by content. Administrative site/calendars are not used to infer a primary analysis-population change.

