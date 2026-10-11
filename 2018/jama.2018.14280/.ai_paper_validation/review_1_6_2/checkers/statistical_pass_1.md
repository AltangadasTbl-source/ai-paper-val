# Statistical pass 1 — main-report and plan shard

Runtime agent: /root/statistics_pass1_main; fresh gpt-6.1-sol/high; pass 1 only. Controls QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. Exact assigned scope: main report DOC-001 all inferential tuples/methods, including abstract, Table 2, Figure 2 and captions; primary distribution eFigure 1 at DOC-004 p10; all prospective statistical-method/design relationships in DOC-002 and DOC-003. The other fresh statistical shards own all eTable 1–5 inferential tuples and eFigure 2–4 comparisons. References to supplementary result coverage below test planned versus reported analyses; they do not duplicate the support-tuple pass.

110 stable relationships S001–S110 were reviewed and receive PASS_1_COMPLETE in statistics/parts/main_plan_inventory.md. This shard emits three findings and ten excluded observations. There is no scientific coverage gap. No severity, validity, adjudication, or correction is assigned.

## Checks and constraints

The check covers each printed inferential tuple's estimate containment, endpoint order, direction, confidence/significance concordance, matching report copies, and source-stated test/model. All main-report CI/null/P decisions reconcile: no estimate is outside its CI, no CI endpoints are reversed, and no CI-versus-P significance conflict is observed. No test statistic or standard error is supplied. Primary t-test reproduction uses source means/SD/n only as a rounded-input diagnostic: SE≈.744, approximate P≈.717, approximate95%CI [−1.73,1.19], compatible with the reported -.27[−1.74,1.19], P=.71 under input rounding. It does not invent equal-variance assumptions or exact degrees of freedom. Other CI inversion diagnostics do not establish unstated models or variance estimators. Table 2 RR estimand/producing-method identity is independently handled by the numeric checker; the statistical checks here do not treat an undisclosed model as crude.

The supplied methods state two-sided .05 and95% CIs, unadjusted multiplicity, superiority, complete cases if primary missing≤1%, and no efficacy interim analysis. Six primary outcomes are missing among961 enrolled (.624%), consistent with the complete-case rule. All four Figure 2 Schoenfeld residual P values (.68,.13,.21,.82) exceed .05. No noninferiority/equivalence margin or numeric efficacy stopping boundary is stated. Sample-size normal approximation392.44/arm is explicitly a diagnostic; the stated two-group t-test397/arm and stated20% increase to476 reconcile within the display-precision rule. No preferred analysis is proposed.

Evidence: fresh source-linked mapper records, source-matched reusable text, direct Poppler pdftotext25.03.0 stdout at DOC-001 pp4,6–7; DOC-002 pp10,19,33–35; DOC-003 pp12–15,21–22; and visual inspection of source-matched DOC-004 p10 image. No new derivative was created, no supplied/reused asset modified, and no web or old scientific review conclusion read. Source roles are assigned by content: main article/results supplement REPORT; protocol/SAP/change matrix PLAN, including its 'in the paper' descriptive column.

## Findings

### F-ST1-001

**Observation:** Five prespecified analysis families involving a primary endpoint are not reported in the supplied report materials.

**Relationships:** S074, S083, S085, S087, S097, S098. **Focus area:** D, planned versus reported statistical design. **Proposed review domain:** protocol_report. **Proposed primary relationship type:** P_R. **All relationships:** P_R. **Qualifying route:** Route A, category 5.

**Exact locations and document roles:**

- PLAN [DOC-002 p33, Primary and secondary analyses](../../../joi180108supp1_prod.pdf#page=33) promises per-protocol analysis; PLAN [DOC-003 p13](../../../joi180108supp2_prod.pdf#page=13) and [p14](../../../joi180108supp2_prod.pdf#page=14) define exclusions for primary-outcome per-protocol analysis. PLAN [DOC-003 p22, Per protocol analyses row](../../../joi180108supp2_prod.pdf#page=22) says updated SAP 'Described according to protocol violations' and in the paper 'Not described'.
- PLAN [DOC-003 pp14–15, Other exploratory analyses](../../../joi180108supp2_prod.pdf#page=14) specifies a zero-inflated generalized linear sensitivity model of the primary VFD outcome adjusting for age, LIPS, SAPS II score and PaO2/FiO2; covariates continue on [p15](../../../joi180108supp2_prod.pdf#page=15). PLAN [DOC-003 p21, Additional analyses row](../../../joi180108supp2_prod.pdf#page=21) lists both covariate-adjusted GLM and stratification-random-effects GLMM in the updated SAP; its post-hoc column states 'Not reporting the GLM with adjustment for covariates'. REPORT [DOC-001 p4, Statistical Analysis](../../../jama_simonis_2018_oi_180108.pdf#page=4) describes only the random-effects sensitivity analysis, with its result P=.72 in REPORT [DOC-001 p6, Outcomes](../../../jama_simonis_2018_oi_180108.pdf#page=6).
- PLAN [DOC-003 p14, Subgroup analyses item9](../../../joi180108supp2_prod.pdf#page=14) specifies high versus low respiratory rate based on the median of the first2 days, applied to VFD28. PLAN [DOC-003 p22, continuation of Subgroup analyses row](../../../joi180108supp2_prod.pdf#page=22) lists respiratory rate in both updated-SAP and in-paper columns. REPORT [DOC-001 p4, prespecified subgroup list](../../../jama_simonis_2018_oi_180108.pdf#page=4) lists eight categories without respiratory rate; REPORT [DOC-004 p9, complete eTable5](../../../joi180108supp3_prod.pdf#page=9) contains eight subgroup pairs and no respiratory-rate row.
- PLAN [DOC-003 p15, mediation paragraph](../../../joi180108supp2_prod.pdf#page=15) states a mechanical-power mediation analysis of randomized treatment effects on VFD will be performed; PLAN [DOC-003 p22, Other row](../../../joi180108supp2_prod.pdf#page=22) shows updated 'Mediation analyses' and in-paper 'None'. No mechanical-power mediation result is supplied in REPORT DOC-001 pp4–8 or DOC-004 pp5–13.
- PLAN [DOC-002 p11](../../../joi180108supp1_prod.pdf#page=11) and [p34, Cost-effectiveness endpoints](../../../joi180108supp1_prod.pdf#page=34) explicitly designate incremental cost per ICU day avoided as the primary cost-effectiveness measure; p34 additionally calls cost-data collection/analysis fully integrated into the study and defines ICER as between-arm cost difference divided by effect difference. REPORT [DOC-001 p4, Other Study Parameters](../../../jama_simonis_2018_oi_180108.pdf#page=4) states health care cost information was collected but its analysis is not reported in this article. The supplied results supplement contains no cost-effectiveness result.

**Printed statements and logical rule:** The prospective specification promises the five families above. Supplied reporting contains the primary t-test estimate -.27[−1.74,1.19], P=.71, one random-effects sensitivity P=.72 and eight subgroup categories, but lacks the promised per-protocol, covariate-adjusted sensitivity, ninth subgroup, mediation, and primary economic result. The modification matrix expressly documents nonreporting for three families and lists respiratory rate as in-paper despite no corresponding supplied row. This is a source-grounded coverage comparison, not a claim that an unreported analysis had a particular numerical result. No arithmetic display-precision test applies to presence/absence of specified analyses.

**Affected result or extracted value:** Alternative planned estimates of the primary VFD28 treatment effect, its respiratory-rate effect modification and mechanical-power mediation, and the expressly primary incremental cost per ICU day avoided. Their absence prevents extraction or comparison with the available unadjusted VFD estimate and random-effects sensitivity result.

**Why context does not resolve it:** Route A category5 requires recording a planned primary-outcome analysis that is not reported. The change matrix and cost paragraph disclose portions of the omission, but supply neither the missing results nor a source location containing them. Disclosure is retained as an alternative explanation and does not replace a promised result.

**Source-grounded alternatives and missing definitions:** The covariate sensitivity, per-protocol and mediation analyses may have been deliberately omitted, as the matrix describes. The respiratory-rate analysis may have been included in the matrix from an intended version yet absent from final reporting. Economic results may have been reserved for a separate report, but none is supplied. The supplied documents do not establish whether each omitted analysis was performed, abandoned, or reported elsewhere. The economic endpoint is a separate expressly primary cost-effectiveness endpoint; it is not relabeled as the clinical primary endpoint.

**Exact human question:** Which source-linked results, if any, correspond to the promised per-protocol VFD comparison, covariate-adjusted primary sensitivity analysis, high/low respiratory-rate VFD subgroup analysis, mechanical-power mediation analysis and primary incremental-cost-per-ICU-day-avoided analysis, and what documented analysis-plan decision accounts for each result absent from the supplied report?

### F-ST1-002

**Observation:** The primary VFD28 endpoint's time origin changes from ICU admission in the protocol to randomization in the report; the final SAP's day1–28 wording does not explicitly resolve the origin.

**Relationships:** S042, S056. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary relationship type:** P_R. **All relationships:** P_R. **Qualifying route:** Route A, category 5.

**Exact locations and document roles:** PLAN [DOC-002 p10, Study endpoints](../../../joi180108supp1_prod.pdf#page=10) names VFD and alive at day28 'after ICU admission'; PLAN [DOC-002 p19, Sample size](../../../joi180108supp1_prod.pdf#page=19) specifies detecting one VFD and alive at day28 'after ICU admission'; PLAN [DOC-002 p33, Primary study parameters](../../../joi180108supp1_prod.pdf#page=33) again gives day28 after ICU admission. PLAN [DOC-003 p8, Outcomes](../../../joi180108supp2_prod.pdf#page=8) defines days1–28 alive and breathing without invasive assistance, without explicitly stating which event starts day1. REPORT [DOC-001 p4, Outcomes](../../../jama_simonis_2018_oi_180108.pdf#page=4) states the primary number of days alive/free from invasive ventilation is 'calculated from the moment of randomization'. REPORT [DOC-001 p5, Intervention](../../../jama_simonis_2018_oi_180108.pdf#page=5) reports median interval from ICU ventilation initiation to randomization .57hours(IQR.23–1.00).

**Printed statements, rule and calculation:** The source definitions set the end at ICU-admission time+28days versus randomization time+28days. If admission time is t_ICU and randomization t_R, their start and end anchors differ by t_R−t_ICU; the exact person-specific offsets and endpoint recoding are not supplied. The .57-hour reported ventilation-to-randomization interval is not substituted for admission-to-randomization. The comparison concerns the primary composite's counting window, not a rounding difference in a printed estimate.

**Affected result or extracted value:** VFD28 mean difference−.27[−1.74,1.19] and the outcome definition used to extract or pool it with other VFD endpoints.

**Why context does not resolve it:** This is the primary composite's window definition under Route A category5. Randomization soon after ICU ventilation does not establish identical admission and randomization times for all patients or identify a documented endpoint-anchor amendment. The primary-analysis change matrix documents Cox-to-t-test conversion but does not expressly describe the time-origin conversion.

**Source-grounded alternatives and missing definitions:** The final SAP may intend randomization as day1 and thereby amend the earlier origin; alternatively ICU-admission wording may be shorthand for an almost coincident event. The report supplies an explicit randomization anchor. The missing definition is which start event governs the final prospectively defined VFD28 outcome and whether endpoint values were recomputed to that anchor.

**Exact human question:** Was the final VFD28 endpoint counted from ICU admission or from randomization, and where does the supplied plan document the final time-origin definition or its amendment?

### F-ST1-003

**Observation:** The updated SAP's primary-outcome subgroup interaction model is zero-inflated, while the reported model is Gaussian; the change matrix expressly places this replacement among post-hoc modifications.

**Relationships:** S084, S109. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary relationship type:** P_R. **All relationships:** P_R. **Qualifying route:** Route A, category 5.

**Exact locations and document roles:** PLAN [DOC-003 p14, Subgroup analyses](../../../joi180108supp2_prod.pdf#page=14) specifies subgroup-by-treatment interactions in generalized linear models considering zero-inflated distributions, applied to VFD28. PLAN [DOC-003 p22, Statistical approach for subgroup analyses row](../../../joi180108supp2_prod.pdf#page=22) repeats that model in the updated-SAP column, lists Gaussian distributions in the in-paper column, and states in the post-hoc column 'Change the zero-inflated distribution to Gaussian distribution (according to the CLT)'. The matrix footnote defines post-hoc modifications as not considered in either original plan or updated SAP. REPORT [DOC-001 p4, Statistical Analysis](../../../jama_simonis_2018_oi_180108.pdf#page=4) describes prespecified exploratory subgroup categories and Gaussian GLM interactions. REPORT [DOC-001 p6, Subgroups and Exploratory Analyses](../../../jama_simonis_2018_oi_180108.pdf#page=6) gives the location-of-intubation interaction P=.01 with inside-ICU MD−2.50[−4.63,−.36] and outside-ICU MD1.45[−.52,3.43]. REPORT [DOC-004 p9 eTable5](../../../joi180108supp3_prod.pdf#page=9) gives the additional subgroup effects/interaction tests, whose individual tuples are checked by another statistical shard.

**Printed statements and logical rule:** The last supplied prospective model specification calls for zero-inflated subgroup GLMs. The reported producing model is Gaussian, and the matrix identifies its change as post-hoc. They are different specified statistical models for the primary-outcome subgroup analysis; no computation from raw data is needed to reproduce that planned-versus-reported relationship. No claim is made that either coherent model choice is unsuitable, nor that the printed subgroup estimates or P=.01 would change numerically under the planned model.

**Affected result or extracted value:** Interpretation of the prespecification of the VFD28 subgroup-interaction estimates, particularly the location-of-intubation P=.01 and its treatment-effect differences, plus the eTable5 primary-outcome subgroup results.

**Why context does not resolve it:** Route A category5 covers replacement/nonreporting of a planned primary-outcome analysis. The CLT explanation discloses the reason for using a different model, but does not make the reported producing model the one in the updated SAP. The distinction between prespecified subgroup definitions and post-hoc model replacement must remain available for extraction.

**Source-grounded alternatives and missing definitions:** The subgroup definitions were prespecified, while the Gaussian producing model was selected subsequently, as the matrix states. A further pre-analysis amendment may exist but is not supplied. Gaussian interaction analysis is an internally coherent stated choice; this finding concerns its relationship to the supplied updated plan and does not recommend a replacement method. No zero-inflated-model subgroup estimates are supplied for comparison.

**Exact human question:** Should the reported primary-outcome subgroup estimates and interaction P values be described as results from prespecified subgroup definitions analyzed with a post-hoc Gaussian model, and is there a supplied prospective amendment or a reported zero-inflated-model analysis that establishes a different mapping?

## Excluded observations

Only apparent issues actually considered and not emitted appear here; reconciled checks are in the S inventory. Each row has one reason code. No route-A interval/test, numerical-slip, same-display count, reproducing-method or planned-primary-analysis observation is excluded merely by disclosure or missing model detail.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p6 subgroup narrative; REPORT DOC-004 p9 eTable5 | The main narrative calls −4.63 to−.36 and−.52 to3.43 'IQR', while identical effect-estimate ranges are labeled95%CI in the matching subgroup display. The effect estimate/range mapping is immediately identifiable; no printed numeric value changes. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002/DOC-003 intervention sections; REPORT DOC-001 p2 | Comparison arm called high in the plans and intermediate in the report; actual10mL/kg start,8–10target and25cmH2O limit establish the same comparison strategy. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-003 p14 Other exploratory analyses | 'Pre-specified post-hoc exploratory analyses' combines prospective and retrospective terms; the source explicitly enumerates the analysis specifications. Their actual reported/omitted status is recorded in F-ST1-001/F-ST1-003 rather than treating this phrase as an independent finding. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001 p7 Figure2B caption | 'Minimum value observed is0.60' appears where a median survival observation time was not computed. In the survival-curve context it can refer to the curve remaining near.60 and never crossing.50; no exact time value is printed in conflict. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-003 pp10–11; REPORT DOC-001 p2 | SAP reports statistician safety analyses while main says no interim analyses. The main separately describes a committee blind to the primary endpoint, so safety monitoring and efficacy interim analyses are distinct in immediate context. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002 p31; PLAN DOC-003 p10 | Protocol DSMB six-monthly schedule versus SAP reports after first150patients and the following year; no numeric efficacy boundary, primary decision rule or result is changed by this calendar comparison. | PERIPHERAL_COMPARISON |
| PLAN DOC-003 p12; REPORT DOC-001 pp4–5; REPORT DOC-004 pp5–7 | Seven-day longitudinal modeling planned but only three-day respiratory tables printed. The report does not state its fitted model time window, so absent days4–7 display alone does not establish that a different window produced the reported model comparison. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p4 VFD definition; REPORT DOC-004 p10 eFigure1; REPORT DOC-001 p6 mortality | A visual comparison of the zero-VFD CDF jump with day28 death percentages would require assigning zero VFD to every patient dying before28. The supplied definition does not explicitly state that rule; no exact curve coordinates are printed. No death-zero convention or exact CDF numerator is invented. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp10,15,27–30; REPORT DOC-001 p4 | ICU weakness/EAdi/VOC unreliable and not reported, and some other non-key secondary measures lack numerical rows. No source changes their outcome status or supplies a conflicting result; none is designated key secondary in the abstract. The expressly primary economic omission is retained in F-ST1-001. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 p19; REPORT DOC-001 p4 sample size | Explicit20% increase397→476 differs from dividing by.8 to retain397 after20%dropout. Allowing397 its[396.5,397.5] interval and20% its[19.5%,20.5%] interval, alternative retention gives[396.5/.805,397.5/.795]=[492.5466,500.0000]; printed476 allows[475.5,476.5], gap16.0466 and relative gap16.0466/476=.03371≤.05. The source's explicit multiplication reproduces476.4. | ROUNDING_OR_DISPLAY_PRECISION |

## Limitations and handoff

No assigned source unit or relationship remains unreviewed. Missing numerical inputs are precisely named in the S records: event/censor data, survivor/subgroup sample sizes, test statistics/standard errors, t-test variant and degrees of freedom, inverse-Gaussian link/variance estimator, exact binary generating model, longitudinal fitted time window and numerical curve coordinates. They do not authorize assumptions from convention. The mechanical evidence rechecker must independently inspect every included finding's exact supplied PDF location. This shard's links resolve from its assigned parts directory; the coordinator must shorten ../../../ to ../../../ when merging into the canonical checkers/statistical_pass_1.md.
# Statistical pass 1 — support shard A

- Runtime task ID: /root/statistics_pass1_support_a
- Model and effort: gpt-6.1-sol / high; fresh pass-1 statistical shard
- Scope: REPORT DOC-004 joi180108supp3_prod.pdf, eTable 1 p5 all 48 variable–occasion tuples; eTable 2 p6 all 72 variable–mode–occasion tuples; matched eFigures 2–4 pp11–13 within nine existing tuples.
- Relationship inventory: statistics/parts/support_a_inventory.md, stable S201–S320 in source-row order; all 120 explicitly PASS_1_COMPLETE.
- Findings: 1; excluded observations: 1 consolidated row; scientific coverage gaps: 0.
- Source roles: DOC-004 REPORT by methods/results content. Main REPORT and SAP PLAN are used solely to establish context; they do not create additional assigned relationships here.

The full normative QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read before checking. Every assigned tuple was checked for median/IQR containment and endpoint order, units and effect-measure identity, printed P and applicable stated statistical rules, matched figure direction and attribution, and analysis logic. The IQRs are not treated as confidence intervals for between-group estimates. No contrast confidence intervals, standard errors or test statistics appear in these tuples. No superiority, noninferiority, equivalence, interim, stopping or sample-size decision occurs in the assigned displays.

The main article specifies two-sided P values and .05 significance without multiplicity adjustment. It describes a repeated-measures mixed model for longitudinal tidal volumes, not an explicit model/test mapping for each separate mode/day table or cumulative-distribution panel. Continuous P values cannot be reproduced solely from medians/IQRs without that mapping and observations; this absence supplies no independent contradiction. Eight binary comparisons were assessed against printed n/N and percent values and a labelled uncorrected Pearson χ² diagnostic; all reconcile under display precision. The ABG footnote supplies the binary denominators, so headers are not substituted. All nine figure comparisons match table mode, day, contrast, direction and printed P (including .027 versus .03 after precision). These reconciling checks are recorded in the inventory, not as excluded observations.

## Findings

### F-ST1-201

**Observation:** The intermediate-arm PEEP median and interquartile-range entry after titration in the other-ventilation-mode section does not satisfy quartile ordering or contain its median.

**Exact locations and roles:** REPORT [DOC-004 eTable 2, physical p6](../../../joi180108supp3_prod.pdf#page=6), “Other Mode of Ventilation,” “After titration on day of randomization,” PEEP, cmH2O, intermediate tidal volume cell; REPORT footer on the same page defining the summaries as “median (interquartile range).” The table is a retrospective results display, not PLAN material. A direct source rendering confirms the printed reading (preprocessing/st1-a-source-p6.png; Poppler pdftoppm 25.03.0, CPU). Reusable layout text and the reusable image independently show the same digits.

**Printed values:** Intermediate PEEP is **8 (5–1)** cmH2O; low PEEP is **5 (5–10)** cmH2O; comparison **P=0.50**. Contributor headers are 33 low and 28 intermediate patients. No effect confidence interval is printed. This finding concerns the intermediate median/IQR, not the P value.

**Rule and calculation:** Any median (interquartile range) must satisfy Q1 ≤ median ≤ Q3, with Q1 ≤ Q3. The printed reading gives Q1=5, median=8 and Q3=1, so 5>1 and 8>1. Permitting integer display half-units gives Q1∈[4.5,5.5], median∈[7.5,8.5], Q3∈[0.5,1.5]. Thus even the largest displayed upper-quartile allowance, 1.5, is below the smallest allowed median, 7.5, by **6 cmH2O**, and below the smallest allowed lower quartile by **3 cmH2O**. Reordering the two endpoints to [1,5] would still leave its largest possible endpoint 5.5 below the smallest possible median 7.5 by 2 cmH2O.

**Recomputed interval and relative gap:** Given the printed median alone, the admissible upper-quartile interval is [7.5,∞) cmH2O; the printed upper-quartile half-unit interval is [0.5,1.5]. The minimum gap is 6 cmH2O and relative discrepancy against the printed upper quartile 1 is 6/1=**6.00**. The exact intended Q3 is not reconstructable from the supplied summaries. For the primary containment rule below, Route A category 1 is not screened by display precision; the half-unit calculation also demonstrates that this is not a precision reconciliation.

**Focus area:** B, estimate and interval logic.

**Proposed review domain:** statistical_results.

**Proposed relationship type:** S_W. **All relationships:** S_W.

**Qualifying route:** Route A, category 1. The displayed median lies outside its printed IQR under any endpoint order. The substituted or truncated upper-quartile digit is also consistent with category 2's printed-value-slip rule, but its production mechanism and intended digit are not inferred.

**Affected result or extracted value:** The intermediate-arm PEEP distribution after titration among patients ventilated in the “other mode” category, specifically its upper quartile and median/IQR to be extracted.

**Why context does not resolve it:** Route A category 1 requires registration of point-estimate/interval containment conflicts. The same-page footer establishes that the parentheses are an interquartile range; no intended upper quartile is provided in immediate context. Knowing that the Q3 must be at least the median does not identify its value for extraction.

**Source-grounded alternatives and missing definitions:** An upper-quartile digit may be absent or substituted, an endpoint may have been displaced, or the central value may belong to a different summary. The reported table footnote provides no alternative statistic or ordering convention. Reversing the two printed endpoints does not restore containment. No particular replacement digit or final correction is proposed. The per-row statistical test is not mapped, but that does not affect the arithmetic quartile relationship or establish a P discrepancy.

**Exact human question:** What are the intended median and first and third quartiles for intermediate-arm PEEP after titration in the other-ventilation-mode group, and which upper-quartile value should a reader extract from eTable 2?

**Related relationship:** S313. The single cell's ordering and containment conflicts are consolidated into this one finding.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 eTable 2 p6 PSV VT day 2 (S275) versus eFigure 3 p12 PSV day 2; diagnostic binary P checks eTable 1 p5 pHa<7.25 day 1/day 2 (S242, S243) | Figure P=.027 versus table P=.03 has overlapping half-unit intervals [.0265,.0275] and [.025,.035], gap 0. For the labelled uncorrected Pearson χ² diagnostics, P≈.390901 versus .40 and P≈.715260 versus .71 produce point-diagnostic residual gaps .004099/.40≈.01025 and .000260/.71≈.000367 before any input allowance, both ≤.05; the diagnostic is not asserted as the authors' test. These apparent precision differences are one consolidated pattern and do not establish significance or interval conflicts. | ROUNDING_OR_DISPLAY_PRECISION |

## Limitations and handoff

No assigned scientific unit is omitted. The table/figure P algorithm, individual continuous-variable measured sample sizes, degrees of freedom, covariance and variance estimator are not fully supplied or mapped; no such specification is inferred, and no t-test or rank-test approximation is substituted for continuous P reproduction. The inventory separates IQRs from confidence intervals and records all tuple-specific printed values and status. Curves were inspected visually for attribution, axes, median direction and P rather than digitized for invented exact quantiles. Count/denominator diagnostics found no qualifying observation in this scope. Pass 2 must be executed by a different fresh runtime agent after the merged ledger, screening log and mechanical recheck exist.

Artifact paths: checkers/parts/statistical_pass_1_support_a.md; statistics/parts/support_a_inventory.md. New source derivative: preprocessing/st1-a-source-p6.png, direct Poppler pdftoppm 25.03.0, CPU. Reused images inspected: review_1_5_2/preprocessing/rendered_pages/joi180108supp3_prod-p5.png, p6.png, p11.png, p12.png, p13.png; source-matched reusable assets preserved unchanged.

# Statistical pass 1 — support shard B

- Runtime agent ID: /root/statistics_pass1_support_b
- Model and reasoning effort: gpt-6.1-sol / high
- Start mode: FRESH_SPAWN
- Exact scope: DOC-004 REPORT, joi180108supp3_prod.pdf, physical pages 7–9; all 72 eTable 3 mode–variable–occasion tuples, all 30 eTable 4 rows, and all 16 eTable 5 subgroup estimate/95% CI rows with all eight shared pair interaction P values.
- Stable relationship IDs: S321–S438, 118 relationships, each PASS_1_COMPLETE.
- Findings: 1, F-ST1-501.
- Excluded apparent observations: 4 rows.
- Scientific coverage gaps: 0.

QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. Current evidence maps and narrowly relevant main REPORT/SAP method excerpts were used; earlier checker/candidate/report conclusions and the web were not read. Exact supplement pages were checked against direct Poppler pdftotext 25.03.0 layout extraction and source-matched reusable page images. New derivative: preprocessing/st1-b-supp-p7-9.txt, produced by `pdftotext -layout -f 7 -l 9 joi180108supp3_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/st1-b-supp-p7-9.txt`. Page images for pages 7, 8, and 9 were visually read on CPU; their historical rendering engine is UNKNOWN_LEGACY_RENDERER. Sources and reused assets were preserved.

Every tuple's detailed pass record appears in statistics/parts/support_b_inventory.md. Continuous eTable 3/4 ranges are IQRs, not CIs; overlapping IQRs and equal rounded medians were not treated as null-effect tests. Binary counts/denominators/percentages were checked with displayed-input/output half-unit intervals and the scope's relative-gap cutoff. All 16 subgroup point estimates lie within ordered CIs and agree with the direction and rounding intervals of the printed group means. Only the ICU-start subgroup CI excludes zero; its P=.01 belongs to the interaction pair, not to that subgroup alone. The main REPORT p4 states two-sided P values, significance .05, no multiplicity adjustment, Gaussian GLM interaction analyses, and exploratory subgroup analyses. No noninferiority/equivalence margin or numeric interim/stopping boundary appears in the assigned tables. Exact subgroup sample sizes and inferential mapping are not supplied, as recorded below.

## Findings

### F-ST1-501

**Title:** Pre-randomization ventilation subgroup labels do not align with the two numerical result rows.

**Relationships:** S435 and S436.

**Exact locations and document roles:** REPORT [DOC-004 joi180108supp3_prod.pdf physical p9, eTable 5, “Ventilation before randomization” block](../../../joi180108supp3_prod.pdf#page=9), including the first numerical line at the section heading, the second numerical line beside “> 6 hours,” and the “≤ 6 hours” label below both numerical lines. REPORT [DOC-001 main article physical p4, subgroup method paragraph](../../../jama_simonis_2018_oi_180108.pdf#page=4) confirms that >6 hours versus ≤6 hours before randomization are the intended two categories but does not supply category-specific results resolving their placement. The main REPORT corroborates the comparison definition; the inconsistency lies within the supplement display.

**Printed values:** First numerical line: low 16.5 ± 11.6, intermediate 16.8 ± 10.7, mean difference −0.29 (95% CI −7.04 to 6.45). Second numerical line: low 15.2 ± 11.6, intermediate 15.4 ± 11.5, mean difference −0.21 (95% CI −1.72 to 1.28). The label “> 6 hours” is printed beside the second numerical line; “≤ 6 hours” is printed below it without a numerical row beside it. Shared interaction P=.98 is placed between the numerical lines. The source image confirms this placement rather than merely an extraction-spacing discrepancy.

**Rule and calculation:** A subgroup estimate/CI row must be mapped to one stated subgroup category for extraction. Sequential category order suggests >6 hours first and ≤6 hours second, whereas direct horizontal alignment puts >6 hours beside the second numerical line and leaves the first line and ≤6-hour label without aligned counterparts. The two CIs have widths 6.45−(−7.04)=13.49 days and 1.28−(−1.72)=3.00 days, a width ratio of 4.50; the extraction choice therefore changes the interval taken for a specified category. Display precision cannot determine which category labels belong to which line. No rounding reconstruction or assumption about subgroup sample size is used to choose a category.

**Focus area:** B, estimate/contrast attribution; the numerical subgroup result cannot be assigned unambiguously to its comparison category.

**Proposed review domain:** report_internal_inconsistency.

**Proposed relationship type / all relationships:** S_W / S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** The >6-hour and ≤6-hour pre-randomization ventilation subgroup means, mean differences, and 95% CIs for ventilator-free days at day 28, especially whether the >6-hour subgroup takes CI −7.04 to 6.45 or −1.72 to 1.28.

**Why context does not resolve it:** This is a label-to-result assignment that changes which numerical result applies, rather than a wording variant. Category sequence and horizontal row alignment give different assignments. The table supplies no subgroup sample sizes or alternative category-specific result location, and the main subgroup paragraph lists the categories without resolving these two numerical rows. A data extractor cannot select an assignment from the supplied label placement alone.

**Alternatives and missing definition:** A vertical layout displacement may have moved both subgroup labels down by one numerical row, making the first numerical line the >6-hour result and the second the ≤6-hour result. Alternatively, the >6-hour label may identify the second numerical line as its printed alignment suggests, with the first line belonging to the other category. Neither assignment is made here. The needed definition is the intended category-to-numerical-line mapping; subgroup sample sizes could corroborate it but are not printed. The shared interaction P=.98 does not distinguish the assignments.

**Exact human question:** Which numerical line in eTable 5 is intended for ventilation >6 hours before randomization, and which is intended for ventilation ≤6 hours: 16.5 versus 16.8 days with mean difference −0.29 (95% CI −7.04 to 6.45), or 15.2 versus 15.4 days with mean difference −0.21 (95% CI −1.72 to 1.28)?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 p8 eTable 4, sedative infusion, analgesic infusion, neuromuscular blockade and vasopressor use; headers 477/484 | The eight count/percentage cells differ from using the arm headers as denominators. Permitting count/header half-unit intervals and percentage ±0.05 yields recomputed intervals and remaining relative gaps: 320/477 versus 70.6%, [66.911,67.261], gap/70.6=.04658; 333/484 versus 72.1%, [68.627,68.976], .04263; 277/477 versus 61.1%, [57.906,58.237], .04604; 273/484 versus 59.1%, [56.244,56.567], .04202; 53/477 versus 11.7%, [10.995,11.228], .03609; 60/484 versus 13.0%, [12.281,12.513], .03362; 363/477 versus 80.0%, [75.916,76.285], .04581; 353/484 versus 76.4%, [72.755,73.113], .04237. All are ≤.05. Exact integers in place of count/header half-unit intervals likewise leave all relative gaps below .05. No row-specific denominator is invented. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-004 p9 eTable 5, eight subgroup pairs, especially pneumonia; REPORT DOC-001 p4 Gaussian interaction-model paragraph | A hypothetical independent normal contrast using subgroup CI widths gives approximate interaction P values .473, .188, .318, .958, .203, .255, .982, .0077 versus printed .16, .17, .32, .96, .23, .26, .98, .01. This is a **diagnostic approximation**, using SE≈CI width/3.92 and SE of the difference≈sqrt(SE1²+SE2²), not a reconstruction of the reported GLM. Subgroup sample sizes, the method producing these CIs, degrees of freedom, link/covariates, variance estimator, covariance and mapping between subgroup CI estimators and the interaction model are not supplied. Independence/covariance is not inferred. The diagnostic does not reproduce all other pairs under the display-precision rule and cannot establish category 4; both pneumonia CIs include zero and its interaction P=.16 is nonsignificant, so there is also no individual CI-versus-null-test contradiction. The pair P tests a different null from either subgroup CI. Preserve this apparent issue and its missing inputs for fresh pass 2. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-004 p7 eTable 3, other-mode respiratory acidosis after titration, low arm | The percentage is printed “35.” for 7/20. Its reading is 35%, and no numeric value or inference changes. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-004 p9 eTable 5 footer | “Data are mean ()” leaves an empty parenthesis despite the ± dispersion shown in each arm; the ± values and the separate mean-difference 95% CI columns remain identifiable. No estimate, interval, P value or extraction assignment conflicts merely because the dispersion abbreviation is absent. | NOTATION_OR_TYPOGRAPHY |

## Limitations and closure

All 118 assigned relationships have PASS_1_COMPLETE records. No source unit/cell in the assigned scope remains unread or unmapped. Exact continuous test names for eTables 3/4, exact sparse binary test/continuity-correction choices, subgroup sample sizes, and CI-to-interaction model mappings are not supplied. Missing details without a reproduced conflict were not treated as findings. No SE, covariance, degrees of freedom, estimand mapping, or model adjustment was inferred from convention. Family-level planned-versus-reported checks remain with the separate plan assignment. A fresh pass-2 agent must reread every stable record and every excluded observation under route A and the display-precision rule.

## Complete per-relationship pass-1 closure

This index merges the explicit PASS_1_COMPLETE relationship records and completed fresh-agent handoffs. Detailed evidence and calculations remain in statistics/relationship_inventory.md and the corresponding assigned shard. Every ID is enumerated here; intervals of IDs are not used as completion shorthand.

| Relationship ID | Fresh pass-1 runtime | Status | Detailed artifact |
|---|---|---|---|
| S001 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S002 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S003 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S004 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S005 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S006 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S007 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S008 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S009 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S010 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S011 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S012 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S013 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S014 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S015 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S016 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S017 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S018 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S019 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S020 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S021 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S022 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S023 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S024 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S025 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S026 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S027 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S028 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S029 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S030 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S031 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S032 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S033 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S034 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S035 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S036 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S037 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S038 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S039 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S040 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S041 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S042 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S043 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S044 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S045 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S046 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S047 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S048 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S049 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S050 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S051 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S052 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S053 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S054 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S055 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S056 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S057 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S058 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S059 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S060 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S061 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S062 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S063 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S064 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S065 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S066 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S067 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S068 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S069 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S070 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S071 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S072 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S073 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S074 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S075 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S076 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S077 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S078 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S079 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S080 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S081 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S082 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S083 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S084 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S085 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S086 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S087 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S088 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S089 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S090 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S091 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S092 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S093 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S094 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S095 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S096 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S097 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S098 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S099 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S100 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S101 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S102 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S103 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S104 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S105 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S106 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S107 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S108 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S109 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S110 | root/statistics_pass1_main | PASS_1_COMPLETE | statistics/parts/main_plan_inventory.md |
| S201 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S202 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S203 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S204 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S205 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S206 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S207 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S208 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S209 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S210 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S211 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S212 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S213 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S214 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S215 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S216 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S217 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S218 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S219 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S220 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S221 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S222 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S223 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S224 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S225 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S226 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S227 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S228 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S229 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S230 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S231 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S232 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S233 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S234 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S235 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S236 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S237 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S238 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S239 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S240 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S241 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S242 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S243 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S244 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S245 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S246 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S247 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S248 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S249 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S250 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S251 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S252 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S253 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S254 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S255 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S256 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S257 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S258 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S259 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S260 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S261 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S262 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S263 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S264 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S265 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S266 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S267 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S268 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S269 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S270 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S271 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S272 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S273 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S274 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S275 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S276 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S277 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S278 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S279 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S280 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S281 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S282 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S283 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S284 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S285 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S286 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S287 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S288 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S289 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S290 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S291 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S292 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S293 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S294 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S295 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S296 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S297 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S298 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S299 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S300 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S301 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S302 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S303 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S304 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S305 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S306 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S307 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S308 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S309 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S310 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S311 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S312 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S313 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S314 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S315 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S316 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S317 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S318 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S319 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S320 | root/statistics_pass1_support_a | PASS_1_COMPLETE | statistics/parts/support_a_inventory.md |
| S321 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S322 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S323 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S324 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S325 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S326 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S327 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S328 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S329 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S330 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S331 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S332 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S333 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S334 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S335 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S336 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S337 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S338 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S339 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S340 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S341 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S342 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S343 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S344 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S345 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S346 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S347 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S348 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S349 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S350 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S351 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S352 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S353 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S354 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S355 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S356 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S357 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S358 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S359 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S360 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S361 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S362 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S363 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S364 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S365 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S366 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S367 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S368 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S369 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S370 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S371 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S372 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S373 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S374 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S375 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S376 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S377 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S378 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S379 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S380 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S381 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S382 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S383 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S384 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S385 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S386 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S387 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S388 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S389 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S390 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S391 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S392 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S393 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S394 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S395 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S396 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S397 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S398 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S399 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S400 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S401 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S402 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S403 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S404 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S405 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S406 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S407 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S408 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S409 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S410 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S411 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S412 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S413 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S414 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S415 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S416 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S417 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S418 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S419 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S420 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S421 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S422 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S423 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S424 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S425 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S426 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S427 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S428 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S429 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S430 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S431 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S432 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S433 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S434 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S435 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S436 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S437 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |
| S438 | root/statistics_pass1_support_b | PASS_1_COMPLETE | statistics/parts/support_b_inventory.md |


