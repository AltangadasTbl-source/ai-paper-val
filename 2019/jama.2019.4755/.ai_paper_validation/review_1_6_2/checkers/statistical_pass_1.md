# Statistical pass 1

- **Runtime agent ID:** root/statistics_one
- **Model:** gpt-6.1-sol
- **Reasoning effort:** high
- **Start mode:** FRESH_SPAWN
- **Pass:** 1
- **Exact scope:** Every inferential/statistical relationship in the main and merged support maps: 49 main groups, 34 protocol groups and 22 SAP/support groups; 105 total. Every assigned group is completed below.
- **Findings:** 2
- **Excluded observations:** 10
- **Scientific coverage limitation:** None. Exact inversion is bounded by named unreported definitions: individual primary P-value algorithm/test statistic/SE; sex-allocation inputs for power; site likelihood-ratio reference distribution; patient-level first-sample dates. No missing definition is used to infer a contradiction.

The complete QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read. Discovery used supplied source PDFs, permitted reusable extraction/page assets, and fresh evidence maps; no old candidate set, checker conclusions, screening log or final report was read. Fixed-method arithmetic is auxiliary JavaScript; scientific findings and self-screening are source-grounded agent reasoning. Sources and reusable assets are unchanged. No preference for another analysis is proposed.

## Method and full-scope result

All 90 displayed aspirin-minus-placebo difference intervals reproduce the stated Agresti–Caffo method, and all 87 visible point differences reproduce observed diagnostic proportions. Integer counts are exact. Allowing each printed 0.1-point estimate/endpoint its ±0.05 half-unit interval yields overlap for every calculation, so every discrepancy gap is zero. Three women’s eTable 5 PPV point cells visibly contain dashes; their embedded numerical tokens remain source-layer metadata rather than substituted printed estimates. No point lies outside its matched interval; every endpoint order and effect direction agrees after signed contrasts are matched. All six main P/CI pairs agree in significance at two-sided .05. Every overall predictive-value interval includes zero. Women’s subgroup PPV intervals excluding zero do not contradict the explicitly overall narrative.

The source defines Agresti–Caffo difference CIs and Agresti–Coull metric CIs. The difference interval uses adjusted proportions (x+1)/(n+2) and their binomial standard error; the displayed point difference uses unadjusted observed proportions. Their centers need not coincide. A complete 90-row calculation record is [stat1_calculation_record.md](../statistics/stat1_calculation_record.md). Null-exclusion/containment checks require no assumed P-value algorithm. Exact P-value equivalence beyond significance was not invented from convention.

Diagnostic checks, labeled as approximations: binomial-logit sex-interaction Wald calculations from the six Table 2 contrasts give P values 0.3013, 0.1128, 0.4931, 0.2862, 0.2580 and 0.0783; the rounded range .08–.49 and universal nonsignificance reproduce. Continuity-corrected normal planning approximation with 100 advanced cases per arm and sensitivities .36/.60 gives power90.90%, compatible with planned90% under display precision; 50 cases per sex/arm gives90.74% for .36/.70 but this is a diagnostic allocation assumption, not a supplied sex-count input. With900 disease-negative participants per arm and specificity .90, a normal95% CI is88.04%–91.96%, reproducing the printed88%–92%. No sample-size discrepancy is established. The paper's nonsignificant primary conclusion follows its intervals/P values; no noninferiority/equivalence conclusion or inferential interim decision is supplied. Eighteen site-effect P values .16–.50 are nonsignificant under the stated criterion, consistent with retaining the model without site random intercept.

## Findings

### F-ST1-001

**Title:** Primary outcome hierarchy differs across protocol clauses, SAP and report.

**Relationships:** S039, S101, S102, S109, S125, S126, S127, S205, S206, S213. Primary proposed relationship P_R; all relationships P_R, P_P. **Focus area:** D. **Proposed review domain:** protocol_report.

**Exact compared locations and roles:**

- PLAN [DOC-002 protocol PDF p11 §3.4](../../../joi190039supp1_prod.pdf#page=11), repeated [p22 §6.1](../../../joi190039supp1_prod.pdf#page=22): primary sensitivity at predefined positivity cutpoints of FOBGold; specificity and ROC AUC listed secondary.
- PLAN [DOC-002 protocol PDF pp13–14 §3.9](../../../joi190039supp1_prod.pdf#page=13): parenthetical primary endpoint includes sensitivity and specificity at predefined cutpoints and ROC AUC of FOBGold on day3.
- PLAN [DOC-002 protocol PDF p28 §§7.1–7.2](../../../joi190039supp1_prod.pdf#page=28): §7.1 primary is FOBGold sensitivity; primary endpoints confirmatory and others exploratory; §7.2 describes primary sensitivity, specificity and ROC AUC of two immunochemical FOBTs.
- PLAN [DOC-003 SAP PDF p6 §3.2](../../../joi190039supp2_prod.pdf#page=6): primary FOBGold sensitivity, while FD qualitative sensitivity, FOBGold AUC and specificities are secondary; [p8 §§5.4–5.5](../../../joi190039supp2_prod.pdf#page=8) retains this distinction. [p9 §7](../../../joi190039supp2_prod.pdf#page=9) changes primary population/missingness, without an explicit hierarchy amendment.
- REPORT [DOC-001 PDF p3 Outcomes/Statistical Analyses](../../../jama_brenner_2019_oi_190039.pdf#page=3): primary quantitative sensitivity at10.2/17 μg Hb/g; specificity and qualitative sensitivity secondary/exploratory; AUC described as secondary and explicitly not reported. [p4 Primary/Secondary End Points](../../../jama_brenner_2019_oi_190039.pdf#page=4) reports specificity differences -6.4 (95%CI -9.6 to -3.2), P<.001 and -3.1 (-5.4 to -0.8), P=.008 as secondary, and qualitative sensitivity12.7 (0.1 to24.7), P=.048 as secondary.

**Printed statements and logical rule/calculation:** The expanded protocol primary descriptions include specificity and AUC; §7.2 also expands assay coverage to two tests. Narrow clauses/SAP/report retain quantitative sensitivity as primary and move specificity, qualitative sensitivity and AUC into secondary status, with AUC absent from reported results. A metric expressly called primary in one supplied plan clause is secondary in other plan clauses and in the report. Therefore the prespecified status/confirmatory set does not reconcile. This is a categorical comparison; half-unit numeric intervals and relative discrepancy are not applicable.

**Qualifying route:** Route A, category 5.

**Affected result or extracted value:** Prespecified primary versus exploratory-secondary status of both quantitative specificity results, qualitative sensitivity, and AUC; interpretation/extraction of the qualitative sensitivity P=.048 and specificity P=.008/<.001 depends on the planned confirmatory set. AUC is explicitly unreported despite being included in the expanded primary clauses.

**Why context does not resolve it:** Route A category5 always registers a reproduced outcome-status change. The narrow clauses make one interpretation plausible, but neither the broadened primary parentheticals nor their confirmatory scope is removed by an explicit supplied hierarchy amendment.

**Alternatives and missing definition:** The broadened clauses may be carried-forward summary language while the detailed endpoint sections/SAP establish the intended narrow hierarchy. Alternatively, those clauses may reflect a broader original primary set later narrowed. No supplied statement identifies an effective hierarchy amendment or resolves precedence between these primary descriptions. This is not an adjudication of which clause governs.

**Exact human question:** Which prespecified hierarchy governed quantitative specificity, qualitative sensitivity and ROC AUC, and does a supplied amendment or clause-precedence statement explain the broadened protocol primary descriptions and the report's secondary/unreported status?

### F-ST1-002

**Title:** Protocol allows constipation-related sample postponement but excludes participants whose first stool sample is on day4.

**Relationships:** S114, S127. Primary proposed relationship P_P; all relationships P_P. **Focus area:** D. **Proposed review domain:** plan_material.

**Exact compared locations and roles:**

- PLAN [DOC-002 protocol PDF p18 §5](../../../joi190039supp1_prod.pdf#page=18): baseline can be skipped when unavailable; medication remains on day1; postdrug samples planned ondays3/4/5 can be postponed to subsequent days because of constipation or other reasons.
- PLAN [DOC-002 protocol PDF p21 Table1 footnote4](../../../joi190039supp1_prod.pdf#page=21): stool collection may be postponed to subsequent days for constipation or other reasons.
- PLAN [DOC-002 protocol PDF p28 §7.2](../../../joi190039supp1_prod.pdf#page=28): primary comparisons use day3 stools, and “patients who due to constipation give their first stool sample on day4 will be excluded from the study.”

**Printed statements and logical rule/calculation:** Medicationday1 and intended first postdrugday3 correspond to2 days after medication; postponedday4 corresponds to3 days after medication. In the scenario explicitly permitted by §5—no baseline, constipation preventing the day3 stool, first available stoolday4—the schedule clauses permit postponement, while §7.2 explicitly requires exclusion from the study. The supplied protocol supplies both collection permission and a whole-study exclusion for the same circumstance, without identifying which population receives the permission. This is an analysis-population decision-rule comparison, not a claim that a particular reported participant or denominator is affected. Half-unit arithmetic and relative discrepancy are not applicable to the categorical eligibility rule.

**Qualifying route:** Route B.

**Affected result or extracted value:** Definition/size of the planned primary FOBGold sensitivity analysis population for participants with delayed first collection. The report's primary day2 intention-to-screen estimate is the corresponding extraction target; aggregate results cannot establish the number, if any, of affected participants.

**Why context does not resolve it:** B1 is met by a plan-internal primary analysis-population rule. B2 is met because the text says excluded “from the study,” whereas the collection clauses explicitly permit postponement even when baseline is skipped; neither source location limits permission to participants in a specified secondary-only population. B3 is met because application of one rule retains a potentially eligible participant, while the other excludes that participant from the study/primary population. The actual affected count is not supplied and is not inferred.

**Alternatives and missing definition:** Exclusion may have been intended only for the strict day3/per-protocol primary analysis while postponed specimens remained available for secondary analyses; “first stool sample” may have meant first postdrug specimen rather than first specimen overall. The later SAP explicitly changes the primary population to intention-to-screen, which could supersede an earlier primary analysis restriction, but it does not explain the simultaneous operational permission/whole-study exclusion within protocolv1.5. These are alternative interpretations, not numerical proof of any report-versus-plan count discrepancy.

**Exact human question:** In protocolv1.5, were participants with no baseline and a constipation-delayed first stool onday4 retained in the study, excluded altogether, or retained only outside the primary analysis, and which supplied clause defines that decision?

## Excluded observations

Only apparent issues investigated and not emitted appear here; reconciling checks remain in the inventory.

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 p5 Tables2/3; DOC-003 p8 | Raw point differences are not exactly the midpoint of adjusted difference CIs; all90 intervals reproduce the stated Agresti–Caffo construction with adjusted center distinct from raw point. | NOT_REPRODUCED |
| DOC-001 p4 male specificity ranges; p5 Table2 | Positive magnitudes2.5/6.6 described as “lower” accompany signed difference CIs; matching signed contrasts -2.5/-6.6 reconciles containment and direction. | NOT_REPRODUCED |
| DOC-004 p7 eTable5, womenPPV three rows | Native-layer -18.2/-25.7/-21.6 tokens differ from visibly printed dash cells; no visible numerical point estimate exists to compare, and all three visible CIs reproduce. Derivative-versus-display disagreement is retained as metadata. | NOT_REPRODUCED |
| DOC-003 p8 §5.4 versus p9 §7 | Original per-protocol primary versus intention-to-screen primary is an explicitly disclosed change in the supplied plan. | CONTEXT_RESOLVES |
| DOC-003 p7 §4 versus p9 §7 | Exclusion versus inclusion of missing collection day is expressly superseded in Changes to the plan; missing/invalid test outcomes remain a distinct rule. | CONTEXT_RESOLVES |
| DOC-002 pp19/27 §6.11 versus p34 §8.8 | No-colonoscopy dropout cannot be reincluded, while delayed>3month patients returning with colonoscopy can be reincluded; different conditions explain the apparent population contradiction. | CONTEXT_RESOLVES |
| DOC-003 p8 repeated-participant model versus DOC-001 p3/DOC-004 p8 site model | The site model addresses a different clustering unit; no source says it replaced the planned participant model or produced a conflicting primary result. Absence of repeated-model output alone is insufficient. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 pp8–9 secondary/subgroup sections versus supplied report package | Individual-day/baseline contrasts, age/smoking/BMI/lesion strata and some secondary reciprocal-detection metrics are not reported; none is expressly key secondary or a conflicting reported analysis here. Primary-status AUC discrepancy is included above. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 p8 §5.5 reciprocal detection metrics | An Agresti–Coull label is specified for tests/colonoscopies per detected neoplasm, but no such interval/result is printed and transformation is unstated; no reproduced output conflicts. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 p5 Table3 all quantitative17 PPV | Rounded arms29.6−32.9 suggest -3.3 whereas difference is -3.2. Input half-unit difference interval[-3.40,-3.20] overlaps printed[-3.25,-3.15]; gap0, relative discrepancy0; exact counts give-3.2275. | ROUNDING_OR_DISPLAY_PRECISION |

## Complete relationship pass records

The canonical [relationship inventory](../statistics/relationship_inventory.md) carries full exact source scopes and outcomes. IDs are source-linked groups, not finding limits. The following explicit pass records cover every group.

| S ID | Pass 1 result | Status |
|---|---|---|
| S001 | 9.8[-3.1,22.2], P=.14; raw estimate, adjusted 95% endpoints and nonsignificance reconcile. | PASS_1_COMPLETE |
| S002 | -6.4[-9.6,-3.2], P<.001; lower specificity and significance reconcile. | PASS_1_COMPLETE |
| S003 | 6.0[-5.7,17.5], P=.32; raw estimate, adjusted endpoints and nonsignificance reconcile. | PASS_1_COMPLETE |
| S004 | -3.1[-5.4,-0.8], P=.008; lower specificity and significance reconcile. | PASS_1_COMPLETE |
| S005 | 12.7[0.1,24.7], P=.048; null exclusion and significance reconcile. | PASS_1_COMPLETE |
| S006 | -8.0[-11.0,-4.9], P<.001; lower specificity and significance reconcile. | PASS_1_COMPLETE |
| S007 | 15.1[-1.6,30.6]; counts reproduce point/CI, containment and direction agree; no row P supplied. | PASS_1_COMPLETE |
| S008 | -5.1[-10.0,-0.1]; counts reproduce point/CI, containment and direction agree; no row P supplied. | PASS_1_COMPLETE |
| S009 | 8.4[-7.5,23.3]; counts reproduce point/CI and narrative range endpoint. | PASS_1_COMPLETE |
| S010 | -2.5[-6.1,1.1]; counts reproduce point/CI; narrative decrease magnitude is distinct from signed interval. | PASS_1_COMPLETE |
| S011 | 17.6[1.3,32.6]; counts reproduce point/CI and narrative range endpoint. | PASS_1_COMPLETE |
| S012 | -6.6[-11.2,-2.0]; counts reproduce point/CI; lower-direction narrative agrees. | PASS_1_COMPLETE |
| S013 | 1.0[-19.1,21.4]; counts reproduce point/CI; near-zero comparison description agrees. | PASS_1_COMPLETE |
| S014 | -7.9[-12.0,-3.8]; counts reproduce point/CI; lower-direction description agrees. | PASS_1_COMPLETE |
| S015 | -0.8[-17.9,17.2]; counts reproduce point/CI, direction and containment. | PASS_1_COMPLETE |
| S016 | -3.7[-6.7,-0.8]; counts reproduce point/CI and lower direction. | PASS_1_COMPLETE |
| S017 | 1.1[-17.7,20.9]; counts reproduce point/CI and near-zero comparison description. | PASS_1_COMPLETE |
| S018 | -9.6[-13.5,-5.5]; counts reproduce point/CI and lower direction. | PASS_1_COMPLETE |
| S019 | -1.5[-10.7,7.4]; matched positive-test denominators reproduce point/CI; overall nonsignificance agrees. | PASS_1_COMPLETE |
| S020 | -0.1[-2.7,2.5]; matched negative-test denominators reproduce point/CI and overall nonsignificance. | PASS_1_COMPLETE |
| S021 | -3.2[-17.2,10.5]; matched counts reproduce point/CI, despite subtraction of rounded arm values suggesting -3.3. | PASS_1_COMPLETE |
| S022 | -0.3[-2.8,2.3]; matched counts reproduce point/CI; overall nonsignificance agrees. | PASS_1_COMPLETE |
| S023 | -3.8[-14.4,6.5]; matched counts reproduce point/CI and overall nonsignificance. | PASS_1_COMPLETE |
| S024 | 0.6[-2.1,3.3]; matched counts reproduce point/CI and overall nonsignificance. | PASS_1_COMPLETE |
| S025 | 8.8[-3.0,19.8]; matched counts reproduce point/CI and containment. | PASS_1_COMPLETE |
| S026 | -1.7[-5.9,2.4]; matched counts reproduce point/CI and containment. | PASS_1_COMPLETE |
| S027 | 7.8[-10.3,24.8]; matched counts reproduce point/CI and containment. | PASS_1_COMPLETE |
| S028 | -2.5[-6.4,1.4]; matched counts reproduce point/CI and containment. | PASS_1_COMPLETE |
| S029 | 7.5[-6.4,20.2]; counts from qualitative row reproduce; blank test label makes no numeric contradiction. | PASS_1_COMPLETE |
| S030 | -1.1[-5.3,3.0]; counts from qualitative row reproduce point/CI. | PASS_1_COMPLETE |
| S031 | -17.3[-31.8,-2.5]; counts reproduce point/CI; overall p4 statement refers all-participant rows. | PASS_1_COMPLETE |
| S032 | 1.6[-1.7,4.8]; counts reproduce point/CI and containment. | PASS_1_COMPLETE |
| S033 | -21.4[-42.2,0.8]; counts reproduce point/CI and containment. | PASS_1_COMPLETE |
| S034 | 1.9[-1.4,5.2]; counts reproduce point/CI and containment. | PASS_1_COMPLETE |
| S035 | -20.8[-37.8,-4.0]; counts reproduce point/CI; subgroup significance is not an overall contradiction. | PASS_1_COMPLETE |
| S036 | 2.3[-1.1,5.8]; counts reproduce point/CI and containment. | PASS_1_COMPLETE |
| S037 | 36%→60%, alpha.05,90% power; diagnostic continuity-corrected n100/case arm gives90.90%; no reproduced power discrepancy. | PASS_1_COMPLETE |
| S038 | Randomized-group analysis with stated eligibility and sample exclusions; scheduled versus actual day2 populations differentiated; amended SAP agrees. | PASS_1_COMPLETE |
| S039 | Main primary quantitative sensitivity versus secondary specificity/qualitative sensitivity/AUC matches narrow plan clauses but conflicts broader protocol clauses; F-ST1-001. | PASS_1_COMPLETE |
| S040 | Every displayed difference interval reproduces Agresti–Caffo; PPV/NPV method supported by SAP secondary specification. Raw differences and adjusted interval centers distinct. | PASS_1_COMPLETE |
| S041 | Six sex-binomial-logit Wald diagnostic P values0.0783–0.4931 reproduce rounded .08–.49 and all nonsignificance; no inference from sex-specific significance difference. | PASS_1_COMPLETE |
| S042 | Two-sided .05; no multiplicity adjustment, secondary exploratory. All six matched P/95%CI significance states agree; no supplied row SE/statistic. | PASS_1_COMPLETE |
| S043 | Site random intercept differs from participant repeated-measure intercept;18 site fits have nonsignificant P .16–.50; retaining no-site model follows stated decision. | PASS_1_COMPLETE |
| S044 | All sensitivity/specificity range endpoints match appropriate signed contrasts; decrease magnitudes with signed CIs do not reverse direction. | PASS_1_COMPLETE |
| S045 | Men quantitative10.2 23.2[5.0,39.5] and qualitative22.5[4.5,38.6] match eTable4; counts reproduce both. | PASS_1_COMPLETE |
| S046 | All12 overall intention-to-screen/per-protocol predictive-value CIs include zero; subgroup null exclusions do not conflict overall wording. | PASS_1_COMPLETE |
| S047 | Combining up to3 samples increases sensitivity and decreases specificity in both arms in all matched rows; source does not infer improvement from sensitivity alone. | PASS_1_COMPLETE |
| S048 | Both primary quantitative sensitivity CIs include zero, P=.14/.32; no significant increase statement is compatible and does not assert equivalence. | PASS_1_COMPLETE |
| S049 | Advanced cases224→214 and analyzed population2134→valid quantitative2042 imply4.46%/4.31% reductions; approximately4% permits both, no conflicting printed denominator. | PASS_1_COMPLETE |
| S100 | Abbreviations distinguish AUC/ROC/ITT and safety categories; no quantitative identity conflict. | PASS_1_COMPLETE |
| S101 | Narrow primary quantitative sensitivity wording contrasts expanded §3.9/7.2; F-ST1-001. | PASS_1_COMPLETE |
| S102 | Specificity/AUC listed secondary but called primary elsewhere; consolidated hierarchy finding F-ST1-001. | PASS_1_COMPLETE |
| S103 | Single300mg non-enteric ASA versus placebo matches main and SAP intervention; future lower-dose discussion is distinct. | PASS_1_COMPLETE |
| S104 | Two named assays, quantitative versus qualitative measurements and laboratory assignment match report; no identity conflict. | PASS_1_COMPLETE |
| S105 | Participant randomization, blinding and center blocks are coherent; report block20 provides detail absent plan without contradiction. | PASS_1_COMPLETE |
| S106 | Eligibility age40–80, screening/diagnostic, prior colorectal history and antithrombotic exclusions match available-case report boundaries. | PASS_1_COMPLETE |
| S107 | Original medicationday1, first postdrugday3 maps explicitly to reportday2 via SAP footnote; colonoscopy≥4 full free days unchanged. | PASS_1_COMPLETE |
| S108 | Sex, multiday and safety objectives appear in report; optional biomarkers do not create primary-result omission. | PASS_1_COMPLETE |
| S109 | Available endpoint+colonoscopy population is coherent; primary endpoint parenthesis broadens status to specificity/AUC: F-ST1-001. | PASS_1_COMPLETE |
| S110 | Sex-stratified diagnostic outcomes reported, interaction binomial GLM prespecified in SAP; no unplanned-primary model claim. | PASS_1_COMPLETE |
| S111 | Repeated-day combined performance reported in eTable3; aggregate combination has one binary outcome per participant, distinct from repeated model. | PASS_1_COMPLETE |
| S112 | Safety all-randomized population planned; report AE counts contain no conflicting denominator, missing explicit denominator alone not finding. | PASS_1_COMPLETE |
| S113 | Preceding observational ASA results are distinct design/exposure; not matched to randomized single-dose estimates. | PASS_1_COMPLETE |
| S114 | Optional baseline, postponed collection and two-sample permission conflict explicit exclusion for firstday4 collection: F-ST1-002. | PASS_1_COMPLETE |
| S115 | Delayed-colonoscopy sensitivity analysis specified, but report gives no delay counts/results; no reproduced primary-count conflict established. | PASS_1_COMPLETE |
| S116 | No-colonoscopy dropout versus returning>3month reinclusion concern different conditions; not a reproduced population contradiction. | PASS_1_COMPLETE |
| S117 | AE recordingday1–5 and follow-up contact≤3weeks are distinct windows; report event listing supplies no incompatible timing. | PASS_1_COMPLETE |
| S118 | Blinded extraction, two reviewers and emergency participant unblinding coherent; no printed data-method conflict. | PASS_1_COMPLETE |
| S119 | Medication and collection-date documentation supports actual-dayper-protocol; no dose-compliance model claimed. | PASS_1_COMPLETE |
| S120 | Optional future biomarkers excluded from current efficacy; no mandatory primary/key secondary biomarker model supplied. | PASS_1_COMPLETE |
| S121 | Recruitment/safety operational stop criteria; no reported stopping decision contradicts rule, no inferential efficacy interim boundary. | PASS_1_COMPLETE |
| S122 | Withdrawn consent/dropout/nonreused numbers consistent with reported exclusions; no forced imputation assumed. | PASS_1_COMPLETE |
| S123 | Diagnostic95%CIs and colonoscopy gold standard; more precise CI algorithm supplied SAP/report; >90% phrase describes usual threshold context. | PASS_1_COMPLETE |
| S124 | Randomized-arm primary quantitative sensitivity comparison matches observed estimates; no plan covariate/model specification conflicts. | PASS_1_COMPLETE |
| S125 | AUC/ROC and lesion stratification status compared; broader primaryAUC versus secondary/unreported AUC joins F-ST1-001; no assumed composite shift. | PASS_1_COMPLETE |
| S126 | Confirmatory primary/exploratory secondary distinction bears on hierarchy F-ST1-001; no supplied multiplicity or NI rule contradicted. | PASS_1_COMPLETE |
| S127 | Expanded sensitivity/specificity/AUC of2tests hierarchy F-ST1-001; firstday4 exclusion versus constipation permission F-ST1-002. | PASS_1_COMPLETE |
| S128 | 10% of1000 gives100 advanced cases per arm; continuity-corrected normal diagnostic90.90% power for.36→.60; sex inputs incomplete, n50 diagnostic90.74%, no numeric conflict. | PASS_1_COMPLETE |
| S129 | 900 nondiseased/arm at90% specificity gives normal95%CI88.04–91.96%, matching printed88–92; method approximation labeled diagnostic. | PASS_1_COMPLETE |
| S130 | AE/SAE/SUSAR definitions differentiate counts and causality; reported hospitalizations categorized SAE, no incompatible result. | PASS_1_COMPLETE |
| S131 | Only supplied version1.5 and SAP changes available; do not invent an amendment or attribute misconduct from absent version history. | PASS_1_COMPLETE |
| S132 | Screening failures have no randomization number; main flow only randomization onwards, assessed-eligibility count not collected explicitly. | PASS_1_COMPLETE |
| S133 | Missing records pursued operationally; no stated imputation conflicts with report available diagnostic data. | PASS_1_COMPLETE |
| S200 | Objectives consistent assays/intervention; primary hierarchy narrower than expanded protocol: F-ST1-001 through primary specification S205. | PASS_1_COMPLETE |
| S201 | Explicit medicationday0 renumbering resolves originalday3 versus reportday2; collection flexibility matches protocol §5. | PASS_1_COMPLETE |
| S202 | Colonoscopy timing and dropout definitions coherent; delayed-colonoscopy sensitivity output unavailable with no demonstrated conflicting value. | PASS_1_COMPLETE |
| S203 | Full eligibility population versus per-protocol exactday2 distinguished; first-valid duplicate rule permits fewer participant outcomes than sample counts. | PASS_1_COMPLETE |
| S204 | Valid sample before colonoscopy or timing unavailable defines intention-to-screen; main and eTable2 footnote compatible. | PASS_1_COMPLETE |
| S205 | Primary quantitative sensitivity and CRC/advanced adenoma composite match report; secondary status differs broader protocol: F-ST1-001. | PASS_1_COMPLETE |
| S206 | Qualitative positivity categories and secondary diagnostic hierarchy match report; no composite change from listing serrated categories. | PASS_1_COMPLETE |
| S207 | Missing/invalid test excluded; missing collection day rule explicitly superseded insection7; no internal unresolved amendment contradiction. | PASS_1_COMPLETE |
| S208 | Flow/descriptive tabulation reported; baseline testing absence supplies no primary/key-secondary inferential contradiction. | PASS_1_COMPLETE |
| S209 | All20 eTable2 rows retain sample timing/counts; pooled duplicate actualday2 samples not interchangeable with participant denominators. | PASS_1_COMPLETE |
| S210 | Per-protocol original primary changed explicitly to intention-to-screen; Agresti–Caffo method and two-sided.05 match report. | PASS_1_COMPLETE |
| S211 | Se/Sp/PPV/NPV conditioning and numerator definitions reproduce all reported cells; reciprocal detection-count metrics not reported. | PASS_1_COMPLETE |
| S212 | All72 single-day performance interval cells reproduce stated adjusted binomial method; no secondary significant/non-significant decision conflict. | PASS_1_COMPLETE |
| S213 | ROC/AUC designatedsecondary/unreported in SAP/main but primary in broader protocol; status pattern F-ST1-001; no ROC estimates supplied. | PASS_1_COMPLETE |
| S214 | Participant repeated-measure model differs site model, neither labeled as replacement; absence of repeated-model output alone does not establish a changed primary model. | PASS_1_COMPLETE |
| S215 | Combined-day and safety analyses reported; individual-day/baseline contrast outputs absent, no primary/key-secondary result contradiction from absence alone. | PASS_1_COMPLETE |
| S216 | Sex interaction specification matches diagnostics; age/smoking/BMI/lesion strata unreported, not explicitly primary/key or called reported. | PASS_1_COMPLETE |
| S217 | Explicit primary ITS and missing-date changes match report; Fisher missing-outcome decision result/algorithm unprinted, no reproduced conflicting output. | PASS_1_COMPLETE |
| S218 | Every TP/FN/TN/FP-derived Se/Sp difference and95%CI reproduces; intervals ordered, contain points; combined-day gain/loss directions match main. | PASS_1_COMPLETE |
| S219 | Every day2per-protocol Se/Sp difference and95%CI reproduces; male narrative matching complete; exact-day population kept distinct. | PASS_1_COMPLETE |
| S220 | All18 CIs and15 visible differences reproduce from eTable4;3 womenPPV point cells visiblydash, embedded tokens not substituted; overall nonsignificance agrees. | PASS_1_COMPLETE |
| S221 | All18 P=.16–.50 nonsignificant; no estimate CI/SE/statistic to invert; near-zero SD/.50 supports boundary-null behavior without inferring unstated reference law. | PASS_1_COMPLETE |

## Derivative provenance

All fresh derivatives below are inside review_1_6_2; engines Poppler26.01.0, CPU; no OCR/fallback/Python extraction was used.

- Native/layout: `pdftotext -layout -f3 -l6 jama_brenner_2019_oi_190039.pdf preprocessing/stat1-main-p3-6.txt` (actual command uses separated -f/-l arguments); protocol pp13–14,18–21,28–29 and singlep11/p22 similarly target `stat1-protocol-p13-14.txt`, `stat1-protocol-p18-21.txt`, `stat1-protocol-p28-29.txt`, `stat1-protocol-p11.txt`, `stat1-protocol-p22.txt`. Full SAP layout targets `preprocessing/stat1-SAP.txt`.
- Direct visual confirmations: `pdftoppm -f28 -l28 -singlefile -scale-to1800 -png joi190039supp1_prod.pdf preprocessing/stat1-protocol-p28`; corresponding protocolp11/p13/p21 use scale1600; p18 scale1700; SAPp6 scale1600. Actual commands use separated numeric flags and package-local review_1_6_2/preprocessing paths. All six rendered pages were viewed; primary hierarchy and postpone/exclusion text visually confirmed.
- Reusable main sourcep3 image `.ai_paper_validation/document_outputs/D01/ocr_pages/page-3.png` was viewed to confirm main hierarchy, methods and reported population. Source-authoritative fresh native text confirms mainp4/5 numeric correspondence. The support mapper’s source-confirmed eTable5 visible-versus-text-layer distinction was retained; numerical interval checks used its displayed values without replacing the three dash cells.
- Direct supplement confirmation: `pdftotext -layout -f 5 -l 8 joi190039supp3_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/stat1-supp-p5-8.txt`; all eTable3/4/5/6 cells reread against direct source text. Existing current-run direct Poppler render `preprocessing/support-other-DOC004-p7.png` was independently viewed to confirm the three women’s visible PPV dash cells.

Artifact output only; independent inclusion screening remains mandatory. No candidate ID, evidence state, final correction, severity or adjudication is assigned by this pass.

