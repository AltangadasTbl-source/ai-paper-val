# Mechanical evidence recheck — Workflow 1.6.2

Pending Human Adjudication. Runtime ID: 01a129c8-65ac-77a3-bd94-7df0e00a6fb0; model gpt-6.1-sol; reasoning effort high; start mode FRESH_SPAWN. Assigned and completed scope: C001–C013, every retained source/comparator location, all three C008 occurrences, and both C013 arms. The complete current ledger, initial screening log, scope, review contract, report specification, relevant canonical checker findings and new source maps were read. No older scientific conclusion or external source was used. Evidence states below are mechanical record facts; every ID remains Pending Human Adjudication.

Authority is the supplied PDF page as visually inspected in a current-source CPU render. Text and maps supplied locators; no text derivative alone determined a candidate's evidence state. PDF links are relative to this artifact. Main article DOC-001 and results tables DOC-004 are REPORT because they report this trial's results; protocol DOC-002 and prospective SAP DOC-003 are PLAN because their content specifies proposed conduct/analysis. No role depends on a supplement filename. Printed input intervals use half a unit of the last displayed place. Designated significance thresholds are fixed decision rules. Diagnostic assumptions are identified explicitly rather than substituted for the producing analysis.

## Recheck classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state |
|---|---|---|---|---|---|
| C001 | statistical_results | S_C | S_C, S_W | REPORT main Key Points vs REPORT main primary copies and REPORT results original/VAS24 copies | reproduced |
| C002 | statistical_results | S_W | S_W | REPORT main Methods vs REPORT main Discussion | reproduced |
| C003 | protocol_report | P_R | P_R | PLAN protocol VAS definition vs REPORT main VAS definition | reproduced |
| C004 | statistical_results | S_W | S_W | REPORT main ICOAP raw ranges vs REPORT main question-count/scoring definition | reproduced |
| C005 | protocol_report | P_R | P_R | PLAN protocol adopted power inputs vs REPORT main power inputs | reproduced |
| C006 | protocol_report | P_R | P_R | PLAN protocol/SAP primary model vs REPORT main producing model | reproduced |
| C007 | protocol_report | P_R | P_R | PLAN protocol/SAP per-protocol analysis vs REPORT main/results efficacy material | reproduced |
| C008 | statistical_results | S_W | S_W | REPORT main within-display modeled contrasts and REPORT results within-display modeled contrasts | reproduced |
| C009 | statistical_results | S_C | S_C | REPORT main safety counts vs REPORT results safety counts | reproduced |
| C010 | statistical_results | S_C | S_C | REPORT main SAE relatedness summary vs REPORT results SAE classifications | reproduced |
| C011 | plan_material | P_P | P_P | PLAN protocol power inputs vs PLAN protocol claimed power/statistical specification | reproduced |
| C012 | statistical_results | S_W | S_W | REPORT results glucose12 and REPORT main/results WOMAC total24 within-display contrast intervals vs arm intervals and reproducing rows | reproduced |
| C013 | statistical_results | S_W | S_W | REPORT results within-display WORMS counts/totals vs percentages | reproduced |

All thirteen provisional domain and relationship assignments are confirmed. Expanded C012 was independently rechecked by fresh runtime 01a129d8-cbb2-7722-9cd1-850c8005a09c, gpt-6.1-sol/high, after pass-2 screening; its complete replacement card retains glucose12 and WOMAC total24. The original full recheck is preserved in parts/evidence_recheck_initial.md and the extension in evidence_recheck_pass_2.md. Primary precedence is P_R > P_P > S_C > S_W; only C001 has more than one actual relationship. No plan-only corroboration adds P_R, and a shared pattern across distinct outcomes in different reports does not by itself add S_C.

## C001 — Primary signed contrast differs between report locations

**Location found; source and comparator matched:** Yes, all six locations. REPORT [main p2 Key Points](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2) prints mean difference 0.30, 95% CI −6.9 to 6.4, P=.94. REPORT [main p1 abstract](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=1), [p6 Table 2 primary row](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), and [p7 Primary Outcome](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7) each print −0.3 with that interval; Table 2/body give P=.94. REPORT [results p2 eTable 1 original-data row](../../../joi240048supp3_prod_1727199125.83025.pdf#page=2) prints −0.27 (−6.92 to 6.38), P=.94, and modeled changes −19.93/−20.21. REPORT [results p5 knee VAS week24](../../../joi240048supp3_prod_1727199125.83025.pdf#page=5) prints −0.3 (−6.9 to 6.4), P=.94. All concern primary knee VAS change at 24 weeks. Age-adjusted/imputed results are distinct rows and are not silently substituted.

**Applicable rule and reproduced comparison:** Route A, category 2: direction-changing printed sign. Positive interval [.295,.305] versus main/results −.3 interval [−.35,−.25] leaves gap .545/.30=1.8167. Against the original −.27 interval [−.275,−.265], gap .560/.30=1.8667. Negative −.27 and −.3 copies overlap at their displayed precision. The ordinary displayed contrast −20.2−(−19.9)=−.3 supports the negative direction but does not identify the Key Points convention. Neither null exclusion nor significance differs.

**Inputs available; missing definitions:** Exact values, matched endpoint/time/CI and treatment changes are available. The explicitly intended group order or absolute-magnitude convention for Key Points is not supplied.

**Alternative; direct observation versus inference:** An opposite contrast or unsigned magnitude could be intended. Reversing the contrast also reverses the CI orientation to −6.4 to 6.9; the printed interval remains −6.9 to 6.4. Opposite signs are directly observed; their production mechanism is inferred and not assigned.

**Classification:** statistical_results; primary S_C; all S_C, S_W. Confirmed REPORT roles at each location. The supplement's original and VAS24 values are themselves matched conflicting comparators to +0.30; their negative values also corroborate the main body, but that does not erase their direct cross-report comparison. This is distinct from citing a plan solely to support the intended value. S_C takes precedence over the within-main S_W conflict. **Classification ambiguity:** The Key Points contrast convention is unspecified.

**Evidence state:** reproduced. The positive printed Key Points value is present and does not reconcile with matched signed primary copies after display allowances. **Exact remaining human question:** Which signed treatment contrast and group order belong to the primary estimate and its printed interval in Key Points?

## C002 — Placebo composition percentages differ by a decimal place

**Location found; source and comparator matched:** Yes. REPORT [main p2 Interventions last line](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=2) prints less than 5 mg/g (0.5%), completed as other omega-3 content at REPORT [main p3 first continuation](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3). REPORT [main p9 Discussion](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=9) describes the same oil without EPA/DHA and less than 5 mg/g (0.05%) other omega-3.

**Applicable rule and reproduced calculation:** Route A, category 2: magnitude-changing decimal. Percentage intervals [.45,.55]% and [.045,.055]% leave .395 percentage-point gap/.5=.79 (or /.05=7.9). Since 1 g=1000 mg, 5 mg/g corresponds to .5%; allowing 5±.5 mg/g yields [.45,.55]% and the same discrepancy against .05%. This compares parenthetical concentration bounds, not measured unreported oil concentrations.

**Inputs available; missing definitions:** Both concentration/percentage copies and unit conversion are available. Actual concentration and whether a distinct upper bound was intended are absent.

**Alternative; direct observation versus inference:** An actual concentration could satisfy both inequalities; that does not equate their printed parenthetical conversions. A differing intended bound or decimal-position substitution is possible. The tenfold printed percentage difference is observed; a mechanism is not established.

**Classification:** statistical_results; primary/all S_W; all compared/continuation content is REPORT within the main article. Confirmed without change. **Classification ambiguity:** None concerning role or relationship; intended concentration remains a question.

**Evidence state:** reproduced, determined by the printed .5%/.05% separation. **Exact remaining human question:** Which mass-concentration bound and parenthetical percentage describe the randomized placebo's other omega-3 composition?

## C003 — Primary VAS recall periods differ between plan and report

**Location found; source and comparator matched:** Yes. PLAN [protocol p6 Primary outcome](../../../joi240048supp1_prod_1727199125.7845.pdf#page=6) identifies 24-week VAS knee-pain change; PLAN [protocol p8 Primary outcome: Pain](../../../joi240048supp1_prod_1727199125.7845.pdf#page=8) specifies a 100-mm VAS question asking pain today. REPORT [main p3 Primary Outcome](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=3) defines 24-week change in VAS pain over the past 7 days; REPORT [main p5 Table 1 footnote b](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=5) repeats the past-7-days definition.

**Applicable rule and reproduced comparison:** Route B, focus D: the reference period is part of the primary endpoint definition. Today and past 7 days differ despite the matching scale/time of follow-up. Half-unit numerical precision is inapplicable to this categorical window comparison. The discrepancy affects definition extraction for the primary −.3 contrast.

**Inputs available; missing definitions:** Both endpoint passages and recall statements are available. The administered questionnaire, version/date, or amendment linking the windows is absent.

**Alternative; direct observation versus inference:** The instrument may have changed or both recall items may have been collected. Printed window difference is observed; which question generated the primary analysis is not directly observed.

**Classification:** protocol_report; primary/all P_R; PLAN protocol endpoint compared with REPORT main endpoint. Confirmed. Plan p6 matches the primary time point and does not create P_P. **Classification ambiguity:** A supplied future amendment or instrument could explain the difference; none is present in the package.

**Evidence state:** reproduced, determined by the two distinct printed primary reference periods. **Exact remaining human question:** Which recall period was administered for the analyzed primary VAS, and what dated instrument or amendment connects the supplied definitions?

## C004 — ICOAP item count does not identify the scoring denominator

**Location found; source and comparator matched:** Yes. REPORT [main p4 Post Hoc Outcomes](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4) gives item scoring 0–4, raw total 0–44, constant 0–20, intermittent 0–24, all rescaled to 0–100. REPORT [main p5 Table 1 footnote g](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=5) states five constant questions and eight on pain that comes and goes. REPORT [main p6 ICOAP rows and footnote d](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6) uses these descriptions for the reported rescaled outcomes.

**Applicable rule and reproduced calculation:** Route B, focus C: the printed numbers do not jointly specify an additive scoring denominator. Eight×four implies maximum 32, five×four=20, and their sum maximum is 52 rather than 44. Even conservative literal half-unit inputs [7.5,8.5]×[3.5,4.5]=[26.25,38.25] versus printed 24 interval [23.5,24.5] leave gap 1.75/24=.0729167. Integer scale definitions normally are exact; the broader rounding envelope still does not reconcile the intermittent maximum. The total discrepancy is consequential to the same scoring-definition issue.

**Inputs available; missing definitions:** Printed question counts, item maximum, subscale maxima and rescaling destination are available. Which questions contribute to the intermittent sum, any unscored branching questions/weights, and exact rescaling denominator are absent.

**Alternative; direct observation versus inference:** Eight questions could include items omitted from the score, or a weighting/branching rule could produce maximum 24. The source does not supply such a bridge. Counts/ranges are observed; eight scored equal-weight items is an explicit diagnostic interpretation, not an externally imposed instrument version.

**Classification:** statistical_results; primary/all S_W; every compared location is REPORT main article. Confirmed. **Classification ambiguity:** A field-specific question-versus-scored-item convention may explain the difference, but is not established from supplied material.

**Evidence state:** reproduced, determined by the unresolved printed count/raw-maximum combination under the source-supported additive reading and its precision envelope. **Exact remaining human question:** Which of the eight intermittent questions contributed to the raw 0–24 score, and which denominators normalized the intermittent and total ICOAP outcomes?

## C005 — Adopted power specifications differ between plan and report

**Location found; source and comparator matched:** Yes. PLAN [protocol p12 Power calculations](../../../joi240048supp1_prod_1727199125.7845.pdf#page=12) prints pain difference 10 mm, change SD 25.5, 90% power, .05, 234 participants inflated to 260/130 per arm; effusion power 96% for 20% difference, mean 2.24 cm², change SD 1.35. PLAN [protocol p2 secondary hypothesis](../../../joi240048supp1_prod_1727199125.7845.pdf#page=2) gives 20% effusion reduction over 24 weeks. REPORT [main p4 Power Calculations](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4) gives 130/group, 90% power, VAS difference 10 points/change SD 23.8, effusion-volume difference 4.5 mL, alpha .05.

**Applicable rule and reproduced calculation:** Route B, focus D: compare adopted design inputs. SD intervals [25.45,25.55]/[23.75,23.85] leave 1.60/25.5=.0627451. Power intervals [95.5,96.5]/[89.5,90.5] leave 5/96=.0520833. Plan absolute area target .20×2.24=.448 cm² differs dimensionally from report volume 4.5 mL; no rounding operation converts area into volume. Same nominal sample size does not identify a shared design calculation.

**Inputs available; missing definitions:** All compared printed specifications are available. A dated adopted calculation/amendment, area-to-volume target link, and report effusion-volume dispersion input are absent.

**Alternative; direct observation versus inference:** Different cited source trials, an amended calculation or retrospective summary could explain the specifications. The differing inputs and dimensions are observed; their adoption history is not established. The historical n=54 WOMAC illustration explicitly regarded as optimistic is not substituted.

**Classification:** protocol_report; primary/all P_R; PLAN protocol design vs REPORT main design. Confirmed. The independent plan-internal power-reproduction question is C011 and is not added here as P_P. **Classification ambiguity:** An unsupplied amendment or retrospective summary could bridge the records.

**Evidence state:** reproduced, determined by the disjoint SD/power intervals and different effusion target dimensions. **Exact remaining human question:** Which dated calculation prospectively governed the trial's pain dispersion and effusion target/power, and what document explains the changed specifications?

## C006 — Reported primary model differs from supplied planned model

**Location found; source and comparator matched:** Yes. PLAN [protocol p12 Statistics](../../../joi240048supp1_prod_1727199125.7845.pdf#page=12) and PLAN [SAP p1 lines 5–7](../../../joi240048supp2_prod_1727199125.8245.pdf#page=1) prescribe between-group linear regression of changes in pain, maximal effusion size and function, with univariate/conditional multivariable modeling. REPORT [main p4 Statistical Analyses](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4) specifies longitudinal mixed model with treatment, month, interaction, participant/center random intercepts and month random slope; REPORT [main p7 continuation](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7) explains arm changes/contrasts as linear combinations of coefficients. The complete new report maps and direct current main/results extraction supply no separately identified original change-score regression primary estimate.

**Applicable rule and reproduced comparison:** Route A, category 5: planned primary analysis compared with producing reported model. The random-effects/time structure is materially more specific than the stated planned regression of changes, and no separate original-model result is identified. Categorical analysis-specification comparison; numerical precision does not apply. Conditional baseline adjustment is shared and is not claimed as a discrepancy.

**Inputs available; missing definitions:** Both full producing/planned statements are available. The dated prespecification/amendment, operational elaboration of the original model, and original-model primary output are absent.

**Alternative; direct observation versus inference:** Mixed modeling may be an approved amendment or elaboration of broad linear-regression intentions. Both choices can be coherent. Printed specification difference is observed; an unauthorized change is not inferred.

**Classification:** protocol_report; primary/all P_R. Protocol and SAP are PLAN; the mixed-model description is REPORT. Confirmed. Plan copies agree, so no P_P; main methods continuation agrees, so no S_W. **Classification ambiguity:** Whether a documented amendment or elaboration explains the model is unknown from supplied material.

**Evidence state:** reproduced, determined by the distinct supplied model specifications and absence of a separately identified original-model primary estimate. **Exact remaining human question:** Where is the dated specification connecting the supplied change-score regression to the reported longitudinal mixed model, or the planned-model primary result?

## C007 — Planned per-protocol primary efficacy analysis is not reported

**Location found; source and comparator matched:** Yes. PLAN [protocol p12 Statistics](../../../joi240048supp1_prod_1727199125.7845.pdf#page=12) and PLAN [SAP p1 lines 8–9](../../../joi240048supp2_prod_1727199125.8245.pdf#page=1) unconditionally state analyses for participants consuming ≥80% capsules. REPORT [main p4 methods](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [p7 methods/results](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7), and [p6 Table 2](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6) identify randomized longitudinal analyses. REPORT [results p2 eTable 1](../../../joi240048supp3_prod_1727199125.83025.pdf#page=2) gives original, age-adjusted and imputed primary rows. REPORT [results p3 eTable 2](../../../joi240048supp3_prod_1727199125.83025.pdf#page=3) gives ≥80%-adherence frequencies, limited to available pill-count/trial-completion data, without efficacy estimates.

**Applicable rule and reproduced comparison:** Route A, category 5: absence of an unconditionally planned primary analysis in supplied results. Absence recheck covers complete main pp1–10 and results pp1–15 through the full new maps, fresh direct layout extraction and review of all result/table families, with exact visual confirmation of pertinent methods, efficacy and adherence pages. No primary effect/CI/P is identified as using the ≥80%-capsule population. This conclusion is bounded to supplied reporting, not whether an analysis was ever performed. A keyword search alone did not determine it. Numerical precision is inapplicable.

**Inputs available; missing definitions:** Prespecified restriction and complete supplied result units are available. Restricted population definition/size, efficacy output, or amendment removing the analysis are absent. Descriptive adherence counts do not supply those missing quantities.

**Alternative; direct observation versus inference:** It may have been performed but not supplied, amended, or prevented by incomplete pill data. Those are explanations; absence of an identified supplied result is observed.

**Classification:** protocol_report; primary/all P_R; PLAN protocol/SAP vs REPORT main/results efficacy material. Confirmed. Agreement of plans and adherence descriptives adds no other conflict. **Classification ambiguity:** Unsupplied analysis/amendment could explain reporting status.

**Evidence state:** reproduced, determined by explicit planned analysis and no corresponding supplied primary estimate. **Exact remaining human question:** Where are the planned ≥80%-capsule primary per-protocol population definition, estimate and interval, or the dated amendment removing that analysis?

## C008 — Repeated modeled arm-change and point-contrast discrepancies

**Location found; source and comparator matched:** Yes, every retained row and witness. REPORT [main p6 Table 2 ICOAP total24/intermittent24](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6), REPORT [results p5 WOMAC weight-bearing4/function4](../../../joi240048supp3_prod_1727199125.83025.pdf#page=5), and REPORT [results p6 hsCRP12/24 and glucose12](../../../joi240048supp3_prod_1727199125.83025.pdf#page=6) were visually read. Producing-model REPORT [main p4](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4) and [main p7](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7) describe modeled arm changes and linear-combination differences.

| Affected row | Krill modeled change (95% CI) | Placebo modeled change (95% CI) | Printed contrast (95% CI), P | Half-unit recomputation vs printed envelope | Gap/printed magnitude |
|---|---|---|---|---|---|
| ICOAP total24 | −9.9 (−13.3,−6.57) | −8.2 (−11.9,−4.5) | 2.05 (−2.64,6.74), .39 | P−K=1.7; [1.60,1.80] vs [2.045,2.055] | .245/2.05=.119512 |
| WOMAC weight-bearing4 | −84 (−122,−46) | −103 (−141,−65) | 3 (−10,16), .66 | P−K=−19; [−20,−18] vs [2.5,3.5] | 20.5/3=6.833333 |
| hsCRP12 | −.53 (−1.32,.26) | .24 (−.55,1.03) | .07 (−1.19,1.33), .92 | P−K=.77; [.760,.780] vs [.065,.075] | .685/.07=9.785714 |

**Applicable rule and reproduced calculation:** Route A, category 4, the same modeled P−K identity that reproduces other continuous rows. Witnesses: intermittent ICOAP −8.2−(−9.7)=1.5; function4 −103−(−84)=−19; hsCRP24 −.12−(−.76)=.64; primary VAS24 −20.2−(−19.9)=−.3. These witnesses reconcile under display precision. All three affected gaps exceed .05. This comparison uses displayed modeled changes, not crude final-minus-baseline means. CI/P significance agreement does not reconcile the conflicting point contrasts.

**Inputs available; missing definitions:** Every displayed change, contrast, CI/P and model statement is available. Row-specific fitted output, marginalization, common model/population and exact contrast definition are absent.

**Alternative; direct observation versus inference:** Distinct row-specific models or marginalization may underlie arm and contrast columns. Weight-bearing4 changes/CIs exactly repeat function4; ICOAP placebo total change/CI repeats intermittent; hsCRP12 contrast tuple repeats glucose12. These repetitions are observed; a copying or column-production mechanism is not established.

**Classification:** statistical_results; primary/all S_W. Every failure is within its own REPORT display. No same matched result conflicts across the two reports for this issue; the shared methods corroborate the interpretation rather than creating S_C. Confirmed. **Classification ambiguity:** Undisclosed row-specific analysis distinctions may explain individual occurrences.

**Evidence state:** reproduced, determined separately by each of the three disjoint contrast envelopes. **Exact remaining human question:** Which modeled arm changes and contrast belong to each affected endpoint/time row, and did the columns use a shared model, population and marginalization procedure?

## C009 — Selected adverse-event counts change treatment attribution

**Location found; source and comparator matched:** Yes, all three event types. REPORT [main p8 Table 3](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8) labels columns krill n130/placebo n132; cough 2/0, reflux 1/3, abdominal discomfort 0/3. REPORT [results p10 eTable 7 headers and cough](../../../joi240048supp3_prod_1727199125.83025.pdf#page=10) has the same K/P order and cough blank/2. REPORT [results p11 continuation gastrointestinal rows](../../../joi240048supp3_prod_1727199125.83025.pdf#page=11) gives reflux 3/1 and abdominal discomfort 3/blank. Blank cells remain blank; no implicit zeros enter the calculations.

**Applicable rule and reproduced calculation:** Route A, category 2: treatment-specific count attribution changes. Krill reflux 1[.5,1.5] vs 3[2.5,3.5] gap1/1=1; placebo reflux 3 vs1 gap1/3=.333333. Krill abdominal discomfort 0[−.5,.5] vs3[2.5,3.5] gap2; placebo cough 0[−.5,.5] vs2[1.5,2.5] gap1. Against printed zero any positive gap reproduces. Nonnegative truncation of zero's interval does not alter either gap. Main K cough2 and P abdominal3 have supplementary blanks, which document treatment attribution but are not independently quantified comparisons.

**Inputs available; missing definitions:** Explicit counts, event names, treatment headers and study period are available. Any distinct coding, event/person unit, population subset or table-specific counting definition is absent.

**Alternative; direct observation versus inference:** Different coding/subsets or treatment-column substitutions are possible. Conflicting explicit treatment counts are directly observed; their production mechanism is not established. Adjacent 1-vs2 copies with touching half-unit intervals are not part of this retained pattern.

**Classification:** statistical_results; primary/all S_C; REPORT main safety vs REPORT supplementary safety. Confirmed. **Classification ambiguity:** An undisclosed differing counting basis could explain selected rows.

**Evidence state:** reproduced, determined by the four explicit matching arm/event comparisons above. **Exact remaining human question:** Which treatment-specific cough, reflux and abdominal-discomfort counts apply, and do both displays use the same event-count definitions and population?

## C010 — Serious-event relatedness classifications do not reconcile

**Location found; source and comparator matched:** Yes. REPORT [main p8 Table 3 final row, footnote b, safety narrative](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=8) gives treatment-related SAE0/0, no related serious events identified by investigators, and all serious events considered unrelated. REPORT [results p14 eTable 8](../../../joi240048supp3_prod_1727199125.83025.pdf#page=14) explicitly labels parentheses as relationship with treatment. Its treatment order is placebo first, krill second. Krill transfusion-dependent anaemia is 1 (Probable); seven other krill entries and three placebo entries are Possible. Krill fracture fixation and placebo appendicitis are Unlikely; two placebo unknown entries are NA. All event entries total K9/P6 as in the main report.

**Applicable rule and reproduced comparison:** Route B, focus A/C: categorical relatedness-to-summary mapping is unresolved. The probable treatment relation is not reconciled by the main all-unrelated assertion or a supplied classification threshold. No conversion of every Possible to related is assumed. Numerical half-unit precision is inapplicable to the categorical comparison; no 0-vs1 argument is used to bypass touching integer intervals. The affected extracted result is final treatment-related SAE classification, particularly anaemia.

**Inputs available; missing definitions:** Event/treatment labels, relatedness entries, main assertions and total event alignment are available. The final investigator assessment date/version and mapping of Possible/Probable/Unlikely/NA into treatment-related status are absent.

**Alternative; direct observation versus inference:** Main may summarize a later assessment while supplement retains earlier coding, or relatedness may have an unstated threshold. The printed classifications conflict as supplied; clinical causation or adjudication history is not inferred.

**Classification:** statistical_results; primary/all S_C; both compared materials are REPORT safety results. Confirmed. This concerns classification of a numerical safety outcome, not a clinical causality audit. **Classification ambiguity:** Unsupplied final assessment/mapping may reconcile the records.

**Evidence state:** reproduced, determined by Probable treatment-related coding versus the all-unrelated summary without a supplied bridge. **Exact remaining human question:** Which final assessment and mapping govern the related-SAE summary, and was the probable krill anaemia classification subsequently changed?

## C011 — Planned effusion power does not reproduce from supplied inputs

**Location found; source and comparator matched:** Yes. PLAN [protocol p12 Power calculations/Statistics](../../../joi240048supp1_prod_1727199125.7845.pdf#page=12) gives 234 participants before 10% loss, 260/130 per arm after allowance, and 96% effusion power for a 20% difference using mean2.24 cm²/change SD1.35. It specifies between-group regression and two-tailed .05. PLAN [protocol p2 hypothesis](../../../joi240048supp1_prod_1727199125.7845.pdf#page=2) confirms 20% effusion reduction over24 weeks; PLAN [SAP p1 lines5–10](../../../joi240048supp2_prod_1727199125.8245.pdf#page=1) corroborates model/significance.

**Applicable rule and reproduced calculation:** Route B, focus C/D: stated power from explicit design inputs. A labelled equal-size two-arm normal mean-change diagnostic uses absolute effect .20×2.24=.448 cm² and SE=1.35×sqrt(2/n), with fixed designated two-sided alpha .05. n117/130 per arm gives normal power71.84438%/76.28552%. This diagnoses the supplied simple between-arm specification; it is not the authors' unpublished exact method. Input allowances20%[19.5,20.5],mean[2.235,2.245],SD[1.345,1.355] give fixed-n envelopes[69.15113%,74.44664%]/[73.67002%,78.77797%]. Compared with96%[95.5,96.5], best fixed-n gap16.72203/96=.1741878.

The recheck additionally broadens the derived n117 and printed n130 each by±.5, conservatively enclosing the half-unit total-derived sample range. The envelopes become[68.96565%,74.62587%]/[73.50681%,78.93133%]. Even this favorable n130.5 bound leaves gap16.56867/96=.1725903. This expands arithmetic allowances; no source transcription or location changed. Specified alpha is a decision rule rather than an uncertain input. The independent diagnostic is recorded with R4.5.2/base stats in ../preprocessing/evidence_rechecker/numeric-diagnostics.txt.

**Inputs available; missing definitions:** Effect percentage, mean, change SD, nominal sample, loss allowance and significance/model statements are available. Exact powering formula/software, whether 234 or260 governs the effective sample, alternative effect/variance definition and any covariate-efficiency/correlation assumption are absent. Therefore the diagnostic reproduces the need for an additional unstated assumption, not a definitive recomputation of unpublished model power.

**Alternative; direct observation versus inference:** A different effective SD, endpoint contrast or adjustment efficiency could produce96%. The plan also anticipates natural effusion fluctuation in both arms, supporting a between-arm comparison rather than a single-arm change test. Stated inputs/claim are observed; the extra adopted assumption remains unknown. Historical n54 WOMAC illustration is not substituted.

**Classification:** plan_material; primary/all P_P. Conflicting calculation components lie within PLAN protocol; SAP only corroborates the specification. Confirmed. The reported power specifications are a distinct C005 issue, not a P_R relationship here. **Classification ambiguity:** Exact adopted calculation and efficiency assumptions are unsupplied.

**Evidence state:** reproduced, determined by the large diagnostic gap under the supplied simple two-arm interpretation, still present after every specified numeric allowance above. **Exact remaining human question:** What adopted calculation and additional effect, variance or efficiency assumption produce96% power for the stated20% effusion target with these sample/mean/change-SD inputs?

## C012 — Repeated contrast-interval widths differ from a reproducing display rule

**Finding IDs:** F-ST1-002, F-ST2-001. The completed fresh pass-2 screen independently includes F-ST2-001 and consolidates it into existing C012; its source-confirmation, threshold and consolidation notes were read in screening/inclusion_screen_pass_2.md after completion. This recheck confirms the expanded ledger without assigning or removing a stable ID.

**Location found:** Yes, separately for every affected occurrence: REPORT main article Table 2 WOMAC total pain24 at [DOC-001 PDF p6](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=6); REPORT results eTable 4 WOMAC total pain24 at [DOC-004 PDF p5](../../../joi240048supp3_prod_1727199125.83025.pdf#page=5); and REPORT results eTable 4 fasting glucose12 at [DOC-004 PDF p6](../../../joi240048supp3_prod_1727199125.83025.pdf#page=6). The five earlier WOMAC total-pain method-witness rows all lie on results p5. The glucose24, triglyceride12, HDL12, LDL12 method-witness rows and hsCRP12 tuple comparator all lie on results p6. Main p6 also contains glucose24 as a corroborating copy. REPORT [main p4 Statistical Analyses](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=4), [main p7 continuation](../../../jama_laslett_2024_oi_240048_1727199125.7595.pdf#page=7), main p6 Table 2 footnote a and results p6 adjustment footnote were read and visually confirmed. No cited page or affected occurrence is missing.

**Source value/text matched:** Yes. Main WOMAC total pain24 prints krill change −87 (95% CI −110 to −63), placebo change −83 (−106 to −59), between-group change difference 3.0 (−24 to 31), P=.81. Results p5 prints the same arm changes and intervals and contrast 3 (−24 to 31), P=.81. Its observed follow-up contributors are krill106 and placebo111; the display headings identify randomized groups n=130/n=132. Main follow-up means identify n=129/n=130, but this candidate does not compare those contributor counts or substitute them into the modeled interval rule.

Results p6 fasting glucose12 prints krill change .09 (−.07 to .24), placebo change .15 (−.01 to .31), contrast .07 (−1.19 to 1.33), P=.92, contributors112/112. Glucose24 prints changes .07 (−.12 to .26)/.11 (−.08 to .29), contrast .04 (−.23 to .30), P=.79, contributors100/100. Main p6 corroborates this glucose24 interval. The entire glucose12 contrast .07 (−1.19 to 1.33), P=.92 also appears in the results p6 hsCRP12 row, whose arm changes are −.53 (−1.32 to .26)/.24 (−.55 to 1.03). This repeated tuple is a direct observation; a copying mechanism is not asserted.

The source states that primary and secondary outcomes were evaluated using a linear mixed model with treatment, month, treatment-by-month interaction and baseline outcome adjustment where baseline differences were present. Participant and center are random intercepts; month is a random slope. Main p7 states that within-group changes and between-group differences in changes were calculated using linear combinations of estimated coefficients. Main p6 and results p6 specify the baseline-adjustment threshold at P≤.10 and list hsCRP, back pain, WOMAC total pain and weight-bearing pain. No 24-week-specific WOMAC interval convention or glucose12-specific interval convention is disclosed at these locations. No values were imputed for the displayed analyses; the age sensitivity is separately identified. These model and adjustment statements support matching the displayed modeled changes and contrasts, without proving zero covariance.

**Comparator matched:** Yes. Each witness was separately confirmed from the source image. K/P columns below contain modeled change intervals, not raw baseline/follow-up differences. RSS means the empirical root-sum-square rule applied to arm CI half-widths, with h=(upper−lower)/2. The rule is a diagnostic supported by the same display, not an assertion of the actual unpublished variance formula.

| Witness and source | K change CI | P change CI | Printed contrast CI | Nominal RSS half-width | RSS half-width envelope after each endpoint's own precision | Printed contrast half-width envelope | Result |
|---|---|---|---|---:|---|---|---|
| WOMAC total4; results p5 | −45 to−20 | −50 to−25 | −23 to13 |17.677670|[16.970563,18.384776]|[17.5,18.5]|Overlap|
| WOMAC total8; results p5 | −64 to−37 | −67 to−40 | −22 to16 |19.091883|[18.384776,19.798990]|[18.5,19.5]|Overlap|
| WOMAC total12; results p5 | −69 to−40 | −72 to−43 | −24 to18 |20.506097|[19.798990,21.213203]|[20.5,21.5]|Overlap|
| WOMAC total16; results p5 | −83 to−51 | −84 to−52 | −24 to22 |22.627417|[21.920310,23.334524]|[22.5,23.5]|Overlap|
| WOMAC total20; results p5 | −90 to−54 | −85 to−49 | −21 to30 |25.455844|[24.748737,26.162951]|[25,26]|Overlap|
| Glucose24; results p6, main p6 corroborates | −.12 to.26 | −.08 to.29 | −.23 to.30 |.265189|[.258118,.272259]|[.260,.270]|Overlap|
| Triglyceride12; results p6 | −.23 to.02 | .01 to.26 | .07 to.42 |.176777|[.169706,.183848]|[.170,.180]|Overlap|
| HDL12; results p6 | 0.0 to.08 | −.01 to.07 | −.07 to.05 |.056569|[.037165,.081125]|[.055,.065]|Overlap|
| LDL12; results p6 | −.01 to0.2 | −.15 to.06 | −.29 to.005 |.148492|[.126516,.172210]|[.144750,.150250]|Overlap|

Three additional same-main-display witnesses were visually confirmed on main p6: WOMAC weight-bearing24 arm CIs−61 to−42/−58 to−39, contrast CI−10 to16; WOMAC non-weight-bearing24 arm CIs−32 to−15/−29 to−13, contrast CI−10 to14; WOMAC function24 arm CIs−299 to−182/−247 to−132, contrast CI−31 to133. Their nominal RSS half-widths are13.435029,11.672618 and82.027435 respectively. Integer endpoint allowances give RSS envelopes[12.727922,14.142136], [10.965856,12.379418] and[81.320354,82.734515], each overlapping its printed half-width envelope[12.5,13.5], [11.5,12.5] and[81.5,82.5]. They support the rule within main Table 2 itself; the WOMAC24 main occurrence does not depend solely on a witness in another document.

Every witness has zero remaining width-interval gap after its actual display precision. The point and endpoint rounding allowances also permit centered intervals for these witnesses: for example WOMAC20's contrast5 permits a center4.5 and RSS width25.455844, yielding endpoints−20.955844/29.955844 inside the printed endpoint allowances. No nominal center/half-width difference caused solely by integer rounding is claimed. HDL12 prints 0.0, whose half-unit is .05; LDL12 prints 0.2, whose half-unit is .05, and its contrast upper .005 has half-unit .0005. The table respects these mixed precisions rather than silently giving all endpoints two decimal places. The broader allowances reinforce witness compatibility and do not alter either affected occurrence's mismatch.

**Consistency rule applicable:** Yes. Route A, category 4 of QUALITY_CONTROL_SCOPE.md covers a printed interval that does not reproduce, beyond the display-precision rule, under a method that reproduces other rows of the same display. All five earlier time points of the same adjusted WOMAC total-pain outcome support the empirical RSS width rule. The same-page glucose24 and lipid rows support it for glucose12. The source does not establish that the model uses zero cross-arm covariance or common row-specific critical values, and none is assumed as a factual model property. Category 4 makes the missing producing method a human question rather than an automatic conditional exclusion. This is not a category1 interval-null/P conflict: both affected CIs contain0 and both printed P values exceed.05.

**Calculation or logical comparison reproduced, including display precision:** Yes, separately for both occurrences and both WOMAC copies.

For WOMAC24 both nominal arm CI half-widths are23.5. Allowing each integer arm endpoint ±.5 gives hK and hP in[23,24], and empirical RSS contrast half-width[32.5269119,33.9411255], nominal33.2340187. The printed contrast endpoints−24 and31 imply half-width27.5 with envelope[27,28]; the width gap is4.5269119, relative4.5269119/27.5=.1646150.

Main prints the contrast3.0, so its center allowance is[2.95,3.05]. Combining that allowance with the RSS envelope gives the lower endpoint envelope[−30.9911255,−29.4769119] and upper[35.4769119,36.9911255]. Printed lower−24 allows[−24.5,−23.5]; the nearest gap is4.9769119 and relative gap4.9769119/24=.2073713. Printed upper31 allows[30.5,31.5]; gap3.9769119 and relative gap3.9769119/31=.1282875. Both exceed.05.

Results prints contrast3, so its wider center allowance is[2.5,3.5]. The recomputed lower envelope becomes[−31.4411255,−29.0269119] and upper[35.0269119,37.4411255]. The respective gaps from the same printed endpoint allowances are4.5269119/24=.1886213 and3.5269119/31=.1137714. Thus the discrepancy remains beyond precision in each printed copy. Arm point subtraction−83−(−87)=4 permits[3,5]; that overlaps main3.0[2.95,3.05] and results3[2.5,3.5]. No point-estimate algebra discrepancy is added.

For glucose12, hK=.155/hP=.160 nominally and RSS=.222766694. Each arm endpoint is printed to .01, allowing ±.005; hK[.150,.160], hP[.155,.165] therefore give RSS[.215696546,.229836899]. The printed contrast .07 permits center[.065,.075], giving lower envelope[−.164836899,−.140696546] and upper[.280696546,.304836899]. Printed lower−1.19 permits[−1.195,−1.185], and upper1.33 permits[1.325,1.335]. Both gaps equal1.020163101, with relative gaps1.020163101/1.19=.857279917 and /1.33=.767039926. Nominal printed half-width1.26 is also disjoint from RSS. Arm point subtraction.15−.09=.06 permits[.05,.07], overlapping the printed contrast[.065,.075]; no point discrepancy is claimed.

**Necessary inputs available:** Yes for the empirical rule and every display-precision comparison: exact arm endpoints, contrast point/endpoints, time points, outcomes, confidence-level labels, column bindings and same-display witness rows are available. Each relevant endpoint has its actual printed precision applied. Inputs are not taken from descriptive final means or from crude participant ratios. The printing of 95% CIs and the two-sided .05 test threshold is confirmed, but no exact P-value inversion is used.

**Exact missing inputs or definitions:** The fitted coefficient covariance matrix; covariance between the modeled arm changes; row-specific residual/variance estimates; degrees of freedom; critical values for the marginal-change and contrast intervals; exact contrast vectors and marginalization convention; and any distinct row-specific interval calculation. Raw fitted output is not supplied. These absences limit exact statistical regeneration. They do not prevent reproducing the empirical same-display discrepancy under category4.

**Source-grounded alternative interpretation:** The reported longitudinal model can share coefficients between arms, so nonzero arm-change covariance can change contrast variance. Marginal and contrast intervals could use different degrees of freedom, critical values or variance/marginalization conventions, especially if these depend on outcome and follow-up. A row-specific calculation could therefore explain either printed interval. WOMAC total pain is baseline-adjusted, whereas glucose is not listed among baseline-adjusted outcomes; consolidation does not assert these fits are identical. Neither a covariance convention nor an identified row-specific interval convention in the supplied methods explains the printed exceptions to the rule reproducing their own neighboring rows. The hsCRP/glucose repeated contrast tuple is compatible with a transcription-production explanation, but such an explanation is inferred and not adopted as a fact.

**Direct observation versus inferred explanation:** Direct: all printed rows, the agreeing report copies of WOMAC24, the repeated hsCRP/glucose12 tuple, the model/adjustment descriptions, and the disjoint recomputation intervals under the stated diagnostic. Inferred and unconfirmed: any copying mechanism, zero actual covariance, use of a common critical value, or a particular intended replacement interval. No preferred analysis or final correction is assigned.

**Classification confirmed:** Review domain statistical_results; primary relationship type S_W; all relationships S_W. **Compared document roles:** REPORT results glucose12 and REPORT main/results WOMAC total24 within-display contrast intervals vs arm intervals and reproducing rows. Both documents contain observed current-trial results, not prospective plans. The two WOMAC copies agree, so their comparison creates no S_C conflict. Main glucose24 corroborates a witness; main methods explain the modeled results and add no plan relationship. No P_R/P_P relationship exists. Each inconsistency is within a REPORT display, so S_W applies without a higher-precedence code. Estimates/intervals/method logic belong to statistical_results, not report_internal_inconsistency. These fields match the expanded ledger; no classification correction is needed.

**Classification ambiguity:** The document roles and primary/all relationships are resolved by content. The producing covariance and row-specific CI conventions remain unprovided; that is a bounded scientific interpretation question, not an ambiguous document role.

**Consolidation check:** Both occurrences fail the same empirical RSS arm-width rule supported by their own eTable4 neighboring rows; both require the same missing producing variance/critical-value definition. No separate production cause is established from the supplied evidence. Retaining glucose12 and WOMAC24 under expanded C012 is supported as one repeated display-width pattern, with the differing outcomes, baseline adjustments and possible row-specific explanations explicitly preserved. C008 instead concerns point-contrast algebra and remains a different rule. The consolidation preserves every new WOMAC occurrence and witness; it does not turn main-versus-supplement agreement into a cross-report inconsistency.

**Evidence state:** reproduced. Determining fact: the exact source values remain as transcribed, the same-display empirical rule reproduces the stated witness rows within actual half-unit intervals, and both affected occurrences remain separated from it by relative endpoint gaps above.05. No transcribed source value or source location required correction. Clarification of mixed witness endpoint precision broadens their compatibility envelopes but changes neither occurrence's evidence state.

**Exact remaining human question:** Which covariance, degrees-of-freedom, critical-value or interval/marginalization calculation produced the WOMAC total-pain24 contrast3.0(−24 to31) and fasting glucose12 contrast.07(−1.19 to1.33), and what row-specific convention explains their departure from the arm-CI-width rule that reproduces all five earlier WOMAC total-pain rows and the neighboring glucose/lipid rows? The question concerns producing definitions and extractable interval precision; both candidates' significance directions remain unchanged.

**Provenance and compute:** Poppler26.01.0 pdftoppm direct CPU rendering produced main-p04.png, main-p06.png, main-p07.png at120dpi and results-p05.png/results-p06.png at140dpi under preprocessing/evidence_recheck_pass_2/. All five were visually inspected. Direct pdftotext -layout produced main-p04-p07-layout.txt and results-p05-p06-layout.txt in the same directory. Arithmetic used explicitly transcribed supplied values and JavaScript Math.hypot in the interactive tool isolate; all resulting bounds are printed above. No OCR, fallback interpreter, GPU, external material or new Python helper was used. Assigned stable ID coverage1/1; affected result occurrences3/3; same-display witness relationships12/12 plus the main glucose24 corroborating copy; source pages5/5; no source-location or scientific-coverage gap. Missing producing-model definitions are named above. Pending Human Adjudication.

## C013 — WORMS smaller-one-unit percentages differ from their counts

**Location found; source and comparator matched:** Yes, both arms. REPORT [results p8 eTable5 smaller−1-unit and totals](../../../joi240048supp3_prod_1727199125.83025.pdf#page=8) prints K10(12%) and P16(12%), totals107(100%)/109(100%). Other category counts K2,80,12,3 and P2,75,13,3 sum with these counts to107/109.

**Applicable rule and reproduced calculation:** Route A, category3: numerator/denominator/percentage within one display. K100×10/107=9.345794%; half-unit numerator/denominator bounds100×[9.5/107.5,10.5/106.5]=[8.837209%,9.859155%]. Printed12% interval[11.5,12.5] leaves gap1.640845/12=.1367371. P100×16/109=14.678899%; bounds100×[15.5/109.5,16.5/108.5]=[14.155251%,15.207373%], gap1.655251/12=.1379376. Both exceed .05; both retained occurrences reproduce independently. Counts are discrete, but even the broader mandated literal half-unit envelopes fail to reconcile.

**Inputs available; missing definitions:** Explicit numerators, percentages, arm totals and complete count sums are available. Any different denominators or weighted percentage definition are absent; the source provides no such indication.

**Alternative; direct observation versus inference:** Another count/denominator could underlie each12%, or percentages may have been reused. The two count/percentage mismatches are observed; their mechanism is not established. Matching printed12% across arms does not identify a unique underlying input.

**Classification:** statistical_results; primary/all S_W; every comparison is within one REPORT results display. Confirmed. **Classification ambiguity:** None concerning role or relationship.

**Evidence state:** reproduced, determined independently by the two separated percentage envelopes. **Exact remaining human question:** Which numerators and denominators produce the smaller-by-one-unit WORMS percentage in each treatment arm?

## Provenance, completeness and bounded limits

Thirteen assigned IDs covered; thirteen reproduced, zero reproduced_after_transcription_correction, zero not_reproduced. Classification counts: statistical_results8, report_internal_inconsistency0, protocol_report4, plan_material1. Primary types:S_C3,S_W5,P_R4,P_P1. No source location, repeated-pattern occurrence or classified ID remains unexamined. All original assigned IDs are retained. The C011 expansion changes only a diagnostic envelope, not a transcribed source value or location.

Current-source images visually inspected: preprocessing/inclusion_screener/main-p1.png,main-p3.png,main-p7.png,main-p8.png,results-p2.png,results-p3.png,results-p10.png; preprocessing/numeric/main-p02.png,main-p05.png; preprocessing/statistical_pass_1/main-p06.png,result-p05.png,result-p06.png; preprocessing/cross_source/main-p04.png,main-p09.png,protocol-p08.png,protocol-p12.png,sap-p01.png,results-p14.png; preprocessing/numeric_support/p08.png,p11.png. All are current supplied-source direct Poppler26.01.0 CPU renders, source/command provenance recorded in their originating checker or screen artifact. This stage viewed them independently; no existing image/text artifact was modified.

Fresh derivatives owned by this stage: preprocessing/evidence_rechecker/protocol-p02.png and protocol-p06.png, direct pdftoppm26.01.0, commands `pdftoppm -f N -l N -singlefile -scale-to 1800 -png joi240048supp1_prod_1727199125.7845.pdf OUTPUT_PREFIX`, CPU, physical pages2/6. preprocessing/evidence_rechecker/main-layout.txt and results-layout.txt, direct `pdftotext -layout SOURCE OUTPUT`, Poppler26.01.0, complete DOC-001/DOC-004; used for bounded absence recheck alongside the new maps and pertinent source images. preprocessing/evidence_rechecker/numeric-diagnostics.txt, R4.5.2/base stats, CPU, labelled normal-power/CI/percentage arithmetic only. No OCR, fallback capability, scientific orchestration in Python, or source/reused-asset modification was used.

Remaining human questions are evidence-content limits, not coverage gaps: Key Points contrast order, concentration bound, administered questionnaire/amendments, scored ICOAP item rule, dated adopted power/model specification, per-protocol result, row-specific model output/marginalization/covariance/critical values, safety counting definitions, final SAE assessment mapping and WORMS numerator/denominator. No production mechanism, final correction, severity or disposition is assigned.
