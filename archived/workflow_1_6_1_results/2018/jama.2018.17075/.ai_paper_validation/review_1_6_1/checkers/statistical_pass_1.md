# Statistical consistency review — pass 1

Runtime agent ID: /root/statistics_1. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. This is the fresh mandatory pass-1 stage, not a mapper extension or pass 2.

Scope: all 110 stable statistical relationships in statistics/relationship_inventory.md, including every underlying cell, interval, test, model label, method paragraph and decision rule represented by its grouped rows. The canonical inventory was supplied by the coordinator; this assigned artifact owns its explicit pass-1 completion records. The coordinator performs the canonical inventory merge. Two findings meet this checker's inclusion screen; 26 distinct observations are excluded below. No candidate IDs or adjudications are assigned here.

Read QUALITY_CONTROL_SCOPE.md and the complete workflow_1_6_1/review_contract.md, settings, current tooling record, source inventory, statistical inventory and source-linked mapper parts. No earlier candidate, checker, screening, quality or report conclusions were consulted. REPORT: main article DOC-001 and results supplement DOC-003. PLAN: original/final protocol, dated amendments, SAP update and DSMC governance material DOC-002; its interim tabulations were checked as prospective operational material with their masked labels preserved.

Evidence authority: supplied PDFs. Direct Poppler pdftotext -layout was used for assigned main methods/results pp3–8; DOC-003 result/method tables pp4–6 and8–23; DOC-002 relevant original/final statistical specifications, amendments, ancillary methods and all interim tables pp189–194. Current maps and unchanged source-matched native/layout assets were locators. Source-matched rendered pages visually confirmed main Table2, eTable7, eTable12, eFigures1/2/4, and scanned amendment/SAP-update pages144,150,151,152,183,184,185. The source-matched images are the existing legacy renderings; their rendering engine is unrecorded as stated in the curator inventory. No new persistent derivative, OCR, fallback environment, GPU or external source was used.

## Check rules and calculation boundaries

Every printed estimate lies between ordered interval endpoints, except that source typography is retained and screened separately. H versus N is the comparison; risks, odds and hazards retain their distinct labels. Binary unadjusted RRs are checked only where the report explicitly states an unadjusted analysis. The unadjusted chi-square equal-proportions method and two-sided significance rule are supplied in main pp3–4. Two-arm Pearson calculations use the table's exact counts: pooled p=(a+b)/(n+m), X²=(a/n−b/m)²/[p(1−p)(1/n+1/m)]. The mathematical degrees of freedom follow the displayed contingency table, rather than an inferred model. A four-category homogeneity diagnostic is detailed separately in F-ST1-002, with its tested-category alternatives explicit.

Log-Wald intervals recomputed from SE(log RR)=sqrt(1/a−1/n+1/b−1/m) are diagnostic approximations because the source does not specify its complete CI implementation; they do not replace the printed CIs. For example primary RR=0.992568, diagnostic CI0.824455–1.194959 and X²0.006207/P0.937204 reconcile with RR0.99(0.82–1.19), P=.94. Hospital mortality RR1.111628/P.568097 and six-month mortality RR1.145774/P.453996 reconcile. All infection and primary subgroup rows outside the bleeding pattern reconcile with the displayed unadjusted risks/tests. Main ordinal OR0.97(0.71–1.34), adjusted RR0.98(0.87–1.11), and mortality HR1.13(0.76–1.69) have ordered containing intervals, coherent directions and nonsignificant null inclusion. Exact covariance, estimator implementation and coefficient tests are not reconstructed from convention.

Primary sample-size diagnostics preserve formula uncertainty: with alpha.05, p0=.50, p1=.65, an uncorrected normal planning formula gives approximately169.31 per arm rather than the stated182. This is a diagnostic, not a contradiction: the source does not establish that formula or its continuity treatment. Loss inflation364/.95=383.16 supports384; noncompliance dilution384/.88²=495.87 is a plausible source-grounded explanation of496, rather than treating intervention withdrawal as deletion of all outcomes. The latest plan expressly supplies East approximate chi-square power82.3% with366 fully evaluable and additional monitoring, while original planning quotes80% with364. Main82% is compatible with that context. Exact sequential power requires the unprinted information fractions/joint dependence, not merely visit counts. Ancillary normal/correlation approximations for AKI, renal biomarkers, energy and brain biomarkers are compatible with approximate stated targets; no ancillary result in the report relies on an unresolved competing plan specification.

All superiority statements were matched to the printed nonsignificant primary result; they were not recast as equivalence. No reported noninferiority/equivalence margin or success declaration applies. Multiplicity is disclosed as unadjusted and secondary results exploratory. Interim tables contain no reported comparison near any stated stopping boundary; no unprinted stopping recommendation was assumed.

## Findings

### F-ST1-001

**Issue:** The two main Table2 bleeding rows attach incompatible unadjusted RR/CI/P blocks to their printed event counts.

**Relationships:** S010, S011, S027, S095. **Focus areas:** A and B. **Proposed review domain:** statistical_results. **Proposed primary relationship:** S_C; all relationships S_C, S_W.

**Locations and roles:** REPORT [main PDF p7, Table2, intracranial and extracranial bleeding rows](../../../jama_cooper_2018_oi_180132.pdf#page=7); REPORT [main p3, Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=3) and [p4, two-sided testing rule](../../../jama_cooper_2018_oi_180132.pdf#page=4); REPORT [results supplement PDF p10, eTable6, cerebral and non-cerebral bleeding rows](../../../joi180132supp2_prod.pdf#page=10). Main pp1/5 repeat the intracranial proportions but do not independently settle the RR/interval assignment.

**Printed values:** Main intracranial bleeding47/260(18.1%) versus37/240(15.4%); absolute difference2.7(−3.9 to9.2) percentage points; RR1.23(0.43–3.5), P=.70. Main extracranial bleeding8/260(3.1%) versus6/240(2.5%); absolute difference0.6(−2.3 to3.5); RR1.17(0.79–1.74), P=.43. eTable6 prints exactly the same respective counts with intracranial P=.43 and extracranial P=.70. Main methods explicitly specify unadjusted chi-square comparisons with RR/RD95%CI.

**Rule and calculation:** An explicitly unadjusted risk ratio must equal the ratio of the printed event risks. Intracranial(47/260)/(37/240)=1.172557, and its stated equal-proportions Pearson calculation gives X²=.631872/P=.426669. Extracranial(8/260)/(6/240)=1.230769, X²=.152625/P=.696039. Diagnostic log-Wald95%CI is0.791181–1.737769 for intracranial and0.433345–3.495582 for extracranial. These diagnostic intervals align with the *other* main row's interval, as do the count-determined RR and P. CI diagnostics support a possible exchanged block but are not required for the point-estimate discrepancy. Fixed integer counts yield rounded RR1.17 and1.23 respectively; these cannot belong to the opposite displayed half-unit RR intervals[1.225,1.235) and[1.165,1.175). The P values likewise remain different beyond their .005 half-unit display allowances. Risk differences/count percentages remain on their count-consistent rows.

**Affected result or extracted value:** ITT ten-day intracranial and extracranial bleeding risk ratios and confidence intervals, and the P value attached to each adverse-event outcome. Extracting Table2 verbatim gives the broad interval for the common intracranial event and the narrow interval for the rare extracranial event, whereas the printed counts support the other precision pattern.

**Why context does not resolve it:** Neither main row identifies a different analysis population or adjusted model. Counts/RD and RR/CI/P coexist as one unadjusted result per outcome. The supplement clarifies the P attachment but supplies no independent RR/CI block, so a reader must reconstruct and decide which printed block applies. This exceeds a missing symbol or routine terminology difference and can change effect/precision extraction for both outcomes.

**Alternatives and missing definitions:** A exchanged RR/CI/P block is consistent with the count diagnostics; alternatively an undisclosed different population or method could produce different blocks. The supplied table and stated method do not identify such a population/model. No causal explanation is asserted and no preferred replacement is prescribed.

**Exact human question:** Which RR, confidence interval and P value belong to each ten-day bleeding outcome, given the printed unadjusted counts, risk differences and supplementary P assignments?

### F-ST1-002

**Issue:** The time-to-33°C table's P=.09 does not reconcile with the displayed equal-proportions comparison, and the tested category set is not separately identified.

**Relationships:** S023, S030, S096. **Focus areas:** B and C. **Proposed review domain:** statistical_results. **Proposed primary relationship:** S_C; all relationships S_C, S_W.

**Locations and roles:** REPORT [results supplement PDF p11, eTable7, all four time categories and merged P cell](../../../joi180132supp2_prod.pdf#page=11); REPORT [main PDF p4, Statistical Analysis, time to achieve33°C method](../../../jama_cooper_2018_oi_180132.pdf#page=4); REPORT [main p5, Additional Outcomes](../../../jama_cooper_2018_oi_180132.pdf#page=5). eTable7 visually confirms that the P cell spans the displayed category block.

**Printed values and rule:** eTable7:1–7hours18/49 favorable,8–13hours28/67,>13hours32/59, never39/65; one P=.09, favorable proportions36.7%,41.8%,54.2%,60.0% with95%CI. Main p4 states that the effect on favorable outcome of time taken for cooled patients to achieve33°C was compared using an unadjusted chi-square test for equal proportions. Main p5 describes no significant difference and cites eTable7. Main general rule is two-sided P<.05.

**Calculation:** For the displayed4×2 table, favorable/unfavorable counts are(18,31),(28,39),(32,27),(39,26), total117 favorable/240. The homogeneity statistic sum over the eight cells of(O−E)²/E with E=n_category×(117/240 or123/240) is8.133762. Its degrees of freedom are(4−1)(2−1)=3, determined by those four displayed independent category proportions; the corresponding chi-square upper-tail probability is.043327. All numerators/denominators are integers and fixed, so percentage display precision does not alter this calculation; P=.09 allows[.085,.095), which excludes.043327. If only the three attained-temperature categories were tested, the printed counts instead give X²3.658952 with(3−1)(2−1)=2, P=.160498, also outside that interval. These calculations diagnose the printed equal-proportions mapping; no ordinal trend test, stratification, model, covariance or unprinted denominator is assumed.

**Affected result or extracted value:** The additional primary-GOS-E association with time to reach33°C: the P value a reader would extract, the category set to which it applies, and the report's nonsignificant description of that association. The displayed four-category calculation crosses the report's .05 rule; this does not change the randomized primary treatment contrast and does not establish a causal timing effect.

**Why context does not resolve it:** A reader cannot choose between a four-category comparison displayed under one merged P value and a comparison restricted to the three groups that attained33°C. Both count-based equal-proportions calculations differ from.09. Neither the table nor the cited method identifies another tested-category set or computation to reconcile.09. This is a supplied test/result relationship, rather than a comparison of contributor counts across exploratory displays.

**Alternatives and missing definitions:** The printed P could apply to an unshown tested subset, a different chi-square computation or a different analysis; alternatively the displayed counts/P mapping may require clarification. The exact tested categories, any non-Pearson computation or correction, and any omitted records are not defined. Pearson homogeneity is the conventional direct realization of the stated unadjusted equal-proportions test; its calculation is labeled a diagnostic where that implementation is not explicitly named. These limits remain for independent inclusion screening; they are not resolved by inferring the reported method from external convention.

**Exact human question:** What tested category set and chi-square computation produced P=.09 in eTable7, and how should that P be matched to the four printed favorable-outcome counts and the main nonsignificant claim?

## Excluded observations

Each observation below is recorded once with exactly one scope reason code; no excluded observation receives a finding ID.

| Location | Observation | Reason code |
|---|---|---|
| Main pp1,5,7; S001 | Abstract prints positive0.4% while narrative/table print−0.4;48.8% versus49.1% and the interval immediately identify H−N as negative. A missing sign is locally resolved. | NOTATION_OR_TYPOGRAPHY |
| Main Table2 and supplementary unadjusted outcome tables; S001,S004,S005,S007,S008,S009,S012,S013,S014,S015,S018,S019,S098,S099,S103,S104 | Recomputed risks, percentage differences, RRs and intervals may differ in last displayed digit; half-unit input allowances and exact count calculations reconcile outside the separately emitted bleeding pattern. | ROUNDING_OR_DISPLAY_PRECISION |
| Main pp3–5/7; S002,S027 | Severity-adjusted primary RR/CI need not reproduce from unadjusted event proportions; prognostic model and random strata are disclosed. | MODEL_VERSUS_CRUDE |
| Main pp4–5; S003,S028 | A diagnostic log-normal P from rounded ordinal OR/CI does not determine the actual coefficient test; printed precision permits nonsignificant compatibility. Score-test statistic/coding are not printed. | CONDITIONAL_OR_UNREPORTED |
| Main pp4–5 and supplement p5; S006,S029,S091 | Main/caption P=.54 differs from displayed logrank.5349; Cox coefficient and logrank are distinct statistics, and an exact shared-test attribution is unprinted. | CONDITIONAL_OR_UNREPORTED |
| Main p3; original/final plan pp27/83–84; S024,S038,S054,S055 | Normal uncorrected planning n169.31/arm versus182/arm does not establish a discrepancy without the planning formula/continuity convention; amended East power explains original80% versus main82%. | CONDITIONAL_OR_UNREPORTED |
| Original/final plan pp27/83; S038,S054 |384→496 is not reproduced by ordinary attrition division alone, but intervention noncompliance can dilute the treatment contrast;384/.88²≈496 reconciles, so treating all intervention withdrawals as missing outcomes is conditional. | CONDITIONAL_OR_UNREPORTED |
| Original/final plan pp28/84 and scanned amendment pp150–151; S039,S057,S080 |96% ordinal power cannot be fully reconstructed without the eight-category probability vector and exact rank-test calculation. One-sided planning power is explicitly identified, separate from report's two-sided inferential rule. | CONDITIONAL_OR_UNREPORTED |
| Original plan p28 versus final plan pp84–85; S041,S043,S058,S059,S060 | Original MH/logistic wording differs from later binary/ordinal model specifications; supplied dated revisions resolve which is final. | CONTEXT_RESOLVES |
| Plan pp25/81 versus endpoint pp19/72; S047,S048,S053 | Six-month post-injury versus post-randomization follow-up wording is resolved by enrollment within hours of injury and common six-month endpoint context. No competing reported outcome is identified. | TERMINOLOGY_OR_WORDING |
| Plan pp84–86; S025,S055,S068 | Eleven analyses versus six visits is resolved as two outcomes at five visits plus one short-term-mortality assessment; no different monitoring visit rule is needed. | CONTEXT_RESOLVES |
| Main p4 and final plan p84/charter p188; S032,S055,S056,S086 | Conventional.05 versus stated final.0459/.048 monitoring thresholds does not change any printed primary/secondary decision; plan explicitly treats monitoring adjustment as small, and versions differ. Exact spending implementation is not supplied. | CONTEXT_RESOLVES |
| Scanned plan p152 and charter p188; S045,S080,S086 | P<.005 or approximately P<.001 accompanies an explicit three-SD boundary; absolute Z≥3 establishes the intended monitoring rule despite shorthand P descriptions. | CONTEXT_RESOLVES |
| Main p3 and plan pp69,77,97,99–100; S026 | Synopsis's further72hours after target versus detailed72hours after randomization/ideal post-injury wording is resolved by the operative rewarming flowchart, including late-cooling minimum48hours. | CONTEXT_RESOLVES |
| Main p3 and final plan pp77,99–100; S026 | Main rewarming ceiling.25°C/h versus plan target.17°C/h is compatible with the slower target and individualized emergency/ICP exceptions; no competing reported inferential value is identified. | CONTEXT_RESOLVES |
| Main pp3–4 and plan pp84,174–175; S027,S040,S052,S082 | Randomized-group language versus named modified-ITT exceptions does not establish excluded ineligible-never-treated participant counts beyond the reported consent exclusions. | CONDITIONAL_OR_UNREPORTED |
| Main p3 and plan pp72,84–85; S044,S049,S062,S064,S083 | Sliding dichotomy, QOL, economics, SACE/CACE and other secondary analyses are absent or expressly deferred; none is designated a key secondary endpoint in supplied material. | PERIPHERAL_COMPARISON |
| Plan pp108–132/163–170; S069,S070,S071,S072,S073,S074,S075,S076,S077,S078,S079,S081 | Ancillary renal/energy/brain-biomarker/TEG/PK methods and literal terminal-slope AUC wording have no reported main/key-secondary quantity depending on them; no broad ancillary methodology review is registered. | PERIPHERAL_COMPARISON |
| Main p5 Table1 and supplementary baseline tables; S036,S097,S102,S110 | Baseline descriptive quantity differences, literal median/IQR placement, and transposed count/percentage typography do not change a primary/key-secondary estimate or analysis-set size. | PERIPHERAL_COMPARISON |
| Supplement pp8–10/13/18/23 and interim tables; S087,S088,S089,S092,S093,S094,S095,S097,S102,S110 | Exact continuous, rank, sparse-cell or corrected-test P values cannot be reconstructed from displayed summaries or unspecified implementation; e.g. sparse VF P1.00 can reflect a corrected/exact comparison. | CONDITIONAL_OR_UNREPORTED |
| Supplement p8; S093 | Noradrenaline-duration P<.0001 wraps the final digit to the next source line; no display-zero-only finding is appropriate. | NOTATION_OR_TYPOGRAPHY |
| Supplement p5; S091 | Caption uses death probability while plot title/axis/curve show survival and mortality HR; the complementary quantity is immediately identifiable. | TERMINOLOGY_OR_WORDING |
| Supplement pp14/19; S097,S102 | Adjusted RR1.04 and1.11 happen to resemble crude favorable ORs; equality of rounded numbers does not establish model/effect-measure identity under the disclosed adjustment. Each adjusted outcome row names its endpoint, including unfavorable in eTable11. | MODEL_VERSUS_CRUDE |
| Supplement pp15–16/20–21; S100,S101,S105,S108 | Unlabelled plotted intervals, AUC compliance cutoff, imputation strata and pooling details are not supplied; conclusions about those implementations would depend on assumed definitions. MI RR1.00(.95–1.06) cannot be tested as a crude ratio/CI; no pooling or covariance is inferred. | CONDITIONAL_OR_UNREPORTED |
| Supplement p22; S109 | Stray275 in the adjusted interval is an obvious inserted token. | NOTATION_OR_TYPOGRAPHY |
| Supplement pp22–23; S109,S110 | Mean-time P=.01 and median/rank-time P=.02 refer to different summaries and do not contradict. | CONTEXT_RESOLVES |

## Explicit relationship completion

Grouped rows cover every underlying mapped row/cell; a missing definition limits mechanical reconstruction, not review coverage. All statuses below are pass-specific completion, without an evidence/adjudication disposition.

| S ID | Pass 1 status | Check result and rationale |
|---|---|---|
| S001 | PASS_1_COMPLETE | Primary counts, unadjusted RR/RD, null-containing CI and chi-square P reconcile; abstract sign screened. |
| S002 | PASS_1_COMPLETE | Adjusted RR interval ordered/containing, direction/test coherent; model-versus-crude comparison excluded. |
| S003 | PASS_1_COMPLETE | Ordinal OR interval contains estimate/null; rounding and unprinted coefficient test prevent unique inversion. |
| S004 | PASS_1_COMPLETE | Hospital mortality counts/RR/RD/P reconcile; one unavailable N hospital outcome is distinct from six-month set. |
| S005 | PASS_1_COMPLETE | Six-month mortality RR 1.14577/P .453996 reconcile; death denominator matched to Figure 1. |
| S006 | PASS_1_COMPLETE | HR/CI/direction coherent; survival and logrank matched without forcing coefficient-test equality. |
| S007 | PASS_1_COMPLETE | Pneumonia risks/RR 1.07317/P .401146 reconcile. |
| S008 | PASS_1_COMPLETE | Bacteremia risks/RR 1.46154/P .285058 reconcile. |
| S009 | PASS_1_COMPLETE | Other infection RR .874494/P .531864 reconcile. |
| S010 | PASS_1_COMPLETE | Intracranial unadjusted RR/P blocks do not reconcile; F-ST1-001 consolidated bleeding pattern. |
| S011 | PASS_1_COMPLETE | Extracranial unadjusted RR/P blocks do not reconcile; same F-ST1-001. |
| S012 | PASS_1_COMPLETE | Hematoma-yes counts/RR .839506/P .443828 reconcile. |
| S013 | PASS_1_COMPLETE | Hematoma-no counts/RR 1.02696/P .793606 reconcile; strata partition primary set. |
| S014 | PASS_1_COMPLETE | Mass-lesion-yes RR .808489/P .351126 reconcile. |
| S015 | PASS_1_COMPLETE | Mass-lesion-no RR 1.03748/P .716224 reconcile; partition totals match. |
| S016 | PASS_1_COMPLETE | InteractionP .43 corresponds logistic subgroup interaction, not either within-subgroup P. |
| S017 | PASS_1_COMPLETE | InteractionP .33 corresponds the separate lesion interaction; nonsignificant claim coherent. |
| S018 | PASS_1_COMPLETE | PP pneumonia counts in eTable 9 give RR 1.23295/P .018773 and positive RD. |
| S019 | PASS_1_COMPLETE | AT pneumonia eTable 11 gives RR 1.29464/P .003317; CI/direction coherent. |
| S020 | PASS_1_COMPLETE | All PP/AT baseline tests/outcome rows read; primary nonsignificant statements match eTables 9/11. |
| S021 | PASS_1_COMPLETE | PP/AT 72-hour sensitivity primary estimates remain nonsignificant; outcome and compliance subsets matched. |
| S022 | PASS_1_COMPLETE | Worst/best/MI and adequate-cooling statements matched; primary randomized contrast remains separate. |
| S023 | PASS_1_COMPLETE | Other-outcome tests read; time-to 33°C equal-proportions relationship raises F-ST1-002. |
| S024 | PASS_1_COMPLETE | Power/target inputs compared with final plan; formula-specific approximations screened as conditional. |
| S025 | PASS_1_COMPLETE | Interim schedule matched to dated amendments; no supplied stopping decision conflicts. |
| S026 | PASS_1_COMPLETE | Intervention durations/targets and operative rewarming flow matched; context resolves summarized anchors/ceiling. |
| S027 | PASS_1_COMPLETE | Randomized-group/no-imputation and hierarchical adjusted model read; bleeding unadjusted specification supports F-ST1-001. |
| S028 | PASS_1_COMPLETE | Ordinal model/score-check description coherent; exact score/coding absence recorded. |
| S029 | PASS_1_COMPLETE | Cox/KM/logrank, censoring and visual PH check distinguished; no guessed covariance/test. |
| S030 | PASS_1_COMPLETE | Logistic interactions coherent; stated unadjusted cooling-time comparison supports F-ST1-002. |
| S031 | PASS_1_COMPLETE | Eligibility, compliance and early-death rules matched to SAP update/results populations. |
| S032 | PASS_1_COMPLETE | Two-sided .05/unadjusted multiplicity/exploratory status explicit; no equivalence margin assumed. |
| S033 | PASS_1_COMPLETE | Temperature/ICP graphics and process tests read; no exact trajectory test invented from boxplots. |
| S034 | PASS_1_COMPLETE | No-improvement conclusion matched to nonsignificant primary estimate, not read as equivalence. |
| S035 | PASS_1_COMPLETE | Historical RR/CI/P kept separate; historical tests not reconstructed externally. |
| S036 | PASS_1_COMPLETE | Main baseline table contains no inferential P; peripheral descriptive observations excluded. |
| S037 | PASS_1_COMPLETE | Superiority/null/no-difference aim consistent with randomized primary comparison. |
| S038 | PASS_1_COMPLETE | Original power inputs/attrition/noncompliance read; unprinted planning formula prevents unique reproduction. |
| S039 | PASS_1_COMPLETE | One-sided ordinal power recognized; category probabilities unavailable for exact calculation. |
| S040 | PASS_1_COMPLETE | Original ITT/withdrawal follow-up matched to revised final population definitions. |
| S041 | PASS_1_COMPLETE | Original stratified/logistic primary methods superseded by dated final plan context. |
| S042 | PASS_1_COMPLETE | Original KM/Cox specifications coherent with final/report survival methods. |
| S043 | PASS_1_COMPLETE | Original adjusted ordinal method compared with final unadjusted ordinal specification; versions distinguished. |
| S044 | PASS_1_COMPLETE | Sliding dichotomy definition read; report deferral and non-key-secondary status retained. |
| S045 | PASS_1_COMPLETE | Original single interim 3 SD rule matched chronologically to later schedule; approximate P shorthand screened. |
| S046 | PASS_1_COMPLETE | Individual randomization and ambulance/centre strata do not imply cluster-randomized treatment. |
| S047 | PASS_1_COMPLETE | Original six-month ascertainment/missingness forms read; no missing-data method inferred from absence. |
| S048 | PASS_1_COMPLETE | Final favorableGOSE 5–8 endpoint/null/time anchor matches report; hours-scale anchor wording resolved. |
| S049 | PASS_1_COMPLETE | All final secondary endpoint models/distinct ordinal/sliding outcomes read; key status not invented. |
| S050 | PASS_1_COMPLETE | Time and lesion interactions matched to report statistical method; timing result separately examined. |
| S051 | PASS_1_COMPLETE | Individual 1:1/strata/block design supports independent-arm and sensitivity descriptions. |
| S052 | PASS_1_COMPLETE | Final full-analysis exceptions and later cooling withdrawal follow-up distinguished. |
| S053 | PASS_1_COMPLETE | Blinded assessor/GOSE and lost/unscorable form definitions read; no imputation inference. |
| S054 | PASS_1_COMPLETE |364/384/496/500 power/inflation sequence read; formula uncertainty and dilution alternative recorded. |
| S055 | PASS_1_COMPLETE | East 82.3%, amended monitoring and .0459 final rule read; visit/outcome count and robust decisions screened. |
| S056 | PASS_1_COMPLETE | Two-sided 95%CI and primary multiplicity statement coherent; report exploratory distinction retained. |
| S057 | PASS_1_COMPLETE | One-sided 96% ordinal planning example separate from two-sided reported tests; missing category vector named. |
| S058 | PASS_1_COMPLETE | Final primary binomial/RR/RD/OR specification matched; report primary RR/RD reconcile. |
| S059 | PASS_1_COMPLETE | Proportional/partial-proportional model options consistent with report's justified proportional assumption. |
| S060 | PASS_1_COMPLETE | Binary log/identity-binomial estimates compatible with report's RR/RD labeling outside bleeding issue. |
| S061 | PASS_1_COMPLETE | Robust continuous linear-regression plan read; no supplied main QOL model result depends on absent detail. |
| S062 | PASS_1_COMPLETE | SACE explicitly distinct from crude favorable-survivor percentages; no estimand equivalence assumed. |
| S063 | PASS_1_COMPLETE | KM/logrank/unadjusted and adjusted Cox plan read; reported HR direction/CI coherent. |
| S064 | PASS_1_COMPLETE | Economic endpoint/QALY/cost windows read; deferred non-key result not registered. |
| S065 | PASS_1_COMPLETE | Prespecified lesion strata and treatment interaction matched to main Table 2; no statistical conflict. |
| S066 | PASS_1_COMPLETE | Adjustment intention read with report's named IMPACT/strata model; absent individual covariates not invented. |
| S067 | PASS_1_COMPLETE | PP/AT/compliance causal estimands distinguished; dated dose update resolves operational subsets. |
| S068 | PASS_1_COMPLETE | Monitoring primary/mortality windows/no-futility rule matched;11 tests versus 6 visits resolved. |
| S069 | PASS_1_COMPLETE | AKI approximate continuous/binary power checked diagnostically; no main result reliance. |
| S070 | PASS_1_COMPLETE | AKI endpoints, transforms and model types read; no supplied paired/independent contradiction relied on by report. |
| S071 | PASS_1_COMPLETE | Renal correlation/change power inputs coherent approximately; unknown repeated correlation expressly disclosed. |
| S072 | PASS_1_COMPLETE | Renal repeated-measure interaction/logistic/ROC specifications read; ancillary/nonreported scope screened. |
| S073 | PASS_1_COMPLETE | BEAR 72-hour/7-day/treatment-period endpoints and ratio denominators distinguished. |
| S074 | PASS_1_COMPLETE | Energy 400/400 effect and 16→20 attrition power approximately coherent; no reported dependent value. |
| S075 | PASS_1_COMPLETE | Brain biomarker correlation 40/group and repeated-group analysis read; exact rank power unprinted. |
| S076 | PASS_1_COMPLETE | TEG between/within-patient contrast consistent with patient random-effects model. |
| S077 | PASS_1_COMPLETE | PK 10 patient convenience/paired-temperature and mixed model defined coherently. |
| S078 | PASS_1_COMPLETE | Clearance units reconcile; terminal-slope AUC phrase preserved with missing definition, ancillary scope excluded. |
| S079 | PASS_1_COMPLETE | PK paired t/Wilcoxon/McNemar choices conditional on stated within-patient structure/assumptions. |
| S080 | PASS_1_COMPLETE | Scanned V 2→V 3 sample/interim/ordinal changes visually checked; versions and explicit 3 SD rule retained. |
| S081 | PASS_1_COMPLETE | Full TEG data structure/model/amendment read; paired/repeated structure accounted for. |
| S082 | PASS_1_COMPLETE | V 8 modified ITT and extra safety schedule explain later final-plan specifications. |
| S083 | PASS_1_COMPLETE | V 9 May 2017 SAP context, monitoring outcome windows and CACE addition read; no raw survivor equivalence assumed. |
| S084 | PASS_1_COMPLETE |500→510 blinded attrition rationale read; no fully specified revised power formula to contradict. |
| S085 | PASS_1_COMPLETE | SAP dose/eligibility/early-death rules and IMPACT-only adjustment templates visually checked against results. |
| S086 | PASS_1_COMPLETE | Charter 3 SD/.048 final and no-futility rules read; approximateP shorthand/context exclusions recorded. |
| S087 | PASS_1_COMPLETE | All 11 masked 2015 tests/category and block tables checked; no stopping-boundary crossing printed. |
| S088 | PASS_1_COMPLETE | All 13 masked 2016 tests/category and survival denominators checked; no stopping decision conflict. |
| S089 | PASS_1_COMPLETE | All 13 masked 2017 tests/category/survival denominators checked; no unprinted recommendation inferred. |
| S090 | PASS_1_COMPLETE | All 9 rewarming positions visually checked for interval containment/order; patient random effects/95%CI explicit. |
| S091 | PASS_1_COMPLETE | KM curve/HR/logrank/null direction coherent; caption terminology and test-attribution exclusions recorded. |
| S092 | PASS_1_COMPLETE | All location/time comparisons read; exact median-based P unavailable without distributions. |
| S093 | PASS_1_COMPLETE | Every process comparison/interval/definition checked; sparse/continuous test reconstruction limited, wrapped P screened. |
| S094 | PASS_1_COMPLETE | All 5 outcomes checked; mean 4.2 withP .86 permits rounded differences; survivor denominator coherent. |
| S095 | PASS_1_COMPLETE | All adverse-event tests checked; supplement bleeding P assignments support F-ST1-001. |
| S096 | PASS_1_COMPLETE | All 4 time-bin proportions/CIs/P checked; stated equal-proportions mapping raises F-ST1-002. |
| S097 | PASS_1_COMPLETE | All PP baseline/primary/adjusted rows read; unadjusted primary RR 1.02361/P .858283 reconcile. |
| S098 | PASS_1_COMPLETE | All 7 PPsecondary outcome count/RR/CI/P rows checked; pneumonia significant/exploratory and others coherent. |
| S099 | PASS_1_COMPLETE | All 4 PPsubgroup estimates and 2 interactionP values checked; partitions/directions/intervals coherent. |
| S100 | PASS_1_COMPLETE | All 17 PPtemperature positions visually checked; bars contain plotted centers; unprinted level/model not assumed. |
| S101 | PASS_1_COMPLETE | PP 72-hour sensitivity counts/RR 1.00302/P .981933/kappaCI checked; AUC cutoff absent, not inferred. |
| S102 | PASS_1_COMPLETE | All AT baseline/primary/adjusted rows checked; primaryRR 1.05912/P .648119 coherent; explicit unfavorable adjusted label retained. |
| S103 | PASS_1_COMPLETE | All 7 ATsecondary count/RR/CI/P rows checked; pneumoniaRR 1.29464/P .003317 coherent. |
| S104 | PASS_1_COMPLETE | All 4 ATsubgroup estimates/2 interactionP values checked; no null/claim/direction conflict. |
| S105 | PASS_1_COMPLETE | AT 72-hour sensitivityRR 1.02363/P .854003 reconcile; no inferred AUC threshold or imputation. |
| S106 | PASS_1_COMPLETE | Worst-casecounts/RR .864/RD−7.08333/P .113325 reconcile and remain nonsignificant. |
| S107 | PASS_1_COMPLETE | Best-caseRR 1.13929/RD 6.44231/P .150027 reconcile; null-containing intervals ordered. |
| S108 | PASS_1_COMPLETE | MI row, MAR/PMM/11 datasets/CMH/score method read; no stratification/pooling variance inferred; model comparison excluded. |
| S109 | PASS_1_COMPLETE | Adequate-dose OR/adjusted OR contain null;16-minute mean-time contrast coherent;275 token excluded. |
| S110 | PASS_1_COMPLETE | All post hoc baseline tests/footnotes checked; mean versus median P distinguished and peripheral values screened. |

## Limitations and handoff

No assigned statistical relationship was omitted. Exact model coefficients, covariance matrices, variance estimators, imputation strata/pooling, time-test implementation/category set and complete planning formulas are not supplied; each affected mechanical boundary is named above. Source scans were covered with source-matched images. Source/reused artifacts were preserved. No exact unlabelled graphical coordinates were promoted to printed numbers. Pass 2 must use a different fresh high-effort runtime agent after the complete ledger, independent screening and mechanical recheck exist, revisit every explicit S ID, and retain these exclusions without re-emitting observations already screened.
