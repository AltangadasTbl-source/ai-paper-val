# Workflow 1.6.2 Mechanical Evidence Recheck

Stable scope: C001, C002, C003, C004, C005, C006, C007. All remain Pending Human Adjudication. This artifact records mechanical facts and classification, without a scientific disposition. Runtime agent ID: 01a129c2-9398-7d72-a901-f965a97cdd81. Role: evidence_rechecker; model: gpt-6.1-sol; reasoning effort: high; start mode: FRESH_SPAWN.

The complete current candidate ledger, current inclusion screen, QUALITY_CONTROL_SCOPE.md and review_contract.md were read. All 15 included finding IDs map to the seven assigned IDs. Supplied PDFs were independently extracted again with direct Poppler pdftotext 26.01.0; source page images, rather than legacy OCR or a prior conclusion, confirmed alignment in the critical result displays. The direct supplied sources are authoritative. Newly extracted text and current source-matched rendered pages are confirmation aids. No source or reused asset was modified. Compute device: CPU, as recorded in tooling_record.md. No OCR, fallback environment, external source, or raw-data assumption was used.

## Classification handoff

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Classification correction |
|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT DOC-001 ED absolute CrI versus separately adjusted RR/P in Table 3 | reproduced | None |
| C002 | protocol_report | P_R | P_R | PLAN DOC-002 triggered primary sensitivity specification versus REPORT DOC-001/DOC-003 supplied primary sensitivities | reproduced | None |
| C003 | protocol_report | P_R | P_R | PLAN DOC-002 explicit week-4 symptom/chart comparisons versus REPORT DOC-001/DOC-003 time-point-specific results | reproduced | None; fatigue/QoL comparative timing remains an alternative |
| C004 | protocol_report | P_R | P_R | PLAN DOC-002 final intervention analysis specification versus REPORT DOC-001/DOC-003 logistic analyses | reproduced | None |
| C005 | statistical_results | S_W | S_W | REPORT DOC-003 empty severe-mouth-sore cohorts versus finite effects and stated logistic methods | reproduced | None |
| C006 | statistical_results | S_C | S_C, S_W | REPORT DOC-001 sadness significance statement/rule versus REPORT DOC-003 sadness CI/P pair | reproduced | None |
| C007 | statistical_results | S_C | S_C, S_W | REPORT DOC-001 neuropathy/hunger significance statements versus REPORT DOC-003 corresponding CI/P pairs | reproduced | None |

All document roles were assigned from content: DOC-001 is a results article, DOC-003 contains results tables/figures and methods, and the cited portions of DOC-002 are prospective protocol/SAP specifications and amendment history. A document corroborating one side does not create another relationship. Primary precedence P_R > P_P > S_C > S_W is applied. No transcribed number or cited page required correction, so none uses reproduced_after_transcription_correction. No location confirmation remains unresolved.

## C001 — ED absolute interval and separately adjusted test

**Evidence state:** reproduced. **Review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W. **Finding IDs:** F-NUM-003, F-ST1-001. **Classification correction:** None. **Classification ambiguity:** None.

**Location found, source matched and comparator matched:** Yes, separately for every listed anchor:

| Exact supplied-source location | Role by content | Independently matched content and function |
|---|---|---|
| [DOC-001 p. 9, Table 3 emergency department row and footnote b](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=9) | REPORT | Absolute rate difference per 100 patient-weeks 3.38, 95% CrI −0.57 to 7.94; RR 1.72, 95% CI 1.03 to 2.87; adjusted P=.04. Footnote distinguishes the treatment-plus-random-site marginalization model from the RR model containing treatment, random site and two stratification factors. Direct page image confirms all columns. |
| [DOC-001 p. 4, significance rule and encounter methods](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=4) | REPORT | Tests are two-sided; P<.05 is significant. Encounter RR analysis is mixed Poisson with site and two stratification factors. |
| [DOC-001 p. 1, abstract ED result](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=1) | REPORT | RR 1.72 (1.03–2.87) and significantly more ED visits; corroborates adjusted RR, not an absolute-effect test. |
| [DOC-001 p. 6, ED narrative](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=6) | REPORT | Means 0.77 versus 0.45 and significant RR 1.72 (1.03–2.87); corroborating only. |
| [DOC-003 p. 17, eTable 12 ED Poisson row](../../../joi240111supp2_prod_1733431204.76024.pdf#page=17) | REPORT | Poisson RR 1.72 (1.03, 2.87), P=.04; Bayesian negative-binomial sensitivity RR 1.73 (0.89, 3.43), probability RR>1 95.2%. These are separate reported analyses, not conflicting copies of the Table 3 absolute effect. |

**Applicable consistency rule:** Route A category 1 expressly retains interval-versus-test null-value differences even when different analyses are disclosed. The Bayesian marginalized absolute-effect credible interval and the frequentist adjusted RR confidence interval/P are separate inferential objects. This is a displayed different-null-reading candidate, not a claim that P=.04 tests the absolute difference.

**Calculation/logical reproduction and precision:** −0.57<0<7.94, whereas .04<.05; the RR interval excludes 1 and agrees with its own P. Absolute estimate half-unit interval [3.375,3.385]; absolute lower/upper-limit intervals [−.575,−.565] and [7.935,7.945]; P interval [.035,.045]. The absolute interval contains zero for every endpoint rounding combination, and P remains below .05. RR lower-limit interval [1.025,1.035] remains above 1. Relative discrepancy is not applicable to the null-value logical comparison; category 1 is exempt from rounding screening. No standard normal approximation or assumed common model was needed.

**Necessary inputs available:** Printed effects, interval types/levels, significance rule, P, and explicitly distinct model covariates are available. **Exact missing inputs/definitions:** The Table 3 absolute-effect posterior/credible-interval construction, priors or posterior draws, and an explicit statement of which inferential summary accompanies the absolute effect are not supplied at these locations. These are unnecessary to reproduce the printed null readings but prevent rerunning the absolute model.

**Source-grounded alternative:** The table intends P only for the adjusted RR; the marginalized absolute Bayesian summary is presented on its own scale without an associated frequentist test. The different models and Bayesian/frequentist meanings can explain the different readings. This alternative is explicit and must stay with the candidate.

**Direct observation versus inference:** Directly observed are the two printed intervals, P, and model distinction. A common-analysis incompatibility or a claim that the RR test fails to reconcile is not inferred. No production mechanism is established.

**Determining recheck fact:** The source-matched absolute CrI contains zero and the separately adjusted P is .04; their displayed null readings differ under the required category-1 rule, with the disclosed separate analyses preserved.

**Remaining human question:** Which inferential summary should accompany extraction of the absolute ED rate difference, and is the printed P intended solely for the separately adjusted RR?

**Classification reason:** The contrasted readings are inside one REPORT table (S_W). The supplement/abstract corroborate its adjusted RR and create no S_C. No PLAN conflicts. The issue concerns intervals and tests, hence statistical_results.

## C002 — Triggered primary total-score ordinal sensitivity

**Evidence state:** reproduced. **Review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R. **Finding IDs:** F-XS-002, F-ST1-005. **Classification correction:** None. **Classification ambiguity:** None.

**Location found, source matched and comparator matched:** Yes at every anchor:

| Exact supplied-source location | Role by content | Independently matched content and function |
|---|---|---|
| [DOC-002 p. 11, final protocol primary comparative analysis](../../../joi240111supp1_prod_1733431204.57929.pdf#page=11) | PLAN | Substantial non-normality of week-8 total SSPedi residuals triggers two sensitivities: one normalizing transformation and another ordinal regression. |
| [DOC-002 p. 36, SAP primary comparative analysis](../../../joi240111supp1_prod_1733431204.57929.pdf#page=36) | PLAN | Same two-sensitivity requirement for the week-8 total-score model. |
| [DOC-002 p. 31, amendment history](../../../joi240111supp1_prod_1733431204.57929.pdf#page=31) | PLAN | November 21, 2023 statistical edits match the final SAP; identifies applicable supplied specification. |
| [DOC-001 p. 3, primary model](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=3) | REPORT | Patient-level week-8 total SSPedi mixed linear model and covariate-adjusted mean difference. |
| [DOC-001 p. 4, primary sensitivity methods/results](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=4) | REPORT | Baseline-adjusted, change-score and chemotherapy-restricted analyses and reference to eFigure 1; individual-symptom proportional-odds analysis is separately identified as secondary. |
| [DOC-003 p. 18, eFigure 1, primary sensitivity items 1–5](../../../joi240111supp2_prod_1733431204.76024.pdf#page=18) | REPORT | Item 2 explicitly says residuals were clearly non-normal/right-skewed; square-root transformation result −0.7 (−1.1,−0.3), P=.003. Other items are restricted/unadjusted/baseline-adjusted and missing-data analyses, not total-score ordinal regression. |
| [DOC-003 p. 19, continuation of eFigure 1](../../../joi240111supp2_prod_1733431204.76024.pdf#page=19) | REPORT | Five imputation strategies and six-row result table, all expressed as mean differences; no ordinal total-score sensitivity. |

**Complete supplied-report absence check:** The complete DOC-001 pp. 1–11 and DOC-003 pp. 1–23 were directly extracted and searched for ordinal, proportional, sensitivity and total-score terms. The result inventory/contents and every potentially relevant result section were reread, including [DOC-003 p. 1 contents](../../../joi240111supp2_prod_1733431204.76024.pdf#page=1), [p. 9 total-score primary model](../../../joi240111supp2_prod_1733431204.76024.pdf#page=9), [p. 10 baseline model](../../../joi240111supp2_prod_1733431204.76024.pdf#page=10), [p. 11 dichotomous individual-item post hoc analysis](../../../joi240111supp2_prod_1733431204.76024.pdf#page=11), [p. 20 week-8 individual-item ordinal figure](../../../joi240111supp2_prod_1733431204.76024.pdf#page=20) and [p. 22 methods](../../../joi240111supp2_prod_1733431204.76024.pdf#page=22), all REPORT. Neither individual-item ordinal results nor dichotomous severe-item results supply an ordinal sensitivity for the total score. The complete figure on p. 20 was visually inspected. No matching total-score ordinal result is present in the supplied REPORT corpus.

**Applicable consistency rule:** Route A category 5, a triggered planned primary analysis not supplied. The observed trigger is a printed report statement, not an assumption that a sensitivity should have been performed.

**Calculation/logical reproduction and precision:** The PLAN requires two distinct analyses if substantial non-normality occurs; REPORT explicitly observes clear non-normality and supplies the transformation branch but no total-score ordinal branch. Display-precision intervals and relative discrepancy are not applicable to this presence/absence comparison; no printed numeric difference is asserted. The square-root estimate is within its own interval and is only a location/branch identifier.

**Necessary inputs available:** Final specification, observed residual statement, endpoint definition and complete supplied report inventory are available. **Exact missing inputs/definitions:** The ordinal total-score sensitivity result, its model/output, or a supplied amendment/replacement explanation; raw residuals and ordinal model data for rerunning it. Absence outside the supplied package cannot be established.

**Source-grounded alternative:** The ordinal result may exist outside the supplied documents, or the successful transformation may have been chosen as a replacement. The supplied final plan says one analysis and another, rather than choosing either, and no replacement is disclosed.

**Direct observation versus inference:** Directly observed are the two-branch requirement, explicit non-normality and the report's listed analyses. The reproduced fact is absence from the supplied report; non-performance of the analysis is not inferred.

**Determining recheck fact:** The report satisfies the stated non-normality trigger and supplies only the transformation branch among the two specifically required sensitivity types.

**Remaining human question:** Where is the planned ordinal total-score sensitivity result, or a supplied explanation of its replacement?

**Classification reason:** The conflict compares prospective PLAN specifications with REPORT analysis inventory, so P_R/protocol_report. Agreement between final protocol and SAP is not a P_P conflict, and multiple report corroborations do not create S_C/S_W.

## C003 — Explicit week-4 symptom and chart comparisons

**Evidence state:** reproduced. **Review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R. **Finding IDs:** F-XS-003, F-ST1-007. **Classification correction:** None. **Classification ambiguity:** The definite core is individual symptoms and chart documentation/interventions; fatigue/QoL comparative timing remains an alternative reading.

**Location found, source matched and comparator matched:** Yes at every anchor:

| Exact supplied-source location | Role by content | Independently matched content and function |
|---|---|---|
| [DOC-002 p. 11, final protocol secondary items 1–4](../../../joi240111supp1_prod_1733431204.57929.pdf#page=11) | PLAN | Individual SSPedi symptoms at weeks 4 and 8: 15 proportional-odds models with ORs/95% CIs; documentation at weeks 4 and 8: logistic effects for three cohorts. Fatigue/QoL use the primary approach. |
| [DOC-002 p. 12, final protocol item 5](../../../joi240111supp1_prod_1733431204.57929.pdf#page=12) | PLAN | Any/symptom-specific intervention at weeks 4 and 8, three cohorts, planned comparative differences/tests/intervals. Direct image resolves extracted threshold glyphs as symptom score ≥3. |
| [DOC-002 p. 34, SAP PRO definitions](../../../joi240111supp1_prod_1733431204.57929.pdf#page=34) | PLAN | Questionnaires obtained at weeks 4 and 8; total score, individual scores, fatigue and eight QoL domains defined. |
| [DOC-002 p. 35, SAP chart definitions](../../../joi240111supp1_prod_1733431204.57929.pdf#page=35) | PLAN | Documentation and intervention binary outcomes assessed at weeks 4 and 8 within the stated 3-day windows. |
| [DOC-002 p. 36, SAP secondary item 1](../../../joi240111supp1_prod_1733431204.57929.pdf#page=36) | PLAN | Explicit weeks 4 and 8 individual-symptom proportional-odds analysis and OR/95% CI presentation. |
| [DOC-002 p. 37, SAP items 2–5](../../../joi240111supp1_prod_1733431204.57929.pdf#page=37) | PLAN | Explicit weeks 4 and 8 documentation and intervention comparisons, all-participant/score>0/score≥3 cohorts; fatigue/QoL timing less explicit. Direct page image confirms definitions. |
| [DOC-001 p. 1, abstract](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=1) | REPORT | Individual-symptom findings and intervention conclusion identify relevant secondary outcome families; documentation/interventions described at week 8. |
| [DOC-001 p. 4, secondary comparative methods/results](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=4) | REPORT | Individual-symptom proportional-odds models, fatigue and QoL explicitly at week 8. |
| [DOC-001 p. 7, Table 2 and footnotes](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=7) | REPORT | Baseline/week-8 distributions and week-8 adjusted effects; no week-4 comparative columns. |
| [DOC-003 p. 12, eTable 9](../../../joi240111supp2_prod_1733431204.76024.pdf#page=12) | REPORT | Week-4 n=208/207 SSPedi; 15 severe-symptom counts/percentages; mean/SD total score, fatigue and QoL. No comparative effect, interval or test columns. |
| [DOC-003 p. 13, eTable 10 beginning](../../../joi240111supp2_prod_1733431204.76024.pdf#page=13) | REPORT | Heading explicitly week 8; documentation all 15 symptoms and beginning of any-intervention rows, three cohorts. Direct source image confirms entire display. |
| [DOC-003 p. 14, eTable 10 continuation](../../../joi240111supp2_prod_1733431204.76024.pdf#page=14) | REPORT | Remaining any-intervention rows and beginning symptom-specific intervention rows, same week-8 display/cohorts. Direct image confirms entire display. |
| [DOC-003 p. 15, eTable 10 conclusion and footnotes](../../../joi240111supp2_prod_1733431204.76024.pdf#page=15) | REPORT | Remaining three symptom-specific rows and definitions of cohorts/model tests; no week-4 effect display. |
| [DOC-003 p. 20, eFigure 2](../../../joi240111supp2_prod_1733431204.76024.pdf#page=20) | REPORT | Complete 15-item ordinal forest plot explicitly week 8; visually confirmed. |
| [DOC-003 p. 21, eFigure 3](../../../joi240111supp2_prod_1733431204.76024.pdf#page=21) | REPORT | Complete eight-domain QoL plot explicitly week 8; visually confirmed and relevant only to broader timing alternative. |

**Every affected occurrence of the supported repeated pattern:** The 15 symptom classes are sadness, anxiety, anger, thinking/remembering, body/face appearance, fatigue, mouth sores, headache, other hurt/pain, tingly/numb hands or feet, vomiting/nausea, hunger, taste, constipation and diarrhea. At week 4 the PLAN explicitly requires their ordinal 0–4 comparative analyses; eTable 9 displays all 15 severe-score descriptions without those effects. For each of the same 15 classes, the three chart families are documentation, any intervention and symptom-specific intervention, each in all participants, score>0 (equivalent to ≥1 for integer scores), and score≥3 cohorts. The full resulting chart pattern was checked across eTable 10 pp. 13–15: only week-8 contrasts are supplied. No symptom class or cohort in this registered core was sampled away.

**Complete supplied-report absence check:** Direct extraction/search covers all DOC-001 pp. 1–11 and DOC-003 pp. 1–23, with the full contents, every comparative result table, all methods/sensitivity sections, and both full forest plots checked. Week-4 references elsewhere concern collection, completion counts, descriptive values or imputation predictors; none provides the named week-4 symptom/chart effects. The week-4 total SSPedi mean is not treated as another planned primary analysis.

**Applicable consistency rule:** Route A category 5 for explicit planned analyses of abstract-represented secondary families not supplied. This is a comparative analysis/time-point inventory comparison, not a discrepancy among contributor counts.

**Calculation/logical reproduction and precision:** A week-8 OR/difference cannot supply a specified week-4 contrast; descriptive severe-symptom percentages cannot supply a full 0–4 ordinal-model OR/CI. Matching endpoint, time point, cohort and reported inferential quantity reproduces the absence. Display precision and relative discrepancy are not applicable to this categorical/inventory difference.

**Necessary inputs available:** Explicit week-4 comparative specifications, all symptom/cohort definitions, all relevant result displays and complete supplied report inventory. **Exact missing inputs/definitions:** Week-4 comparative effects/intervals/tests for the supported symptom/chart core, or their replacement explanation; raw data/code for rerunning them. Fatigue/QoL comparative time-point intent is not explicit enough to establish an additional required absence.

**Source-grounded alternatives:** The report may focus on week 8 or early effects may exist outside the supplied package. Questionnaires are collected at weeks 4 and 8, but fatigue/QoL are analyzed like the primary outcome whose model is explicitly week 8: broader and week-8-only comparative readings are both possible. Fatigue and eight QoL week-4 model omissions are therefore not asserted as established occurrences.

**Direct observation versus inference:** Directly observed are explicit symptom/chart week-4 obligations and week-8-only comparative displays plus descriptive week-4 values. Lack of performance outside the supplied report is not inferred; the fatigue/QoL timing possibility remains an interpretation.

**Determining recheck fact:** No supplied REPORT comparative result matches the explicit week-4 individual-symptom/chart analysis core, despite complete matched result inventory inspection.

**Remaining human question:** Where are the explicit week-4 symptom/chart comparative results or the explanation of their replacement, and which comparative time points were intended for fatigue/QoL?

**Classification reason:** PLAN versus REPORT analysis time point/inventory is P_R/protocol_report. PLAN concordance and REPORT time-point corroboration create no additional relationship. Alternative fatigue/QoL timing does not change the confirmed classification of the explicit core.

## C004 — Final intervention analysis specification versus logistic ORs

**Evidence state:** reproduced. **Review domain:** protocol_report. **Relationship type:** P_R. **All relationships:** P_R. **Finding IDs:** F-XS-001, F-ST1-004. **Classification correction:** None. **Classification ambiguity:** None.

**Location found, source matched and comparator matched:** Yes at every anchor:

| Exact supplied-source location | Role by content | Independently matched content and function |
|---|---|---|
| [DOC-002 p. 12, final protocol secondary item 5](../../../joi240111supp1_prod_1733431204.57929.pdf#page=12) | PLAN | Simple differences in intervention proportions, ignoring clustering; Fisher exact P values; Newcombe 95% CIs; three cohorts. Direct image confirms all words/definitions. |
| [DOC-002 p. 37, final SAP secondary item 5](../../../joi240111supp1_prod_1733431204.57929.pdf#page=37) | PLAN | Same effect/test/interval procedure. Direct page image confirms this final specification. |
| [DOC-002 p. 31, amendment history](../../../joi240111supp1_prod_1733431204.57929.pdf#page=31) | PLAN | Final protocol statistical edits align with the final November 21, 2023 SAP; earlier protocol logistic methods are version context, not a later reconciliation. |
| [DOC-001 p. 1, abstract secondary outcomes/conclusion](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=1) | REPORT | Interventions are secondary outcomes; increased symptom-specific interventions highlighted. |
| [DOC-001 p. 4, secondary chart-outcome methods](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=4) | REPORT | Mixed/fixed logistic models for documentation, any and symptom-specific interventions; effect expressed as OR with 95% CI. |
| [DOC-003 p. 13, eTable 10](../../../joi240111supp2_prod_1733431204.76024.pdf#page=13) | REPORT | Three-cohort any-intervention rows sadness through body/face appearance; direct image confirms displayed multiplicative effects/intervals/Ps and week-8 heading. Documentation rows are context, not part of this method-change scope. |
| [DOC-003 p. 14, eTable 10 continuation](../../../joi240111supp2_prod_1733431204.76024.pdf#page=14) | REPORT | Remaining any-intervention rows fatigue through diarrhea, then symptom-specific rows sadness through hunger; direct image confirms every displayed cohort. |
| [DOC-003 p. 15, eTable 10 final rows and footnote b](../../../joi240111supp2_prod_1733431204.76024.pdf#page=15) | REPORT | Symptom-specific taste, constipation and diarrhea rows; P values described as mixed/fixed logistic regression depending on event numbers. |
| [DOC-003 p. 22, eMethods](../../../joi240111supp2_prod_1733431204.76024.pdf#page=22) | REPORT | Mixed logistic model estimates ORs adjusting stratification factors; if random-site variance cannot be estimated, fixed logistic model includes treatment only. |

**Every affected occurrence of the repeated pattern:** Each of the 15 symptom classes listed under C003 occurs in both any-intervention and symptom-specific-intervention families, each with all-participant, score≥1 and score≥3 cohorts: 2×15×3=90 supplied week-8 contrasts. The complete families spanning pp. 13–15 were checked against the common final-plan specification. Documentation's 45 contrasts are not included in this method-change pattern because documentation's final PLAN procedure is logistic. The broad table header “Difference (95% CI)” is read with the main/eMethods explicit OR definition rather than assumed to mean a risk difference.

**Applicable consistency rule:** Route A category 5 for replaced planned key-secondary analyses, also an explicit method/effect specification conflict under Route B. The comparison is between stated procedures, not adjusted estimates and crude arithmetic.

**Calculation/logical reproduction and precision:** Difference in proportions has null 0; odds ratio has null 1. PLAN specifies unclustered proportion differences/Fisher/Newcombe; REPORT specifies mixed or fixed logistic ORs/logistic P values. These procedures/scales differ categorically for every covered contrast. Display-precision intervals and relative discrepancy are not applicable to specification identity. No numeric RR/OR was reconstructed from counts as proof of this issue.

**Necessary inputs available:** Final plan/version context, stated report model/effect/test, each affected cohort and table family. **Exact missing inputs/definitions:** A supplied later amendment or rationale linking the logistic procedure to the final plan; row-specific model fits and interval/test output sufficient to reproduce implementation. Raw participant/site data are unavailable but unnecessary for the stated-specification comparison.

**Source-grounded alternative:** A later analytical choice may have used logistic methods similar to an earlier plan, or the written report could incompletely describe some test/interval implementations. Neither later amendment nor a reconciliation with the final specification is supplied; no preferred analysis is proposed.

**Direct observation versus inference:** Directly observed are final PLAN and REPORT descriptions on different effect/model/test scales. The estimator for each row, reasons for choosing it, and whether a later unsupplied change occurred are not inferred.

**Determining recheck fact:** The final supplied plan explicitly specifies intervention proportion differences/Fisher/Newcombe while the supplied report explicitly defines the corresponding displayed effects and P values through logistic OR analyses.

**Remaining human question:** Which analysis generated each intervention effect/interval/P value, and what supplied specification or explanation connects it to the final planned procedure?

**Classification reason:** Prospective PLAN versus REPORT analysis specification is P_R/protocol_report. The documented amendment is not itself a P_P conflict; the mutually consistent report descriptions create no additional S relationship.

## C005 — Finite effects with an empty severe-mouth-sore intervention cohort

**Evidence state:** reproduced. **Review domain:** statistical_results. **Relationship type:** S_W. **All relationships:** S_W. **Finding IDs:** F-ST1-006. **Classification correction:** None. **Classification ambiguity:** None.

**Location found, source matched and comparator matched:** Yes for every occurrence and method comparator:

| Exact supplied-source location | Role by content | Independently matched content and function |
|---|---|---|
| [DOC-003 p. 13, eTable 10 documentation, mouth sores, SSPedi≥3](../../../joi240111supp2_prod_1733431204.76024.pdf#page=13) | REPORT | Intervention 0/0, control 2/8 (25%), OR 2.6 (95% CI 0.04,170.4), P>.99. Direct source image confirms empty denominator and severe-cohort column alignment. |
| [DOC-003 p. 14, any intervention, mouth sores, SSPedi≥3](../../../joi240111supp2_prod_1733431204.76024.pdf#page=14) | REPORT | Intervention 0/0, control 1/8 (12.5%), OR 5.00 (0.07,366.4), P>.99. Direct image confirms alignment. |
| [DOC-003 p. 14, symptom-specific intervention, mouth sores, SSPedi≥3](../../../joi240111supp2_prod_1733431204.76024.pdf#page=14) | REPORT | Intervention 0/0, control 1/8 (12.5%), OR 5.00 (0.07,366.4), P>.99; separately confirmed, not assumed from the preceding row. |
| [DOC-003 p. 15, footnotes b/c](../../../joi240111supp2_prod_1733431204.76024.pdf#page=15) | REPORT | Logistic P-value description and cohort-specific denominators, including severe SSPedi≥3. |
| [DOC-003 p. 22, eMethods chart-outcome model](../../../joi240111supp2_prod_1733431204.76024.pdf#page=22) | REPORT | Mixed logistic adjustment for strata; fallback fixed logistic includes treatment only; no empty-arm estimator/additional information described. |

**Applicable consistency rule:** Source-grounded statistical method logic, Route B: the defined observed cohort has no intervention participants but three finite between-treatment effects are supplied, and the described ordinary logistic methods do not identify the added information producing them. This is not just an omitted detail without a conflicting display.

**Calculation/logical reproduction and precision:** Each intervention denominator is exact integer 0, not a rounded continuous value. With all observations in one treatment level, the treatment contrast cannot be identified from the observed severe cohort alone in the described ordinary logistic regression. Diagnostic only: adding .5 to each contingency cell gives (.5×6.5)/(.5×2.5)=2.6 for documentation and (.5×7.5)/(.5×1.5)=5.0 separately for each intervention family. These diagnostic values lie in the printed half-unit intervals [2.55,2.65] and [4.995,5.005]; diagnostic display gaps and relative discrepancies are zero. They do not establish the actual estimator or reproduce its interval/test. No magnitude mismatch is claimed. ORs are within their intervals and each interval contains 1, consistent with P>.99; the candidate concerns identifiability/method definition, not an interval/P conflict.

**Necessary inputs available:** All three exact numerator/denominator pairs, printed OR/CI/P, cohort definitions and stated model/fallback. **Exact missing inputs/definitions:** Empty-arm estimation rule; continuity adjustment, penalty, prior or borrowed information if used; row-level model/output and CI/test construction. No intervention-arm observed severity data exist in the displayed defined cohort.

**Source-grounded alternative:** Continuity-cell information, penalization, a prior or another explicitly defined estimator could yield finite effects. The displayed values match a .5-cell diagnostic, but this numerical match is not evidence of the authors' actual procedure and no such procedure is recommended.

**Direct observation versus inference:** Direct observations are all three 0/0 denominators, finite effects and ordinary logistic descriptions. Nonidentification under that stated observed-cohort model is a logical consequence. Continuity adjustment or any explanation for production remains inferred/possible, not established.

**Determining recheck fact:** Three finite between-treatment ORs are source-confirmed for severe-mouth-sore cohorts with zero observed intervention participants, without a supplied added-information rule connecting them to the stated logistic method.

**Remaining human question:** What estimator and added information produced the three finite effects/intervals/tests when the observed severe-cohort intervention denominator was zero?

**Classification reason:** All conflicting display/method content is in one REPORT supplement, S_W/statistical_results. No PLAN comparator or conflicting main-report value is involved; a corroborating logistic description does not create S_C.

## C006 — Sadness any-intervention interval and displayed boundary P

**Evidence state:** reproduced. **Review domain:** statistical_results. **Relationship type:** S_C. **All relationships:** S_C, S_W. **Finding IDs:** F-NUM-002, F-XS-005, F-ST1-003. **Classification correction:** None. **Classification ambiguity:** None; unrounded P is an inferential alternative, not a role ambiguity.

**Location found, source matched and comparator matched:** Yes at every anchor:

| Exact supplied-source location | Role by content | Independently matched content and function |
|---|---|---|
| [DOC-003 p. 13, eTable 10 any intervention, sadness, all participants](../../../joi240111supp2_prod_1733431204.76024.pdf#page=13) | REPORT | 52/220 (23.6%) versus 82/224 (36.6%); OR .51, 95% CI (.26,.99), P=.05. Direct source image confirms row/family/cohort. |
| [DOC-001 p. 4, significance rule](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=4) | REPORT | Two-sided P<.05 is statistically significant. |
| [DOC-001 p. 5, sadness any-intervention narrative](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=5) | REPORT | Same 52/220 versus 82/224 counts, calls usual-care intervention significantly more common, prints P=.05 for sadness. |
| [DOC-003 p. 15, footnote b](../../../joi240111supp2_prod_1733431204.76024.pdf#page=15) | REPORT | P values calculated by mixed/fixed logistic regression. |
| [DOC-003 p. 22, eMethods](../../../joi240111supp2_prod_1733431204.76024.pdf#page=22) | REPORT | Mixed logistic adjustment with treatment-only fixed fallback; no row-specific unrounded P given. |

**Applicable consistency rule:** Route A category 1. The printed CI excludes 1 while displayed equality P=.05 does not satisfy the strict printed P<.05 rule; the main narrative also describes significance. Category 1 requires retaining this printed reading despite a possible unrounded-P explanation.

**Calculation/logical reproduction and precision:** .26<.51<.99<1, but displayed .05 is not <.05. Half-unit intervals: OR [.505,.515], lower CI [.255,.265], upper CI [.985,.995], P [.045,.055]. The CI upper bound remains below 1; the P interval includes values on both sides of .05, so an underlying P<.05 is possible and cannot be excluded. Relative discrepancy is not applicable to this boundary decision; category 1 is exempt from precision screening. Diagnostic percentage checks: 100×52/220=23.63636… and 100×82/224=36.60714…, which fall inside [23.55,23.65] and [36.55,36.65]; both count/percentage display gaps and relative discrepancies are zero. Those percentages are not compared to the adjusted OR.

**Necessary inputs available:** Matched endpoint/family/cohort counts, CI/P, significance rule and narrative. **Exact missing inputs/definitions:** Unrounded P or intended P inequality and the row-specific interval/test computation. No raw-data rerun is needed to reproduce the displayed boundary reading.

**Source-grounded alternative:** A P slightly below .05 rounded to .05, or an intended inequality, could reconcile the underlying test with the CI and narrative. The supplied equality does not identify it. No claim is made that the unprinted underlying test is nonsignificant.

**Direct observation versus inference:** Direct observations are the upper limit .99, P=.05, strict rule and significant narrative. Underlying nonsignificance and a typographic production mechanism are not inferred; an unrounded significant P remains possible.

**Determining recheck fact:** The source-confirmed printed upper CI is below 1, while the source-confirmed displayed P equality lies on the nonqualifying boundary of the report's strict rule; the required category-1 displayed comparison is reproduced.

**Remaining human question:** What is the unrounded or intended P expression and inferential reading for the sadness any-intervention contrast?

**Classification reason:** The supplement's CI/P pair is S_W; main significance wording/rule versus that matched supplemental combination is S_C. S_C takes precedence over S_W, and the issue concerns a statistical result. No PLAN relationship is added.

## C007 — Two symptomatic-cohort intervals contain one despite significant P values

**Evidence state:** reproduced. **Review domain:** statistical_results. **Relationship type:** S_C. **All relationships:** S_C, S_W. **Finding IDs:** F-NUM-001, F-XS-004, F-ST1-002. **Classification correction:** None. **Classification ambiguity:** None.

**Location found, source matched and comparator matched:** Yes, including each repeated result separately:

| Exact supplied-source location | Role by content | Independently matched content and function |
|---|---|---|
| [DOC-003 p. 14, eTable 10 symptom-specific intervention, neuropathy, SSPedi≥1](../../../joi240111supp2_prod_1733431204.76024.pdf#page=14) | REPORT | Tingly/numb hands or feet: 6/57 (10.5%) versus 0/70 (0%); OR17.8, 95%CI (.98,323.1), P=.007. Direct image confirms symptom-specific family and symptomatic cohort, rather than the neighboring all-participant OR17.96 row result. |
| [DOC-003 p. 14, same family/cohort, hunger](../../../joi240111supp2_prod_1733431204.76024.pdf#page=14) | REPORT | Hunger changes: 6/111 (5.4%) versus 0/130 (0%); OR16.08, 95%CI (.9,288.74), P=.009. Separately visually confirmed, rather than neighboring all-participant OR22.4 result. |
| [DOC-003 p. 15, footnote b/c](../../../joi240111supp2_prod_1733431204.76024.pdf#page=15) | REPORT | Logistic P-value methods and symptom-specific cohort denominator definitions. |
| [DOC-003 p. 22, eMethods](../../../joi240111supp2_prod_1733431204.76024.pdf#page=22) | REPORT | Mixed logistic/site/strata, with fixed treatment-only fallback; no row-specific interval versus test construction. |
| [DOC-001 p. 4, secondary methods and significance rule](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=4) | REPORT | Three analysis cohorts and two-sided P<.05 criterion. |
| [DOC-001 p. 5, matched neuropathy/hunger counts](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=5) | REPORT | Among participants with any symptom: neuropathy 6/57 versus 0/70 and hunger 6/111 versus 0/130; separately confirms outcome/population alignment. |
| [DOC-001 p. 6, continuation of intervention significance narrative](../../../jama_dupuis_2024_oi_240111_1733431204.38761.pdf#page=6) | REPORT | Symptom-specific intervention significantly more common for neuropathy/hunger among all participants and those with SSPedi≥1; matched symptomatic readings conflict with null-containing supplemental intervals. |

**Applicable consistency rule:** Route A category 1 for both occurrences of the same zero-control-event symptomatic-row pattern. An assumed Wald test is unnecessary: compare the supplied interval/null and P/threshold directly.

**Calculation/logical reproduction and precision:** Neuropathy .98<1<323.1 with .007<.05; hunger .9<1<288.74 with .009<.05. Neuropathy estimate interval [17.75,17.85], lower/upper-CI intervals [.975,.985]/[323.05,323.15], P [.0065,.0075]. Hunger estimate [16.075,16.085], lower/upper-CI intervals [.85,.95]/[288.735,288.745], P [.0085,.0095]. Both intervals contain 1 for every displayed-endpoint rounding combination, and both P intervals remain below .05. Relative discrepancy is not applicable to null-value decisions; category 1 is exempt from rounding screening. Percentage diagnostic checks: 100×6/57=10.526315… falls inside [10.45,10.55], and 100×6/111=5.405405… falls inside [5.35,5.45]; zero control counts yield exact 0%. Count/percentage gaps and relative discrepancies are zero. No modeled OR is compared against a crude ratio.

**Necessary inputs available:** Both printed matched numerator/denominator pairs, OR/CI/P combinations, report significance rule, cohort definitions and narrative. **Exact missing inputs/definitions:** The interval construction and test procedure used for each row, whether each pair came from identical fits/estimators, and row-level output/unrounded data sufficient to recreate those procedures. None is assumed.

**Source-grounded alternative:** Sparse-data intervals and tests can be obtained from different constructions or fits. The stated logistic fallback and event sparsity make this possible, but the supplied methods do not define the construction for either named row. No particular procedure is asserted or proposed.

**Direct observation versus inference:** Direct observations are both null-containing intervals, significant P values and the matched significant narrative. The explanation in terms of a particular interval/test pairing is an unestablished possibility. The two rows are consolidated because the same printed decision rule recurs, not because a common production cause has been proved.

**Determining recheck fact:** Both source-confirmed SSPedi≥1 symptom-specific rows have intervals containing 1 and P values below .05, persisting under every displayed-endpoint rounding interval.

**Remaining human question:** Which interval constructions and tests generated the neuropathy and hunger symptomatic-cohort contrasts, and how should their different interval/test null readings be interpreted?

**Classification reason:** Each supplemental CI/P pair is S_W, while its matched main-report significance interpretation versus that interval is S_C. S_C has precedence; both concern statistical results. No PLAN conflicts or mere corroborations are added as relationships.

## Confirmation assets and boundaries

New uniquely owned derivatives are below preprocessing/evidence_recheck/:

| Derivative | Direct source/command | Engine/device |
|---|---|---|
| main-direct-layout.txt | pdftotext -layout jama_dupuis_2024_oi_240111_1733431204.38761.pdf OUTPUT; complete 11-page REPORT corpus | Poppler 26.01.0 / CPU |
| report-direct-layout.txt | pdftotext -layout joi240111supp2_prod_1733431204.76024.pdf OUTPUT; complete 23-page REPORT corpus | Poppler 26.01.0 / CPU |
| plan-p11-12-direct-layout.txt | pdftotext -f 11 -l 12 -layout joi240111supp1_prod_1733431204.57929.pdf OUTPUT | Poppler 26.01.0 / CPU |
| plan-p31-39-direct-layout.txt | pdftotext -f 31 -l 39 -layout joi240111supp1_prod_1733431204.57929.pdf OUTPUT | Poppler 26.01.0 / CPU |
| plan-p12.png | pdftoppm -f 12 -l 12 -singlefile -r 110 -png joi240111supp1_prod_1733431204.57929.pdf PREFIX | Poppler 26.01.0 / CPU |
| plan-p37.png | pdftoppm -f 37 -l 37 -singlefile -r 110 -png joi240111supp1_prod_1733431204.57929.pdf PREFIX | Poppler 26.01.0 / CPU |

The current-run source-matched images preprocessing/inclusion_initial/main-p9.png, report-13.png, report-14.png, report-figure-20.png and report-figure-21.png were independently visually inspected as confirmation aids. Their source-page identity and alignment were cross-checked against fresh direct extraction. Their existing files were preserved. Searches/extracted text cannot establish absence outside the supplied corpus, and no such claim is made.

Covered IDs: C001, C002, C003, C004, C005, C006, C007. Evidence-state counts: reproduced 7; reproduced_after_transcription_correction 0; not_reproduced 0. Classification corrections: 0. All assigned exact source locations and all occurrences of the repeated patterns are confirmed. Remaining items are the seven stated human questions and their named missing analytic definitions/output; no scientific source-location confirmation gap remains.
