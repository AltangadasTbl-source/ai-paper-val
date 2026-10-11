# Mechanical evidence recheck

Status: COMPLETE. Assigned scope: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011, C012, C013, C014, C015, C016, C017, C018, C019. All 19 IDs have separate source confirmation, rule and input checks, classification, evidence state, and remaining human question below. Every ID remains Pending Human Adjudication. Evidence states describe the recheck facts and are not adjudications.

The stable ledger and current checker provenance supplied the questions and locators. Final confirmation used the supplied PDFs directly: fresh Poppler 25.03.0 layout extraction and CPU page rendering, followed by visual inspection of every cited page. Previously extracted text and images were not final authority. All registered transcriptions were found as printed; no OCR disagreement or corrected transcription was needed. No source, reused derivative, ledger, or other agent artifact was changed. No web, GPU, custom Python, OCR, package installation, or fallback environment was used.

## Engines and direct-source derivatives

Engine: direct `pdftotext` and `pdftoppm`, Poppler 25.03.0. All new derivatives are below `review_1_6/preprocessing/` and carry the unique `recheck-` prefix. Source scope and actual derivative units:

| Source | Physical pages | Layout derivative names | Render derivative names |
|---|---|---|---|
| jama_wang_2018_oi_180070.pdf | 2, 3, 4, 5, 6, 7, 8 | recheck-main-p2-layout.txt, recheck-main-p3-layout.txt, recheck-main-p4-layout.txt, recheck-main-p5-layout.txt, recheck-main-p6-layout.txt, recheck-main-p7-layout.txt, recheck-main-p8-layout.txt | recheck-main-p2.png, recheck-main-p3.png, recheck-main-p4.png, recheck-main-p5.png, recheck-main-p6.png, recheck-main-p7.png, recheck-main-p8.png |
| joi180070supp2_prod.pdf | 2, 3, 5, 8 | recheck-results-p2-layout.txt, recheck-results-p3-layout.txt, recheck-results-p5-layout.txt, recheck-results-p8-layout.txt | recheck-results-p2.png, recheck-results-p3.png, recheck-results-p5.png, recheck-results-p8.png |
| joi180070supp1_prod.pdf | 13, 14, 15, 16, 19 | recheck-plan-p13-layout.txt, recheck-plan-p14-layout.txt, recheck-plan-p15-layout.txt, recheck-plan-p16-layout.txt, recheck-plan-p19-layout.txt | recheck-plan-p13.png, recheck-plan-p14.png, recheck-plan-p15.png, recheck-plan-p16.png, recheck-plan-p19.png |

For each listed physical page N the executed command patterns were:

```bash
pdftotext -layout -f N -l N "SOURCE.pdf" ".ai_paper_validation/review_1_6/preprocessing/recheck-LABEL-pN-layout.txt"
pdftoppm -f N -l N -singlefile -scale-to 1800 -png "SOURCE.pdf" ".ai_paper_validation/review_1_6/preprocessing/recheck-LABEL-pN"
```

The table expands every N and SOURCE/LABEL pair; all 16 layouts and 16 fresh page images were produced and read/visually inspected. Calculations were independently reproduced with ordinary arithmetic, including exact integer sums, percentage division, and logical order-statistic bounds. Links below resolve from this verification directory using three parent levels and physical PDF page numbers.

## Per-ID evidence-state and classification summary

| ID | Evidence state | Relationship type | All relationships | Review domain | Classification change |
|---|---|---|---|---|---|
| C001 | recorded_candidate | S_W | S_W | statistical_results | None |
| C002 | recorded_candidate | S_W | S_W | statistical_results | None |
| C003 | recorded_candidate | S_W | S_W | statistical_results | None |
| C004 | recorded_candidate | S_W | S_W | report_internal_inconsistency | None |
| C005 | recorded_candidate | S_W | S_W | report_internal_inconsistency | None |
| C006 | recorded_candidate | S_W | S_W | report_internal_inconsistency | None |
| C007 | record_input_error | S_W | S_W | statistical_results | None; unsupported population alignment identified |
| C008 | recorded_candidate | S_W | S_W | statistical_results | None |
| C009 | recorded_candidate | S_W | S_W | statistical_results | None |
| C010 | recorded_candidate | S_W | S_W | statistical_results | None |
| C011 | recorded_candidate | S_W | S_W | statistical_results | None |
| C012 | record_input_error | P_P | P_P | plan_material | None; unsupported inventory alignment identified |
| C013 | recorded_candidate | P_R | P_R, S_C, S_W | protocol_report | None |
| C014 | recorded_candidate | S_C | S_C | statistical_results | None |
| C015 | recorded_candidate | S_C | S_C | report_internal_inconsistency | None |
| C016 | recorded_candidate | S_C | S_C | report_internal_inconsistency | None; diagnostic conditions preserved |
| C017 | recorded_candidate | P_R | P_R, S_C | protocol_report | None |
| C018 | recorded_candidate | S_W | S_W | statistical_results | None; prose scope remains conditional |
| C019 | recorded_candidate | S_W | S_W | statistical_results | None; common CI/test construction unestablished |

State counts: recorded_candidate 17; record_input_error 2; not_reproduced 0; repaired_residual 0. Document-role summary: 13 S_W main/results-report comparisons, 3 S_C main-versus-results-supplement comparisons, 1 P_P plan-internal comparison, and 2 P_R primary comparisons with additional report relationships. All document roles, primary categories, relationship sets, precedence decisions, and derived domains agree with the registered classification. Corroborating-only locations do not add discrepancy relationships.

## C001 — Primary-analysis population labels give different totals

- **Location found:** Yes. [Main p4, Results and Data Analysis](../../../jama_wang_2018_oi_180070.pdf#page=4), [main p5, Figure 1 bottom boxes and preceding follow-up boxes](../../../jama_wang_2018_oi_180070.pdf#page=5), and [main p7, Table 2 all-or-none row](../../../jama_wang_2018_oi_180070.pdf#page=7), confirmed in fresh source renders.
- **Source value/text matched:** Yes. Results says 4800 enrolled and included in primary analysis; Data Analysis states intention-to-treat for all outcomes.
- **Comparator matched:** Yes. Figure 1 labels 2003 and 1977 patients included in primary analysis, with preceding 397 and 423 lost to 12-month follow-up. Table 2 shows denominators 2400 and 2400.
- **Consistency rule applicable:** Yes for labels referring to the same primary-analysis population; exact integer totals should match. A different follow-up-specific analysis would require a population distinction.
- **Calculation or logical comparison reproduced:** 2003 + 1977 = 3980; 4800 − 3980 = 820; 397 + 423 = 820. Table 2 denominator total is 4800.
- **Necessary inputs available:** All printed counts and labels are available for the observed conflict; actual analysis membership is unavailable.
- **Exact missing inputs or definitions:** Figure-box population definition and outcome-specific analysis membership, especially whether the bottom counts label follow-up completion.
- **Source-grounded alternative interpretation:** Main p4 explicitly identifies 2003/1977 as 12-month completers. Figure 1 may have applied a primary-analysis label to these follow-up counts.
- **Direct observation versus inferred explanation:** Conflicting printed totals/labels are direct; describing a diagram-label production error is inferred. No assertion that 820 were omitted from co-primary analyses follows.
- **Exact remaining human question:** What population do Figure 1's bottom patient boxes intend, and which patients entered each primary analysis?
- **Classification:** Category Denominator, proportion, or total inconsistency. Each compared location is REPORT by its published results/methods content within the main article. Relationship type S_W; All relationships S_W; Review domain statistical_results. Confirmed without change. PLAN intention-to-treat material only corroborates one side and adds no P_R relationship. Ambiguity: possible follow-up-specific population.
- **Evidence state:** recorded_candidate. Determining fact: the exact primary-analysis wording accompanies 3980 in Figure 1 and 4800 in Results/Table 2; the source also supports the explicitly preserved follow-up explanation.

## C002 — Intervention CAD percentage and displayed count/total differ

- **Location found:** Yes. [Main p6, Table 1 Intervention Patients total and CAD/previous myocardial infarction row](../../../jama_wang_2018_oi_180070.pdf#page=6), fresh source image inspected.
- **Source value/text matched:** Yes: intervention total 2400 and CAD/previous MI count 311.
- **Comparator matched:** Yes: accompanying percentage 13.05, confirmed visually with two decimal places.
- **Consistency rule applicable:** Yes under Table 1's No. (%) and displayed arm-total convention; a row-specific denominator would change the calculation but is not stated.
- **Calculation or logical comparison reproduced:** 100 × 311/2400 = 12.958333%; nearest two decimals 12.96. Printed-minus-computed difference 0.091667 percentage point exceeds ±0.005-point two-decimal rounding tolerance.
- **Necessary inputs available:** All displayed arithmetic inputs are present; a possible alternative row denominator is not.
- **Exact missing inputs or definitions:** Any CAD-specific missingness/denominator or weighting convention. Main p4 general imputation does not identify such a denominator.
- **Source-grounded alternative interpretation:** A row-specific denominator or a transcribed numerator/percentage could explain the printed cell; the table gives no choice among them.
- **Direct observation versus inferred explanation:** 311, 2400, and 13.05 are direct; their division is derived. A denominator or transcription explanation is inferred.
- **Exact remaining human question:** Which numerator and denominator generated 13.05%, and does this CAD cell use the displayed intervention total of 2400?
- **Classification:** Category Denominator, proportion, or total inconsistency. Count, total, and percentage are all REPORT content in the same main table. Relationship type S_W; All relationships S_W; Review domain statistical_results. Confirmed without change. Ambiguity: unstated row denominator.
- **Evidence state:** recorded_candidate. Determining fact: visual source confirmation and reproduced fraction show a difference beyond displayed rounding under the table's stated format.

## C003 — Control EMS percentage and count/total differ

- **Location found:** Yes. [Main p6, Table 1 Control Patients total and Transported to ED by EMS row](../../../jama_wang_2018_oi_180070.pdf#page=6), fresh source image inspected.
- **Source value/text matched:** Yes: 236 control EMS patients and control total 2400.
- **Comparator matched:** Yes: 9.9 in the same cell. The adjacent onset-to-arrival row has 238 (9.9) and was kept separate.
- **Consistency rule applicable:** Yes under the table's No. (%) and displayed arm-total convention; no EMS-specific denominator is printed.
- **Calculation or logical comparison reproduced:** 100 × 236/2400 = 9.833333%, nearest one decimal 9.8. Difference from 9.9 is 0.066667 percentage point, exceeding ±0.05-point tolerance.
- **Necessary inputs available:** Displayed arithmetic inputs are available; variable-specific observation count is not separately provided.
- **Exact missing inputs or definitions:** Any EMS-specific missingness denominator or nonstandard percentage construction.
- **Source-grounded alternative interpretation:** A smaller row-specific denominator could yield 9.9; the neighboring row's 238 is another characteristic and cannot replace 236 without source authority.
- **Direct observation versus inferred explanation:** The cell, header, and total are direct; arithmetic is derived; denominator/transcription mechanisms are inferred.
- **Exact remaining human question:** Does EMS use a row-specific denominator, and which printed input or percentage convention explains 236 (9.9) among 2400?
- **Classification:** Category Denominator, proportion, or total inconsistency. All compared cells are REPORT in the same main Table 1. Relationship type S_W; All relationships S_W; Review domain statistical_results. Confirmed without change. Ambiguity: missingness denominator.
- **Evidence state:** recorded_candidate. Determining fact: the source confirms 236 rather than 238, and the registered same-table percentage difference is reproduced.

## C004 — Unqualified all-nine outcome label differs from eligible-measure definition

- **Location found:** Yes. [Main p2, Key Points Findings](../../../jama_wang_2018_oi_180070.pdf#page=2), [main p3, Outcomes](../../../jama_wang_2018_oi_180070.pdf#page=3), and [main p7, Table 2 all-or-none and rtPA rows](../../../jama_wang_2018_oi_180070.pdf#page=7), all visually inspected.
- **Source value/text matched:** Yes: Key Points says adherence to all 9 performance measures.
- **Comparator matched:** Yes: Outcomes defines all performance measures for which the patient was eligible. Table 2 gives all-or-none 1290/2400 and 1147/2400, versus rtPA receipt 46/212 and 23/204.
- **Consistency rule applicable:** Yes as a conditional literal label check: receiving all nine entails receiving rtPA. The eligible-measure definition does not entail this for ineligible patients.
- **Calculation or logical comparison reproduced:** Literal all-nine recipient counts cannot exceed 46/23; 1290 − 46 = 1244 and 1147 − 23 = 1124. The actual eligible all-or-none definition permits the larger counts.
- **Necessary inputs available:** Label, eligibility definition, and counts are available; no patient-level receipt record is needed for this logical distinction.
- **Exact missing inputs or definitions:** Whether Key Points intentionally uses all nine as shorthand for the nine-measure bundle with patient-specific eligibility.
- **Source-grounded alternative interpretation:** Outcomes and the Table 2 title explicitly describe eligible measures/patients; Key Points may abbreviate that already stated definition.
- **Direct observation versus inferred explanation:** Omission of the eligibility qualification is direct; a literal all-nine impossibility is a diagnostic interpretation, not evidence that the actual analysis used that interpretation.
- **Exact remaining human question:** Is the Key Points phrase intended as eligible-bundle shorthand, and should its patient-specific eligibility qualification be explicit?
- **Classification:** Category Measure, label, or scale inconsistency. All compared locations are REPORT in the same main article. Relationship type S_W; All relationships S_W; Review domain report_internal_inconsistency. Confirmed without change. PLAN eligibility corroborates the Methods definition and adds no discrepancy relationship. Ambiguity: shorthand interpretation.
- **Evidence state:** recorded_candidate. Determining fact: the printed qualification differs and its registered literal interpretation diagnostic is reproduced; actual eligibility-based computation is not contradicted.

## C005 — Matched clinical results use discharge and onset time origins

- **Location found:** Yes. [Main p5, Clinical Events opening and linked estimates](../../../jama_wang_2018_oi_180070.pdf#page=5), [main p3, Outcomes](../../../jama_wang_2018_oi_180070.pdf#page=3), [main p8, Table 3 footnote b and Figure 2 axes/caption](../../../jama_wang_2018_oi_180070.pdf#page=8), and [main p6, stay row](../../../jama_wang_2018_oi_180070.pdf#page=6), visually confirmed.
- **Source value/text matched:** Yes: p5 says clinical outcomes at 3, 6, and 12 months after discharge and repeats Table 3 vascular/disability results.
- **Comparator matched:** Yes: p3 says after initial symptom onset; Table 3 disability footnote says after stroke onset; Figure 2 axes/caption say days after stroke symptom onset. Stay medians are 13/12 days by arm.
- **Consistency rule applicable:** Yes for reference-time labels of the matched outcomes; discharge and onset are distinct time origins.
- **Calculation or logical comparison reproduced:** Time since discharge = time since onset − onset-to-discharge interval. The matched 12-month vascular figures 9.1%/11.8% and HR 0.72 support result alignment; no fixed time shift can be calculated from stay medians.
- **Necessary inputs available:** Both reference-time labels and matching reported results are available; patient-specific onset/discharge/assessment dates are absent.
- **Exact missing inputs or definitions:** Which origin defined actual assessment windows and event times; whether p5 uses discharge merely as informal follow-up-contact language.
- **Source-grounded alternative interpretation:** Methods, Table 3 footnote, and Figure 2 consistently support onset; the p5 phrase could be narrative shorthand or a wording error.
- **Direct observation versus inferred explanation:** Time-label difference is direct; its cause and actual implemented clock are inferred/unknown.
- **Exact remaining human question:** Which clock generated these matched clinical outcomes and risk sets, and how should the after-discharge wording be understood?
- **Classification:** Category Measure, label, or scale inconsistency. Every compared main location is REPORT. Relationship type S_W; All relationships S_W; Review domain report_internal_inconsistency. Confirmed without change. [PLAN p16 lines223–230](../../../joi180070supp1_prod.pdf#page=16) corroborates onset and adds no P_R relationship. Ambiguity: contact wording versus outcome horizon.
- **Evidence state:** recorded_candidate. Determining fact: fresh direct source pages preserve the discharge-versus-onset labels for demonstrably matched results.

## C006 — Cumulative-incidence plots called HR curves

- **Location found:** Yes. [Main p7, Discussion right column](../../../jama_wang_2018_oi_180070.pdf#page=7) and [main p8, Figure 2A/B axes and annotations](../../../jama_wang_2018_oi_180070.pdf#page=8), source images inspected.
- **Source value/text matched:** Yes: Discussion says HR curves of new clinical vascular events separated in the first 30 days.
- **Comparator matched:** Yes: both plots' ordinate is Cumulative Incidence with 0, .05, .10, .15 ticks and separate group curves; scalar annotations are HR 0.72 (0.60–0.87), P < .001 for vascular events and HR 0.86 (0.68–1.09), P = .21 for death.
- **Consistency rule applicable:** Yes: cumulative-incidence probability and a comparative hazard ratio are different measures.
- **Calculation or logical comparison reproduced:** The ordinate labels identify the drawn quantities; the scalar HR annotations do not turn arm-specific incidence curves into HR curves. No HR reconstruction is warranted.
- **Necessary inputs available:** Curve names, axes, and annotations are sufficient; individual time-to-event data are unnecessary for this naming comparison.
- **Exact missing inputs or definitions:** Whether HR curves was intended as informal shorthand for survival/event curves accompanied by an HR.
- **Source-grounded alternative interpretation:** Each displayed incidence plot does carry an HR annotation, allowing informal reference to an HR analysis.
- **Direct observation versus inferred explanation:** Axis/prose naming difference is direct; reader confusion or informal terminology as its cause is inferred.
- **Exact remaining human question:** Which plotted quantity did HR curves intend, and should its name agree explicitly with the cumulative-incidence ordinate?
- **Classification:** Category Measure, label, or scale inconsistency. Prose and plots are REPORT in the same main article. Relationship type S_W; All relationships S_W; Review domain report_internal_inconsistency. Confirmed without change. Ambiguity: informal nomenclature.
- **Evidence state:** recorded_candidate. Determining fact: visual source confirmation reproduces the registered quantity-label difference without questioning the scalar HR values.

## C007 — NIHSS imputation median differs from displayed group medians

- **Location found:** Yes. [Main p4, Data Analysis missingness paragraph](../../../jama_wang_2018_oi_180070.pdf#page=4) and [main p6, Table 1 NIHSS row and patient totals](../../../jama_wang_2018_oi_180070.pdf#page=6), visually inspected.
- **Source value/text matched:** Yes: one missing NIHSS score was replaced by the median value of 3; medians were used for missing continuous variables.
- **Comparator matched:** Yes: baseline-survey n = 801 median 4 (2–8), intervention/control n = 2400 each median 4 (2–6).
- **Consistency rule applicable:** Conditional only. Median insertion preserves the reference median if the inserted value is that reference distribution's median. The source does not identify the imputation reference distribution as pooled trial patients or any displayed group.
- **Calculation or logical comparison reproduced:** Appending 3 to an odd observed reference sample with median 3 preserves median 3. If both 2400-patient arm medians conventionally equal 4, the full pooled median cannot be exactly 3; at most 2400 scores can be ≤3, so its two middle values cannot both be 3. This conditional diagnostic is reproducible but its required common-reference premise is unestablished.
- **Necessary inputs available:** Printed replacement and displayed group medians are available. The necessary reference population and score inputs connecting them are not available.
- **Exact missing inputs or definitions:** Hospital-, subgroup-, arm-, pooled-, or other reference population; data snapshot; quantile convention; pre/post-imputation descriptive input counts.
- **Source-grounded alternative interpretation:** The trial is clustered by hospital, and p4 does not name the imputation population. A local/subgroup reference or a different data stage could have median 3 while Table 1 groups have displayed median 4.
- **Direct observation versus inferred explanation:** Different displayed numbers are direct. Treating 3 as the pooled trial median is an inference that the source does not establish; a particular local or external implementation is also unconfirmed.
- **Exact remaining human question:** What reference population/data stage supplied the replacement median 3, and was it the same score set used for Table 1's group medians?
- **Classification:** Category Numeric or arithmetic inconsistency. Both compared locations are REPORT methods/results within the main article. Relationship type S_W; All relationships S_W; Review domain statistical_results. Confirmed without change as the classification of the registered comparison. Ambiguity: unsupported population alignment; C016 has a separate partition comparator.
- **Evidence state:** record_input_error. Determining fact: direct source content never assigns median 3 to a displayed Table 1 population; the registered mismatch depends on an unsupported shared-reference alignment, and existence of a residual numeric discrepancy cannot be settled. This is not a disproven transcription and does not remove the ID.

## C008 — Sensitivity control discharge-antithrombotic fraction and percentage differ

- **Location found:** Yes. [Results supplement p8, eTable 4 discharge Antithrombotics Control No./Total (%) cell](../../../joi180070supp2_prod.pdf#page=8), visually inspected.
- **Source value/text matched:** Yes: integer fraction 2141/2400.
- **Comparator matched:** Yes: same-cell percentage 89.3.
- **Consistency rule applicable:** Yes: the percentage in a No./Total (%) cell should equal its displayed integer fraction within one-decimal rounding; adjusted effects are separate columns.
- **Calculation or logical comparison reproduced:** 100 × 2141/2400 = 89.208333%, rounding to 89.2. Difference 0.091667 percentage point exceeds ±0.05.
- **Necessary inputs available:** Complete displayed numerator, denominator, percentage, and column header are present.
- **Exact missing inputs or definitions:** Any separate raw-percentage weighting/denominator convention or underlying cell-production record; none is printed.
- **Source-grounded alternative interpretation:** Undisclosed percentage construction or a transcribed cell could explain the difference. Adjusted effect columns cannot explain a raw fraction's percentage without an additional stated rule.
- **Direct observation versus inferred explanation:** All printed inputs are direct; division is derived; any production explanation is inferred.
- **Exact remaining human question:** Does this percentage use 2141 of 2400, and which input or convention explains the printed 89.3?
- **Classification:** Category Denominator, proportion, or total inconsistency. Both compared quantities are REPORT results within the same results-supplement cell. Relationship type S_W; All relationships S_W; Review domain statistical_results. Confirmed without change. Ambiguity: unstated percentage construction.
- **Evidence state:** recorded_candidate. Determining fact: current source image and independent calculation reproduce the registered difference beyond one-decimal rounding.

## C009 — Sensitivity control AF-anticoagulation fraction and percentage differ

- **Location found:** Yes. [Results supplement p8, eTable 4 Anticoagulation for Atrial Fibrillation Control cell](../../../joi180070supp2_prod.pdf#page=8), visually inspected.
- **Source value/text matched:** Yes: 39/174 under No./Total (%).
- **Comparator matched:** Yes: accompanying 22.5.
- **Consistency rule applicable:** Yes: same-cell raw percentage versus exact displayed fraction with ±0.05-point one-decimal tolerance.
- **Calculation or logical comparison reproduced:** 100 × 39/174 = 22.413793%, rounding to 22.4. Difference 0.086207 percentage point exceeds tolerance.
- **Necessary inputs available:** All displayed arithmetic inputs and raw/effect column distinctions are present.
- **Exact missing inputs or definitions:** Any different percentage denominator or weighting convention; underlying source cell inputs are not supplied.
- **Source-grounded alternative interpretation:** A different raw input or undisclosed construction could produce 22.5; effect adjustment is not a stated alternative percentage definition.
- **Direct observation versus inferred explanation:** Fraction and percentage are direct; arithmetic is derived; mechanism is inferred.
- **Exact remaining human question:** Which denominator/count or percentage convention generated 22.5 for the displayed 39/174 cell?
- **Classification:** Category Denominator, proportion, or total inconsistency. Compared values are REPORT in the same results-supplement eTable 4 cell. Relationship type S_W; All relationships S_W; Review domain statistical_results. Confirmed without change. Ambiguity: possible undisclosed construction.
- **Evidence state:** recorded_candidate. Determining fact: visually confirmed exact inputs do not reconcile under displayed percentage precision.

## C010 — Sensitivity control lipid-lowering fraction and percentage differ

- **Location found:** Yes. [Results supplement p8, eTable 4 Lipid-lowering Control No./Total (%) cell](../../../joi180070supp2_prod.pdf#page=8), visually inspected.
- **Source value/text matched:** Yes: 1439/1586.
- **Comparator matched:** Yes: same-cell 90.8.
- **Consistency rule applicable:** Yes: exact displayed fraction and one-decimal raw percentage convention, independently of eligibility-label C013.
- **Calculation or logical comparison reproduced:** 100 × 1439/1586 = 90.731400%, rounding to 90.7. Difference 0.068600 percentage point exceeds ±0.05.
- **Necessary inputs available:** All displayed inputs are present; actual raw-percentage implementation is absent.
- **Exact missing inputs or definitions:** Any weighting or alternate numerator/denominator used to generate this percentage.
- **Source-grounded alternative interpretation:** An undisclosed denominator/weighting or cell transcription may explain the difference; none can be selected from the package.
- **Direct observation versus inferred explanation:** Cell values are direct; division is derived; possible production mechanisms are inferred.
- **Exact remaining human question:** Does 1439/1586 determine this raw percentage, and which convention or input explains 90.8?
- **Classification:** Category Denominator, proportion, or total inconsistency. Both quantities are REPORT in one results-supplement cell. Relationship type S_W; All relationships S_W; Review domain statistical_results. Confirmed without change. The separate PLAN/report eligibility comparison is not this arithmetic relationship.
- **Evidence state:** recorded_candidate. Determining fact: direct image confirms the fraction and 90.8, with reproduced rounding discrepancy.

## C011 — Sensitivity control antidiabetic fraction and percentage differ

- **Location found:** Yes. [Results supplement p8, eTable 4 Antidiabetic Medication Control No./Total (%) cell](../../../joi180070supp2_prod.pdf#page=8), visually inspected.
- **Source value/text matched:** Yes: 557/688.
- **Comparator matched:** Yes: accompanying percentage 81.1.
- **Consistency rule applicable:** Yes: raw integer fraction versus one-decimal percentage with ±0.05-point rounding tolerance.
- **Calculation or logical comparison reproduced:** 100 × 557/688 = 80.959302%, rounding to 81.0. Difference 0.140698 percentage point exceeds tolerance.
- **Necessary inputs available:** Displayed numerator, denominator, percentage and column format are complete.
- **Exact missing inputs or definitions:** Any weighting or alternative raw fraction underlying 81.1.
- **Source-grounded alternative interpretation:** Transcription or undisclosed percentage construction may explain it. Adjusted effects are distinct and do not change the printed raw-fraction identity.
- **Direct observation versus inferred explanation:** Inputs are direct, arithmetic derived, and any error mechanism inferred.
- **Exact remaining human question:** Which raw inputs or percentage convention explains 81.1 beside 557/688?
- **Classification:** Category Denominator, proportion, or total inconsistency. All compared content is REPORT within the same results-supplement cell. Relationship type S_W; All relationships S_W; Review domain statistical_results. Confirmed without change. Ambiguity: raw-percentage construction.
- **Evidence state:** recorded_candidate. Determining fact: fresh visual confirmation and calculation reproduce the difference beyond printed precision.

## C012 — PLAN example names seven measures while the PLAN specifies nine

- **Location found:** Yes. [PLAN p19, lines276–279](../../../joi180070supp1_prod.pdf#page=19) and [PLAN p13 Table 2 acute list](../../../joi180070supp1_prod.pdf#page=13)/[p14 discharge continuation](../../../joi180070supp1_prod.pdf#page=14), all visually inspected.
- **Source value/text matched:** Yes: the sentence begins For example, if and describes eligibility for 5 of the 7 performance measures, receiving 3 and contributing 5 observations: 3 outcome ones and 2 zeros.
- **Comparator matched:** Yes: actual predefined list contains 4 acute measures plus 5 discharge measures, total 9.
- **Consistency rule applicable:** Not established for a shared inventory. Seven differs from nine, but an expressly hypothetical model example need not assert the actual trial's total universe. Its own observation arithmetic is coherent.
- **Calculation or logical comparison reproduced:** 4 + 5 = 9; 7 ≠ 9 if they denote the same inventory; 3 + 2 = 5 and 5 ≤ 7 are coherent within the example. Direct content does not supply the required inventory identity.
- **Necessary inputs available:** All printed example/list inputs are available; the connection between their universes is not established.
- **Exact missing inputs or definitions:** Whether 7 intentionally denotes a hypothetical/subset universe or was intended to describe the trial's nine-measure bundle.
- **Source-grounded alternative interpretation:** Explicit For example, if wording introduces an illustration of opportunity-level coding rather than an independent trial-total statement. [Main p4](../../../jama_wang_2018_oi_180070.pdf#page=4) repeats the same illustrative structure, which corroborates the example rather than creates a discrepancy relationship.
- **Direct observation versus inferred explanation:** The numbers and hypothetical phrasing are direct. Treating seven as an actual trial-inventory assertion is an unsupported inference.
- **Exact remaining human question:** Was the example's seven intended as a hypothetical/subset count or as the actual trial inventory, and is any clarifying wording warranted?
- **Classification:** Category Numeric or arithmetic inconsistency, preserved as the registered comparison's category. All substantive compared locations are PLAN by prospective outcome/analysis content within one bound protocol/SAP. Relationship type P_P; All relationships P_P; Review domain plan_material. Confirmed without change. The parallel main REPORT example only corroborates and adds no P_R. Ambiguity: inventory identity is unsupported.
- **Evidence state:** record_input_error. Determining fact: the source explicitly frames the seven-measure passage as a hypothetical example; registering seven versus nine as a shared trial total rests on unsupported inventory alignment, and intent/residual discrepancy cannot be settled from the package.

## C013 — Lipid-measure threshold/eligible-set labels differ across supplied definitions

- **Location found:** Yes. [Main p3 Outcomes](../../../jama_wang_2018_oi_180070.pdf#page=3), [main p7 Table 2 lipid row](../../../jama_wang_2018_oi_180070.pdf#page=7), [results supplement p8 eTable 4 lipid row](../../../joi180070supp2_prod.pdf#page=8), [results supplement p3 eTable 1 LDL definition](../../../joi180070supp2_prod.pdf#page=3), and [PLAN p15 Table 3 LDL definition](../../../joi180070supp1_prod.pdf#page=15), visually inspected.
- **Source value/text matched:** Yes: main Outcomes more than 100 mg/dL or undocumented LDL; main/results-table lipid titles LDL >100 mg/dL. Primary fractions 1415/1481 and 1439/1547; sensitivity fractions 1415/1517 and 1439/1586.
- **Comparator matched:** Yes: results eTable 1 and PLAN Table 3 specify LDL ≥100 mg/dL, previous lipid-lowering treatment, or LDL not documented.
- **Consistency rule applicable:** Yes for literal threshold/eligible-set identity; > excludes exactly 100 whereas ≥ includes it. Prior treatment and undocumented LDL also exceed the abbreviated table-title conditions.
- **Calculation or logical comparison reproduced:** At LDL = 100, the predicates >100 and ≥100 yield different eligibility; the additional prior-treatment condition can include a patient below the threshold. Primary-versus-sensitivity denominator increases 36/39 do not identify boundary-case counts and are not a separate arithmetic conflict.
- **Necessary inputs available:** All definition/label texts and displayed denominators are available; patient-level LDL/prior-treatment/contraindication data are absent.
- **Exact missing inputs or definitions:** Implemented eligibility algorithm, counts at exactly 100, treatment-before-admission handling, and whether titles abbreviate the full definition.
- **Source-grounded alternative interpretation:** Main Outcomes explicitly refers readers to detailed eTable 1 specifications, supporting the possibility that table titles summarize the broader rule.
- **Direct observation versus inferred explanation:** Different printed predicates/criteria are direct. A change in actual eligible counts or analytic implementation is not established.
- **Exact remaining human question:** Which eligible-set algorithm generated each primary/sensitivity denominator, and are the >100 titles intended as shorthand for the fuller ≥100/prior-treatment/undocumented rule?
- **Classification:** Category Measure, label, or scale inconsistency. Main Outcomes/Table 2 and results eTable 4/eTable 1 are REPORT; PLAN Table 3 is PLAN by prospective specification content. Relationship type P_R; All relationships P_R, S_C, S_W; Review domain protocol_report. P_R compares literal REPORT >100 with PLAN ≥100; S_C compares main wording/title with another REPORT's fuller definition; S_W compares results eTable 4 title with its own eTable 1 definition. P_R has precedence. No P_P discrepancy is registered: PLAN specification corroborates the fuller definition, and an abbreviated plan listing does not create an independent conflicting algorithm. Confirmed without change. Ambiguity: abbreviated labels and disclosed cross-reference.
- **Evidence state:** recorded_candidate. Determining fact: exact ≥ and > signs and additional eligibility criteria are directly confirmed; the label/definition difference persists with unknown implementation impact.

## C014 — Baseline survey total differs from per-cluster statement

- **Location found:** Yes. [Main p6, Table 1 baseline Hospitals/Patients rows](../../../jama_wang_2018_oi_180070.pdf#page=6) and [results supplement p2, eAppendix opening](../../../joi180070supp2_prod.pdf#page=2), visually inspected.
- **Source value/text matched:** Yes: baseline 40 hospitals and 801 patients.
- **Comparator matched:** Yes: supplement says 20 patients per cluster were prospectively included in this baseline phase.
- **Consistency rule applicable:** Yes if 20 denotes an exact per-cluster achieved count for the same reported baseline survey; it would not apply as exact arithmetic to a nominal target.
- **Calculation or logical comparison reproduced:** 40 × 20 = 800; 801 − 800 = 1, exact integer tolerance zero.
- **Necessary inputs available:** Hospital total, patient total, and per-cluster statement are available; per-cluster counts are not.
- **Exact missing inputs or definitions:** Whether 20 is achieved count or intended target, and the finalized baseline enrollment count for each hospital.
- **Source-grounded alternative interpretation:** Recruitment may have exceeded a nominal target in one cluster; no cluster-level record is supplied to establish this.
- **Direct observation versus inferred explanation:** Printed counts/statement are direct; interpreting 20 as an exact achieved count is conditional; over-recruitment is an inferred explanation.
- **Exact remaining human question:** Was 20 patients per cluster an exact achieved count or a target, and what cluster counts produced the reported 801?
- **Classification:** Category Denominator, proportion, or total inconsistency. Main baseline table and retrospective eAppendix reporting the conducted baseline survey are both REPORT by content; the eAppendix is not a prospective plan. Relationship type S_C; All relationships S_C; Review domain statistical_results. Confirmed without change. Ambiguity: nominal target wording or snapshot.
- **Evidence state:** recorded_candidate. Determining fact: source reports an achieved-sounding 20 per cluster and a total 801 in the matched baseline phase, preserving the registered exact-count conditional question.

## C015 — Dyslipidemia totals differ across the same full cohort's partitions

- **Location found:** Yes. [Main p6, Table 1 Dyslipidemia and patient totals](../../../jama_wang_2018_oi_180070.pdf#page=6) and [results supplement p5, eTable 2 Dyslipidemia and partition-denominator cells](../../../joi180070supp2_prod.pdf#page=5), visually inspected. [Main p4 Results](../../../jama_wang_2018_oi_180070.pdf#page=4) identifies the eTable 2 baseline characteristics as those with/without one-year mRS.
- **Source value/text matched:** Yes: main intervention 305/2400 (12.7) and control 291/2400 (12.1).
- **Comparator matched:** Yes: eTable 2 with mRS 285/3949 (7.2%) and loss to mRS 62/851 (7.3%).
- **Consistency rule applicable:** Yes for the same baseline characteristic, dataset snapshot, and exhaustive cohort partitions; partitioning should not change its total count.
- **Calculation or logical comparison reproduced:** 2400 + 2400 = 4800 and 3949 + 851 = 4800; 305 + 291 = 596 versus 285 + 62 = 347; difference 249. Corroborating shared totals include men 3043, prior ischemic stroke 1388, diabetes 1086, hypertension 3090, CAD 609, AF 245, and smoking 2116 in both partitions.
- **Necessary inputs available:** Matched row names, all counts, complete partition totals, and article cross-reference are available. Patient-level recoding/data-version details are unavailable.
- **Exact missing inputs or definitions:** Any different dyslipidemia criterion, records, missingness treatment, or data snapshot between the two tables.
- **Source-grounded alternative interpretation:** An undocumented variable recoding or snapshot could explain the difference, although seven other displayed characteristic totals corroborate common-cohort alignment.
- **Direct observation versus inferred explanation:** Counts and repeated characteristic names are direct; partition sums are derived; common-definition identity is source-supported but cannot be proved at record level.
- **Exact remaining human question:** Which dyslipidemia definition/data snapshot generated each table, and how should the 596 and 347 full-cohort totals be reconciled?
- **Classification:** Category Cross-document numeric inconsistency. All compared table content is REPORT: main and results supplement. Relationship type S_C; All relationships S_C; Review domain report_internal_inconsistency. Confirmed without change. Ambiguity: possible recoding/snapshot.
- **Evidence state:** recorded_candidate. Determining fact: direct-source counts reproduce a 249-person discrepancy across exhaustive same-sized partitions with independent source support for cohort alignment.

## C016 — NIHSS medians differ across exhaustive cohort partitions

- **Location found:** Yes. [Main p6, Table 1 NIHSS at admission and arm totals](../../../jama_wang_2018_oi_180070.pdf#page=6), [results supplement p5, eTable 2 NIHSS at admission and group denominator cells](../../../joi180070supp2_prod.pdf#page=5), and contextual [main p4 missing-score paragraph/Results eTable 2 reference](../../../jama_wang_2018_oi_180070.pdf#page=4), visually inspected.
- **Source value/text matched:** Yes: two arm patient groups n = 2400 each have median 4, IQR 2–6.
- **Comparator matched:** Yes: mRS availability groups displayed through denominators 3949 and 851 both have NIHSS median 3, IQR 2–6. The score range 0–42 is printed.
- **Consistency rule applicable:** Conditional order-statistic check for the identical 4800 integer NIHSS inputs under a common conventional quantile and imputation/data stage. Patient totals alone do not establish each NIHSS median's actual observation count.
- **Calculation or logical comparison reproduced:** If each 2400-score conventional median is exactly 4, at most 1200 scores per arm can be ≤3, hence at most 2400 pooled. This bound also holds if an integer display 4 rounds a conventional half-integer median 3.5. If each odd availability group uses all 3949/851 scores and has median 3, at least (3949 + 1)/2 = 1975 and (851 + 1)/2 = 426 scores are ≤3, totaling at least 2401. These bounds cannot both hold for the same full score set. This is a conditional diagnostic, not reconstruction of a corrected median.
- **Necessary inputs available:** Printed medians, IQRs, patient/group totals, score scale, and cross-reference are available. Actual NIHSS observation counts by each partition, quantile details, and score/imputation snapshots are not available.
- **Exact missing inputs or definitions:** NIHSS-specific n in all four groups; which group contains the one missing score; whether medians use pre- or post-imputation values; rounding/quantile convention; whether score sets are identical. One omitted score can change an odd group's required ≤3 bound by one and bridge this strictly one-observation contradiction. Thus the patient totals cannot be silently promoted to score counts.
- **Source-grounded alternative interpretation:** Main p4 explicitly reports one missing NIHSS score and replacement by 3. Different omission/imputation stages or observation counts can affect the rank diagnostic even when patient cohort totals match; that passage does not prove both tables used identical score inputs.
- **Direct observation versus inferred explanation:** The same named admission-NIHSS row prints medians 4/4 versus 3/3 directly. The incompatibility is derived only under stated score-count/quantile conditions; a particular missingness mechanism is not established.
- **Exact remaining human question:** What NIHSS-specific counts and imputation/quantile/data stages produced each table's medians, and do all four summaries partition the same 4800 scores?
- **Classification:** Category Cross-document numeric inconsistency. Compared table locations are REPORT in main and results supplement. Relationship type S_C; All relationships S_C; Review domain report_internal_inconsistency. Confirmed without change. Imputation paragraph is contextual, not an additional discrepancy relationship; C007 keeps its separate reference-population question. Ambiguity: actual score counts and data/quantile stage.
- **Evidence state:** recorded_candidate. Determining fact: both matched-source median pairs are printed as registered and the registered conditional diagnostic is reproduced, pending explicitly named score-count/quantile definitions. The record does not elevate the diagnostic to an unconditional contradiction.

## C017 — Composite descriptions imply different aggregation weights

- **Location found:** Yes. [Main p3, Outcomes composite definition](../../../jama_wang_2018_oi_180070.pdf#page=3), [main p7, Table 2 composite mean (SD)](../../../jama_wang_2018_oi_180070.pdf#page=7), [PLAN p16, lines216–219](../../../joi180070supp1_prod.pdf#page=16), and [results supplement p2, eAppendix formula and same-endpoint statement](../../../joi180070supp2_prod.pdf#page=2), visually inspected. [Main p4 opportunity-level analysis](../../../jama_wang_2018_oi_180070.pdf#page=4) was checked as distinct context.
- **Source value/text matched:** Yes: main says the composite was calculated for each patient and then averaged; Table 2 mean (SD) is 88.2 (15.1) and 84.8 (18.2).
- **Comparator matched:** Yes: PLAN and reported eAppendix say total interventions performed among eligible patients divided by total possible interventions among eligible patients. The eAppendix explicitly claims the same endpoint definition as the randomized phase and reports baseline 80.2%/79.5%.
- **Consistency rule applicable:** Yes as a conditional aggregation-definition comparison. Averaging patient ratios and pooling opportunities are generally different weighting rules when patients have different eligibility totals.
- **Calculation or logical comparison reproduced:** Patient mean is (1/n)Σ(m_i/e_i); pooled ratio is Σm_i/Σe_i = Σ[e_i/Σe_j](m_i/e_i). Their weights differ unless eligible totals are constant or special cancellations occur. Actual numerical differences cannot be calculated from supplied summaries.
- **Necessary inputs available:** Both wording/formula constructions are available. Patient-level m_i/e_i, cluster aggregation details, and implementation are absent.
- **Exact missing inputs or definitions:** Whether totals among eligible patients denotes pooled opportunities or patient-specific totals subsequently averaged; weighting across patients/hospitals and definition used in each phase.
- **Source-grounded alternative interpretation:** Aggregate wording may omit an implicit per-patient intermediate step. Main p4's opportunity-level GEE/OR analysis is a separate inferential estimand and does not disprove or redefine the descriptive mean (SD).
- **Direct observation versus inferred explanation:** Different definition wording is direct; translating the aggregate wording into a pooled ratio is explicitly conditional; no incorrect descriptive percentage is established.
- **Exact remaining human question:** What patient/opportunity/hospital weighting produced each descriptive composite summary, and does the aggregate wording intend the same patient-average construction?
- **Classification:** Category Measure, label, or scale inconsistency. Main definition/table/analysis and retrospective baseline eAppendix are REPORT; prospective PLAN outcome definition is PLAN. Relationship type P_R; All relationships P_R, S_C; Review domain protocol_report. P_R compares main per-patient averaging with PLAN aggregate wording; S_C compares main with reported baseline aggregate wording and its same-endpoint claim. PLAN and eAppendix agree and do not create P_P; opportunity-level GEE is contextual and adds no S_W. P_R precedence confirmed without change. Ambiguity: implicit aggregation step.
- **Evidence state:** recorded_candidate. Determining fact: direct source wording reproduces the registered conditional weighting difference; missing individual inputs preclude quantifying any actual percentage effect.

## C018 — Mortality prose and in-hospital AD P value have different significance interpretations

- **Location found:** Yes. [Main p5, Clinical Events final mortality sentence](../../../jama_wang_2018_oi_180070.pdf#page=5), [main p8, Table 3 in-hospital death and Figure 2B](../../../jama_wang_2018_oi_180070.pdf#page=8), and [main p4, statistical significance convention](../../../jama_wang_2018_oi_180070.pdf#page=4), visually inspected.
- **Source value/text matched:** Yes: no significant difference in total mortality rates in the hospital and at 3, 6, and 12 months, citing Figure 2B.
- **Comparator matched:** Yes: in-hospital Table 3 adjusted absolute-difference P = .009, alongside HR P = .14. Main p4 specifies P less than .05 and two-sided tests. Figure 2B carries 12-month HR P = .21.
- **Consistency rule applicable:** Yes if the unqualified mortality sentence covers both displayed effect columns. AD .009 is below the stated threshold; HR .14 is above it. Different estimands/tests need not have identical significance.
- **Calculation or logical comparison reproduced:** .009 < .05; .14 > .05. AD significant-by-declared-threshold conflicts with a literal blanket reading; an HR-only reading coheres with the paired HR and Figure 2B. No CI inversion is needed for this separate prose comparison.
- **Necessary inputs available:** Printed sentence, AD/HR P values, column assignment, threshold, and figure citation are present. Intended prose scope is not explicitly stated.
- **Exact missing inputs or definitions:** Whether total mortality sentence summarizes HR/time-to-event tests exclusively or every displayed AD result; whether the AD P value is correctly printed.
- **Source-grounded alternative interpretation:** The sentence's explicit Figure 2B citation and HR analyses in Data Analysis support an HR-focused summary. This alternative does not change the observed unqualified wording.
- **Direct observation versus inferred explanation:** Sentence and P values are direct. Calling it a blanket interpretation is a conditional reading; attributing a wrong test or transcription is unconfirmed.
- **Exact remaining human question:** Which mortality estimand/test does the sentence summarize, and how should its scope relate to in-hospital AD P = .009?
- **Classification:** Category Statistical reporting inconsistency. All compared locations are REPORT in the same main article. Relationship type S_W; All relationships S_W; Review domain statistical_results. Confirmed without change. Ambiguity: HR-only versus blanket prose scope. The separate C019 CI/test question is not this comparator.
- **Evidence state:** recorded_candidate. Determining fact: visually confirmed AD .009 and unqualified mortality nonsignificance sentence reproduce the registered conditional scope mismatch; an HR-specific interpretation remains source-grounded.

## C019 — In-hospital death CI and paired P value show different inferential signals

- **Location found:** Yes. [Main p8, Table 3 Death/In hospital AD/CI/AD P columns and footnote a](../../../jama_wang_2018_oi_180070.pdf#page=8), with [main p4, analysis and inferential conventions](../../../jama_wang_2018_oi_180070.pdf#page=4), visually inspected.
- **Source value/text matched:** Yes: death 11/2400 versus 23/2400; adjusted AD −0.7 percentage point, 95% CI −1.1 to positive 0.2. Source image confirms the positive upper endpoint.
- **Comparator matched:** Yes: the P value directly adjacent to the AD column is .009. Separate HR is 0.96 (0.90–1.02), P = .14 and was not used as the AD comparator. Main p4 supplies 95% CIs, two-sided tests, and significance threshold P < .05.
- **Consistency rule applicable:** Conditional: a 95% CI obtained by inversion of the identical two-sided α = .05 test should exclude zero when that test's P = .009. The package does not establish shared test/CI construction. Original-scale symmetry is only an additional diagnostic condition, not a supplied method.
- **Calculation or logical comparison reproduced:** −1.1 < 0 < +0.2 while .009 < .05. CI midpoint (−1.1 + 0.2)/2 = −0.45 differs from estimate −0.7 by 0.25. For nearest-tenth rounding, midpoint is bounded approximately [−0.50, −0.40], while estimate lies [−0.75, −0.65]; these cannot be a symmetric original-scale interval around the estimate. No Wald SE, corrected endpoint, or reconstructed P was asserted.
- **Necessary inputs available:** Displayed estimate, endpoints, confidence level, adjacent P value, sidedness, significance convention, and covariate-adjustment labels are available. The inputs needed to establish a common CI/test identity are absent.
- **Exact missing inputs or definitions:** AD model/link/estimand, confidence-interval algorithm and scale, test statistic/null construction, variance estimator and cluster handling, degrees of freedom, unrounded values, and whether CI and P derive from the same fitted contrast and test inversion.
- **Source-grounded alternative interpretation:** A non-inverted/asymmetric CI or different inferential construction could break the usual CI/P equivalence. General methods/adjustment footnotes do not resolve it. A transcription is also possible but is not established by the source.
- **Direct observation versus inferred explanation:** Positive upper endpoint and small paired P are direct. CI/P incompatibility assumes common inversion; interval asymmetry is a reproduced diagnostic; any wrong cell or algorithm explanation is inferred.
- **Exact remaining human question:** Which AD fit, CI algorithm, test, variance/cluster convention, degrees of freedom, and unrounded values produced −0.7 (−1.1 to +0.2), P = .009, and were CI and P intended as the same inferential construction?
- **Classification:** Category Statistical reporting inconsistency. Both compared values and their method/footnote context are REPORT in the same main article. Relationship type S_W; All relationships S_W; Review domain statistical_results. Confirmed without change. Ambiguity: common CI/test construction and possible asymmetry are unestablished; HR is context only.
- **Evidence state:** recorded_candidate. Determining fact: direct source image reproduces the registered CI-includes-zero/paired-P-below-threshold signals. The mismatch remains a conditional inferential question pending the named construction definitions; source content does not supply an unconditional equivalence or a correction.

# Recheck completion

All assigned 19 stable IDs were individually rechecked without deletion, merge, renumbering, or adjudication. No classification code/category correction was required. C007 and C012 receive record_input_error for unsupported alignment premises; the other 17 preserve the registered observation/conditional question as recorded_candidate. No new missing-definition-only candidate was created. All new direct-source derivative locations, engines, exact PDF links, alternative interpretations, and unresolved human questions are documented above.
