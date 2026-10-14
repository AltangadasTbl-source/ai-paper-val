# Mechanical source recheck — protocol/report candidates

Fresh evidence rechecker `/root/recheck_protocol`, gpt-6.1-sol/high. Assigned stable IDs: C001, C002, C003, C004, C005, C006, C007. Every affected location in these seven cards was found and visually read from a source-matched page image. The current ledger, initial screening record and bounded protocol screen supplied locators; neither their conclusions nor OCR are final authority. QUALITY_CONTROL_SCOPE.md and the complete review contract were read. No earlier-run candidate record, external material or participant data was used. All candidates remain Pending Human Adjudication.

## C001 — Added diabetes-range HbA1c primary-composite disqualifier

**Location found and source/comparator matched:** Yes, at every registered location:

| Exact supplied location | Role by content | Directly matched fact |
|---|---|---|
| [DOC-002 p6, synopsis endpoint](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=6) | PLAN | Success is any of ≥5% weight loss, ≥4% loss with ≥150 minutes/week, or ≥0.2 percentage-point A1c reduction; no follow-up diabetes-range disqualifier appears in this definition. |
| [DOC-002 p15, §3.2](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=15) | PLAN | The three-branch disjunction is repeated, with binary success if at least one branch is met; incident A1c ≥6.5% is listed separately among secondary endpoints. |
| [DOC-002 p86, incident-diabetes SAP-change row](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=86) | PLAN | The original method did not prespecify incident diabetes as grounds for primary failure. The revised method assigns primary failure to diabetes-range A1c ≥6.5% at six or twelve months regardless of weight/PA improvement; clinical rationale is printed. |
| [DOC-001 p3, Outcomes](../../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=3) | REPORT | Primary outcome requires HbA1c <6.5% throughout plus one or more listed branches. |
| [DOC-001 p4, Primary Analysis](../../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4) | REPORT | This maintained-HbA1c composite is achieved by 58/183 versus 59/185; RD −0.2 percentage points and one-sided 95% lower limit −8.2 are printed. |
| [DOC-003 p29, eTable13 method opening](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=29) | REPORT | The table identifies participants with diabetes-range A1c during six- and/or twelve-month visits in the primary cohort. |
| [DOC-003 p30, continued eTable13 method](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=30) | REPORT | These participants were marked as failing the endpoint regardless of weight/PA improvements. Formal diabetes diagnosis was not adjudicated and requires two confirmatory tests. |
| [DOC-003 p56, eTable13 and note](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=56) | REPORT | Fifteen participant rows, seven human-DPP and eight AI-DPP, contain at least one follow-up A1c ≥6.5%; the nonadjudication note is repeated. |

**Consistency rule applicable:** Yes. Route A, category 5 concerns a changed primary-composite definition. Let W denote either weight/PA branch, H the HbA1c-reduction branch and D a diabetes-range follow-up measurement. The original definition is W OR H; the reported definition additionally requires NOT D. The change is expressly identified in the supplied PLAN, so it is more than absence of an unreported detail. Disclosure does not turn it into a claim of a protocol violation.

**Logical comparison reproduced and display precision:** Yes. The additional condition is exact and does not depend on rounding; no half-unit interval discrepancy is alleged. The 15 listed measurements corroborate application context, not the size of any change in achiever counts. A participant with D and an otherwise successful W/H branch would be classified differently, but the package does not give that cross-classification.

**Necessary inputs available:** Yes for the printed definition comparison and the reported result. **Exact missing inputs or definitions:** The dated approval/adoption of this SAP change; original-branch success among the 15 listed participants; primary results under the original definition. These are unavailable for quantifying a result change.

**Source-grounded alternative interpretation:** The disclosed revised definition is the intended governing composite; the SAP provides its clinical rationale and expressly distinguishes diabetes-range measurements from an adjudicated diagnosis. This alternative is retained in the evidence record.

**Direct observation versus inferred explanation:** Direct observation is the added disqualifier and its explicit original/change contrast. Its adoption timing, the reason a particular participant's endpoint changed and any numerical effect on the primary estimate are not observed and are not inferred.

**Classification confirmation:** PLAN DOC-002 pp.6,15,86 vs REPORT DOC-001 pp.3-4 and DOC-003 pp.29-30,56. Primary relationship **P_R**; all relationships **P_R**; review domain **protocol_report**. These exactly match the ledger. The REPORT locations agree with one another and the revised plan; no independent S_C/S_W conflict is added. Original versus amended PLAN versions are the disclosed history of the same change, not an independently alleged unresolved P_P issue. No classification correction is needed.

**Evidence state:** reproduced. Determining fact: both original and revised primary-composite conditions are present at the exact supplied locations, and their logical difference persists when read directly.

**Exact remaining human question:** Which dated original or amended composite definition governed the reported 58/183 versus 59/185 result, and what primary results correspond to the original definition?

## C002 — Primary PA averaging window

**Location found and source/comparator matched:** Yes, at every registered location:

| Exact supplied location | Role by content | Directly matched fact |
|---|---|---|
| [DOC-002 p6, synopsis PA branch](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=6) | PLAN | The ≥4% weight-loss/≥150-minutes-weekly branch uses serial monthly actigraphy during months 6–11. |
| [DOC-002 p15, §3.2](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=15) | PLAN | Average PA over months 6–11 explicitly belongs to the primary weight-plus-PA branch. |
| [DOC-002 p80, version1.4 amendment opening](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=80) | PLAN | Version 1.4 is dated 03-28-2022 and says the primary endpoint was modified to clarify the PA measurement timeframe; exact replacement start/end months are not printed. |
| [DOC-002 p81, amendment continuation](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=81) | PLAN | The continued primary modification addresses the HbA1c subset and expanded eligibility; it supplies no replacement PA start/end months. |
| [DOC-001 p3, Outcomes](../../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=3) | REPORT | The primary branch requires ≥4% loss with at least 150 weekly MVPA minutes; the averaging months are not stated in this sentence. |
| [DOC-001 p7, Figure2 PA component](../../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=7) | REPORT | The branch is achieved by 23/183 versus 23/185, with RD 0.1 and lower one-sided 95% limit −5.5 percentage points. |
| [DOC-003 p13, aggregation paragraph](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=13) | REPORT | Average weekly MVPA throughout twelve-month follow-up sums all valid wear periods and divides by available wear periods, maximum eleven postbaseline visits. |
| [DOC-003 p49, eTable8b](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=49) | REPORT | Postbaseline monthly PA assessments are listed for months 1–11, with zero assignment to nonwear periods. |

**Consistency rule applicable:** Yes for the exact original primary window and reported aggregation description, under Route A, category 5. The endpoint-specific mapping remains the named human question. The comparison must retain that the report's aggregation paragraph does not explicitly say its all-postbaseline window is the input to the binary primary branch.

**Logical comparison reproduced and display precision:** Yes, the printed windows differ: original months 6–11 are six designated periods, while all postbaseline periods through month 11 can include eleven. This is an exact window comparison, so half-unit numeric intervals do not apply. No claim is made that the actual primary achievement counts were produced using eleven periods or would differ under six periods. The 23/183 and 23/185 cells are matched as the affected extracted component, not as evidence of participant reclassification.

**Necessary inputs available:** Yes for the printed window comparison, amendment disclosure and component result. **Exact missing inputs or definitions:** The complete amended primary endpoint's PA start/end months; explicit mapping from p13's aggregation to the binary primary branch; participant-level monthly PA and resulting classifications. Without these, a numerical primary-result effect cannot be reproduced.

**Source-grounded alternative interpretation:** The all-postbaseline formula may govern only the continuous PA summary, while a separate months6–11 calculation governs the primary component; alternatively, the approved 03-28-2022 amendment may govern a broader primary window. Both interpretations fit the supplied statements, and neither final mapping is printed.

**Direct observation versus inferred explanation:** Direct observations are the original months6–11 primary rule, the dated acknowledgement of a timeframe modification and the all-postbaseline averaging description. Applying the latter to the binary primary endpoint is an unresolved inference, not a directly established production fact.

**Classification confirmation:** PLAN DOC-002 pp.6,15,80-81 vs REPORT DOC-001 pp.3,7 and DOC-003 pp.13,49. Primary relationship **P_R**; all relationships **P_R**; review domain **protocol_report**, exactly matching the ledger. PLAN and REPORT contents are correctly assigned. No separate S_C/S_W contradiction is demonstrated between the mutually compatible report statements. No independent unresolved P_P issue is added. Classification ambiguity is the endpoint-specific mapping and supplied amendment disclosure, not the document roles. No classification correction is needed.

**Evidence state:** reproduced. Determining fact: the original primary window and the different reported aggregation window are directly present, with the primary-input mapping explicitly unresolved. This state records the printed comparison; it does not resolve which implementation generated the binary endpoint.

**Exact remaining human question:** Which months entered the ≥4%-weight-loss/150-minutes-weekly primary component, and what exact dated amended specification establishes that window, as distinct from the continuous PA summary?

## C003 — Primary HbA1c branch restricted to baseline subset

**Location found and source/comparator matched:** Yes, at every registered location:

| Exact supplied location | Role by content | Directly matched fact |
|---|---|---|
| [DOC-002 p15, §3.2 original branch](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=15) | PLAN | Original primary definition includes ≥0.2 percentage-point A1c reduction at twelve months without a separate baseline-subset qualifier in the endpoint definition. |
| [DOC-002 p80, version1.4 opening](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=80) | PLAN | Amendment dated 03-28-2022 explicitly modifies the primary endpoint and begins the A1c-change limitation. |
| [DOC-002 p81, continuation](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=81) | PLAN | The baseline 5.7%–6.4% subset restriction is explicit, as is broadened inclusion based on fasting glucose or oral glucose tolerance evidence of prediabetes. The rationale aligns eligibility with CDC entry criteria and reduces screen failure. |
| [DOC-001 p3, Outcomes](../../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=3) | REPORT | Change in the HbA1c endpoint applies only to participants with baseline HbA1c 5.7%–6.4%. |
| [DOC-001 p7, Figure2 HbA1c row and footnote c](../../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=7) | REPORT | Each arm has 35/130 (26.9%) successes, RD 0 and lower one-sided 95% limit −9.1; footnote restricts the population to prediabetes-range baseline HbA1c, N=130 each. Other component denominators are 183/185. |

**Consistency rule applicable:** Yes. Route A, category 5 covers a changed primary-composite branch definition. The amendment expressly changes the branch's eligible subset, and the report follows that subset. The reported denominator is therefore not itself a count inconsistency.

**Logical comparison reproduced and display precision:** Yes. The original unrestricted endpoint wording and dated subset qualification are matched; 130+130=260 versus 183+185=368 describes the stated populations without asserting they should be equal. As a coherent supporting check, 100×35/130=26.9231%, within the displayed 26.9% half-unit interval [26.85,26.95]%; hence no percentage discrepancy is alleged. Display precision cannot resolve the exact eligibility-rule change.

**Necessary inputs available:** Yes for the original rule, amendment, implemented subset and component counts. **Exact missing inputs or definitions:** The complete final consolidated amended composite specification and any participant-level original-versus-amended classifications. The original eligibility relied on prediabetes-range HbA1c, so the endpoint qualifier may preserve the same HbA1c branch for originally eligible people while accommodating newly eligible people; no effect magnitude is inferred.

**Source-grounded alternative interpretation:** This is the intended prospective amendment accompanying expanded prediabetes eligibility. Its date and rationale are supplied. The report agrees with that amended specification; the candidate records the definition history required for extraction under the mandated category5 rule.

**Direct observation versus inferred explanation:** Direct observations are the expressly modified branch definition, broadened eligibility and report's 130/130 denominators. Practical changes to endpoint membership for particular participants, or whether the change alters the final primary conclusion, are not established.

**Classification confirmation:** PLAN DOC-002 pp.15,80-81 vs REPORT DOC-001 pp.3,7. Primary relationship **P_R**; all relationships **P_R**; review domain **protocol_report**, exactly as in the ledger. The amendment is PLAN by prospective content. No independent unresolved P_P inconsistency is inferred between documented versions, and the report's results and footnote agree. No classification correction is needed.

**Evidence state:** reproduced. Determining fact: the supplied dated amendment explicitly restricts the primary HbA1c branch, and the report directly implements that restriction relative to the original endpoint wording.

**Exact remaining human question:** Which final amended composite definition should accompany extraction of the baseline-subset HbA1c branch and the expanded eligible trial population?

## C004 — Primary exclusions replaced by all-randomized failure assignment

**Location found and source/comparator matched:** Yes, at every registered location:

| Exact supplied location | Role by content | Directly matched fact |
|---|---|---|
| [DOC-002 p37, §9.3](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=37) | PLAN | The plan calls the approach ITT and includes participants according to initial randomization irrespective of adherence, but expressly excludes withdrawal from the study or consent from effectiveness analyses. |
| [DOC-002 p86, first SAP-change row](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=86) | PLAN | Original method excludes withdrawal or lacking twelve-month data; changed method includes all randomized participants and classifies missing twelve-month data as primary failures. Conservative-effectiveness and preservation-of-randomization rationale is stated. |
| [DOC-001 p4, primary methods/results](../../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4) | REPORT | All randomized participants enter ITT; absent twelve-month visits are nonachievers. Randomized N=368, complete data N=313; primary counts are 58/183 and 59/185. |
| [DOC-001 p5, Figure1](../../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=5) | REPORT | Primary populations remain 183/185 despite 26/29 missed visits. The missed-visit boxes include 19/19 study withdrawals and 7/10 lost contacts, distinguishing withdrawal from all missing visits. |
| [DOC-003 p27, primary cohort definition](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=27) | REPORT | The primary cohort is all randomized participants. |
| [DOC-003 p50, eTable8c and rationale](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=50) | REPORT | Missing twelve-month A1c/body-weight counts are 26 (14.2%) and 29 (15.7%), assumed failure in primary analysis and handled by MICE sensitivity. No outcome missingness occurs among study completers. |

**Consistency rule applicable:** Yes. Route A, category 5 applies to replacing the primary population exclusion/failure rules. Original ITT terminology does not erase its express exclusion clause or the supplied change-table comparator.

**Calculation/logical comparison reproduced and display precision:** Yes. 183+185=368; 26+29=55; 183−26=157; 185−29=156; 157+156=313; 313+55=368. Thus the reported counts reconcile while the operations governing included participants differ. Withdrawal total 19+19=38 is not the missing-visit total 55. The source establishes no equation that the original analysis denominator was 313. The supporting percentages 26/183=14.2077% and 29/185=15.6757% fall in printed intervals [14.15,14.25]% and [15.65,15.75]%; the gap is zero. Numeric precision does not apply to the exact inclusion/failure rule change.

**Necessary inputs available:** Yes for the explicit original/change comparison and all reported population totals. **Exact missing inputs or definitions:** The date of the primary-population SAP change, individual consent-withdrawal status and the original planned denominator/results. Study withdrawal, consent withdrawal and absence of a visit cannot be silently equated.

**Source-grounded alternative interpretation:** The all-randomized population with missing outcomes assigned failure is the intended conservative revised specification, explicitly justified in the source. The original plan's broad ITT language provides context, while its effectiveness exclusion remains an actual printed qualifier.

**Direct observation versus inferred explanation:** Direct observations are exclusion versus inclusion/failure operations and coherent reported totals. The size of the original primary population or the corresponding alternate primary estimate is not supplied and is not reconstructed from complete visits.

**Classification confirmation:** PLAN DOC-002 pp.37,86 vs REPORT DOC-001 pp.4-5 and DOC-003 pp.27,50. Primary relationship **P_R**; all relationships **P_R**; review domain **protocol_report**, exactly matching the ledger. Main and results REPORT material agree, and the revision history is disclosed rather than an independently alleged unresolved P_P issue. No classification correction is needed.

**Evidence state:** reproduced. Determining fact: the original exclusion clause and its explicitly disclosed replacement by all-randomized failure assignment are directly matched in the supplied source.

**Exact remaining human question:** Which dated population specification governed the primary 58/183 versus 59/185 estimate, including the treatment of study withdrawal, consent withdrawal and missing twelve-month visits?

## C005 — Clustered logistic primary model replaced by binomial RD regression

**Location found and source/comparator matched:** Yes, at every registered location:

| Exact supplied location | Role by content | Directly matched fact |
|---|---|---|
| [DOC-002 p37, §9.4.1](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=37) | PLAN | Between-group primary/secondary differences use mixed-effects logistic regression to account for potential within-program-site clustering. |
| [DOC-002 p38, §9.4.7](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=38) | PLAN | Primary efficacy analysis uses logistic regression with treatment group as the primary exposure; covariate-adjusted models are described separately. |
| [DOC-002 p86, model-change row](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=86) | PLAN | The original mixed-effects logistic analysis is replaced by unadjusted binomial regression to estimate RD directly; the rationale is stated. |
| [DOC-001 p4, primary and sensitivity methods](../../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4) | REPORT | Primary RD is estimated with binomial regression; cluster-robust standard errors occur in post hoc sensitivity analyses. Primary RD/lower limit are −0.2/−8.2 percentage points. |
| [DOC-003 p31, eTables19a/19b methods](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=31) | REPORT | Site-based robust inference uses four human-DPP clusters plus one AI cluster; a second analysis uses DPP-site/calendar-month cluster IDs. |
| [DOC-003 p62, eTables19a/19b](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=62) | REPORT | Same primary counts 58/183 and 59/185; site-robust RD −0.20 with lower limit −4.8, and site/month-robust RD −0.20 with lower limit −6.8. |

**Consistency rule applicable:** Yes. Route A, category 5 concerns replacement of the planned primary statistical model and clustering implementation. It does not require selecting a preferred model, inferring an unprinted link function or questioning an internally coherent binomial choice.

**Logical comparison reproduced and display precision:** Yes. Mixed-effects logistic primary analysis and unadjusted binomial RD regression are expressly different model specifications. Separate cluster-robust sensitivity estimates are not the planned mixed-effects primary fit. −0.2 and −0.20 are overlapping precision representations, not a discrepancy. Lower limits −8.2, −4.8 and −6.8 belong to explicitly different analyses, so no interval-versus-result conflict or rounding comparison is asserted.

**Necessary inputs available:** Yes for model identity, primary/sensitivity distinction and reported outputs. **Exact missing inputs or definitions:** The dated approval of the primary model replacement and output from the originally specified mixed-effects primary analysis. Raw cluster data are absent, and no mixed-effects interval is recomputed.

**Source-grounded alternative interpretation:** The binomial primary model is the intended revision because it directly estimates RD. Its rationale is supplied; robust sensitivities assess related clustering assumptions without claiming to be the original mixed-effects fit.

**Direct observation versus inferred explanation:** The model replacement is direct. Its effect on a hypothetical original-model result, its approval timing or the production code underlying either model is not observed and is not inferred.

**Classification confirmation:** PLAN DOC-002 pp.37-38,86 vs REPORT DOC-001 p.4 and DOC-003 pp.31,62. Primary relationship **P_R**; all relationships **P_R**; review domain **protocol_report**, matching the ledger. REPORT statements describe compatible distinct analyses. Disclosed changed PLAN versions do not add an independently unresolved P_P issue. No classification correction is needed.

**Evidence state:** reproduced. Determining fact: the source change row expressly replaces the original model, and the REPORT primary/sensitivity descriptions match that replacement.

**Exact remaining human question:** Which dated primary-model specification governed the published RD, and where is the originally specified mixed-effects primary analysis reported, if available?

## C006 — Primary PA missing-data procedure and complete-case sensitivity replaced

**Location found and source/comparator matched:** Yes, at every registered location:

| Exact supplied location | Role by content | Directly matched fact |
|---|---|---|
| [DOC-002 p38, §9.4.2](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=38) | PLAN | If >5% of PA data are missing, primary analysis is based on multiple imputation, with complete-case sensitivity requiring participants with 100% PA data. |
| [DOC-002 p39, §9.4.8 continuation](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=39) | PLAN | The same MI trigger and sensitivity requiring 100% valid PA data are repeated; primary analysis is interpreted in light of the sensitivity if results differ significantly. |
| [DOC-002 p86, PA-missingness change row](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=86) | PLAN | Instead of planned MI, a worst-case assumption assigns zero minutes to missing actigraphy intervals; a conservative-activity rationale is printed. |
| [DOC-001 p4, sensitivities](../../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4) | REPORT | Post hoc sensitivities include MICE for missing twelve-month outcomes, alternate PA assumptions and MNAR pattern-mixture assumptions. |
| [DOC-003 p13, PA processing/compliance](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=13) | REPORT | Invalid accelerometry days have zero MVPA; noncompliant assigned weeks have zero PA. |
| [DOC-003 p30, eTables16–18 methods](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=30) | REPORT | MICE imputes missing twelve-month outcomes using twenty datasets; MNAR concerns missed twelve-month outcomes; PA sensitivities assign 150 minutes/week to noncompliant participants or everyone. |
| [DOC-003 p49, eTable8b and rationale](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=49) | REPORT | Missing monthly PA is assigned zero. Postbaseline displayed missingness ranges from 9.3% to 35.1%; the conservative rationale and alternate routes to primary success are stated. |
| [DOC-003 p59, eTable16](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=59) | REPORT | The sensitivity explicitly concerns missing twelve-month outcomes using MICE, with pooled risks 32.2/31.9 and RD −1.1/lower −11.5. Their numerical relationship is outside this assigned candidate and is rechecked under C013. |
| [DOC-003 p60, eTable17](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=60) | REPORT | Pattern-mixture sensitivity assigns 0% success to AI noncompleters and 37.8% to human noncompleters; the printed result is 58/183 versus 70/185, RD −6.1/lower −14.3. |
| [DOC-003 p61, eTables18a/18b and notes](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=61) | REPORT | One sensitivity grants 150 minutes/week to actigraphy-noncompliant participants; the other grants it to everyone. They do not restrict membership to participants with 100% valid PA. The fresh full-page source render was used; the upper display is visibly clipped in the supplied page itself, but both qualifying assumptions are readable. |

**Consistency rule applicable:** Yes. Route A, category 5 concerns the replacement of the original primary monthly-PA missing-data procedure and its linked complete-case sensitivity. Monthly PA missingness and missing twelve-month endpoints are different quantities; analyses imputing the latter do not establish execution of the original former procedure.

**Logical comparison reproduced and display precision:** Yes. The explicit PLAN change states MI was replaced by zero assignment. The reported alternate PA sensitivities change assumed attainment, whereas the original complete-case sensitivity selects a fully observed PA population. This comparison is exact; half-unit intervals do not reconcile different imputands or membership rules. The 9.3%–35.1% monthly percentages support relevance but are not summed or transformed into an unstated aggregate missingness fraction. No numerical inconsistency among the displayed sensitivity estimates is alleged here.

**Necessary inputs available:** Yes for the original procedure, explicit replacement, primary zero assignment and definitions of reported sensitivities. **Exact missing inputs or definitions:** Dated adoption of the replacement; original monthly-PA MI results; results of the planned 100%-valid-PA complete-case analysis; the precise aggregate missingness quantity used to evaluate the >5% trigger. The explicit replacement establishes the comparison without inventing the latter quantity.

**Source-grounded alternative interpretation:** Zero assignment is the intended conservative revised primary method, as stated in the SAP change and report rationale. The available supportive analyses explore different assumptions or missing quantities. They should not be silently treated as the original complete-case analysis.

**Direct observation versus inferred explanation:** Direct observation is the printed linked procedure replacement and the different stated sensitivity operations. The number of participants whose primary success changed, the effect of original MI, or the result from an unavailable original complete-case analysis is not observed or inferred.

**Classification confirmation:** PLAN DOC-002 pp.38-39,86 vs REPORT DOC-001 p.4 and DOC-003 pp.13,30,49,59-61. Primary relationship **P_R**; all relationships **P_R**; review domain **protocol_report**, matching the ledger. Source p30's descriptions and the sensitivity displays are REPORT by their executed-results content. The separate report-internal PA stream and averaging questions belong to other assigned candidates and do not add S_W here. No independent P_P contradiction is inferred from the disclosed revision. No classification correction is needed.

**Evidence state:** reproduced. Determining fact: the supplied source explicitly replaces planned MI with zero assignment, while the reported supportive procedures do not state execution of the original fully observed PA sensitivity.

**Exact remaining human question:** When did zero assignment supersede the planned monthly-PA MI and linked 100%-valid-PA complete-case specification, and are those originally specified primary and sensitivity results available?

## C007 — Program-completer primary analysis replaced by complete-data/no-medication cohort

**Location found and source/comparator matched:** Yes, at every registered location:

| Exact supplied location | Role by content | Directly matched fact |
|---|---|---|
| [DOC-002 p16, §3.3 completion](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=16) | PLAN | Human completers attend ≥8 sessions in months1–6 with ≥9 months from first cohort session to last attendance; AI completers engage ≥8 weeks in months1–6 with ≥9 months from installation to last engagement. |
| [DOC-002 p37, §9.3](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=37) | PLAN | A per-protocol effectiveness analysis uses program completers as defined in §3.3 to benchmark outcomes against CDC standards. |
| [DOC-002 p86, PP-change row opening](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=86) | PLAN | The original PP population is program completers; the revised population begins with available twelve-month outcomes. |
| [DOC-002 p87, PP-change continuation](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=87) | PLAN | Revised eligibility excludes initiation of prohibited medications. The rationale refers to adherence and complete follow-up and calls the estimate supportive under those conditions. |
| [DOC-001 p4, restricted method/results](../../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4) | REPORT | Restricted analysis requires twelve-month outcome data and no prohibited medications; 313 complete participants minus 13 medication initiators leaves 300. |
| [DOC-001 p9, Figure4](../../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=9) | REPORT | Program-completer columns contain 117 AI and 93 human participants, with 43 and 33 achievers. Descriptive engagement/outcome counts are supplied without the originally planned program-completer primary inferential model/interval. |
| [DOC-003 p27, cohort definition](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=27) | REPORT | Per-protocol cohort includes all randomized participants completing the twelve-month visit without prohibited steroids, antihyperglycemics or weight-loss medications; program engagement is not a stated membership requirement. |
| [DOC-003 p58, eTable15 and note](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=58) | REPORT | Restricted primary result is 54/151 (35.8%) versus 53/149 (35.6%), RD 0.2/lower −8.9. The note calls the cohort supportive complete data without pharmacologic confounding and does not estimate a causal effect of adherence. |

**Consistency rule applicable:** Yes. Route A, category 5 concerns replacement of a planned supportive primary inferential population. Different labels are not the issue: the explicit membership rules and cohorts differ. Descriptive successes among completers are not equivalent to reporting the originally planned model/interval.

**Calculation/logical comparison reproduced and display precision:** Yes. Program completers total 117+93=210; restricted cohort totals 151+149=300; 313−13=300. Every member of the 300-person cohort cannot belong to a 210-person program-completer set, regardless of their overlap. Success proportions 54/151=35.7616% and 53/149=35.5705% lie in printed intervals [35.75,35.85]% and [35.55,35.65]%; those numeric gaps are zero. Exact membership-rule substitution, rather than percentage discrepancy, is the registered issue.

**Necessary inputs available:** Yes for both membership definitions, their aggregate counts and the restricted result. **Exact missing inputs or definitions:** Dated adoption of the revised supportive primary cohort; overlap between program completers and the restricted cohort; original program-completer inferential output and associated interval. The narrative rationale's adherence language does not establish an additional unprinted engagement requirement.

**Source-grounded alternative interpretation:** The reported restricted cohort is the intended amended supportive population; main article and supplement consistently identify its operative criteria. The supplied noncausal caveat and revision rationale are preserved. This does not establish availability of the original program-completer inferential result.

**Direct observation versus inferred explanation:** Direct observations are program engagement versus complete-data/no-medication membership, unequal cohort totals and descriptive completer success cells. Their participant-level overlap, the original inferential estimate and any causal adherence effect are not inferred.

**Classification confirmation:** PLAN DOC-002 pp.16,37,86-87 vs REPORT DOC-001 pp.4,9 and DOC-003 pp.27,58. Primary relationship **P_R**; all relationships **P_R**; review domain **protocol_report**, exactly matching the ledger. REPORT materials agree about different populations; the supplied revision history is not an independently unresolved P_P inconsistency. No classification correction is needed.

**Evidence state:** reproduced. Determining fact: the explicitly planned program-completer population and the revised/report restricted population have different operative rules and totals, and only descriptive program-completer outcomes are located among the cited displays.

**Exact remaining human question:** When was the complete-data/no-prohibited-medication supportive primary population adopted, and where is the originally planned program-completer inferential result, if available?

## Classification facts for coordinator handoff

| ID | Compared document roles | Relationship type | All relationships | Review domain | Evidence state | Classification change |
|---|---|---|---|---|---|---|
| C001 | PLAN DOC-002 pp.6,15,86 vs REPORT DOC-001 pp.3-4 and DOC-003 pp.29-30,56 | P_R | P_R | protocol_report | reproduced | None |
| C002 | PLAN DOC-002 pp.6,15,80-81 vs REPORT DOC-001 pp.3,7 and DOC-003 pp.13,49 | P_R | P_R | protocol_report | reproduced | None; endpoint-specific PA mapping remains explicit |
| C003 | PLAN DOC-002 pp.15,80-81 vs REPORT DOC-001 pp.3,7 | P_R | P_R | protocol_report | reproduced | None |
| C004 | PLAN DOC-002 pp.37,86 vs REPORT DOC-001 pp.4-5 and DOC-003 pp.27,50 | P_R | P_R | protocol_report | reproduced | None |
| C005 | PLAN DOC-002 pp.37-38,86 vs REPORT DOC-001 p.4 and DOC-003 pp.31,62 | P_R | P_R | protocol_report | reproduced | None |
| C006 | PLAN DOC-002 pp.38-39,86 vs REPORT DOC-001 p.4 and DOC-003 pp.13,30,49,59-61 | P_R | P_R | protocol_report | reproduced | None |
| C007 | PLAN DOC-002 pp.16,37,86-87 vs REPORT DOC-001 pp.4,9 and DOC-003 pp.27,58 | P_R | P_R | protocol_report | reproduced | None |

Precedence P_R > P_P > S_C > S_W was applied to every ID. All seven involve the PLAN-versus-REPORT comparison. REPORT corroboration does not add a report-report relationship, and disclosed PLAN revisions are not separately alleged unresolved plan-internal issues. No transcription or page-location correction was needed. Evidence state is a mechanical fact, not a human disposition or inclusion-audit decision.

## Inspected source pages and engine record

Twenty-eight unique supplied PDF pages were visually inspected, covering every cited location: DOC-001 pp.3,4,5,7,9; DOC-002 pp.6,15,16,37,38,39,80,81,86,87; DOC-003 pp.13,27,29,30,31,49,50,56,58,59,60,61,62. No new render, OCR, package installation or source/reused-asset modification was needed.

Current-run image paths below are relative to review_1_6_2/preprocessing/. Producer records identify PyMuPDF 1.28.0 through the supplied pdf_tools.py, 200 dpi, CPU rendering. The user's approved GPU_USER_REQUESTED setting concerns RapidOCR CUDA; no OCR was run by this rechecker.

| Source scope | Images directly viewed | Engine/provenance |
|---|---|---|
| DOC-001 pp.3,4,9 | cross-main-3.png; cross-main-4.png; cross-main-9.png | Current source-matched PyMuPDF CPU render |
| DOC-002 pp.6,15,16,37,38,39,80,81,86,87 | cross-plan-6.png; cross-plan-15.png; cross-plan-16.png; cross-plan-37.png; cross-plan-38.png; cross-plan-39.png; cross-plan-80.png; cross-plan-81.png; cross-plan-86.png; cross-plan-87.png | Current source-matched PyMuPDF CPU render |
| DOC-003 pp.13,27,49,56,58 | cross-results-13.png; cross-results-27.png; cross-results-49.png; cross-results-56.png; cross-results-58.png | Current source-matched PyMuPDF CPU render |
| DOC-003 pp.29,30,31,59 | st1-report-p29.png; screen-results-30.png; screen-results-31.png; st1-report-p59.png | Current source-matched PyMuPDF CPU render |
| DOC-003 p61 | screen-repair-protocol-results-61.png | Current source-matched PyMuPDF CPU render; source's upper display clipping remains visible, qualifying PA assumptions readable |
| DOC-001 pp.5,7 | Historical document_outputs/DOC-001-main-article/page_images/page-005.png and page-007.png | Reusable source-page images; historical rendering engine unspecified |
| DOC-003 pp.50,60,62 | Historical document_outputs/DOC-003-results-supplement/page_images/page-050.png, page-060.png and page-062.png | Reusable source-page images; historical rendering engine unspecified |

Completion counts: seven assigned stable IDs, seven separately completed cards, twenty-eight unique source pages, seven reproduced evidence states, zero classification corrections, zero source-coverage gaps. Remaining questions are named amendment chronology, endpoint-specific mapping and unavailable original inferential outputs; no participant-level numerical effect is asserted.
