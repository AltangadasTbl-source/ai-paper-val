# Mechanical evidence recheck — Workflow 1.6.2

Pending Human Adjudication

This fresh recheck covers C001, C002, C003, C004 and C005 separately. Source-page images are the authority for printed facts; current maps and raw extraction are locators and delimit searches for an absent counterpart. Every link below names the physical PDF page. No source or reused asset was changed, and no additional OCR or raster was produced by this agent. Classification is by the compared content: the protocol/SAP bundle is PLAN, the article and results supplement are REPORT.

## C001 — Missing stratification-only primary-outcome analysis

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN final protocol vs REPORT main article

**Evidence state:** reproduced

**Finding IDs:** F-XS-001, F-ST1-002

**Locations found and source/comparator matched:**

| Exact location | Role | Directly confirmed content |
|---|---|---|
| [Original protocol p30, §4.2.2](../../../joi250042supp1_prod_1753377747.92525.pdf#page=30) | PLAN | Primary outcome analyzed both with stratification variables only and with additional baseline covariates; the fuller model is primary. |
| [Final protocol p70, §4.2.2](../../../joi250042supp1_prod_1753377747.92525.pdf#page=70) | PLAN | Same two-analysis statement remains in v1.8, dated 14 October 2024; analyses will be lodged in a SAP before unblinding. |
| [Article p3, Statistical Analysis](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=3) | REPORT | Models include site/diagnostic subgroup and age, SpO2, PaO2:FiO2, COVID-19 and date; binary outcomes use logistic regression. |
| [Article p6, Primary and Secondary Outcomes](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=6) | REPORT | Adjusted RD 0.7 percentage points (95% CI −0.7 to 2.0), P=.28, contrasted with an expressly unadjusted RD 0.5 (−1.0 to 2.0). |
| [Article p8, Table 2 and footnotes a/b](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8) | REPORT | Available-case RD 0.7 (−0.6 to 2.1) and imputed RD 0.7 (−0.7 to 2.0); both use the fuller covariate set. Neither is a stratification-only result. |
| [Final SAP p126, §5.3.1](../../../joi250042supp1_prod_1753377747.92525.pdf#page=126) and [p127 continuation](../../../joi250042supp1_prod_1753377747.92525.pdf#page=127) | PLAN, alternative context | Fully adjusted primary regression and marginal RD/RR/OR are specified. Diagnostic-subgroup interactions on p127 are a different analysis from a stratification-only companion model. |
| [SAP change summary p136](../../../joi250042supp1_prod_1753377747.92525.pdf#page=136) | PLAN, alternative context | Lists additions and expansions for v1.1; no explicit removal of the companion model is identified. |

**Consistency rule and reproduced comparison:** Covariate-set membership defines the analysis. A crude/unadjusted contrast is not the regression adjusted only for site and diagnostic strata; available-case versus multiply-imputed data does not change the extra covariate set. The complete current article/results maps and raw-text counterpart search cover article pp1–11 and results supplement pp1–29; they identify no separately labeled stratification-only primary-outcome treatment effect. This absence is confined to the supplied reports. The rule is Route A category 5, a planned primary-outcome analysis without a reported counterpart. Display-precision intervals are inapplicable to model membership and counterpart absence; no numerical discrepancy is inferred from the adjusted and crude estimates.

**Necessary inputs and exact missing inputs:** The printed protocol specification, report model labels and reported estimates are available. The companion model's estimate/interval, its implemented code, and an explicit cancellation or replacement instruction are not supplied. A companion value cannot be calculated from the fuller model or crude counts.

**Source-grounded alternative and classification ambiguity:** The detailed final SAP may intentionally supersede the shorter protocol statement; the final protocol directs analyses to a SAP. The final SAP matches the implemented full model. It does not expressly say that the retained protocol companion analysis is removed. This possible supersession is retained as a human question. No independent PLAN-versus-PLAN inconsistency is claimed here: SAP content corroborates the reported full model and provides context. P_R and protocol_report are confirmed without correction.

**Direct observation versus inferred explanation:** Direct observations are the retained two-analysis sentence and the labeled report models/results. Intentional supersession and an unsupplied companion result are possible explanations, not observed facts. The recheck fact determining **reproduced** is that the printed retained companion specification has no identified counterpart in the complete supplied REPORT scope.

**Exact remaining human question:** Was the stratification-only primary-outcome companion analysis retained, where is its treatment effect reported, or where was its replacement documented?

## C002 — Retained protocol stay test versus SAP/report stay method

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, P_P

**Compared document roles:** PLAN final protocol vs PLAN final SAP and REPORT main article

**Evidence state:** reproduced

**Finding IDs:** F-XS-004, F-ST1-004

**Locations found and source/comparator matched:**

| Exact location | Role | Directly confirmed content |
|---|---|---|
| [Original protocol p30, §4.2.2](../../../joi250042supp1_prod_1753377747.92525.pdf#page=30) | PLAN | ICU/acute-hospital duration comparisons use Wilcoxon rank-sum tests stratified by survival status. |
| [Final protocol p70, §4.2.2](../../../joi250042supp1_prod_1753377747.92525.pdf#page=70) and [p71 continuation](../../../joi250042supp1_prod_1753377747.92525.pdf#page=71) | PLAN | The same Wilcoxon specification begins at the bottom of p70 and continues with survival-status stratification at the top of p71. |
| [Original SAP p104, §5.3.2](../../../joi250042supp1_prod_1753377747.92525.pdf#page=104) | PLAN | Duration among survivors uses proportional-hazards regression with Fine and Gray to account for competing death. |
| [Final SAP p128, §5.3.4](../../../joi250042supp1_prod_1753377747.92525.pdf#page=128) | PLAN | Retains the Fine and Gray competing-risk duration model. |
| [Article p3, Statistical Analysis](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=3) | REPORT | Explicit Fine–Gray subdistribution hazards regression for ICU/hospital stay with death competing. |
| [Article p8, Table 2 and abbreviations/footnotes](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8) | REPORT | ICU sHR 1.00 (0.96 to 1.04), P=.97; hospital sHR 0.98 (0.94 to 1.02), P=.27; sHR explicitly defined as Fine–Gray with competing death. |
| [SAP change summary p136](../../../joi250042supp1_prod_1753377747.92525.pdf#page=136) | PLAN, alternative context | Later SAP additions/expansions are listed; no express Wilcoxon replacement statement is listed. |

**Consistency rule and reproduced comparison:** A survival-stratified rank-sum test and a competing-risk regression are distinct specified procedures. The final protocol retains one, while both SAP versions and the report specify the other. The article/results current maps and raw locators identify no separate Wilcoxon stay result in the supplied REPORT scope. Route B concerns the status of the retained prospective stay comparison attached to the named sHR analyses. No interval/P conflict or preferred method is asserted. Display precision is inapplicable to test/model identity; the printed sHRs are context and are not being recomputed.

**Necessary inputs and exact missing inputs:** Both model/test specifications and the report's model identity are available. An explicit instruction saying replacement versus addition, any retained Wilcoxon statistic/P value, and the implemented analysis code are absent. The missing rank-sum test cannot be recovered from the printed medians/IQRs.

**Source-grounded alternative and classification ambiguity:** The later detailed SAP may supersede protocol shorthand, as the final protocol directs analyses to a SAP; alternatively both comparisons may have been intended. Neither printed specification explicitly identifies that relationship. The protocol/report comparison supplies P_R, and the retained protocol versus final SAP supplies P_P. The SAP/report agreement adds no separate relationship. Precedence selects P_R, therefore protocol_report; registration is confirmed without correction.

**Direct observation versus inferred explanation:** Directly observed are the different printed retained procedures and the clearly labeled report sHRs. Replacement, addition or historical carryover are explanations requiring human confirmation. **Reproduced** is determined by the retained final protocol Wilcoxon statement versus final SAP/report Fine–Gray statement.

**Exact remaining human question:** Did the final SAP replace the protocol Wilcoxon stay comparisons, or were both retained, and where is that relationship and any retained result documented?

## C003 — SAP all-outcome MICE versus reported selected predictors and stay censoring

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R, S_C

**Compared document roles:** PLAN final SAP vs REPORT main article and REPORT results supplement

**Evidence state:** reproduced

**Finding IDs:** F-XS-003, F-ST1-003

**Locations found and source/comparator matched:**

| Exact location | Role | Directly confirmed content |
|---|---|---|
| [Final SAP p131, §7 start](../../../joi250042supp1_prod_1753377747.92525.pdf#page=131) | PLAN | Hourly treatment-delivery carry-forward/logical imputation is separate and does not affect outcome analysis; the primary-outcome missingness paragraph begins here. |
| [Final SAP p132, §7 continuation](../../../joi250042supp1_prod_1753377747.92525.pdf#page=132) | PLAN | Secondary outcomes expected unavailable after refused/withdrawn consent; each MICE model includes all adjusted-model baseline variables and all outcome variables. Twenty datasets/Rubin rules are specified, with explicit computational alternatives of five datasets/1000 bootstrap replications or imputed OR only. |
| [Article p3, imputation paragraph](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=3) | REPORT | Chained-equations imputation incorporates at least the primary outcome as an auxiliary variable to support secondary-outcome imputation. |
| [Article p8, Table 2 and footnote b](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8) | REPORT | Multiply-imputed column includes the binary/ordinal outcome models; ICU/hospital durations are explicitly excepted and missing times are censored. One-year available-case RD 1.0 (−0.7 to 2.6), imputed RD 3.3 (−0.7 to 7.3). |
| [Results supplement p24, eTable 7, complete outcome rows and footnote a](../../../joi250042supp2_prod_1753377747.93025.pdf#page=24) | REPORT | Exact imputation-model/auxiliary assignments transcribed in the next table; footnote a separately lists allocated treatment and adjusted baseline predictors included in all models. |
| [Results supplement p24, duration rows and footnote e](../../../joi250042supp2_prod_1753377747.93025.pdf#page=24) | REPORT | Missing ICU/hospital durations: 1653 (10.1%)/1677 (10.2%); model Censoring, auxiliaries N/A. The hour/day cutoff distinction is independently rechecked under C004. |
| [SAP change summary p136](../../../joi250042supp1_prod_1753377747.92525.pdf#page=136) | PLAN, alternative context | Final SAP explicitly expanded missing-data handling; no predictor-selection or missing-duration exception is described here. |

Every outcome row of eTable 7 was reread directly, not reconstructed from OCR:

| Outcome | Printed imputation model | Printed auxiliary variables |
|---|---|---|
| 90-day mortality | Logit | Duration of acute hospital stay |
| ICU duration | Censoring | N/A |
| Acute-hospital duration | Censoring | N/A |
| Days alive and free from organ support at 30 days | Ordered logit | 90-day mortality; mortality at ICU discharge |
| Mortality at ICU discharge | Logit | 90-day mortality |
| Mortality at acute-hospital discharge | Logit | 90-day mortality; duration of acute hospital stay |
| 60-day mortality | Logit | 90-day mortality; one-year mortality |
| One-year mortality | Logit | None |

**Consistency rule and reproduced comparison:** The SAP's all-outcome predictor membership differs from the selected auxiliary sets/None explicitly printed in the results supplement, and its broad MICE procedure differs from the report's explicit duration exception. The baseline-predictor footnote does not list the absent outcome variables. Main p3's at-least-primary-outcome auxiliary description also differs from the one-year auxiliary None entry; the one-year row has 1661 (12.7%) missing among 13052 reaching one year, and the article supplies an imputed one-year estimate. This is one repeated missing-data specification pattern, not a new issue per row. Display-precision intervals do not apply to predictor-set membership or imputation-versus-censoring. Distinct labeled available-case and imputed RDs are not treated as conflicting copies, and no effect-change calculation is claimed.

**Necessary inputs and exact missing inputs:** Printed model memberships, procedure exceptions, missing counts and named results are available. The implemented MICE predictor matrices, whether outcomes entered elsewhere than the auxiliary column, handling of unavailable stay times within any predictor matrix, any implementation amendment, and the extent to which the main sentence applies to every secondary model are absent. These inputs are necessary to identify the implemented specification, not to reproduce the printed difference. The source p132 bootstrap alternative is 1000, already correctly registered; the earlier map transcription of 100 was corrected before registration and does not change this candidate's evidence state.

**Source-grounded alternative and classification ambiguity:** The SAP might have intended a general framework refined during implementation or imputation of discrete outcomes only. The eTable auxiliary list could omit other outcome predictors included through a separate mechanism, but neither its None entry nor its baseline-only footnote states that mechanism. Main p3 could describe auxiliary incorporation across the imputation exercise rather than require it in every outcome-specific model. This narrows how firmly the report/report comparison can be interpreted, but does not supply an explicit exception to its at-least-primary statement for the printed one-year None row. P_R is confirmed for final SAP versus report; S_C is retained for the main auxiliary statement versus results-supplement one-year specification, with this explicit ambiguity. P_R precedence therefore selects protocol_report. No S_W is added: main p8 identifies its duration exception rather than giving a second conflicting predictor definition. No classification correction is required.

**Direct observation versus inferred explanation:** Direct observations are all-outcome MICE in the final SAP, selected/None auxiliaries and Censoring in eTable 7, the main auxiliary description and duration exception. Refinement, an unprinted predictor mechanism or a nonuniversal reading of main p3 are possible explanations. Numerical effects of these implementation choices are not observable from the supplied evidence. **Reproduced** is determined by the explicit printed membership/procedure difference, including all affected outcome rows, rather than an assumption about analysis code.

**Exact remaining human question:** Which outcome predictors entered each implemented imputation model, does the one-year model incorporate the primary outcome despite its None auxiliary entry, and where were the selected predictors and early-censoring duration exception reconciled with final SAP §7?

## C004 — Hospital missing-duration censoring at one hour versus one day

**Review domain:** statistical_results

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT main article vs REPORT results supplement

**Evidence state:** reproduced

**Finding IDs:** F-XS-002, F-ST1-001

**Locations found and source/comparator matched:** The REPORT [article p8, Table 2 acute-hospital stay row and footnote b](../../../jama_martin_2025_oi_250042_1753377747.91025.pdf#page=8) gives hospital sHR 0.98 (95% CI 0.94 to 1.02), P=.27, and includes both ICU and acute-hospital missing discharge times as censored 1 hour after randomization. The REPORT [results supplement p24, eTable 7 acute-hospital row and footnote e](../../../joi250042supp2_prod_1753377747.93025.pdf#page=24) lists 1677 (10.2%) missing hospital durations and specifies 1 hour for ICU duration but 1 day for acute-hospital duration. The entire footnote was reread, confirming the two outcome-specific time assignments. Both locations are results/methods REPORT content, not prospective PLAN content.

**Consistency rule, calculation and display precision:** For the same missing acute-hospital durations, 1 day equals 24 hours, while the main cutoff is 1 hour; the operational difference is 23 hours. Even treating these specified times conservatively as rounded integers gives main [0.5,1.5] hours versus supplement [0.5,1.5] days = [12,36] hours. The intervals do not overlap: gap = 12−1.5 = 10.5 hours; relative discrepancy against the main printed 1 hour = 10.5/1 = 10.5, above 0.05. Thus rounding cannot reconcile the quantity-changing time specification. The identical displayed sHRs do not determine which cutoff was implemented. No sHR or P-value recalculation, change in significance or change in effect magnitude is inferred.

**Necessary inputs and exact missing inputs:** Both printed time definitions, outcome attribution, missing count and named sHR are available. The actual censoring timestamps and analysis code are not supplied; they are needed to choose the implemented cutoff. No participant-level data are needed to reproduce the printed specification conflict.

**Source-grounded alternative and classification ambiguity:** The main footnote might generalize the ICU cutoff to both outcomes, or the supplement might describe a different hospital implementation. Neither identifies a distinct analysis to which its cutoff applies. Calendar-day hospital measurement does not establish equality of the printed hour/day cutoffs. Only REPORT-versus-REPORT content conflicts, so S_C and statistical_results are confirmed. SAP material associated with C003 is not an additional relationship in this candidate.

**Direct observation versus inferred explanation:** The one-hour versus one-day statements are direct observations. A generalized main footnote or a differing supplemental description is an inferred explanation. **Reproduced** is determined by the two nonoverlapping specified hospital times, including the half-unit interval comparison.

**Exact remaining human question:** Were the missing acute-hospital discharge durations censored at 1 hour or 1 day after randomization in the reported model?

## C005 — Pilot adherence numerator and progression direction

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN original SAP vs PLAN final SAP and PLAN final protocol

**Evidence state:** reproduced

**Finding IDs:** F-NUM-001

**Locations found and source/comparator matched:**

| Exact location | Role | Directly confirmed content |
|---|---|---|
| [Original SAP p95, Table 1 and footnote](../../../joi250042supp1_prod_1753377747.92525.pdf#page=95) | PLAN | Treatment adherence: Green ≥75% cases, Amber 50–75%, Red <50%. The progression footnote defines the percentage using conservative-group patients with one or more adjudicated protocol deviations. |
| [Original SAP p98, §3.2.2 continuation](../../../joi250042supp1_prod_1753377747.92525.pdf#page=98) | PLAN | Patient-level adherence is defined as not having experienced any protocol deviation, immediately after a sentence about reporting patients with at least one deviation. |
| [Final SAP p118, Table 1 and footnote](../../../joi250042supp1_prod_1753377747.92525.pdf#page=118) | PLAN | Retains the same adherence thresholds and explicit one-or-more-deviation numerator. |
| [Final protocol p69, Table 2 and adherence footnote](../../../joi250042supp1_prod_1753377747.92525.pdf#page=69) | PLAN | Same adherence thresholds; adherence defined as adjustments to ventilator settings or supplemental oxygen as per protocol. |
| [Final protocol p70, §4.2.1](../../../joi250042supp1_prod_1753377747.92525.pdf#page=70) | PLAN | All-green progression unchanged, any-amber amendment, any-red stop; final funder decision after TSC recommendation. |
| [Original SAP p96, pilot continuation](../../../joi250042supp1_prod_1753377747.92525.pdf#page=96) and [final SAP p119, pilot continuation](../../../joi250042supp1_prod_1753377747.92525.pdf#page=119) | PLAN | Same green/amber/red decision consequences and final NIHR/TSC decision process. |

**Consistency rule and reproduced calculation:** For the same conservative-group population and adjudicated binary event, d = fraction with at least one deviation and a = fraction with none, hence a=1−d. The SAP footnote's Green d≥0.75 implies a≤0.25, while Green applied to adherence a≥0.75 implies d≤0.25. Its Red d<0.50 implies a>0.50. An illustrative a=0.80, d=0.20 gives Green using the adherence definition but Red using the footnote numerator. These are algebraic demonstrations, not observed pilot fractions or actual decisions. The explicit membership contrast determines the discrepancy; no assumption about observed trial adherence is needed.

**Display-precision check:** The traffic-light cutoffs are decision thresholds and the discrepancy is opposite event membership, not a count/percentage that fails rounding. Half-unit rounding of an observed percentage cannot make having a deviation and having none the same event. Even a sensitivity allowing 75% to represent [74.5%,75.5%] maps the deviation-based Green boundary to an adherence boundary in [24.5%,25.5%], separated by at least 49 percentage points from the adherence-based Green boundary; this illustrative boundary comparison remains far beyond a 0.05 relative gap (49/75≈0.653). It does not reinterpret the specified thresholds as actually rounded or infer an observed pilot color. Exact equality conventions at 50%/75% are a separate matter and are not this candidate.

**Necessary inputs and exact missing inputs:** The progression numerator definition, the no-deviation adherence definition, the common treatment-group scope and decision thresholds/consequences are supplied. The actual pilot denominator, adjudicated deviation count, applied progression fraction/color and decision record are absent. Those inputs are necessary to reconstruct an actual decision; the registered candidate concerns the printed rule only.

**Source-grounded alternative and classification ambiguity:** The at-least-one-deviation percentage might have been intended for separate nonadherence reporting while the progression rule used its complement. Alternatively the footnote might identify the applied statistic, leaving the direction of the thresholds to be clarified. The explicit patient-level no-deviation definition supports the former possibility without identifying which statistic was actually used. All conflicting comparisons are within prospective PLAN material. The final protocol adherence definition corroborates the no-deviation side and is not an extra relationship type. P_P and plan_material are confirmed without correction.

**Direct observation versus inferred explanation:** Direct observations are the deviation numerator in both SAP versions, the no-deviation patient-level definition and the unchanged prospective traffic-light consequences. A complementary intended numerator or the actual applied pilot rule is inferred and remains unestablished. **Reproduced** is determined by the opposite event membership used under the same high-is-Green adherence thresholds.

**Exact remaining human question:** Was the progression fraction based on no adjudicated deviation or at least one deviation, and which numerator was used for the color thresholds?

## Recheck completion and bounded limitations

All five stable IDs and all nine included finding provenance IDs are retained. Every cited affected location, including repetitions in original/final plan versions and contextual change summaries, was found and visually read. No registration transcription or location was changed. Evidence state is reproduced for each ID. No document-role, relationship or domain correction is required; C003 retains P_R, S_C with the explicit auxiliary-sentence ambiguity recorded above.

| ID | Recheck coverage | Evidence state | Classification action |
|---|---|---|---|
| C001 | Complete | reproduced | Retain protocol_report; P_R; all P_R |
| C002 | Complete | reproduced | Retain protocol_report; P_R; all P_R, P_P |
| C003 | Complete | reproduced | Retain protocol_report; P_R; all P_R, S_C; preserve stated ambiguity |
| C004 | Complete | reproduced | Retain statistical_results; S_C; all S_C |
| C005 | Complete | reproduced | Retain plan_material; P_P; all P_P |

Image authority used: reusable main pp3,6,8 and results p24 from the curator-listed document_outputs page renders; reusable PLAN p30 from review_1_5_1/preprocessing/doc002_b and p126 from review_1_5_1/preprocessing/stat_pass1; current PLAN pp69,70,71,95,96,98,104,118,119,127,128,131,132,136 from review_1_6_2/preprocessing/doc002. Their source identities and unchanged reusable hashes are tracked in the source/evidence inventories. Existing REPORT rasters are 200 dpi; current PLAN rasters are pinned PyMuPDF 1.26.4 CPU renders at 170 dpi, as recorded in tooling_record.md. This agent needed no new extraction or OCR; GPU OCR text remained only a locator.

Limits concern implementation, not unread source evidence: no analysis code, explicit replacement instruction for C001/C002, outcome-specific predictor matrices for C003, actual hospital censor timestamps for C004 or pilot statistic/decision record for C005 is supplied. No actual effect change, pilot decision reversal or paper-level conclusion impact is inferred. Every candidate remains Pending Human Adjudication.
