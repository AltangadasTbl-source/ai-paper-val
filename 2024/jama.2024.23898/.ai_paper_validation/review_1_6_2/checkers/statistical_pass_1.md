# Statistical consistency review — pass 1

Runtime agent ID: 01a129b6-dd28-7c32-bf59-a2509c3c5d7d. Model gpt-6.1-sol; reasoning effort high; FRESH_SPAWN. Exact scope: all 105 stable relationships S001–S105 in statistics/relationship_inventory.md, covering all five supplied source documents through the complete fresh maps and source-confirmed inferential locations. Every S record is PASS_1_COMPLETE. Twelve findings; eleven excluded apparent observations. Findings are self-screened observations for independent inclusion screening, not adjudications. No candidate IDs assigned.

The complete scope and review contract were read. Main/statistical result authority is direct supplied PDF content. Main Table 2 p.6 and subgroup eFigure p.2 spatial values/legend were also checked visually in source-linked reusable images. Main pp.4–8, protocol pp.16–18,24,40–41,60 and SAP pp.3,9–16,20–22,26–27,31–38 were reread in direct Poppler layout extraction. Engine pdftotext26.01.0; CPU; no new OCR; no raw data or external sources. Original sources and prior artifacts preserved.

## Inferential checks and diagnostics

All main and subgroup point estimates are within ordered intervals. Primary RR/absolute-difference intervals include their null and P=.54/.49 agree. All 24 modeled continuous estimates have ordered intervals, contained points and compatible displayed P values; day5 EQ-5D alone excludes0 and printsP=.04. All five interaction P values exceed the prespecified .01; individual subgroup intervals/testP are not paired hypotheses. Time-to-event and LOS rows supply no P value. No significance was invented for them.

Primary and per-protocol estimates, continuous scores, and LOS are explicitly adjusted/modeled. No crude count ratio, independent-groups standard error, or raw mean difference was substituted as authoritative model output. A symmetric normal-Wald diagnostic from continuous interval widths gives displayed-compatible P values, but model-specific degrees of freedom/covariance/output are absent; the diagnostic cannot establish exact reproduction. No fitted statistic or standard error is printed to permit an additional exact equality test.

Power diagnostics use equal-arm normal two-proportion calculations only: 40%→26.8% requires about532.4 total before continuity adjustment, about562.3 with a usual continuity diagnostic; 30%→18% about528.2 before adjustment; 20%→10% about531.7. At562, uncorrected diagnostic powers are about.915,.917,.915 respectively. These support the printed nominal90% and similar-power statements, without asserting an unreported calculation engine. Changing from nonreturn40→26.8% to return60→73.2% changes relative reduction33% to relative increase22% but leaves absolute13.2 points unchanged. No sample-size finding follows from these diagnostics.

The RCT is superiority; no noninferiority/equivalence margin or such claim is supplied. No minimally-invasive efficacy interim occurred or was claimed; open-trial group-sequential plans are expressly separate and closed. Primary no-significant-benefit conclusion agrees with the primary interval. No secondary multiplicity adjustment is planned in SAP §11.1. Clinical-importance margins are not supplied, so no quantitative equivalence interpretation was imposed on precision rhetoric.

## Findings

### F-ST1-001

**Title:** Blanket secondary nonsignificance statement does not reconcile with the EQ-5D day5 result.

**Relationship IDs:** S031, S041, S101. **Focus area:** B. **Proposed review domain:** statistical_results. **Proposed relationship type / All relationships:** S_W / S_W.

**Exact locations and roles:** REPORT [main Table 2, PDF p.6](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6), EQ-5D postoperative day5 row; REPORT [main p.5](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5), Secondary Outcomes paragraph; REPORT [abstract p.1](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=1), Results; REPORT [discussion p.7](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=7) and [p.8](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8), no-benefit statements. PLAN [SAP p.14](../../../joi240139supp2_prod_1741633738.17362.pdf#page=14) establishes no adjustment to secondary outcomes for multiple testing; it corroborates the significance rule and is not an additional document relationship.

**Printed values/statements:** Day5 EQ-5D modeled treatment difference−0.057,95%CI−0.111to−0.003,P=.04; higherEQ-5D means better quality of life. Main p.5 states no significant difference in quality of life; abstract states no statistically significant differences in any11 secondary outcomes; discussion states no benefit on any11, including quality of life. Clinical no-benefit is distinct from nonsignificance and is retained as context.

**Rule and calculation:** At the stated/default two-sided 5% level, .04<.05, and the95%interval excludes0. The printed upper-limit rounding interval[−.0035,−.0025] remains below0 and the printedP interval[.035,.045] remains below.05. No secondary multiplicity rule changes that level; .01 applies only to subgroup interactions. The interval and printed P agree with each other but conflict with the stated nonsignificant test conclusion for this secondary endpoint. Display-relative-discrepancy screening does not apply to routeAcategory1.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** EQ-5D day5 treatment difference−.057 and the extraction of a statistically nonsignificant versus significant secondary quality-of-life contrast.

**Why context does not resolve it:** This is an always-register interval-versus-stated-test conflict. The direction favors placebo, so a no-lidocaine-benefit claim can coexist with the table; the specific no-significant-difference claim cannot be reconciled by direction.

**Alternatives and missing definitions:** A nonsignificant overall longitudinal/global quality-of-life test might underlie the narrative, while the printed row is a time-specific contrast. No such global statistic/P or mapping is supplied. If that is the explanation, the analyses are different and both should be identified; routeA still applies.

**Exact human question:** Does the nonsignificant quality-of-life statement refer to an unreported overall test, and how should it be distinguished from the printed day5 difference, interval andP=.04?

### F-ST1-002

**Title:** The subgroup display assigns two confidence levels to the same printed intervals.

**Relationship IDs:** S046–S058, S078. **Focus area:** B/C. **Proposed review domain:** statistical_results. **Proposed relationship type / All relationships:** S_W / S_W.

**Exact locations and roles:** REPORT [result supplement eFigure p.2](../../../joi240139supp3_prod_1741633738.18862.pdf#page=2), horizontal-line legend and sentence immediately below the graph. PLAN [SAP p.15](../../../joi240139supp2_prod_1741633738.17362.pdf#page=15), corresponding99%subgroup intervals, is corroborating context rather than a conflicting implemented-analysis observation.

**Printed values/statements:** Graph legend says99%CI; prose says right-side numbers are within-subgroup relative risks and95%confidence interval. Printed subgroup intervals:6h .92(.73,1.15),12h1.03(.82,1.28),nonright .95(.78,1.15),right .99(.76,1.28),female .95(.78,1.16),male .98(.77,1.26),age50–74 .95(.77,1.16),age<50 .82(.49,1.37),age≥75 1.12(.78,1.59),ERAShigh .96(.82,1.12),moderate .99(.76,1.29),low1.01(.49,2.08). Overall .97(.88,1.07) matches the main95%CI.

**Rule and calculation:** One numeric interval cannot simultaneously be designated a95% and99%interval for the same analysis. The level is an exact inferential definition, not a rounded estimated percentage; display-precision arithmetic is not an estimate-recomputation comparison here. All points are contained and all intervals include1; none is paired to the factor interactionP as the same hypothesis. If normal-log intervals were otherwise identical,99/95half-width ratio would be2.5758/1.9600≈1.314; this is a diagnostic illustration, not reconstruction of the models.

**Qualifying route:** Route B.

**Affected result or extracted value:** The confidence level attached to every extracted subgroupRRinterval and whether the reported interval corresponds to the planned .01 subgroup convention.

**Why context does not resolve it:** Both definitions are printed adjacent to the same graph; the source supplies no within-subgroup standard errors or model output that identifies which confidence level generated the numeric limits. The overall95%interval also appears inside the99%legend display.

**Alternatives and missing definitions:** The horizontal graphical intervals could be99%while separately printed numbers are95%, or one label might describe the intended convention. Source does not identify two separate numeric interval sets or label that distinction. The point-and-line geometry broadly tracks the right-side numbers.

**Exact human question:** Are the printed within-subgroup numeric limits95%or99%, do the plotted line intervals differ, and which confidence level applies to the overall row?

### F-ST1-003

**Title:** The supplied protocol's primary logit analysis is replaced by a log-link analysis.

**Relationship IDs:** S004, S070. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type / All relationships:** P_R / P_R, P_P.

**Exact locations and roles:** PLAN [protocol §10.2, p.40](../../../joi240139supp1_prod_1741633738.16362.pdf#page=40); PLAN [SAP version history p.3](../../../joi240139supp2_prod_1741633738.17362.pdf#page=3), [§11.3 p.14](../../../joi240139supp2_prod_1741633738.17362.pdf#page=14), [primary code p.34](../../../joi240139supp2_prod_1741633738.17362.pdf#page=34); REPORT [main methods p.5](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5) and [primary Table 2 p.6](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6).

**Printed values/statements:** Protocol primary GLM logit link with minimization covariates. Main primary GLM log link produces adjustedRR.97(.88,1.07),P=.54. SAP current version also log link and samplePoisson/log/robust code; history says section11.3 had statedlogit, changed09/09/2024 after analysis completion to match the log-link analysis.

**Rule and calculation:** Logit and log specify different primary link functions and effect scales. The planned logit primary analysis is not reported in supplied results; current SAP/report align after the disclosed update. This logical model comparison has no rounded-input interval or relative numeric gap.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Planned primary model and interpretation of the primaryRR.97(.88,1.07), as compared with the protocol's logit-based analysis.

**Why context does not resolve it:** RouteA registers a planned primary analysis not reported. The SAP explicitly explains the documentary change, and that explanation is retained; it does not supply the planned logit result or establish a prospectively revised protocol model.

**Alternatives and missing definitions:** SAP history describes original link wording as a documentation omission/slip rather than an intended model change. If contemporaneous prespecification outside the supplied package established log link, that would resolve the plan-history interpretation, but it is not supplied. No preferred model is proposed; both links can be coherent.

**Exact human question:** Was the log-link primary analysis prospectively specified despite the supplied protocol's logit statement, and is a logit primary analysis available or was it explicitly superseded?

### F-ST1-004

**Title:** Planned unadjusted primary analyses are not reported.

**Relationship IDs:** S007, S008, S090. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type / All relationships:** P_R / P_R.

**Exact locations and roles:** PLAN [SAP Table 13.8 p.20](../../../joi240139supp2_prod_1741633738.17362.pdf#page=20); REPORT [main primary narrative p.5](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5), [Table 2 p.6](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6), [Table 2 footnote c p.7](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=7); REPORT [result supplement p.2](../../../joi240139supp3_prod_1741633738.18862.pdf#page=2). Complete remaining result units including sharing statement checked via maps; no additional results document supplied.

**Printed values/statements:** Planned Table 13.8 contains unadjusted and adjusted model estimates,95%CIs andP for both ITT and per-protocol. Main estimates are explicitly minimization-adjusted:ITT RR.97(.88,1.07),P=.54;PP RR.96(.86,1.07),P=.49. Printed counts are160/279 versus164/278 and154/267 versus158/265.

**Rule and calculation:** Two planned unadjusted primary model rows have no matching estimate/interval/test row in any supplied REPORT. Crude ratios derivable from printed counts do not supply those missing planned model intervals/tests. This is a report-absence comparison, not a crude-versus-adjusted discrepancy; no numerical display interval applies.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** The prespecified unadjusted primary GI-3 effects inITT/PP and the completeness of the primary analysis set available for extraction.

**Why context does not resolve it:** A planned primary analysis not reported is always-register. The adjusted rows and raw counts identify other results, not the omitted unadjusted model output.

**Alternatives and missing definitions:** The authors may have selected adjusted models for concise publication or made full unadjusted output available elsewhere. No such output or explicit abandonment is supplied.

**Exact human question:** Where are the planned unadjustedITT andPP primary estimates, confidence intervals and tests, or was their reporting prospectively changed?

### F-ST1-005

**Title:** The unconditional planned Edinburgh-versus-other-centres primary sensitivity analysis is not reported.

**Relationship IDs:** S088. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type / All relationships:** P_R / P_R.

**Exact locations and roles:** PLAN [SAP §11.6 p.15](../../../joi240139supp2_prod_1741633738.17362.pdf#page=15); REPORT [main analysis/results p.5](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5), [primary Table 2 p.6](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6), [discussion p.7](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=7), [limitations p.9](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=9), and REPORT [complete subgroup supplement p.2](../../../joi240139supp3_prod_1741633738.18862.pdf#page=2). The complete fresh result maps contain no Edinburgh comparison.

**Printed values/statements:** SAP says sponsorEdinburgh expected largest recruiter and therefore a sensitivity analysis comparingEdinburgh with the rest of centres will be performed. Published subgroup factors are intendedinfusion,operation,sex,age,ERAS; primary sensitivities reported includePP and actualduration exploration, not Edinburgh.

**Rule and calculation:** There is no matching primary sensitivity method/result in supplied REPORT material. This sentence is unconditional; the preceding>10%missingness condition applies to missing-data sensitivity, not to the independent sponsor-site paragraph. No rounding calculation applies to absence of a prespecified primary analysis.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified primary GI-3 sensitivity to sponsor-site versus other-site composition, used to interpret the reported robustness of the primary result.

**Why context does not resolve it:** Planned primary sensitivity analysis not reported is an always-register category; a generic robustness statement does not provide it.

**Alternatives and missing definitions:** The comparison may have been performed but omitted, or the expected largest-site premise may have changed. The plan does not state that the analysis occurs only ifEdinburgh proves largest, and the report gives no amendment/result.

**Exact human question:** Was the Edinburgh-versus-other-centres primary sensitivity performed, and where is its result or a documented change to that plan?

### F-ST1-006

**Title:** The postoperative opioid endpoint window changes from72 hours to24 hours.

**Relationship IDs:** S041, S081. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type / All relationships:** P_R / P_R.

**Exact locations and roles:** PLAN [protocol secondary opioid endpoint p.17](../../../joi240139supp1_prod_1741633738.16362.pdf#page=17), [collection p.33](../../../joi240139supp1_prod_1741633738.16362.pdf#page=33) and [p.35](../../../joi240139supp1_prod_1741633738.16362.pdf#page=35); PLAN [SAP schedule p.11](../../../joi240139supp2_prod_1741633738.17362.pdf#page=11); REPORT [main outcome list p.4](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4), [secondary results p.5](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5), [Table 2 p.6](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6).

**Printed values/statements:** Protocol cumulative morphine-equivalent consumption until72 hours afteroperationstart; SAP in-hospital consumption up to72 hours. Main endpoint consumption up to24 hours; mediansIQR70.6(30.0,150.0) versus45.0(17.1,98.6), n 210 each; table separately lists intraoperative opioid.

**Rule and calculation:** The integration window72h differs from24h by48h and changes the endpoint quantity. These exact scheduled boundaries are not rounded estimates; no half-unit/display rule can identify the72h total from24h medians. No72h result or amendment is supplied.

**Qualifying route:** Route B.

**Affected result or extracted value:** Total postoperative opioid consumption70.6 versus45.0mg OME and which planned observation window those descriptive results represent.

**Why context does not resolve it:** The report consistently labels24h and the plan consistently labels72h; the supplied material does not explain replacement or give both results. A data extractor cannot treat the24h values as the planned72h outcome.

**Alternatives and missing definitions:** The72h endpoint may have been replaced, abbreviated for publication, or unavailable; the supplied package does not distinguish these possibilities. No significance test was reconstructed from medians.

**Exact human question:** Was the planned72h opioid endpoint changed to24h, and where are the72h consumption results or the documented change?

### F-ST1-007

**Title:** Specific planned discharge-time displays and sample code differ from the reported Cox models.

**Relationship IDs:** S005, S036, S037, S084. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type / All relationships:** P_R / P_R, P_P.

**Exact locations and roles:** PLAN [SAP §11.4 p.14](../../../joi240139supp2_prod_1741633738.17362.pdf#page=14), [Tables13.21–13.22 p.26](../../../joi240139supp2_prod_1741633738.17362.pdf#page=26), [sample code p.36](../../../joi240139supp2_prod_1741633738.17362.pdf#page=36); REPORT [main methods p.5](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5), [Table 2 rows and footnote d p.7](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=7).

**Printed values/statements:** SAP discharge/readiness table footnotes specify GLM; code uses `meglm Time_medicalcriteria...` and `meglm Time_readiness...`, with random centre and robust variance, without family/link. The SAP general paragraph specifies Cox for time-to-event outcomes. Main explicitly reports Cox and HR0.99(0.84,1.17), HR0.99(0.83,1.17), adjusted for age, sex and centre.

**Rule and calculation:** The endpoint-specific plan displays/code and the report identify different model classes for the same two discharge endpoints; the SAP itself also has a general Cox instruction. No GLM family/link is inferred from defaults, and no Cox covariance is reconstructed. This logical model comparison has no numerical rounding gap.

**Qualifying route:** Route B.

**Affected result or extracted value:** Planned-versus-reported analysis for medical discharge/readiness and interpretation of the published hazard ratios.

**Why context does not resolve it:** The report unambiguously gives Cox, but the plan's specific tables/code give GLM while its general instruction gives Cox. Nothing identifies which plan instruction supersedes the other. A reader reconstructing the planned analysis has two specifications.

**Alternatives and missing definitions:** The code is expressly sample code and may differ from implementation; the general Cox instruction may govern. This is a credible alternative for independent screening, but the specific specifications remain printed. No effect scale is assigned to the unspecified GLM family/link.

**Exact human question:** Were discharge/readiness always intended to use Cox under the general SAP rule, and how should the endpoint-specific GLM displays/code be interpreted relative to the published HRs?

### F-ST1-008

**Title:** The ERAS sample model omits age despite the plan's minimization-covariate interaction specification.

**Relationship IDs:** S063, S099. **Focus area:** D. **Proposed review domain:** plan_material. **Proposed relationship type / All relationships:** P_P / P_P.

**Exact locations and roles:** PLAN [SAP §11.3–11.5 p.14](../../../joi240139supp2_prod_1741633738.17362.pdf#page=14), [p.15](../../../joi240139supp2_prod_1741633738.17362.pdf#page=15), and [ERAS code p.38](../../../joi240139supp2_prod_1741633738.17362.pdf#page=38). REPORT [main primary-model interaction description p.5](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5) corroborates the general adjustment specification; REPORT [ERAS results p.2](../../../joi240139supp3_prod_1741633738.18862.pdf#page=2) identifies the affected result, without establishing the implemented model.

**Printed values/statements:** Primary model includes age, sex and centre; subgroup interactions use models outlined above. ERAS code `meglm i.GI3 i.IV##i.ERAS i.Male || CentreNo:, family(poisson) link(log) vce(robust) eform` omits AgeBand, while other factor code retains it where applicable. ERAS RRs0.96(0.82,1.12),0.99(0.76,1.29),1.01(0.49,2.08), interactionP=.966.

**Rule and calculation:** Adding an ERAS interaction to the stated primary model retains unrelated minimization covariates. ERAS is not itself age, so its code's omission of age differs from the stated covariate set. This logical covariate comparison has no rounding calculation.

**Qualifying route:** Route B.

**Affected result or extracted value:** Adjustment specification used to interpret/reproduce the ERAS subgroup RRs and interactionP=.966.

**Why context does not resolve it:** Code and prose give different covariate sets, with no stated age exception for ERAS. The result display gives no fitted covariates or model output.

**Alternatives and missing definitions:** Code may be illustrative or abbreviated while actual analysis retained age, or age may have been intentionally omitted. Actual implementation is not assumed from sample code. No preferred model is proposed.

**Exact human question:** Did the ERAS model include age, and is the code's age omission an intended exception or an incomplete representation of the primary-model specification?

### F-ST1-009

**Title:** GI-2/GI-3 survival-variable definitions use anesthesia as origin while endpoint prose uses operation start.

**Relationship IDs:** S009, S010, S082. **Focus area:** D. **Proposed review domain:** plan_material. **Proposed relationship type / All relationships:** P_P / P_P.

**Exact locations and roles:** PLAN [protocol endpoint p.16](../../../joi240139supp1_prod_1741633738.16362.pdf#page=16); PLAN [SAP endpoint p.9](../../../joi240139supp2_prod_1741633738.17362.pdf#page=9), [composite p.33](../../../joi240139supp2_prod_1741633738.17362.pdf#page=33), [survival variables p.34](../../../joi240139supp2_prod_1741633738.17362.pdf#page=34). REPORT [main Figure 2 p.8](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8) says days since surgery and corroborates the prose; REPORT [time-to-GI3/GI2 p.6](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6) identifies affected results. Neither establishes the implemented timestamp definition.

**Printed values/statements:** Endpoint time is from surgery/start of operation to the later diet and GI component. SAP code variable Time is defined from start of general anesthetic to GI2/GI3. Main Cox HR0.98(0.83,1.17) for GI3 and1.03(0.86,1.23) for GI2; figure axis says days since surgery.

**Rule and calculation:** Start of anesthesia and start of operation are different named events. Elapsed recovery time is event timestamp minus origin timestamp; changing origin changes individual elapsed time by the operation/anesthesia start difference. That delay is not supplied, so no constant-shift or no-effect assumption is made. Exact definitions are not rounded estimates.

**Qualifying route:** Route B.

**Affected result or extracted value:** Defined origin of GI2/GI3 survival time and the GI3 distribution, needed to extract elapsed time consistently.

**Why context does not resolve it:** Both origins are printed as analysis definitions; no timestamp mapping or priority statement identifies the actual Time variable. Anesthesia induction is explicitly part of the treatment before operation, so the terms need not identify the same event.

**Alternatives and missing definitions:** Sample code may use loose wording while implementation uses operation start, or vice versa. The delay and implemented variable construction are absent; no quantitative effect-size impact is asserted.

**Exact human question:** Was GI2/GI3 survival time measured from operation start or general-anesthetic start, and how does that match the prespecified endpoint and figure origin?

### F-ST1-010

**Title:** Total length of stay is assigned tertiary and secondary status within the report.

**Relationship IDs:** S041, S045, S087. **Focus area:** D. **Proposed review domain:** report_internal_inconsistency. **Proposed relationship type / All relationships:** S_W / S_W.

**Exact locations and roles:** REPORT [main outcomes p.4](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4), [discussion p.7](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=7), [Table 3 p.8](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8). PLAN [protocol p.16](../../../joi240139supp1_prod_1741633738.16362.pdf#page=16) and [SAP p.10](../../../joi240139supp2_prod_1741633738.17362.pdf#page=10) corroborate tertiary status; they add no conflicting relationship.

**Printed values/statements:** Outcomes lists LOS among 5 tertiary objectives; Table 3 is titled Tertiary/Safety Outcomes. Discussion says no benefit on any11 secondary endpoints including total LOS. LOS means6.0(5.9) versus5.8(4.5), IRR1.03(0.92,1.14).

**Rule and calculation:** The same LOS result is tertiary in objectives/results and secondary in discussion. The11-item secondary list onp.4 excludes LOS. Endpoint status is categorical prespecification, not rounding.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified status of LOS and membership of the11-secondary-endpoint summary.

**Why context does not resolve it:** RouteA registers outcome-status changes. Both status statements are explicit and cannot identify the same listed11 secondary outcomes.

**Alternatives and missing definitions:** Discussion may use secondary colloquially for nonprimary outcomes while formal tertiary status remains intended. The claim nevertheless names a formal11-endpoint set, so the alternative does not erase the printed status difference.

**Exact human question:** Should LOS be tertiary as in objectives/Table 3, and which11 outcomes belong to the discussion's secondary-endpoint statement?

### F-ST1-011

**Title:** The reported readmission window is90 days while the planned endpoint is30 days.

**Relationship IDs:** S045, S086. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type / All relationships:** P_R / P_R, P_P, S_W.

**Exact locations and roles:** PLAN [protocol objectives p.16](../../../joi240139supp1_prod_1741633738.16362.pdf#page=16) and [endpoint p.18](../../../joi240139supp1_prod_1741633738.16362.pdf#page=18); PLAN [SAP outcome p.10](../../../joi240139supp2_prod_1741633738.17362.pdf#page=10), [Table 13.23 p.27](../../../joi240139supp2_prod_1741633738.17362.pdf#page=27); REPORT [main objectives p.4](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4), [Table 3 p.8](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8).

**Printed values/statements:** Protocol objective30 days after discharge; protocol endpoint/SAP 30 days after operation; main objective30 days after surgery; Table 3 after discharge and within90 days after operation,31(11.1%) versus34(12.2%).

**Rule and calculation:** Published90 days after operation differs from planned30 days after operation. The protocol also uses30 days after discharge as an alternative origin. These exact endpoint windows are not rounded quantities; the30day counts cannot be identified from90day counts.

**Qualifying route:** Route B.

**Affected result or extracted value:** Readmission31/34 and11.1%/12.2%, with follow-up horizon and origin for extraction.

**Why context does not resolve it:** Planned day90follow-up collects later admissions, but that does not identify Table 3 as replacing the30day endpoint. The30day numbers are absent, and alternative operation/discharge origins remain in the plan.

**Alternatives and missing definitions:** The90day table may show additional exploratory results, or its label may differ from the actual count window. The source does not identify which window produced31/34.

**Exact human question:** Do31/34readmissions refer through30or90 days, from operation or discharge, and where is the prespecified30day result?

### F-ST1-012

**Title:** The reported safety population includes nonrecipients while the SAP specifies recipients.

**Relationship IDs:** S069. **Focus area:** A/D. **Proposed review domain:** protocol_report. **Proposed relationship type / All relationships:** P_R / P_R.

**Exact locations and roles:** PLAN [SAP safety p.13](../../../joi240139supp2_prod_1741633738.17362.pdf#page=13); REPORT [main Figure 1 p.3](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=3), receipt and safety boxes; REPORT [Table 3 p.8](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8), group headings and footnotee.

**Printed values/statements:** SAP safety data for all randomized participants who received IMP. Figure 1 receipts267lidocaine/265placebo, nonreceipt12/13; one extra excluded placebo recipient enters safety. Figure 1 safety279/279. Table 3 headings279/278 plus the extra placebo footnote; AE40(14.3%)/37(13.3%), SAE4(1.4%)/9(3.2%).

**Rule and calculation:** Planned recipient safety set267+(265+1)=533; printed safety279+279=558, a difference25, equal to12+13 nonrecipients. These are exact discrete counts. This compares analysis-set specifications rather than rounding of percentages. The additional placebo recipient explains one exclusion, but does not account for retaining25 nonrecipients.

**Qualifying route:** Route B.

**Affected result or extracted value:** Safety population sizes and denominators behind AE/SAE proportions, including participants unexposed to study treatment.

**Why context does not resolve it:** The SAP specifies exposure-based safety; Figure 1 expressly labels all primary participants plus one additional recipient. The footnote does not explain all nonrecipients' inclusion.

**Alternatives and missing definitions:** Safety may have expanded to eligibleITT participants, or Figure 1 may show available data while an exposed subset supplied the analysis. The report does not distinguish these possibilities. No change in event counts or preferred analysis is asserted.

**Exact human question:** Was safety analyzed in279/279 participants or267/266 recipients, and how does that relate to the SAP's recipient definition and printed AE/SAE proportions?

## Excluded observations

Only apparent issues deliberately not emitted appear here. Reconciled checks are in the S records. Each row has exactly one reason code; pass2 must reread every row against routeA and display precision.

| Location | Observation | Reason code |
|---|---|---|
| Main pp.5–8/Table 2/3; S007–S039 | Adjusted RR/RD/continuous differences and modeled LOS differ from crude ratios or observed means, including some raw/model sign contrasts. Adjustment/interactions are explicit. | MODEL_VERSUS_CRUDE |
| Main pp.5–6 PONV, opioid, ERAS; S080 | Simple reconstructed tests might challenge nonsignificance in descriptive-only rows, but actual tests/model output are absent. No printed interval/test conflict exists for those rows. The independent EQ-5D conflict is emitted. | CONDITIONAL_OR_UNREPORTED |
| Main baseline/follow-up n; SAP p.16; S073 | Missing-baseline imputation and fitted-model inclusion are not specified in output; observed n alone does not establish a contradiction. | CONDITIONAL_OR_UNREPORTED |
| Protocol p.60; S094 | Worked OBAS example totals9 under its coherent scoring rule but prints8. An illustrative plan example does not change a primary/key result, analysis population or planned decision rule. | PERIPHERAL_COMPARISON |
| SAP p.32; protocol p.61/main p.7; S095 | Literal '=5' in one appendix sentence versus≥5in dummy table/protocol/report. The intended relational symbol is obvious from surrounding plan/table context; no changed result/composite calculation is demonstrated. | NOTATION_OR_TYPOGRAPHY |
| SAP pp.35–36; S071 | Sample 'memixed' spelling differs from prose linear mixed model. The model is clear from prose and random-effect/time-interaction specification; no number conflicts. | NOTATION_OR_TYPOGRAPHY |
| Supplement p.2/main p.4/protocol p.41; S050 | Right subgroup301 includes272 right plus29extended-right. Protocol expressly groups right/extended-right; the abbreviated label does not obscure effect identity. | TERMINOLOGY_OR_WORDING |
| Supplement p.2; S047–S048 | Intended-duration counts271+261=532 rather than557. Equality with PP n does not prove all nonrecipients had defined intended duration or establish an implemented subgroup exclusion rule. Membership definition is absent. | CONDITIONAL_OR_UNREPORTED |
| Protocol p.18/SAP p.15/supplement p.2; S076–S077 | ERAS added to SAP after analysis, but protocol contains it prospectively. Protocol grades are examples; supplement expressly says thresholds were not predefined. No separate plan-absent subgroup inferred. | CONTEXT_RESOLVES |
| SAP p.36/p.26/protocol p.18; S100 | Medical-criteria variable description says time to discharge, although its name/title and five criteria identify readiness. Actual use of discharge date is not demonstrated; wording alone does not establish another reported outcome. | TERMINOLOGY_OR_WORDING |
| Protocol pp.41–42/SAP p.10; S091 | Economic output is absent from clinical results, but a separate economic plan is expressly required. No supplied HEAP/key economic result establishes an unconditional primary/key-secondary clinical-analysis omission. | CONDITIONAL_OR_UNREPORTED |

## Limitations and pass-2 handoff

No scientific coverage gap remains. Exact model reproduction is limited by missing fitted output, raw data, covariance, standard errors, test statistics/degrees of freedom, implemented code and subgroup membership definitions. Diagnostic approximations support no finding alone. Missing planned primary analyses are assessed against the complete REPORT union. Every finding requires independent screening and source recheck if included. A distinct fresh statistical agent must revisit all 105S IDs, the complete ledger, screening/recheck facts and all eleven exclusions; this agent cannot perform pass2.

## Explicit pass-1 relationship completion records

The following complete original pass-1 records are copied mechanically from the specialist's durable [statistical inventory](../statistics/relationship_inventory.md), omitting only the later pass-2 column. Original source evidence, pass-1 checks and PASS_1_COMPLETE states are unchanged. This adds individual ID locators to the checker, not a new scientific pass. Source-file keys are M main article, P protocol, A SAP, R subgroup report and D data-sharing report, using the exact filenames defined in the inventory.

## Main-paper relationships

| ID | Exact source location and relationship | Printed statistical evidence, population, time and model | Pass 1 |
|---|---|---|---|
| S001 | pp.2-4 randomization, intervention and population | Individual adult randomization1:1; age<50,50-74,≥75,sex,site strata;2% lidocaine vs0.9%saline schedule N 004/N 043; eligible surgery N 021; masked patients/site outcome collection | PASS_1_COMPLETE |
| S002 | pp.4-5 sample size, primary superiority assumption | n 562;90% power;two-sided 5%;primary72 h recovery increase60% to73.2%,relative22%,absolute13.2%;effect direction L benefit | PASS_1_COMPLETE |
| S003 | p.5 sample-size secondary assumption | Same n 562 similar power for ileus reduction20% to10%,absolute10%,failure GI-3 at5 d | PASS_1_COMPLETE |
| S004 | p.5 primary model and analysis set | GLM log-link;fixed sex,age category;random trial site;primary set557;PP excludes nonrecipients;no primary missing;secondary observed data;95%CIs;Stata17 | PASS_1_COMPLETE |
| S005 | p.5 secondary/survival/repeated-measure methods,p.7 footnotes | Similar approach appropriate links;Cox regression for time-to-event;KM empirical distribution;PH test no evidence of violation;linear mixed model interaction time×treatment per footnote f;minimization adjustment age/sex/center;negative-binomial LOS per p.8 | PASS_1_COMPLETE |
| S006 | pp.4-5 subgroup specification and testing | Primary treatment×subgroup interactions;stricter two-sided1% significance;intended6/12 h,right/nonright,sex,age categories,high/low ERP;post hoc actual duration mentioned separately;all preplanned subgroup claims linked to supplement | PASS_1_COMPLETE |
| S007 | p.1 abstract,p.5 text,p.6 primary Table 2 | L160/27957.3% vs P164/27859.0%;adjusted absolute difference−1.9 percentage points (−8.0,4.2);RR0.97 (0.88,1.07),P.54 in body/table;GLM log-link minimization adjusted;GI-3 at72 h | PASS_1_COMPLETE |
| S008 | p.5 text,p.6 Table 2 PP | L154/26757.7% vs P158/26559.6%;absolute difference−2.3 pp (−8.9,4.3);RR0.96 (0.86,1.07),P.49;PP recipients;same primary endpoint/model | PASS_1_COMPLETE |
| S009 | p.6 Table 2 timeGI-3,p.8 Figure 2 | L275/27998.6%,P275/27898.9%;Cox adjusted HR0.98 (0.83,1.17);no P printed;recovery-event direction;Figure 2 N 099 | PASS_1_COMPLETE |
| S010 | p.6 Table 2 timeGI-2 | L261/27993.5%,P256/27892.1%;Cox adjusted HR1.03 (0.86,1.23);no P printed | PASS_1_COMPLETE |
| S011 | p.6 Table 2 prolonged ileus | L44/27915.8%,P39/27814.0%;absolute1.8 pp (−3.3,6.8);printed IRR1.13 (0.80,1.61);GLM log-link footnote b,c;no P printed;failure GI-3 by120 h | PASS_1_COMPLETE |
| S012 | p.6 OBAS day1,N 054 |0.086 (−0.505,0.678),P.78;linear mixed time interaction | PASS_1_COMPLETE |
| S013 | p.6 OBAS day2,N 055 |−0.574 (−1.176,0.027),P.06;linear mixed time interaction | PASS_1_COMPLETE |
| S014 | p.6 OBAS day3,N 056 |−0.296 (−0.924,0.332),P.36;linear mixed time interaction | PASS_1_COMPLETE |
| S015 | p.6 OBAS day4,N 057 |0.565 (−0.148,1.279),P.12;linear mixed time interaction | PASS_1_COMPLETE |
| S016 | p.6 OBAS day5,N 058 |0.231 (−0.641,1.102),P.60;linear mixed time interaction | PASS_1_COMPLETE |
| S017 | p.6 OBAS day6,N 059 |0.696 (−0.328,1.720),P.18;linear mixed time interaction | PASS_1_COMPLETE |
| S018 | p.6 OBAS day7,N 060 |0.278 (−0.300,0.856),P.35;linear mixed time interaction | PASS_1_COMPLETE |
| S019 | p.6 QoR-15 day1,N 064 |1.22 (−1.27,3.70),P.34;linear mixed time interaction | PASS_1_COMPLETE |
| S020 | p.6 QoR-15 day2,N 065 |−1.22 (−3.77,1.33),P.35;linear mixed time interaction | PASS_1_COMPLETE |
| S021 | p.6 QoR-15 day3,N 066 |1.17 (−1.46,3.80),P.38;linear mixed time interaction | PASS_1_COMPLETE |
| S022 | p.6 QoR-15 day4,N 067 |−2.28 (−5.38,0.81),P.15;linear mixed time interaction | PASS_1_COMPLETE |
| S023 | p.6 QoR-15 day5,N 068 |0.23 (−3.47,3.93),P.90;linear mixed time interaction | PASS_1_COMPLETE |
| S024 | p.6 QoR-15 day6,N 069 |1.75 (−2.60,6.09),P.43;linear mixed time interaction | PASS_1_COMPLETE |
| S025 | p.6 QoR-15 day7,N 070 |0.21 (−2.24,2.66),P.86;linear mixed time interaction | PASS_1_COMPLETE |
| S026 | p.6 QoR-15 day30,N 071 |0.31 (−2.11,2.73),P.80;linear mixed time interaction | PASS_1_COMPLETE |
| S027 | p.6 EQ-5D day1,N 073 |−0.005 (−0.042,0.032),P.78;linear mixed time interaction | PASS_1_COMPLETE |
| S028 | p.6 EQ-5D day2,N 074 |0.005 (−0.033,0.042),P.81;linear mixed time interaction | PASS_1_COMPLETE |
| S029 | p.6 EQ-5D day3,N 075 |−0.018 (−0.057,0.021),P.37;linear mixed time interaction | PASS_1_COMPLETE |
| S030 | p.6 EQ-5D day4,N 076 |−0.011 (−0.055,0.034),P.64;linear mixed time interaction | PASS_1_COMPLETE |
| S031 | p.6 EQ-5D day5,N 077 |−0.057 (−0.111,−0.003),P.04;linear mixed time interaction | PASS_1_COMPLETE |
| S032 | p.6 EQ-5D day6,N 078 |−0.013 (−0.076,0.050),P.69;linear mixed time interaction | PASS_1_COMPLETE |
| S033 | p.6 EQ-5D day7,N 079 |−0.017 (−0.054,0.019),P.35;linear mixed time interaction | PASS_1_COMPLETE |
| S034 | p.6 EQ-5D day30,N 080 |−0.011 (−0.047,0.024),P.54;linear mixed time interaction | PASS_1_COMPLETE |
| S035 | p.6 EQ-5D day90,N 081 |−0.002 (−0.038,0.034),P.92;linear mixed time interaction | PASS_1_COMPLETE |
| S036 | p.7 clinician discharge readiness,N 096 |L278/27999.6%,P277/27899.6%;adjusted Cox HR0.99 (0.84,1.17);no P printed | PASS_1_COMPLETE |
| S037 | p.7 patient discharge fitness,N 097 |L278/27999.6%,P277/27899.6%;adjusted Cox HR0.99 (0.83,1.17);no P printed | PASS_1_COMPLETE |
| S038 | p.8 Figure 2 survival geometry,N 099 |KM cumulative recovery0-7 d;at-risk and event table fully N 099;caption recipients wording;baseline risk counts279/278;no figure CI/P | PASS_1_COMPLETE |
| S039 | p.8 Table 3 LOS,N 100/N 109 |Within30 d;Lmean6.0SD5.9,Pmean5.8SD4.5;negative-binomial minimization-adjusted IRR1.03 (0.92,1.14);one P excluded unknown discharge date;no P printed | PASS_1_COMPLETE |
| S040 | p.1 abstract,p.2 KeyPoints,p.5 primary text,p.9 conclusion |No significant improvement/benefit in primary72 h GI-3;matches S007/S008 and N 005 | PASS_1_COMPLETE |
| S041 | p.1 abstract,p.5 secondary text,p.7 discussion |No significant difference in any11 secondary endpoints;specifically timeGI-3/GI-2/ileus,PONV,intra/postoperative opioid,painOBAS,QoR-15,EQ-5D,ERP,medical/patient discharge readiness;discussion includes total LOS among 11 secondary endpoints;matched to full Table 2 and Table 3 evidence without interpreting consistency | PASS_1_COMPLETE |
| S042 | p.5 subgroup narrative,p.7 discussion,p.9 limitations |No treatment effect moderation across intended6/12 h,operation,sex,age,ERP;no evidence effect in post hoc actual duration;robust results;6 vs12 h no difference;interaction rule S006 | PASS_1_COMPLETE |
| S043 | p.5 safety narrative,p.8 discussion |Low30/90-day mortality and complications,similar LOS/AEs/safety;most AEs mild/moderate and unrelated/surgical;no attributable lidocaine AEs;no deaths within72 h;Table 3 all values N 100-N 109 | PASS_1_COMPLETE |
| S044 | p.8 discussion,p.9 strengths |40% not recovered at72 h;sample557;primary recorded all;>95%allocated treatment;adequate precision said to rule out meaningful benefit in primary/secondary;matched full estimate/CI inventory | PASS_1_COMPLETE |
| S045 | pp.4,7,8 outcome hierarchy and window relationships |p.4 tertiary LOS30 d,readmission30 d,complication≥3,mortality30/90 d;Table 3 titled tertiary/safety,readmission90 d;p.7 discussion secondary narrative includes LOS;N 044,N 100,N 107,N 109;direct quantitative status/window relationship preserved | PASS_1_COMPLETE |
Main result checks: S007–S039 all point estimates lie inside ordered printed intervals. Ratio null is 1; modeled continuous-difference null is 0. S007/S008 intervals include their null and their P=.54/.49 are nonsignificant. S012–S030 and S032–S035 intervals include 0 and all printed P values exceed .05. S031 excludes 0, P=.04, and favors placebo (higher EQ-5D better); its numerical interval and P agree, but S041's stated nonsignificant quality-of-life result conflicts: F-ST1-001. S009/S010/S011/S036/S037/S039 have no printed P: no test was invented. A diagnostic symmetric normal-Wald approximation to the 24 continuous estimates gives compatible displayed P values after allowing the input display intervals; model-specific degrees of freedom are unavailable and the approximation is not treated as exact authority. S038 risk/event geometry concerns arithmetic tracked in N 099 and numeric checking; no printed curve interval/P to test. S040 primary no-benefit interpretation follows the observed estimate and interval without a noninferiority/equivalence claim. S042 interaction conclusions reconcile with every factor P at .01 (see S059–S063). S043 does not give a formal safety test. S044 precision rhetoric gives no prespecified clinical margin, so a quantitative equivalence claim was not inferred. S045 captures the LOS status and readmission-window changes (F-ST1-010/F-ST1-011). S001/S004/S005/S006 design/model checks are extended below; S002/S003 power diagnostics are S064/S066.

## Result-supplement rows

All entries are R p.2, REPORT, primary GI-3 at72h, lidocaine/placebo relative risk. Subgroup effect intervals are within-subgroup intervals, whereas factor P values are interaction tests. These are distinct hypotheses. Every point is contained, endpoints ordered, and every interval includes 1 under either printed confidence convention. Confidence convention conflict is F-ST1-002, not an interval-versus-interaction-P contradiction.

| ID | Exact row | Printed n; RR (interval); contextual test | Pass-1 result | Pass 1 |
|---|---|---|---|---|
| S046 | R p.2 Overall | n absent; .97 (.88,1.07); matches M p.6 | Matches S007; baseline overall CI95%; graph legend99% applies ambiguously | PASS_1_COMPLETE |
| S047 | R p.2 Intended6h |271; .92 (.73,1.15) | Containment/order/null/direction reconcile; CI convention F-ST1-002 | PASS_1_COMPLETE |
| S048 | R p.2 Intended12h |261;1.03 (.82,1.28) | Same checks; duration rows total532, not557; missing subgroup membership specification not inferred | PASS_1_COMPLETE |
| S049 | R p.2 Nonright operation |256;.95 (.78,1.15) | Same checks; operation total557 | PASS_1_COMPLETE |
| S050 | R p.2 Right operation |301;.99 (.76,1.28) | Same checks; includes extended-right count corroborated P p.41, M p.4 | PASS_1_COMPLETE |
| S051 | R p.2 Female |249;.95 (.78,1.16) | Same checks; sex total557 | PASS_1_COMPLETE |
| S052 | R p.2 Male |308;.98 (.77,1.26) | Same checks; counts agree M baseline | PASS_1_COMPLETE |
| S053 | R p.2 Age50–74 |396;.95 (.77,1.16) | Same checks; age total557 | PASS_1_COMPLETE |
| S054 | R p.2 Age<50 |37;.82 (.49,1.37) | Same checks; no within-subgroup P supplied | PASS_1_COMPLETE |
| S055 | R p.2 Age≥75 |124;1.12 (.78,1.59) | Same checks; RR>1 favors lidocaine per recovery outcome | PASS_1_COMPLETE |
| S056 | R p.2 High ERAS |191;.96 (.82,1.12) | Same checks; ERAS total557 | PASS_1_COMPLETE |
| S057 | R p.2 Moderate ERAS |274;.99 (.76,1.29) | Same checks; implied 5–6/10 criteria from high≥7/low<5 | PASS_1_COMPLETE |
| S058 | R p.2 Low ERAS |92;1.01 (.49,2.08) | Same checks; no arm-specific event counts for exact RR reproduction | PASS_1_COMPLETE |
| S059 | R p.2 Infusion interaction |P=.401; A pp.14–15 intended6/12h interaction,alpha .01 | .401>.01; no moderation conclusion agrees; exact joint model covariance absent | PASS_1_COMPLETE |
| S060 | R p.2 Operation interaction |P=.773; A pp.14–15 right/nonright interaction,alpha .01 | .773>.01; no moderation conclusion agrees | PASS_1_COMPLETE |
| S061 | R p.2 Sex interaction |P=.830; A pp.14–15 interaction,alpha .01 | .830>.01; no moderation conclusion agrees | PASS_1_COMPLETE |
| S062 | R p.2 Age interaction |P=.162; A pp.14–15 three-level interaction,alpha .01 | .162>.01; no moderation conclusion agrees; degrees of freedom not inferred | PASS_1_COMPLETE |
| S063 | R p.2 ERAS interaction |P=.966; A pp.14–15 three-level interaction,alpha .01 | .966>.01; no moderation conclusion agrees; adjustment conflict S099 | PASS_1_COMPLETE |
## Plan power, design, methods and matched report relationships

These are logical relationships, not dummy numeric trial results. Blank dummy counts/model outputs do not generate fictional inferential estimates. The fresh support map records every prospective outcome, score rule, assessment matrix, dummy table, and command; the following relationships group only logically linked specifications.

| ID | Exact source/role locations | Printed rule / matched relationship | Pass-1 result and named limits | Pass 1 |
|---|---|---|---|---|
| S064 | P pp.10,20,40; A p.13 PLAN; M pp.4–5 REPORT | N 562, allocation1:1, power 90%, two-sided 5%; nonreturn40%→26.8% versus return60%→73.2% | Complements and absolute13.2 percentage points agree. Relative33% nonreturn reduction equals22% return increase. Diagnostic normal total n≈532.4, continuity-adjusted diagnostic n≈562.3; power at562≈.915 without continuity adjustment. Exact calculation engine absent; no contradiction established. | PASS_1_COMPLETE |
| S065 | P p.40; A p.13 PLAN | Alternative nonreturn30%→18%, relative40%, absolute12 points; N 562, same nominal90% power | Arithmetic agrees. Diagnostic total n≈528.2, power at562≈.917 without continuity adjustment. Exact engine absent; nominal90% is plausible. | PASS_1_COMPLETE |
| S066 | P p.40 PLAN; M p.5 REPORT | PPOI20%→10%, absolute10 points; N 562, similar90% power | Diagnostic total n≈531.7, power at562≈.915 without continuity adjustment. Exact engine absent; no contradictory sample size. | PASS_1_COMPLETE |
| S067 | P pp.19–20,40; A pp.8,14 PLAN; M pp.1,3,5 REPORT | Target562 eligible minimally invasive participants; replace postrandomization exclusions;590 randomized minus33 excluded equals557 | Final557 is5below target, an observed recruitment shortfall rather than an arithmetic discrepancy. The plan does not promise exactly562 final participants. Separate open stratum closed June2020, as disclosed. | PASS_1_COMPLETE |
| S068 | P pp.24,28,41; A pp.8,13–15 PLAN; M pp.3,5 REPORT | Eligible consenting ITT after presurgery ineligibility exclusions; nonrecipients retained; death before recovery counts as noGI3 | Primary279/278 equals267/265 recipients plus12/13 nonrecipients. PP is expressly receipt-based. Ineligible randomized participants excluded under plan; primary analysis-set definitions agree. | PASS_1_COMPLETE |
| S069 | A p.13 PLAN; M pp.3,8 REPORT | Safety includes randomized participants who received IMP; report safety279/279, with one extra placebo recipient | Printed safety558 versus recipient533, calculated267+265+1. F-ST1-012. Actual analyzed safety population needs clarification; it is not inferred solely from table headings. | PASS_1_COMPLETE |
| S070 | P p.40; A pp.3,14,20,34 PLAN; M pp.5–6 REPORT | Protocol primary logit link versus amended SAP/report log link; SAP history changed after completed analysis | Current SAP/report agree. Earlier logit primary analysis is absent; disclosed documentation alternative retained. F-ST1-003. | PASS_1_COMPLETE |
| S071 | A pp.14,24–25,35–36 PLAN; M pp.6–7 REPORT | Repeated OBAS/QoR/EQ models: baseline covariate, age, sex, random centre/participant, time-by-treatment interaction | Report linear mixed models/time interactions agree. Covariance structure not guessed. Sample command spelling is a notation exclusion. Adjusted effects are not equated with crude mean differences. | PASS_1_COMPLETE |
| S072 | P p.41; A p.15 PLAN; M p.5 REPORT | Primary MI/MNAR sensitivity if substantial or>10%missing; available valid data under MAR; report primary100%complete | Primary0%missing makes conditional MI unnecessary. Secondary observed-data analysis is compatible with the available-data strategy; no unstated secondary imputation requirement inferred. | PASS_1_COMPLETE |
| S073 | A p.16 PLAN; M pp.4,6–7 REPORT | Missing baseline covariates imputed by overall mean; derived scores require complete items | Baseline and follow-up n differ, but fitted-model membership and imputation logs are absent. Missing implementation detail alone gives no contradiction. | PASS_1_COMPLETE |
| S074 | P pp.40–41; A pp.14,20,34 PLAN; M p.5 REPORT | GI2/GI3 Cox models with shared centre; RMST if PH violated; report PH test finds no violation | Cox choice follows stated PH assessment. Test statistic/P absent; no conflicting assertion. Conditional RMST is not required when its trigger is absent. | PASS_1_COMPLETE |
| S075 | P pp.20,40,53; A p.14 PLAN; M pp.2,5 REPORT | No minimally invasive interim analysis; separate open scoping/group-sequential plan, subsequently closed; DMC safety reports | No contrary efficacy interim/stopping event claimed. Open-trial rule does not conflict with the minimally invasive rule. | PASS_1_COMPLETE |
| S076 | P p.41; A pp.3,14–15,37–38 PLAN; M pp.4–5; R p.2 REPORT | Primary interaction factors; ERAS entry added to SAP after analysis, but protocol already contains ERAS subgroup | Underlying ERAS subgroup was prospectively included in protocol. SAP addition disclosed. This is not a subgroup absent from every supplied prospective plan. Thresholds tracked separately in S077. | PASS_1_COMPLETE |
| S077 | P pp.17–18,31,41; A pp.3,15,38 PLAN; R p.2; M pp.4–5 REPORT | Protocol grades e.g.0–30%,30–60%,>60%; supplement ten criteria, high≥7 and low<5; thresholds not predefined; SAP three levels | Category construction expressly disclosed. Protocol examples are not binding numerical cutpoints. Moderate group is present in supplement; main high/low shorthand is not assumed to exclude it. | PASS_1_COMPLETE |
| S078 | A pp.13–15 PLAN; M p.5; R p.2 REPORT |95%overall and99%subgroups, interactionalpha .01; supplement legend99%versus prose95% | F-ST1-002. Actual confidence convention remains unclear. Subgroup-effect intervals and factor-interaction P values are different hypotheses. | PASS_1_COMPLETE |
| S079 | P p.16; A pp.20,33 PLAN; M pp.4,6 REPORT | GI2 diet AND stool, binary at96h plus elapsed time | HR1.03(0.86,1.23) is not the fixed96h proportion. Planned fixed-time fraction is absent; none invented. Cross-source checker assesses endpoint omission; no supplied statement calls this secondary outcome key. | PASS_1_COMPLETE |
| S080 | P pp.17,31–32,61; A pp.10–11,21–22,32 PLAN; M pp.4–6 REPORT | PONV≥5, vomiting episodes and rescue antiemetics through72h; report daily binary score | Score-threshold fractions reported, vomiting/antiemetic totals absent. No actual tests supplied. No numerical test conflict inferred from descriptive-only rows. Endpoint omissions also covered by cross-source review. | PASS_1_COMPLETE |
| S081 | P pp.17,33,35,37; A p.11 PLAN; M pp.4–6 REPORT | Planned postoperative opioid cumulative72h versus reported up to24h | F-ST1-006. Different windows change the consumption quantity;24h medians cannot be converted to72h totals. | PASS_1_COMPLETE |
| S082 | P pp.16,32–35; A pp.9,33–34 PLAN; M pp.4,8 REPORT | Endpoint prose uses surgery as recovery-time origin; sample survival variable uses general anesthesia | F-ST1-009. Exact timestamp definitions differ. Implemented origin and quantitative delay are absent. | PASS_1_COMPLETE |
| S083 | P p.16; A pp.9,33 PLAN; M pp.1,4,6,8 REPORT | GI3 requires diet for3 meals AND first flatus OR stool; binary by72h after operation start | Binary composite and event direction agree. Binary success RR and recovery HR represent distinct estimands; not compared as identical measures. | PASS_1_COMPLETE |
| S084 | P p.18; A pp.14,26,36 PLAN; M pp.5,7 REPORT | Discharge/readiness specific GLM tables/code versus reported Cox HR0.99(0.84,1.17),0.99(0.83,1.17) | F-ST1-007. Sample GLM family/link not supplied and not inferred. General SAP Cox instruction retained as alternative context. | PASS_1_COMPLETE |
| S085 | P p.18; A pp.10,27,36–37 PLAN; M p.8 REPORT | LOS primary admission plus readmissions30d; planned GLM; reported negative-binomial IRR1.03(0.92,1.14) | Negative binomial is a specific GLM; unspecified planned family gives no contradiction. Conventional exponential-coefficient IRR terminology is resolved in context; no person-time quantity inferred. | PASS_1_COMPLETE |
| S086 | P pp.16,18; A pp.10,27 PLAN; M pp.4,8 REPORT | Readmission planned30d after operation/discharge versus Table 3 within90d after operation | F-ST1-011. Definitions remain distinct. No assumption that31/34 are30d counts. | PASS_1_COMPLETE |
| S087 | P pp.16–19; A p.10 PLAN; M pp.4,7–8 REPORT | LOS tertiary in objectives/Table 3 but called one of11 secondary outcomes in discussion | F-ST1-010. Endpoint status affects membership of the summary. SAP retrospective footnote is not treated as a separate prospective endpoint change. | PASS_1_COMPLETE |
| S088 | A p.15 PLAN; complete M/R REPORT union | Primary sensitivity comparing Edinburgh with all other centres will be performed | No matching method/result anywhere in supplied results. F-ST1-005. Missingness condition does not attach to this independent sponsor-site paragraph. | PASS_1_COMPLETE |
| S089 | P pp.24,27–28; A p.15 PLAN; M pp.3,5,9 REPORT | Explore nonreceipt and actual versus intended duration in compliance analysis | Receipt-based PP532 and post hoc actual-duration exploration described. Missing coefficients alone do not establish an independent contradiction. | PASS_1_COMPLETE |
| S090 | A p.20 PLAN; M pp.5–6; R p.2 REPORT | Primary ITT/PP each have planned adjusted AND unadjusted rows | Only adjusted inferential effects supplied. F-ST1-004. Counts permit crude proportions but do not provide planned unadjusted GLM intervals/tests. | PASS_1_COMPLETE |
| S091 | P pp.18,41–42; A p.10 PLAN; M pp.1,4–9 REPORT | Economic90d QALYs by AUC, GLM, ICER, sensitivities; separate signed HEAP required | Separate economic plan/report expressly envisaged. No supplied HEAP or key economic result. Documented scope limitation; no invented conflict with clinical primary result. | PASS_1_COMPLETE |
| S092 | P pp.19,49–50 PLAN | Pilot50 recruits/4 sites; month12Poisson3.3×36=118.8≈119, SD≈10.90≈11; thresholds75/97 | Mean/variance and119−4×11=75,119−2×11=97 agree. No actual feasibility decision contrary to the rule supplied. | PASS_1_COMPLETE |
| S093 | P pp.31,60; A p.32 PLAN; M p.6 REPORT | OBAS=sum(items1–6)+(4−item7), range0–28, lower better | Rule/direction agree; means within range. No item-level result permits exact model reproduction. | PASS_1_COMPLETE |
| S094 | P p.60 PLAN | Worked OBAS item scores1,4,0,0,0,1,1 yield printed8 | Exact scoring gives9. Peripheral illustrative example does not alter the coherent formula or primary/key result; excluded once in checker table. | PASS_1_COMPLETE |
| S095 | P p.61; A pp.21,32 PLAN; M p.7 REPORT | PONV=two0–3 items; threshold≥5 versus literal=5 in SAP appendix | Adjacent dummy table, protocol and report make≥5clear. Relational-symbol omission excluded as notation; no printed result independently conflicts. | PASS_1_COMPLETE |
| S096 | P p.62; A p.32 PLAN; M p.6 REPORT | QoR15 sum0–150, higher better; symptom items reverse numeric anchors | Numeric scoring direction agrees with total; means74–97 are within bounds. No item totals supplied for exact sum reproduction. | PASS_1_COMPLETE |
| S097 | A pp.18,31–32 PLAN | p-POSSUM12physiological and6operative items, scores1/2/4/8; dummy physiological range12–88; mortality logit−7.04+.13phys+.16op | Naive12×8=96 does not establish a conflicting maximum without all item-specific scoring rules. No trial risk result printed. Missing item definitions named; external scoring conventions not imported. | PASS_1_COMPLETE |
| S098 | A p.16; P pp.48–52 PLAN; M p.5 REPORT | COVID descriptions first, formal analysis if needed; report pause and no design change | No unconditional formal efficacy comparison required; no inferential decision contradicts this conditional plan. | PASS_1_COMPLETE |
| S099 | A pp.14–15,37–38 PLAN; M p.5 REPORT | Primary model includes age/sex/centre; ERAS code includes treatment×ERAS, sex and centre without AgeBand | F-ST1-008. Sample ERAS covariate set differs from general specification. No assertion that actual analysis ran unchanged sample code. | PASS_1_COMPLETE |
| S100 | P p.18; A pp.26,36 PLAN; M p.7 REPORT | Medical readiness requires five criteria; sample variable description says time to actual discharge | Variable name/title/criteria identify readiness. Actual use of discharge date unestablished; apparent wording ambiguity excluded. Distinct model-class comparison remains F-ST1-007. | PASS_1_COMPLETE |
| S101 | All supplied sources, complete maps | SuperiorityRCT; no NI/equivalence margin; no minimally invasive efficacy interim; no secondary multiplicity; subgroupalpha .01 | NI/equivalence/stopping claims have no applicable unit. No margin, alpha allocation or stopping threshold invented. | PASS_1_COMPLETE |
| S102 | M p.2 REPORT; P pp.13,40 PLAN, historical context | Supplied historical OR0.52(0.35,0.75), diet MD−6.2(−12.37,−0.03), ileusRR0.38(0.15,0.99), other background intervals | Containment/order/direction agree as printed; no source P paired. Historical estimates are not current trial results. No external literature consulted. | PASS_1_COMPLETE |
| S103 | P pp.26–29; A p.8 PLAN; M pp.1,4 REPORT | Bolus1.5mg/kg, infusion1.5mg/kg/h, maximum120mg/h=6mL/h of2%; intended6–12h; early stopping permitted | Dose20mg/mL×6mL/h=120mg/h agrees; five weight-table rates/totals reconcile. Intended/actual duration distinction explicit; no intervention discrepancy. | PASS_1_COMPLETE |
| S104 | P p.23; A pp.9,34–38 PLAN; M pp.2,5 REPORT | Individual randomization1:1, minimization age/sex/site; random centre and repeated-participant effects | Supplied specification represents site/longitudinal structure. No independent-versus-paired mismatch. ERAS age omission tracked separately in S099. | PASS_1_COMPLETE |
| S105 | A pp.16,31–33; P pp.60–62 PLAN; M pp.4,6; D p.1 REPORT | Complete-item PROM calculation, baseline covariate imputation, validated UK utility algorithm, GI component timing; sharing administration | Derived-score completeness distinguished from baseline covariate imputation. No missing-item imputation inferred. Utility link not followed. Sharing statement adds no statistical relationship. | PASS_1_COMPLETE |
## Coverage and precision limits

All 105 relationships were checked for applicable containment, endpoint order, effect/reference direction, interval-versus-test logic, stated decision rules, method logic and plan/report implications. Independent numeric checks are cross-referenced to the N inventory; inferential records retain their own population distinctions. No finding rests on crude-versus-adjusted comparisons or invented sidedness, degrees of freedom, covariance, variance estimator or raw data. Power and normal-Wald approximations are expressly diagnostic because calculation engines/fitted output are absent. Dummy outputs are blank; background and administrative units are mapped without manufacturing trial results. Twelve self-screened findings and eleven excluded apparent observations appear in checkers/statistical_pass_1.md.
