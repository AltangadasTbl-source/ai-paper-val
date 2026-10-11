# Cross-source consistency review

Fresh mandatory cross-source checker; model gpt-6.1-sol, medium effort. Scope: all matched results across DOC-001 REPORT pp.1–10, DOC-003 REPORT pp.1–17, DOC-004 REPORT p.1; all prospective statistical-design elements and criterion lists in DOC-002 PLAN pp.1–55. QUALITY_CONTROL_SCOPE.md and the complete 1.6.2 review contract were read. Current main/support maps were used as locators; no previous scientific conclusions were read. Targeted source confirmation used direct `pdftotext -layout` (Poppler 25.03.0) to stdout, and source-linked reusable page images for graphical material. No derivative was produced, no source or reused asset changed; CPU. No external evidence was used.

## Coverage and matched checks

All main mapping relationships MN001–MN023 and MS001–MS098, support-results N301–N310/S301–S307, plan-a PA-N001–PA-N018/PA-S001–PA-S017, and plan-b N-PB01–N-PB06/S-PB01–S-PB14 were reviewed for matched-source implications. Complete table-cell transcription and source-unit coverage in those current maps were included, rather than limiting review to the abstract. Checked populations, timing, treatment contrast, Bayesian versus frequentist model, genotype, scale, reference group, and precision before comparison. DOC-004 contains no data available for additional result comparisons.

| Comparison family | Complete check and outcome |
|---|---|
| Abstract, Key Points, main narrative, Tables 1–2 and Figures 1–3 | Enrolled/completed/genotype counts, primary stiffness treatment summaries, Bayesian overall/genotype effects and probabilities, frequentist stiffness effect, earlier RCT quotation, clinical response, safety, and interpretation checked. Sex proportion is finding F-XS-001. Remaining repeated primary numerical copies reconcile. Baseline genotype table is 27 completers, rather than the 30 enrolled patients. |
| Main narrative/Table 2 secondary results | Pain, weakness, tiredness, SF-36, INQoL, bedside tests, Timed Up&Go, force, paresis and EMG text matched to appropriate rows, genotype contrasts and models. Matching narrative repeats reconcile; estimate/test checks remain separately covered by statistical reviewers. |
| Main versus results supplement | All individual patient IDs, completion/set counts, genotype, efficacy labels, posterior probabilities, graphical primary effects, adverse events and implemented models matched. Findings F-XS-006 and F-XS-007 concern population-definition and nonresponder-label statements. Distinct interim versus hierarchical individual results were not silently treated as identical. |
| Plan versus report primary definition/window and intervention | Stiffness primary mean, daily final-two-week window, 0.75 threshold, positive placebo-minus-mexiletine contrast, 4-week arms, 1-week between-arm washout, 1–4 sets and 600-mg target dose checked. No superiority/noninferiority/equivalence margin is specified; this is a meaningful-benefit probability question. Titration absent from report does not establish contradictory delivered dose. |
| Plan versus report populations and criteria | Three inclusion items and eight exclusion items compared individually to report eTable 1 and main narrative, including age, genotype, consent, neurological conditions, DM1/2, ECG thresholds, antiarrhythmic list, pregnancy/lactation, medication-specific washouts and renal/hepatic/cardiac/seizure criteria. Analysis-set restriction is F-XS-005. Broad psychiatric eligibility statement is F-XS-006. |
| Plan versus report analyses/priors | Hierarchical model, patient effects, subgroup/center structure, common residual variance, priors, clinical-prior sensitivity, pair/order checks and frequentist comparison checked. Planned versus implemented primary priors/sensitivity are F-XS-002. Secondary hierarchy/analysis changes are F-XS-003. Single-center removal of center contrast is intelligible from actual setting; no assumption about unseen covariances is imposed. |
| Secondary definitions item by item | IVR pain/weakness/fatigue; other-week/washout IVR; INQoL; SF-36; clinical myotonia including percussion; quantitative grip/warm-up; biceps force; plasma; needle EMG. Quantitative grip relaxation endpoint changes are F-XS-004. Other apparent procedural differences were screened as below. No planned key-secondary designation is supplied. |
| Sample size, power, missingness, stopping and multiplicity | Planned 30-person simulations, clinical design/analysis priors, 10 observations/arm and 2/3 pairs, expected posterior probabilities versus reported explicitly post hoc 14-observation stopping simulations, fixed 1.75 and 68.5%/69% power checked as distinct analyses. Missingness planning does not specify imputation; report explicitly uses available data and no imputation. Individual efficacy thresholds, advisory nature, safety stopping and absence of study-wide efficacy interim analysis checked. Plan-internal prior and safety rules are F-XS-008/009. Report's unadjusted exploratory secondary interpretation versus prospective status is retained in F-XS-003. |

## Findings

### F-XS-001 — Abstract enrolled male proportion does not reconcile with enrolled sex counts

- **Locations and roles:** [DOC-001 abstract Results p.1](../../../jama_stunnenberg_2018_oi_180136.pdf#page=1), REPORT; [DOC-001 Baseline Data p.4](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4), REPORT. Supplement [DOC-003 eTable 2 pp.3–4](../../../joi180136supp2_prod.pdf#page=3) corroborates enrolled sex identities; it is REPORT and does not create a separate conflict.
- **Printed statements:** Abstract: 30 enrolled, “22% men.” Body: “Twenty-two men and 8 women” enrolled.
- **Comparison logic/calculation:** Same enrolled population. 22/30×100=73.333%, versus 22%. Conservatively allowing half-unit intervals for both count inputs yields 100×[21.5/30.5,22.5/29.5]=[70.492,76.271]%; abstract percentage interval [21.5,22.5]%; gap 47.992 percentage points; relative discrepancy 47.992/22=2.1815 (>0.05). Exact integer counts strengthen the discrepancy.
- **Focus area:** A. **Proposed review domain:** statistical_results. **Relationship:** S_W.
- **Qualifying route:** Route A, category 2.
- **Affected result or extracted value:** Enrolled sample male percentage extracted from the abstract.
- **Why context does not resolve it:** Route A printed percentage changes the sample reading despite body counts permitting reconstruction.
- **Supported alternatives:** “22” may refer to the male count rather than percentage; no normalization is imposed.
- **Human question:** Which enrolled male proportion should be retained, and what does the abstract's 22% represent?

### F-XS-002 — Planned primary clinical-prior and robustness analyses are replaced by different printed priors without their results

- **Locations and roles:** [DOC-002 Study Design p.12](../../../joi180136supp1_prod.pdf#page=12), [§9.1 pp.40–41](../../../joi180136supp1_prod.pdf#page=40), PLAN; [DOC-001 Bayesian Analysis p.3](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3), REPORT; [DOC-003 eMethods 2 pp.11–12](../../../joi180136supp2_prod.pdf#page=11) and [eMethods 3 pp.13–14](../../../joi180136supp2_prod.pdf#page=13), REPORT.
- **Printed statements:** Plan requires clinical priors for individual treatment effects and overall mean effect, almost noninformative remaining parameters, inverse-gamma variance priors with shape/scale 0.001; elicited overall effect prior normal mean 1.75/SD 0.89. It explicitly promises robustness comparison replacing elicited priors with noninformative priors. Implemented group code instead specifies independent arm means `dnorm(4,0.001)`, subgroup coefficients `dnorm(0,0.01)` and each SD `dunif(0.01,10)`. The complete main article/results supplement reports no paired clinical-prior/noninformative-prior primary results.
- **Comparison logic:** The supplied implemented primary group/subgroup code contains a different prior specification and no elicited effect prior; neither report document supplies the prospective primary sensitivity comparison. This finding combines the primary-prior replacement and its omitted planned robustness counterpart, rather than treating every prior line as a separate issue. Numeric rounding is inapplicable to distribution-family/analysis-presence differences.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship:** P_R.
- **Qualifying route:** Route A, category 5.
- **Affected result or extracted value:** Overall primary stiffness effect 3.06 (95% CrI 1.96–4.15), clinically meaningful probability 100%, and genotype estimates/probabilities, whose planned robustness under clinical priors is not reported.
- **Why context does not resolve it:** Route A covers a planned primary analysis that is replaced or not reported. The reported post hoc sample-size simulation is not an analysis of observed efficacy under alternative priors.
- **Supported alternatives:** A later amendment may have selected the printed priors; clinical-prior sensitivity may exist outside the supplied package. Neither is supplied. The vague individual interim prior is separately allowed by plan §9.2 and is not itself this issue.
- **Human question:** Was the observed primary analysis under elicited clinical priors and its planned prior-sensitivity comparison conducted, and which specification/amendment generated the reported posterior results?

### F-XS-003 — Prespecified secondary outcomes are described as exploratory and non-IVR Bayesian analyses are replaced by frequentist results

- **Locations and roles:** [DOC-002 summary p.7](../../../joi180136supp1_prod.pdf#page=7), [§7.1.2 p.31](../../../joi180136supp1_prod.pdf#page=31), [§9.1 p.40](../../../joi180136supp1_prod.pdf#page=40), PLAN; [DOC-001 secondary definitions/frequentist methods p.3](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [Statistical Analysis p.4](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4), [Table 2 pp.7–8](../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), REPORT.
- **Printed statements:** Plan lists IVR pain, weakness/fatigue, clinical myotonia, quantitative grip, INQoL, SF-36, plasma, biceps force and needle EMG as secondary and states “The secondary endpoints will be analyzed in the same way” following its hierarchical Bayesian model. Report explicitly says secondary measures “should be interpreted as exploratory,” owing to no multiple-testing adjustment, and describes dependent t tests for other normally distributed secondary outcomes. Observed Bayesian results are supplied for IVR pain/weakness/tiredness, while Table 2 reports frequentist estimates/CIs/P values for non-IVR endpoints.
- **Comparison logic:** Prespecified secondary status versus explicitly exploratory interpretation is a status change under the required Route A rule. In the same changed secondary-analysis pattern, the printed prospective model is replaced for non-IVR endpoints by frequentist tests. No amendment or clarification limiting the plan's secondary-model promise is supplied. No numerical recomputation applies.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship:** P_R.
- **Qualifying route:** Route A, category 5 (status change); Route B additionally supports the printed planned-versus-reported secondary model conflict.
- **Affected result or extracted value:** Secondary IVR and objective/quality-of-life outcome status and the analysis interpretation of Table 2 non-IVR treatment effects.
- **Why context does not resolve it:** Route A requires registration of reproduced status changes. Calling P values exploratory explains the report's inferential caution, but does not supply the prospective-to-reported hierarchy/analysis reconciliation.
- **Supported alternatives:** “Exploratory” might refer only to interpretation of unadjusted tests, while outcomes retain formal secondary status; a methodological amendment may have replaced non-IVR models. Human review can distinguish these readings.
- **Human question:** What formal outcome status and prospective analysis specification apply to each listed secondary outcome, and where is the change from the plan's Bayesian specification documented?

### F-XS-004 — Reported quantitative-grip relaxation endpoint differs from all three planned cutoffs

- **Locations and roles:** [DOC-002 Quantitative grip myotonia pp.32–33](../../../joi180136supp1_prod.pdf#page=33), PLAN; [DOC-001 Outcomes p.3](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [Table 2 relaxation rows p.7](../../../jama_stunnenberg_2018_oi_180136.pdf#page=7), [footnote j p.8](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8), REPORT.
- **Printed statements:** Plan measures three relaxation durations: 90%→10%, 90%→50%, 90%→75% MVIC. Report defines and labels relaxation as 90%→5%, with first/fifth/mean dynamometry results.
- **Comparison logic:** The lower force threshold is 5% rather than any prospectively specified 10%, 50% or 75%; this changes the measured relaxation-time quantity. These are exact endpoint thresholds, not interchangeable descriptions or rounded outcome estimates. Display precision therefore cannot reconcile the endpoint-definition change.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Table 2 dynamometry relaxation treatment differences, including mean −0.02 seconds (95% CI −0.28–0.25), and the endpoint definition a reviewer would extract.
- **Why context does not resolve it:** A reader cannot assume that 90%→5% is one of the three specified cutoffs; reaching 5% represents a different portion of relaxation. The report does not describe a threshold amendment.
- **Supported alternatives:** A later measurement specification may have selected the 5% cutoff; the historical study description in plan p.26 mentions a 90%→5% endpoint but does not amend the current protocol's operative pp.32–33 measurements.
- **Human question:** Which quantitative-grip endpoint was prospectively specified and implemented, and how do the 90%→5% results relate to the three planned relaxation outcomes?

### F-XS-005 — Completer-based primary analysis conflicts with planned inclusion of pretermination data

- **Locations and roles:** [DOC-002 §7.5 p.35](../../../joi180136supp1_prod.pdf#page=35), PLAN; [DOC-001 Bayesian Analysis p.3](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [Figure 1/Numbers Analyzed p.4](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4), REPORT; [DOC-003 eTable 3 p.5](../../../joi180136supp2_prod.pdf#page=5), REPORT.
- **Printed statements:** Plan: intent-to-treat, “All data acquired prior to termination ... included in the primary analysis unless patient withdraws consent.” Report restricts aggregate inclusion to completion of at least one treatment period, and analyzed results/flow include exactly 27 completers with 31 sets. Patients 3,6,7 dropped out and are absent from individual primary-result table; patient 7 discontinued for an adverse reaction, not described as withdrawal of consent.
- **Comparison logic:** Prospective inclusion of all acquired pretermination data uses consent withdrawal as the exception; reported completion-based inclusion uses a different criterion. This concerns the stated analysis population, not a claim that unseen withdrawal data must change the estimate. No raw early data or consent records are supplied, so numerical effect recalculation is unavailable.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Primary Bayesian stiffness analysis population n=27 and overall treatment effect 3.06.
- **Why context does not resolve it:** The report's “all available data” applies within the completion-defined population and does not state whether pretermination data from excluded patients were unavailable, withdrawn, or omitted under an amended rule.
- **Supported alternatives:** Dropouts may have no evaluable postbaseline primary data, or may have withdrawn consent. The package does not establish either; the observed finding is the different printed population rules.
- **Human question:** Were pretermination primary data from patients 3,6,7 included or unavailable/withdrawn, and what reconciles the reported completion criterion with the planned intent-to-treat criterion?

### F-XS-006 — Main eligibility description excludes psychiatric comorbidity while supplied criteria and enrolled histories do not

- **Locations and roles:** [DOC-001 Clinical Trial Design and Patients p.2](../../../jama_stunnenberg_2018_oi_180136.pdf#page=2), REPORT; [DOC-003 eTable 1 p.2](../../../joi180136supp2_prod.pdf#page=2), [eTable 2 p.3 patients 7/10](../../../joi180136supp2_prod.pdf#page=3), REPORT; [DOC-002 §4.2–4.3 pp.18–19](../../../joi180136supp1_prod.pdf#page=18), PLAN.
- **Printed statements:** Main describes trials in patients “without cardiac or psychiatric comorbidity or comedication,” referring to eTable 1. Item-by-item supplied exclusion lists contain cardiac and specified systemic conditions, but no psychiatric exclusion. Reported enrolled patient histories include patient 7 depression and patient 10 panic disorder; patient 10 remains in primary analysis. Patient 11 has stable angina, adding a cardiac reading that may depend on the specified ECG criteria.
- **Comparison logic:** Broad psychiatric-comorbidity exclusion is not contained in the supplied prospective or report criterion list, and the report itself lists psychiatric diagnoses in enrolled/analysed patients. This is a population-definition conflict, not merely different names for one condition. No inference about clinical suitability is made.
- **Focus area:** D (planned population), A/C population labeling. **Proposed review domain:** protocol_report. **Relationship:** P_R; **All relationships:** P_R, S_C.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Population eligibility/transportability definition for the primary effect n=27, including whether psychiatric-comorbidity patients were excluded.
- **Why context does not resolve it:** The qualifying restriction “active,” “unstable,” or interfering comorbidity is not printed in the main eligibility statement or eTable 1; it cannot be assumed from patient diagnoses alone.
- **Supported alternatives:** The sentence may mean unstable or clinically relevant comorbidity, with stable disease permitted; “comorbidity or comedication” may summarize a narrower clinical judgment. An unsupplied amendment could add criteria. None gives the exact printed population definition.
- **Human question:** What precise cardiac/psychiatric exclusion criterion applied, and how should eligibility be represented alongside the enrolled comorbidity histories?

### F-XS-007 — All three nonresponders are described as meeting predefined Bayesian ineffectiveness although patient 11's probability is 38%

- **Locations and roles:** [DOC-001 Primary Outcome Measure p.4](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4), [Bayesian stopping rule p.3](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3), REPORT; [DOC-003 eTable 3 patient 11 and footnote p.5](../../../joi180136supp2_prod.pdf#page=5), REPORT.
- **Printed statements:** Main: “In 3 patients (11%), Bayesian analysis showed the predefined clinical ineffectiveness”; lower than 20% probability is its ineffectiveness stopping rule. Supplement labels patients 11,13,22 nonresponders and defines nonresponse <20%, but patient 11 is 38%; footnote explains zero observed stiffness, influential flat prior and clinical discontinuation after one set. Other two probabilities are 2% and 1%.
- **Comparison logic:** Patient 11's 38% is in the 20–80% continuation interval, not below20%. Rounding [37.5,38.5]% cannot place it below20%; this is decision-rule classification rather than a recomputed outcome estimate. Two patients meet the printed probabilistic nonresponse criterion; a third received a clinical override disclosed in the footnote.
- **Focus area:** B/C. **Proposed review domain:** statistical_results. **Relationship:** S_C; **All relationships:** S_C, S_W.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Number/proportion classified as Bayesian predefined ineffective (3/27, 11%) and the distinction between posterior criterion failure and clinical discontinuation.
- **Why context does not resolve it:** The footnote explains a clinical decision, but does not make 38% satisfy the stated Bayesian cutoff. Main explicitly attributes all three classifications to predefined Bayesian ineffectiveness.
- **Supported alternatives:** Patient 11 can reasonably be a clinical nonresponder because observed stiffness was absent; a clinical override may have been intended. This is distinct from the printed probabilistic criterion.
- **Human question:** Should the three nonresponders be described as two meeting the predefined probability rule plus one clinical override, or was another prespecified ineffectiveness rule used?

### F-XS-008 — Plan's interim diagram adds informative priors where its operative text permits only noninformative priors

- **Locations and roles:** [DOC-002 §9.2 p.42](../../../joi180136supp1_prod.pdf#page=42), [Figure 4 p.43](../../../joi180136supp1_prod.pdf#page=43), both PLAN. Source-linked full-page image p.43 was visually inspected.
- **Printed statements:** Text: “For our interim analyses we will use non-informative priors only,” to prevent elicited priors driving stopping advice. Figure prints “+informative priors” arrows into the LR1 discontinuation-criteria path and LR2 effectiveness decision.
- **Comparison logic:** The diagram labels adding informative priors on paths that produce continuation/discontinuation and treatment advice, while adjacent operative text rules them out. This changes primary-outcome interim computation, rather than a peripheral figure pointer. No arithmetic or display-precision calculation applies.
- **Focus area:** D. **Proposed review domain:** plan_material. **Relationship:** P_P.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Prospective prior specification for individual posterior efficacy advice used to stop primary N-of-1 observation.
- **Why context does not resolve it:** Caption/diagram supplies no separation of informative-prior treatment decisions from noninformative-prior stopping calculations; one arrow visibly feeds the “discontinuation criteria met?” branch.
- **Supported alternatives:** Informative priors may have been intended only for subsequent clinical decisions or as a schematic optional analysis; text may supersede an earlier illustration. The binding decision path is not identified.
- **Human question:** Which prior specification governed each diagrammed interim decision, and should the informative-prior arrows be read as separate clinical decision support?

### F-XS-009 — Plan text and safety diagram define different study-level DSMB review triggers

- **Locations and roles:** [DOC-002 §8.4 p.38](../../../joi180136supp1_prod.pdf#page=38), [Figure 3 p.39](../../../joi180136supp1_prod.pdf#page=39), both PLAN. Source-linked full-page p.39 image was visually inspected.
- **Printed statements:** Text: accumulated serious adverse events related to study “equal to or more than 10% (three patients)” or two or more same cardiac AE/SAE triggers review. Diagram: cardiac events AE/SAE in “more than 10% (three patients)” or two or more same cardiac event triggers review.
- **Comparison logic:** First trigger differs in event category (all study-related SAEs versus cardiac AE/SAE) and boundary (≥10% versus >10%). With planned n=30, three patients=10%; ≥10% includes three and >10% first includes four, while diagram itself says three. Parenthetical three does not resolve the differing event sets. Percent threshold is a decision rule, so display rounding cannot replace its inequality.
- **Focus area:** D. **Proposed review domain:** plan_material. **Relationship:** P_P.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Prespecified safety-dependent study continuation/stopping review rule underlying the observed safety evaluation.
- **Why context does not resolve it:** Three noncardiac study-related SAEs and three varied cardiac AEs would activate different printed versions; no precedence instruction identifies the operative trigger.
- **Supported alternatives:** Diagram may summarize only cardiac surveillance while text retains a broader SAE rule; “more than” may have intended ≥. Both alternatives require clarifying which rule governed decisions.
- **Human question:** Did three study-related SAEs of any type, three cardiac AE/SAEs, or more than three cardiac events trigger DSMB review, and which text/diagram rule governed?

### F-XS-010 — Reported bedside relaxation measurements use a different preceding contraction duration

- **Locations and roles:** [DOC-002 Clinical Myotonia test p.32](../../../joi180136supp1_prod.pdf#page=32), PLAN; [DOC-001 Outcomes p.3](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3), [Table 1 footnote d p.5](../../../jama_stunnenberg_2018_oi_180136.pdf#page=5), [Table 2 footnote h p.8](../../../jama_stunnenberg_2018_oi_180136.pdf#page=8), REPORT.
- **Printed statements:** Plan instructs eye closure tightly for three seconds and fist closure forcefully for three seconds, each repeated five times with relaxation timed. Report defines both eyelid and handgrip relaxation after forceful contraction for five seconds, repeated five times.
- **Comparison logic:** Both sources specify the preceding contraction duration as part of the same secondary relaxation-time endpoint. Exact three-second versus five-second instructions differ; this is not different terminology for one test and cannot be equated by rounding. The finding is about the prospective/report endpoint specification, without assuming any clinical effect of the duration change.
- **Focus area:** D. **Proposed review domain:** protocol_report. **Relationship:** P_R.
- **Qualifying route:** Route B.
- **Affected result or extracted value:** Table 2 first/fifth/mean handgrip and eyelid action-myotonia treatment differences and the measurement definition for extraction.
- **Why context does not resolve it:** Report footnotes repeat five seconds, whereas the operative protocol repeats three seconds for both assessments; no supplied amendment identifies the performed duration or equates the two definitions.
- **Supported alternatives:** Actual assessments may have adopted a revised five-second specification, or one document may summarize another protocol version. Neither is supplied.
- **Human question:** Were the bedside relaxation times collected after three-second or five-second contractions, and where is the endpoint-specification change documented?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 pp.1/4 versus REPORT Table 1 p.5 | Enrolled genotype/sex totals differ from Table 1 totals because Table 1 presents 27 completers (16/11), whereas enrolled totals are 30 (19/11); no matched-population numerical conflict beyond F-XS-001. | CONTEXT_RESOLVES |
| REPORT DOC-001 p.3 versus REPORT Table 2 pp.7–8 | Bayesian effects/CrIs differ from frequentist mixed-model effects/CIs, explicitly identified as distinct analyses. | CONTEXT_RESOLVES |
| PLAN DOC-002 p.12 versus pp.44–45 | Two Nijmegen cohorts of10 versus total30 with additional Maastricht10; later recruitment section supplies the additional group, rather than establishing a competing final sample size. | CONTEXT_RESOLVES |
| PLAN DOC-002 pp.19–21 versus REPORT DOC-001 p.3/DOC-003 pp.15–17 | Planned expected posterior probability0.817/0.821 and0.782/0.784 versus reported power68.5%/69% arise from explicitly different post hoc simulation design and estimand, not two copies of the same power. | CONTEXT_RESOLVES |
| PLAN DOC-002 p.18 versus REPORT DOC-003 eTable1 p.2 | Third inclusion item permits earlier-registry participant OR any new genetically confirmed NDM patient, so shorter adult/genetic-confirmation report list does not narrow that criterion. Missing CTG-repeat cutoff in eTable1 is identifiable as exclusion of DM1/2, with protocol supplying the cutoff. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002 p.13 versus REPORT DOC-001 p.2 | Drug-specific prebaseline washout minima2/3/5days versus actual2weeks do not conflict:14days meets all minima. | CONTEXT_RESOLVES |
| PLAN DOC-002 pp.12–13 versus REPORT DOC-001 pp.1–2 | Initial1/day then2/day dose titration absent from report's600mg target-dose description; no printed administered-dose statement excludes titration. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 p.34 versus REPORT DOC-001 p.3 | Rectus femoris needle-EMG descriptions differ in procedural detail (three areas/minimum500ms versus10insertions/30seconds); report states same named grading criteria, no incompatible grade threshold reproduced. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp.31–34 versus REPORT DOC-001 p.3/Table2 | Timed Up&Go and grip-derived transient paresis appear in report; protocol separately lists biceps force/percussion/other-week IVR. Added reported analyses are not called prespecified and omitted analyses are not primary or designated key-secondary; absence alone does not meet Route A5. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 p.42 versus REPORT DOC-001 p.3/eTable3 p.5 | Inclusive80%/20% versus strict>80%/<20% wording, including printed80% responders, cannot establish different decisions because displayed integer probabilities can conceal values>80%. No exact-boundary probability is supplied. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 Figure3C p.6 versus narrative pp.4/9 | Caption's patient1–11 references include dropout IDs and its x-axis does not match Figure2; precise included sequential data are not supplied. The apparent issue concerns a pointer/label, without a reproduced changed posterior value. | PERIPHERAL_COMPARISON |
| REPORT DOC-001 Table1 p.5 versus REPORT DOC-003 eTable2 pp.3–4 | Baseline descriptive copies and individual distributions are peripheral across documents; current table internal arithmetic/scale checks belong to numeric/statistical checker scope. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 calendar/site lists versus REPORT DOC-001 pp.1–2/4 | Recruitment calendar and two planned centers versus actual one center are administrative comparisons. Single-center actual data make center contrast unnecessary; no conflicting reported adjustment claim is printed. | PERIPHERAL_COMPARISON |

## Limitations and completion

Ten findings; thirteen excluded observations. All assigned matched-result and prospective design families covered, no scientific-coverage gap. No raw participant-level outcomes/covariance matrices or early-withdrawal data supplied; interval coordinates in main individual graph are approximate and are not substituted for printed supplement intervals. An unprinted specification is not manufactured to turn these limits into a finding. Source confirmation and human adjudication remain separate stages.
