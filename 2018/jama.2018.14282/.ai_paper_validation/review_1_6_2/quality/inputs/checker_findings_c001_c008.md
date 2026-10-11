### F-NUM-001

**Observation:** Four Table 1 count/percentage pairs do not reconcile with their printed arm denominator.

**Exact source locations and document roles:** REPORT [main article physical p.4, Table 1](../../../../jama_azoulay_2018_oi_180109.pdf#page=4), headers n=388 in both columns: chronic liver disease H row; chronic kidney disease C row; postextubation randomization H and C cells. REPORT same table footnotes a–f supply definitions but no alternate denominators. Canonical relationships N017, N018, N035. Every affected location is included in this single denominator-pattern finding.

**Printed inputs:** H liver 45(13.3%); C kidney 69(20.4%); postextubation H 14(4.1%), C 18(5.3%); denominator 388 for each arm.

**Rule and calculation:** For 100 n/d, allow n and d their ±0.5 intervals, then compare the output with the printed percentage ±0.05 percentage points.

| Affected cell | Central recomputation | Recomputed half-unit interval, % | Printed percentage interval, % | Relative discrepancy |
|---|---:|---|---|---:|
| H liver | 45/388×100=11.5979% | [11.4543,11.7419] | [13.25,13.35] | 1.5081/13.3=.113388 |
| C kidney | 69/388×100=17.7835% | [17.6319,17.9355] | [20.35,20.45] | 2.4145/20.4=.118359 |
| H postextubation | 14/388×100=3.6082% | [3.4749,3.7419] | [4.05,4.15] | .3081/4.1=.075138 |
| C postextubation | 18/388×100=4.6392% | [4.5045,4.7742] | [5.25,5.35] | .4758/5.3=.089775 |

All exceed 0.05 after display precision. Other numerator/denominator percentages in Table 1 were checked; they reconcile under the same rule. Numerators with explicitly smaller denominators, such as chemotherapy 221/294, were checked against those explicitly printed denominators.

**Focus area:** A, counts and denominators.
**Proposed review domain:** statistical_results.
**Proposed relationship:** S_W; all relationships S_W.
**Qualifying route:** Route A, category 3.
**Affected result or extracted value:** Baseline liver/kidney prevalences and the proportions randomized after extubation in each arm.
**Why context does not resolve it:** This is an always-register count/denominator/percentage conflict within one display. No row-specific available-case denominator is printed; the intended alternate denominator cannot be identified from the table.
**Alternatives:** Smaller available-case denominators might underlie the percentages, or counts/percentages might represent different source fields. A denominator near 338–339 would approximately explain these percentages, but the source does not state it. This is an inferred possible explanation, not a supplied denominator or proposed correction.
**Exact human question:** Which denominators and count/percentage pairs should be used for high-flow liver disease, standard-oxygen kidney disease, and postextubation randomization in both groups, and were any row-specific missing-data denominators omitted from Table 1?

### F-XS-001

The abstract assigns oxygenation to a post-intubation period while the reported matching result belongs to the randomization-based oxygenation series.

- **Locations and roles:** REPORT [main p.1, Main Outcomes and Results](../../../../jama_azoulay_2018_oi_180109.pdf#page=1); REPORT [main p.6, Secondary Outcomes](../../../../jama_azoulay_2018_oi_180109.pdf#page=6); REPORT [supplement p.2, eTable](../../../../joi180109supp2_prod.pdf#page=2) and [p.4, eFigure 2B](../../../../joi180109supp2_prod.pdf#page=4). Mapper keys N010, S023, R4-02, R4-05.
- **Printed statements and values:** Abstract secondary outcome is PaO2/FiO2 over three days after intubation; its150 versus119 and difference 19.5 (95%CI 4.4–34.6) reappear in narrative describing higher oxygenation until day 4. The eTable explicitly reports150[104–230] versus119[86–165] six hours after randomization; eFigure 2 uses randomization, H6, days 1–7.
- **Comparison logic:** Match150/119 and19.5 interval across abstract/narrative; then compare outcome time origin and population. Post-intubation subset/time is not interchangeable with the randomized oxygenation series. No arithmetic discrepancy is alleged: matching printed numeric intervals overlap, discrepancy0; display precision cannot convert the two time/population definitions.
- **Focus area:** B/C. **Proposed review domain:** report_internal_inconsistency. **Relationship type:** S_C. **All relationships:** S_C, S_W.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Population and measurement window for the PaO2/FiO2 treatment effect19.5 (4.4–34.6).
- **Why context does not resolve it:** Both post-intubation oxygenation and early randomized oxygenation are plausible outcomes, and the abstract explicitly assigns a different time origin rather than using an abbreviated endpoint name.
- **Supported alternatives:** The abstract may intend three days after randomization; a separate intubated-subset result may be intended, but none of the supplied displays identifies19.5 as that result.
- **Exact human question:** Does the oxygenation effect19.5 (95%CI 4.4–34.6) apply to measurements after randomization or after intubation, and to which patients and measurement window?

### F-XS-003

The matching IMV cumulative-incidence result is attributed to Gray testing in the article and log-rank testing in the supplement.

- **Locations and roles:** REPORT [main p.3, competing-risk definition](../../../../jama_azoulay_2018_oi_180109.pdf#page=3); REPORT [main p.4, methods continuation](../../../../jama_azoulay_2018_oi_180109.pdf#page=4); REPORT [main p.5, Table 2 IMV P=.17](../../../../jama_azoulay_2018_oi_180109.pdf#page=5) and [p.6, IMV result and supplement pointer](../../../../jama_azoulay_2018_oi_180109.pdf#page=6); REPORT [supplement p.3, eFigure 1](../../../../joi180109supp2_prod.pdf#page=3). Keys S006, S015, R4-03.
- **Printed statements:** Article cumulative incidence with death withoutIMV as competing risk, compared by Gray test; matching IMV P=.17. eFigure 1 labels cumulative incidence of mechanical ventilation and P(log Rank test)=.17.
- **Comparison logic:** Same randomized population, time since randomization, day 28 IMV and P .17, but different named inferential procedures. Numeric copies overlap[.165, .175], discrepancy0; this is method attribution, not a numeric-copy difference .
- **Focus area:** C. **Proposed review domain:** statistical_results. **Relationship type:** S_C. **All relationships:** S_C.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Test identity for the reported day 28 cumulative-IMV P=.17.
- **Why context does not resolve it:** Gray and log-rank tests target differently handled event processes; neither the figure nor its article pointer says separate tests produced the coincident printed P .
- **Supported alternatives:** The graph may show an additional log-rank comparison; alternatively its test label may denote the article's Gray comparison. The supplied material does not distinguish these possibilities.
- **Exact human question:** Is eFigure 1 P=.17 from the Gray test or a separate log-rank test, and how were competing events handled for that plotted comparison?

### F-XS-004

The primary effect measure changes from planned risk ratio to reported hazard ratio.

- **Locations and roles:** PLAN [p.54, lines 808–812](../../../../joi180109supp1_prod.pdf#page=54), [p.82, lines 1297–1300](../../../../joi180109supp1_prod.pdf#page=82), [p.104, lines 1730–1734](../../../../joi180109supp1_prod.pdf#page=104); REPORT [main p.3, primary methods](../../../../jama_azoulay_2018_oi_180109.pdf#page=3), [p.5, Table 2](../../../../jama_azoulay_2018_oi_180109.pdf#page=5). Keys S-P 2-022, S307, P4-17, S005, S013.
- **Printed specifications:** Plan binary alive/dead at day 28, relative risk of hospital death experimental/control with95%CI . Article Kaplan–Meier, absolute RD and univariable CoxHR.98(.77, 1.24); Table 2 uses RR for ICU/hospital mortality but HR for primary day 28 mortality.
- **Comparison logic:** Same primary treatment comparison and day 28 endpoint; RR and HR are different estimands. No numerical conflict is claimed between a hazard ratio and a crude risk ratio. Numeric precision is not applicable to a categorical effect-measure change.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Primary day 28 mortality effect-measure identity and planned versus reported estimand.
- **Why context does not resolve it:** The final published plan retains RR while the report specifies CoxHR; the disclosed noninferiority-to-superiority revision does not explain this final-plan measure change.
- **Supported alternatives:** CoxHR may replace the planned RR; alternatively a planned RR analysis may have been performed but not supplied. Hospital-death wording may refer to day 28 death, which does not equate RR with HR .
- **Exact human question:** Was the prespecified primary day 28 risk-ratio analysis replaced by the Cox hazard-ratio analysis, and where is the applicable analysis-plan change or the planned RR result documented?

### F-XS-005

Prespecified adjusted and per-protocol primary analyses are not reported in the supplied results.

- **Locations and roles:** PLAN [p.53, lines 786–787](../../../../joi180109supp1_prod.pdf#page=53), [p.54, lines 808–812](../../../../joi180109supp1_prod.pdf#page=54), [p.82, lines 1297–1300](../../../../joi180109supp1_prod.pdf#page=82), [p.104, lines 1723, 1734](../../../../joi180109supp1_prod.pdf#page=104); REPORT [main p.3, univariable primary analysis](../../../../jama_azoulay_2018_oi_180109.pdf#page=3), [p.5, Table 2](../../../../jama_azoulay_2018_oi_180109.pdf#page=5), [p.8, unadjusted-treatment-effect limitation](../../../../jama_azoulay_2018_oi_180109.pdf#page=8); REPORT results supplement pp.1–5 contains no PP or adjusted-primary display. Keys S-P 2-017, S-P 2-022, S307, P4-15, P4-17, S005, S010.
- **Printed specifications:** Final plan explicitly says per-protocol analysis will be performed and analyses adjusted for potential confounders will be performed. Article reports allocation-based388-per-arm univariableCox and states effects were not adjusted for stratification factors. Its post hoc site frailty model is a different specified analysis.
- **Comparison logic:** Complete report search across article/supplement finds no PP primary population/result and no planned adjusted-primary result. This is a planned primary analysis omission, not merely an unreported model detail. Missing PP membership rules and covariate names are acknowledged; numeric rounding is not applicable.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** Primary mortality sensitivity to adherence-based population and prespecified confounder adjustment.
- **Why context does not resolve it:** Category5 applies; an unadjustedITT result and post hoc site model do not supply the planned PP and confounder-adjusted analyses.
- **Supported alternatives:** These analyses may exist outside the supplied report; PP may coincide with another set, but substantial reported treatment crossovers mean equality cannot simply be assumed. The final plan may retain superseded requirements without a disclosed corresponding amendment.
- **Exact human question:** Were the final-plan per-protocol and confounder-adjusted primary analyses performed, and what are their populations, covariates and results, or the documented reason for their replacement?

### F-XS-006

The reported ICU-acquired-event analyses differ from the planned competing-risk specification.

- **Locations and roles:** PLAN [p.54, lines 816–821](../../../../joi180109supp1_prod.pdf#page=54), [p.82, lines 1305–1310](../../../../joi180109supp1_prod.pdf#page=82), [p.105, lines 1738–1742](../../../../joi180109supp1_prod.pdf#page=105); REPORT [main p.3, IMV competing risk](../../../../jama_azoulay_2018_oi_180109.pdf#page=3), [p.4, infection/IMV methods](../../../../jama_azoulay_2018_oi_180109.pdf#page=4), [p.5, Table 2 infection footnoted cause-specificHR](../../../../jama_azoulay_2018_oi_180109.pdf#page=5), [p.6, secondary outcomes](../../../../jama_azoulay_2018_oi_180109.pdf#page=6). Keys S-P 2-024, S309, S310, P4-18, S006, S007, S015, S016.
- **Printed specifications/values:** Plan both intubation/infection cumulative incidence with death or liveICU discharge competing, Gray tests and adjusted cause-specificCox. Report intubation death-withoutIMV competition and univariableCox; infection proportions compared byχ2; infection39/388 versus41/388, HR 1.01(.96, 1.06), P .91, footnoted cause-specificHR.
- **Comparison logic:** Named shared key-secondary endpoints have changed test/model/event specifications. LiveICU discharge is absent from article's explicit IMV competing-event definition; infectionχ2 is not plannedGray. No inference from crude counts is substituted for model estimates. Precision not applicable to these analysis-rule differences.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** IMV/infection cumulative-incidence estimands, competing events, infectionP.91 and effectHR1.01.
- **Why context does not resolve it:** The report explicitly identifies different methods while neither article nor results supplement explains replacement of the final-plan competing-risk strategy.
- **Supported alternatives:** The article may omit live-discharge competition from a fuller implemented model; infectionHR may arise from an additionalCox analysis whileχ2 suppliesP.91. Both require identification of the actual analysis rather than inferred conventions.
- **Exact human question:** Which competing events, adjustment and tests generated the reported IMV and infection results, and how do they relate to the final-plan Gray/cause-specificCox specification with death and live discharge competing?

### F-XS-009

Retained key-secondary outcome definitions contain prespecified measures absent from the supplied results.

- **Locations and roles:** PLAN [p.38, lines 548–550](../../../../joi180109supp1_prod.pdf#page=38), [p.46, lines 688–691](../../../../joi180109supp1_prod.pdf#page=46), [p.103, lines 1694–1697](../../../../joi180109supp1_prod.pdf#page=103); REPORT [main p.1, abstract](../../../../jama_azoulay_2018_oi_180109.pdf#page=1), [p.3, endpoint definitions](../../../../jama_azoulay_2018_oi_180109.pdf#page=3) and [p.6, dyspnea/oxygenation results](../../../../jama_azoulay_2018_oi_180109.pdf#page=6); REPORT [supplement p.2, eTable](../../../../joi180109supp2_prod.pdf#page=2), [p.4, eFigure 2B](../../../../joi180109supp2_prod.pdf#page=4), [p.5, eFigure 3B](../../../../joi180109supp2_prod.pdf#page=5). Keys S-P 2-003, P4-12, S023, S024, R4-02, R4-05, R4-07.
- **Printed specifications:** Final plan dyspneaVAS andBorg; oxygenation lowestSpO2 andPaO2/FiO2 days 1–3. Report dyspnea0–10VAS and oxygenationPaO2/FiO2; no Borg or lowestSpO2 outcome result appears in full supplied results.
- **Comparison logic:** Both dyspnea/oxygenation appear in abstract and retain secondary status; these are missing prespecified measurement analyses within retained key-secondary outcomes, not peripheral deleted early endpoints. Precision not applicable; no SpO2 values reconstructed from PaO2/FiO2 .
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category5.
- **Affected result or extracted value:** Whether null dyspnea and improved oxygenation conclusions cover the prespecified Borg and lowestSpO2 measures.
- **Why context does not resolve it:** Category5 applies to planned key-secondary measure analyses absent from report; the two scales/oxygen measures are not synonymous.
- **Supported alternatives:** OnlyVAS andPaO2/FiO2 may have been analyzed/reported; Borg/SpO2 may exist elsewhere or have been dropped. The disclosed earlier endpoint revisions do not explain their continued presence in final plan.
- **Exact human question:** What are the prespecified Borg dyspnea and lowestSpO2 oxygenation results, or where was their removal from the final-plan key-secondary outcome analyses documented?

### F-XS-011

The final plan prohibits control-group HFNO while the report permits rescue HFNO for DNI patients.

- **Locations and roles:** PLAN [p.99, line 1621](../../../../joi180109supp1_prod.pdf#page=99); REPORT [main p.3, control intervention](../../../../jama_azoulay_2018_oi_180109.pdf#page=3), [p.5, Interventions](../../../../jama_azoulay_2018_oi_180109.pdf#page=5). Keys P4-07, N006, N056.
- **Printed statements/values:** Final plan HFNO will not be used in control. Report HFNO could be used only for DNI patients after standard failure; 30(7.7%) controls switched, 14(46.7%) died.
- **Comparison logic:** Compare allowable randomized intervention strategy, not adherence alone. The report expressly authorizes a subgroup exception absent from final-plan rule. Counts are not divergent copies; rounding not applicable to prohibition versus allowance.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Treatment-policy interpretation of primary mortality and IMV under standard oxygen with authorized rescueHFNO.
- **Why context does not resolve it:** The report explains why rescue was used but does not reconcile permission with the categorical final-plan prohibition.
- **Supported alternatives:** An ethical rescue amendment or undocumented permitted exception may govern these patients; alternatively this was treatment crossover underITT rather than a prespecified allowance.
- **Exact human question:** Was DNI rescueHFNO a prespecified/amended control-strategy exception, and where is its authorization relative to the final-plan prohibition documented?

### F-XS-012

Patients at exactly9 L/min belong to different oxygen-flow strata in plan and report.

- **Locations and roles:** PLAN [p.99, line 1602](../../../../joi180109supp1_prod.pdf#page=99); REPORT [main p.2, Randomization](../../../../jama_azoulay_2018_oi_180109.pdf#page=2), [p.7, Figure 3A/B oxygen-flow rows](../../../../jama_azoulay_2018_oi_180109.pdf#page=7). Keys P4-06, N004, S035, S036, S048, S049.
- **Printed specifications:** Final plan<9 versus≥9 L/min; report>9 versus≤9 L/min. Figure repeats≤9/>9 with populations 348/347 versus40/41.
- **Comparison logic:** Truth-table comparison at exactly9 yields plan high/report low; all other flow values agree. Exact threshold membership is a logical criterion rather than a rounded copy of an estimate; half-unit percentage arithmetic is inapplicable.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Prespecified allocation strata and primary/IMV oxygen-flow subgroup membership and interactionP.39/.65.
- **Why context does not resolve it:** Equality membership cannot be inferred consistently from two explicit opposing inequalities; 9 L/min is a feasible clinical setting.
- **Supported alternatives:** Report reflects actual randomization lists and final-plan inequality differs; alternatively subgroup analysis used a revised boundary. Counts at exactly9 are not supplied.
- **Exact human question:** Were patients receiving exactly9 L/min randomized/analyzed in the lower or higher oxygen-flow stratum, and which plan/report boundary governs Figure 3?

### F-XS-013

The ICU-time forest subgroups differ from the reported stratification groups that the methods say define the subgroups.

- **Locations and roles:** REPORT [main p.2, Randomization](../../../../jama_azoulay_2018_oi_180109.pdf#page=2), [p.4, subgroup methods and Table 1 randomization timing](../../../../jama_azoulay_2018_oi_180109.pdf#page=4), [p.5, three predefined subgroups claim](../../../../jama_azoulay_2018_oi_180109.pdf#page=5), [p.7, Figure 3A/B ICU-time rows](../../../../jama_azoulay_2018_oi_180109.pdf#page=7). PLAN [p.98, lines 1600–1601](../../../../joi180109supp1_prod.pdf#page=98) and [p.99, line 1602](../../../../joi180109supp1_prod.pdf#page=99) corroborate reported allocation boundary only. Keys N004, N031–N034, S009, S031, S032, S044, S045, P4-06.
- **Printed specifications/counts:** Randomization≤2 versus≥3 days; methods subgroup effects defined by stratification variables. Figure 0–1 versus≥2 days, 321/330 and67/58 patients. Table 1 days 0, 1, 2, ≥3:H244, 77, 47, 20; C251, 79, 38, 20.
- **Calculation:** Figure low subgroup321=244+77 and330=251+79; high67=47+20 and58=38+20. Reported allocation low would368=244+77+47 and368=251+79+38; high20/20. Integer counts are exact membership counts; the discrepancy in low-H population47/368=.1277 and low-C38/368=.1033 exceeds5% even if conventional half-unit intervals are allowed: recomputed three-input totals[366.5, 369.5], figure low-H[320.5, 321.5] and low-C[329.5, 330.5], gaps45 and36, relative discrepancies45/368=.1223 and36/368=.0978. Thus this is actual regrouping, not only a heading abbreviation.
- **Focus area:** A/C. **Proposed review domain:** report_internal_inconsistency. **Relationship type:** S_W. **All relationships:** S_W. The PLAN is corroboration, not a conflict location.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Population/time definition of ICU-time primary-mortality andIMV subgroup effects and interactionsP.15/.17.
- **Why context does not resolve it:** Table 1 supports the figure grouping, but the methods explicitly tie analyses to different stratification groups; no regrouping rule is given.
- **Supported alternatives:** Figure intentionally uses an analysis-specific0–1/≥2 boundary; methods may describe only variables and omit changed category thresholds. These alternatives require clarification of which subgroup analysis was prespecified.
- **Exact human question:** Why does Figure 3 use0–1/≥2 days rather than the≤2/≥3day randomization strata, and which grouping was prespecified for the reported interactions?

### F-ST1-002

**Observation:** Planned primary relative-risk and adjusted analyses are not identified in the report.

- **Exact locations and document roles:** PLAN bundle p.54 lines 809–813; p.82 lines 1297–1300; p.104 lines 1731–1734. REPORT main article p.3 Statistical Analysis; p.5 Table 2 and Primary Outcome; p.8 discussion of no stratification adjustment.
- **Source links:** [REPORT main p.3](../../../../jama_azoulay_2018_oi_180109.pdf#page=3); [REPORT main p.5](../../../../jama_azoulay_2018_oi_180109.pdf#page=5); [REPORT main p.8](../../../../jama_azoulay_2018_oi_180109.pdf#page=8); [PLAN bundle p.54](../../../../joi180109supp1_prod.pdf#page=54); [PLAN bundle p.82](../../../../joi180109supp1_prod.pdf#page=82); [PLAN bundle p.104](../../../../joi180109supp1_prod.pdf#page=104).
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
- **Source links:** [REPORT main p.3](../../../../jama_azoulay_2018_oi_180109.pdf#page=3); [REPORT main p.4](../../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.5](../../../../jama_azoulay_2018_oi_180109.pdf#page=5); [REPORT main p.6](../../../../jama_azoulay_2018_oi_180109.pdf#page=6); [REPORT main p.7](../../../../jama_azoulay_2018_oi_180109.pdf#page=7); [REPORT main p.8](../../../../jama_azoulay_2018_oi_180109.pdf#page=8); [PLAN bundle p.53](../../../../joi180109supp1_prod.pdf#page=53); [PLAN bundle p.104](../../../../joi180109supp1_prod.pdf#page=104); [REPORT supplement 2 p.1](../../../../joi180109supp2_prod.pdf#page=1); [REPORT supplement 2 p.2](../../../../joi180109supp2_prod.pdf#page=2); [REPORT supplement 2 p.3](../../../../joi180109supp2_prod.pdf#page=3); [REPORT supplement 2 p.4](../../../../joi180109supp2_prod.pdf#page=4); [REPORT supplement 2 p.5](../../../../joi180109supp2_prod.pdf#page=5).
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
- **Source links:** [REPORT main p.3](../../../../jama_azoulay_2018_oi_180109.pdf#page=3); [REPORT main p.4](../../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.5](../../../../jama_azoulay_2018_oi_180109.pdf#page=5); [PLAN bundle p.54](../../../../joi180109supp1_prod.pdf#page=54); [PLAN bundle p.82](../../../../joi180109supp1_prod.pdf#page=82); [PLAN bundle p.105](../../../../joi180109supp1_prod.pdf#page=105).
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

### F-ST1-007

**Observation:** Planned and displayed subgroup boundaries differ.

- **Exact locations and document roles:** PLAN bundle p.98 lines 1600–1601 and p.99 lines 1602–1604. REPORT main article p.2 Randomization; p.4 subgroup method; p.7 Figure 3A/B time and oxygen-flow rows.
- **Source links:** [REPORT main p.2](../../../../jama_azoulay_2018_oi_180109.pdf#page=2); [REPORT main p.4](../../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.7](../../../../jama_azoulay_2018_oi_180109.pdf#page=7); [PLAN bundle p.98](../../../../joi180109supp1_prod.pdf#page=98); [PLAN bundle p.99](../../../../joi180109supp1_prod.pdf#page=99).
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

### F-ST1-009

**Observation:** Oxygenation outcome is attributed to a different window in the abstract.

- **Exact locations and document roles:** REPORT main article p.1 Main Outcomes and Measures/Results and p.6 Secondary Outcomes; REPORT results supplement p.2 e Table heading and PaO2/FiO2 row, p.4 e Figure 2B time axis.
- **Source links:** [REPORT main p.1](../../../../jama_azoulay_2018_oi_180109.pdf#page=1); [REPORT main p.6](../../../../jama_azoulay_2018_oi_180109.pdf#page=6); [REPORT supplement 2 p.2](../../../../joi180109supp2_prod.pdf#page=2); [REPORT supplement 2 p.4](../../../../joi180109supp2_prod.pdf#page=4).
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
- **Source links:** [REPORT main p.3](../../../../jama_azoulay_2018_oi_180109.pdf#page=3); [REPORT main p.4](../../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.6](../../../../jama_azoulay_2018_oi_180109.pdf#page=6); [REPORT supplement 2 p.3](../../../../joi180109supp2_prod.pdf#page=3).
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

### F-ST1-012

**Observation:** The final planned Borg dyspnea measure is not reported.

- **Exact locations and document roles:** PLAN bundle p.103 lines 1695–1696; corroborating initial PLAN p.38 dyspnea objective and p.90 secondary list. REPORT main article pp.1,3–4,6 and REPORT results supplement p.5 e Figure 3B.
- **Source links:** [REPORT main p.1](../../../../jama_azoulay_2018_oi_180109.pdf#page=1); [REPORT main p.3](../../../../jama_azoulay_2018_oi_180109.pdf#page=3); [REPORT main p.4](../../../../jama_azoulay_2018_oi_180109.pdf#page=4); [REPORT main p.6](../../../../jama_azoulay_2018_oi_180109.pdf#page=6); [PLAN bundle p.38](../../../../joi180109supp1_prod.pdf#page=38); [PLAN bundle p.90](../../../../joi180109supp1_prod.pdf#page=90); [PLAN bundle p.103](../../../../joi180109supp1_prod.pdf#page=103); [REPORT supplement 2 p.5](../../../../joi180109supp2_prod.pdf#page=5).
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
- **Source links:** [REPORT main p.3](../../../../jama_azoulay_2018_oi_180109.pdf#page=3); [REPORT main p.5](../../../../jama_azoulay_2018_oi_180109.pdf#page=5); [PLAN bundle p.99](../../../../joi180109supp1_prod.pdf#page=99).
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

