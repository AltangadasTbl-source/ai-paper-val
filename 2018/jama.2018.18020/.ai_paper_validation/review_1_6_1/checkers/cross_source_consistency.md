# Cross-source consistency review — Workflow 1.6.1

Runtime agent: `/root/cross_source_checker`. Scope: DOC-001 REPORT physical pages 1–10; DOC-002 PLAN pages 1–55; DOC-003 REPORT pages 1–17; DOC-004 REPORT page 1. All 83 mapped pages were covered through the current complete quantitative maps and targeted direct-source rereading. No structured result file, separate SAP, or amendment is supplied. Three findings and 20 excluded observations are recorded. Findings require independent inclusion screening and human adjudication; no stable candidate IDs or dispositions are assigned here.

The complete QUALITY_CONTROL_SCOPE.md and review_contract.md, current inventories, tooling record, settings and both fresh quantitative evidence maps were read. Review covered all mapped numeric/statistical families, all 27 individual primary-result tuples, the four group IVR distributions, all Table 2 rows and their matching narrative occurrences, complete flow/safety denominators, figures/captions/footnotes, and all prospective statistical design relationships. Matched comparisons distinguish Bayesian from frequentist results, individual interim from hierarchical estimates, enrolled from completing populations, baseline from treatment means, historical from current results, and posterior expected probability from simulation power. No old scientific conclusion artifact or external material was used.

## Coverage and comparison record

| Comparison family | Scope and outcome |
|---|---|
| Abstract, Key Points, results and conclusions | Primary frequentist 3.12 (2.46–3.78), Bayesian 3.06 (1.96–4.15), n=27 and genotype populations match their corresponding narrative/table occurrences. Enrolled 30 and completed 27 are explicitly differentiated. Abstract demographic notation is immediately resolved by the detailed count; excluded below. |
| Primary group Bayesian graphics | Figure 2 group estimates compared with p.4 exact Bayesian values and Figure 3 distributions after matching genotype, analysis set, contrast and measure; F-XS-001. |
| Individual primary results | All 27 Figure 2 patients matched to eTable 3. Hierarchical shrinkage and independent interim estimates are different models. Patient 11's explicit no-stiffness exception resolves continuation/advice observations. |
| Secondary narrative, Table 2 and eFigure 2 | IVR pain/weakness/tiredness probabilities 45%/87%/74% reconcile across reported locations; corresponding Bayesian and frequentist estimates remain separate. All other narrative effect/interval/interaction copies match corresponding Table 2 rows. Peripheral descriptive comparisons screened below. |
| Flow, treatment sets, safety and follow-up | 30 randomized, 3 dropouts, 27 completed, 23 one-set and 4 two-set patients, 31 sets, 24 continuing-treatment patients, GI discomfort 21/30 versus 1/30 and one serious reaction reconcile across main/results supplement. |
| Endpoint definition and timing | Primary IVR stiffness, >0.75 clinically meaningful threshold, final two-week frequentist observation window, four-week treatment periods, 1–4 sets and one-week interperiod washout compared with protocol summary, endpoint sections, assessment schedule and diagrams. Non-key physiologic differences and unreported Bayesian time filtering screened below. |
| Bayesian model and covariates | Protocol pp.40–42 compared with main p.3 and eMethods 1–3: common within-person variance and hierarchical genotype analysis represented. Explicit variance-prior family changes yield F-XS-002. Center, treatment-order/pair investigations, clinical prior sensitivity and sequential updating are treated separately from contradictions; exclusions below. |
| Analysis population and missingness | Protocol intention-to-treat/all pretermination data versus report at-least-one-period eligibility/all available data and observed 27-person analysis assessed; unavailable dropout observations/consent status prevent a categorical contradiction. Report says missing at random and no multiple imputation; protocol supplies no incompatible imputation rule. |
| Sample size and power | Planned n=30, 1000 replicates, 0.75 threshold and prior-averaged expected posterior probabilities assessed against explicitly post hoc 30-patient stopping simulation, 14 observations/arm, fixed effect 1.75, 68.5% power/69% rounded and −0.46 bias. Different calculations and disclosure resolve numerical contrasts. |
| Interim, stopping, margins and multiplicity | Individual advisory >80%/<20% stopping reviewed against protocol ≥80%/≤20% with displayed rounding. No noninferiority/equivalence margin is established. Report declares two-sided frequentist P<.05 and exploratory unadjusted secondary outcomes; protocol supplies no conflicting multiplicity rule. Plan-internal group safety decision F-XS-003. Individual drug-level advice assessed without assuming the timing of unavailable advice. |
| Background/administration/data sharing | All mapped historical and administrative pages retained as outside current-result comparison; DOC-004 has no quantitative analysis/design claim. No scientific coverage gap. |

## Findings

### F-XS-001

**Observation:** The CLCN1 primary Bayesian group estimate and interval in Figure 2 do not align with the numerical result to which the narrative refers.

**Exact locations and roles:** REPORT [main p.4, Primary Outcome Measure, genotype treatment effects](../../../jama_stunnenberg_2018_oi_180136.pdf#page=4); REPORT [main p.5, Figure 2, right-hand dark-blue CLCN1 group marker, interval and caption](../../../jama_stunnenberg_2018_oi_180136.pdf#page=5). REPORT [main p.6, Figure 3A and caption](../../../jama_stunnenberg_2018_oi_180136.pdf#page=6) corroborates the narrative distribution but is not an additional conflicting relationship.

**Printed values and comparison logic:** The narrative reports CLCN1 n=16 mean reduction 3.84, 95% CrI 2.52–5.16, explicitly referring to Figure 2 and Figure 3A. Figure 2 labels the quantity reduction in IVR stiffness score, mean and 95% CrI; its group legend gives CLCN1 n=16, and its caption states genotype estimates borrow information from all patients. The dark-blue group marker is between 3.5 and 3.6 and its upper interval endpoint below 4.9, rather than near 3.84 and 5.16. These are conservative visual bounds, not invented exact plot coordinates. The numerical point rounding interval [3.835,3.845] cannot intersect [3.5,3.6]; the numerical upper-limit interval [5.155,5.165] cannot intersect the plotted bound below 4.9. All populations, primary endpoint, placebo-minus-mexiletine direction and Bayesian interval labels match. The Figure 3A dark-blue density peaks near 3.8, which does not explain the Figure 2 group value.

**Focus area:** B. **Proposed review domain:** `statistical_results`. **Proposed relationship:** `S_W`.

**Affected result or extracted value:** Primary CLCN1 Bayesian mean stiffness reduction and its 95% credible interval; the graphic and narrative supply differing effect magnitudes/interval limits for extraction.

**Why context does not resolve it:** The immediately surrounding caption does not assign the group marker a different analysis, population or estimand; the narrative explicitly cites that plot for its numerical estimate. The difference exceeds printed numerical precision and conservative graphical reading uncertainty.

**Supported alternatives:** The graphic could represent a separate model output or the narrative could represent a later output; neither is identified in the supplied caption. Figure 3A supports the narrative magnitude. The exact underlying graphic coordinates are unavailable.

**Human verification steps:** Inspect the dark-blue marker and endpoints against the 1-point y-axis ticks; verify that the right-hand marker is the CLCN1 group rather than patient 29. Compare the exported group plot data and numerical Bayesian summary, including model version and analysis population. Determine which output Figure 2 is intended to display.

### F-XS-002

**Observation:** The supplied report model code uses a different variance-prior family from the prospective Bayesian analysis specification.

**Exact locations and roles:** PLAN [protocol p.40, Bayesian hierarchical model and prior specification](../../../joi180136supp1_prod.pdf#page=40) and PLAN [protocol p.41, noninformative variation priors](../../../joi180136supp1_prod.pdf#page=41); REPORT [eMethods 1 p.10, individual interim model](../../../joi180136supp2_prod.pdf#page=10); REPORT [eMethods 2 p.11, population model](../../../joi180136supp2_prod.pdf#page=11); REPORT [eMethods 3 p.13, genotype model](../../../joi180136supp2_prod.pdf#page=13). REPORT [main p.3, Bayesian Analysis and pointers to eMethods 1–3](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3) identifies their result-producing roles.

**Printed values and comparison logic:** Protocol p.41 states that variation parameters will use inverse-gamma distributions with shape and scale both 0.001; p.42 specifies noninformative priors for individual interim analyses. Report eMethods 1 instead gives sigma_plac and sigma_mex ~ dunif(0.01,10), with tau=1/sigma². Both population and genotype models give sigma.within, sigma.mex and sigma.plac ~ dunif(0.01,10), again with tau=1/sigma². A uniform standard-deviation prior implies variance support 0.0001–100 and density proportional to v^(−1/2) on that support. It does not equal an inverse-gamma(0.001,0.001) prior on variance, which has positive unbounded support. This is a distributional specification contrast, not a rounding or notation difference. One finding consolidates the repeated variance-prior pattern across individual, population and genotype models. No numerical result change is asserted or computed.

**Focus area:** D. **Proposed review domain:** `protocol_report`. **Proposed relationship:** `P_R`.

**Affected result or extracted value:** The prespecified versus reported Bayesian analysis underlying individual primary stopping probabilities, overall stiffness reduction 3.06 (95% CrI 1.96–4.15), CLCN1 reduction 3.84 (2.52–5.16), SCN4A reduction 1.94 (0.35–3.53), and their meaningful-effect probabilities.

**Why context does not resolve it:** Both specifications concern the analysis priors for variation parameters. Calling each noninformative does not make their mathematical distributions identical. No supplied amendment or local explanation reconciles the changed prior family, which is an explicit analysis specification rather than an omission.

**Supported alternatives:** A documented analysis amendment could authorize the uniform-SD priors; the published code could be a simplified illustration rather than the executed code. The package supplies neither an amendment nor a statement distinguishing illustrative from executed variance priors. Planned clinical-mean-prior sensitivity reporting is a separate unreported detail, screened below.

**Human verification steps:** Confirm the executed prior definitions for interim, population and genotype analyses, the parameterization of each distribution, and any approved amendment. Identify the model run underlying each primary result. No preferred prior is proposed.

### F-XS-003

**Observation:** The group DSMB convening rule has different event definitions in the protocol text and its decision figure.

**Exact locations and roles:** PLAN [protocol p.38, section 8.4 final paragraph](../../../joi180136supp1_prod.pdf#page=38); PLAN [protocol p.39, Figure 3, Adverse reactions/events item 2](../../../joi180136supp1_prod.pdf#page=39). Both are prospective PLAN content within one protocol.

**Printed statements and comparison logic:** The paragraph requires convening/review when accumulated serious adverse events deemed study-related are equal to or more than 10% (three patients), or when two or more of the same cardiac event (AE/SAE) occur. The figure instead names cardiac events (AE/SAE) in more than 10% (three patients), or two or more of the same cardiac event. The shared repeated-cardiac-event branch agrees, but the cumulative branch changes from all study-related serious events to cardiac events including nonserious events. Those event sets are not interchangeable. The greater-than versus inclusive threshold is recorded with the event-definition pattern; the printed three-patient parenthesis could resolve the boundary but cannot resolve the different event set. The comparison establishes a plan decision-rule inconsistency; it does not assert that any trigger occurred in the completed trial.

**Focus area:** D. **Proposed review domain:** `plan_material`. **Proposed relationship:** `P_P`.

**Affected result or extracted value:** The extracted prospective aggregate safety stopping/review criterion for the 30-participant trial, including whether cumulative noncardiac study-related serious events or nonserious cardiac events belong to the three-patient trigger. The completed study reports one serious skin reaction and no clinically relevant cardiac abnormalities, so no actual stopping consequence is inferred.

**Why context does not resolve it:** Figure 3 is explicitly introduced as more detailed DSMB decision guidance. Neither local location supplies precedence or identifies the figure's cardiac branch as an additional rule alongside the text's all-serious-event branch. The event set changes a planned decision rule even if the numerical threshold is read as three patients.

**Supported alternatives:** The text could give the general cumulative serious-event rule and the figure an additional cardiac rule; alternatively the figure could be intended to restate the text. These readings imply different prespecified review triggers. No adjudicated interpretation is supplied.

**Human verification steps:** Read both cumulative-event branches, distinguish the shared two-identical-cardiac-events branch, and check the operative DSMB charter or protocol amendment for event definitions and the inclusive threshold. Confirm whether the rules were intended to be cumulative or alternatives.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT main pp.1,4; eTable 2 pp.3–4 | Abstract 22% men versus detailed 22 men/8 women; count and roster immediately identify the intended demographic quantity. | NOTATION_OR_TYPOGRAPHY |
| REPORT main p.4; Figure 2 p.5; eTable 3 p.5 | Enrolled 19/11 genotypes versus analyzed 16/11, and 30 versus 27 participants, explicitly reflect enrolled versus completing populations. | CONTEXT_RESOLVES |
| REPORT main Table 1 p.5; eTable 2 pp.3–4 | Baseline subgroup summaries, previous medications and individual IVR distributions are peripheral descriptive cross-document comparisons. | PERIPHERAL_COMPARISON |
| REPORT main pp.1–4; PLAN pp.44–46 | Recruitment/enrollment calendars and center numbers differ; no primary result, analysis-population size or decision rule is changed by these administrative comparisons. | PERIPHERAL_COMPARISON |
| REPORT Figure 2 p.5; eTable 3 p.5; eMethods 1/3 pp.10,13 | Individual plot intervals versus interim table intervals, including patient 11's wide interval, compare hierarchical borrowing with independent individual-interim models. | NOT_REPRODUCED |
| REPORT main p.4; eTable 3 p.5; PLAN pp.42–43 | Patient 11 has 38% rather than <20% probability but explicitly stopped because stiffness was absent on both treatments; advisory stopping and the footnote resolve the exception. | CONTEXT_RESOLVES |
| REPORT eTable 3 p.5; main p.3; PLAN p.42 | Patients 8/20 show rounded 80%; >80% versus ≥80% does not establish differing decisions with underlying unrounded probabilities unavailable. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT Figure 3C p.6; main p.4; PLAN p.43 | Sequential subgroup curves use subgroup-sized accumulations; comparing their terminal probabilities directly with genotype estimates informed by all 27 patients requires assuming the same information set. Descriptive evidence after 11 patients is not a claim of stopping the aggregate study. | CONDITIONAL_OR_UNREPORTED |
| REPORT eMethods 2/3 pp.11–14 | Reversed arm labels in individual-mean glossary lines and SCN4A in the CLCN1 difference glossary are immediately resolved by code, data-arm definitions and explicit genotype equations. | NOTATION_OR_TYPOGRAPHY |
| REPORT eMethods 4 p.15 | References to eMethods 2 for individual simulation and eMethods 3 for group simulation are footnote/pointer comparisons. | PERIPHERAL_COMPARISON |
| REPORT main p.3; eMethods 4 pp.15–17; PLAN pp.19–21 | 69% versus 68.5% power is rounded; prospective expected posterior probabilities 0.782–0.821 and post hoc power 68.5% are explicitly different simulation criteria/designs. | CONTEXT_RESOLVES |
| REPORT main p.3; eMethods 1–3; PLAN pp.40–42 | Clinical mean-prior sensitivity results and posterior-to-prior sequential updating are not reported as completed; omission alone does not establish a replaced prespecified analysis. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p.3; eMethods 2/3; PLAN p.40 | Center covariate planned but trial explicitly single-center; treatment-order/pair tests are reported in frequentist reanalysis, while unreported Bayesian interaction details alone establish no contradiction. | CONDITIONAL_OR_UNREPORTED |
| REPORT main pp.3–4; PLAN p.35 | At-least-one-period eligibility and 27 analyzed completers versus intent-to-treat pretermination data: dropout treatment observations and consent-withdrawal status are unavailable; a different eligible dataset cannot be established. | CONDITIONAL_OR_UNREPORTED |
| REPORT main pp.3–4; PLAN pp.14,19,31,35 | Final-two-week primary definition agrees with frequentist analysis; exact Bayesian observation filtering and any protocol imputation rule are unreported, preventing an established conflicting timing/missingness specification. | CONDITIONAL_OR_UNREPORTED |
| REPORT main pp.1–2; PLAN pp.7,12–14,22 | 600 mg/day versus first-two-day titration is an abbreviated steady-dose description; no statement establishes that titration was omitted. A longer prebaseline washout does not contradict minimum drug-specific washouts. | CONTEXT_RESOLVES |
| REPORT main pp.3,7–8; PLAN pp.32–34 | Three versus five-second bedside contractions and 90%–10%/50%/75% versus 90%–5% grip endpoints concern secondary physiologic outcomes not abstract-reported or designated key secondary. No primary/key secondary effect or planned decision changes. | PERIPHERAL_COMPARISON |
| REPORT main pp.2,8; eTable 1 p.2; PLAN pp.18–19 | Broad cardiac/psychiatric descriptions versus detailed specific exclusion lists are resolved by the eligibility-table pointer; comorbidities alone do not establish ineligibility under those specific rules. | TERMINOLOGY_OR_WORDING |
| REPORT main p.8; PLAN Figure 3 p.39 | Patient 4 subtherapeutic level 0.11 μg/mL and advice to stop for 0–0.25 μg/mL do not establish when the level was available to the DSMB; report explicitly analyzes random serum levels at trial end. | CONDITIONAL_OR_UNREPORTED |
| REPORT main pp.8–9 | Preference 26/31 treatment sets (84%) abbreviated as patients preferring mexiletine is immediately resolved by the detailed set-denominator statement; it is peripheral to primary/key secondary results. | PERIPHERAL_COMPARISON |

## Limitations and derivative provenance

No scientific source-coverage gap remains in this assigned check. Graphs do not supply exact coordinate tables; F-XS-001 uses conservative visual bounds, not high-precision digitization. The missing executed analysis files, dropout treatment observations, clinical-prior sensitivity output, amendment and DSMB charter limit causal interpretation and claims about actual rule application. Neither missing material nor differing simulation objectives is treated as a contradiction alone.

Direct source authority was reread using available Poppler pdftotext 25.03.0, selected pages streamed to standard output. Two targeted direct renders were created and visually inspected with Poppler pdftoppm 25.03.0: `preprocessing/xs-main-page5.png` from DOC-001 p.5, maximum dimension 2200 pixels, and `preprocessing/xs-plan-page39.png` from DOC-002 p.39, maximum dimension 1800 pixels. Commands used `-f N -l N -singlefile -scale-to SIZE -png SOURCE OUTPUT_PREFIX`. Reused page images were used only as locator/visual aids for DOC-001 pp.5–6, DOC-002 p.39 and DOC-003 p.5. No OCR, external web, GPU, unauthorized Python helper, source modification or reused-asset modification occurred.
