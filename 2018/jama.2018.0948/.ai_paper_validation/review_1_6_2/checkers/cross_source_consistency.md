# Cross-source consistency review — Workflow 1.6.2

Runtime agent ID: 01a129b8-3f5d-7cd0-8dc6-3c2fc4520907. Role: cross_source_consistency_reviewer; gpt-6.1-sol / medium; fresh spawn. Scope: all matched REPORT–REPORT, PLAN–REPORT and relevant PLAN–PLAN relationships across DOC-001 pp.1–11, DOC-002 pp.1–37, DOC-003 pp.1–7 and DOC-004 pp.1–14. Sources and legacy assets were preserved. No old scientific conclusions or external evidence were read. Complete scope and review contract were read, together with canonical main and support maps. No shard appendix was treated as an additional source.

Direct confirmation used Poppler pdftotext 25.03.0, CPU, `pdftotext -layout SOURCE OUTPUT` for each of the four supplied PDFs. Unique derivatives are preprocessing/cross-main.txt, preprocessing/cross-protocol.txt, preprocessing/cross-sap.txt and preprocessing/cross-results.txt. These retain physical PDF form-feed boundaries. Direct source text, rather than previous conclusions, establishes the findings below; visual/mechanical recheck remains an independent stage. Relative evidence links resolve from this checker directory to supplied PDFs.

## Coverage and matched comparison record

| Scope | Comparisons completed and result |
|---|---|
| Primary mortality | Abstract, Key Points, narrative, Table 3, Figure 2, eFigure 1 and eTable 2 match counts, rates, adjusted OR/RD and null conclusion. Primary population includes eligible ward exposure and DNR deaths in plan and report. Planned model changes are recorded below. Figure line-style descriptions were self-screened separately. |
| Main secondary deterioration | Abstract, narrative, Table 3 and eTable 3 match 127/259 events, 0.50/0.84 per thousand patient-days, RR 0.77 (0.61–0.97), P=.03 and RD −0.34 (−0.73–0.05). Composite components were compared item by item against protocol Table 5; changes are recorded below. |
| Documentation | Table 2 and eFigure 2 match last-set denominators 2588/2832 and ≥5 completeness. Every individual observation type, model covariate and reported significance claim was matched. Planned all-seven/all-set endpoint differs as recorded below. Unadjusted P values were distinguished from Holm values. |
| Other report relationships | Calls, urgent consultations, preventable arrests, ICU mortality and ICU resource use were matched by unit and analysis population across narrative, Table 3 and eTables 1–4. ICU admission events were distinguished from per-patient ICU records; 686+967=1653 and cross-period exclusions match SAP. Predicted mortality probabilities were distinguished from mean PIM scores and their nonlinear transformation. |
| Outcome hierarchy | All protocol clinical, process and resource outcomes and SAP shell rows were checked against main methods/Table 3 and result-supplement definition/result tables. Status differences are consolidated below. Survey omissions alone are peripheral secondary outcomes. |
| Analysis models | Protocol primary/secondary logit, Poisson and linear specifications, weighting, covariates and strata were compared with all SAP links and main analysis descriptions. Primary replacement and main-secondary baseline adjustment are recorded below. Individual ICU aggregation and first-admission ventilator-free days agree between SAP and report. |
| Subgroups and sensitivities | All four protocol subgroups, both SAP subgroup interaction plans and all eight relative-scale/five absolute-scale sensitivities were checked against the complete report and results supplement. Reporting omissions affecting primary/key-secondary analyses are recorded below. |
| Population/criteria | Hospital and patient inclusion/exclusion criteria were compared item by item: ward exposure, NICU/PICU exclusions, anesthetist-controlled areas, high-dependency staff responsibility, ED documentation, preterm age, age limit, prior score use, planned new MET, and randomization acceptance. No demonstrated analysis-population size conflict remains. |
| Intervention/time | Four PEWS components, control care, 26-week baseline, 5-week run-in, subsequent 52-week intervention and extensions were matched. Education timing descriptions and operational threshold wording were screened by the scope tiers. |
| Missingness/design rules | Anticipated hospital attrition versus two withdrawn hospitals, period-end discharge convention, no event follow-up loss, ICU cross-period patient exclusion, repeat-admission aggregation and 28-day VFD definition were checked. No imputation rule is prospectively specified that conflicts with a printed reported result. No noninferiority/equivalence margin, efficacy/futility stopping boundary or prespecified multiplicity rule is supplied; main two-sided .05 and post hoc Holm are coherent. No interim outcome analysis is planned or reported; DSMC safety/implementation reviews are separate. |
| Power and plan internal | Main, protocol summary/body/appendix and eTable 5 were matched for baseline mortality, 20 analytic clusters/22 recruited, power .80, alpha .05, k .15, occupancy .90, LOS4 and target reductions. Appendix absolute reduction is recorded below. Historical validation/background values were distinguished from trial results; administrative copies do not alter the target analyses. |

## Findings

### F-XS-001 — Main-secondary composite differs across the protocol and report definitions

**Locations and roles:** PLAN [protocol Table 5, p.24](../../../joi180015supp1_prod.pdf#page=24), with PLAN [definition pp.10–11](../../../joi180015supp1_prod.pdf#page=10); REPORT [main Study Outcomes, p.4](../../../jama_parshuram_2018_oi_180015.pdf#page=4); REPORT [eTable 1, p.6](../../../joi180015supp3_prod.pdf#page=6). Affected result occurrences: REPORT [abstract p.1](../../../jama_parshuram_2018_oi_180015.pdf#page=1), [Table 3 p.7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), [eTable 3 p.11](../../../joi180015supp3_prod.pdf#page=11).

**Printed statements and comparison:** Protocol category 4, included in SCDE, requires >60 mL/kg fluid in the prior 12 h **and** vasoactive medication. Main p.4 lists vasoactive medication **or** ≥60 mL/kg fluid as independently sufficient components. Results eTable 1 uses >60 mL/kg **and/or** vasoactive medication. Protocol death category 7 requires ward death with no transfer; both report definitions additionally include death in the first ICU hour. Thus the circulatory conjunction becomes a disjunction, the main cutoff includes exactly 60, and the death component expands into the ICU. Category 3 respiratory and category 6 CPR/ECMO windows were matched separately and do not resolve these differences. This is one changed composite-definition pattern, not separate findings for each component. Logical set membership, rather than rounding arithmetic, reproduces it.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R, S_C.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Main secondary SCDE event counts 127 versus 259 and RR 0.77 (95% CI 0.61–0.97), P=.03; an extractor must know which composite defines these events.

**Why context does not resolve it:** A changed prespecified composite is always registered. The supplied materials do not identify a prospective amendment or show which rule generated the events.

**Supported alternatives:** The protocol table may represent an earlier operational definition; report components may reflect a later expansion; the main fluid boundary may summarize the supplement. These alternatives cannot establish the implemented rule from supplied aggregate data.

**Human question:** Which circulatory conjunction/fluid threshold and death-location window defined the analyzed SCDE composite, and where is any corresponding prospective amendment documented?

### F-XS-002 — Planned outcome status differs from reported status in a repeated pattern

**Locations and roles:** PLAN [protocol clinical secondaries pp.11–12](../../../joi180015supp1_prod.pdf#page=11), [process outcomes p.12](../../../joi180015supp1_prod.pdf#page=12), [analysis p.16](../../../joi180015supp1_prod.pdf#page=16); PLAN [SAP shell table p.5](../../../joi180015supp2_prod.pdf#page=5); REPORT [main Study Outcomes p.4](../../../jama_parshuram_2018_oi_180015.pdf#page=4), [Table 3 and footnote g p.7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), [eTable 4 p.12](../../../joi180015supp3_prod.pdf#page=12).

**Printed statements and comparison:** Protocol explicitly lists potentially preventable cardiac arrest, hospital/ICU readmission, immediate physician calls, resuscitation-team calls and urgent ICU consultations as secondary outcomes. Table 3 places each under “Post hoc Outcomes”; footnote g calls all ten displayed analyses exploratory. Main p.4 itself says these outcomes are prespecified. Main p.4 calls the PIM2 admission **score** not prespecified, whereas protocol p.16 explicitly plans a linear-regression analysis of the PIM2 score, and eTable 4 reports that score. SAP p.5 also explicitly includes urgent ICU admission although the main calls it not prespecified; the protocol does not name the urgent-admission rate as an outcome, so this occurrence carries plan-timing ambiguity. This finding consolidates the common planned-status versus reported-status pattern. It does not equate overall ICU mortality with ward-origin urgent-ICU mortality or claim that all ten Table 3 outcomes were in the original protocol.

Additional occurrence: main p.4 includes mortality without DNR among the21 other prespecified outcomes, while Table3 places that row under “Primary Outcome” alongside all-cause mortality. The protocol's sole named primary endpoint is all-cause mortality including DNR ([PLAN p.10](../../../joi180015supp1_prod.pdf#page=10)). A primary-family sensitivity analysis is a supported alternative to an actual status elevation, but the displayed hierarchy does not name it as a sensitivity analysis. This occurrence is retained in the same status pattern for independent screening.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R, S_W.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecification and hierarchy of the named Table 3 results and the PIM2 score comparison 0.13 (95% CI −0.11–0.37), P=.29; these statuses affect interpretation of exploratory versus planned evidence.

**Why context does not resolve it:** Prespecified outcome-status changes are always registered. “Exploratory” can describe inferential intent, but “Post hoc Outcomes” also conveys timing, and the supplied documents do not delimit whether it refers to added models or changed outcomes.

**Supported alternatives:** Prespecified endpoints may have been analyzed with post hoc models/multiplicity treatment; the SAP may document an analysis added after the original protocol. Its supplied copy has no date establishing prospective status. PIM predicted mortality and PIM score are distinct, but protocol p.16 names the score itself.

**Human question:** Which named outcomes and analyses were prospectively specified, and does the Table 3 post hoc designation refer to outcomes, models, multiplicity treatment, or all three? What establishes the prospective status of the PIM2-score and urgent-admission analyses?

### F-XS-003 — Planned subgroup analyses are explicitly not reported

**Locations and roles:** PLAN [protocol p.16](../../../joi180015supp1_prod.pdf#page=16); PLAN [SAP p.6](../../../joi180015supp2_prod.pdf#page=6); REPORT [main Data Analyses p.5](../../../jama_parshuram_2018_oi_180015.pdf#page=5). Full REPORT supplement [pp.1–14](../../../joi180015supp3_prod.pdf#page=1) contains no subgroup-result display.

**Printed statements and comparison:** Protocol says four subgroups will be performed: hospital size <200/≥200 beds, presence/absence of MET, ECMO service, and ward-initiated urgent PICU admission. SAP explicitly plans ECMO/MET subgroup treatment estimates and a GEE treatment-by-subgroup interaction. Main says four planned subgroup analyses, including rapid-response-team presence, are “not reported herein.” Complete report inspection confirms no subgroup estimates or interaction results are supplied. This is one omitted planned subgroup-analysis pattern; the SAP narrower list does not supply the absent results.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Planned subgroup characterization of the primary all-cause mortality treatment effect and main-secondary SCDE treatment effect; treatment-by-service interactions promised in the SAP.

**Why context does not resolve it:** A planned primary/key-secondary analysis not reported is always registered. Disclosure of nonreporting does not supply the planned estimates.

**Supported alternatives:** Subgroup analyses may have been performed for a separate report, or dropped because of sparse clusters. The main explains removal of the size stratification from adjustment, but provides no subgroup-result set. The plan does not restrict ECMO/MET subgroup testing to peripheral outcomes.

**Human question:** Were the four protocol subgroups and SAP ECMO/MET interactions performed for primary/key-secondary outcomes, and where can the estimates, intervals and interaction tests be found, or the prospective change be identified?

### F-XS-004 — SAP model-choice sensitivity analyses of primary/key-secondary effects have no supplied results

**Locations and roles:** PLAN [SAP pp.4–5](../../../joi180015supp2_prod.pdf#page=4); REPORT [main Data Analyses pp.4–5](../../../jama_parshuram_2018_oi_180015.pdf#page=4), [primary/main-secondary results pp.6–7](../../../jama_parshuram_2018_oi_180015.pdf#page=6); REPORT [complete results supplement pp.1–14](../../../joi180015supp3_prod.pdf#page=1).

**Printed statements and comparison:** SAP “Sensitivity to model choice” states that models for ORs, probabilities and rate ratios “were also run” using eight relative-scale specifications and five probability/rate specifications. These include post-only GEE/GLMER, pre/post treatment-time GEE/GLMER, baseline-adjusted GEE/GLMER, inverse-variance weighted linear and quasi-likelihood alternatives. Report supplies the baseline-adjusted GEE primary/secondary effects and selected fallback differences but no estimates or robustness summary across the stated sensitivity set. Full report/results-supplement inspection was used to confirm absence; this is not a search limited to a single paragraph. The supplied SAP is PLAN by content despite retrospective tense.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Robustness of primary mortality OR1.01/RD0.01 and main-secondary SCDE RR0.77/RD−0.34 to the explicitly listed analysis models.

**Why context does not resolve it:** The SAP documents analyses for the effect measures used by primary/key-secondary outcomes; the absence of these planned sensitivity results qualifies by category 5. No missing model detail is assumed to generate a numeric contradiction.

**Supported alternatives:** The retrospective SAP may describe completed, supplementary analyses rather than a prospective specification, or sensitivity results may exist outside this package. The date/sequence of the supplied SAP is not established.

**Human question:** Which of the listed sensitivity analyses applied to the primary and main-secondary results, what were their estimates and intervals, and when was this sensitivity plan specified?

### F-XS-005 — Protocol primary analysis is replaced by the reported GEE specification

**Locations and roles:** PLAN [protocol p.16](../../../joi180015supp1_prod.pdf#page=16); PLAN [SAP pp.1–2](../../../joi180015supp2_prod.pdf#page=1); REPORT [main Data Analyses pp.4–5](../../../jama_parshuram_2018_oi_180015.pdf#page=4), [Table 3 p.7](../../../jama_parshuram_2018_oi_180015.pdf#page=7).

**Printed statements and comparison:** Protocol primary analysis regresses the **logit of the proportion dying in each hospital**, with intervention, baseline logit and hospital-size stratum, weighted by hospital size. SAP specifies binomial GEE on event/non-event counts with intervention and baseline logit, exchangeable hospital clustering, and no size-stratum predictor. Main reports that GEE specification and states the size stratification was removed because only three hospitals were in the large stratum. The planned weighted hospital-logit regression is not supplied as a primary or sensitivity result. This finding concerns a replaced primary specification, not whether GEE is preferable. SAP/report coherence does not supply results under the protocol specification or establish a prospective amendment.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R, P_P.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Primary all-cause mortality OR1.01 (95% CI0.61–1.69), P=.96 and corresponding primary interpretation under the protocol-versus-implemented analysis.

**Why context does not resolve it:** Category 5 applies to replacement/nonreporting of the planned primary analysis. The removal of stratification is disclosed, but the protocol hospital-logit regression and reported grouped-binomial GEE are different specifications.

**Supported alternatives:** The SAP may formalize an approved revision; the GEE analysis may be regarded by the investigators as the implementation of broad “logit regression.” Direct inspection identifies different dependent-variable/likelihood and weighting descriptions; no amendment timing is supplied.

**Human question:** Was the protocol weighted hospital-logit/size-stratified primary analysis prospectively replaced by the SAP binomial GEE, and are the original-specification results or a dated amendment available?

### F-XS-006 — Main-secondary absolute-effect analysis omits planned baseline adjustment

**Locations and roles:** PLAN [protocol secondary Poisson specification p.16](../../../joi180015supp1_prod.pdf#page=16); PLAN [SAP count models pp.2–3](../../../joi180015supp2_prod.pdf#page=2); REPORT [main fallback rule p.5](../../../jama_parshuram_2018_oi_180015.pdf#page=5), [Table 3 footnote a p.7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), [abstract p.1](../../../jama_parshuram_2018_oi_180015.pdf#page=1).

**Printed statements and comparison:** Protocol SCDE Poisson analysis includes baseline event rate and hospital-size stratum. SAP identity-link rate-difference model includes baseline rate. Main allows removal of baseline adjustment if an identity-link GEE does not converge; Table 3 explicitly identifies SCDE RD among models not baseline adjusted. Consequently the key-secondary RD −0.34 (95% CI−0.73–0.05), including its abstract appearance, does not come from the baseline-adjusted absolute-effect model specified in the supplied SAP. Its RR0.77 remains baseline adjusted; that separate ratio does not provide the planned absolute-effect analysis. No nonconvergence fallback appears in the supplied SAP. Other exploratory rows with the same fallback are corroborating occurrences, not an additional key-secondary finding.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Main-secondary SCDE absolute effect and 95% CI used in abstract/data extraction.

**Why context does not resolve it:** The replacement is disclosed but the planned key-secondary absolute-effect analysis is not reported; category 5 applies. This finding does not equate the RD interval with the RR-associated P value.

**Supported alternatives:** Nonconvergence may have prevented the planned fit, motivating a documented analysis revision. The report states a general rule but supplies neither a prospective revision nor the planned SCDE absolute-effect fit.

**Human question:** Was removal of baseline adjustment for the SCDE absolute effect prospectively specified, and what fit/convergence facts explain replacement of the SAP baseline-adjusted RD analysis?

### F-XS-007 — Planned all-seven documentation endpoint is replaced by last-set ≥5 completeness

**Locations and roles:** PLAN [protocol documentation analysis p.16](../../../joi180015supp1_prod.pdf#page=16), [measurement p.14](../../../joi180015supp1_prod.pdf#page=14); REPORT [main documentation methods pp.3–4](../../../jama_parshuram_2018_oi_180015.pdf#page=3), [Table 2 p.6](../../../jama_parshuram_2018_oi_180015.pdf#page=6); REPORT [eFigure 2 pp.4–5](../../../joi180015supp3_prod.pdf#page=4).

**Printed statements and comparison:** Protocol plans comparisons of “the number of times that all seven items were documented” across sampled patients. Main explicitly states revision before analysis: instead of evaluating all observation sets, the last one was selected, and threshold reduced from seven to five. Table 2 reports last sets with ≥5, with adjusted difference38.1 percentage points (95% CI20.8–55.4), P<.001. This changes a constructed multi-item endpoint and its measurement/analysis unit; it is more than interchangeable wording for completeness. eFigure2 corroborates the applied last-set definition. Individual vital-sign-frequency outcomes remain separately reported.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Interpretation/extraction of the documentation-completeness effect38.1 percentage points as all-seven documentation versus ≥5 in the last set.

**Why context does not resolve it:** Category 5 applies to the changed prespecified composite definition. Disclosure of the change and its rationale establish what changed but do not remove registration under that category.

**Supported alternatives:** The revised measure may reflect the clinical minimum required to calculate the PEWS score, as the main states; this explains the revision but does not make the endpoint identical to the supplied protocol.

**Human question:** Was the last-set ≥5 documentation endpoint prospectively adopted in a dated amendment, and are results for the planned all-seven/all-set definition available?

### F-XS-008 — Protocol power appendix prints an absolute mortality reduction ten times its body value

**Locations and roles:** PLAN [protocol power p.14](../../../joi180015supp1_prod.pdf#page=14), [appendix p.29](../../../joi180015supp1_prod.pdf#page=29), [summary p.1](../../../joi180015supp1_prod.pdf#page=1). REPORT [main sample size p.4](../../../jama_parshuram_2018_oi_180015.pdf#page=4) corroborates 0.9 per thousand; it is not a conflicting side.

**Printed values and comparison:** Protocol p.14 prints 18% relative reduction, absolute reduction0.09%, baseline5.1 per1000. Appendix p.29 instead prints 18% corresponding to absolute reduction0.9%. Summary prints0.9 deaths per1000. Calculation18%×5.1/1000=0.000918=0.0918%, compatible with0.09%, not0.9%. Half-unit intervals for printed copies0.9% and0.09% are [0.85,0.95]% and [0.085,0.095]%; gap0.755 percentage points divided by0.9=0.8389. Recomputing from18% and5.1 permits [0.088375,0.095275]%; gap from [0.85,0.95]% is0.754725 percentage points, relative0.8386. Both exceed0.05. The appendix reading changes the printed target reduction magnitude, regardless of whether an intended decimal can be inferred.

**Focus area:** D. **Proposed review domain:** plan_material. **Proposed relationship type:** P_P. **All relationships:** P_P.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** Absolute target mortality reduction underlying the 20-cluster/80%-power design and its reproducible extraction from the protocol appendix.

**Why context does not resolve it:** A printed decimal/value slip changing magnitude beyond display precision is always registered. Arithmetic reconstruction does not remove the differing printed reading.

**Supported alternatives:** The appendix may intend0.09%, or0.9 per1000; those alternatives are supported elsewhere but require human confirmation.

**Human question:** Which absolute mortality-reduction value was used in the supplied power calculation, and how should the appendix0.9% reading be interpreted?

### F-XS-009 — Planned ICU-readmission denominator changes between protocol and SAP/report

**Locations and roles:** PLAN [protocol p.12](../../../joi180015supp1_prod.pdf#page=12); PLAN [SAP shell table p.5](../../../joi180015supp2_prod.pdf#page=5); REPORT [main Table 3 and footnote h p.7](../../../jama_parshuram_2018_oi_180015.pdf#page=7).

**Printed statements and comparison:** Protocol states that PICU mortality and unplanned hospital/PICU readmission will be represented per thousand **hospital discharges**. SAP ICU-readmission row instead divides by PatientDischargesICU, and Table 3 uses per thousand **ICU discharges**: 94 events at28.40 in BedsidePEWS and108 at21.25 in usual care. The hospital discharge totals on that same display are50173 and94366; using those planned denominators gives1.874 and1.144 per thousand, rather than28.40 and21.25. This is a change in the denominator/analysis population underlying the planned endpoint, not a copy of peripheral per-time-point observations. No model-versus-crude contradiction is alleged: these are displayed event rates, not the adjusted OR1.11.

**Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R. **All relationships:** P_R, P_P.

**Qualifying route:** Route B.

**Affected result or extracted value:** ICU-readmission rates28.40 and21.25 per thousand and the population/denominator definition for the corresponding endpoint. B1 is a planned-versus-reported endpoint/analysis-population definition; B2 is the unresolved change from the protocol to SAP; B3 is extraction of a different rate quantity.

**Why context does not resolve it:** Report and SAP establish the implemented ICU denominator but do not establish whether/when the prospective hospital-denominator endpoint was revised. The two denominators select distinct discharge populations. The outcome-status pattern in F-XS-002 does not explain this denominator change.

**Supported alternatives:** SAP may supersede an earlier protocol denominator; the protocol sentence may summarize intended denominator families too broadly. An amendment/date is not supplied.

**Human question:** Was the prespecified hospital-discharge denominator for unplanned ICU readmission prospectively changed to ICU discharges, and which denominator defines the intended endpoint for extraction?

## Excluded observations

Only apparent issues considered and not emitted appear here. Reconciled checks are recorded in the coverage table. Route A findings above are not excluded merely because changes were disclosed.

| Location | Observation | Reason code |
|---|---|---|
| [Main Figure 2 p.8](../../../jama_parshuram_2018_oi_180015.pdf#page=8), [eFigure 1 pp.2–3](../../../joi180015supp3_prod.pdf#page=2) | Caption color/line-style descriptions disagree with legends, but group-specific point identities, supplied numeric hospital data and the primary estimate are available; no reversed numerical direction or group-attributed estimate is established by this style difference. | NOTATION_OR_TYPOGRAPHY |
| [Main Figure 2 p.8](../../../jama_parshuram_2018_oi_180015.pdf#page=8), [eFigure 1 p.2](../../../joi180015supp3_prod.pdf#page=2) | Main x-axis says baseline and intervention periods, while caption and supplement identify baseline x/intervention y. Immediate caption resolves intended coordinate; no printed numerical result differs. | CONTEXT_RESOLVES |
| [Protocol pp.9,24](../../../joi180015supp1_prod.pdf#page=9), [main p.2](../../../jama_parshuram_2018_oi_180015.pdf#page=2) | Protocol PICU descriptive footnote mentions routine patients <12 while overall eligibility is <18; report uses pediatric eligible ward patients up to18. This incidental PICU description does not establish a different trial eligibility/analysis set or size. | TERMINOLOGY_OR_WORDING |
| [Protocol p.11](../../../joi180015supp1_prod.pdf#page=11), [p.28](../../../joi180015supp1_prod.pdf#page=28), [main p.7](../../../jama_parshuram_2018_oi_180015.pdf#page=7) | Quality audit visually confirmed the p.11 comparator is ≥4; native text loses its underline. The printed comparator, explicit ratings 4,5,6 and p.28 agree. Apparent >4 mismatch is not reproduced. | NOT_REPRODUCED |
| [Protocol pp.11,27](../../../joi180015supp1_prod.pdf#page=27) | Abstraction legend calls arrest scale ratings4/5 while Table5 and arrest definition use6/7. This is a peripheral plan-internal abstraction pointer, not a competing main/key-secondary endpoint or decision rule. | PERIPHERAL_COMPARISON |
| [Protocol survey pp.13–14](../../../joi180015supp1_prod.pdf#page=13), [main p.4](../../../jama_parshuram_2018_oi_180015.pdf#page=4), [results p.8](../../../joi180015supp3_prod.pdf#page=8) | Frontline/administrator survey results are explicitly not reported. They are other secondary process/resource outcomes, not a planned primary/key-secondary outcome analysis; no changed status/composite is established. | PERIPHERAL_COMPARISON |
| [Protocol p.8](../../../joi180015supp1_prod.pdf#page=8), [main p.5](../../../jama_parshuram_2018_oi_180015.pdf#page=5) | Analytic team intended blinded but main says unblinded. Blinding is a general conduct feature here, with no source-grounded differing statistical specification or result established solely by the difference. | OUT_OF_FOCUS |
| [Protocol pp.7,23](../../../joi180015supp1_prod.pdf#page=7), [main p.2](../../../jama_parshuram_2018_oi_180015.pdf#page=2) | Staff education preparation described three months before run-in versus one-to-two months before implementation; implementation/course descriptions are not a change in the randomized52-week intervention duration or a result-producing statistical rule. | OUT_OF_FOCUS |
| [Protocol p.15](../../../joi180015supp1_prod.pdf#page=15), [main p.4](../../../jama_parshuram_2018_oi_180015.pdf#page=4) | Report does not repeat assumption that early discharged patients are alive/ventilator-free to day28; no competing printed missing-data rule is supplied. | CONDITIONAL_OR_UNREPORTED |

## Limitations

No unmatched scientific source unit remains in this assigned cross-source scope. No individual-level dataset or dated SAP/amendment is supplied; date/sequence alternatives are named in relevant findings rather than assumed. Figure bar heights and fitted curves lack exact printed values and cannot establish additional quantitative discrepancies by pixel estimates. Statistical compatibility and numeric arithmetic within individual displays belong to the independently assigned numeric/statistical lanes. Nine findings and nine excluded observations are handed to independent inclusion screening; no candidate IDs or adjudications are assigned here.
