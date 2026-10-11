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

**Compared locations and roles:** PLAN [protocol synopsis p.8](../../../joi240006supp2_prod_1708623114.99233.pdf#page=8), PLAN [protocol outcome section p.37](../../../joi240006supp2_prod_1708623114.99233.pdf#page=37), PLAN [protocol secondary analysis p.50](../../../joi240006supp2_prod_1708623114.99233.pdf#page=50), PLAN [trial SAP hierarchy p.13](../../../joi240006supp3_prod_1708623114.99733.pdf#page=13), PLAN [trial SAP tertiary continuation p.14](../../../joi240006supp3_prod_1708623114.99733.pdf#page=14).

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

**Compared locations and roles:** PLAN [analysis SAP imaging definitions p.3](../../../joi240006supp4_prod_1708623115.00733.pdf#page=3), PLAN [post hoc appendix p.7](../../../joi240006supp4_prod_1708623115.00733.pdf#page=7); REPORT [statistical analysis p.4](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4), REPORT [Figure1 and narrative p.6](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6), REPORT [Figure3 p.8](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=8).

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

**Compared locations and roles:** PLAN [analysis SAP principles p.3](../../../joi240006supp4_prod_1708623115.00733.pdf#page=3); REPORT [analysis population p.4](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4), REPORT [Figure1 p.6](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6), REPORT [ITT eTable2 p.38](../../../joi240006supp5_prod_1708623115.01733.pdf#page=38).

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

**Compared locations and roles:** PLAN [analysis SAP sICH p.5](../../../joi240006supp4_prod_1708623115.00733.pdf#page=5), PLAN [parent SAP definition p.13](../../../joi240006supp3_prod_1708623114.99733.pdf#page=13), PLAN [parent SAP sICH p.18](../../../joi240006supp3_prod_1708623114.99733.pdf#page=18), PLAN [parent SAP illustrative footnote p.31](../../../joi240006supp3_prod_1708623114.99733.pdf#page=31); REPORT [outcomes p.3](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3), REPORT [sICH counts eTable2 p.38](../../../joi240006supp5_prod_1708623115.01733.pdf#page=38).

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

**Compared locations and roles:** PLAN [analysis SAP independent-ambulation prediction p.5](../../../joi240006supp4_prod_1708623115.00733.pdf#page=5); REPORT [age/time results p.10](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10), REPORT [eFigure18 p.24](../../../joi240006supp5_prod_1708623115.01733.pdf#page=24), REPORT [eFigure19 p.25](../../../joi240006supp5_prod_1708623115.01733.pdf#page=25).

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

**Compared locations and roles:** PLAN [protocol primary outcome p.37](../../../joi240006supp2_prod_1708623114.99233.pdf#page=37), PLAN [protocol Appendix B p.80](../../../joi240006supp2_prod_1708623114.99233.pdf#page=80), PLAN [protocol Appendix B p.81](../../../joi240006supp2_prod_1708623114.99233.pdf#page=81), PLAN [trial SAP Appendix B p.39](../../../joi240006supp3_prod_1708623114.99733.pdf#page=39), PLAN [trial SAP Appendix B p.40](../../../joi240006supp3_prod_1708623114.99733.pdf#page=40). REPORT [mRS scale and treatment effect p.3](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3) corroborates only the scale direction; it is not an additional conflicting relationship.

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
# Cross-source consistency: report relationships

Scope: all REPORT-to-REPORT and REPORT-internal matched results in DOC-001 physical pp.1–14 and DOC-006 physical pp.1–53. DOC-002 pp.1–30 and DOC-007 p.1 have no applicable scientific-result relationships, confirmed from their complete administrative maps. PLAN comparisons are assigned separately. Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Current complete maps M001–M120, report portion A019–A041 and B001–B017 were used as locators; exact supplied PDF text and matched images were consulted. No prior-run conclusions or external sources were used. Current numeric main findings were read only after independent scope reconstruction to identify shared issues.

## Complete matched-result coverage

| Matched scope | Locations and identity checks | Result |
|---|---|---|
| Abstract, Key Points and study population | Main pp.1–4, Table1 p.5; supplement flow p.8 and eTables1/2 pp.35–38: 352 randomized,16 excluded,336 analyzed,168/168 ITT,170/166 received-treatment; age67,female139; eligibility/imaging scales and outcome time point | Matched. Baseline population differences retain ITT versus as-treated identity. |
| Primary ordinal treatment results | Main abstract p.1, text pp.4–6, Figure1 p.6; supplement eFigure10 p.16, eTable3 p.39,eTable4 p.40,eTables9/10 pp.47–50 | Abstract/body ASPECTS3/4/5 and ≥70/100/150mL estimates/CIs match exactly. Site ASPECTS, MRI exclusion, CT hypodensity/composite core and discordance results retain distinct populations/measurements/adjustments. No comparison substitutes these sensitivities for the main CTP/MRI analysis. |
| Full ordinal distributions and binary thresholds | Main Figure2 p.7, discussion p.10; supplement112 forest rows eFigures7–13 pp.13–19, all33 strata/66 arm bars eFigure20 pp.26–34, eTable2 p.38,eTables8–10 pp.45–50 | Category legend, arm, denominator, time, threshold and modality matched for all applicable copies. F-XS-101 and F-XS-104 below identify two distinct patterns. Other cumulative threshold percentages reconcile within their component rounding intervals. |
| Within-treatment prognosis | Main abstract p.1, text p.6, Table2 p.7; supplement eFigures14–16 pp.20–22, eTable5 p.41,eTable6 p.42 | Main repeated ASPECTS/core estimates match. Added core adjustment, distinct volume definitions and ordinal-logistic model-comparison metrics distinguish the support results. Increasing injury has matching unfavorable directions. Ratio interpretations follow stated modified Poisson methods and null1. |
| Mismatch profiles, volume and treatment effect | Main pp.3,6–11, Figure1 p.6,Table3 p.9; supplement eFigures5/6 pp.10–12, eFigures7–13 pp.13–19,eFigure17 p.23,eFigure20 pp.32–34,eTable7 pp.43–44 | Both joint threshold definitions, CTP versus composite and ITT versus received treatment retained.29/307 and120/216 CTP totals,74/262 and211/125 composite totals match. All time/core trend directions and printed P values match. F-XS-102 retains continuous EVT direction conflict. Adjusted profile effects are not crude comparisons. |
| Prognostic prediction contours | Main pp.10–11; supplement eFigures18/19 pp.24–25 | Age/imaging-delay unfavorable directions match. F-XS-105 addresses differing core-measure labels. No exact fitted coordinates or unsupported pointwise numerical estimates are invented. |
| Follow-up imaging/infarct/growth | Main pp.4,9–11; supplement eTable2 p.38,eTables11–13 pp.51–53 | MRI analysis population204=101+24+79 supplies corroboration for shared numeric finding F-NUM-001. Outcome subgroup totals46+290=336 and96+240=336 match. Three overestimation cases match. Peripheral IQR-copy differences are listed below. |
| Caption/footnote treatment direction | Main Figures1/3 pp.6/8; supplement all eFigures7–19 pp.13–25 and eTables3–10 pp.39–50 | Primary ordinal better-outcome reference and binary EVT/MM references checked throughout. F-XS-103 retains unfavorable-outcome axis reversal. Interaction P values are not treated as individual stratum effect tests. |
| Administrative/reference scope | Main pp.12–14,supplement title/contents pp.1–3,DOC002 pp.1–30,DOC007 p.1 | COMPLETE_NO_APPLICABLE_NEW_RESULT. Source-linked administrative maps cover each page; no endpoint, result, analysis population or prospective design evidence appears. |

## Findings

### F-XS-101

**Title:** Large-core primary mRS distribution does not reconcile across Figure2, supplemental functional-threshold counts and discussion.

**Compared locations and document roles:** REPORT DOC-001 [Figure2B, physical p.7](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7), [discussion, physical p.10](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10); REPORT DOC-006 [eFigure7, physical p.13](../../../joi240006supp5_prod_1708623115.01733.pdf#page=13), [eFigure8, physical p.14](../../../joi240006supp5_prod_1708623115.01733.pdf#page=14). Matched ≥100mL CTP/MRI core,90-day outcome,ITT EVT51/MM49; main M073/M074/M117,support A028/A029. Proposed relationship S_C; all relationships S_C,S_W. Shared issue with F-NUM-002, adding both arms and exact supplemental thresholds.

**Printed values:** Figure2B category colors/legend assign EVT mRS0/1/2/3 percentages2/6/10/20, and MM0/2/3 percentages2/4/16 (mRS1 has zero width). Thus cumulative mRS0–2 and0–3 are EVT18%/38%,MM6%/22%. eFigure7 prints EVT4(7.84%),MM1(2.04%); eFigure8 prints EVT9(17.65%),MM3(6.12%). Main discussion describes about80% mRS≥4 and one in five independently ambulant after EVT, matching the supplemental threshold scale rather than Figure2B.

**Rule and calculation:** Same full mRS distribution must yield its dichotomized thresholds. Allowing each printed whole-percentage segment ±0.5 yields EVT mRS0–2 [16.5,19.5] and0–3 [36,40]; MM mRS0–2 [5,7] and0–3 [20.5,23.5], where absent-width categories contribute no fabricated printed value. Supplemental printed intervals are [7.835,7.845],[17.645,17.655],[2.035,2.045],[6.115,6.125]%. Minimum gaps divided by supplemental reference copies are respectively8.655/7.84=1.104,18.345/17.65=1.039,2.955/2.04=1.449,14.375/6.12=2.349. All exceed0.05. Count/denominator half-unit recomputation also gives broad ranges EVT4/51 [6.796,8.911]%,9/51 [16.505,18.812]%;MM1/49 [1.010,3.093]%,3/49 [5.051,7.216]%, which still do not overlap Figure2B cumulative intervals. These are observed distributions, not adjusted effect estimates.

**Focus area:** A. **Proposed review domain:** statistical_results.

**Qualifying route:** Route B.

**Affected result or extracted value:** Primary90-day mRS distribution among ≥100mL-core patients and its independence/ambulation thresholds, in both randomized groups.

**Why context does not resolve it:** All displays explicitly match time,modality,core threshold and arm sizes. The intended category placement or threshold proportions cannot be determined from Figure2 alone. The discrepancy concerns the primary outcome distribution and therefore is not a peripheral secondary-display comparison.

**Supported alternatives:** Figure2 category placement, the supplemental threshold counts or a label could represent a different intended outcome partition. Discussion supports the smaller EVT ambulation proportion, but does not authorize selecting a replacement. An ITT/as-treated shift of only two crossovers does not explain these large discrepancies, and Figure2/eFigures7/8 already match ITT denominators.

**Exact human question:** Which mRS category distribution applies to the ≥100mL CTP/MRI-core EVT51/MM49 groups, and how should Figure2B reconcile with the eFigure7/8 threshold counts and discussion?

### F-XS-102

**Title:** EVT mismatch-volume functional-outcome direction reverses between the narrative and its cited prediction figure.

**Compared locations and document roles:** REPORT DOC-001 [physical p.8, mismatch paragraph ending above discordance heading](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=8); REPORT DOC-006 [eFigure17 panelsA/B, physical p.23](../../../joi240006supp5_prod_1708623115.01733.pdf#page=23). Main M110,support A038. Proposed relationship S_C.

**Printed values/statements:** Main text states that as mismatch volume increased,the marginal probability of functional independence and independent ambulation increased for EVT but decreased for MM, citing eFigure17. eFigure17 labels x-axis Mismatch Vol(mL),panelsA/B estimated probabilities mRS0–2/mRS0–3,cyan EVT and salmon MM. Both cyan EVT curves decrease continuously from left to right across the displayed range; both MM curves also decrease.

**Rule and calculation:** A stated increase and a plotted decrease for the same arm,outcomes and predictor are opposite directions. The two EVT panels are one pattern. Exact curve coordinates are not printed and are not imputed; display-precision arithmetic is inapplicable to this direction comparison. The curve direction is unambiguous over the plotted range,including positive mismatch volumes.

**Focus area:** B. **Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** Direction of association between increasing continuous mismatch volume and EVT functional independence/ambulation predictions.

**Why context does not resolve it:** RouteA category2 applies to a direction statement reversing displayed results. The article cites this exact figure and does not identify a separate model or predictor; binary mismatch-presence comparisons in Table3 are a different contrast and do not reconcile continuous slopes.

**Supported alternatives:** The narrative or plotted predictor/curves may describe a different intended model. No supplied statement identifies such a model; the MM direction agrees while the EVT direction differs.

**Exact human question:** What EVT continuous mismatch-volume prediction was intended, and how does the stated increasing EVT probability reconcile with both decreasing EVT curves in eFigure17A/B?

### F-XS-103

**Title:** eFigure13 favors labels reverse the direction implied by its unfavorable outcome and EVT/MM risk ratios.

**Compared locations and document roles:** REPORT DOC-006 [eFigure13, physical p.19, title,16rows,axis/reference caption](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19), corroborated by REPORT DOC-006 [eFigure9, physical p.15](../../../joi240006supp5_prod_1708623115.01733.pdf#page=15). Support A034/A030. Proposed relationship S_W.

**Printed values/statements:** eFigure13 outcome is complete dependence/death,mRS5–6. Axis caption specifies relative risk in thrombectomy compared with MM. It labels RR<1 side “Favours Medical Management” and RR>1 side “Favours Thrombectomy.” All16 ratios are below1: .68,.77,.82,.72,.61,.87,.62,.78,.76,.55,.72,.69,.67,.74,.76,.71. Every EVT printed adverse-outcome percentage is lower than its MM counterpart; e.g.first row39.71% versus60.94%,RR.68(.49–.95). eFigure9 for the same unfavorable threshold has favors EVT on the left and MM on the right.

**Rule and calculation:** With adverse outcome and EVT/MM reference,RR<1 means less dependence/death with EVT; axis favors labels assign the opposite intervention. This is a direction/reference statement, not a discrepancy between adjusted and crude numeric estimates. Numeric half-unit relative discrepancies are inapplicable; no adjusted ratio is recomputed from raw percentages.

**Focus area:** B. **Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** Direction of EVT treatment association for dependence/death across every CT hypodensity/composite and mismatch stratum in eFigure13.

**Why context does not resolve it:** RouteA category2 applies to reference/direction statements that reverse displayed values. This is not a peripheral panel-heading discrepancy: the favors annotation changes treatment benefit reading of all16 effect estimates.

**Supported alternatives:** The axis labels may correspond to a favorable outcome or opposite ratio reference,but both title and caption expressly specify mRS5–6 and EVT compared with MM. No such alternative reference is printed.

**Exact human question:** Which favors direction/reference is intended for eFigure13’s EVT/MM dependence-or-death risk ratios?

### F-XS-104

**Title:** Discordant-profile functional-outcome counts are attributed to opposite treatment arms in eTable9 versus matched eTable8/distribution.

**Compared locations and document roles:** REPORT DOC-006 [eTable8 mRS0–2, physical p.45](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45), [eTable8 mRS0–3, physical p.46](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46), [eTable9, physical p.47](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47), [eFigure20x, physical p.32, top bar pair continued from heading on p.31](../../../joi240006supp5_prod_1708623115.01733.pdf#page=32), [panel heading, physical p.31](../../../joi240006supp5_prod_1708623115.01733.pdf#page=31). Support B011/B012,A041x. Proposed relationship S_W.

**Printed values:** Profile2 ASPECTS6–10/CTP-MRIcore≥70mL has EVT12/MM11 in all compared rows. eTable8 prints EVT1/12(8%) andMM0/11(0%) for independence,EVT3/12(25%) andMM0/11(0%) for ambulation. eTable9 explicitly labels columns MM,EVT and prints MM1/11(9.1%),EVT0/12(0%) andMM3/11(27.3%),EVT0/12(0%) for those respective outcomes. eFigure20x has EVT8% in mRS2 plus17% in mRS3,and no MM mRS0–3 segment; its EVT/MM arm sizes are12/11. All outcomes90days.

**Rule and calculation:** Identical arm-specific outcome counts should not move to the other treatment column between descriptive copies. Percent-copy half-unit intervals for EVT independence8% versus0% are [7.5,8.5] versus[-.5,.5],gap7/reference8=.875; EVT ambulation25% versus0% gap24/reference25=.96. MM0% versus9.1% intervals[-.5,.5] and[9.05,9.15] have gap8.55; MM0% versus27.3% gap26.75. A positive gap against a zero reference reproduces. Diagram EVT ambulation component interval[24,26]% agrees with eTable8[24.5,25.5] and does not overlap eTable9 zero interval. Half-unit count copies alone for1versus0 can touch; the printed percentage and plotted distribution comparisons independently establish the discrepancy.

**Focus area:** A/B. **Proposed review domain:** report_internal_inconsistency, because the same result is assigned to different treatment populations.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** Treatment attribution and direction for 90-day independence/ambulation in the ASPECTS6–10/core≥70mL discordant profile.

**Why context does not resolve it:** RouteA category2 applies to substituted numeric population attribution that reverses the arm with favorable outcomes. The matched denominators12/11 and profile definition are identical. eTable8's within-arm analysis is received-treatment whereas eTable9's treatment contrast is randomized allocation; the supplied report describes only MM-to-EVT crossovers. A crossover within this profile would increase the received-treatment EVT denominator and decrease MM's, while these displayed profile denominators remain12/11. The other discordant profile also has unchanged76/63 denominators; the concordant profile changes75/82 to74/83, locating its net transfer separately. Thus the reported population convention does not reproduce the movement of these favorable events with unchanged profile denominators. Modeling of treatment contrasts versus within-arm covariates does not change the descriptive event counts. This is not an adjustment-versus-crude effect comparison.

**Supported alternatives:** eTable8/figure or eTable9 may have a treatment-count placement discrepancy. eTable9 switches its general column order relative to eTable8,but has explicit MM/EVT headers; the human reader must decide which values belong to each arm. Composite-core eTable10 contains similarly shaped zero/nonzero rows,but no matching composite discordant2 distribution is supplied,so its intended arm attribution is not inferred or appended to the reproduced pattern.

**Exact human question:** Which arm had the1independence and3ambulation events in CTP/MRI discordant profile2,and how should eTable9 reconcile with eTable8 and eFigure20x?

### F-XS-105

**Title:** Core-volume measure for the age/time ambulation predictions is unclear between captions and explanations.

**Compared locations and document roles:** REPORT DOC-001 [physical p.10, Association of Age and Time With Functional Outcome After EVT](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10); REPORT DOC-006 [eFigure18 title/explanation, physical p.24](../../../joi240006supp5_prod_1708623115.01733.pdf#page=24), [eFigure19 title/explanation, physical p.25](../../../joi240006supp5_prod_1708623115.01733.pdf#page=25). Main M115/M116,support A039/A040. Proposed relationship S_C; all relationships S_C,S_W.

**Printed values/statements:** Main narrative discusses both time predictors,cites eFigures18/19,and states that the relationship was consistent across CT perfusion/MRI core volumes fixed at70,100,150mL. eFigure18 title specifies CTP/MRIcore,but its following explanation twice specifies composite core. eFigure19 title and explanation explicitly specify composite core70,100,150mL. Main p.3 defines composite as the maximum of CTP/MRIcore andCT hypodensity,so these are distinguishable numerical measurements.

**Rule and calculation:** A fitted contour fixed at70/100/150mL of one volume measurement is not identified by fixing a different volume measurement at the same numbers. Exact predicted coordinates are not supplied; no numerical discrepancy or preferred model is asserted. Display-precision arithmetic is inapplicable to measure identity.

**Focus area:** C. **Proposed review domain:** statistical_results.

**Qualifying route:** Route B.

**Affected result or extracted value:** Which core measurement produced the independent-ambulation prediction surfaces at70/100/150mL,and therefore which volume measure a reader could use to interpret the stated150mL prognosis.

**Why context does not resolve it:** The main definition distinguishes composite from perfusion/diffusion core; Figure18 contains competing explicit measurement labels,and Figure19 conflicts with the main paragraph’s shared CTP/MRIdescription. The contours lack a covariate legend or numerical fitted table identifying which volume entered each model. This is a quantity-changing label,not two names for the same measure or merely a missing model detail.

**Supported alternatives:** Figure18 may use CTP/MRI whileFigure19 uses composite; both may use composite; or shared explanatory text may not describe the depicted model. None is selected as a correction.

**Exact human question:** Which core-volume measurement was entered into each eFigure18/19 prediction model,and which70/100/150mL measure underlies the main narrative?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| Mainp.4 follow-up MRI8/336;p.9 MRI204; supplementp.51 eTable11 N101+24+79=204 | The additional support population corroborates the reproduced main follow-up MRI population discrepancy already emitted as F-NUM-001. Preservep.51 as an affected/corroborating location for that issue rather than creating another finding. | DUPLICATE_OF_INCLUDED |
| Mainp.5 Table1 versus supplementpp.35–36 eTable1 | Apparent differences in baseline copies,including median/IQRs,sex/race/referral/occlusion counts and time summaries,are baseline descriptive comparisons; explicitly168/168ITT versus170/166as-treated populations also distinguish them. No primary/key result or analysis-population size is changed. | PERIPHERAL_COMPARISON |
| Mainp.7 Table2/p.9 Table3 versus supplementpp.13–15forests/p.38 eTable2/p.32–34 distributions | Apparent34/170 versus34/168,66/170 versus65/168 and mismatch contributor differences arise between received-treatment and randomized groups. These are not matched arm-specific population definitions. Two MM-to-EVT crossovers explain the net arm/outcome transfers in the overall copies. | NOT_REPRODUCED |
| Mainp.9 infarct/growth narrative versus supplementpp.38/51 eTables2/11 | Follow-up infarct IQRs170(123–268)vs170(123–266),168(110–253)vs168(109–254),and MMgrowth95(56–125)vs95(56–135)are post hoc imaging-summary copies. The125/135 endpoint minimumgap9/135=.0667 exceedsprecision,but this exploratory outcome comparison does not change a primary/key outcome or analysis population. The difference is not an estimate-CI or test conflict. | PERIPHERAL_COMPARISON |
| MainTable2/3 footnotes pp.7/9 versus model methods p.4 and ratio labels in supplement | aRR expanded as absolute risk reduction versus evident modified-Poisson ratio,ratio null1 and explicit higher-rate-ratio footnote. The intended ratio quantity is identifiable immediately; no numeric computation as an alternative effect measure is established. | TERMINOLOGY_OR_WORDING |
| Mainp.8 mismatch-presence narrative/Table3p.9 versus eFigure17 continuous curves | Higher crude favorable-outcome proportions with binary mismatch presence do not establish that adjusted continuous mismatch-volume slopes must increase; they differ in contrast and modeling. The independent direction conflict with the explicit continuous narrative is retained in F-XS-102. | MODEL_VERSUS_CRUDE |
| Supplement eFigures7–13 pp.13–19 versus eFigure20 pp.26–34 | Apparent one-percentage-point differences when rounded mRS category percentages are cumulated,including independent rounding totals99–101%,reconcile after each segment’shalf-unit allowance; no separate distribution mismatch beyondF-XS-101/F-XS-104 was reproduced. | ROUNDING_OR_DISPLAY_PRECISION |

## Completion, limitations and derivative provenance

Findings:5(F-XS-101 throughF-XS-105). Excluded-observation rows:7. Scientific coverage gaps:None. All report matched-result groups above were checked without candidate-count calibration. Standalone inferential checks and all PLANrelationships remain assigned to their separate lanes.

Direct source extraction: Poppler26.01.0 `pdftotext -layout`,main physicalpp.4,8–11 and supplementpp.24–25,45–47,for exact narrative/caption confirmation. Candidate figure/cell authority additionally used fresh source rendering with `pdftoppm`26.01.0,CPU,`-scale-to1800 -png`: mainp.7 and supplementpp.13,14,19,23,47. Durable outputs are preprocessing/cross_reports/main-p7.png,supp-13.png,supp-14.png,supp-p19.png,supp-p23.png,supp-p47.png. Fresh mainp.7 and supplementpp.13,14,19,23,47 images were visually inspected; matched reusable source images supplied page7category reading andpp.32/45/46additional corroboration. Mainp.7direct render preserves a direct-source derivative for recheck. No OCR,Python extraction or GPU processing was used. Legacy image/text engines are unrecorded but source-linked assets were inventoried by curator. All source and reusable assets preserved.

Continuous prediction figures supply curve directions and legends but no exact fitted-point table; no coordinates were invented. eTable7 lacks explicit repeated treatment/interaction headers; surrounding as-treated conventions were retained as an evidence limitation,not used to manufacture a comparison. Composite discordant-profile2 has no supplied matched distribution sufficient to infer a treatment-attribution discrepancy from resemblance alone.

## Requested bounded REPORT-counterpart confirmation

This is a factual locator/absence handoff for the separate PLAN comparison lane, not a finding or screening decision. Complete REPORT coverage consists of main pp.1–14, results supplement pp.1–53, administrative DOC002 pp.1–30 and DOC007 p.1. Across that complete scope, no outcome/treatment-effect table, forest, distribution or narrative reports strata defined by **mismatch volume50mL or100mL**. Reported mismatch comparisons use the joint ratio/volume definitions≥1.2/≥10mL and≥1.8/≥15mL in main Figure1/Table3 and supplementary eFigures5–13,20/eTable7; eFigure17 p.23 treats mismatch volume continuously. The50/100mL appearances in core-volume bins/axis ticks and eligibility are different quantities and do not constitute those mismatch strata. This closes the supplied-REPORT counterpart search for DOC005p.6 section5.3.3 without inferring any external reporting.

Likewise no supplied REPORT display presents the combination of **age × time from last known well to randomization** for EVT independent-ambulation probability. The only matched age/time contour displays are eFigure18 p.24, using perfusion acquisition→reperfusion/end procedure, and eFigure19 p.25, using last known well→reperfusion/end procedure. Mainp.10 describes those two timing variables. Last-known-well→randomization appears elsewhere as baseline timing,adjustment variable and mismatch-profile time-bin analyses, not an age×time ambulation contour. This is the bounded no-counterpart result for DOC005p.5 section5.2.3's stated combination. A statistical/plan reviewer independently decides the inclusion implication.
