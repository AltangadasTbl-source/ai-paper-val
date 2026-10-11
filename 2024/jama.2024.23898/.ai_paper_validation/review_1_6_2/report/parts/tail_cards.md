## C008 — Planned Edinburgh primary sensitivity analysis

Pending Human Adjudication.

**Candidate statement:** The SAP prespecifies an Edinburgh-versus-other-centres sensitivity analysis of the primary outcome, but no matching result or documented withdrawal is present in the supplied REPORT material.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN SAP p.15 vs REPORT main pp.5,6,7,9 and subgroup supplement p.2

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-004

**Qualifying route:** Route A, category 5

**Classification rationale:** The prospective SAP sensitivity specification is PLAN, and the published article and results supplement are REPORT. The inconsistency concerns an explicit planned primary analysis without a corresponding report result, giving P_R and protocol_report. Multiple report documents establish the scope of the absence comparison; they do not establish an inter-REPORT conflict. F-ST1-005 independently identified the same issue and was screened as a duplicate of the included finding.

**Classification ambiguity:** There is no document-role ambiguity. Whether the analysis was performed, omitted from publication or withdrawn in documentation outside the supplied package remains unknown.

**Exact source locations:** PLAN [joi240139supp2_prod_1741633738.17362.pdf — PDF p.15, §11.6 primary sensitivity analysis](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=15). REPORT [jama_paterson_2024_oi_240139_1741633738.12862.pdf — PDF p.5, analysis methods and results](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5), [PDF p.6, Table 2 primary estimates](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6), [PDF p.7, robustness discussion](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=7), [PDF p.9, limitations](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=9), and [joi240139supp3_prod_1741633738.18862.pdf — PDF p.2, subgroup eFigure](../../../../joi240139supp3_prod_1741633738.18862.pdf#page=2). The absence check also covered every remaining page of the main article, both pages of the subgroup supplement and [joi240139supp4_prod_1741633738.20861.pdf — PDF p.1, data-sharing statement](../../../../joi240139supp4_prod_1741633738.20861.pdf#page=1), comprising all 13 supplied REPORT pages.

**Source evidence:** SAP §11.6 states that Edinburgh is expected to recruit the largest number of participants and therefore a sensitivity analysis comparing Edinburgh with the other centres will be performed. This is a separate paragraph after the missing-data sensitivity specification. The report presents overall and per-protocol primary estimates, subgroups by intended infusion duration, operation, sex, age and ERAS adherence, and a post hoc actual-duration analysis. None is the named Edinburgh-versus-other-centres sensitivity comparison.

**Reported-versus-comparator:** The comparator is an explicit planned primary sensitivity result. The report contains no corresponding estimate, interval, test or cancellation statement. Adjustment for trial site in the primary model is reported, but a site random effect is a different analysis element from the separately specified sensitivity comparison.

**Reasoning procedure:** Identify the primary-outcome sensitivity paragraph; distinguish its unconditional Edinburgh statement from the preceding condition on missing-data sensitivity; then search the complete REPORT union for a matched site comparison or documented replacement. All planned subgroup and published sensitivity descriptions were compared by factor and analysis purpose, rather than by the generic word sensitivity.

**Calculation:** This is a categorical comparison of planned analysis versus reporting presence. No numeric result is imputed, and half-unit rounding intervals or a relative numeric discrepancy do not apply. The preceding threshold of more than 10% missingness governs its own missing-data analysis; it does not condition the separate Edinburgh paragraph.

**Affected result or extracted value:** Availability of the planned primary GI-3 sensitivity result assessing Edinburgh versus other centres, relevant to the documented robustness of the primary finding.

**Why context does not resolve it:** Route A, category 5 covers a planned primary analysis that is not reported. General trial-site adjustment, other subgroup comparisons and broad robustness statements do not supply this named sensitivity result.

**Alternative source-grounded interpretations:** The sensitivity may have been conducted but omitted from this publication package. The expected recruitment composition may have changed, or the analysis may have been withdrawn in documentation not supplied. The SAP does not condition this analysis on Edinburgh ultimately being the largest recruiter, and no supplied report or amendment explains its removal.

**Mechanical evidence recheck:** The exact SAP paragraph and all cited report locations were found and matched against the supplied PDFs. The complete 13-page REPORT union was independently reread, with no matching Edinburgh comparison found. PLAN/REPORT roles, P_R precedence, protocol_report domain and reproduced evidence state were confirmed. No source transcription or physical-page correction was necessary. The missing materials are the analysis output or a documented change to this plan; actual performance and numerical effect are not established.

**Potential downstream evidence impact:** An evidence extractor could record the primary site-sensitivity analysis as planned but unavailable in this package, rather than treating site adjustment or other subgroup results as its substitute. No effect on the reported primary estimate or clinical conclusion is demonstrated.

## C009 — Discharge and readiness model specifications

Pending Human Adjudication.

**Candidate statement:** Endpoint-specific SAP tables and sample commands specify generalized linear models for medical discharge criteria and patient readiness, whereas the SAP's general instruction and published report specify Cox regression for these time-to-event outcomes.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN SAP pp.14,26,36 vs REPORT main pp.5,7

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-007

**Qualifying route:** Route B

**Classification rationale:** Specific prospective PLAN GLM instructions differ from the explicit REPORT Cox specification, establishing P_R. Within the SAP, the endpoint-specific GLM instructions also differ from the general Cox rule, establishing P_P. P_R takes precedence, yielding protocol_report. Both discharge endpoints are retained in one model-specification pattern.

**Classification ambiguity:** Document roles are clear. The sample commands may be illustrative, and the general Cox instruction may govern final implementation; the supplied material does not state priority between the general and endpoint-specific plan specifications.

**Exact source locations:** PLAN [joi240139supp2_prod_1741633738.17362.pdf — PDF p.14, §11.4 secondary analyses](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=14), [PDF p.26, Tables 13.21–13.22 and model footnotes](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=26), and [PDF p.36, discharge/readiness sample commands](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=36). REPORT [jama_paterson_2024_oi_240139_1741633738.12862.pdf — PDF p.5, time-to-event methods](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5) and [PDF p.7, Table 2 medical-discharge/patient-readiness rows and footnotes c,d](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=7).

**Source evidence:** SAP §11.4 specifies Cox regression for time-to-event outcomes. The endpoint-specific tables for discharge criteria and readiness instead specify generalized linear models. The corresponding sample commands are `meglm Time_medicalcriteria i.IV i.AgeBand i.Male || CentreNo:, vce(robust)` and the analogous command for `Time_readiness`; neither supplies a family or link. The report explicitly identifies Cox regression and hazard ratios, adjusted for age, sex and centre: medical criteria HR 0.99 (0.84–1.17) and patient readiness HR 0.99 (0.83–1.17).

**Reported-versus-comparator:** Published Cox hazard ratios are compared with endpoint-specific planned GLM descriptions, not with a reconstructed crude estimate. The SAP's general Cox paragraph supports the published model class but leaves the separately printed GLM specifications unreconciled.

**Reasoning procedure:** Match the two named endpoints across the general SAP analysis paragraph, their specific dummy tables, their sample commands and the report's Table 2 footnotes. Compare model classes while preserving the explicit sample-code status. Do not infer a GLM distribution, link or effect scale from software defaults, and do not treat the sample commands as evidence of actual execution.

**Calculation:** Model-class membership is categorical. The two exact endpoint-specific GLM specifications differ from the two reported Cox specifications; the SAP also contains a general Cox instruction. No rounded numeric copies are being compared, so half-unit intervals and relative-discrepancy arithmetic do not apply. The published HRs are source context, not recomputed model outputs.

**Affected result or extracted value:** Planned-versus-reported model class underlying the medical-discharge HR 0.99 (0.84–1.17) and patient-readiness HR 0.99 (0.83–1.17).

**Why context does not resolve it:** The report's model is explicit, but a reader reconstructing the planned analysis encounters both Cox and endpoint-specific GLM instructions without a superseding statement. The discrepancy concerns two abstract-listed key secondary analyses and the documented analysis provenance attached to their hazard ratios.

**Alternative source-grounded interpretations:** The general Cox paragraph may govern, with the endpoint-specific tables and expressly sample commands serving as illustrative material. Alternatively, the reporting model may differ from an earlier endpoint-specific instruction. No supplied priority rule or explanatory amendment distinguishes these readings. No preferred model or numerical impact is proposed.

**Mechanical evidence recheck:** Every cited location was found in the exact supplied PDFs. Both GLM table footnotes, both `meglm` commands, the general Cox paragraph and the report's Cox/hazard-ratio labels were matched independently. P_R and P_P relationships, P_R precedence, protocol_report domain and reproduced state were confirmed without transcription correction. Missing materials are the governing plan instruction, intended GLM family/link and final executed commands or explanatory amendment.

**Potential downstream evidence impact:** A data extractor could attach different planned-model descriptions to the two published hazard ratios depending on which SAP instruction is used. The supplied evidence establishes a documentary specification inconsistency, without establishing a numerical change in either estimate or its interpretation of benefit.

## C010 — Planned key-secondary result components

Pending Human Adjudication.

**Candidate statement:** Five groups of expressly planned measurement outputs for abstract-listed key secondary outcomes lack matching results in the supplied REPORT material: GI-2 status at 96 hours, cumulative vomiting and rescue antiemetic dose over 72 hours, nine postoperative EQ visual-analogue summaries, and day-1 weight.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN protocol pp.16,17,18,31 and SAP pp.20,21,22,25,26 vs REPORT main pp.1,4,5,6,7 and complete REPORT union

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-008, F-ST2-002

**Qualifying route:** Route A, category 5

**Classification rationale:** Prospective protocol/SAP component definitions and output displays are PLAN; published article and result-supplement measurements are REPORT. The explicit planned components lack corresponding published outputs, giving P_R and protocol_report. Corroborating plan definitions and multiple report locations do not create additional relationship types. The pass-2 VAS and weight occurrences extend the same absent-component pattern rather than creating separate candidates.

**Classification ambiguity:** Document roles are clear; collection, execution and reporting changes remain unknown. The 72-hour rescue-antiemetic horizon is stated in the protocol and SAP schedule, not in the dose dummy table itself. Disclosed ERAS subgroup criteria do not identify the status of the independently planned descriptive weight display.

**Exact source locations:** The five component groups and their affected locations are listed separately below. Key-secondary status is established by REPORT [jama_paterson_2024_oi_240139_1741633738.12862.pdf — PDF p.1, abstract outcome list](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=1) and [PDF p.4, outcome list](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4); [PDF p.5, results summary](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5) supplies no missing component output. The absence comparison covered the complete main article, the two-page subgroup supplement and [joi240139supp4_prod_1741633738.20861.pdf — PDF p.1](../../../../joi240139supp4_prod_1741633738.20861.pdf#page=1), all 13 REPORT pages.

| Planned component group | Exact PLAN location and planned output | REPORT comparator and distinct published quantity |
|---|---|---|
| GI-2 recovery status at 96 hours | [joi240139supp1_prod_1741633738.16362.pdf — PDF p.16, GI-2 definition](../../../../joi240139supp1_prod_1741633738.16362.pdf#page=16); [joi240139supp2_prod_1741633738.17362.pdf — PDF p.20, Table 13.7](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=20). Both binary status at 96 hours and time-to-event are specified; the planned status display is n(%). | [Main PDF p.6, Table 2 GI-2 row](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6): all-follow-up events 261/256 and time-to-event HR 1.03 (0.86–1.23), without 96-hour status counts/proportions. |
| Cumulative vomiting episodes over 72 hours | [Protocol PDF p.17, PONV measurement](../../../../joi240139supp1_prod_1741633738.16362.pdf#page=17); [SAP PDF p.21, Table 13.12](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=21): cumulative episodes within 72 hours and descriptive summaries. | [Main PDF p.6, daily clinically important PONV](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6): score ≥5 counts 7/16, 5/19 and 5/5 on postoperative days 1,2,3, rather than cumulative vomiting burden. |
| Rescue antiemetic dose over 72 hours | [Protocol PDF p.17](../../../../joi240139supp1_prod_1741633738.16362.pdf#page=17) and [SAP PDF p.11, schedule](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=11) specify the horizon; [SAP PDF p.22, Table 13.13](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=22) specifies intraoperative, postoperative and total dose summaries, with postoperative dose derived as total minus intraoperative dose. | [Main PDF p.6, PONV rows](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6) and [PDF p.7, regular antiemetic prophylaxis counts](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=7) do not supply the planned rescue-dose quantity. |
| Postoperative EQ visual-analogue scale (VAS) | [SAP PDF p.25, Table 13.19](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=25): mean ± SD by arm and overall at baseline and nine follow-up times—postoperative days 1,2,3,4,5,6,7,30,90. | [Main PDF p.4, Table 1](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4) gives baseline VAS 77.7 (18.3), n=269, and 78.1 (18.1), n=266. [PDF p.6, Table 2](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6) gives postoperative utility-index results, not any of the nine follow-up VAS summaries. |
| Day-1 weight / specified fluid-balance measurement | [SAP PDF p.26, Table 13.20](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=26) separately specifies postoperative day-1 weight, mean (SD). [Protocol PDF p.17](../../../../joi240139supp1_prod_1741633738.16362.pdf#page=17) describes IV fluids and preoperative/postoperative weight; [PDF p.18](../../../../joi240139supp1_prod_1741633738.16362.pdf#page=18) gives ERAS compliance timing; [PDF p.31](../../../../joi240139supp1_prod_1741633738.16362.pdf#page=31) defines day-1 weight change as weight approximately 24 hours after anaesthesia, ±6 hours, minus preoperative weight. | [Main PDF p.7, ERAS rows](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=7) gives IV-fluid volumes 3000 (2000–4000) mL in both arms, with other ERAS counts, but no weight/weight-change summary. [Subgroup supplement PDF p.2](../../../../joi240139supp3_prod_1741633738.18862.pdf#page=2) discloses non-predefined ERAS categories and selected criteria, including IV fluids <4 L; it neither supplies nor expressly withdraws the separate day-1 weight display. |

**Source evidence:** Each table row identifies a distinct planned measurement rather than a model detail inferred by the reviewer. The initial finding contains the GI-2 binary status and two PONV components; F-ST2-002 adds the nine follow-up VAS rows and day-1 weight display. All belong to outcome families expressly listed in the abstract: GI-2 recovery, nausea/vomiting, quality of life and enhanced-recovery adherence. The supplied report instead gives the alternative quantities shown above, with no matching designated output elsewhere.

**Reported-versus-comparator:** Five planned component groups have no matching result in the complete REPORT union. The nine absent VAS follow-up summaries are days 1,2,3,4,5,6,7,30,90; baseline VAS is present and is not counted as absent. The day-1 weight display is independently planned, with weight-change/fluid-balance definitions supplying context. All-follow-up GI-2 events, PONV score categories, baseline VAS, utility indices and administered IV-fluid volumes cannot provide the corresponding missing component values.

**Reasoning procedure:** First establish key-secondary status from the abstract. Match each planned component by instrument or measurement, time horizon and intended summary to every published report page. Preserve each distinct planned quantity when considering a nearby alternative display. Confirm all five component groups individually, then consolidate the common absent-component reporting pattern. The reported ERAS subgroup definition is considered as context without treating a disclosed subgroup rule as withdrawal of the separate planned weight summary.

**Calculation:** Nine postoperative VAS times are seven daily assessments plus days 30 and 90: 7+2=9. The five component groups are binary GI-2, vomiting episodes, rescue dose, follow-up VAS and day-1 weight. These are categorical output-presence comparisons; no absent value is assigned zero, and half-unit rounding intervals or relative numeric discrepancy do not apply. Numeric reconstruction would require the missing 96-hour event counts/denominators, vomiting/dose records, nine VAS summaries and day-1 weight observations. Weight change also requires paired preoperative/postoperative weights and measurement times; IV-fluid volume and BMI do not provide these inputs.

**Affected result or extracted value:** The 96-hour GI-2 recovery proportion; 72-hour vomiting burden and rescue antiemetic dose; postoperative VAS means/SD at all nine planned times; and the day-1 weight measurement relevant to the specified ERAS fluid-balance component.

**Why context does not resolve it:** Route A, category 5 covers explicitly planned primary or key secondary analyses/results that are not reported. The published replacement quantities have different definitions, instruments or horizons and do not supply these planned component outputs.

**Alternative source-grounded interpretations:** Components may have been collected or analyzed but selected out of the clinical publication, relocated outside the supplied package, or withdrawn in documentation not supplied. EQ measurements may also contribute to the separately described economic analysis, but the SAP expressly specifies a VAS display. The subgroup supplement transparently defines its chosen ERAS categories; this does not establish that postoperative weight was uncollected or that its independent descriptive display was withdrawn. No actual collection failure, omission mechanism or subgroup-estimate change is inferred.

**Mechanical evidence recheck:** Initial and fresh pass-2 rechecks located and matched every component definition, dummy-table heading, VAS follow-up time and cited report comparator against the supplied PDFs. The expanded recheck independently confirmed absence in all 13 REPORT pages, including all nine VAS rows and day-1 weight, and visually confirmed the added protocol locations. The antiemetic horizon was traced to protocol p.17 and SAP p.11 rather than inferred from Table 13.13. All roles, P_R classification, protocol_report domain and reproduced evidence state were confirmed without source transcription correction. Missing outputs, participant-level measurement records and unprovided reporting changes limit explanation and numerical reconstruction.

**Potential downstream evidence impact:** An extractor could lack the named recovery proportion, PONV burden/dose, follow-up VAS or weight summaries, or substitute a different measurement for one of them. This is a bounded concern about availability and quantity matching; no change in a treatment conclusion or effect estimate is demonstrated.

## C011 — GI-2 and GI-3 survival time origin

Pending Human Adjudication.

**Candidate statement:** Plan endpoint prose uses surgery/operation start as the GI-2 and GI-3 time origin, whereas the SAP survival-variable definitions use the start of general anaesthesia.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol p.16 and SAP pp.9,33 vs PLAN SAP p.34

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-009

**Qualifying route:** Route B

**Classification rationale:** Both conflicting time-origin specifications are prospective PLAN content, yielding P_P and plan_material. The report's surgery wording corroborates the operation-based side and identifies the affected published results, but does not establish the executed timestamp construction. It therefore adds no P_R or inter-REPORT relationship.

**Classification ambiguity:** Document roles are clear. Loose wording in the sample-variable description versus an intended distinct analytic origin remains unresolved; actual timestamp construction is not supplied.

**Exact source locations:** PLAN [joi240139supp1_prod_1741633738.16362.pdf — PDF p.16, GI-2/GI-3 endpoint definitions](../../../../joi240139supp1_prod_1741633738.16362.pdf#page=16); [joi240139supp2_prod_1741633738.17362.pdf — PDF p.9, endpoint prose](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=9), [PDF p.33, binary composite definitions](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=33), and [PDF p.34, continuous survival Time definitions](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=34). Corroborating REPORT [jama_paterson_2024_oi_240139_1741633738.12862.pdf — PDF p.6, GI-2/GI-3 time-to-event results](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6) and [PDF p.8, Figure 2 time axis](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8).

**Source evidence:** Protocol/SAP endpoint prose defines elapsed recovery time from surgery or the start of operation. SAP p.33 uses operation-based 96-hour/72-hour binary horizons. On SAP p.34, the continuous GI-2 and GI-3 Time variables are defined from the start of general anaesthesia to recovery. The report gives GI-3 HR 0.98 (0.83–1.17), GI-2 HR 1.03 (0.86–1.23) and a Figure 2 axis described as days since surgery.

**Reported-versus-comparator:** The conflicting comparator pair is inside the plans: operation-start versus anaesthetic-start elapsed time for both GI survival endpoints. The published HRs and figure identify relevance and corroborate one wording convention; they are not proof that a particular origin was implemented.

**Reasoning procedure:** Match both endpoints across prose, binary definitions and survival-variable descriptions. Compare the named start events rather than treating anaesthesia and operation as equivalent labels. Separate the direct documentary comparison from inference about the final data variable or any numerical effect on the reported Cox estimates.

**Calculation:** Let recovery, operation-start and anaesthetic-start denote the corresponding timestamps. Recovery minus anaesthetic-start exceeds recovery minus operation-start by operation-start minus anaesthetic-start. The source supplies neither these timestamps nor their differences, so no magnitude, constant offset or effect on a hazard ratio is assumed. Exact variable definitions are not rounded numeric measurements; display-precision interval arithmetic is inapplicable.

**Affected result or extracted value:** Time origin for GI-2/GI-3 elapsed recovery, including interpretation of the GI-3 distribution and the reported survival estimates.

**Why context does not resolve it:** The two named start events are both printed as analysis definitions, with no equivalence, mapping or priority statement. Anaesthesia induction precedes operation in the described intervention sequence. A reader cannot establish the intended Time variable from those competing instructions; the difference could affect which elapsed duration is extracted.

**Alternative source-grounded interpretations:** The sample-variable description may use anaesthetic-start wording loosely while actual data use operation start. Alternatively, implementation may use anaesthetic start. Figure 2's surgery wording supports one interpretation but does not expose the underlying timestamp calculation. No numerical effect on the reported HRs is established.

**Mechanical evidence recheck:** Both endpoints' exact protocol/SAP definitions and the report's results/axis were independently matched against the supplied source pages, including visual confirmation of Figure 2. The logical difference between the two named origins was reproduced. PLAN roles, P_P relationship, plan_material domain and reproduced evidence state were confirmed without transcription correction. Missing inputs are the actual timestamps, their mapping, final Time construction and any governing amendment.

**Potential downstream evidence impact:** A data extractor could assign different origin definitions to the same recovery-time measure, affecting comparability of elapsed durations across studies. The supplied evidence does not establish a numerical change in either published hazard ratio.

## C012 — ERAS subgroup age adjustment specification

Pending Human Adjudication.

**Candidate statement:** The SAP's general subgroup rule extends a primary model adjusted for age, sex and centre, but its specific ERAS subgroup command omits age without stating an ERAS exception.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN SAP pp.14,15 vs PLAN SAP sample code p.38

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-008

**Qualifying route:** Route B

**Classification rationale:** The conflicting general and ERAS-specific covariate specifications are both SAP PLAN content, yielding P_P and plan_material. The main article corroborates the general primary-model extension, and the result supplement identifies the relevant ERAS estimates. Neither report location reveals the fitted ERAS covariate list, so no P_R relationship is inferred.

**Classification ambiguity:** Document roles are clear. An illustrative or abbreviated command versus an intended age-adjustment exception remains unresolved, and the actual executed model is not supplied.

**Exact source locations:** PLAN [joi240139supp2_prod_1741633738.17362.pdf — PDF p.14, §11.3–11.5 model/subgroup instructions](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=14), [PDF p.15, subgroup specification continued](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=15), and [PDF p.38, ERAS sample command and adjacent age-subgroup command](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=38). [SAP PDF p.34, primary-model sample command](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=34) corroborates the age term. REPORT [jama_paterson_2024_oi_240139_1741633738.12862.pdf — PDF p.5, subgroup interaction method](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5) and [joi240139supp3_prod_1741633738.18862.pdf — PDF p.2, ERAS subgroup results](../../../../joi240139supp3_prod_1741633738.18862.pdf#page=2) provide context and the affected estimates.

**Source evidence:** The SAP primary model includes age, sex and a random centre effect; subgroup interactions are to use the models outlined above. The ERAS command is `meglm i.GI3 i.IV##i.ERAS i.Male || CentreNo:, family(poisson) link(log) vce(robust) eform`, with no AgeBand term. Primary and adjacent age-subgroup commands include AgeBand. Published ERAS RRs are high adherence 0.96 (0.82–1.12), moderate 0.99 (0.76–1.29) and low 1.01 (0.49–2.08), with interaction P=.966.

**Reported-versus-comparator:** The direct discrepancy is plan-internal: the general primary-model/subgroup specification retains age, whereas the specific ERAS command does not. Published ERAS estimates establish the affected analysis but do not identify whether age was included in execution.

**Reasoning procedure:** Compare the stated primary covariate set with the complete ERAS command. Distinguish adding an ERAS interaction from replacing an age term with an age subgroup factor: ERAS is not age. Check for an explicit ERAS age exception and preserve the expressly sample-code status when discussing implementation.

**Calculation:** The general adjustment set contains age, sex and centre; the ERAS command contains sex, centre and the treatment-by-ERAS interaction but not age. This categorical covariate-membership comparison has no rounded numeric interval or relative discrepancy. No numerical RR or P-value impact is reconstructed from the omission.

**Affected result or extracted value:** Adjustment specification attached to the three ERAS subgroup RRs and their interaction P=.966, relevant to interpretation and reproducibility of that primary-outcome subgroup analysis.

**Why context does not resolve it:** The prose and specific command give different covariate sets, without a stated age exception for ERAS. The report supplies neither that subgroup's fitted covariate list nor model output. A reader cannot determine which planned specification governs the adjustment description attached to the estimates.

**Alternative source-grounded interpretations:** The sample command may be abbreviated or illustrative while the executed model retained age. Alternatively, age may have been intentionally omitted in the ERAS model. No supplied exception or executed output establishes either interpretation, and no preferred covariate choice is proposed.

**Mechanical evidence recheck:** Exact model/subgroup prose and the entire ERAS command were independently matched on the supplied PDF pages. The age term's inclusion in the general model and absence from the ERAS command were reproduced; the three result rows and interaction P were visually confirmed. PLAN roles, P_P classification, plan_material domain and reproduced state were confirmed without transcription correction. Missing materials are final executed commands, fitted covariates/output and any intended ERAS-specific exception.

**Potential downstream evidence impact:** An extractor could record an age-adjusted or age-unadjusted ERAS subgroup analysis depending on which SAP specification is followed. The evidence does not show a change in any reported RR, interaction P value or clinical conclusion.

## C013 — Subgroup confidence-level definitions

Pending Human Adjudication.

**Candidate statement:** The subgroup eFigure labels graphical intervals as 99% CIs while its adjacent prose defines the right-hand numeric intervals as 95%, without expressly distinguishing two interval sets.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT subgroup supplement p.2 graphical legend vs REPORT subgroup supplement p.2 numeric-interval caption

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-007

**Qualifying route:** Route B

**Classification rationale:** The conflicting graphical and numeric confidence-level descriptions are both within the same REPORT eFigure, giving S_W and statistical_results. Main REPORT and SAP PLAN confidence conventions provide corroborating context without establishing an independently observed inter-REPORT result conflict or implemented plan-versus-report analysis change; neither S_C nor P_R is added. F-ST1-002 identified the same pattern and was screened as a duplicate.

**Classification ambiguity:** Document roles are clear. Intentionally distinct graphical 99% and numeric 95% intervals remain a plausible unresolved interpretation. The overall row is noted separately because it repeats the main 95% interval within the same graphical legend.

**Exact source locations:** REPORT [joi240139supp3_prod_1741633738.18862.pdf — PDF p.2, eFigure horizontal-line legend, 12 subgroup rows, overall row and numeric-interval caption](../../../../joi240139supp3_prod_1741633738.18862.pdf#page=2). Corroborating REPORT [jama_paterson_2024_oi_240139_1741633738.12862.pdf — PDF p.5, confidence/subgroup methods](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5), [PDF p.6, overall primary 95% interval](../../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6), and PLAN [joi240139supp2_prod_1741633738.17362.pdf — PDF p.15, subgroup significance and CI rule](../../../../joi240139supp2_prod_1741633738.17362.pdf#page=15).

**Source evidence:** The eFigure line legend states 99% CI; adjacent prose describes the right-hand values as within-subgroup relative risks with 95% confidence intervals. The SAP specifies a two-sided 1% subgroup significance level and corresponding 99% intervals. Main methods state that treatment-effect estimates use 95% CIs while also specifying a 1% subgroup significance level. Every affected numeric subgroup row is preserved below; the printed levels do not identify an expressly separate pair of graphical and numeric interval sets.

| Factor | Subgroup | RR | Printed numeric interval |
|---|---|---:|---|
| Intended infusion | 6 hours | 0.92 | 0.73–1.15 |
| Intended infusion | 12 hours | 1.03 | 0.82–1.28 |
| Operation | Non-right | 0.95 | 0.78–1.15 |
| Operation | Right | 0.99 | 0.76–1.28 |
| Sex | Female | 0.95 | 0.78–1.16 |
| Sex | Male | 0.98 | 0.77–1.26 |
| Age | 50–74 years | 0.95 | 0.77–1.16 |
| Age | <50 years | 0.82 | 0.49–1.37 |
| Age | ≥75 years | 1.12 | 0.78–1.59 |
| ERAS adherence | High | 0.96 | 0.82–1.12 |
| ERAS adherence | Moderate | 0.99 | 0.76–1.29 |
| ERAS adherence | Low | 1.01 | 0.49–2.08 |

The separate overall row is RR 0.97 (0.88–1.07), matching the main article's primary 95% CI while appearing in the same display with the 99% graphical legend.

**Reported-versus-comparator:** One source display supplies a 99% graphical designation and a 95% numeric designation for the subgroup intervals. The comparator is the confidence convention attached to those displayed limits, not a comparison of factor interaction P values with within-subgroup treatment tests. All 12 numeric subgroup intervals include 1 and contain their respective point estimates.

**Reasoning procedure:** Read the exact legend and numeric-caption wording, match all 12 subgroup values plus the separate overall row, and distinguish confidence level from estimate magnitude. Consider whether graphical and numeric intervals may intentionally differ, without inferring a convention from visual geometry alone. Preserve SAP/main confidence statements as context rather than assuming the implemented fitted analysis changed.

**Calculation:** Confidence levels here are exact inferential definitions rather than rounded estimated percentages; the numeric display-precision threshold does not apply. As a diagnostic illustration only, normal-log intervals with identical standard error would have a 99%/95% half-width ratio of approximately 2.5758/1.9600=1.3142. This does not reconstruct the actual model intervals or determine their generating confidence level. Within-subgroup standard errors, fitted output and separately specified graphical limits are unavailable.

**Affected result or extracted value:** Confidence convention attached to all 12 within-subgroup RR intervals and the uncertainty interpretation or reconstruction based on those limits; the overall interval supplies additional contextual evidence.

**Why context does not resolve it:** Both confidence levels are printed adjacent to the same figure, without an explicit explanation of separate graphical and numeric interval sets. The main overall 95% match does not determine the within-subgroup confidence level. The ambiguity affects extractable uncertainty rather than merely a pointer or formatting label.

**Alternative source-grounded interpretations:** Numeric 95% intervals and graphical 99% intervals may deliberately coexist, or one level may describe the intended whole display. The horizontal geometry broadly tracks the right-hand numeric limits, but visual matching is not precise enough to establish the fitted convention. The sources provide no within-subgroup model output or separately designated graphical limits to distinguish these interpretations.

**Mechanical evidence recheck:** The exact source eFigure was visually reread, and both confidence labels, all 12 numeric subgroup rows and the separate overall value matched. Main methods/overall interval and SAP rules were independently matched as context. S_W classification, statistical_results domain and reproduced evidence state were confirmed without transcription correction. No point-containment or interval-versus-interaction-test conflict was inferred. The unresolved inputs are fitted subgroup uncertainty output, explicitly separate graphical limits and the governing level for each interval set.

**Potential downstream evidence impact:** An extractor could assign either 95% or 99% to the printed subgroup limits and reconstruct different uncertainty from them. The source evidence establishes the confidence-definition ambiguity, without demonstrating an altered subgroup conclusion or downstream propagation.
