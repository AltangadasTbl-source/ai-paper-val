# Cross-source consistency: plan relationships

## Scope and source authority

Fresh review of all PLAN-to-REPORT and PLAN-internal statistical-design relationships: DOC-003 protocol pp.1–82; DOC-004 parent-trial SAP pp.1–40; DOC-005 analysis-specific SAP pp.1–7; DOC-001 report pp.1–14; DOC-006 report definitions, eMethods, flow, forests, prediction plots and eTables relevant to these comparisons. REPORT-to-REPORT comparisons are assigned separately. Read QUALITY_CONTROL_SCOPE.md and review_contract.md completely. Reconstructed maps were used as locators, with targeted direct pdftotext -layout confirmation and visual confirmation of trial-SAP Appendix B pp.39–40. Direct tools and CPU follow tooling_record.md. No sources or reused assets modified; no external sources or earlier scientific conclusions consulted.

The parent trial and this exploratory imaging analysis are distinguished. The July 7, 2023 analysis SAP governs analysis-specific models; parent-trial missing-data and primary-test rules are not automatically imposed on the exploratory report. Disclosed >100-mL inclusion and one-year follow-up amendments, and the disclosed 300-patient DSMB review, were retained. Numerical rounding intervals are inapplicable to the categorical analysis specifications below; no difference between two rounded numerical copies is used as the basis of a finding.

## Completed relationship checks

| Relationship group | Complete comparison and outcome |
|---|---|
| Eligibility | Compared all eight general inclusion items; five general exclusion items, including each of the five nested 3–4.5-hour thrombolysis exclusions; two imaging inclusion items, with all three large-core alternatives; and all eight imaging exclusions between protocol synopsis/body and trial SAP. Age18–85, NIHSS≥6, prestroke mRS0–1,0–24h, life expectancy≥3months, ICA/M1, ASPECTS3–5 OR core≥50mL, ASPECTS≤2 exclusion, and each remaining criterion reconcile. Local eligibility versus central adjudication explains subsequently observed ASPECTS0–2 and M2 labels. |
| Intervention | EVT+MM versus MM, 1:1; stent retriever/aspiration/combination and background medical care reconcile. No different randomized dose/duration is reported. Report's abbreviated procedure account does not assert use of prohibited IA thrombolysis or a different puncture window. |
| Imaging endpoints | Reviewed rCBF<30%, ADC threshold, Tmax>6s, site versus core-lab ASPECTS, follow-up24h–7d, all three ischemic-volume estimates, both mismatch conjunctions, and every concordance criterion. Findings address primary/sensitivity volume hierarchy; remaining definitions reconcile or have excluded wording observations below. |
| Outcome lists and composites | Compared every protocol secondary safety component, recanalization/reperfusion, hospital stay, discharge, early NIHSS improvement and imaging endpoint with SAP items1–14 and tertiary items1–6. Compared all six discharge categories, all procedural-complication components, mRS0–2/0–3/5–6, mortality and sICH against analysis SAP/report. Outcome-status pattern and sICH window are findings below. The current SAP expressly includes mRS5–6 and the report discloses addition relative to parent analyses. |
| Models/covariates | Parent WMW/CMH and current PIM distinguished; current PIM, modified Poisson/robust standard errors, age/NIHSS/LKW-to-randomization/core, omission of the stratification covariate, and logistic calibration fallback checked. Report presents both ASPECTS associations without volume adjustment and the planned volume-adjusted association; differing results are explicitly attributed to adjustment. |
| Population/missing data | Checked parent ITT/as-treated/per-protocol criteria item by item, imputation30/ordinal-logistic/Rubin/tipping-point rules, current SAP no-imputation, and full cohort352 versus observed336 after16 disclosed exclusions. Current ITT-versus-as-treated departure is a finding; the parent's imputation rule is not misapplied to the current no-imputation SAP. |
| Subgroups/sensitivity | Compared each age, NIHSS, clot, time, volume70/100/150, ASPECTS, mismatch, restricted-population, hemisphere and geographic subgroup; each trial-SAP tertiary imaging analysis; all current SAP ASPECTS3/4/5, mismatch50/100mL, continuous-mismatch, discordance, and post hoc appendix analyses. Parent analysis lists explicitly allow later separate reports. Current contour-analysis time definition is a finding. |
| Hypothesis/power/stopping | Compared all seven projected mRS cells per arm, maximum560/fixed376/188 per arm/add184, interims200/380, group proportions and all enrichment decision branches, alpha/power, b2.604/b-tilde−1.897/c2.772 and direction. Stopping at requested300-patient review is explicitly disclosed; rank/hypothesis direction remains a finding. |
| Multiplicity | Parent adaptive primary control distinguished from exploratory analyses; current two-sided.05/no multiplicity adjustment reconciles with analysis-specific SAP. No unreported noninferiority/equivalence margin is inferred. Protocol discordance15% aim pertains to its own50-mL profiles, rather than automatically governing the later70-mL exploratory profiles. |

## Findings

### F-XS-001

**Title:** Outcome hierarchy differs within the protocol and between parent-trial plans.

**Compared locations and roles:** PLAN [protocol synopsis p.8](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=8), PLAN [protocol outcome section p.37](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=37), PLAN [protocol secondary analysis p.50](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=50), PLAN [trial SAP hierarchy p.13](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=13), PLAN [trial SAP tertiary continuation p.14](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=14).

**Printed statements:** Protocol p.8 calls mRS0–2 a second primary outcome; p.37 repeats primary outcome #2 and says the dichotomized outcome will remain the second primary outcome. Protocol p.50 calls the same90-day mRS0–2 endpoint secondary. Trial SAP p.13 places functional independence in the secondary list. Protocol p.50 also lists infarct volume, lesion growth and length of stay as secondary; trial SAP pp.13–14 lists these as tertiary.

**Comparison logic:** Match exactly the same endpoint/time point. A single endpoint has two explicit hierarchy assignments within the same protocol; later plan lists also change the status of the imaging and stay endpoints. Consolidated as one hierarchy pattern, retaining every affected endpoint. The report's exploratory scope does not resolve the contradiction inside the parent protocol.

**Focus area:** D. **Proposed review domain:** plan_material. **Relationship type:** P_P. **All relationships:** P_P.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Primary-versus-secondary classification of90-day functional independence and secondary-versus-tertiary classification of infarct volume, growth and hospital stay in extraction of the planned trial hierarchy.

**Why context does not resolve it:** Route A category5 explicitly retains reproduced outcome-status changes. The same dated protocol prints both primary and secondary for functional independence; no hierarchy amendment is identified at those locations.

**Supported alternatives / missing definition:** The later SAP may represent a deliberate hierarchy revision; the supplied locations do not identify the operative revision or account for the protocol's internal dual designation. No inference about primary-trial outcome omission is made.

**Human question:** Which hierarchy governed the trial, and where is the revision documenting the status of functional independence, infarct volume/growth and hospital stay?

### F-XS-002

**Title:** Composite core is planned as primary but presented as post hoc sensitivity.

**Compared locations and roles:** PLAN [analysis SAP imaging definitions p.3](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=3), PLAN [post hoc appendix p.7](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=7); REPORT [statistical analysis p.4](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4), REPORT [Figure1 and narrative p.6](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6), REPORT [Figure3 p.8](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=8).

**Printed statements:** SAP p.3 specifies primary analysis using the larger of CTP/MRI core and CT hypodensity; CTP/MRI-only is sensitivity. Appendix p.7 explicitly calls composite core prespecified. Main p.4 calls analyses using composite core and CT hypodensity post hoc sensitivity; p.6 labels the composite results post hoc. Main Figure1/3 instead foreground CTP/MRI core.

**Comparison logic:** The same90-day outcomes,70/100/150-mL strata and treatment contrast use different prespecified-primary/sensitivity assignments. Composite is not merely an alternative name for perfusion core: main p.4 gives medians101 versus73mL and says hypodensity exceeds perfusion in203 patients.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Whether Figure1 core-specific aGenORs and Figure3 core-related probabilities are the prespecified primary imaging analysis or its sensitivity analysis, and whether composite-core results were prespecified.

**Why context does not resolve it:** Route A category5 retains changed analysis status. The supplied specific SAP explicitly calls composite primary/prespecified, whereas the report calls its analyses post hoc.

**Supported alternatives / missing definition:** Reporting emphasis may have been revised; hypodensity-alone and several appendix analyses were explicitly post hoc. Those disclosures do not identify a revision of composite-core primary status.

**Human question:** Was the planned composite-core primary analysis replaced by CTP/MRI-only analysis, and which dated specification establishes the primary/sensitivity and prespecified/post hoc status?

### F-XS-003

**Title:** Analysis-specific plan specifies all analyses as-treated, while treatment-effect strata use randomized assignment.

**Compared locations and roles:** PLAN [analysis SAP principles p.3](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=3); REPORT [analysis population p.4](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4), REPORT [Figure1 p.6](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6), REPORT [ITT eTable2 p.38](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=38).

**Printed statements:** Specific SAP: all analyses under an as-treated approach. Report: treatment comparisons across imaging strata use randomization groups, while within-arm associations use received treatment. Report retains168/168 randomized groups, with two MM-to-EVT crossovers; received-treatment groups are170/166.

**Comparison logic:** Population/time/outcome match; actual treatment grouping differs for the randomized treatment-effect analyses. Exact counts clarify that this is not two names for the same analysis set. Counts themselves reconcile and are not the numeric basis of the finding.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route B.

**Affected result or extracted value:** Treatment-effect aGenORs across ASPECTS, core and mismatch strata in Figure1 and binary treatment-effect results in supporting displays.

**Why context does not resolve it:** The report clearly describes what it did, but the analysis-specific plan does not contain its split ITT/as-treated specification. The parent trial's ITT approach does not remove the explicit current-plan all-as-treated statement.

**Supported alternatives / missing definition:** Randomized treatment comparisons may intentionally retain parent-trial ITT, with as-treated restricted to prognosis. A specific amendment or qualification of the current SAP is not identified.

**Human question:** Which prespecified or amended analysis-population rule governed treatment-effect versus within-treatment imaging analyses?

### F-XS-004

**Title:** Symptomatic hemorrhage assessment window differs between supplied plans.

**Compared locations and roles:** PLAN [analysis SAP sICH p.5](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=5), PLAN [parent SAP definition p.13](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=13), PLAN [parent SAP sICH p.18](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=18), PLAN [parent SAP illustrative footnote p.31](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=31); REPORT [outcomes p.3](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3), REPORT [sICH counts eTable2 p.38](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=38).

**Printed statements:** Analysis SAP defines PHII or remote PH associated with NIHSS increase≥4 at a4-hour follow-up window. Parent SAP defines SITS-MOST hemorrhage/NIHSS increase or death within24hours, and pp.18/31 repeat24hours. Report calls sICH SITS-MOST and eTable2 gives0/168 versus2/168 without a separate temporal qualifier.

**Comparison logic:** The same named safety endpoint has explicitly different planned ascertainment windows. Four versus24hours is a change in the event definition, not a display-precision difference. Parent SAP also explicitly includes death in its definition, whereas the analysis SAP sentence includes the NIHSS criterion only; this is retained as an endpoint-component distinction within the same pattern.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R, P_P.

**Qualifying route:** Route B.

**Affected result or extracted value:** Definition attached to the sICH0/168 and2/168 counts, including eligible assessment time and whether death alone qualifies.

**Why context does not resolve it:** The report's SITS-MOST reference aligns with the parent plan, while the analysis-specific plan explicitly prints4hours. Supplied current results do not name which assessment window produced the counts.

**Supported alternatives / missing definition:** The4-hour window may be a printed temporal slip or a separately intended early assessment; report may have retained the parent trial's24-hour adjudication. Neither interpretation is demonstrated by the supplied counts alone.

**Human question:** Which assessment window and component rule produced the reported sICH counts, and how does it relate to the analysis SAP's4-hour definition?

### F-XS-005

**Title:** Planned joint age/time prediction uses time to randomization, while reported predictions use time to reperfusion.

**Compared locations and roles:** PLAN [analysis SAP independent-ambulation prediction p.5](../../../../joi240006supp4_prod_1708623115.00733.pdf#page=5); REPORT [age/time results p.10](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10), REPORT [eFigure18 p.24](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=24), REPORT [eFigure19 p.25](../../../../joi240006supp5_prod_1708623115.01733.pdf#page=25).

**Printed statements:** SAP specifies joint age and last-known-well-to-randomization prediction for EVT patients achieving mRS0–3. Report predicts using CTP-to-reperfusion/end-procedure and last-known-well-to-reperfusion/end-procedure; the former association is aRR0.97(0.93–1.00) per10minutes and the latter aRR1.00(0.99–1.00).

**Comparison logic:** Same EVT subset,90-day mRS0–3 and age/time prediction task; the temporal endpoint changes from randomization to reperfusion/end-procedure, and one model additionally changes temporal origin to CTP. Supplied report does not show the planned age×LKW-to-randomization contour in these matched displays.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecification of the independent-ambulation age/time predictions and interpretation of the reported imaging-to-reperfusion association.

**Why context does not resolve it:** Route A category5 retains replacement of a planned key-secondary analysis. The report explicitly names different time variables; the post hoc appendix does not identify this temporal revision.

**Supported alternatives / missing definition:** Reperfusion-based predictions may be additional exploratory analyses, with planned randomization-based prediction omitted or elsewhere not identified. Time to randomization remains a prognostic adjustment covariate; this does not supply the planned joint prediction.

**Human question:** Was the planned joint age/LKW-to-randomization independent-ambulation analysis performed, and were the reperfusion-based prediction analyses prespecified or added later?

### F-XS-006

**Title:** Positive rank-sum efficacy direction does not reconcile with the supplied treatment-score definitions.

**Compared locations and roles:** PLAN [protocol primary outcome p.37](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=37), PLAN [protocol Appendix B p.80](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=80), PLAN [protocol Appendix B p.81](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=81), PLAN [trial SAP Appendix B p.39](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=39), PLAN [trial SAP Appendix B p.40](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=40). REPORT [mRS scale and treatment effect p.3](../../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3) corroborates only the scale direction; it is not an additional conflicting relationship.

**Printed statements:** W is the sum of EVT Rankin-score ranks; Z=(W−nEVT(nEVT+nMM+1)/2)/sqrt[nEVT*nMM*(nEVT+nMM+1)/12]. EVT efficacy requires Z≥2.604 at interim or Z≥2.772 at final. The alternative is P(Y≤X)=.5+θ, θ=.0791, explicitly Y=MM score and X=EVT score. Primary outcome text describes lower mRS as better, including improvement5→4/3.

**Comparison logic:** On the printed raw-score definition, Y≤X means MM has no greater disability than EVT; a probability above.5 thus points toward MM having the lower score. With ascending ranks, better/lower EVT scores give a smaller EVT rank sum and negative Z, whereas the printed efficacy rule uses positive Z. Both appendices repeat the same direction pattern. The hypothesis's printed treatment-score definitions establish the contrast conflict independently of an assumed fitted model.

**Focus area:** D. **Proposed review domain:** plan_material. **Relationship type:** P_P. **All relationships:** P_P.

**Qualifying route:** Route B.

**Affected result or extracted value:** Direction of the parent trial's one-sided superiority hypothesis and efficacy/stopping statistic referenced in the report's stopped-for-EVT-benefit account.

**Why context does not resolve it:** No descending-rank convention, transformed outcome or reversed operational treatment coding is specified in these appendix locations. The stated inequality and raw-score treatment labels point in the opposite direction to lower-mRS EVT benefit.

**Supported alternatives / missing definition:** Descending ranks may explain positive EVT Z; a reversed X/Y definition or transformed score could explain the probability direction. These are possible implementation conventions, not statements that the operational analysis used them. No operational interim statistic is supplied.

**Human question:** What rank ordering, score transformation and treatment coding were used, and how do they reconcile the printed probability alternative and positive efficacy boundary with benefit defined by lower EVT mRS?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| Analysis SAPp.3 versus mainp.3/results eFigure1p.5 | SAP says ratio of core and hypoperfused volumes; the accompanying≥1.8/≥1.2 definitions and explicit report numerator/denominator identify the intended ratio immediately. No printed numeric value changes. | TERMINOLOGY_OR_WORDING |
| Protocolp.51 | Two written descriptions of the discordant direction use rearranged favorable/unfavorable CT/CTP names; the two profiles and neighboring aim/diagram identify them. | TERMINOLOGY_OR_WORDING |
| Parent protocolpp.17,42 versus earlier eligibility/visit accounts | Explicit additions of >100-mL patients and365-day follow-up account for these prospective changes. | CONTEXT_RESOLVES |
| Protocol planned interims200/380; parent SAPp.12; mainp.4 | Requested300-patient review and stopping are disclosed in both later plan and report; no printed interim statistic is supplied to reproduce a boundary-control conflict solely from timing. | CONDITIONAL_OR_UNREPORTED |
| Parent protocol/SAP versus current analysis SAP/report | Parent multiple imputation and WMW versus exploratory no-imputation/PIM could appear different; these describe different analysis tasks, and the specific imaging SAP expressly specifies the latter. | NOT_REPRODUCED |
| Current SAP all enrolled; mainp.4 and flowp.8 |352 randomized versus336 analyzed is fully explained by4 missing90-day outcomes and12 imaging exclusions, with no imputation planned. | CONTEXT_RESOLVES |
| Mainp.1/6/7 and analysis SAPp.4; eFigure14p.20 | Foregrounded ASPECTS association omits core, whereas planned model includes core; report explicitly presents the fully adjusted model as well and distinguishes its estimate/significance. No planned model is absent. | CONTEXT_RESOLVES |
| Protocolp.22/51/71 versus current discordance definitions | Original second aim15% superiority contrast uses50-mL imaging profiles; current exploratory SAP prospectively defines70-mL profiles and different contrasts. Treating them as the same missing primary analysis would misalign the tasks. | NOT_REPRODUCED |
| Parent SAPp.23 versus mainp.4/6/11 and current SAPp.7 | Broad total-lesion/core-overestimation concepts were prespecified; the current SAP distinguishes the concept from specific post hoc analyses. Apart from composite-primary status in F-XS-002, a concept's existence does not establish that every later implementation was prespecified. | CONTEXT_RESOLVES |
| Protocolp.49 versus trial SAPp.11 simulation scenario4 | Fixed-design power cell21.2% versus51.2% differs between prospective operating-characteristic tables. It is not an observed outcome, sample-size/power input, primary decision boundary or a changed planned sample size; therefore this plan-internal historical simulation comparison is peripheral. | PERIPHERAL_COMPARISON |
| Protocolp.78 versus trial SAPp.37 | Minimization weights and category detail differ across dated plans; current report agrees with later factor list including physician ASPECTS. No supplied statement attributes a particular conflicting weight to the reported primary estimate or decision rule. | PERIPHERAL_COMPARISON |
| Current SAP mismatch50/100-mL strata versus report continuous-mismatch displays | Extra threshold displays are not found among matched current results, but their omission alone does not establish replacement of a primary/key-secondary outcome analysis; the planned continuous association and two profile analyses are reported. | CONDITIONAL_OR_UNREPORTED |

## Limitations and missing definitions

No scientific comparison scope gap. Missing implementation definitions relevant to the findings: operative hierarchy amendment; revised composite primary/sensitivity status; qualification of all-as-treated principle; sICH assessment-window/component adjudication; status and location of planned versus added joint age/time predictions; rank ordering/transformation/treatment coding and operational interim statistic. Native text and reusable source-matched images are locators; final mechanical recheck remains against each exact source. Six findings and twelve excluded observations. All findings remain proposed reporting issues for independent inclusion screening; no candidate IDs or adjudications assigned.
