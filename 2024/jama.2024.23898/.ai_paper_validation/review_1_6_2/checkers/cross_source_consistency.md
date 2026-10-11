# Cross-source consistency review

Runtime agent: 01a129b6-fc00-7351-bd76-e5d3e4f6b89b. Role/model/effort: cross_source_consistency_reviewer, gpt-6.1-sol, medium. Fresh independent discovery; no prior conclusions or external sources consulted. Complete scope and review contract read. Tools: direct Poppler pdftotext 26.01.0 plus existing source-page images; compute CPU; no sources or reused assets modified.

## Scope and completed comparison coverage

All five direct sources were covered through the complete fresh main/support maps and targeted direct-source rereading: DOC-001 REPORT pp.1–10, DOC-002 PLAN pp.1–66, DOC-003 PLAN pp.1–40, DOC-004 REPORT pp.1–2, DOC-005 REPORT p.1. DOC-005 has no statistical comparison. No supplied Office/CSV evidence exists. Exact quoted locations below were independently extracted from supplied PDFs; main pp.3,7,8 and subgroup p.2 were also visually checked.

Matched N001–N110 and S001–S045 across abstract, Key Points, narrative, tables, survival curves, captions and footnotes; matched all PROT-001–PROT-032 and SAP/SUB evidence keys. Population, time, contrast, measure, model, analysis set and precision were matched before comparison. Primary numerical copies reconcile: 160/279 versus164/278, RR0.97(0.88–1.07), RD−1.9%(−8.0–4.2); per-protocol154/267 versus158/265, RR0.96(0.86–1.07), RD−2.3%(−8.9–4.3). Overall subgroup estimate agrees with main. All baseline copies, discharge outputs, tertiary outcomes and adverse-event labels were considered. Arithmetic and within-row inferential reproduction are independently assigned to other checkers; cross-location observations remain documented here.

Design comparison covered primary GI-3 AND/OR components and72h operation-start window; secondary GI-2 components/time/96h; PPOI120h; PONV components; OBAS/QoR/EQ5D schedules; opioid window; every medical-discharge criterion (independent hydration/nutrition, adequate oral analgesia, independent mobilization, GI-3, no medical contraindication) and patient readiness adding happiness to go home; major complications threshold; readmission/mortality/LOS; treatment bolus1.5mg/kg ideal weight, infusion1.5mg/kg/h maximum120mg/h, intended6/12h and permitted clinical shortening; all eligibility/exclusion and postrandomization analysis-set criteria; age/sex/centre minimization, primary link and random centre, repeated-measure baseline adjustment/interactions, missing-data conditions, sample-size/power/hypothesis, no minimally-invasive interim, stopping and multiplicity, subgroup/compliance/sensitivity plans.

Eligibility comparison item by item: adult capacity/consent; indicated minimally invasive operations; planned epidural; concurrent regional/local lidocaine; planned open operation; pregnancy; breastfeeding; allergy; complete heart block; Child A-or-greater liver dysfunction; eGFR<30; interventional-trial participation/co-enrolment; surgical indication; rectal cancer below peritoneal reflection/TME; neoadjuvant rectal radiotherapy; planned new stoma. Article explicitly points to full protocol list; compressed prose does not establish additional missing criteria. Inflammatory bowel disease is outside the listed eligible indications. Both plans separate eligibility exclusions before surgery/IMP from follow-up withdrawal. Safety inclusion has the finding below.

ERAS lists compared individually: protocol avoidance of long-acting maintenance opioids,48h PONV prophylaxis, fluid policy/weight, carbohydrate/early solid feeding, mobilization plus walking, laxatives, no immediate postoperative NG tube; report subgroup ten criteria are prophylaxis, no NG at operation,<4L first24h fluids, carbohydrate drink,day1 mobilization,day1 food,day-of-surgery supplemental drinks,48h IV-fluid cessation,48h catheter removal,day2 mobilization. The report explicitly discloses that category definitions were not predefined. No absent ERAS prespecification finding is supported: protocol p41 expressly plans the subgroup despite its later addition to SAP. Initial open-trial adaptive interim rules apply to a different randomized stratum, expressly closed June2020; they do not conflict with no interim analysis for minimally invasive cases. Primary power inputs are complements,40%→26.8% nonrecovery versus60%→73.2% recovery, with the same13.2-point difference and562 target. Missing-primary-data contingency is untriggered because100% primary outcomes are reported. No noninferiority/equivalence margin or changed hypothesis was found.

## Findings

### F-XS-001

**Title:** Blanket secondary-outcome nonsignificance statement conflicts with printed day-5 quality-of-life result.

**Compared locations and roles:** REPORT [main abstract p.1](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=1), REPORT [main results p.5](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5), REPORT [Table2 p.6, EQ-5D-5L postoperative day5](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6), REPORT [discussion p.7](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=7); corroborating PLAN [SAP pp.13–14, no secondary multiplicity adjustment](../../../joi240139supp2_prod_1741633738.17362.pdf#page=14).

**Printed comparison:** Abstract states no significant difference in any11 secondary endpoints; results explicitly includes quality of life and discussion says no benefit in any11. Table2 day5 EQ-5D prints treatment effect−0.057,95%CI−0.111 to−0.003,P=.04.

**Comparison logic:** The CI excludes0 and P<.05. This is a within-time treatment effect for an abstract-listed secondary endpoint; source footnote f says effects derive from time-by-treatment interactions. No secondary multiplicity correction is prescribed. Thus printed significance and universal nonsignificance do not reconcile. Display rounding cannot remove CI exclusion: upper limit rounding interval[−.0035,−.0025]; P interval[.035,.045].

**Focus area:** B. **Proposed review domain:** statistical_results. **Relationship type / All relationships:** S_W / S_W. **Qualifying route:** Route A, category 1.

**Affected result or extracted value:** Day5 quality-of-life treatment effect and the abstract claim about all11 secondary outcomes.

**Why context does not resolve it:** Route A category1 applies to the significant interval/test versus the nonsignificant statement. A separate overall repeated-measures test could differ, but none is identified as the basis of the universal statement.

**Supported alternatives:** The narrative may refer to an overall outcome-level comparison whereas the table presents individual-time contrasts, or may mean no consistent clinically beneficial pattern. Neither interpretation changes the printed day5 statistical result. **Human question:** Which statistical comparison supports the statement of no significant difference in any11 secondary endpoints, and how does it relate to day5 EQ-5D P=.04?

### F-XS-002

**Title:** Reported safety population includes participants who did not receive randomized treatment despite the SAP exposure criterion.

**Compared locations and roles:** PLAN [SAP p.13, adverse events](../../../joi240139supp2_prod_1741633738.17362.pdf#page=13); REPORT [main p.3, Figure1 treatment and safety boxes/footnote b](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=3); REPORT [main p.8, Table3 AE/SAE rows and footnote e](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8).

**Printed comparison:** SAP safety data are for all randomized participants who received IMP. Figure1 prints267 lidocaine and265 placebo recipients,12 and13 nonrecipients, but279 and279 in safety analysis. Its footnote adds one exposed placebo postrandomization exclusion; Table3 repeats that addition. AE participants40/37 and SAE participants4/9 are reported.

**Comparison logic:** Apply both planned criteria, randomized AND exposed, item by item. Exposed safety totals supported by flow are267 lidocaine and266 placebo including the extra exposed exclusion. Printed safety boxes279/279 instead include12 and13 eligible nonrecipients. This is a categorical analysis-set mismatch, not a numeric rounding finding; integer participant membership and exposure criteria do not have display-precision intervals.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type / All relationships:** P_R / P_R. **Qualifying route:** Route B.

**Affected result or extracted value:** AE/SAE safety proportions and the population to which safety conclusions apply.

**Why context does not resolve it:** The added placebo participant explains one exposed inclusion but does not explain the25 nonrecipients retained in the safety boxes. Both planned exposure-only and reported full eligible sets are explicitly printed.

**Supported alternatives:** Figure1 may call the overall follow-up cohort a safety set while AE/SAE computations use another set; alternatively safety was broadened to all eligible participants. **Human question:** Which participants form the AE/SAE denominator, and why does the reported safety set include eligible nonrecipients relative to the SAP exposure requirement?

### F-XS-003

**Title:** Opioid consumption window is shortened from the planned72hours to the reported24hours.

**Compared locations and roles:** PLAN [protocol p.17, total postoperative opioid consumption](../../../joi240139supp1_prod_1741633738.16362.pdf#page=17), PLAN [SAP p.11, schedule](../../../joi240139supp2_prod_1741633738.17362.pdf#page=11); REPORT [main outcomes p.4](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4), REPORT [main secondary-result narrative p.5](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5), REPORT [Table2 p.6, postoperative opioid row](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6).

**Printed comparison:** Protocol defines cumulative morphine-equivalent dose until72h after operation start; SAP schedule says total opioid consumption in hospital up to72h. Article defines consumption up to24h and prints median70.6mg(IQR30.0–150.0),n210 lidocaine versus45.0mg(17.1–98.6),n210 placebo.

**Comparison logic:** Same secondary outcome, measure and randomized contrast; exposure accumulation windows differ by48hours. This is an endpoint-definition/time-window comparison, not a difference between rounding copies. No72h result or disclosed window amendment was located in supplied REPORT sources.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type / All relationships:** P_R / P_R. **Qualifying route:** Route B.

**Affected result or extracted value:** Extracted postoperative morphine-equivalent consumption70.6 versus45.0mg and its relation to the planned secondary endpoint.

**Why context does not resolve it:**24h cannot substitute for cumulative72h without a documented definition change; no same-result alternative is identified.

**Supported alternatives:** Only the first24h may have been analyzed/available, or the printed horizon may differ from the actual analyzed horizon. **Human question:** Was the planned72h opioid endpoint changed to24h, and what window produced the printed70.6 and45.0mg values?

### F-XS-004

**Title:** Planned primary-outcome Edinburgh-versus-rest sensitivity analysis is not reported.

**Compared locations and roles:** PLAN [SAP p.15, section11.6](../../../joi240139supp2_prod_1741633738.17362.pdf#page=15); REPORT [main methods/results p.5](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5), REPORT [Table2 primary analyses p.6](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6), REPORT [subgroup eFigure p.2](../../../joi240139supp3_prod_1741633738.18862.pdf#page=2). Complete main pp.1–10 and all supplied REPORT supplements checked for the comparison.

**Printed comparison:** SAP states a sensitivity analysis comparing Edinburgh with the rest of centres will be performed because Edinburgh is expected to have the largest recruitment. The preceding section frames sensitivity analyses on the primary outcome. Main reports overall and per-protocol primary estimates and infusion/operation/sex/age/ERAS subgroups plus a post hoc actual-duration analysis, but no Edinburgh-versus-rest result.

**Comparison logic:** This planned primary sensitivity is unconditional, unlike the >10% missingness contingency in the preceding paragraph. Site random-effect adjustment is a primary-model feature rather than the specified separate comparison. No such analysis or disclosed cancellation was located anywhere in the supplied report package.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type / All relationships:** P_R / P_R. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Robustness of the primary GI-3 result to sponsor-site recruitment.

**Why context does not resolve it:** Route A category5 covers an unreported planned primary analysis. No missingness condition attaches to this distinct paragraph.

**Supported alternatives:** The analysis may have been performed but omitted from this publication package, or prospectively withdrawn in material not supplied. **Human question:** Where is the planned Edinburgh-versus-rest primary sensitivity result, or where was its cancellation documented?

### F-XS-005

**Title:** Total hospital stay is called secondary in discussion but tertiary in the planned and reported hierarchy.

**Compared locations and roles:** PLAN [protocol pp.16/18, tertiary objectives/endpoints](../../../joi240139supp1_prod_1741633738.16362.pdf#page=18), PLAN [SAP p.10, tertiary outcomes](../../../joi240139supp2_prod_1741633738.17362.pdf#page=10); REPORT [main p.4, outcomes](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4), REPORT [main discussion p.7](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=7), REPORT [Table3 p.8](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8).

**Printed comparison:** Protocol/SAP and article methods classify total hospital stay as tertiary; Table3 is titled Tertiary/Safety Outcomes. Discussion says there was no benefit on any of11 secondary endpoints 'including ... total length of hospital stay.' Table3 LOS6.0(5.9) versus5.8(4.5)days,IRR1.03(0.92–1.14).

**Comparison logic:** Match the identical LOS outcome; inclusion in the11-secondary set conflicts with the explicit tertiary hierarchy. This is an outcome-status comparison; display rounding is inapplicable. SAP's footnote referring to a published protocol outside this supplied protocol does not change the tertiary classification printed in the supplied current protocol.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type / All relationships:** P_R / P_R, S_W. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Evidence extraction of the prespecified status of LOS and membership of the11-secondary endpoint set.

**Why context does not resolve it:** Route A category5 expressly includes changed outcome status, even when a different source supplies the intended hierarchy.

**Supported alternatives:** Discussion may use 'secondary' loosely, or the hierarchy may have changed for discussion reporting. **Human question:** Is total hospital stay a tertiary outcome as specified in plans/methods/Table3, or one of the11 secondary endpoints as stated in discussion?

### F-XS-006

**Title:** Readmission result is labelled90days despite a30-day outcome definition.

**Compared locations and roles:** PLAN [protocol p.16, objective](../../../joi240139supp1_prod_1741633738.16362.pdf#page=16), PLAN [protocol p.18, endpoint](../../../joi240139supp1_prod_1741633738.16362.pdf#page=18), PLAN [SAP p.10, tertiary readmission](../../../joi240139supp2_prod_1741633738.17362.pdf#page=10); REPORT [main outcomes p.4](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4), REPORT [Table3 p.8, unplanned readmission](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8).

**Printed comparison:** Main definition and SAP/protocol endpoint say within30days of operation. Table3 says unplanned readmission after discharge and within90days of operation,31(11.1%) lidocaine versus34(12.2%) placebo. Protocol objective separately says30days after discharge; its detailed endpoint says30days from operation.

**Comparison logic:**30-day and90-day operation-relative windows represent distinct event sets. No supplied report explains which window underlies31/34. Protocol's discharge-relative objective is an additional in-scope endpoint-definition comparator; it does not reconcile90days. This is a quantity-changing outcome label and report-versus-plan endpoint definition, rather than a peripheral comparison of tertiary numeric copies. No half-unit numeric result calculation is used because no comparator event count is supplied.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type / All relationships:** P_R / P_R, S_W. **Qualifying route:** Route B.

**Affected result or extracted value:**31/34 unplanned-readmission events and their follow-up window in evidence synthesis.

**Why context does not resolve it:** Follow-up at both30and90days makes either window plausible. The immediate table says90days while methods identify30days; no event-date information permits deciding.

**Supported alternatives:** The analysis may intentionally extend the planned window to90days, or only the row label may use90days; the intended30-day anchor also needs clarification. **Human question:** Do31and34 represent readmissions within30days of operation,30days of discharge, or90days of operation, and was the planned endpoint amended?

### F-XS-007

**Title:** Subgroup interval confidence level differs between figure legend, caption and statistical plan.

**Compared locations and roles:** PLAN [SAP p.15, subgroup significance/CI rule](../../../joi240139supp2_prod_1741633738.17362.pdf#page=15); REPORT [main methods p.5](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5), REPORT [eFigure p.2, legend and caption](../../../joi240139supp3_prod_1741633738.18862.pdf#page=2).

**Printed comparison:** SAP states two-sided1% subgroup significance and corresponding99% CIs. eFigure line legend says99%CI, while its prose says the right-hand numbers are within-subgroup RRs and95%CI. Main says all treatment-effect estimates are presented with95%CIs while prescribing1% subgroup significance. Affected within-subgroup intervals:6h0.92(0.73–1.15);12h1.03(0.82–1.28);nonright0.95(0.78–1.15);right0.99(0.76–1.28);female0.95(0.78–1.16);male0.98(0.77–1.26);age50–74 0.95(0.77–1.16),<50 0.82(0.49–1.37),≥75 1.12(0.78–1.59);ERAShigh0.96(0.82–1.12),moderate0.99(0.76–1.29),low1.01(0.49–2.08). Overall0.97(0.88–1.07) repeats main95%CI and is separate.

**Comparison logic:** Confidence levels are inferential definitions rather than rounded copies of an estimate. It is possible the plotted lines are99%and the numeric intervals95%, but the source never identifies such two separate quantities. Caption/legend disagreement changes variance interpretation and the planned inference, not solely a peripheral pointer or formatting label. No within-subgroup event counts permit mechanically deciding which interval convention generated each display.

**Focus area:** D and B. **Proposed review domain:** protocol_report. **Relationship type / All relationships:** P_R / P_R, S_W. **Qualifying route:** Route B.

**Affected result or extracted value:** Confidence level assigned to all12 within-subgroup RR intervals and reconstruction of their uncertainty.

**Why context does not resolve it:** Both confidence levels are explicit. The overall95%CI corroboration does not determine the within-subgroup interval level.

**Supported alternatives:** Numeric95%intervals and99%graphical lines may intentionally coexist, or all subgroup intervals may use one level with a conflicting label. **Human question:** Are the subgroup numeric and graphical intervals95%or99%, and how do they implement the SAP99%rule?

### F-XS-008

**Title:** Planned measurements for abstract-listed secondary outcomes are absent from the supplied results.

**Compared locations and roles:** PLAN [protocol p.16, GI-2 binary96h plus time-to-event](../../../joi240139supp1_prod_1741633738.16362.pdf#page=16), PLAN [protocol p.17, PONV components](../../../joi240139supp1_prod_1741633738.16362.pdf#page=17); PLAN [SAP p.20, GI-2 status96h dummy table](../../../joi240139supp2_prod_1741633738.17362.pdf#page=20), PLAN [SAP p.21, vomiting72h](../../../joi240139supp2_prod_1741633738.17362.pdf#page=21), PLAN [SAP p.22, rescue antiemetic72h](../../../joi240139supp2_prod_1741633738.17362.pdf#page=22); REPORT [main abstract p.1](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=1), REPORT [Table2 p.6](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6), REPORT [results p.5](../../../jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5). All main/report-supplement pages inspected for these measures.

**Printed comparison:** Plans specify GI-2 yes/no at96h as well as time-to-event, and nausea/vomiting measured by PONV score, cumulative vomiting episodes72h and rescue antiemetic dose72h. SAP includes explicit dummy reporting tables for each. Article gives time-GI-2 HR1.03(0.86–1.23) with261/256 event totals, and PONV-score≥5 day1–3 counts7/16,5/19,5/5; no96h GI-2 status count, cumulative vomiting-episode quantity or rescue antiemetic dose is displayed. These outcomes are expressly listed in the abstract, with blanket nonsignificance statements.

**Comparison logic:** Binary GI-2 at96h is distinct from the all-follow-up time-to-event count. Vomiting-episode quantity and rescue dose are distinct from dichotomized PONV scores. Consolidated pattern: prespecified result measures for key secondary outcomes are not reported in any supplied REPORT location. This is grounded in explicit planned measures and displays, not an imagined additional model detail.

**Focus area:** D. **Proposed review domain:** protocol_report. **Relationship type / All relationships:** P_R / P_R. **Qualifying route:** Route A, category 5.

**Affected result or extracted value:**96h GI-2 recovery proportion and72h postoperative nausea/vomiting burden and rescue-medication results underlying abstract-listed secondary outcomes.

**Why context does not resolve it:** Route A category5 covers planned key secondary analyses not reported. Printed alternative measures cannot supply the missing horizon/component-specific result.

**Supported alternatives:** These measures may have been collected/analyzed but left out of this report, or removed from the reporting plan in a change not supplied. **Human question:** Where are the prespecified96h GI-2 proportion,72h cumulative vomiting episodes and72h rescue antiemetic dose results, or where was their removal documented?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN protocol p.40 primary logit; PLAN SAP p.3 version history and p.14 log; REPORT main p.5 log | Original logit versus analyzed log link is explicitly addressed in the supplied post-analysis SAP amendment; current SAP and report agree. This establishes a disclosed change, without establishing an absent analysis or a conflicting printed result. | CONTEXT_RESOLVES |
| PLAN SAP p.3 ERAS insertion; PLAN protocol p.41 ERAS subgroup; REPORT eFigure p.2 footnote | SAP added ERAS after data review, but supplied protocol already specifies the ERAS subgroup; report discloses newly defined categories. An observation that the subgroup itself was absent from supplied plans is not reproduced. | NOT_REPRODUCED |
| PLAN protocol pp.17–18 ERAS; REPORT eFigure p.2 ten criteria/high≥7/low<5 | The different criterion selection/thresholds for subgroup categorization are explicitly disclosed as not predefined, rather than asserted to reproduce a prospective criterion set. | CONTEXT_RESOLVES |
| PLAN SAP p.34 time from anesthesia versus p.9 time from surgery | Secondary elapsed-time code/prose clocks differ; no supplied matched result establishes an analysis-population or primary/key-secondary decision-rule change from this plan-internal clock distinction. | PERIPHERAL_COMPARISON |
| PLAN SAP p.36 medical-discharge sample code/GLM versus p.14 general Cox time-to-event rule; REPORT Table2 p.7 Cox | Reported time-to-event Cox model follows the explicit general SAP rule. Appendix illustrative code has no family/link specification and does not establish a separate intended definitive method. | CONTEXT_RESOLVES |
| PLAN SAP p.32 PONV '=5' versus p.21 dummy ≥5; REPORT main Table2 footnote ≥5 | The single symbol is resolved directly by the scale table and report; no different analyzed threshold or quantity is established. | NOTATION_OR_TYPOGRAPHY |
| REPORT Figure1 p.3 90-day questionnaire death exclusions2/1 versus Table3 p.8 deaths2/3 | Questionnaire disposition does not identify every mortality event among already-withdrawn/lost participants or the extra exposed placebo exclusion; these are nonmatching event sets without individual reconciliation data. The final source audit corrected the locator's original 1/1 transcription to the printed 2/1; the exclusion decision is unchanged. | NOT_REPRODUCED |
| REPORT Figure2 p.8 caption 'received' versus risk-table initial279/278 and treatment recipients267/265 | Caption wording refers to randomized groups; displayed initial counts clearly identify the primary eligible cohort. | TERMINOLOGY_OR_WORDING |
| REPORT main pp.4–5 high versus low ERAS description versus REPORT eFigure p.2 high/moderate/low | The displayed moderate category is clear in the cited figure and SAP; abbreviated narrative grouping does not obscure any printed RR. | TERMINOLOGY_OR_WORDING |
| REPORT main Table1 p.4 female127(45.7) and all later female249 total | Missing space/parenthesis spacing leaves counts unchanged and unambiguous. | NOTATION_OR_TYPOGRAPHY |
| PLAN protocol p.16 secondary health economics versus REPORT main abstract11 clinical secondaries | Economic analysis has its own planned analysis/report stream; absence from this clinical report alone does not reproduce a conflicting statistical result or an outcome-status reassignment. | CONDITIONAL_OR_UNREPORTED |

## Completion and limitations

Complete assigned cross-source scope,8 findings,11 excluded observations. Source-linked comparisons cover every supplied report/plan unit through the mapper inventories and direct rereading of all relevant statements; no unresolved source-coverage gap. Underlying participant-level event dates, subgroup arm counts, unpublished analyses and earlier complete SAP version are not supplied; no findings assume them. Source and asset integrity preserved. All proposed findings require independent inclusion screening and human adjudication.
