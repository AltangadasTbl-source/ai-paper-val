# Cross-source consistency review — Workflow 1.6.2

Scope: all matched REPORT results and supplied PLAN statistical design elements for DOC-001 pp.1–11, DOC-002 pp.1–33, DOC-003 pp.1–19 and DOC-004 p.1. The complete canonical main/support maps were used, covering N001–N051, N101–N119 and S001–S082. All four documents were classified by content: DOC-002 is PLAN, including its addendum; the other three are REPORT. No structured data source is supplied. Original protocol and latest supplied 2015/2016 addendum were compared separately; an amendment is not silently treated as a contemporaneous plan contradiction. Source-linked comparisons use population, time, contrast, model, measure, analysis set and precision keys. All supplied units and relationships were covered; no scientific coverage gaps.

Evidence: source-matched reusable Poppler native/layout extracts and canonical CPU rendered pages, with direct `pdftotext -layout` rereading of exact source pages for the plan/report comparisons. Canonical main p.8 and supplementary p.18 were visually reread for headers and plot direction. No fresh OCR, Python, external literature or legacy scientific conclusions were used. Complete source maps retain exact graphic-only observations; no numerical forest interval endpoints were invented.

## Completed matching and design coverage

| Relationship scope | Comparison completed and result |
|---|---|
| N001–N005, N006, N009; S001–S002, S009–S020, S043–S050 | Abstract, Key Points, narrative, Tables2–3, Figure1, discussion/conclusions and applicable supplement results matched. Primary change/CI values agree across abstract/body/Table2; imputed population, observed contributors and paired samples kept distinct. Forest counts and ACR direction findings below are separate from effect-estimate agreement. Safety abstract/body/eTable11 counts agree. Composite164 equals85+79 and86+78; overlapping component counts are explicitly explained. |
| N007–N008, N010–N012; S003–S008; S051–S077 | Every planned/reported population, eligibility list, intervention, endpoint/status, composite component, time, model/covariate, missingness, interaction, subgroup, adherence, power, hypothesis, interim/stopping and multiplicity specification compared. Latest addendum explains the change to five-year eGFR, LMM, Cox and imputation. Findings distinguish documented outcome revision from other specification differences. |
| N013–N045, N101–N105, N113 | Narrative/baseline/flow/adherence/medication/safety occurrences checked; descriptive baseline-copy differences and administrative counts handled under comparison tiers. Full item-by-item eligibility reconciliation below. |
| N046–N048; S021–S042; N106–N118; S078–S082 | All figure panels, subgroup rows, continuous tables, categorical post-hoc tables, caption/footnote quantities and sensitivity keys checked. Full-imputed versus complete-case/adherent/UTI-excluded results are distinct analyses; their unequal estimates do not themselves conflict. Assay harmonization is explicitly described and matches eAppendix. |
| N049–N051; N119; no-applicable units | Background cited-study numbers, references and operational data-sharing statements inspected, without treating them as trial effect estimates or prospective analysis specifications. |

Eligibility was compared item by item, rather than inferred from an overall label. Original PLAN p.12 parent criteria: age60/65 differs (F-XS-003); education, calcium ceiling, run-in>67%, kidney stones, hypercalcemia, parathyroid disease, cirrhosis, granulomatous disease, fish allergy and serious illness have no contrary printed REPORT criterion (mere omission is not a finding). VitaminD≤800 and foregoing fish oil agree; CVD/cancer exclusions agree in scope (expanded versus abbreviated descriptions). Kidney failure exclusion agrees with reported ESKD exclusion. Ancillary self-reported physician diabetes, gestational-only exclusion and non-diabetic kidney disease exclusion agree. The type1-diabetes proxy differs (F-XS-004). A kidney-transplant-specific exclusion is not separately reported, without a contrary inclusion statement. PLAN required actual baseline blood/urine return, whereas REPORT says agreement to provide samples; missing baseline measurements do not by themselves establish whether collection or assay failed, so this observation is not emitted. PLAN p.14 algorithm wording is retained, without assuming a different hypertension eligibility population from its malformed phrase.

Outcome components were compared individually: original ACR progression (doubling plus≥30), absolute eGFR loss≥12, ESRD and death; amended relative eGFR loss≥40%, ESRD and death; reported relative eGFR loss≥40%, kidney failure and death. Amended continuous ACR years2/5 is reported in eTable6; the distinct standalone categorical ACR analysis has the separate prespecification issue below. Post-hoc40%-decline/kidney-failure and30%-decline outcomes are consistently labeled post-hoc. No noninferiority/equivalence margin is supplied; two-sided alpha.05 and no formal multiplicity correction reconcile. Parent Haybittle–Peto monitoring is distinguished from ancillary final analysis, with no supplied claim of an ancillary interim crossing or early-stopping decision.

## Findings

### F-XS-001 — Forest-display participant counts do not reconcile with the assigned treatment groups

- **Locations and roles:** REPORT [main p.1 allocations](../../../jama_de_boer_2019_oi_190122.pdf#page=1), [p.5 Table1](../../../jama_de_boer_2019_oi_190122.pdf#page=5), [p.6 Figure1](../../../jama_de_boer_2019_oi_190122.pdf#page=6), [p.8 Figure3 and Table2](../../../jama_de_boer_2019_oi_190122.pdf#page=8), [p.9 Figure4](../../../jama_de_boer_2019_oi_190122.pdf#page=9); REPORT [supplement p.18 eFigure2](../../../joi190122supp2_prod.pdf#page=18), [p.19 eFigure3](../../../joi190122supp2_prod.pdf#page=19), [p.16 eTable11](../../../joi190122supp2_prod.pdf#page=16).
- **Printed comparison:** Four assigned groups are370 BOTH,333 D-only,289 omega-only,320 neither. VitaminD active is therefore703 and placebo609; eTable11 states these marginal counts. Figure3 and eFigure2 instead print overall Placebo703 and VitaminD/Active609, alongside means that match the treatment-specific effects in Table2/eTable6. Their omega-assignment rows print Placebo-column333/370 and Active-column320/289. Figure4/eFigure3 print the D-assignment-placebo row as Placebo289 and Omega320, whereas allocation has neither320 and omega-only289; the D-assignment-active row prints Placebo370 and Omega333, whereas allocation has D-only333 and BOTH370.
- **Rule/reproduction:** Match randomized marginal and factorial-cell counts to the same assignment labels, independently of observed contributor counts. For D-placebo609 versus printed703, conservative recomputed interval from320+289 is[608,610], printed703 interval[702.5,703.5], gap92.5/609=0.1519. For D-active703 versus609, interval[702,704] versus[608.5,609.5], gap92.5/703=0.1316. Factorial cells also exceed5% in several rows: e.g. Figure4 D-active omega-placebo370 versus assigned333 gives half-unit gap36/333=0.1081. The omega overall659-versus653 contrast alone falls within5%; it is not the basis for inclusion. All affected rows of the four forest displays are retained as occurrences of the same assignment/count-column pattern, without claiming an independently reproduced discrepancy in every subgroup count.
- **Focus area:** A. **Proposed review domain:** statistical_results. **Relationship type:** S_C. **All relationships:** S_C, S_W.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Treatment-specific randomized denominator and assignment attributed to the primary eGFR forest summaries and the parallel ACR subgroup summaries.
- **Why context does not resolve it:** The printed headers place counts beside treatment-specific means; the package does not state that count columns use the opposite assignment from the mean columns. Reconstructing allocation does not specify which subgroup counts accompany which estimates.
- **Supported alternatives/missing definition:** Count columns may have been exchanged while means and forest contrasts retain their intended labels; alternatively another unexplained population/count convention was used. No convention explaining this is supplied.
- **Human question:** Which assignment does each forest count column represent, and which exact counts accompany each treatment-specific mean and subgroup contrast?

### F-XS-002 — ACR forest favor labels reverse the direction of the printed active/placebo ratio

- **Locations and roles:** REPORT [supplement p.18 eFigure2](../../../joi190122supp2_prod.pdf#page=18), [p.19 eFigure3](../../../joi190122supp2_prod.pdf#page=19), [p.11 eTable6](../../../joi190122supp2_prod.pdf#page=11); REPORT [main p.4 ACR narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4). PLAN [p.11 hypotheses](../../../joi190122supp1_prod.pdf#page=11) and [p.17 ACR definition](../../../joi190122supp1_prod.pdf#page=17) corroborate the direction only, and are not conflicting locations.
- **Printed comparison:** The eFigure2/3 axis is “Ratio of change, active/placebo (95%CI)” with null1; left (<1) says Favors Placebo and right (>1) says Favors VitaminD/Omega-3. eTable6 describes these changes as baseline-to-year5 ACR ratios; eFigure overall placebo3.02 versus active2.97 for D and3.05 versus2.94 for omega. The trial hypotheses seek slower albuminuria progression, and main p.4 describes the observed threefold rise.
- **Rule/reproduction:** For a ratio of ACR increase active/placebo, a ratio below1 means a smaller increase with active treatment; above1 means a larger increase. The printed favor labels assert the reverse. This is a direction/reference-label comparison, not reconstruction of adjusted estimates from crude means; display-precision arithmetic does not resolve a reversed axis direction. The axis labels explicitly include values.5 and1.7, well away from the null.
- **Focus area:** B. **Proposed review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W.
- **Qualifying route:** Route A, category 2.
- **Affected result or extracted value:** Direction of benefit/harm attributed to all ACR subgroup forest ratios in eFigures2–3.
- **Why context does not resolve it:** RouteA category2 applies to reversal of direction/reference statements; a reader reconstructing intended benefit does not remove the printed direction issue.
- **Supported alternatives/missing definition:** Favor labels may be exchanged, or the axis could intend placebo/active despite its active/placebo text. The tables and plot title favor the latter text being the intended ratio definition, but no source resolves the choice.
- **Human question:** Are these forest ratios active/placebo or placebo/active, and which side of1 should the treatment-favor labels identify?

### F-XS-003 — Numeric age eligibility differs between the supplied protocol and report

- **Locations and roles:** PLAN [p.4 abstract](../../../joi190122supp1_prod.pdf#page=4), [p.11 aims](../../../joi190122supp1_prod.pdf#page=11), [p.12 Table1 and population](../../../joi190122supp1_prod.pdf#page=12); REPORT [main p.2 Study Population](../../../jama_de_boer_2019_oi_190122.pdf#page=2). The PLAN [pp.31–33 addendum](../../../joi190122supp1_prod.pdf#page=31) changes analysis, without revised age criteria.
- **Printed comparison:** Parent/ancillary eligibility is men≥60 and women≥65 in the plan, versus men≥50 and women≥55 in the report.
- **Rule/reproduction:** These define different eligible ranges (men50–59 and women55–64 enter only under the reported threshold). Even conservative half-unit threshold intervals do not overlap: gap9/60=.150 for men and9/65=.1385 for women; thresholds are operational criteria, not rounded age means.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Eligible population attached to the1312-person five-year primary eGFR treatment contrasts.
- **Why context does not resolve it:** No supplied amendment connects the two explicit numerical eligibility lists. The report gives the actual range but leaves which planned population the effect estimates represent changed.
- **Supported alternatives/missing definition:** Parent-trial age eligibility may have been revised in material outside this package; the supplied addendum may not be intended as a complete parent-protocol history. No additional plan is supplied.
- **Human question:** Which dated eligibility amendment lowered the age thresholds, and which thresholds defined this ancillary cohort?

### F-XS-004 — The type1-diabetes exclusion proxy changes its insulin criterion

- **Locations and roles:** PLAN [p.12 eligibility table/narrative](../../../joi190122supp1_prod.pdf#page=12), [p.14 enrollment algorithm](../../../joi190122supp1_prod.pdf#page=14); REPORT [main p.2 Study Population](../../../jama_de_boer_2019_oi_190122.pdf#page=2).
- **Printed comparison:** Plan excludes diagnosis before age30 AND “first treated with insulin”; report excludes diagnosis before30 AND insulin treatment for more than20years. These are initial treatment and treatment-duration criteria, respectively.
- **Rule/reproduction:** Item-by-item Boolean criterion comparison: neither insulin initially nor insulin duration>20 implies the other. A participant initially given insulin for≤20years meets the planned proxy but not the reported one; later insulin use>20years has the converse possibility. This is a logical definition difference; no display-precision rule applies.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Type2-diabetes analysis-population definition for the primary treatment contrasts.
- **Why context does not resolve it:** Both sources give explicit conjunctions; the report does not describe the duration rule as equivalent to initial insulin use or disclose a revised criterion.
- **Supported alternatives/missing definition:** Screening may have been updated to a pragmatic duration proxy; actual cohort membership changes cannot be counted from supplied aggregate data.
- **Human question:** Which insulin criterion was implemented, and where is the revised type1-diabetes exclusion specified?

### F-XS-005 — Latest planned primary analysis requires follow-up; reported primary analysis includes every randomized participant

- **Locations and roles:** PLAN [p.32 §15c](../../../joi190122supp1_prod.pdf#page=32); REPORT [main p.3 Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.4 retention](../../../jama_de_boer_2019_oi_190122.pdf#page=4), [p.6 Figure1](../../../jama_de_boer_2019_oi_190122.pdf#page=6), [p.8 Table2 footnote](../../../jama_de_boer_2019_oi_190122.pdf#page=8).
- **Printed comparison:** Latest plan defines ITT as all participants returning “at least one follow-up biosample.” Report explicitly says all randomized participants regardless of follow-up, Figure1 primary counts370+333+289+320=1312, and only1090 return≥1 follow-up blood sample,1091≥1 urine sample.
- **Rule/reproduction:** Compare inclusion criteria for the same primary baseline-to-year5 eGFR analysis. The report eliminates the latest plan's follow-up requirement. Blood-specific shortfall1312−1090=222; the union with urine returns is not supplied and is not claimed to equal1090 or1091. The discrepancy is the explicit population rule, independently of an unsupplied exact union size.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Full analytic denominator1312 and primary five-year estimates0.9(−0.7,2.5) and0.9(−0.7,2.6), generated under a population differing from the supplied planned primary analysis.
- **Why context does not resolve it:** RouteA category5 covers replacement of a planned primary analysis; consistent report use of all-randomized ITT does not reconcile the supplied planned inclusion condition.
- **Supported alternatives/missing definition:** A later amendment may authorize all-randomized imputation; no such amendment is supplied. Broader report ITT terminology is explicit and does not itself establish retrospective participant classification.
- **Human question:** Was the follow-up requirement formally removed, and which participants were included in the planned and reported imputation analyses?

### F-XS-006 — Imputation dataset count differs between latest plan and report

- **Locations and roles:** PLAN [p.32 §15c](../../../joi190122supp1_prod.pdf#page=32); REPORT [main p.3 Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.8 Table2 footnotes](../../../jama_de_boer_2019_oi_190122.pdf#page=8).
- **Printed comparison:** Plan combines10 chained-equations datasets using Rubin rules; report states multiple imputation M=20 and Rubin pooling.
- **Rule/reproduction:** Match the primary-analysis imputation setting:10 versus20. Half-unit intervals[9.5,10.5] and[19.5,20.5] have gap9, relative to10=.90, exceeding.05. No inference is made about the unreported chained-equations implementation.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Imputation/pooling specification used to produce the primary eGFR estimates and confidence intervals.
- **Why context does not resolve it:** These are explicit analysis settings, rather than an absent detail; no revised setting is supplied in plan material. The finding records specification divergence, without claiming it changes the paper's conclusion.
- **Supported alternatives/missing definition:** Twenty datasets may be an intentional later computational revision; the supplied plan records ten.
- **Human question:** Which final imputation specification governed the analysis, and when was the count revised from10 to20?

### F-XS-007 — Reported primary covariate adjustment differs from latest planned primary model

- **Locations and roles:** PLAN [p.32 §15e Equation2 and sensitivity paragraph](../../../joi190122supp1_prod.pdf#page=32), [p.33 continuation](../../../joi190122supp1_prod.pdf#page=33); REPORT [main p.3 Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.8 Table2 footnotea](../../../jama_de_boer_2019_oi_190122.pdf#page=8); REPORT [supplement pp.9–10 eTables4–5](../../../joi190122supp2_prod.pdf#page=9).
- **Printed comparison:** Planned primary Equation2 has treatment, categorical time, treatment×time and participant random intercept; additional baseline terms are conditional sensitivity analyses for imbalance. Report primary models include age,sex and their time interactions, with baselineACR and its time interaction additionally for eGFR. Table2 labels its estimates as derived from this adjusted model.
- **Rule/reproduction:** Compare fixed effects and planned primary versus conditional sensitivity role for the same outcome/contrast/time/random-intercept structure. Fixed age/sex/ACR adjustment is absent from the printed planned primary equation and changes which model is used for the headline contrast; no primary unadjusted counterpart is supplied. Logical specification comparison; rounding does not apply.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Primary adjusted five-year vitaminD/omega effects and CIs in Table2 and abstract.
- **Why context does not resolve it:** RouteA category5 covers a planned primary analysis replaced in reporting; an available conditional sensitivity-adjustment clause does not state that this adjusted model replaces the planned primary model.
- **Supported alternatives/missing definition:** These terms may implement a later planned revision or reflect chosen imbalance sensitivity analyses elevated to primary. No package statement explains that role change or supplies the planned-model result.
- **Human question:** Were the planned Equation2 results produced, and what final plan authorized the reported covariate-adjusted model as the primary analysis?

### F-XS-008 — Planned and reported adherence sensitivity populations use different criteria

- **Locations and roles:** PLAN [p.19 §VIg](../../../joi190122supp1_prod.pdf#page=19), [p.33 §15g](../../../joi190122supp1_prod.pdf#page=33); REPORT [main p.3 Covariates/Data Analysis](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.4 sensitivity narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4); REPORT [supplement p.6 eTable1](../../../joi190122supp2_prod.pdf#page=6), [p.10 eTable5](../../../joi190122supp2_prod.pdf#page=10), [p.13 eTable8](../../../joi190122supp2_prod.pdf#page=13).
- **Printed comparison:** Original plan≥80%; latest plan “continuous adherence to≥80%” study medications. Report defines high adherence≥2/3 of study drug on≥4 of6 questionnaires, yielding1032 for each intervention. Both minimum consumption and continuity criteria change.
- **Rule/reproduction:** Compare item-by-item analysis-set criteria for the adherence sensitivity of the primary eGFR result. Exact2/3=.6667 versus≥.80; allowing80% a half-percentage-unit interval[.795,.805] still leaves minimum gap.12833, relative.80=.1604. Four-of-six reports do not imply continuous qualifying adherence. Conversely continuously taking80% meets the stated thresholds when recorded on all questionnaires. This is not comparison of overall adherence percentages at particular visits.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Primary eGFR adherent-subset effects0.89(−0.74,2.52) and0.42(−1.22,2.06), and denominator1032; parallel ACR sensitivity effects in eTable8 are affected locations of the same criterion pattern.
- **Why context does not resolve it:** A reader can identify the reported criterion, but cannot equate it to the latest planned population or determine the result for that planned subset.
- **Supported alternatives/missing definition:** The change may reflect questionnaire availability or a later adherence rule; this is not stated as an amendment in the supplied plan.
- **Human question:** Which adherence criterion governed the intended sensitivity analysis, and were results for the continuously≥80% subset generated?

### F-XS-009 — Original prespecified outcome hierarchy and composite components were revised before reporting

- **Locations and roles:** PLAN [p.11 aims](../../../joi190122supp1_prod.pdf#page=11), [p.17 §§VIb–c](../../../joi190122supp1_prod.pdf#page=17), [p.19 Table2 hierarchy](../../../joi190122supp1_prod.pdf#page=19), [p.31 amendment dates](../../../joi190122supp1_prod.pdf#page=31), [p.32 §15b](../../../joi190122supp1_prod.pdf#page=32); REPORT [main p.1 primary](../../../jama_de_boer_2019_oi_190122.pdf#page=1), [p.2 Outcomes](../../../jama_de_boer_2019_oi_190122.pdf#page=2), [p.3 secondary definitions](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.9 Table3](../../../jama_de_boer_2019_oi_190122.pdf#page=9).
- **Printed comparison:** Original primary is four-year continuousACR change, with eGFR secondary (Table2 also calls continuous outcomes co-primary). Original composite is ACR progression(doubling plus≥30), absolute eGFR loss≥12, ESRD and/or death. Latest addendum promotes five-year eGFR to primary, makes ACR change secondary and removes ACR progression from the composite while replacing absolute loss with≥40% relative decline. Report follows this revised hierarchy/composite and explicitly states the primary change occurred with the2016 extension.
- **Rule/reproduction:** Compare outcome status and composite component lists across original prespecification and reporting. ACR primary→secondary and eGFR secondary→primary are status changes; albuminuria-progression removal and absolute→relative decline are endpoint-component/threshold changes. These are exact logical differences, not rounding. The amended plan agrees with the report; no contemporaneous conflict between latest plan and report is alleged.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R, P_P.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Which outcome is the originally prespecified primary versus amended primary, and which components define the reported secondary compositeHR0.92 and1.11.
- **Why context does not resolve it:** RouteA category5 expressly includes prespecified outcome-status or composite-definition changes. Disclosure of the amendment is retained as evidence and an alternative interpretation; it does not remove the reproduced change under that route.
- **Supported alternatives/missing definition:** The changes are explicitly supplied as a2015 proposal implemented February24,2016, and the report discloses the extension. They may be fully authorized prospective amendments. Original Table2 “co-primary” versus narrative hierarchy and original4-year versus addendum's prior2-year description indicate intervening plan history is not fully supplied; those superseded historical differences are not separate findings.
- **Human question:** Which outcome hierarchy and component list should be tagged as original versus amended prespecification, and how should the documented2016 revision be adjudicated for evidence reuse?

### F-XS-010 — Standalone categorical ACR doubling is described as prespecified but absent from the latest supplied secondary analyses

- **Locations and roles:** PLAN [p.17 original composite](../../../joi190122supp1_prod.pdf#page=17), [p.32 §15b/e](../../../joi190122supp1_prod.pdf#page=32), [p.33 secondary categorical models](../../../joi190122supp1_prod.pdf#page=33); REPORT [main p.3 Outcomes](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.4 secondary narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4), [p.9 Table3/footnotea](../../../jama_de_boer_2019_oi_190122.pdf#page=9).
- **Printed comparison:** Report calls ACR change prespecified both continuously and as time to doubling with finalACR≥30. Latest plan lists ACR change baseline→years2/5 and specifies a log-continuous LMM; categorical secondary outcomes are≥40% eGFR loss and eGFR-loss/ESRD/death composite. The original plan's ACR doubling is a component of a different four-year composite, not a standalone ACR time-to-event secondary analysis.
- **Rule/reproduction:** Match outcome status and analysis definition, not just the words ACR or doubling. A component of an original composite is not the same prespecified analysis as standalone Cox time to doubling in the amended five-year design. No standalone analysis is specified in the supplied original or amended plan.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Prespecified status attached to ACR-doubling HR1.34(1.00,1.80),P=.05 and1.08(.81,1.44),P=.60 in Table3.
- **Why context does not resolve it:** RouteA category5 covers an analysis described as prespecified but absent from the supplied plan; reusing an original composite component does not establish prespecification of the newly reported analysis.
- **Supported alternatives/missing definition:** Another final plan may specify standalone ACR time-to-event analysis, or the authors may intend an expanded analysis of the original component. That prespecification document/definition is not supplied.
- **Human question:** Where was standalone time to ACR doubling with finalACR≥30 prespecified, and how was it classified relative to the revised continuous ACR outcome?

### F-XS-011 — Planned bioavailable25(OH)D subgroup analysis is absent from the reported primary-outcome subgroup results

- **Locations and roles:** PLAN [p.33 §15f](../../../joi190122supp1_prod.pdf#page=33); REPORT [main p.3 subgroup list](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.8 Figure3](../../../jama_de_boer_2019_oi_190122.pdf#page=8), [pp.9–10 interpretation](../../../jama_de_boer_2019_oi_190122.pdf#page=9); REPORT [supplement p.18 eFigure2](../../../joi190122supp2_prod.pdf#page=18). All other REPORT pages were checked for a corresponding analysis; the occurrence in main p.10 author disclosures names a patent, not a subgroup result.
- **Printed comparison:** Latest plan prespecifies baseline “total and bioavailable serum25(OH)D concentrations” for vitaminD subgroup analyses in the primary eGFR LMM. Report lists baseline25(OH)D, race/ethnicity,ACR,eGFR plus addedBMI; Figure3 shows one25(OH)D partition(<20,20–<30,≥30ng/mL), corresponding to total concentration. No bioavailable subgroup result or omission statement appears in the supplied REPORT documents.
- **Rule/reproduction:** Compare each planned subgroup dimension with the complete reported subgroup inventory. Total and bioavailable are explicitly separate measures in the plan; reporting the total partition does not supply the planned bioavailable analysis. This is an omitted prespecified analysis of the primary outcome, not a generic missing methods detail.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Prespecified treatment-effect heterogeneity of the primary eGFR result by bioavailable25(OH)D; the report states no significant heterogeneity for the displayed subgroups.
- **Why context does not resolve it:** RouteA category5 covers a planned primary-outcome analysis not reported; the ordinary total25(OH)D partition cannot identify its bioavailable counterpart.
- **Supported alternatives/missing definition:** Bioavailable assays or analysis may have been unavailable, discontinued or reported elsewhere. None is documented in this package.
- **Human question:** Was the prespecified bioavailable25(OH)D subgroup analysis performed, and where are its result or documented removal from the plan?

### F-XS-012 — Supplied protocol names a different eGFR estimating equation from the reported primary outcome

- **Locations and roles:** PLAN [p.17 Equation1](../../../joi190122supp1_prod.pdf#page=17), [p.32 amended eGFR primary](../../../joi190122supp1_prod.pdf#page=32); REPORT [main p.3 Outcomes](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.11 reference19](../../../jama_de_boer_2019_oi_190122.pdf#page=11); REPORT [supplement pp.2–4 QC](../../../joi190122supp2_prod.pdf#page=2) corroborates harmonization, rather than specifying the original equation.
- **Printed comparison:** Original plan specifically defines eGFR as177.6×SCr^(−.65)×CysC^(−.57)×age^(−.20)×.82(if female)×1.11(if black). Report says CKD-EPI creatinine/cystatinC equation and cites its2012 publication. The2010 protocol gives its own different explicit equation; the addendum promotes eGFR but does not specify a replacement equation.
- **Rule/reproduction:** Match the measure-construction specification, not merely the shared creatinine/cystatinC inputs. The explicit2010 equation and the named2012 equation are distinct supplied identities. No external equation coefficients are imported and no recalculated eGFR discrepancy is asserted; the finding is the planned-versus-reported estimator identity.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Construction of the primary eGFR change and≥40% eGFR decline endpoints.
- **Why context does not resolve it:** The report clearly identifies its estimator, but the latest supplied addendum does not explain whether the originally explicit estimator was replaced for the newly primary endpoint. Laboratory calibration changes explain cystatinC harmonization, not this equation identity change.
- **Supported alternatives/missing definition:** The plan's “most precise serologic methods available” rationale may have been intended to permit updates, or an intervening amendment may specify CKD-EPI. Neither supplies an explicit final estimator rule here.
- **Human question:** Which final plan specified CKD-EPI rather than the original printed equation, and which equation generated all baseline/follow-up outcome values?

### F-XS-013 — Allocation stratification specification differs between plan and report

- **Locations and roles:** PLAN [p.14 §IVc](../../../joi190122supp1_prod.pdf#page=14); REPORT [main p.2 Interventions](../../../jama_de_boer_2019_oi_190122.pdf#page=2). PLAN [pp.31–33 addendum](../../../joi190122supp1_prod.pdf#page=31) contains no randomization revision.
- **Printed comparison:** Plan computer randomization is stratified by5-year age group, with blocks of8 and two participants in each factorial combination. Report states blocks of8 stratified by age,sex and race.
- **Rule/reproduction:** Item-by-item randomization specification: age matches, block8 matches and factorial assignment matches; sex and race are additional stratifiers in the reported design. This is an explicit design difference, without inferring omitted sex/race adjustment or recommending another analysis.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Randomization design attached to the1312-person primary treatment comparison and its statistical-analysis design record.
- **Why context does not resolve it:** The two printed allocation specifications do not establish whether sex/race strata were introduced after the2010 protocol. A reader extracting planned/report design cannot infer the final strata from the supplied addendum.
- **Supported alternatives/missing definition:** Later parent-trial allocation procedures may have added sex/race strata; the ancillary report may summarize that final scheme. No supplied plan records those strata.
- **Human question:** Which allocation strata were implemented for this cohort, and which prospective specification added sex/race?

### F-XS-014 — Latest plan's interaction model omits the common time effect present in its primary model

- **Locations and roles:** PLAN [p.32 §15d Equation1 and §15e Equation2](../../../joi190122supp1_prod.pdf#page=32); REPORT [main p.3 time model](../../../jama_de_boer_2019_oi_190122.pdf#page=3), [p.4 interactionP=.42](../../../jama_de_boer_2019_oi_190122.pdf#page=4) identify the analysis relying on the plan, but are corroborating locations for the plan-internal comparison.
- **Printed comparison:** Interaction Equation1 has intercept,D,omega,D×omega,D×time,omega×time,D×omega×time,participant random intercept and residual; no time main effect. Primary Equation2 includes time main effect together with treatment and treatment×time. Both use times0,2,5; Equation1 tests the three-way coefficient to decide marginal versus four-group comparisons.
- **Rule/reproduction:** Set both treatment indicators to0. Equation1's fixed mean becomes the constant intercept at every time; Equation2 allows a common time effect. Thus the printed interaction model imposes no fixed secular change in double-placebo, while the planned primary model allows it. Random intercepts do not provide a shared fixed time trajectory. This is an explicit equation difference, not a preference for covariate adjustment or an inferred unstated method.
- **Focus area:** C,D. **Proposed review domain:** plan_material. **Relationship type:** P_P. **All relationships:** P_P.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Planned interaction test and theP=.42 used to retain marginal factorial primary contrasts.
- **Why context does not resolve it:** The source does not say a common time effect is implicit in Equation1. That missing term changes the model under which the interaction decision is tested; the primary equation alone cannot establish what was implemented.
- **Supported alternatives/missing definition:** A common time main effect may have been present in implemented software but omitted from the printed equation, or the written restriction may have been intentional. No code is supplied.
- **Human question:** Did the fitted treatment-interaction model include categorical time main effects, and what exact model generated the interactionP=.42?

### F-XS-015 — Plan assigns two microgram quantities to the same printed vitaminD IU dose

- **Locations and roles:** PLAN [p.15 §Ve1 study dose](../../../joi190122supp1_prod.pdf#page=15), [p.21 §VIIa dose and upper limit](../../../joi190122supp1_prod.pdf#page=21). REPORT [main p.2 2000IU regimen](../../../jama_de_boer_2019_oi_190122.pdf#page=2) corroborates only the IU dose; it supplies no conflicting microgram dose and is not a P_R relationship.
- **Printed comparison:** Plan p.15 and p.21 describe the study dose as2000IU(40µg). The same p.21 says the tolerable upper intake level is50µg “or2000IU,” and describes the selected dose as lower than that limit.
- **Rule/reproduction:** Match the same substance and quantity unit:2000IU is paired once with40µg and once with50µg in the same prospective intervention specification. Without importing any external conversion, the two supplied equivalences cannot both assign the same IU quantity its corresponding microgram quantity. Printed intervals[39.5,40.5] and[49.5,50.5] have gap9, relative to40=.225, above.05. Allowing the shared2000IU copy its half-unit interval cannot bridge a25% nominal conversion difference. The dose-versus-limit “lower” statement is retained as context, without a separate finding based on rounded equal2000IU values.
- **Focus area:** D. **Proposed review domain:** plan_material. **Relationship type:** P_P. **All relationships:** P_P.
- **Qualifying route:** Route A, category 2.
- **Affected result or extracted value:** Microgram quantity extracted for the randomized vitaminD dose and its planned limit comparison.
- **Why context does not resolve it:** RouteA category2 covers a substituted printed dose number changing magnitude beyond display precision. Consistent reporting of2000IU does not identify which printed microgram conversion belongs to that dose.
- **Supported alternatives/missing definition:** The40µg dose or the50µg/2000IU limit pairing may need a different numeric value. The package supports no independent choice of a final conversion and this review proposes none.
- **Human question:** Which microgram quantity corresponds to the planned2000IU study dose, and which numeric pair defines the stated upper intake limit?

## Excluded observations

Only apparent issues that were not emitted are listed; reconciled checks above are not exclusions. Each row has exactly one scope reason code.

| Location | Observation | Reason code |
|---|---|---|
| REPORT [main p.7 Figure2](../../../jama_de_boer_2019_oi_190122.pdf#page=7) versus [p.8 Table2](../../../jama_de_boer_2019_oi_190122.pdf#page=8) and [supplement p.11](../../../joi190122supp2_prod.pdf#page=11) | Omega panel participant rows repeat vitaminD contributor counts. These are contributors at individual time points; no change of the full analytic population or primary effect attribution is established by the contributor rows alone. | PERIPHERAL_COMPARISON |
| REPORT [main p.4 medication narrative](../../../jama_de_boer_2019_oi_190122.pdf#page=4) versus [supplement p.7 eTable2](../../../joi190122supp2_prod.pdf#page=7) | Insulin use is described as relatively stable despite20%baseline versus16%year5. This qualitative description does not change a primary/key secondary result or leave a printed medication percentage unidentified. | TERMINOLOGY_OR_WORDING |
| PLAN [p.16 EPA:DHA40:30](../../../joi190122supp1_prod.pdf#page=16) versus REPORT [main p.2 EPA465/DHA375](../../../jama_de_boer_2019_oi_190122.pdf#page=2) | Planned ratio interval[39.5/30.5,40.5/29.5]=[1.2951,1.3729]; reported ratio interval[464.5/375.5,465.5/374.5]=[1.2370,1.2430]. Gap.0521 divided by reference40/30 is.0391, at most.05. Total840mg also agrees. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN [p.33 follow-up1058/80%](../../../joi190122supp1_prod.pdf#page=33) versus REPORT [main p.3 target1320](../../../jama_de_boer_2019_oi_190122.pdf#page=3) | Nominal .80×1320=1056 versus1058. Rounded80% interval with1320 half-unit gives[1049.0025,1063.0025], overlapping printed1058. No target/assumption discrepancy survives display precision. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT [main p.3 secondary “exploratory” interpretation](../../../jama_de_boer_2019_oi_190122.pdf#page=3) versus PLAN [p.32 secondary status](../../../joi190122supp1_prod.pdf#page=32) | Interpretation as exploratory due multiplicity does not relabel the explicitly prespecified secondary outcomes as post-hoc outcomes. This is inferential caution wording, not a reproduced change of outcome status. | TERMINOLOGY_OR_WORDING |
| PLAN [p.14 “diabetes of hypertension”](../../../joi190122supp1_prod.pdf#page=14) | Malformed connecting word in a screening sentence; no cohort count or reported hypertensive-CKD inclusion is supplied to establish a changed analysis population. The symbol/word ambiguity alone does not qualify. | TERMINOLOGY_OR_WORDING |
| PLAN [p.12 baseline samples required](../../../joi190122supp1_prod.pdf#page=12) versus REPORT [main pp.2–3 agreement to provide/baseline missing](../../../jama_de_boer_2019_oi_190122.pdf#page=2) | Four missing baseline eGFR measurements do not establish that required samples were never returned rather than unavailable for assays; no claim of enrolling participants who refused samples is printed. | CONDITIONAL_OR_UNREPORTED |
| PLAN [p.19 adherence/biomarker LMM predecessor](../../../joi190122supp1_prod.pdf#page=19), [p.33 LMM biomarker replacement](../../../joi190122supp1_prod.pdf#page=33) versus REPORT [supplement p.17 correlations](../../../joi190122supp2_prod.pdf#page=17) | Two plotted correlations r=−.05/−.02 alone do not identify their underlying adjustment or establish a specific replacement model. This reviewer does not infer unreported regression details from r; the primary/secondary exploratory distinction needs source-grounded statistical follow-up. | CONDITIONAL_OR_UNREPORTED |
| PLAN [p.17 “secondary dichotomous ... continuous”](../../../joi190122supp1_prod.pdf#page=17) | The displayed eGFR subtraction, no-transformation rationale and analysis equation identify the continuous quantity immediately. No printed number changes. | TERMINOLOGY_OR_WORDING |
| REPORT [supplement pp.18–19 captions “difference”](../../../joi190122supp2_prod.pdf#page=18) | Captions use generic difference while table/forest headers explicitly state ratioactive/placebo with null1. The quantitative measure is apparent from immediate headers; this wording is separate from F-XS-002's reversed favor direction. | TERMINOLOGY_OR_WORDING |
| PLAN [p.23 parent interim rule](../../../joi190122supp1_prod.pdf#page=23) versus REPORT [main p.3 final alpha](../../../jama_de_boer_2019_oi_190122.pdf#page=3) | No ancillary interim statistic or stopping decision is reported. Inferring a conflict from absent ancillary monitoring details would depend on treating the parent cancer/CVD monitoring plan as an ancillary outcome decision. | CONDITIONAL_OR_UNREPORTED |

## Completion

Fifteen findings emitted; eleven apparent observations excluded. Exact source scope64/64pages and every mapped statistical/numeric group covered. No scientific coverage gaps, unavailable source units, tooling limitations or unresolved asset-to-source identity gaps. Supplied aggregate evidence does not quantify participant-level effects of eligibility/analysis-set revisions; forest numerical CI endpoints and implemented model code are not supplied. These content limits are retained in human questions rather than used to omit an assigned comparison. Sources and reused evidence assets remain unchanged.
