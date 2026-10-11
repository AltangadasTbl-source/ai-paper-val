# Independent Initial Screening Evidence and Consolidation

Runtime ID: 01a128e5-2413-7142-a2ea-ee880aee0ed9. Mandatory fresh inclusion_screener, gpt-6.1-sol/high. This artifact supplies evidence for coordinator registration; it assigns no stable ID, evidence-recheck state, inclusion audit, severity, or disposition. All included issues are Pending Human Adjudication.

## Scope, source confirmation, and tooling

Read START_PROMPT.md, complete QUALITY_CONTROL_SCOPE.md, complete workflow_1_6_1/review_contract.md including the inclusion-screen section, complete report_spec.md, tooling_record.md, source_inventory.md, source_coverage.md, all three current initial checker artifacts, and the current source-backed map coverage statements. The source union contains five PDFs and 102 physical pages. The numeric checker has zero findings, cross-source checker five, and statistical pass 1 three. All eight receive one initial screening row. Three overlapping pairs are consolidated without loss of provenance; no C ID is assigned here.

Source roles by content: DOC-001 main article REPORT; DOC-002 protocol PLAN; DOC-003 SAP PLAN; DOC-004 supplementary results REPORT; DOC-005 data-sharing statement REPORT. No physical supplement numbering determines a role. The protocol cover calls version 7 a protocol with final amendments; its cover date is July11,2017 and its page footers July6,2017. The SAP is an analysis plan without a displayed operative date/version; no chronology is inferred.

Direct source derivatives use Poppler 26.01.0 pdftotext layout. Exact command pattern: `pdftotext -layout SOURCE.pdf .ai_paper_validation/review_1_6_1/screening/confirmation/NAME-layout.txt`. Four independently generated full-document outputs are screening/confirmation/main-layout.txt, protocol-layout.txt, sap-layout.txt, and results-layout.txt. Cited main pp.1,2,4,6,7,8,9; protocol pp.1,8,9,16,17,18,20,23,28,43; SAP pp.2,3,4; and results pp.4,5,21,22 were read by physical-page form-feed boundaries. Protocol p.48 was additionally checked for amendment context; its prospective administrative definition supplies no specific dose/model/endpoint/power reconciliation. DOC-005 p.1 was read directly with `pdftotext -layout joi190007supp4_prod.pdf -`; it contains access terms, no additional supplied results.

Visual confirmation uses Poppler 26.01.0 pdftoppm, CPU only. Command pattern: `pdftoppm -f N -l N -scale-to 1500 -singlefile -png SOURCE.pdf .ai_paper_validation/review_1_6_1/screening/confirmation/NAME-pN`. Independently rendered and visually inspected screening/confirmation/protocol-p16.png, protocol-p23.png, protocol-p28.png, protocol-p43.png, and sap-p4.png. They confirm all material headings/values used here. No OCR/source disagreement affected screening; no fallback, conversion, external evidence, GPU, or legacy conclusion was used. No source or reusable asset was modified.

The whole current main/results text was searched for RERI, additive, biological interaction, linear odds, likelihood-based, interaction, sensitivity and post hoc terms. Complete current maps corroborate that all report pages/tables were inspected. Absence of an additive result is bounded to the supplied package, not a claim about an analysis never conducted.

## Deterministic consolidation and source order for coordinator registration

Use each issue's earliest substantive REPORT anchor in DOC-001, in physical-page reading order, with actual paragraph order as a tie-break. The recommended issue order is: daily dose (main p.1 INTERVENTIONS); primary-model/Cox priority (main p.1 MAIN OUTCOME AND MEASURES); planned additive sensitivity missing from the combination evidence (main p.1 RESULTS combination); IDS hierarchy (main p.4 Secondary Outcomes); primary-power specification (main p.4 Sample Size, beginning in the left column and continuing at the top of the right column). This order is a reproducible ordering convention, not a ranking.

- Daily dose: F-XS-002 only.
- MDD model/priority: F-XS-003 and F-ST1-002, one issue with both INCLUDE rows sharing the assigned ID.
- Additive sensitivity: F-XS-005 only.
- IDS hierarchy: F-XS-004 and F-ST1-003, one issue with both INCLUDE rows sharing the assigned ID.
- Primary-power specification: F-XS-001 and F-ST1-001, one issue with both INCLUDE rows sharing the assigned ID.

## Daily EPA+DHA dose

Finding: F-XS-002. Focus D; review domain protocol_report; primary relationship P_R; all relationships P_R. Compared roles are PLAN protocol versus REPORT main article/results supplement. The two REPORT documents agree and introduce no S_C conflict; repetition is retained as evidence.

Exact sources: [protocol p.8 summary](../../../joi190007supp1_prod.pdf#page=8), [p.18 treatment](../../../joi190007supp1_prod.pdf#page=18), [p.20 tolerance](../../../joi190007supp1_prod.pdf#page=20), [p.23 intended dose](../../../joi190007supp1_prod.pdf#page=23); [main p.1 interventions](../../../jama_bot_2019_oi_190007.pdf#page=1), [p.2 supplement intervention](../../../jama_bot_2019_oi_190007.pdf#page=2); [results p.4 composition](../../../joi190007supp3_prod.pdf#page=4), [p.5 testing](../../../joi190007supp3_prod.pdf#page=5). Protocol [p.1](../../../joi190007supp1_prod.pdf#page=1) establishes final-amendment version context.

Source observations: protocol specifies one omega capsule plus one vitamin/mineral pill daily for one year; capsule omega3 1000mg, EPA/DHA3:1, and p.23 explicitly EPA+DHA=1.0g/day. Main p.2 and results p.4 explicitly define 1412mg EPA+DHA, ratio3:1, delivered in the one omega capsule plus vitamin/mineral pill daily for one year. Laboratory p.5 reports fractions in g/100g FAME, not a conversion that reconciles these two daily EPA+DHA masses.

Reproduction/calculation: 1.0g=1000mg; 1412−1000=412mg, a41.2% increase. Protocol p.20 manufacturing deviation90–125% implies an upper1250mg when applied to1000mg, still162mg below1412mg. Ordinary display rounding cannot bridge the difference. This numerical demonstration is not a capsule/FAME dose reconstruction.

All four criteria: source values reproduced and visually confirmed; randomized intervention dose is a qualifying cross-document comparison in focusD; the explicit EPA+DHA=1.0g statement rules out interpreting1000mg merely as total capsule oil or ordinary tolerance; dose extraction attached to the primary multinutrient OR1.06(.87–1.29) could differ. No supplied amendment identifies a1.412g/day revision.

Source-grounded alternatives: delivered formulation may have changed; protocol may retain intended preliminary-dose text. REPORT dose extraction itself is clear; the unresolved issue is its relationship to the supplied planned dose. Human question: what documented formulation change reconciles planned1.0g/day with reported1.412g/day? Classification ambiguity: no role ambiguity; timing of any formulation amendment is unsupplied.

## MDD primary-model priority and Cox prespecification

Findings: F-XS-003/F-ST1-002 consolidated. FocusD; review domain protocol_report; primary relationshipP_R; all relationshipsP_R,P_P. PLAN protocol/SAP conflict givesP_P; PLAN/report conflict givesP_R with precedence. REPORT primary OR and Cox HR labels are internally clear; no S_W numeric conflict is asserted.

Exact sources: [protocol p.43 §10.1](../../../joi190007supp1_prod.pdf#page=43); [SAP p.3 fourth analysis](../../../joi190007supp2_prod.pdf#page=3), [p.4 secondary Cox](../../../joi190007supp2_prod.pdf#page=4); [main p.1 primary analysis](../../../jama_bot_2019_oi_190007.pdf#page=1), [p.4 Outcomes/Statistical Methods](../../../jama_bot_2019_oi_190007.pdf#page=4), [p.6 Table2](../../../jama_bot_2019_oi_190007.pdf#page=6), [p.7 narrative](../../../jama_bot_2019_oi_190007.pdf#page=7). Main [p.2 Study Design](../../../jama_bot_2019_oi_190007.pdf#page=2) expressly points to both supplied protocol and SAP.

Source observations: protocol §10.1 Primary study parameter(s) specifies Kaplan–Meier/log-rank/Cox for time-to-event MDD, plus mixed regression for MDD/IDS. SAP p.3 explicitly specifies primary new-MDD logistic regression; p.4 explicitly specifies secondary Cox time-to-onset. Main explicitly uses primary logistic and repeatedly designates Cox as post hoc. Table2 primary supplement/therapy/interaction ORs1.06/.93/.93 and Cox HRs1.05/.91/.91 clearly belong to their named models.

Reproduction/logical rule: primary model and analysis priority differ from protocol to SAP/report; independently, SAP's prospectively specified secondary Cox analysis is not aligned with report's post hoc status. No OR/HR equality is required. The SAP can refine the protocol's primary modeling, but that refinement does not explain why its own Cox provision is called post hoc. This independent SAP/report contrast carries inclusion even under the source-grounded interpretation that SAP is the operative refined plan.

All four criteria: reproduced exact prospective/retrospective statements; primary-model/analysis hierarchy is focusD and nonperipheral; differing formal priority and prespecification status cannot be resolved by interchangeable model terminology or by simply noting SAP agreement with logistic; interpretation of the actual HR1.05(.86–1.27),HR.91(.75–1.10),HR.91(.75–1.11) as planned supporting versus post hoc evidence can change. No absent model parameter is inferred.

Alternatives: SAP may supersede protocol; post hoc may refer to an unreported narrower Cox implementation. The supplied report does describe onset visit/censoring and a proportionality test but identifies no such narrower element as the reason for post hoc status. Human question: which model priority operated prospectively, and what reconciles the planned secondary Cox analysis with its post hoc designation? Classification ambiguity: supplied SAP date/version and amendment chronology are unavailable; document roles are clear.

## Planned primary-MDD additive-interaction sensitivity not reported

Finding:F-XS-005. FocusD; review domain protocol_report; primary relationshipP_R; all relationshipsP_R. Comparator PLAN SAP versus REPORT main/results supplement. Neither REPORT location conflicts numerically with another; they jointly supply the result-coverage side.

Exact sources: [SAP p.4 Interaction of the intervention strategies for our primary outcome](../../../joi190007supp2_prod.pdf#page=4); [main p.1 combination](../../../jama_bot_2019_oi_190007.pdf#page=1), [p.4 methods](../../../jama_bot_2019_oi_190007.pdf#page=4), [p.6 Table2](../../../jama_bot_2019_oi_190007.pdf#page=6), [p.7 MDD narrative](../../../jama_bot_2019_oi_190007.pdf#page=7), [p.8 sensitivity](../../../jama_bot_2019_oi_190007.pdf#page=8); [results p.21 no-MI sensitivity](../../../joi190007supp3_prod.pdf#page=21), [p.22 CACE](../../../joi190007supp3_prod.pdf#page=22). Full REPORT coverage is mainpp.1–11,resultspp.1–25,data-sharingp.1.

Source observations: SAP unconditionally says the investigators will also study additive interaction as a sensitivity analysis for primaryMDD, specifies RERI from a linear odds-ratio model, likelihood-based95%CI, and recoding joint lowest-risk stratum. The speculative biological rationale precedes a definite analysis commitment; it does not make the commitment conditional on statistically significant multiplicative interaction. Main reports multiplicative logistic interactionOR.93(.76–1.14),P.48 and Cox interactionHR.91(.75–1.11),P.36. Its no-MI GEE sensitivity and CACE address other estimands. The results-supplement interaction terms are moderation or multiplicative secondary-outcome terms; no additive estimate/CI is present.

Reproduction/logical rule: a multiplicative interaction coefficient does not supply the explicitly planned additive-departure estimand. Direct full-document searches, exact cited-page readings, and complete current source maps locate no RERI/additive result or omission explanation. Do not infer a numerical RERI from raw counts, or infer that the analysis was never performed.

All four criteria: the plan commitment and bounded supplied-result absence are reproduced; scopeD expressly includes a prespecified primary/key-secondary analysis not reported and comparison tiers expressly include prespecified sensitivity analyses; no immediate text states replacement/deferment and other sensitivity analyses cannot identify the additive result; interpretation of the reported absence of a combined primaryMDD effect lacks its promised additive-scale sensitivity, and the planned estimate/CI is unavailable to extract.

Reason-code distinction: CONDITIONAL_OR_UNREPORTED covers an assumed analytic condition or a desired/unreported detail without an established design commitment. Here the package explicitly supplies an unconditional primary-outcome sensitivity commitment, bringing the observation within the specific qualifying focusD provision. This is not a request for a preferred additional method.

Alternatives: analysis may have been performed but omitted, or formally replaced/deferred; supplied materials establish neither. Human question: where is the planned additive estimate/CI or its documented reconciliation with the reported combination evidence? Classification ambiguity: no role or relationship ambiguity; whether it was performed is outside supplied evidence. Potential downstream impact is limited to completeness and interpretation of interaction-scale evidence; no conclusion reversal is claimed.

## IDS planned endpoint hierarchy

Findings:F-XS-004/F-ST1-003 consolidated. FocusD; review domain protocol_report; primary relationshipP_R; all relationshipsP_R,P_P. Protocol/SAP hierarchy contrast isP_P; protocol/report isP_R; matching SAP/report secondary status does not introduce an additional conflict.

Exact sources: [protocol p.9 summary](../../../joi190007supp1_prod.pdf#page=9), [p.28 §8.1.1/8.1.2](../../../joi190007supp1_prod.pdf#page=28), [p.43 §10.1/10.2](../../../joi190007supp1_prod.pdf#page=43); [SAP p.2 outcomes](../../../joi190007supp2_prod.pdf#page=2); [main p.4 Secondary Outcomes/Statistical Methods](../../../jama_bot_2019_oi_190007.pdf#page=4), [p.8 Table3/narrative](../../../jama_bot_2019_oi_190007.pdf#page=8).

Source observations: protocol main-endpoint list includes MDD and IDS; §10.1 Primary study parameter(s) includes IDS, whereas §10.2 Secondary study parameter(s) separately includes PHQ and other outcomes. SAP explicitly classifies IDS/PHQ as secondary, and report likewise calls IDS secondary and secondary findings exploratory because of multiple comparisons. The IDS measure/timepoints are matched, and its coefficient.60(.15–1.05),P.01 corresponds to the stated full adjusted difference1.20(.29–2.10),P.01 after effect coding and display precision.

Reproduction/logical rule: compare the endpoint/analysis hierarchy, not the doubled numeric estimates or outcome-name abbreviation. Both the protocol's separate main-endpoint and primary-analysis sections distinguish IDS from its secondary-outcome family. This supports a substantive hierarchy comparison rather than assuming that main is universally synonymous with all assessed outcomes.

All four criteria: exact headings/list membership are reproduced and visually confirmed; same IDS endpoint hierarchy falls in focusD and qualifies independently of where its result appears in the abstract; SAP/report refinement makes current reported status clear but supplies no explanation of the contrast with protocol main/primary placement; the prospective status assigned to the reported significant overall IDS effect can change its interpretation in evidence extraction. No required multiplicity adjustment or co-primary decision rule is inferred.

Alternatives: main/primary study parameters might be broader protocol terminology than formal co-primary endpoints, or SAP might prospectively refine/reclassify the hierarchy. Because PHQ is separately in the secondary-analysis subsection and IDS is in the primary subsection, the broader-terminology explanation is not identifiable at once. Human question: was IDS a main/co-primary/key endpoint or a secondary endpoint in the operative prospective hierarchy, and what reconciles the supplied protocol with SAP/report? Classification ambiguity: formal co-primary status and chronology are not established; the candidate must not assert a proven co-primary designation.

## Primary MDD power specification

Findings:F-XS-001/F-ST1-001 consolidated. FocusD; review domain protocol_report; primary relationshipP_R; all relationshipsP_R. PLAN protocol versus REPORT sample-size/power discussion; SAP contains no alternative sample-size calculation to establish an additional relationship.

Exact sources: [protocol p.16 §4.4](../../../joi190007supp1_prod.pdf#page=16), [p.17 continuation](../../../joi190007supp1_prod.pdf#page=17), [p.1 final-amendment version](../../../joi190007supp1_prod.pdf#page=1); [main p.4 Sample Size](../../../jama_bot_2019_oi_190007.pdf#page=4), [p.9 power discussion/limitations](../../../jama_bot_2019_oi_190007.pdf#page=9).

Source observations: protocol control30%,intervention15%,90%power,two-sidedalpha.05,180/group,20%dropout,250/arm sufficient; it explicitly mentions additive interaction and80%power if synergistic pure groups are compared. Report control30%,active20%,relative33%reduction,absolute10%,90%power,two-sidedalpha.05,196/factorial cell,22%attrition,250/cell; it explicitly targets intervention main effects. Discussion states unexpectedly lower MDD onset reduced power.

Reproduction/calculation: numerical active-rate assumptions15%and20% differ by5percentagepoints; the associated differences from control30% are15and10percentagepoints; dropout assumptions differ by2percentagepoints. Integer percentage rounding intervals for active risk[14.5,15.5)and[19.5,20.5) do not overlap. The report's392/196 wording is readily resolved as marginal/cell allocation in its factorial context and is not a basis for inclusion. Protocol introductory25% wording is likewise not the issue. Different factorial powering contrasts are explicitly retained, not forced to reproduce a common sample-size algorithm.

All four criteria: inputs/contrasts are reproduced and protocol p.16 visually confirmed; primary-outcome power specification is focusD and qualifying; knowing that the contrasts differ explains why calculations need not numerically coincide but does not establish how two materially different sets of incidence/dropout assumptions and power objectives jointly governed the same final recruitment target; extraction of planned assumptions and interpretation of the primary null result's reported power basis could change. No exact interaction-power algorithm is inferred.

Source-grounded context assessment: the strongest alternative is that protocol supplies an interaction-oriented design calculation while report supplies a distinct supplementary main-effect calculation. This permits coexistence and is retained for human review; however, neither text identifies the report calculation as supplementary or maps its input assumptions to the protocol calculation, and the report frames its paragraph as the design sample-size basis. Matching250/cell does not identify the operative assumption set. Inclusion is bounded to this unresolved planned-versus-reported specification, not a claim that power or sample size fails arithmetic.

Other alternative: inputs were revised but retained protocol text was not updated. Human question: what operative primary-design specification and amendment/calculation mapping reconciles30%/15%with20%dropout to30%/20%with22%attrition for the same target? Classification ambiguity: contrasts are explicitly different; the card must retain that distinction and avoid asserting that15%and20% belong to demonstrably identical marginal populations.

## Counts and limitations

Eight findings independently screened; eight included finding rows; five distinct included issues; zero screened-out rows. Consolidation preserves all affected locations and both checker provenances in each overlapping pair. Every qualifying comparison is focusD rather than peripheral. No severity, validity, acceptance, disposition, or final correction is assigned. No missing scientific-source unit affects this screening. Limitations are absent SAP chronology, absent explicit amendment mappings, absence of the planned additive sensitivity result in the supplied package, and inability to infer actual analysis execution from its reporting absence.
