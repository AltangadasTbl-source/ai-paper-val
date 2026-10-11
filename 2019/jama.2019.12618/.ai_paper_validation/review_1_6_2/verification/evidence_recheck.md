# Workflow 1.6.2 Mechanical Evidence Recheck

Pending Human Adjudication. Evidence states below are mechanical evidence facts, not dispositions.

Runtime agent ID: `01a1296b-928f-7c80-a47c-146b970052e8`. Runtime task: `/root/evidence_recheck`. Model: `gpt-6.1-sol`; reasoning effort: `high`; start mode: `FRESH_SPAWN`. Exact assigned and completed stable-ID scope: C001, C002, C003, C004, C005, C006, C007, C008, C009. The current ledger and independent initial screen supplied the stable identities; every affected location was reread against supplied sources. START_PROMPT.md, QUALITY_CONTROL_SCOPE.md, the complete review contract, and report specification were read. No legacy selection or disposition artifact, external literature, sibling package, or web evidence was used.

## Source authority and confirmation method

Source PDFs are the authority. Existing text and page images were used first as locators and transcription aids. Direct Poppler `pdftotext -layout` 26.01.0 then reread the exact native-text source pages cited below. All physical pages of the main REPORT (10 pages), non-plan results REPORT supplement (16 pages), and administrative data-sharing REPORT (1 page) were inspected for the missing-output comparisons in C001, C003 and C004. The latter supplement contains access terms rather than numerical analysis outputs. The main article is a report of completed randomized-trial results; the results supplement contains eligibility context and reported eTables. Original/final SAP versions and the prospective Manual of Operation and Procedures are PLAN by content.

Full-page visual confirmation used current-run source-linked images of main p.6, results supplement p.15, and SAP pp.26, 27, 67 and 68. These display the actual table alignment, confidence-interval labels and formula symbols that plain text can lose. The source-linked reusable original-protocol p.15 and final-protocol p.80 images were inspected. To confirm the raster final definition directly with a recorded current engine, only protocol physical p.80 was newly rendered and visually reread, using CPU Poppler `pdftoppm` 26.01.0:

`pdftoppm -f 80 -l 80 -singlefile -scale-to 1800 -png joi190092supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/evidence_recheck/protocol_p080`

New derivative: `preprocessing/evidence_recheck/protocol_p080.png`; source: [final protocol — physical PDF p.80](../../../joi190092supp2_prod.pdf#page=80); engine: Poppler 26.01.0; compute device: CPU. No OCR, fallback environment, broad duplicate derivative extraction, or source/reused-asset modification was needed. Direct native extraction was read from standard output and created no additional file. Current-run confirmation images are `preprocessing/stat1_core/main_p006.png`, `preprocessing/results_mapping/supp1-page-015.png`, and `preprocessing/stat1_core/sap_p026.png`, `sap_p027.png`, `sap_p067.png`, `sap_p068.png`; reusable images were listed in the current evidence-asset inventory.

Independent arithmetic used JavaScript, with a Lanczos log-gamma evaluation and Simpson integration of the Student t and normal densities. These reproduce the supplied Welch test and the SAP's printed approximation; they do not introduce a preferred analysis. Integer participant counts retain their integer domain inside half-unit intervals. Absence statements below concern the complete supplied REPORT package, not whether an analysis was ever performed or published elsewhere.

## Recheck classification summary

| ID | Review domain | Primary relationship | All relationships | Evidence state | Classification or transcription change |
|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | reproduced | None |
| C002 | protocol_report | P_R | P_R | reproduced | None |
| C003 | protocol_report | P_R | P_R | reproduced | None; Route B and supplementary status retained |
| C004 | protocol_report | P_R | P_R | reproduced | None; nested Aim 2 primary designation retained |
| C005 | statistical_results | S_W | S_W | reproduced | None |
| C006 | protocol_report | P_R | P_R | reproduced | None |
| C007 | statistical_results | S_W | S_W | reproduced | None |
| C008 | plan_material | P_P | P_P | reproduced | None |
| C009 | plan_material | P_P | P_P | reproduced | None |

All nine states are `reproduced`; no assigned ID is deleted. Each candidate has only the stated relationship, so the precedence rule P_R > P_P > S_C > S_W selects that relationship without a tie. Repeated original/final passages corroborating the same planned requirement do not independently create P_P relationships. Agreement among REPORT locations does not create S_C or S_W conflicts within a P_R missing-output candidate.

## C001 — Planned anatomical relative-risk regression outputs are not reported

**Finding IDs:** F-XS-004. **Status:** Pending Human Adjudication.

**Location found and document role, separately for every affected location:**

| Exact supplied-source location | Role from content | Location found and matched content |
|---|---|---|
| [Original SAP p.17, Prespecified Subgroup Analysis](../../../joi190092supp3_prod.pdf#page=17) | PLAN | Yes; anatomical location by history is prespecified; relative risks in each substratum will also be reported using relative-risk regression. |
| [Final SAP p.58, same subgroup section](../../../joi190092supp3_prod.pdf#page=58) | PLAN | Yes; repeats the regression-RR reporting commitment. |
| [Main p.1, abstract anatomical results](../../../jama_rathinam_2019_oi_190092.pdf#page=1) | REPORT | Yes; the two anatomical success results are reported as percentages, risk differences and ORs. |
| [Main p.4, anatomical analysis methods](../../../jama_rathinam_2019_oi_190092.pdf#page=4) | REPORT | Yes; the primary logistic regression is used for this subanalysis. |
| [Main p.5, posterior/panuveitis narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=5) | REPORT | Yes; 74.4% versus 55.3%, RD 19.1%, OR 2.35 and interaction P=.004. |
| [Main p.6, Table 2 and intermediate narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=6) | REPORT | Yes; intermediate 6/18 versus 14/22, posterior/pan 58/78 versus 42/76, with ORs and RDs. |
| [Results supplement p.1, contents](../../../joi190092supp1_prod.pdf#page=1) | REPORT | Yes; all listed eTables were inspected through p.16; no anatomical regression-RR output is present. |

**Source value/text matched:** Yes. Both plans print “We will also report relative risks in each substratum, using relative risk regression.” The history-based anatomical split is designated prespecified.

**Comparator matched:** Yes. The intermediate OR is 0.29 (95% CI 0.08–1.05), RD −30.3% (−51.6% to 1.1%); posterior/pan OR is 2.35 (1.16–4.90), RD 19.1% (3.6% to 30.6%). The report does not label these ORs as RRs and supplies no separate regression-RR result in its complete output set.

**Consistency rule applicable:** Yes; focus D, Route A category 5, a planned key-secondary analysis not reported. The anatomical results appear in the abstract and therefore satisfy the scope's key-secondary definition. The article's exploratory interpretation of secondary analyses does not itself supply the promised effect measure.

**Calculation or logical comparison reproduced:** Yes. The effect-measure matching rule distinguishes OR, RD and regression RR. Every supplied anatomical effect output was matched to the planned split; none supplies the additional regression-RR estimate or interval. A crude RR from counts is not substituted for an unreported model-based RR. **Display-precision interval check:** Not applicable to the absence of a specified analysis/effect measure; no numeric discrepancy is asserted between unlike effect measures.

**Necessary inputs available:** Yes for the observed reporting comparison: both exact planned commitments, the named subgroup definition, and the complete supplied REPORT outputs. **Exact missing inputs or definitions:** The promised RR model output, its estimate/CI and covariate specification as implemented; any supplied amendment replacing that commitment or another publication containing the result is absent. Participant data cannot be used to infer it from this package.

**Source-grounded alternative interpretation:** The RR output may have been considered redundant, reserved for a later report, or changed by an unsupplied amendment. None is identified in the supplied report. ORs and RDs are coherent as their stated quantities; this candidate does not challenge them through a crude-ratio comparison.

**Direct observation versus inferred explanation:** Direct: the two plans promise regression RRs, while the complete supplied report gives other effect measures and no such RRs. No explanation of the omission, unperformed-analysis claim, or treatment-effect change is inferred.

**Exact remaining human question:** Where are the planned relative-risk regression estimates and intervals for each anatomical subgroup, or which supplied amendment changes that analysis commitment?

**Classification confirmed:** `protocol_report`; primary `P_R`; all relationships `P_R`; PLAN original/final SAP versus REPORT main/results supplement. The comparison is of a plan specification and report outputs, not a conflict between the two agreeing plan versions or between agreeing report displays. **Classification ambiguity:** An unsupplied reporting amendment or later report remains possible. **Classification correction:** None.

**Evidence state:** `reproduced`. **Determining recheck fact:** The exact RR reporting commitments occur in both SAP versions, and the complete supplied REPORT contains no anatomical relative-risk regression output.

## C002 — Primary success composite differs in its late-injection component

**Finding IDs:** F-XS-101. **Status:** Pending Human Adjudication.

**Location found and document role, separately for every affected location:**

| Exact supplied-source location | Role from content | Location found and matched content |
|---|---|---|
| [Final protocol p.80, §2.5.1](../../../joi190092supp2_prod.pdf#page=80) | PLAN | Yes; direct CPU rendering confirms the no-periocular/intravitreal-injection-after-first-90-days success component. |
| [Main p.3, Treatment and Outcomes](../../../jama_rathinam_2019_oi_190092.pdf#page=3) | REPORT | Yes; explicit three-part success definition and efficacy-failure definition; other injections are protocol deviations. |
| [Main p.4, primary analysis](../../../jama_rathinam_2019_oi_190092.pdf#page=4) | REPORT | Yes; month-6 visits or early failures are included according to randomization. |
| [Main p.6, late-injection narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=6) | REPORT | Yes; four patients in each arm received injections beyond 90 days. |
| [Final SAP p.70, §3.5.1](../../../joi190092supp3_prod.pdf#page=70) | PLAN | Yes; injection-time inflammation is explicitly a sensitivity analysis. |
| [SAP p.81, injection amendment](../../../joi190092supp3_prod.pdf#page=81) | PLAN | Yes; repeats the new injection sensitivity section and major-deviation addition. |

**Source value/text matched:** Yes. Final protocol §2.5.1 requires no periocular or intravitreal corticosteroid injection after the first 90 follow-up days, alongside controlled inflammation, prednisone/topical-steroid limits and prior safety/tolerability/futility failure restrictions.

**Comparator matched:** Yes. Main p.3 lists inflammation control, oral/topical steroid limits and no declared safety/intolerability failure. It defines efficacy failure through the first two criteria and classifies other injections as deviations. Main p.6 gives four exposed patients per treatment arm. The SAP sensitivity considers the injection-time inflammation: uncontrolled inflammation means failure, while meeting success criteria means success.

**Consistency rule applicable:** Yes; focus D, Route A category 5, a changed/unequally specified composite component. This is the primary endpoint's complete definition, not a procedural or peripheral comparison.

**Calculation or logical comparison reproduced:** Yes. The final PLAN success composite expressly contains the no-late-injection component; the REPORT's enumerated success/failure definition does not. A deviation label does not state the primary outcome classification. The SAP alternative is explicitly a sensitivity estimand, so it does not demonstrate a disclosed replacement primary definition. **Display-precision interval check:** Not applicable to the membership of a logical composite. Ninety days is a decision window and four per arm is a discrete observed count, not the basis of a numeric mismatch. No primary numerator is recalculated.

**Necessary inputs available:** Yes for the definition comparison and existence of eight exposed patients. **Exact missing inputs or definitions:** Each exposed patient's primary outcome status, injection date/reason, month-6 inflammation/steroid status, and which complete endpoint algorithm generated 64/96 and 56/98. The package does not identify an amendment removing the final component.

**Source-grounded alternative interpretation:** The final component may have been applied but omitted from the report's abbreviated definition, or another definition may have generated the counts. The injection-time sensitivity rule is another possible classification for these patients. The [original protocol p.15](../../../joi190092supp2_prod.pdf#page=15), inspected visually, lacks the late-injection component, so version selection is relevant; it does not establish the version used for the reported counts.

**Direct observation versus inferred explanation:** Direct: the two printed primary definitions differ in an explicit component, eight patients had the relevant exposure, and the sensitivity rule differs in purpose. No change to a success count, significance, or actual patient classification is inferred.

**Exact remaining human question:** For the eight patients receiving injections after 90 days, did the six-month primary analysis classify them as failures under final protocol §2.5.1, use their month-6 inflammation/steroid status, or use the SAP injection-time sensitivity rule; and which complete definition generated 64/96 and 56/98?

**Classification confirmed:** `protocol_report`; primary `P_R`; all relationships `P_R`; PLAN final protocol versus REPORT main. The SAP passages explain a separate sensitivity and do not create a second plan-only conflict. The historical original definition is an alternative/version locator, not a separately registered P_P inconsistency. **Classification ambiguity:** Applied definition/version and any undisclosed amendment remain unresolved. **Classification correction:** None.

**Evidence state:** `reproduced`. **Determining recheck fact:** The final protocol's directly rendered primary composite contains the late-injection component, and the report's explicit primary definition omits it while reporting eight late-injection patients.

## C003 — Prespecified primary-endpoint robustness outputs are not reported

**Finding IDs:** F-XS-003. **Status:** Pending Human Adjudication.

**Location found and document role, separately for every affected location:**

| Exact supplied-source location | Role from content | Location found and matched content |
|---|---|---|
| [Original SAP p.22, §3.3.1](../../../joi190092supp3_prod.pdf#page=22) | PLAN | Yes; lost-followup treatment effect needed to change the main test will be determined. |
| [Original SAP p.28, §3.5](../../../joi190092supp3_prod.pdf#page=28) | PLAN | Yes; all four missing-data methods will be reported; complete cases are primary and other analyses supplementary. |
| [Original SAP p.29, continuation](../../../joi190092supp3_prod.pdf#page=29) | PLAN | Yes; longitudinal success model details and reporting of additional modeling are described. |
| [Final SAP p.62, §3.3.1](../../../joi190092supp3_prod.pdf#page=62) | PLAN | Yes; repeats the lost-followup sensitivity commitment. |
| [Final SAP p.68, §3.5 introduction](../../../joi190092supp3_prod.pdf#page=68) | PLAN | Yes; robustness purpose and primary six-month endpoint are stated. |
| [Final SAP p.69, four methods and continuation](../../../joi190092supp3_prod.pdf#page=69) | PLAN | Yes; four-method reporting list, supplementary status and longitudinal model structure recur. |
| [Final SAP p.70, §3.5.1](../../../joi190092supp3_prod.pdf#page=70) | PLAN | Yes; late-injection primary-outcome sensitivity is defined by injection-time inflammation. |
| [SAP p.81, injection revision](../../../joi190092supp3_prod.pdf#page=81) | PLAN | Yes; explicitly adds the injection sensitivity section. |
| [Main p.4, Statistical Analyses](../../../jama_rathinam_2019_oi_190092.pdf#page=4) | REPORT | Yes; complete-case analysis and multiple imputation are identified. |
| [Main p.6, injection and sensitivity narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=6) | REPORT | Yes; eight late-injection patients, geographic sensitivity and adherence sensitivity are described. |
| [Main p.7, Figure 2 and MI result](../../../jama_rathinam_2019_oi_190092.pdf#page=7) | REPORT | Yes; primary/site/per-protocol models and the MI result appear; none of the registered missing outputs appears. |
| [Results supplement p.1, contents](../../../joi190092supp1_prod.pdf#page=1) | REPORT | Yes; complete p.1–16 results set inspected; eTable 7 is homogeneity testing, not the absent missingness/injection outputs. |

**Source value/text matched:** Yes. Original p.28/final p.69 propose reporting all four methods: regression MI; longitudinal GLMM with visit/person/eye-within-person structure; assigned missing-success/failure sensitivity; complete cases. They explicitly designate complete cases primary and all other analyses supplementary. Original p.22/final p.62 promise the lost-followup tipping-point assessment. Final p.70/p.81 define the added injection sensitivity.

**Comparator matched:** Yes. Main complete-case OR 1.50 (0.81–2.81), P=.20, and MI OR 1.4 (0.8–2.4), P=.27, are present. Geographic and adherence sensitivities are reported. No supplied REPORT result gives the longitudinal GLMM, missing-success/failure assignment, lost-followup tipping point, or injection-time sensitivity.

**Consistency rule applicable:** Yes; focus D and the independent screen's final **Route B** rationale. The definite reporting commitment concerns supplementary analyses of the named primary endpoint. Supplementary status is retained; the checker provenance's broader Route A label does not redefine these as a separate primary endpoint or create a status-change claim.

**Calculation or logical comparison reproduced:** Yes. The four-member promised missing-data list was compared with the complete REPORT set; complete cases and MI are found, while the two other list members and the additional tipping-point/injection sensitivities are not. The affected result is the robustness of six-month primary OR 1.50/P=.20 under the specified assumptions. Other secondary endpoints explicitly deferred by the article do not identify these outputs. **Display-precision interval check:** Not applicable to a missing specified output or reporting commitment; no direction or significance of an absent result is calculated.

**Necessary inputs available:** Yes for identifying the endpoint, promised analyses, their supplementary designation and the complete supplied output set. **Exact missing inputs or definitions:** Longitudinal, assigned-outcome, tipping-point and injection-time results; any amendment changing their reporting; participant-level missingness and injection classifications needed to derive them. The review does not attempt their reconstruction.

**Source-grounded alternative interpretation:** These supplementary analyses may be reported elsewhere, intentionally omitted, amended outside the supplied package, or not performed. The package does not decide among these explanations. No claim of failed robustness follows from absence.

**Direct observation versus inferred explanation:** Direct: an explicit reporting promise and a narrower supplied output set. No unperformed-analysis claim, changed treatment effect, or model implementation is inferred. C002 concerns the primary composite definition; C003's injection component concerns an independently specified sensitivity output.

**Exact remaining human question:** Where are the prespecified longitudinal, missing-success/failure, lost-followup tipping-point and injection-time primary-success analyses, or what supplied amendment changes their reporting plan?

**Classification confirmed:** `protocol_report`; primary `P_R`; all relationships `P_R`; PLAN original/final SAP versus REPORT main/results supplement. Both plan versions corroborate the same missing-data commitment, and agreeing report sources corroborate the absence; neither agreement creates another relationship. **Classification ambiguity:** Scope of publication versus another report remains unresolved; supplementary status is explicit and preserved. **Classification correction:** None.

**Evidence state:** `reproduced`. **Determining recheck fact:** All exact reporting commitments remain present, supplementary status is confirmed, and the four named robustness outputs are absent from the complete supplied REPORT package.

## C004 — Planned rescue primary model and individual confidence intervals are not reported

**Finding IDs:** F-XS-002. **Status:** Pending Human Adjudication.

**Location found and document role, separately for every affected location:**

| Exact supplied-source location | Role from content | Location found and matched content |
|---|---|---|
| [Original SAP p.21, §3.2.3](../../../joi190092supp3_prod.pdf#page=21) | PLAN | Yes; primary rescue logistic model includes treatment and first-drug failure reason; success-rate CIs will be presented regardless of the test result. |
| [Original SAP p.25, Specific Aim 2](../../../joi190092supp3_prod.pdf#page=25) | PLAN | Yes; the two individual success-probability estimates with 95% CIs are expressly called primary analyses. |
| [Final SAP p.61, §3.2.3](../../../joi190092supp3_prod.pdf#page=61) | PLAN | Yes; repeats the treatment/failure-reason primary model; continuation follows p.62. |
| [Final SAP p.62, reporting continuation](../../../joi190092supp3_prod.pdf#page=62) | PLAN | Yes; success rates and CIs regardless of test result, plus group-specific 95% CI reporting. |
| [Final SAP p.66, Specific Aim 2](../../../joi190092supp3_prod.pdf#page=66) | PLAN | Yes; repeats the two primary probability/CI estimates and reporting by first-drug failure category. |
| [Main p.4, twelve-month model statement](../../../jama_rathinam_2019_oi_190092.pdf#page=4) | REPORT | Yes; the same primary logistic model is applied at 12 months. |
| [Main p.6, Table 2 switching row and footnote b](../../../jama_rathinam_2019_oi_190092.pdf#page=6) | REPORT | Yes; treatment fixed/site random model is printed, with group proportions and between-group OR/RD CIs. |
| [Main p.7, Prespecified 12-Month Outcomes](../../../jama_rathinam_2019_oi_190092.pdf#page=7) | REPORT | Yes; rescue success proportions and the between-group comparison recur. |
| [Results supplement p.1, contents](../../../joi190092supp1_prod.pdf#page=1) | REPORT | Yes; complete p.1–16 contents inspected; no individual rescue-success CI or failure-reason-adjusted rescue output appears. |

**Source value/text matched:** Yes. The SAP includes reason for initial failure, specifically efficacy versus any other reason, in the primary rescue logistic model. Both versions promise the two individual rescue success probabilities and 95% CIs, irrespective of the comparison test; the Aim 2 sample-size section calls these primary analyses.

**Comparator matched:** Yes. The report explicitly describes treatment fixed/site random for its primary model and reuses that model at 12 months. Its switching comparison prints 20/29 (69%) versus 7/20 (35%), RD 34.2% (6.6%–52.6%), OR 4.17 (1.32–13.16), P=.02. Main p.7 rounds the same OR to 4.2 (1.3–13.2). Neither RD nor OR CI is an individual success-probability CI, and no separately identified failure-reason-adjusted estimate appears.

**Consistency rule applicable:** Yes; focus D, Route A category 5, a specified primary analysis within Aim 2 replaced or unreported. The [final protocol p.72](../../../joi190092supp2_prod.pdf#page=72) explicitly uses the same primary/secondary outcomes for Aim 2; [p.73](../../../joi190092supp2_prod.pdf#page=73) lists rescue success as secondary in the overall trial. Both are PLAN. These are nested designations, so this candidate asserts no changed trial-wide outcome status.

**Calculation or logical comparison reproduced:** Yes. The planned primary predictor list and named outputs were matched to the report's stated model and all output displays. A treatment/site model does not identify the planned failure-reason term. Between-group CIs do not provide either group's probability CI. This is a reported specification/output comparison, not proof of the fitted model's actual internal formula. **Display-precision interval check:** Not applicable to omitted covariate/output identity. Rounding of OR 4.17 to 4.2 reconciles and is not part of the registered issue. No adjusted CI is calculated from aggregate counts.

**Necessary inputs available:** Yes for the exact plan/report specifications, nested hierarchy and displayed outputs. **Exact missing inputs or definitions:** The implemented rescue formula and failure-reason-adjusted model output; each rescue probability's CI and planned failure-reason breakdown; any reporting amendment. Aggregate counts alone do not supply those model outputs.

**Source-grounded alternative interpretation:** The model may have included failure reason without the report saying so, or the report may intentionally display a distinct secondary comparison. The specified outputs may exist in another report. Even a hidden failure-reason term would not supply the absent individual probability CIs in this package.

**Direct observation versus inferred explanation:** Direct: the printed planned and reported models differ in the named failure-reason term, and the planned individual CIs are absent. No actual fitted-covariate omission, altered trial-wide hierarchy, or result direction is inferred.

**Exact remaining human question:** Was the SAP primary rescue analysis with first-drug failure reason performed, and where are its adjusted results and the two prespecified individual rescue-success 95% CIs?

**Classification confirmed:** `protocol_report`; primary `P_R`; all relationships `P_R`; PLAN SAP versus REPORT main/results supplement. Protocol hierarchy passages corroborate the nested design and do not form another conflict. **Classification ambiguity:** Implementation may be incompletely described; primary is within Aim 2, while overall-trial rescue outcome status is secondary. **Classification correction:** None.

**Evidence state:** `reproduced`. **Determining recheck fact:** The directly read nested primary specification includes failure reason and two individual probability CIs; the supplied report identifies neither the planned adjusted result nor those CIs.

## C005 — Adherence summary inputs do not reproduce the printed Welch P value

**Finding IDs:** F-ST1-001. **Status:** Pending Human Adjudication.

**Location found and document role, separately for every affected location:**

| Exact supplied-source location | Role from content | Location found and matched content |
|---|---|---|
| [Main p.4, Statistical Analyses](../../../jama_rathinam_2019_oi_190092.pdf#page=4) | REPORT | Yes; missed doses are compared by Welch t test; two-sided P<.05 is declared significant. |
| [Main p.6, Table 2 missed-dose row and headings](../../../jama_rathinam_2019_oi_190092.pdf#page=6) | REPORT | Yes; mean (SD), %, 4.6 (1.0) versus 4.3 (0.5), P=.87 under n=96/98 headings. |
| [Main p.6, missed-dose narrative and dose-definition footnote](../../../jama_rathinam_2019_oi_190092.pdf#page=6) | REPORT | Yes; the narrative repeats these values; footnote j defines missed over expected doses throughout enrollment. |
| [Main p.7, Figure 2 per-protocol row/footnote e](../../../jama_rathinam_2019_oi_190092.pdf#page=7) | REPORT | Yes; 90/94 patients in the less-than-20%-missed-dose analysis; this is a diagnostic population locator, not an exact descriptive-row n. |

**Source value/text matched:** Yes. The stated test is Welch, and the printed summary label is SD. Means 4.6%/4.3%, SDs 1.0%/0.5% and P=.87 agree between table and narrative. The full-page image confirms the columns and decimals.

**Comparator matched:** Yes. The table's patient headings give 96 and 98; no separate adherence-only n or alternative test/scale is specified at these locations. Figure 2 establishes a substantial measured-adherence population but does not establish the exact sample used for the descriptive row.

**Consistency rule applicable:** Yes; focus B/C and Route B, the displayed summary/test pairing. The computation applies the named test to the displayed patient populations, with missing exact adherence-only n made explicit. It does not treat an assumed Wald test or a crude/model comparison as a source method.

**Calculation reproduced:** Yes. Welch t=(4.6−4.3)/sqrt(1.0²/96+0.5²/98)=2.634450202; Welch–Satterthwaite df=139.060070485; independent two-sided Student t integration yields P=.009382747. Converting percentage points to proportions leaves the test unchanged.

**Display-precision interval check reproduced:** Means allow [4.55,4.65] and [4.25,4.35]; SDs allow [.95,1.05] and [.45,.55]. Thus the mean difference is [.20,.40], and the maximum standard error at integer n=96/98 is sqrt(1.05²/96+.55²/98)=.120710852, giving t≥1.656851868. Welch df≥min(95,97)=95. A deliberately conservative recomputed P enclosure is [0,.100848629]. Printed P=.87 permits [.865,.875]. The gap is at least .764151371, relative discrepancy at least .764151371/.87=.878334910, above .05. Using 90/94 only as a population diagnostic gives conservative P≤.111356271, still far from the printed interval; it does not establish the exact tested n. Count half-unit intervals retain exactly the displayed integer n values.

**Necessary inputs available:** Yes for the stated-test/displayed-population calculation and its rounding bounds. **Exact missing inputs or definitions:** Actual adherence-only participant counts; participant-level dose records; whether dispersion is actually SD; any transformation or distinct test population; original Welch output. The recheck cannot identify the actual test inputs from these aggregate summaries.

**Source-grounded alternative interpretation:** A separately restricted population, transformed adherence variable, other dispersion statistic or different test could explain the pairing. Treating 1.0/.5 as standard errors would instead produce a different variability quantity and a diagnostic large-df two-sided P≈.788, not .87. No such alternate definition is printed.

**Direct observation versus inferred explanation:** Direct: the named Welch procedure and printed summary/population inputs do not reproduce the printed P, even allowing rounding. The actual adherence sample, which printed component requires clarification, and a production mechanism are not inferred.

**Exact remaining human question:** What participant counts, summary-dispersion definition and original test output produced the missed-dose P=.87, and how do those inputs correspond to the printed mean (SD) percentages and table populations?

**Classification confirmed:** `statistical_results`; primary `S_W`; all relationships `S_W`; every compared location is in the same REPORT main article. The issue concerns summary/test logic, not which endpoint a result belongs to. A plan is not a conflicting comparator. **Classification ambiguity:** Exact adherence-only n and implemented summary/test definitions are unreported. **Classification correction:** None.

**Evidence state:** `reproduced`. **Determining recheck fact:** Direct-source SD/mean/P/test transcriptions match the ledger, and the supplied Welch inputs and conservative display-precision P enclosure exclude the printed P interval. This fact is bounded to the displayed pairing rather than a claim to know the actual underlying analysis sample.

## C006 — Reported per-protocol adherence cutoff differs from the planned cutoff

**Finding IDs:** F-XS-001. **Status:** Pending Human Adjudication.

**Location found and document role, separately for every affected location:**

| Exact supplied-source location | Role from content | Location found and matched content |
|---|---|---|
| [Original SAP p.31, §4.1](../../../joi190092supp3_prod.pdf#page=31) | PLAN | Yes; per-protocol excludes major deviations or noncompliance below 50% received. |
| [Final SAP p.71, §4.1](../../../joi190092supp3_prod.pdf#page=71) | PLAN | Yes; repeats the 50%-received rule. |
| [Final SAP p.72, §4.2](../../../joi190092supp3_prod.pdf#page=72) | PLAN | Yes; major-deviation examples include late injections; no 80%-received threshold is introduced. |
| [Main p.6, sensitivity narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=6) | REPORT | Yes; patients missing less than 20% of doses are included. |
| [Main p.7, Figure 2 model 4 and footnote e](../../../jama_rathinam_2019_oi_190092.pdf#page=7) | REPORT | Yes; “Per protocol,” 61/90 versus 54/94, n=184, OR 1.56 (.84–2.96), P=.17, and the same less-than-20%-missed rule. |

**Source value/text matched:** Yes. Both SAP versions define noncompliance as less than 50% of study drug received by self-report or pill counts, and exclude major deviations.

**Comparator matched:** Yes. The report's less-than-20%-missed criterion means more than 80% received; Figure 2 calls that primary-outcome sensitivity per protocol and gives the exact reported result above.

**Consistency rule applicable:** Yes; focus D, Route B. These are numeric primary-sensitivity analysis-population criteria, not immediately equivalent population terminology or a peripheral time-point contributor-count difference.

**Calculation or logical comparison reproduced:** Yes. The plan retains adherence of at least 50%, subject to deviations, while the stated report criterion retains more than 80%. Their treatment of the 50%–80% region differs. No aggregate membership change is claimed. **Display-precision interval check:** The thresholds are exact decision cutoffs; rounding cannot alter their rule identity. Conservatively allowing half-unit intervals for 50 and derived 80 gives [49.5,50.5] versus [79.5,80.5], gap 29 percentage points, relative gap 29/50=.58, above .05. Treating the 20%-missed threshold as [19.5,20.5] yields the same [79.5,80.5] received interval.

**Necessary inputs available:** Yes for the rule comparison and reported sensitivity estimate/population totals. **Exact missing inputs or definitions:** Patient-level adherence, major-deviation flags, and the actually applied filters; an amendment introducing the stricter criterion. Aggregate 90/94 counts cannot identify the planned population. Lack of a reported major-deviation filter is not an additional registered issue by itself.

**Source-grounded alternative interpretation:** This may be a stricter additional sensitivity labeled per protocol, or reflect an unsupplied amendment. The printed labels and thresholds alone do not identify its relation to the planned population.

**Direct observation versus inferred explanation:** Direct: the planned and reported adherence decision thresholds differ. No known patient inclusion/exclusion, change to OR/P, or actual major-deviation filter is inferred.

**Exact remaining human question:** Which adherence and major-deviation criteria produced Figure 2's per-protocol analysis, and how does that population relate to the SAP-defined per-protocol population?

**Classification confirmed:** `protocol_report`; primary `P_R`; all relationships `P_R`; PLAN original/final SAP versus REPORT main. The two plans agree and the report text/figure agree, so neither side adds a separate internal relationship. **Classification ambiguity:** A stricter supplemental analysis or unsupplied amendment is possible. **Classification correction:** None.

**Evidence state:** `reproduced`. **Determining recheck fact:** Exact source readings preserve the 50%-received versus less-than-20%-missed difference and its link to the named primary-sensitivity result.

## C007 — Switching-group serious diarrhea percentage does not reconcile

**Finding IDs:** F-NUM-001. **Status:** Pending Human Adjudication.

**Location found and document role, separately for every affected location:**

| Exact supplied-source location | Role from content | Location found and matched content |
|---|---|---|
| [Results supplement p.15, eTable 9 MMF column heading](../../../joi190092supp1_prod.pdf#page=15) | REPORT | Yes; N=20; number of patients reporting at least one event (%). |
| [Results supplement p.15, Serious Systemic → Diarrhea, MMF](../../../joi190092supp1_prod.pdf#page=15) | REPORT | Yes; 1 (3.4), visually aligned under N=20. |
| [Results supplement p.15, MMF low hemoglobin, allergic reaction and fever](../../../joi190092supp1_prod.pdf#page=15) | REPORT | Yes; each prints 1 (5.0) under the same N=20 heading. |
| [Results supplement p.15, methotrexate heading and serious systemic rows](../../../joi190092supp1_prod.pdf#page=15) | REPORT | Yes; adjacent N=29, diarrhea 0 (0.0), fatigue 1 (3.4). |
| [Results supplement p.16, eTable 9 footnote b](../../../joi190092supp1_prod.pdf#page=16) | REPORT | Yes; drug-related serious adverse events are due to diarrhea and fatigue; no row-specific denominator is given. |

**Source value/text matched:** Yes. Direct native text and full-page visual inspection agree on MMF N=20 and serious diarrhea 1 (3.4%). The row counts patients, not event episodes.

**Comparator matched:** Yes. Three other one-patient rows in the same MMF column give 5.0%; the adjacent methotrexate denominator is 29 and its one-patient serious fatigue entry gives 3.4%. The attribution footnote supplies no alternate MMF population.

**Consistency rule applicable:** Yes; focus A and Route A category 3, count/denominator/percentage within one display. Category 4 also describes the same-column reproduction pattern. This is not a peripheral comparison between separate safety displays.

**Calculation reproduced:** Yes. 100×1/20=5.0%. The other three one-patient MMF entries reproduce this ratio. **Display-precision interval check:** Count [0.5,1.5] and denominator [19.5,20.5] admit only integers 1 and 20, so the recomputed percentage interval is [5.0,5.0]. Printed 3.4% permits [3.35,3.45]. Gap=1.55 percentage points; relative discrepancy=1.55/3.4=.455882353, above .05. The alternative 100×1/29=3.448275862% lies in the printed interval, but 29 belongs to the other column. It is not substituted as the final denominator.

**Necessary inputs available:** Yes; displayed count, integer denominator, percentage, unit and same-display comparators. **Exact missing inputs or definitions:** Any diarrhea-specific population, alternate event attribution, or actual denominator differing from the column heading. Participant-level safety data are not supplied.

**Source-grounded alternative interpretation:** The percentage may reference the adjacent N=29 population or another unstated row population. Source clarification would be required for either reading. The arithmetic match to 29 identifies an alternative denominator, not a known production mechanism.

**Direct observation versus inferred explanation:** Direct: 1, 20 and 3.4% do not reconcile under the display-precision rule. No transposition mechanism, treatment reassignment or final corrected percentage is inferred.

**Exact remaining human question:** For eTable 9 serious systemic diarrhea in the MMF N=20 column, which event count, denominator and percentage should be used, and does the row use a population different from the printed column population?

**Classification confirmed:** `statistical_results`; primary `S_W`; all relationships `S_W`; the conflicting count/percentage and denominator are in one non-plan REPORT supplement. Footnote p.16 is in that same document and corroborates attribution rather than introducing another relationship. **Classification ambiguity:** A row-specific denominator is possible but unidentified. **Classification correction:** None.

**Evidence state:** `reproduced`. **Determining recheck fact:** Exact aligned source values remain 1 (3.4%) under N=20, with a reproduced interval gap above the threshold.

## C008 — Rescue power table sequence sizes differ from planned availability

**Finding IDs:** F-ST1-002. **Status:** Pending Human Adjudication.

**Location found and document role, separately for every affected location:**

| Exact supplied-source location | Role from content | Location found and matched content |
|---|---|---|
| [Original SAP p.25, Aim 2 planning/coding](../../../joi190092supp3_prod.pdf#page=25) | PLAN | Yes; primary probability-estimation aim and A/B rescue coding begin here. |
| [Original SAP p.26, inputs, availability and n0/n1](../../../joi190092supp3_prod.pdf#page=26) | PLAN | Yes; A initial success 60%, B 40%; B/A 58.3/55.4, A/B 38.9/36.9; rounding down to n1=58/n0=38. |
| [Original SAP p.27, Power Table for Specific Aim 2](../../../joi190092supp3_prod.pdf#page=27) | PLAN | Yes; A→B column is 58 and B→A is 38 in the main scenario. All seven scenario rows and their shared headings were inspected. |
| [Final SAP p.66, repeated Aim 2 planning/coding](../../../joi190092supp3_prod.pdf#page=66) | PLAN | Yes; repeats the primary aim, sequence coding and input assumptions. |
| [Final SAP p.67, availability and power-table headings](../../../joi190092supp3_prod.pdf#page=67) | PLAN | Yes; repeats availability 58.3/38.9, n1/n0, and opposite sequence-column headings. |
| [Final SAP p.68, seven power rows](../../../joi190092supp3_prod.pdf#page=68) | PLAN | Yes; repeats 58/38 main-scenario allocation under those headings. |

**Source value/text matched:** Yes. N0=108 per initial arm, initial retention .9, initial success A=.60/B=.40, rescue retention .95. Availability table B/A expected enrollment 58.3 and completion 55.4; A/B enrollment 38.9 and completion 36.9. The formula, integer rounding-down narrative and table labels were confirmed visually.

**Comparator matched:** Yes. In both versions the next table's first sequence column is Drug A then Drug B, with 58 in the main scenario; second is Drug B then Drug A, with 38. The 80% .42/.17 row uses the same sizes/headings. Other rows intentionally vary counts or success fractions and inherit those labels; their intentional changes are not independently registered discrepancies.

**Consistency rule applicable:** Yes; focus C/D and Route B. These are primary Aim 2 sample-size/power inputs; the scope exception for primary analysis populations applies. The comparison is the sequence-to-size mapping, not a peripheral heading or distinction between expected enrollment and expected completion.

**Calculation reproduced:** Yes. B→A enrollment=108×.9×(1−.4)=58.32, completion=58.32×.95=55.404. A→B enrollment=108×.9×(1−.6)=38.88, completion=38.88×.95=36.936. These reproduce the availability display. Rounding down gives 58 and 38 for those same respective sequences, while the next display assigns them to the opposite sequence headings.

**Display-precision interval check reproduced:** For A→B, availability 38.9 permits [38.85,38.95] and printed table 58 permits [57.5,58.5]; gap=18.55 and relative gap=18.55/38.9=.476863753. For B→A, 58.3 permits [58.25,58.35] and 38 permits [37.5,38.5]; gap=19.75 and relative gap=19.75/58.3=.338765009. Both exceed .05. Explicit rounding down of expectations explains the integer magnitude within each correctly retained sequence, not reversal of sequence identity. Initial success/retention values are stated planning assumptions; the key numeric check compares the displayed availability and power-table copies for the same named sequence.

**Necessary inputs available:** Yes for the availability arithmetic, sequence labels, rounding step and table assignments. **Exact missing inputs or definitions:** A transition dictionary connecting A/B, n0/n1 and drug-specific p0/p1 across the availability and power displays. No changed coding is stated. Actual rescue counts are irrelevant to reproducing this planned-input discrepancy.

**Source-grounded alternative interpretation:** A/B may have been recoded between displays, or the power headings may use a different unstated sequence mapping. Swapping entire treatment distributions is mathematically different from swapping only n while retaining its p. The package does not identify the intended transition, so no preferred mapping or revised power is assigned.

**Direct observation versus inferred explanation:** Direct: the same printed sequence is paired with different main-scenario sizes in adjacent plan displays in both versions. No production mechanism or change to actual trial recruitment/results is inferred.

**Exact remaining human question:** Which initial→rescue sequence corresponds to 58 versus 38 patients in the main Aim 2 power scenario, and how were the table's A/B labels matched to n0/n1 and p0/p1?

**Classification confirmed:** `plan_material`; primary `P_P`; all relationships `P_P`. Every compared location is in the prospective SAP, even though supplied as a supplement; original/final versions form one bound PLAN source and one repeated pattern. REPORT is not a conflicting comparator. **Classification ambiguity:** Unstated coding transition remains possible. **Classification correction:** None.

**Evidence state:** `reproduced`. **Determining recheck fact:** Both versions directly show B/A 58.3 and A/B 38.9 availability, then A→B 58 and B→A 38 power-table allocation beyond display precision.

## C009 — Printed detectable rescue difference does not reconcile with probability inputs

**Finding IDs:** F-ST1-003. **Status:** Pending Human Adjudication.

**Location found and document role, separately for every affected location:**

| Exact supplied-source location | Role from content | Location found and matched content |
|---|---|---|
| [Original SAP p.26, source power formula and definitions](../../../joi190092supp3_prod.pdf#page=26) | PLAN | Yes; normal-CDF formula includes absolute probability difference and variance terms with n0/n1; n1=58/n0=38. |
| [Original SAP p.27, opening sentence](../../../joi190092supp3_prod.pdf#page=27) | PLAN | Yes; approximately 80% power to detect a difference of 17%, with MMF success .42. |
| [Original SAP p.27, probability table and summary](../../../joi190092supp3_prod.pdf#page=27) | PLAN | Yes; .42/.17 row is 80%; following summary states a 25% difference. |
| [Final SAP p.67, formula, definitions and 17% sentence](../../../joi190092supp3_prod.pdf#page=67) | PLAN | Yes; exact repeated formula and sentence confirmed visually. |
| [Final SAP p.68, probability rows and 25% summary](../../../joi190092supp3_prod.pdf#page=68) | PLAN | Yes; same .42/.17/80% row and 25% summary. |

**Source value/text matched:** Yes. Both versions explicitly call 17% a detectable difference, with MMF rescue success probability .42 and approximately 80% power. The visually read formula is Phi(abs(p1−p0)/sqrt[p0(1−p0)/n0+p1(1−p1)/n1]−z(alpha/2)).

**Comparator matched:** Yes. The 80% row gives .42 and .17; the summary gives a 25% difference and two-tailed alpha .05. The .42/.15 row gives 87%. These numbers and formula symbols are source readings, not normalization of incomplete native extraction.

**Consistency rule applicable:** Yes; focus C/D, Route A category 2, a printed quantitative detectable effect differing in magnitude. It is a primary Aim 2 power assumption, not peripheral historical material or a symbol-only discrepancy.

**Calculation reproduced:** Yes. .42−.17=.25. Independent evaluation of the exact printed approximation with n1=58/n0=38 and z(.025)=1.959963985 yields power .802453167 for .42/.17 and .874165373 for .42/.15, reproducing approximately 80% and 87%. Reading 17% literally as the absolute difference from .42 gives comparator .25 and formula power .428097398. Those values are independent diagnostics of the source approximation, not alternative recommended power methods. Tiny numerical differences in the final decimal from earlier evaluations do not change any displayed comparison.

**Display-precision interval check reproduced:** Probability inputs .42/.17 permit [.415,.425] and [.165,.175], so their difference lies [.240,.260]. Printed difference 17% permits [.165,.175]. The interval gap is .065; relative discrepancy=.065/.17=.382352941, above .05. The printed 25% summary permits [.245,.255], overlapping the recomputed difference. The approximate 80% output is consistent with the .802453167 calculation; the candidate concerns the competing printed detectable-effect readings.

**Necessary inputs available:** Yes; formula, probabilities, n0/n1, significance level, confidence in visual symbols, and all original/final repeated locations. **Exact missing inputs or definitions:** Whether “17%” denotes the second-arm probability despite being called a difference, or a separate scenario with different unstated inputs. No supplied alternative calculation produces 80% power for a literal 17-point effect under the printed inputs.

**Source-grounded alternative interpretation:** The prose may intend to name a comparator success probability rather than the between-arm difference, or refer to an unstated scenario. The nearby table and summary allow the larger contrast to be reconstructed, but do not remove the printed smaller-magnitude reading under Route A category 2. No production mechanism is assigned.

**Direct observation versus inferred explanation:** Direct: the 17% difference statement, .42/.17 probability row and 25% summary do not all specify the same absolute effect, with reproduced interval arithmetic. The diagnostic powers illustrate the numerical consequence. Intended effect, cause and any impact on actual trial results are not inferred.

**Exact remaining human question:** Does 17% name a rescue success probability or an absolute between-arm difference, and which effect-size/formula scenario supports the stated 80% primary rescue power?

**Classification confirmed:** `plan_material`; primary `P_P`; all relationships `P_P`; every compared statement lies in original/final prospective SAP material. This pattern is separate from C008's sequence-size mapping because the rule and missing definition differ. **Classification ambiguity:** An unstated comparator-probability usage or separate scenario is possible. **Classification correction:** None.

**Evidence state:** `reproduced`. **Determining recheck fact:** Every repeated source occurrence preserves 17% as a difference, while printed probability inputs and summary identify an overlapping 25% difference and a nonoverlapping 17% interval.

## Completion and bounded limitations

Completed: C001, C002, C003, C004, C005, C006, C007, C008, C009; all affected registered source locations found; nine reproduced states; zero source-value/location transcription corrections; zero document-role, relationship or domain corrections; zero unresolved location/coverage gaps. C003's independent Route B rationale and supplementary designation, and C004's nested Aim 2 primary designation, were explicitly retained.

Unresolved inputs are bounded to the exact questions in each card: missing planned RR/robustness/rescue outputs or amendments, implemented rescue formula and individual probability intervals, eight late-injection classifications, actual adherence-only n/dispersion/test output, patient-level per-protocol membership, any alternate safety-row denominator, and the power displays' coding/17% meaning. All assigned IDs remain Pending Human Adjudication. No severity, acceptance, final correction or disposition is assigned. The source PDFs and all reused assets were preserved.
# Mechanical evidence recheck — appended candidate

Runtime agent ID: `01a1297c-ff3e-7392-baa9-e3e271241550`. Runtime task: `/root/evidence_recheck_appended`. Model: `gpt-6.1-sol`; reasoning effort: `high`; start mode: `FRESH_SPAWN`. Exact assigned scope: C010 only. This agent is distinct from the initial mechanical rechecker, both statistical pass-2 reviewers, and the pass-2 inclusion screener. The C010 ledger card, its independent inclusion-screen record, originating checker record, complete QUALITY_CONTROL_SCOPE.md, and complete review contract were read. No canonical ledger, screening, audit, or manifest artifact was modified.

## C010 — Final primary safety-failure laboratory cutoffs differ at exact boundaries

**Status:** Pending Human Adjudication

**Finding IDs:** F-ST2-101

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN final protocol vs REPORT main article and results supplement

**Evidence state:** reproduced

**Qualifying route:** Route A, category 5

### Location found and source/comparator matched

All page numbers are physical supplied-PDF pages. Each registered affected location and each specified historical contextual location was independently checked. Prospective protocol/manual and revision-history content is PLAN; published trial observations and the non-plan adverse-event results supplement are REPORT.

| Exact supplied-source location | Role by content | Location found | Printed source/comparator content matched |
|---|---|---|---|
| [Final protocol p.80, §2.5.1](../../../joi190092supp2_prod.pdf#page=80) | PLAN | Yes; visually confirmed source-linked raster page | Under definitions for the primary endpoint, six-month success requires the stated ocular/steroid criteria without prior treatment failure due to safety, tolerability, or futility. Thus the safety-failure rule is a component of primary success. |
| [Final protocol p.81, §2.5.2 and Table 3](../../../joi190092supp2_prod.pdf#page=81) | PLAN | Yes; visually confirmed source-linked raster page | Nonserious AST/ALT: 2 to <5 times ULN; serious AST/ALT: ≥5 times ULN. Nonserious leukocytes: >1,000 to <2,500/µL; serious leukocytes: ≤1,000/µL. Nonserious laboratory abnormalities persisting at or above their threshold for 28 days become serious and treatment failure is immediately declared. The table footnote repeats that persistent nonserious abnormalities require serious classification and safety failure. |
| [Final protocol p.136, opening paragraph and §6.2](../../../joi190092supp2_prod.pdf#page=136) | PLAN | Yes; visually confirmed source-linked raster page | Laboratory abnormalities meeting the serious-event threshold immediately stop medication and lead to declaration of treatment failure; laboratory serious events preclude Phase II switching. The serious-event list independently repeats ≥5 times ULN AST or ALT; the nonserious list uses ≥2 but <5. |
| [Main article p.3, Outcomes](../../../jama_rathinam_2019_oi_190092.pdf#page=3) | REPORT | Yes; direct supplied-PDF layout extraction | Primary success includes no declaration of treatment failure due to intolerability or safety. An abnormal laboratory result meeting the serious adverse-event threshold is the explicit safety-failure example. |
| [Main article p.6, Table 2 primary result, safety row and safety-failure footnote](../../../jama_rathinam_2019_oi_190092.pdf#page=6) | REPORT | Yes; direct supplied-PDF layout extraction | Primary success: 64/96 versus 56/98; failure: 32 versus 42. Safety accounts for 3/32 versus 2/42 failures. The full safety-failure footnote defines an abnormal laboratory result meeting the serious adverse-event threshold; footnote glyph placement is not the basis of this comparison. |
| [Main article p.7, Adverse Events](../../../jama_rathinam_2019_oi_190092.pdf#page=7) | REPORT | Yes; direct supplied-PDF layout extraction | Of fourteen serious events through the primary outcome, five were deemed drug related: three in methotrexate and two in mycophenolate. All drug-related serious events were elevated liver-function tests. Individual laboratory values and durations are absent. |
| [Main article p.8, Table 3 laboratory rows and footnotes](../../../jama_rathinam_2019_oi_190092.pdf#page=8) | REPORT | Yes; direct supplied-PDF layout extraction | Nonserious AST/ALT: 2 to 5 times ULN for <28 days. Serious AST/ALT: >5 times ULN or 2 to 5 times ULN for ≥28 days, with three versus two patients. Nonserious leukocytes: >1,000 and <2,500/µL for <28 days. Footnote a points to eTable 1 for definitions; footnote c states all drug-related serious events were elevated ALT, AST, or both. No immediate serious-leukocyte cutoff is displayed here; that comparator is in eTable 1. |
| [Results supplement p.5, eTable 1 laboratory rows](../../../joi190092supp1_prod.pdf#page=5) | REPORT | Yes; direct supplied-PDF layout extraction | Repeats nonserious AST/ALT 2 to 5 times ULN for <28 days; serious 2 to 5 times ULN for at least 28 days or >5 times ULN. Nonserious leukocytes: >1,000 and <2,500/µL for <28 days; serious: <2,500/µL for at least 28 days or <1,000/µL. |
| [Original protocol p.16, Table 3 and discontinuation due to safety](../../../joi190092supp2_prod.pdf#page=16) | PLAN, historical context | Yes; direct supplied-PDF layout extraction | AST/ALT is nonserious at 2 to 5 times ULN and serious at >5 times ULN. The serious leukocyte branch prints ≤999/µL, with an additional prolonged <2,500 branch. The original safety prose uses one month for recovery. These are historical definitions, not the supplied final definition. |
| [Protocol revision history p.148, version 2.2 dated May 1, 2013](../../../joi190092supp2_prod.pdf#page=148) | PLAN, historical context | Yes; direct supplied-PDF layout extraction | States that wording of nonserious and serious laboratory thresholds was modified. It does not reproduce the complete revised threshold table or identify a report-specific final algorithm. |
| [Protocol revision history p.153, versions 4.4 and 4.5](../../../joi190092supp2_prod.pdf#page=153) | PLAN, historical context | Yes; direct supplied-PDF layout extraction | Version 4.4 dated February 26, 2016 explicitly adds the 28-day persistent nonserious abnormality rule for safety failure. Version 4.5 dated January 6, 2017 describes randomization and Phase II eligibility changes. Neither printed entry replaces final pp.81/136 with the report's strict AST/ALT or leukocyte boundaries. |

**Source printed value/text matched:** Yes, for each final PLAN component above: the primary safety-failure linkage, inclusive immediate-serious thresholds, persistence branch, and immediate treatment-failure instruction.

**Comparator printed value/text matched:** Yes, for each REPORT location above: the primary outcome and safety-failure linkage, repeated strict AST/ALT threshold, strict immediate leukocyte threshold in eTable 1, persistence branches, and reported safety counts. Historical PLAN text and revisions also match; they provide version context rather than another registered inconsistency.

### Consistency rule applicable

Compare the supplied final planned definition of the primary treatment-success composite with the definition used to describe that outcome in the REPORT. Both explicitly connect a laboratory serious adverse event to safety failure and therefore to the no-safety-failure component of primary success. Exact membership in an immediate-versus-persistent failure branch is part of that endpoint rule. This is focus area D, with the event-to-primary-failure linkage relevant to C. It is not a numerical comparison of unrelated safety summaries, nor a claim about any participant's observed values.

The two REPORT displays corroborate the same strict-cutoff side. The final PLAN has a coherent 2-to-<5 / ≥5 partition, while the REPORT repeatedly has 2-to-5 / >5 with a separate duration condition. Immediate context does not identify a single common inclusive/exclusive interpretation. The original version supplies a plausible historical source for the report wording but does not make the supplied final and reported definitions identical.

### Logical comparison reproduced

| Diagnostic exact-boundary observation, without assuming any participant had it | Supplied final PLAN classification | Printed REPORT classification | Recheck result |
|---|---|---|---|
| AST or ALT exactly 5×ULN, duration shorter than 28 days | Included in ≥5 immediate-serious branch; the laboratory serious-event rule declares treatment failure. It is outside the 2-to-<5 nonserious branch. | Excluded from >5 immediate-serious branch; the 2-to-5 range is nonserious before 28 days and becomes serious under its persistence branch at ≥28 days. | Different printed immediate-serious/primary-failure membership at the shared numeral 5. |
| Leukocytes exactly 1,000/µL, duration shorter than 28 days | Included in ≤1,000 immediate-serious branch; laboratory serious-event rule declares treatment failure. | Excluded from <1,000 immediate-serious branch; >1,000 nonserious branch also omits the exact boundary. The <2,500 persistent-serious branch requires at least 28 days. | Different printed immediate-serious membership; the report's immediate categories leave this exact boundary unnamed. |

These substitutions reproduce the registered decision-rule discrepancy without requiring participant measurements. Persistence for at least 28 days can qualify an AST/ALT value of exactly 5×ULN or a leukocyte count of exactly 1,000/µL under the report's separate prolonged-abnormality branch; that does not reconcile the shorter-duration immediate classification. No observed event, success, failure, numerator, denominator, effect, interval or P value is recalculated or said to change.

**Display-precision interval check:** Not applicable to this logical membership comparison. The printed cutoff numerals agree. They specify decision thresholds, not rounded estimates to be compared through half-unit measurement intervals; allowing an arbitrary half-unit shift would change the specified rule. The reproduced difference is inclusion versus exclusion of the same exact boundary, coupled to the explicit duration branch. Recomputed numerical interval and relative numerical discrepancy: not applicable. No measured laboratory value is assumed to have rounded to a boundary, and no claim that a numerical discrepancy exceeds 0.05 is made.

### Inputs available and exact missing inputs

**Necessary inputs available:** Yes for reproduction of the printed rule comparison: both documents' cutoff inequalities, both persistence branches, and the explicit link to primary treatment failure are supplied and source matched. The reported 64/96 versus 56/98 successes and three versus two safety failures identify the result whose definition is in question.

**Exact missing inputs or definitions:** Participant-level AST/ALT and leukocyte measurements; the laboratory-specific ULN/reference ranges; observation timing and persistence duration; event-to-participant linkage; the actual implemented inclusive/exclusive classification algorithm; operational adjudication instructions; any unsupplied amendment selecting another threshold version; and whether any of the five reported liver-function safety classifications depended on an exact-boundary observation. These are required to determine implementation and any actual consequence, not to reproduce the two printed rules. No printed leukocyte serious-failure count is inferred from the supplied report.

### Alternatives and direct observation versus inferred explanation

**Source-grounded alternative interpretation:** Original protocol p.16 uses >5 times ULN and ≤999/µL, so the report may preserve a historical threshold description. Alternatively, the report's strict symbols may abbreviate an implemented inclusive rule; the final inclusive rule may have been applied while the report used another description; or an unsupplied instruction may identify another actual algorithm. Revision p.148 discloses modified threshold wording and p.153 adds the persistence requirement, but neither supplies the implementation bridge that resolves the final/report exact boundary. None of these alternatives is established as the actual explanation.

**Direct observation:** Final PLAN pp.81/136 print the inclusive immediate AST/ALT cutoff, p.81 prints the inclusive leukocyte cutoff, and REPORT main p.8/results p.5 repeatedly print the strict AST/ALT cutoff while results p.5 prints the strict leukocyte cutoff. PLAN p.80 and REPORT pp.3/6 explicitly attach serious laboratory failure to the primary composite. Counts and contextual historical passages are directly matched above.

**Inferred explanation:** None assigned. The boundary examples are diagnostic substitutions into printed definitions, not reconstructed participant records. No production mechanism, protocol violation, implemented participant classification discrepancy, changed primary count, changed significance or changed conclusion is inferred.

**Exact remaining human question:** Which inclusive/exclusive AST/ALT and leukocyte cutoffs generated the primary safety-failure classifications, how was the 28-day persistence branch applied, and did any primary safety classification depend on an exact-boundary observation?

### Classification confirmation and determining evidence fact

**Document roles confirmed:** Every final/original protocol and revision location is PLAN by its prospective or amendment content. The main article and its adverse-event results supplement are REPORT by their reported-outcome content. No role correction is needed.

**Relationship type confirmed:** P_R. **All relationships confirmed:** P_R. **Review domain confirmed:** protocol_report. The discrepancy compares final prospective endpoint-rule content with reported outcome-rule content. The article and results supplement agree on the comparator and therefore do not add S_C; repeated agreeing locations within either document do not add S_W. Legitimate historical plan versions are contextual and are not separately asserted to conflict in this candidate, so P_P is not added. Precedence P_R > P_P > S_C > S_W is satisfied by the single registered relationship. No classification correction is needed.

**Classification ambiguity:** The implemented threshold version and any unsupplied amendment are unavailable. This concerns implementation, not the content-based PLAN/REPORT role assignments or the observed final-plan/report relationship.

**Evidence state:** reproduced. **Determining recheck fact:** The exact supplied-source final PLAN inequalities include 5×ULN and 1,000/µL in immediate laboratory serious failure, while the repeated REPORT definitions do not include those exact boundaries in their corresponding immediate branches and require the persistence alternative where applicable. Both explicitly supply the primary-safety-failure link. All registered values and locations match; no source-value or location transcription correction was made. The stable ID remains Pending Human Adjudication.

## Methods, provenance and completion

Direct CPU Poppler `pdftotext -layout` 26.01.0 read supplied main PDF pp.3,6,7,8, results supplement p.5, and protocol pp.16,148,153 to standard output; no derivative was written. The raster-bearing final protocol pp.80,81,136 were visually inspected in full using source-linked page images: current `preprocessing/evidence_recheck/protocol_p080.png` (recorded CPU Poppler 26.01.0 derivative), reused `.ai_paper_validation/review_1_6_1/preprocessing/protocol_b/page-81.png`, and reused `protocol_c/page-136.png` (legacy extraction-engine versions not recorded). Images are visual transcription aids; exact supplied PDF page locations remain the evidence authority. No new rendering, OCR, helper environment or derivative was needed. No source or reused asset was modified, no external evidence was used, and no legacy candidate or adjudication artifact was read.

Completed exact assigned ID C010, with all eight registered affected source locations and all three requested historical/contextual locations checked. One evidence state: reproduced; zero transcription corrections; zero role, relationship, or domain corrections. Remaining questions concern only the unavailable implemented rule and participant-level boundary measurements/durations identified above. No severity, disposition, preferred analysis, final correction or human adjudication is assigned.
