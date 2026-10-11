# Cross-source consistency review

Status: COMPLETE. Scope: all mapped content of DOC-001 pp.1–9 (REPORT), DOC-002 pp.1–129 (PLAN), DOC-003 pp.1–5 (REPORT), DOC-004 p.1 (REPORT). Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md completely; read inventories, tooling record, complete main/support evidence maps. No old scientific conclusions, external evidence, or source changes used. Matched population, time, analysis set, contrast, model, measure and precision before comparison. Nine qualifying findings and 21 excluded-observation groups below. These are findings for independent inclusion screening, without candidate IDs or adjudication.

Engine: direct source confirmation with Poppler pdftotext 25.03.0, -layout, exact pages. Visually aligned Figure 3 through the mapper's source-matched rendered-page record and confirmed printed tuples directly from source extraction. PDF sources remain authoritative. Links are relative to this checker artifact.

## Coverage of cross-location relationships

The review covered 61 bounded comparison groups: design/version/hypothesis/margin (5); endpoint definitions/time origins/hierarchy (8); population/consent/missing outcomes/predictors (5); randomization/stratification/subgroups (6); intervention initiation, flow, duration, cessation, exceptions, comparator, NIV, saturation target (8); primary model/measure/adjustment and repeated mortality results (5); secondary estimator/test/longitudinal/LOS/multiplicity rules (8); interim/stopping/power (5); supplementary table and graphical matching (7); administrative/no-applicable units (4). Grouping preserves every subordinate mapped tuple and every Figure 3 row; it is not a sampling or finding limit.

Repeated mortality counts, percentages and risk difference match across abstract, Key Points, main narrative and Table 2. The intubation, infection, ICU/hospital stay and six-hour descriptive values match their repeated REPORT occurrences, subject to the specific labels/analyses below. Figure 2 and eFigure 1 graphical direction matches printed overall event frequencies. All 26 forest-plot tuples and interaction labels were compared with the endpoint definitions, overall rows and stated subgroup rules. All nine time points in each of the four supplementary longitudinal panels were checked for outcome, scale, time origin and qualitative narrative agreement. No supplied workbook or CSV exists. Administrative pages, references, prior-study results and source-clipped background tables are mapped but do not establish current-trial statistical contradictions.

## Findings

### F-XS-001 — Oxygenation endpoint attributed to a different time origin and population

- Compared locations/roles: REPORT [abstract p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1), REPORT [secondary-results p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6), REPORT [eTable p.2](../../../joi180109supp2_prod.pdf#page=2). PLAN [final endpoint p.103](../../../joi180109supp1_prod.pdf#page=103) corroborates the days1–3 oxygenation endpoint and is not a conflicting relationship.
- Printed statements/values: abstract defines PaO2:FIO2 over “3 days after intubation”; its result is 150 versus119, difference19.5 (95%CI4.4–34.6). The eTable expressly labels the same150 [104–230] versus119 [86–165] medians as six hours after randomization, with arm headers388 each. Main narrative repeats150 versus119 and19.5 (4.4–34.6), alongside improvement until day4 and a pointer to that eTable/eFigure2.
- Comparison logic: postintubation days1–3 and six hours after randomization are different windows and potentially different populations. The exact descriptive pair points to the six-hour table, whereas the abstract's outcome-definition line identifies a postintubation outcome. No numeric recomputation is needed; printed150/119 are identical.
- Focus area: D for endpoint attribution comparison; proposed review domain: report_internal_inconsistency. Proposed relationship: S_C; all relationships: S_C, S_W.
- **Affected result or extracted value:** oxygenation150 versus119 and mean difference19.5 (4.4–34.6), whose population and measurement window a data extractor must assign.
- **Why context does not resolve it:** the abstract does not identify the oxygenation result as six hours after randomization; its explicit endpoint definition selects a postintubation window. Main text also combines a six-hour descriptive pair with a longitudinal statement rather than explaining the abstract's origin.
- Supported alternatives: six-hour randomized-arm comparison, as expressly labeled in the eTable; or a separate postintubation longitudinal comparison, as the abstract names. The package does not connect the latter to this result.
- Human verification: compare these three exact locations and determine the intended population/time label for the150/119 and19.5 result.

### F-XS-002 — Forest-plot effects use the reciprocal direction of repeated overall effects

- Compared locations/roles: REPORT [Table2 p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5), REPORT [methods p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4), REPORT [Figure3 p.7](../../../jama_azoulay_2018_oi_180109.pdf#page=7); mortality also repeats in REPORT [abstract p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1), intubation in REPORT [narrative p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6).
- Printed values: Table2 mortality H138/388 versus C140/388, HR0.98 (0.77–1.24); Figure3 all-patient mortality same counts but HR1.02 (0.81–1.29). Table2 intubation H150/388 versus C170/388, cause-specific HR0.85 (0.68–1.06); Figure3 same counts but HR1.17 (0.94–1.46). Both Figure3 panels label the region below1 as favoring high-flow and above1 as favoring standard oxygen. Methods describe high-flow versus standard HRs from Cox models in stratification-defined subgroups.
- Comparison logic: reciprocal mortality tuple is 1/0.98=1.0204, interval[1/1.24,1/0.77]=[0.8065,1.2987]; reciprocal intubation tuple is1/0.85=1.1765, interval[1/1.06,1/0.68]=[0.9434,1.4706]. The printed plot tuples closely follow reciprocal contrasts. More decisively, the intubation point-estimate intervals from two-decimal rounding, [0.845,0.855) and[1.165,1.175), are disjoint and on opposite sides of1. This is not a crude-ratio comparison.
- Focus area: B; proposed review domain: statistical_results. Proposed/all relationship: S_W.
- **Affected result or extracted value:** overall and subgroup mortality/intubation HR direction, notably Figure3B nonhematologic-malignancy HR1.61 (1.16–2.23), and every plot row's favor-side interpretation.
- **Why context does not resolve it:** no caption states an inverted reference group or a different all-patient model, while favor labels retain the high-flow-below1 convention. The reader cannot apply both the reported0.85 and plotted1.17 to the same named high-flow-versus-standard comparison. Subgroup crude risks alone were not used to establish the issue.
- Supported alternatives: reciprocal reference-group coding in Figure3, with favor labels needing human clarification; or distinct analyses producing differently oriented HRs, not disclosed in the caption. The exact coding remains unprinted.
- Human verification: establish model coding for both panels and check all subgroup rows, all-patient rows and favor labels as one repeated pattern.

### F-XS-003 — Primary planned effect/model/adjustment differs from the reported primary analysis

- Compared locations/roles: PLAN [original SAP p.82](../../../joi180109supp1_prod.pdf#page=82), PLAN [final SAP p.104](../../../joi180109supp1_prod.pdf#page=104), REPORT [primary methods p.3](../../../jama_azoulay_2018_oi_180109.pdf#page=3), REPORT [Table2 p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5), REPORT [limitation p.8](../../../jama_azoulay_2018_oi_180109.pdf#page=8).
- Printed specifications: both SAPs describe binary alive/dead classification at day28, estimation of relative risk of hospital death experimental versus control with95%CI, and analyses adjusted on potential confounders. Report uses Kaplan–Meier, absolute risk difference, and HR from univariable Cox; primary tupleHR0.98 (0.77–1.24), P=.94. It explicitly acknowledges no adjustment on stratification factors.
- Comparison logic: binary risk ratio and time-to-event hazard ratio are different estimands; univariable Cox is not the stated confounder-adjusted primary analysis. No RR for the primary day28 endpoint or adjusted primary result is identified; ICU/hospital mortality RRs in Table2 are distinct endpoints and cannot supply it.
- Focus area: D; proposed review domain: protocol_report. Proposed/all relationship: P_R.
- **Affected result or extracted value:** primary mortality effect0.98 (0.77–1.24), its effect-measure identity and whether it represents the planned primary analysis.
- **Why context does not resolve it:** the disclosed grant-stage noninferiority-to-superiority change does not explain this remaining difference against the final superiority SAP. A limitation noting absent adjustment does not identify a planned adjusted binary analysis as performed or replaced. Specific confounders remain unnamed; no claim about their identities is made.
- Supported alternatives: the final analysis intentionally replaced the SAP's adjusted RR with an unadjusted Cox HR; or an adjusted primary RR was obtained but is not identifiable in supplied report materials.
- Human verification: determine which final primary estimand/model was intended and whether a disclosed later analysis specification reconciles the two.

### F-XS-004 — Planned joint longitudinal analysis differs from reported time-specific rank comparisons

- Compared locations/roles: PLAN [original SAP p.82](../../../joi180109supp1_prod.pdf#page=82), PLAN [final SAP p.105](../../../joi180109supp1_prod.pdf#page=105), REPORT [methods p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4), REPORT [results p.6](../../../jama_azoulay_2018_oi_180109.pdf#page=6), REPORT [eFigures2–3 pp.4–5](../../../joi180109supp2_prod.pdf#page=4).
- Printed specifications: SAPs prescribe joint models taking account of right censoring for oxygenation, dyspnea and comfort. Article selects Wilcoxon rank-sum for comfort/dyspnea and respiratory rate, reports no comfort/dyspnea difference “at any time,” six-hour respiratory difference−1.8, and oxygenation difference19.5 with improvement until day4. Supplement presents separate time points and changing contributor counts, without a joint-model label.
- Comparison logic: a joint longitudinal/censoring model differs from Wilcoxon rank-sum comparisons at individual time points. The positive discrepancy is grounded in the stated comfort/dyspnea methods; oxygenation's reported numerical difference is not identified as coming from the planned joint model. No missing-data mechanism is inferred from contributor counts.
- Focus area: D; proposed review domain: protocol_report. Proposed/all relationship: P_R.
- **Affected result or extracted value:** key secondary comfort/dyspnea interpretation and longitudinal oxygenation19.5 (4.4–34.6), as summarized in the abstract and discussion.
- **Why context does not resolve it:** the article supplies an explicitly different test for two of these longitudinal outcomes and does not describe how the planned joint-model result relates to its time-specific conclusions. The final SAP repeats the original joint-model prescription.
- Supported alternatives: time-specific tests replaced joint models; or both were performed but the report identifies only the former. This is not a recommendation for either analysis.
- Human verification: identify the analysis producing each reported longitudinal conclusion and whether the joint-model plan was retained or changed.

### F-XS-005 — Planned competing-risk infection analysis differs from the reported proportion comparison

- Compared locations/roles: PLAN [original SAP p.82](../../../joi180109supp1_prod.pdf#page=82), PLAN [final SAP p.105](../../../joi180109supp1_prod.pdf#page=105), REPORT [methods p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4), REPORT [Table2 p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5).
- Printed specifications: SAPs specify ICU-acquired infection cumulative incidence with death or alive ICU discharge competing, Gray test and confounder-adjusted cause-specific Cox. Article specifies infection proportions compared by chi-square. Table2 gives39/388 versus41/388,10.0% versus10.6%, difference−0.6% (−4.6,4.1), cause-specific HR1.01 (0.96–1.06), P=.91 (footnote d).
- Comparison logic: a chi-square comparison of proportions is not the prescribed competing-risk cumulative-incidence comparison. The effect column's cause-specific HR does not reconcile the expressly different test or identify an adjusted cumulative-incidence analysis.
- Focus area: D; proposed review domain: protocol_report. Proposed/all relationship: P_R.
- **Affected result or extracted value:** abstract-reported ICU-acquired infection difference−0.6% and Table2's infection effect/test interpretation.
- **Why context does not resolve it:** unlike IMV, which the report expressly analyzes with Gray's test, infection receives an explicit proportion-test description. Neither report nor final SAP supplies an analysis-change explanation for this endpoint.
- Supported alternatives: a proportion comparison replaced the planned competing-risk analysis; or both analyses were performed with the reported P and HR needing attribution.
- Human verification: identify the estimator, competing events, adjustment and test actually producing the infection results.

### F-XS-006 — Planned ICU-stay time-to-event analyses differ from the reported rank-sum analysis

- Compared locations/roles: PLAN [original SAP p.82](../../../joi180109supp1_prod.pdf#page=82), PLAN [final SAP p.105](../../../joi180109supp1_prod.pdf#page=105), REPORT [methods p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4), REPORT [Table2 p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5), REPORT [abstract p.1](../../../jama_azoulay_2018_oi_180109.pdf#page=1).
- Printed specifications: SAPs specify ICU length of stay overall and separately in survivors/dead, with Kaplan–Meier/competing-risk estimators. Report specifies Wilcoxon rank-sum; ICU stay medians8(4–14) versus6(4–13), mean difference0.6days (−1.0,2.2), P=.07. Table2 states length-of-stay effects cannot be expressed as HRs.
- Comparison logic: rank-sum of observed stay lengths differs from the prespecified time-to-event analyses and population split. This is an explicit method replacement, not a comparison of the median difference with the stated mean difference.
- Focus area: D; proposed review domain: protocol_report. Proposed/all relationship: P_R.
- **Affected result or extracted value:** abstract/key-secondary ICU-stay comparison and the0.6day difference/P=.07.
- **Why context does not resolve it:** no time-to-event ICU-stay result is identified and the explicit rank-sum prescription does not connect to the final SAP's estimators. Its former/latter wording is retained rather than assigning an unprinted discharge/death coding.
- Supported alternatives: rank-sum replaced the planned estimators; or planned analyses were additional, with report results requiring method attribution.
- Human verification: determine the implemented ICU-stay analysis, population definition, and relationship to the SAP prescription.

### F-XS-007 — Reported comparator permits high-flow rescue that the final plan prohibits

- Compared locations/roles: PLAN [final intervention p.99](../../../joi180109supp1_prod.pdf#page=99), PLAN [rationale pp.95–96](../../../joi180109supp1_prod.pdf#page=95), REPORT [treatments p.3](../../../jama_azoulay_2018_oi_180109.pdf#page=3), REPORT [interventions p.5](../../../jama_azoulay_2018_oi_180109.pdf#page=5), REPORT [Figure1 p.3](../../../jama_azoulay_2018_oi_180109.pdf#page=3).
- Printed specifications: final plan says HFNO will not be used in control group. Article permits high-flow only for do-not-intubate control patients after standard oxygen fails;30 control patients(7.7%) received it,14(46.7%) died. Figure1 records30 control participants received high-flow.
- Comparison logic: unconditional exclusion of high-flow from the randomized comparator differs from a specified permitted rescue exposure. The observation is the stated intervention rule, not merely the occurrence of treatment crossover.
- Focus area: D; proposed review domain: protocol_report. Proposed/all relationship: P_R.
- **Affected result or extracted value:** intervention contrast underlying mortality35.6% versus36.1% and intubation38.7% versus43.8%, including whether the comparator strategy contains rescue HFNO.
- **Why context does not resolve it:** the report explains who received rescue but does not reconcile permission for it with the final plan's categorical prohibition. The initial-to-superiority disclosure does not supply this change in the final intervention specification.
- Supported alternatives: the final comparator strategy was changed to include rescue; or these were deviations from the planned comparator. No violation or clinical judgment is inferred.
- Human verification: establish whether rescue HFNO was part of the intended final comparator and locate any supplied amendment/disclosure that explains the difference.

### F-XS-008 — Reported predefined time subgroup does not use the planned stratification boundary

- Compared locations/roles: PLAN [stratification pp.98–99](../../../joi180109supp1_prod.pdf#page=98), REPORT [randomization p.2](../../../jama_azoulay_2018_oi_180109.pdf#page=2), REPORT [subgroup methods p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4), REPORT [Figure3 p.7](../../../jama_azoulay_2018_oi_180109.pdf#page=7), REPORT [Table1 p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4).
- Printed specifications: plan strata ICU-admission D0,D1,D2 versus≥D3; report randomization≤2 versus≥3days. Report methods describe subgroups defined by stratification variables and Figure3 title calls them predefined. Figure3 instead uses0–1 versus≥2days: mortalityH120/321 versusC118/330, andH18/67 versusC22/58; IMVH128/321 versusC142/330, andH22/67 versusC28/58. Table1 day2 H47,C38; day≥3 H20,C20.
- Comparison logic: Figure3 late totals67=47+20 and58=38+20 explicitly include day2, whereas the planned/report-randomization late stratum starts day3 (20/20). Thus the difference changes the subgroup analysis populations and cannot be explained by rounding or calendar notation alone. Figure bins themselves are clear; their claimed relationship to predefined strata is the issue.
- Focus area: D; proposed review domain: protocol_report. Proposed relationship: P_R; all relationships: P_R, S_W.
- **Affected result or extracted value:** predefined time-subgroup mortality/IMV HRs and interaction P=.15/.17, assigned to a different subgroup partition.
- **Why context does not resolve it:** no analysis-change explanation identifies why day2 patients move from the planned early stratum to the plotted late subgroup. The Table1 counts demonstrate materially different membership, rather than alternative names for the same population.
- Supported alternatives: an intentionally different subgroup boundary was used; or Figure3 should represent the original strata. The package does not establish which was prespecified.
- Human verification: determine the prespecified subgroup bins and attribution of the four subgroup HR tuples and interactions.

### F-XS-009 — Matched mechanical-ventilation figure and methods name different comparison tests

- Compared locations/roles: REPORT [methods p.4](../../../jama_azoulay_2018_oi_180109.pdf#page=4), REPORT [eFigure1 p.3](../../../joi180109supp2_prod.pdf#page=3); PLAN [final SAP p.105](../../../joi180109supp1_prod.pdf#page=105) corroborates Gray and does not add a conflicting relationship.
- Printed statements: article says cumulative IMV incidence incorporates competing death and is compared using Gray test; eFigure1 is titled Cumulative Incidence of Mechanical Ventilation and labels P(log Rank test)=0.17. Article IMV result/Table2 also reportsP=.17.
- Comparison logic: log-rank and Gray tests are distinct tests for different event-process comparisons. Exact P agreement does not identify which test generated the reported cumulative-incidence result.
- Focus area: C; proposed review domain: statistical_results. Proposed/all relationship: S_C.
- **Affected result or extracted value:** day28 IMV P=.17 and whether it tests the stated competing-risk cumulative incidence.
- **Why context does not resolve it:** both labels explicitly describe the comparison attached to the same cumulative-incidence figure; neither location says an additional log-rank analysis was presented. Treating one named statistical test as another requires an unsupported assumption, beyond a recognizable missing symbol.
- Supported alternatives: Gray test was used and the figure's test label needs clarification; or the figure reports an additional log-rank analysis not identified in methods.
- Human verification: identify the test producing the figure and Table2 IMV P value and establish whether they are the same analysis.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN initial pp.2,6,7,38–55; final pp.90–105; REPORT p.3 | Initial noninferiority9%/26%control/80%power/816 versus final superiority30%vs20%/90%/778; article expressly explains grant-jury design revision. | CONTEXT_RESOLVES |
| PLAN p.1 versus REPORT p.3 | Cover says no amendment; article identifies initial grant version and revised IRB version. A pre-IRB revision need not be an amendment to an approved protocol. | CONTEXT_RESOLVES |
| PLAN initial p.6 versus p.7 and final p.97 | Initial English day28 after ICU admission versus French after randomization; later final plan explicitly fixes randomization and reported analysis uses that origin. | CONTEXT_RESOLVES |
| PLAN initial p.42/illustrative pp.40–41 | NI decision lower boundary less than9% conflicts with illustrative lower-limit direction, but abandoned NI rule is not the decision rule used for reported superiority result. | PERIPHERAL_COMPARISON |
| PLAN pp.50,99 | Center called randomization unit although patients assigned1:1 in fixed blocks; immediate allocation paragraph establishes individual patient allocation. | TERMINOLOGY_OR_WORDING |
| PLAN pp.52,104 | Primary-hypothesis sentence names NIV while adjacent intervention/secondary hypotheses unequivocally concern HFNO. | TERMINOLOGY_OR_WORDING |
| PLAN p.100 | Exception clause says standard oxygen will be used; surrounding continuous-HFNO, Venturi-intolerance and cessation clauses make intended restriction clear. | CONTEXT_RESOLVES |
| PLAN initial pp.43–45 versus final pp.99–100 | Initial40L/min minimum, <2L/min weaning, usual NIV differ from final50L/min first3days, <6L/min and restricted NIV; final version agrees with report. | CONTEXT_RESOLVES |
| PLAN initial p.53 versus p.61/final pp.102–103 | No efficacy interim in initial protocol versus safety wording and final100-death interim; final design supersedes initial, efficacy and safety roles distinguishable. | CONTEXT_RESOLVES |
| PLAN final pp.102–103 versus REPORT pp.3,5 | 100-death Haybittle–Peto.001, final.05 and Bayesian supplementary insight agree; no numerical Bayesian stopping threshold is supplied or claimed. | NOT_REPRODUCED |
| PLAN pp.104–105 versus REPORT pp.3–4 | Missing outcomes/predictors strategy is conditional; report has no loss to primary follow-up and no established missing-predictor analysis requiring imputation. | CONDITIONAL_OR_UNREPORTED |
| PLAN p.104 versus REPORT methods/results | Per-protocol sensitivity planned but no separate result identified; absence alone does not establish replacement or change in primary result. | CONDITIONAL_OR_UNREPORTED |
| PLAN p.103 versus REPORT p.3 | 778 versus779 total alongside389 per arm and actual778 randomized; the paired arm counts immediately establish intended recruitment total. | NOTATION_OR_TYPOGRAPHY |
| REPORT abstract p.1 versus narrative p.6 | Respiratory CI upper endpoint−0.2 versus−0.3 at one decimal; adjacent rounding intervals meet at−0.25 and neither changes inference. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT abstract/Key Points/flow/Table2 | 776 included/completed versus778 randomized is expressly explained by two withdrawn consents; identical analyzed arm sizes388. | CONTEXT_RESOLVES |
| REPORT eTable/eFigures2–3 versus main descriptions | Table centers are medians while plotted centers are unlabeled; exact estimates/dispersion cannot be assumed identical. Different pointwise contributor counts do not establish changed primary analysis size. | PERIPHERAL_COMPARISON |
| REPORT Figure2 p.6 versus mortality Table2 | Log-rankP=.85 versusP=.94: article also specifies Cox effect analysis; test statistic/model details do not establish that both P values must be identical. | CONDITIONAL_OR_UNREPORTED |
| PLAN and REPORT centre rosters/calendars/software | 26/30/31/32 centres, recruitment projections, historical data and SAS+R versus R3.1.0 do not change an established trial result/decision. | PERIPHERAL_COMPARISON |
| REPORT Table2 medians versus mean differences | ICU8vs6 and hospital24vs27 are medians, whereas effect column/footnote explicitly names differences in means. | CONTEXT_RESOLVES |
| PLAN final oxygen<9/≥9 versus REPORT≤9/>9 | Equality boundary differs, but no supplied exact9L/min subgroup membership or changed extracted key result is established; Figure3 bins are explicit. | CONDITIONAL_OR_UNREPORTED |
| REPORT posthoc organ-support sentence p.6 |153(19.7%) and31(4%) have an unclear group/therapy attribution, but this is a peripheral posthoc result absent from abstract/key-secondary hierarchy. | PERIPHERAL_COMPARISON |

## Limitations

No scientific coverage gaps within assigned scope. Source-cropped historical Table4 pp.127–128 has incomplete background text, without current HIGH endpoint/model/decision implications. Supplementary graphs lack exact numeric centres and bar definitions; approximate graph readings were used only for qualitative alignment, never for precise effect/CI/P calculations. Exact reference coding, joint-model implementation and named adjustment covariates are not printed; findings state the resulting human verification questions without inferring implementation or proposing a preferred analysis.

Coordinator audit qualification: the respiratory CI upper-limit comparison uses the workflow's half-unit display allowances, which touch at −0.25; the source does not establish a tie/rounding convention or identical unrounded values. Shared negative direction and the isolated final digit support the existing display-level exclusion.

Coordinator audit clarification of method findings: explicit planned and reported procedures differ. Whether a reported procedure replaced a planned analysis or both were performed remains a human question; categorical replacement phrasing must not be carried forward as an established implementation fact.
