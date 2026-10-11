# Evidence recheck part 003

Scope: C073–C106, 34 stable IDs, each retained. All are Pending Human Adjudication. This part records evidence facts and mechanically derived fields only.

Authority: current supplied PDF files. Direct Poppler 26.01.0 native/layout extraction confirmed selectable content; direct Poppler page renders were inspected for eFigures 8–12, eMethods equality glyph, protocol signed boundary graphic/combined effect phrase, and repeated boundary graphic. Existing evidence assets were locators only. No source/reused artifact changed; no web, GPU, raw-data reconstruction, or unpermitted Python was used.

Derivatives: `preprocessing/recheck003_main.txt`, `recheck003_protocol.txt`, `recheck003_amendments.txt`, `recheck003_sap.txt`, `recheck003_results.txt` use direct `pdftotext -layout` (Poppler 26.01.0). `preprocessing/recheck003_results-38.png` through `recheck003_results-42.png`, `recheck003_protocol23.png`, `recheck003_results20.png`, and `recheck003_results31.png` use direct `pdftoppm -png -scale-to 1600` (1200 for results31), Poppler 26.01.0. No OCR was required. Full text derivatives were created only under preprocessing; scientific authority remains the direct PDF pages listed below.

## C073 — Waist-to-hip ratio assigned a length unit

**Cited location found:** Yes. [Figure 2 waist-to-hip heading — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [Table 1 ratio — PDF p. 5](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=5>).

**Source printed value/text matched:** Yes. Waist-to-hip ratio, cm; subgroup thresholds <1.0 and ≥1.0.

**Comparator printed value/text matched:** Yes. Table 1 ratio means 1.01 (0.21) and 1.00 (0.18), with the same thresholds.

**Consistency rule applicable:** Applicable: dividing two circumferences measured in the same length unit cancels the unit.

**Calculation or logical comparison reproduced:** Length/length has dimension 1; cm is a length unit, so it cannot denote that ratio.

**Necessary inputs available:** Ratio name, unit and threshold are available.

**Exact missing inputs or definitions:** No raw measurement is needed; exact construction is not stated independently.

**Source-grounded alternative interpretation:** A circumference unit may have been carried into the ratio heading. A different waist measure would need its definition.

**Direct observation versus inferred explanation:** Direct: ratio name, cm and values. Inferred: inherited unit or intended repair.

**Exact remaining human question:** Does cm belong to a different variable, or is the Figure 2 ratio intended to be dimensionless?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT main Figure 2 heading and REPORT main Table 1 ratio row. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_W

**All relationships:** S_W

**Review domain:** report_internal_inconsistency

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** None

**Evidence state:** recorded_candidate

**Determining recheck fact:** The directly printed ratio heading carries cm; the dimensional comparison reproduces.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C074 — Waist-to-hip ≥1.0 point versus crude risks

**Cited location found:** Yes. [Figure 2 ≥1.0 row — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [Subgroup Methods — PDF p. 4](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>).

**Source printed value/text matched:** Yes. High 98/447; low 112/449; RR 0.92 (0.78–1.08).

**Comparator printed value/text matched:** Yes. Methods analyzes treatment × subgroup interaction in a binomial generalized linear model.

**Consistency rule applicable:** Crude-risk identity is applicable to the counts. Equality with the row point remains an explicitly named estimator question, not an assertion that all fitted ratios must be crude.

**Calculation or logical comparison reproduced:** (98/447)/(112/449) = 0.878915; rounds to 0.88, versus 0.92.

**Necessary inputs available:** Counts, arm direction, labels and model family are available.

**Exact missing inputs or definitions:** Link, model formula, covariates, point-estimator derivation/standardization and whether plotted RR is marginal or conditional.

**Source-grounded alternative interpretation:** A fitted or standardized ratio may differ from the crude arm-risk ratio.

**Direct observation versus inferred explanation:** Direct: counts, printed point and GLM interaction description for heterogeneity. Derived: crude ratio. Neither crude nor fitted point-estimator identity is established.

**Exact remaining human question:** Which link, contrast, adjustment and postprocessing generated 0.92, and does that point purport to equal the two displayed crude arm risks?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT main Figure 2 subgroup counts/point and REPORT main Methods model. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_W

**All relationships:** S_W

**Review domain:** report_internal_inconsistency

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Point-estimator alignment is unresolved; document roles/type remain within one REPORT.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Counts, RR label and point are confirmed; the registered conditional point-estimator/label question remains. The Methods GLM sentence explicitly concerns heterogeneity, so it does not independently identify or disprove the row-point estimator.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C075 — Mortality caption names extrapulmonary complications

**Cited location found:** Yes. [eFigure 11 — PDF p. 41](<../../../../joi190055supp4_prod_16092.pdf#page=41>); [eFigure 10 — PDF p. 40](<../../../../joi190055supp4_prod_16092.pdf#page=40>); [Table 3 five-day mortality — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>).

**Source printed value/text matched:** Yes. eFigure 11 title probability of death; axis 5-Day Mortality; HR 1.67 (0.40–6.97), P=.484; caption assigns 0.5% high/0.3% low to extra-pulmonary complications.

**Comparator printed value/text matched:** Yes. eFigure 10 extra-pulmonary percentages 16.9%/15.2%; main mortality 5 (0.5%)/3 (0.3%), HR 1.67 (0.40–6.97), P=.48.

**Consistency rule applicable:** Applicable: same figure's endpoint title/axis and caption should identify the same quantity.

**Calculation or logical comparison reproduced:** 0.5%/0.3% and HR/CI match mortality; extra-pulmonary comparator is 16.9%/15.2%.

**Necessary inputs available:** Endpoint labels, percentages and mortality comparator are available.

**Exact missing inputs or definitions:** Underlying endpoint code is absent; it is not needed to observe the literal label mismatch.

**Source-grounded alternative interpretation:** Caption wording may have been copied from eFigure 10; alternatively title/axis would need a different endpoint explanation.

**Direct observation versus inferred explanation:** Direct: differing endpoint labels and matching mortality values. Inferred: caption-copy mechanism.

**Exact remaining human question:** Which endpoint was plotted in eFigure 11, and should its caption name mortality or extra-pulmonary complications?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT results supplement eFigure 11 title/axis/caption and eFigure 10; REPORT main mortality row corroborates. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_W

**All relationships:** S_W

**Review domain:** report_internal_inconsistency

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** None

**Evidence state:** recorded_candidate

**Determining recheck fact:** Direct render shows mortality title/axis and an extra-pulmonary caption on the same page.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C076 — Collapsed composite OR/RR headings

**Cited location found:** Yes. [eFigure 12 global tests — PDF p. 42](<../../../../joi190055supp4_prod_16092.pdf#page=42>); [Table 3 primary — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Abstract — PDF p. 1](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=1>); [Primary outcome plan — PDF p. 2](<../../../../joi190055supp3_prod_16092.pdf#page=2>).

**Source printed value/text matched:** Yes. Global Tests header Odds Ratio (95% CI); Collapsed Composite 0.93 [0.83,1.04].

**Comparator printed value/text matched:** Yes. Main and abstract name Risk Ratio 0.93 (0.83–1.04); SAP primary analysis names risk ratio.

**Consistency rule applicable:** Applicable as a matched labeling question; OR and RR are different scales. Exact estimator identity remains conditional.

**Calculation or logical comparison reproduced:** RR=pH/pL; OR=[pH/(1−pH)]/[pL/(1−pL)]. Identical point and CI are printed under the two headings.

**Necessary inputs available:** Both literal effect labels and identical values are available.

**Exact missing inputs or definitions:** Which estimator the collapsed-composite row actually uses; whether global header has a row exception.

**Source-grounded alternative interpretation:** A separate odds-based sensitivity calculation could coincide numerically, or heading may scope differently; neither row exception is stated.

**Direct observation versus inferred explanation:** Direct: conflicting headings for identically displayed collapsed-composite point/CI. Inferred: copying or actual estimator identity.

**Exact remaining human question:** Does the Global Tests OR heading apply to Collapsed Composite, and what estimator produced that row versus main Table 3?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT supplement eFigure 12 global heading versus REPORT main primary table/abstract; PLAN final SAP corroborates RR. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** report_internal_inconsistency

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Cross-report estimator identity is conditional; SAP corroborates RR and creates no P_R discrepancy.

**Evidence state:** recorded_candidate

**Determining recheck fact:** The literal OR header above collapsed composite is confirmed in the current render; main labels identical display RR.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C077 — Synthetic-colloid count P differs

**Cited location found:** Yes. [Synthetic colloids count — PDF p. 8](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>); [eTable 3 — PDF p. 24](<../../../../joi190055supp4_prod_16092.pdf#page=24>).

**Source printed value/text matched:** Yes. Main binary receipt 74 (7.5%)/56 (5.7%), n=989/987, P=.09.

**Comparator printed value/text matched:** Yes. Supplement same receipt counts/populations P=0.10; next amount row 50 (211)/35 (171), P=.09 is a different row.

**Consistency rule applicable:** Applicable as repeated count-row P display comparison; equality of tests is not established.

**Calculation or logical comparison reproduced:** 0.10−0.09 = 0.01; displays have the same two-decimal precision. No tail test is substituted.

**Necessary inputs available:** Count-row identity, arm n and both P displays are available.

**Exact missing inputs or definitions:** Exact test and continuity correction/Fisher convention for each row; exact unrounded output.

**Source-grounded alternative interpretation:** Different test conventions may produce distinct P values; adjacent amount row's .09 is not the count comparator.

**Direct observation versus inferred explanation:** Direct: matched counts and distinct P displays. Inferred: test choice or transcription explanation.

**Exact remaining human question:** Were the two binary receipt P values generated with the same test/analysis set; if different, what conventions produced .09 and .10?

**Category:** Statistical reporting inconsistency

**Compared document roles:** REPORT main Table 2 receipt row versus REPORT results supplement eTable 3 receipt row. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** statistical_results

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** None

**Evidence state:** recorded_candidate

**Determining recheck fact:** Direct native source confirms different P values for the same printed binary receipt counts.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C078 — Mild respiratory failure oxygen boundary

**Cited location found:** Yes. [Table 3 footnote d — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [Mild failure counts — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [eMethods 2.8 — PDF p. 20](<../../../../joi190055supp4_prod_16092.pdf#page=20>).

**Source printed value/text matched:** Yes. Main mild response to 2 L or less; mild counts high135/989 and low154/987.

**Comparator printed value/text matched:** Yes. Supplement responds to oxygen =2 L/min; moderate >2 L/min. The equality glyph is confirmed visually.

**Consistency rule applicable:** Applicable: equality and inclusive upper bound have different membership below 2 L/min.

**Calculation or logical comparison reproduced:** A response at 1 L/min satisfies ≤2 but not =2. No revised count is inferable.

**Necessary inputs available:** Literal criteria and associated mild counts are available.

**Exact missing inputs or definitions:** Operational oxygen test and endpoint dictionary; classification below 2 L/min.

**Source-grounded alternative interpretation:** The equality sign may summarize a test at exactly 2 L/min or stand in for ≤.

**Direct observation versus inferred explanation:** Direct: different printed boundary statements. Inferred: which rule actually generated the numerator.

**Exact remaining human question:** How were patients responding below 2 L/min classified, and which boundary generated the mild respiratory-failure counts?

**Category:** Analysis-unit or population inconsistency

**Compared document roles:** REPORT main Table 3 footnote versus REPORT supplement eMethods definition. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** statistical_results

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Operational equivalence of an exact-2 L test and a ≤2 response criterion is unresolved.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Current source image confirms =2, while main prints 2 L or less.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C079 — Emergency counts across baseline/surgery tables

**Cited location found:** Yes. [Table 1 emergency — PDF p. 5](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=5>); [eTable 6 priority — PDF p. 27](<../../../../joi190055supp4_prod_16092.pdf#page=27>).

**Source printed value/text matched:** Yes. Main Emergency procedure 21 (2.1%)/20 (2.0%), arm n989/987.

**Comparator printed value/text matched:** Yes. Supplement Emergency13/11, Urgent9/13, Elective962/958 under n989/987.

**Consistency rule applicable:** Applicable as repeated-label comparison conditional on timing/category mapping; not proof of identical operational variables.

**Calculation or logical comparison reproduced:** Main−supplement emergency =8 high/9 low; emergency+urgent =22/24; priority totals =984/982.

**Necessary inputs available:** Printed counts, labels and observed category totals are available.

**Exact missing inputs or definitions:** Baseline versus surgical-time definition, urgency crosswalk, missing records and actual observed denominators.

**Source-grounded alternative interpretation:** Different timings/categories or available cases could explain values; simple emergency+urgent pooling does not reproduce main.

**Direct observation versus inferred explanation:** Direct: repeated label with different counts and incomplete priority sums. Derived: differences/sums. Inferred: variable identity.

**Exact remaining human question:** Are main emergency procedure and supplemental emergency priority the same field/time; if so, how are 21/20 reconciled with 13/11, and if not, what mapping defines them?

**Category:** Cross-document numeric inconsistency

**Compared document roles:** REPORT main baseline Table 1 emergency procedure versus REPORT supplement surgical priority eTable 6. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** report_internal_inconsistency

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Emergency timing/category and available-case identity remain unconfirmed.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Exact repeated emergency counts differ as registered; the missing mapping remains the named conditional question.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C080 — Hypoxemia duration-qualified/unqualified definitions

**Cited location found:** Yes. [Secondary outcomes — PDF p. 3](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=3>); [Table 3 count — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Adverse-event footnote — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [eMethods secondary definitions — PDF p. 21](<../../../../joi190055supp4_prod_16092.pdf#page=21>); [Secondary parameters — PDF p. 12](<../../../../joi190055supp1_prod_16092.pdf#page=12>); [RM-related event fields — PDF p. 19](<../../../../joi190055supp1_prod_16092.pdf#page=19>); [Abstract — PDF p. 1](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=1>).

**Source printed value/text matched:** Yes. Main Methods: SpO2 ≤92% for >1 minute; Table 3: 49/989 (5.0%)/134/987 (13.6%).

**Comparator printed value/text matched:** Yes. Main footnote: SpO2 ≤92%, or >5% decline if already <92%, without repeating duration. Supplement threshold-only description also omits duration. Protocol p.12 states duration, whereas p.19 describes new recruitment-related threshold/drop event fields.

**Consistency rule applicable:** Only conditional: a shorter definition is not an affirmative statement that brief events were included. Field/window identity is needed for a numerator-definition contradiction.

**Calculation or logical comparison reproduced:** Printed duration appears in body and is not repeated in footnote/eMethods. No count change can be calculated. The below-baseline drop clause does not itself contradict the threshold because the patient remains below it.

**Necessary inputs available:** All cited text and counts are available.

**Exact missing inputs or definitions:** Counted event field, duration filtering, whole-intraoperative versus recruitment-only window, and whether footnote/eMethods abbreviate the Methods.

**Source-grounded alternative interpretation:** Abbreviated summaries can retain the stated duration implicitly. The protocol expressly separates recruitment-related event fields from its broader secondary-parameter description.

**Direct observation versus inferred explanation:** Direct: duration presence/omission and printed counts. Unsupported inference: omission means no duration restriction or that separate protocol fields are interchangeable.

**Exact remaining human question:** Which exact variable/window generated 49/134 hypoxemia, did it apply the Methods duration, and are footnote/eMethods abbreviated descriptions of that same variable?

**Category:** Analysis-unit or population inconsistency

**Compared document roles:** REPORT main Methods/count footnote versus REPORT supplement eMethods; PLAN protocol duration/RM fields corroborate the two descriptions. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Review domain:** statistical_results

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. A within-main REPORT comparison is also registered; S_C takes precedence over S_W. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Original S_C plus S_W comparison is retained as the registered relationship; plan corroboration adds no P_R/P_P discrepancy.

**Evidence state:** record_input_error

**Determining recheck fact:** The comparison treats omission of a qualifier as a different operational rule, but source supplies no affirmative no-duration rule or field identity; residual count discrepancy cannot be settled.

**Suggested review disposition:** discuss (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C081 — Hypotension duration-qualified/unqualified definitions

**Cited location found:** Yes. [Secondary outcomes — PDF p. 3](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=3>); [Table 3 count — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Adverse-event footnote — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [eMethods secondary definitions — PDF p. 21](<../../../../joi190055supp4_prod_16092.pdf#page=21>); [Secondary parameters — PDF p. 12](<../../../../joi190055supp1_prod_16092.pdf#page=12>); [RM-related event fields — PDF p. 19](<../../../../joi190055supp1_prod_16092.pdf#page=19>).

**Source printed value/text matched:** Yes. Main Methods: systolic pressure <90 mm Hg for >2 minutes; Table 3: 313/989 (31.6%)/170/987 (17.2%).

**Comparator printed value/text matched:** Yes. Main footnote: systolic pressure <90 mm Hg, or >10 mm Hg decline if already <90, without repeating duration. Supplement threshold-only description also omits duration. Protocol p.12 states duration, whereas p.19 describes new recruitment-related threshold/drop event fields.

**Consistency rule applicable:** Only conditional: a shorter definition is not an affirmative statement that brief events were included. Field/window identity is needed for a numerator-definition contradiction.

**Calculation or logical comparison reproduced:** Printed duration appears in body and is not repeated in footnote/eMethods. No count change can be calculated. The below-baseline drop clause does not itself contradict the threshold because the patient remains below it.

**Necessary inputs available:** All cited text and counts are available.

**Exact missing inputs or definitions:** Counted event field, duration filtering, whole-intraoperative versus recruitment-only window, and whether footnote/eMethods abbreviate the Methods.

**Source-grounded alternative interpretation:** Abbreviated summaries can retain the stated duration implicitly. The protocol expressly separates recruitment-related event fields from its broader secondary-parameter description.

**Direct observation versus inferred explanation:** Direct: duration presence/omission and printed counts. Unsupported inference: omission means no duration restriction or that separate protocol fields are interchangeable.

**Exact remaining human question:** Which exact variable/window generated 313/170 hypotension, did it apply the Methods duration, and are footnote/eMethods abbreviated descriptions of that same variable?

**Category:** Analysis-unit or population inconsistency

**Compared document roles:** REPORT main Methods/count footnote versus REPORT supplement eMethods; PLAN protocol duration/RM fields corroborate the two descriptions. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C, S_W

**Review domain:** statistical_results

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. A within-main REPORT comparison is also registered; S_C takes precedence over S_W. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Original S_C plus S_W comparison is retained as the registered relationship; plan corroboration adds no P_R/P_P discrepancy.

**Evidence state:** record_input_error

**Determining recheck fact:** The comparison treats omission of a qualifier as a different operational rule, but source supplies no affirmative no-duration rule or field identity; residual count discrepancy cannot be settled.

**Suggested review disposition:** discuss (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C082 — Conditional thoracic VAS moment bound

**Cited location found:** Yes. [eTable 7 low day 2 thoracic — PDF p. 28](<../../../../joi190055supp4_prod_16092.pdf#page=28>); [10 cm VAS definition — PDF p. 17](<../../../../joi190055supp1_prod_16092.pdf#page=17>); [Postoperative VAS assessment — PDF p. 20](<../../../../joi190055supp1_prod_16092.pdf#page=20>).

**Source printed value/text matched:** Yes. Low day-2 VAS thoracic—cm, mean (SD), No.: 1.4 (3.9), 841; high1.3 (0.8),838, P=.34.

**Comparator printed value/text matched:** Yes. Protocol p.17 names Visual Analogue Scale (10 cm) for dyspnea/thoracic/abdominal pain; p.20 repeats postoperative assessment but no numeric endpoints.

**Consistency rule applicable:** Applicable only if postoperative scores are zero-origin 0–10 cm distances on the protocol line: sample variance ≤n/(n−1) m(10−m).

**Calculation or logical comparison reproduced:** At m1.4,n841, maximum SD=3.47194. Allowing mean rounding up to1.45 gives 3.52310, below minimum rounding-consistent SD3.85 by 0.32690 cm.

**Necessary inputs available:** Mean, SD label, n, cm and 10 cm line length are available.

**Exact missing inputs or definitions:** Numerical scoring origin/endpoints, postoperative identity with the baseline-defined scale, transformation and SD convention.

**Source-grounded alternative interpretation:** A shifted 10 cm interval does not yield the mean-dependent 0–10 bound; its universal maximum SD is about5.00. Different range/transformation could reconcile the tuple.

**Direct observation versus inferred explanation:** Direct: moment tuple and 10 cm plan wording. Conditional inference: zero-origin 0–10 postoperative support. No standard external VAS endpoints are assumed.

**Exact remaining human question:** Were postoperative thoracic scores zero-origin 0–10 cm scores on the protocol line, and does the low Day 2 tuple correctly read mean1.4, SD3.9, n841; if different, what origin/range/transformation was used?

**Category:** Numeric or arithmetic inconsistency

**Compared document roles:** REPORT supplement eTable 7 thoracic summary versus PLAN protocol VAS scale/assessment. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** P_R

**All relationships:** P_R

**Review domain:** protocol_report

**Classification rationale:** The reported completed-trial summary is REPORT and the prospective measurement definition is PLAN; the substantive conditional scale comparison is P_R. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** P_R is conditional scale-to-report comparison; numerical endpoints and postoperative identity are not printed.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Direct source confirms the tuple and 10 cm plan description; the registered bounded-support question remains conditional on its explicitly missing origin/scale identity.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C083 — Conditional event-count mean versus component sum

**Cited location found:** Yes. [eTable 9 Count events — PDF p. 30](<../../../../joi190055supp4_prod_16092.pdf#page=30>); [Table 3 twelve components — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Randomization flow — PDF p. 3](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=3>); [Count analysis definition — PDF p. 3](<../../../../joi190055supp3_prod_16092.pdf#page=3>).

**Source printed value/text matched:** Yes. eTable 9 n989/987; Count events high0.35(0.88), low0.38(0.86); separately Median(IQR)0(0–0) both.

**Comparator printed value/text matched:** Yes. Main high counts135,42,30,44,43,14,17,12,10,2,3,1; low154,58,36,55,21,18,9,10,10,1,1,3. SAP describes number of positive components; main randomization1011/1002.

**Consistency rule applicable:** Applicable if the unlabeled first summary is mean(SD) of those same twelve binary component counts in the displayed populations: mean equals summed component numerators/n.

**Calculation or logical comparison reproduced:** High sum353;353/989=0.356926→0.36, versus0.35. Low sum376;376/987=0.380952→0.38. High two-decimal0.35 permits integer totals342–351 under ordinary rounding. Alternative353/1011=0.349159→0.35 and376/1002=0.375250→0.38.

**Necessary inputs available:** All twelve component counts, displayed n, summary values, randomized n and planned count definition are available.

**Exact missing inputs or definitions:** First summary statistic label, actual event grouping/time rule, analysis n, missing-participant treatment and rounding convention.

**Source-grounded alternative interpretation:** All-randomized denominators with suitable handling reproduce both numbers arithmetically; different grouping/statistic or truncation could do so. This does not prove their use.

**Direct observation versus inferred explanation:** Direct: counts and summary. Derived: sums/ratios. Conditional: first summary mean of the same components and full displayed n; overlap alone does not alter sum identity.

**Exact remaining human question:** Is 0.35(0.88) the mean(SD) of these twelve component counts among989 high participants; if so how does353/989 reconcile, and otherwise what statistic/grouping/window/denominator and participant handling define it?

**Category:** Denominator, proportion, or total inconsistency

**Compared document roles:** REPORT supplement eTable 9 count summary versus REPORT main Table 3 component numerators; REPORT main randomized denominator is an alternative; PLAN SAP count definition corroborates. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** statistical_results

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** First summary and realized count aggregation are not explicitly defined. SAP corroborates count concept without a P_R discrepancy.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Count tuple and component totals are confirmed; arithmetic reproduces the registered conditional high-arm rounding question.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C084 — Median follow-up versus day-five risk count — eFigure 8 PPC

**Cited location found:** Yes. [eFigure 8 PPC caption and risk table — PDF p. 38](<../../../../joi190055supp4_prod_16092.pdf#page=38>).

**Source printed value/text matched:** Yes. Caption median follow-up4(2–5) days.

**Comparator printed value/text matched:** Yes. Direct image risk table at ticks0,1,2,3,4,5: low 987, 987, 791, 767, 760, 756; high 989, 989, 827, 797, 788, 785. Baseline total1976; day-five total1541.

**Consistency rule applicable:** Applicable only if caption duration and plotted time share the same origin, elapsed-day scale and observed/censor-time definition; a median ≤4 cannot coexist with >half observed beyond4 on that same scale.

**Calculation or logical comparison reproduced:** 1976/2=988; day-five total1541 exceeds988 by553. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5.

**Necessary inputs available:** Caption, all twelve risk counts, ticks and baseline total are available.

**Exact missing inputs or definitions:** Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment.

**Source-grounded alternative interpretation:** Follow-up could count elapsed assessment intervals while axis labels postoperative day1 through5, or report assessment duration while administrative ascertainment persists. No particular survival/censoring mechanism is invented.

**Direct observation versus inferred explanation:** Direct: caption and current rendered table. Derived: totals and conditional half-sample bound. Unsupported without definition: equating caption4 to axis elapsed time4.

**Exact remaining human question:** For eFigure 8 PPC, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary?

**Category:** Denominator, proportion, or total inconsistency

**Compared document roles:** REPORT supplement eFigure 8 PPC caption versus same-page risk table. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_W

**All relationships:** S_W

**Review domain:** statistical_results

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C085 — Median follow-up versus day-five risk count — eFigure 9 severe PPC

**Cited location found:** Yes. [eFigure 9 severe PPC caption and risk table — PDF p. 39](<../../../../joi190055supp4_prod_16092.pdf#page=39>).

**Source printed value/text matched:** Yes. Caption median follow-up4(2–5) days.

**Comparator printed value/text matched:** Yes. Direct image risk table at ticks0,1,2,3,4,5: low 987, 987, 791, 767, 760, 756; high 989, 989, 827, 797, 788, 785. Baseline total1976; day-five total1541.

**Consistency rule applicable:** Applicable only if caption duration and plotted time share the same origin, elapsed-day scale and observed/censor-time definition; a median ≤4 cannot coexist with >half observed beyond4 on that same scale.

**Calculation or logical comparison reproduced:** 1976/2=988; day-five total1541 exceeds988 by553. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5.

**Necessary inputs available:** Caption, all twelve risk counts, ticks and baseline total are available.

**Exact missing inputs or definitions:** Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment.

**Source-grounded alternative interpretation:** Follow-up could count elapsed assessment intervals while axis labels postoperative day1 through5, or report assessment duration while administrative ascertainment persists. No particular survival/censoring mechanism is invented.

**Direct observation versus inferred explanation:** Direct: caption and current rendered table. Derived: totals and conditional half-sample bound. Unsupported without definition: equating caption4 to axis elapsed time4.

**Exact remaining human question:** For eFigure 9 severe PPC, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary?

**Category:** Denominator, proportion, or total inconsistency

**Compared document roles:** REPORT supplement eFigure 9 severe PPC caption versus same-page risk table. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_W

**All relationships:** S_W

**Review domain:** statistical_results

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C086 — Median follow-up versus day-five risk count — eFigure 10 extrapulmonary

**Cited location found:** Yes. [eFigure 10 extrapulmonary caption and risk table — PDF p. 40](<../../../../joi190055supp4_prod_16092.pdf#page=40>).

**Source printed value/text matched:** Yes. Caption median follow-up4(2–5) days.

**Comparator printed value/text matched:** Yes. Direct image risk table at ticks0,1,2,3,4,5: low 987, 987, 898, 873, 852, 845; high 989, 989, 896, 861, 834, 828. Baseline total1976; day-five total1673.

**Consistency rule applicable:** Applicable only if caption duration and plotted time share the same origin, elapsed-day scale and observed/censor-time definition; a median ≤4 cannot coexist with >half observed beyond4 on that same scale.

**Calculation or logical comparison reproduced:** 1976/2=988; day-five total1673 exceeds988 by685. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5.

**Necessary inputs available:** Caption, all twelve risk counts, ticks and baseline total are available.

**Exact missing inputs or definitions:** Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment.

**Source-grounded alternative interpretation:** Follow-up could count elapsed assessment intervals while axis labels postoperative day1 through5, or report assessment duration while administrative ascertainment persists. No particular survival/censoring mechanism is invented.

**Direct observation versus inferred explanation:** Direct: caption and current rendered table. Derived: totals and conditional half-sample bound. Unsupported without definition: equating caption4 to axis elapsed time4.

**Exact remaining human question:** For eFigure 10 extrapulmonary, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary?

**Category:** Denominator, proportion, or total inconsistency

**Compared document roles:** REPORT supplement eFigure 10 extrapulmonary caption versus same-page risk table. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_W

**All relationships:** S_W

**Review domain:** statistical_results

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C087 — Median follow-up versus day-five risk count — eFigure 11 mortality

**Cited location found:** Yes. [eFigure 11 mortality caption and risk table — PDF p. 41](<../../../../joi190055supp4_prod_16092.pdf#page=41>).

**Source printed value/text matched:** Yes. Caption median follow-up4(2–5) days.

**Comparator printed value/text matched:** Yes. Direct image risk table at ticks0,1,2,3,4,5: low 987, 987, 987, 987, 986, 986; high 989, 989, 988, 987, 985, 985. Baseline total1976; day-five total1971.

**Consistency rule applicable:** Applicable only if caption duration and plotted time share the same origin, elapsed-day scale and observed/censor-time definition; a median ≤4 cannot coexist with >half observed beyond4 on that same scale.

**Calculation or logical comparison reproduced:** 1976/2=988; day-five total1971 exceeds988 by983. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5.

**Necessary inputs available:** Caption, all twelve risk counts, ticks and baseline total are available.

**Exact missing inputs or definitions:** Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment.

**Source-grounded alternative interpretation:** Follow-up could count elapsed assessment intervals while axis labels postoperative day1 through5, or report assessment duration while administrative ascertainment persists. No particular survival/censoring mechanism is invented.

**Direct observation versus inferred explanation:** Direct: caption and current rendered table. Derived: totals and conditional half-sample bound. Unsupported without definition: equating caption4 to axis elapsed time4.

**Exact remaining human question:** For eFigure 11 mortality, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary?

**Category:** Denominator, proportion, or total inconsistency

**Compared document roles:** REPORT supplement eFigure 11 mortality caption versus same-page risk table. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_W

**All relationships:** S_W

**Review domain:** statistical_results

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C088 — Mild respiratory failure sensitivity-forest point versus crude risks

**Cited location found:** Yes. [eFigure 12 Mild respiratory failure — PDF p. 42](<../../../../joi190055supp4_prod_16092.pdf#page=42>); [Table 3 component counts — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Table 3 footnote b — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [Individual component sensitivity plan — PDF p. 3](<../../../../joi190055supp3_prod_16092.pdf#page=3>).

**Source printed value/text matched:** Yes. Forest Risk Ratio (99.58% CI): 0.92 [0.76,1.12].

**Comparator printed value/text matched:** Yes. Main high135/989 and low154/987; final SAP expressly specifies a generalized linear model for individual-component sensitivity analysis with 99.58% Bonferroni intervals.

**Consistency rule applicable:** Crude RR identity is applicable to main counts, but the equality check against this separately fitted sensitivity point needs an estimator/population alignment not supplied by the sources.

**Calculation or logical comparison reproduced:** (135/989)/(154/987)=0.874851; absolute distance from0.92=0.045149, larger than .005. Interval is positive, ordered and contains its printed point (0.76≤0.92≤1.12). This diagnostic does not reproduce a fitted GLM.

**Necessary inputs available:** Printed forest point/CI, main component counts/populations, RR labels and GLM sensitivity family are available.

**Exact missing inputs or definitions:** Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output.

**Source-grounded alternative interpretation:** A model-based/standardized ratio under a distinct analysis population or estimator can differ from the raw main-arm ratio. Bonferroni width alone does not explain a point shift, but model definition can.

**Direct observation versus inferred explanation:** Direct: point/CI/counts and explicit sensitivity GLM plan. Derived: crude main-count diagnostic. Unsupported inference: sensitivity GLM point is the crude marginal RR calculated from main counts.

**Exact remaining human question:** For Mild respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.92, and does its RR mean the crude main-arm ratio or a model-defined ratio?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** report_internal_inconsistency

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Evidence state:** record_input_error

**Determining recheck fact:** The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled.

**Suggested review disposition:** discuss (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C089 — Moderate respiratory failure sensitivity-forest point versus crude risks

**Cited location found:** Yes. [eFigure 12 Moderate respiratory failure — PDF p. 42](<../../../../joi190055supp4_prod_16092.pdf#page=42>); [Table 3 component counts — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Table 3 footnote b — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [Individual component sensitivity plan — PDF p. 3](<../../../../joi190055supp3_prod_16092.pdf#page=3>).

**Source printed value/text matched:** Yes. Forest Risk Ratio (99.58% CI): 0.83 [0.59,1.17].

**Comparator printed value/text matched:** Yes. Main high42/989 and low58/987; final SAP expressly specifies a generalized linear model for individual-component sensitivity analysis with 99.58% Bonferroni intervals.

**Consistency rule applicable:** Crude RR identity is applicable to main counts, but the equality check against this separately fitted sensitivity point needs an estimator/population alignment not supplied by the sources.

**Calculation or logical comparison reproduced:** (42/989)/(58/987)=0.722674; absolute distance from0.83=0.107326, larger than .005. Interval is positive, ordered and contains its printed point (0.59≤0.83≤1.17). This diagnostic does not reproduce a fitted GLM.

**Necessary inputs available:** Printed forest point/CI, main component counts/populations, RR labels and GLM sensitivity family are available.

**Exact missing inputs or definitions:** Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output.

**Source-grounded alternative interpretation:** A model-based/standardized ratio under a distinct analysis population or estimator can differ from the raw main-arm ratio. Bonferroni width alone does not explain a point shift, but model definition can.

**Direct observation versus inferred explanation:** Direct: point/CI/counts and explicit sensitivity GLM plan. Derived: crude main-count diagnostic. Unsupported inference: sensitivity GLM point is the crude marginal RR calculated from main counts.

**Exact remaining human question:** For Moderate respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.83, and does its RR mean the crude main-arm ratio or a model-defined ratio?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** report_internal_inconsistency

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Evidence state:** record_input_error

**Determining recheck fact:** The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled.

**Suggested review disposition:** discuss (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C090 — Severe respiratory failure sensitivity-forest point versus crude risks

**Cited location found:** Yes. [eFigure 12 Severe respiratory failure — PDF p. 42](<../../../../joi190055supp4_prod_16092.pdf#page=42>); [Table 3 component counts — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Table 3 footnote b — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [Individual component sensitivity plan — PDF p. 3](<../../../../joi190055supp3_prod_16092.pdf#page=3>).

**Source printed value/text matched:** Yes. Forest Risk Ratio (99.58% CI): 0.91 [0.61,1.34].

**Comparator printed value/text matched:** Yes. Main high30/989 and low36/987; final SAP expressly specifies a generalized linear model for individual-component sensitivity analysis with 99.58% Bonferroni intervals.

**Consistency rule applicable:** Crude RR identity is applicable to main counts, but the equality check against this separately fitted sensitivity point needs an estimator/population alignment not supplied by the sources.

**Calculation or logical comparison reproduced:** (30/989)/(36/987)=0.831648; absolute distance from0.91=0.078352, larger than .005. Interval is positive, ordered and contains its printed point (0.61≤0.91≤1.34). This diagnostic does not reproduce a fitted GLM.

**Necessary inputs available:** Printed forest point/CI, main component counts/populations, RR labels and GLM sensitivity family are available.

**Exact missing inputs or definitions:** Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output.

**Source-grounded alternative interpretation:** A model-based/standardized ratio under a distinct analysis population or estimator can differ from the raw main-arm ratio. Bonferroni width alone does not explain a point shift, but model definition can.

**Direct observation versus inferred explanation:** Direct: point/CI/counts and explicit sensitivity GLM plan. Derived: crude main-count diagnostic. Unsupported inference: sensitivity GLM point is the crude marginal RR calculated from main counts.

**Exact remaining human question:** For Severe respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.91, and does its RR mean the crude main-arm ratio or a model-defined ratio?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** report_internal_inconsistency

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Evidence state:** record_input_error

**Determining recheck fact:** The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled.

**Suggested review disposition:** discuss (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C091 — Aspiration sensitivity-forest point versus crude risks

**Cited location found:** Yes. [eFigure 12 Aspiration — PDF p. 42](<../../../../joi190055supp4_prod_16092.pdf#page=42>); [Table 3 component counts — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Table 3 footnote b — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [Individual component sensitivity plan — PDF p. 3](<../../../../joi190055supp3_prod_16092.pdf#page=3>).

**Source printed value/text matched:** Yes. Forest Risk Ratio (99.58% CI): 1.33 [0.41,4.30].

**Comparator printed value/text matched:** Yes. Main high2/989 and low1/987; final SAP expressly specifies a generalized linear model for individual-component sensitivity analysis with 99.58% Bonferroni intervals.

**Consistency rule applicable:** Crude RR identity is applicable to main counts, but the equality check against this separately fitted sensitivity point needs an estimator/population alignment not supplied by the sources.

**Calculation or logical comparison reproduced:** (2/989)/(1/987)=1.995956; absolute distance from1.33=0.665956, larger than .005. Interval is positive, ordered and contains its printed point (0.41≤1.33≤4.30). This diagnostic does not reproduce a fitted GLM.

**Necessary inputs available:** Printed forest point/CI, main component counts/populations, RR labels and GLM sensitivity family are available.

**Exact missing inputs or definitions:** Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output.

**Source-grounded alternative interpretation:** A model-based/standardized ratio under a distinct analysis population or estimator can differ from the raw main-arm ratio. Bonferroni width alone does not explain a point shift, but model definition can.

**Direct observation versus inferred explanation:** Direct: point/CI/counts and explicit sensitivity GLM plan. Derived: crude main-count diagnostic. Unsupported inference: sensitivity GLM point is the crude marginal RR calculated from main counts.

**Exact remaining human question:** For Aspiration, what realized GLM/link/contrast/adjustment/population produced1.33, and does its RR mean the crude main-arm ratio or a model-defined ratio?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** report_internal_inconsistency

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Evidence state:** record_input_error

**Determining recheck fact:** The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled.

**Suggested review disposition:** discuss (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C092 — Bronchospasm sensitivity-forest point versus crude risks

**Cited location found:** Yes. [eFigure 12 Bronchospasm — PDF p. 42](<../../../../joi190055supp4_prod_16092.pdf#page=42>); [Table 3 component counts — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Table 3 footnote b — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [Individual component sensitivity plan — PDF p. 3](<../../../../joi190055supp3_prod_16092.pdf#page=3>).

**Source printed value/text matched:** Yes. Forest Risk Ratio (99.58% CI): 1.09 [0.62,1.91].

**Comparator printed value/text matched:** Yes. Main high12/989 and low10/987; final SAP expressly specifies a generalized linear model for individual-component sensitivity analysis with 99.58% Bonferroni intervals.

**Consistency rule applicable:** Crude RR identity is applicable to main counts, but the equality check against this separately fitted sensitivity point needs an estimator/population alignment not supplied by the sources.

**Calculation or logical comparison reproduced:** (12/989)/(10/987)=1.197573; absolute distance from1.09=0.107573, larger than .005. Interval is positive, ordered and contains its printed point (0.62≤1.09≤1.91). This diagnostic does not reproduce a fitted GLM.

**Necessary inputs available:** Printed forest point/CI, main component counts/populations, RR labels and GLM sensitivity family are available.

**Exact missing inputs or definitions:** Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output.

**Source-grounded alternative interpretation:** A model-based/standardized ratio under a distinct analysis population or estimator can differ from the raw main-arm ratio. Bonferroni width alone does not explain a point shift, but model definition can.

**Direct observation versus inferred explanation:** Direct: point/CI/counts and explicit sensitivity GLM plan. Derived: crude main-count diagnostic. Unsupported inference: sensitivity GLM point is the crude marginal RR calculated from main counts.

**Exact remaining human question:** For Bronchospasm, what realized GLM/link/contrast/adjustment/population produced1.09, and does its RR mean the crude main-arm ratio or a model-defined ratio?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** report_internal_inconsistency

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Evidence state:** record_input_error

**Determining recheck fact:** The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled.

**Suggested review disposition:** discuss (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C093 — ARDS sensitivity-forest point versus crude risks

**Cited location found:** Yes. [eFigure 12 ARDS — PDF p. 42](<../../../../joi190055supp4_prod_16092.pdf#page=42>); [Table 3 component counts — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Table 3 footnote b — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [Individual component sensitivity plan — PDF p. 3](<../../../../joi190055supp3_prod_16092.pdf#page=3>).

**Source printed value/text matched:** Yes. Forest Risk Ratio (99.58% CI): 1.50 [0.65,3.44].

**Comparator printed value/text matched:** Yes. Main high3/989 and low1/987; final SAP expressly specifies a generalized linear model for individual-component sensitivity analysis with 99.58% Bonferroni intervals.

**Consistency rule applicable:** Crude RR identity is applicable to main counts, but the equality check against this separately fitted sensitivity point needs an estimator/population alignment not supplied by the sources.

**Calculation or logical comparison reproduced:** (3/989)/(1/987)=2.993933; absolute distance from1.50=1.493933, larger than .005. Interval is positive, ordered and contains its printed point (0.65≤1.50≤3.44). This diagnostic does not reproduce a fitted GLM.

**Necessary inputs available:** Printed forest point/CI, main component counts/populations, RR labels and GLM sensitivity family are available.

**Exact missing inputs or definitions:** Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output.

**Source-grounded alternative interpretation:** A model-based/standardized ratio under a distinct analysis population or estimator can differ from the raw main-arm ratio. Bonferroni width alone does not explain a point shift, but model definition can.

**Direct observation versus inferred explanation:** Direct: point/CI/counts and explicit sensitivity GLM plan. Derived: crude main-count diagnostic. Unsupported inference: sensitivity GLM point is the crude marginal RR calculated from main counts.

**Exact remaining human question:** For ARDS, what realized GLM/link/contrast/adjustment/population produced1.50, and does its RR mean the crude main-arm ratio or a model-defined ratio?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** report_internal_inconsistency

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Evidence state:** record_input_error

**Determining recheck fact:** The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled.

**Suggested review disposition:** discuss (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C094 — Atelectasis sensitivity-forest point versus crude risks

**Cited location found:** Yes. [eFigure 12 Atelectasis — PDF p. 42](<../../../../joi190055supp4_prod_16092.pdf#page=42>); [Table 3 component counts — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Table 3 footnote b — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [Individual component sensitivity plan — PDF p. 3](<../../../../joi190055supp3_prod_16092.pdf#page=3>).

**Source printed value/text matched:** Yes. Forest Risk Ratio (99.58% CI): 0.88 [0.64,1.23].

**Comparator printed value/text matched:** Yes. Main high44/989 and low55/987; final SAP expressly specifies a generalized linear model for individual-component sensitivity analysis with 99.58% Bonferroni intervals.

**Consistency rule applicable:** Crude RR identity is applicable to main counts, but the equality check against this separately fitted sensitivity point needs an estimator/population alignment not supplied by the sources.

**Calculation or logical comparison reproduced:** (44/989)/(55/987)=0.798382; absolute distance from0.88=0.081618, larger than .005. Interval is positive, ordered and contains its printed point (0.64≤0.88≤1.23). This diagnostic does not reproduce a fitted GLM.

**Necessary inputs available:** Printed forest point/CI, main component counts/populations, RR labels and GLM sensitivity family are available.

**Exact missing inputs or definitions:** Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output.

**Source-grounded alternative interpretation:** A model-based/standardized ratio under a distinct analysis population or estimator can differ from the raw main-arm ratio. Bonferroni width alone does not explain a point shift, but model definition can.

**Direct observation versus inferred explanation:** Direct: point/CI/counts and explicit sensitivity GLM plan. Derived: crude main-count diagnostic. Unsupported inference: sensitivity GLM point is the crude marginal RR calculated from main counts.

**Exact remaining human question:** For Atelectasis, what realized GLM/link/contrast/adjustment/population produced0.88, and does its RR mean the crude main-arm ratio or a model-defined ratio?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** report_internal_inconsistency

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Evidence state:** record_input_error

**Determining recheck fact:** The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled.

**Suggested review disposition:** discuss (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C095 — Cardiopulmonary edema sensitivity-forest point versus crude risks

**Cited location found:** Yes. [eFigure 12 Cardiopulmonary edema — PDF p. 42](<../../../../joi190055supp4_prod_16092.pdf#page=42>); [Table 3 component counts — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Table 3 footnote b — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [Individual component sensitivity plan — PDF p. 3](<../../../../joi190055supp3_prod_16092.pdf#page=3>).

**Source printed value/text matched:** Yes. Forest Risk Ratio (99.58% CI): 1.31 [0.87,1.98].

**Comparator printed value/text matched:** Yes. Main high17/989 and low9/987; final SAP expressly specifies a generalized linear model for individual-component sensitivity analysis with 99.58% Bonferroni intervals.

**Consistency rule applicable:** Crude RR identity is applicable to main counts, but the equality check against this separately fitted sensitivity point needs an estimator/population alignment not supplied by the sources.

**Calculation or logical comparison reproduced:** (17/989)/(9/987)=1.885069; absolute distance from1.31=0.575069, larger than .005. Interval is positive, ordered and contains its printed point (0.87≤1.31≤1.98). This diagnostic does not reproduce a fitted GLM.

**Necessary inputs available:** Printed forest point/CI, main component counts/populations, RR labels and GLM sensitivity family are available.

**Exact missing inputs or definitions:** Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output.

**Source-grounded alternative interpretation:** A model-based/standardized ratio under a distinct analysis population or estimator can differ from the raw main-arm ratio. Bonferroni width alone does not explain a point shift, but model definition can.

**Direct observation versus inferred explanation:** Direct: point/CI/counts and explicit sensitivity GLM plan. Derived: crude main-count diagnostic. Unsupported inference: sensitivity GLM point is the crude marginal RR calculated from main counts.

**Exact remaining human question:** For Cardiopulmonary edema, what realized GLM/link/contrast/adjustment/population produced1.31, and does its RR mean the crude main-arm ratio or a model-defined ratio?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** report_internal_inconsistency

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Evidence state:** record_input_error

**Determining recheck fact:** The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled.

**Suggested review disposition:** discuss (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C096 — Pleural effusion sensitivity-forest point versus crude risks

**Cited location found:** Yes. [eFigure 12 Pleural effusion — PDF p. 42](<../../../../joi190055supp4_prod_16092.pdf#page=42>); [Table 3 component counts — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Table 3 footnote b — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [Individual component sensitivity plan — PDF p. 3](<../../../../joi190055supp3_prod_16092.pdf#page=3>).

**Source printed value/text matched:** Yes. Forest Risk Ratio (99.58% CI): 1.36 [1.05,1.76].

**Comparator printed value/text matched:** Yes. Main high43/989 and low21/987; final SAP expressly specifies a generalized linear model for individual-component sensitivity analysis with 99.58% Bonferroni intervals.

**Consistency rule applicable:** Crude RR identity is applicable to main counts, but the equality check against this separately fitted sensitivity point needs an estimator/population alignment not supplied by the sources.

**Calculation or logical comparison reproduced:** (43/989)/(21/987)=2.043478; absolute distance from1.36=0.683478, larger than .005. Interval is positive, ordered and contains its printed point (1.05≤1.36≤1.76). This diagnostic does not reproduce a fitted GLM.

**Necessary inputs available:** Printed forest point/CI, main component counts/populations, RR labels and GLM sensitivity family are available.

**Exact missing inputs or definitions:** Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output.

**Source-grounded alternative interpretation:** A model-based/standardized ratio under a distinct analysis population or estimator can differ from the raw main-arm ratio. Bonferroni width alone does not explain a point shift, but model definition can.

**Direct observation versus inferred explanation:** Direct: point/CI/counts and explicit sensitivity GLM plan. Derived: crude main-count diagnostic. Unsupported inference: sensitivity GLM point is the crude marginal RR calculated from main counts.

**Exact remaining human question:** For Pleural effusion, what realized GLM/link/contrast/adjustment/population produced1.36, and does its RR mean the crude main-arm ratio or a model-defined ratio?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** report_internal_inconsistency

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Evidence state:** record_input_error

**Determining recheck fact:** The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled.

**Suggested review disposition:** discuss (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C097 — Pneumothorax sensitivity-forest point versus crude risks

**Cited location found:** Yes. [eFigure 12 Pneumothorax — PDF p. 42](<../../../../joi190055supp4_prod_16092.pdf#page=42>); [Table 3 component counts — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Table 3 footnote b — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [Individual component sensitivity plan — PDF p. 3](<../../../../joi190055supp3_prod_16092.pdf#page=3>).

**Source printed value/text matched:** Yes. Forest Risk Ratio (99.58% CI): 0.50 [0.04,5.96].

**Comparator printed value/text matched:** Yes. Main high1/989 and low3/987; final SAP expressly specifies a generalized linear model for individual-component sensitivity analysis with 99.58% Bonferroni intervals.

**Consistency rule applicable:** Crude RR identity is applicable to main counts, but the equality check against this separately fitted sensitivity point needs an estimator/population alignment not supplied by the sources.

**Calculation or logical comparison reproduced:** (1/989)/(3/987)=0.332659; absolute distance from0.50=0.167341, larger than .005. Interval is positive, ordered and contains its printed point (0.04≤0.50≤5.96). This diagnostic does not reproduce a fitted GLM.

**Necessary inputs available:** Printed forest point/CI, main component counts/populations, RR labels and GLM sensitivity family are available.

**Exact missing inputs or definitions:** Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output.

**Source-grounded alternative interpretation:** A model-based/standardized ratio under a distinct analysis population or estimator can differ from the raw main-arm ratio. Bonferroni width alone does not explain a point shift, but model definition can.

**Direct observation versus inferred explanation:** Direct: point/CI/counts and explicit sensitivity GLM plan. Derived: crude main-count diagnostic. Unsupported inference: sensitivity GLM point is the crude marginal RR calculated from main counts.

**Exact remaining human question:** For Pneumothorax, what realized GLM/link/contrast/adjustment/population produced0.50, and does its RR mean the crude main-arm ratio or a model-defined ratio?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** report_internal_inconsistency

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Evidence state:** record_input_error

**Determining recheck fact:** The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled.

**Suggested review disposition:** discuss (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C098 — Pulmonary infiltrates sensitivity-forest point versus crude risks

**Cited location found:** Yes. [eFigure 12 Pulmonary infiltrates — PDF p. 42](<../../../../joi190055supp4_prod_16092.pdf#page=42>); [Table 3 component counts — PDF p. 9](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [Table 3 footnote b — PDF p. 10](<../../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>); [Individual component sensitivity plan — PDF p. 3](<../../../../joi190055supp3_prod_16092.pdf#page=3>).

**Source printed value/text matched:** Yes. Forest Risk Ratio (99.58% CI): 0.87 [0.49,1.55].

**Comparator printed value/text matched:** Yes. Main high14/989 and low18/987; final SAP expressly specifies a generalized linear model for individual-component sensitivity analysis with 99.58% Bonferroni intervals.

**Consistency rule applicable:** Crude RR identity is applicable to main counts, but the equality check against this separately fitted sensitivity point needs an estimator/population alignment not supplied by the sources.

**Calculation or logical comparison reproduced:** (14/989)/(18/987)=0.776205; absolute distance from0.87=0.093795, larger than .005. Interval is positive, ordered and contains its printed point (0.49≤0.87≤1.55). This diagnostic does not reproduce a fitted GLM.

**Necessary inputs available:** Printed forest point/CI, main component counts/populations, RR labels and GLM sensitivity family are available.

**Exact missing inputs or definitions:** Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output.

**Source-grounded alternative interpretation:** A model-based/standardized ratio under a distinct analysis population or estimator can differ from the raw main-arm ratio. Bonferroni width alone does not explain a point shift, but model definition can.

**Direct observation versus inferred explanation:** Direct: point/CI/counts and explicit sensitivity GLM plan. Derived: crude main-count diagnostic. Unsupported inference: sensitivity GLM point is the crude marginal RR calculated from main counts.

**Exact remaining human question:** For Pulmonary infiltrates, what realized GLM/link/contrast/adjustment/population produced0.87, and does its RR mean the crude main-arm ratio or a model-defined ratio?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** S_C

**All relationships:** S_C

**Review domain:** report_internal_inconsistency

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.  No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Evidence state:** record_input_error

**Determining recheck fact:** The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled.

**Suggested review disposition:** discuss (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C099 — Protocol current total748 versus revised2013

**Cited location found:** Yes. [Section 7.2 procedures — PDF p. 12](<../../../../joi190055supp1_prod_16092.pdf#page=12>); [Section 6.4 sample size — PDF p. 11](<../../../../joi190055supp1_prod_16092.pdf#page=11>); [Current recruitment — PDF p. 10](<../../../../joi190055supp1_prod_16092.pdf#page=10>); [Revised sample target — PDF p. 2](<../../../../joi190055supp2_prod_16092.pdf#page=2>).

**Source printed value/text matched:** Yes. Section7.2 current prospective sentence: In total,748 patients will be included.

**Comparator printed value/text matched:** Yes. Section6.4 distinguishes initial748 from revised2013; section6.1 says will randomize2013; amendment records revised2013.

**Consistency rule applicable:** Applicable: current planned total within one protocol version should agree or explicitly identify a historical number.

**Calculation or logical comparison reproduced:** 2013−748=1265. The initial748 is explicitly historical in section6.4, but section7.2 retains a current future-tense total.

**Necessary inputs available:** All totals, version2.6 and historical/current wording are available.

**Exact missing inputs or definitions:** Whether section7.2 was intended as retained historical text despite future tense.

**Source-grounded alternative interpretation:** Section7.2 may be an unupdated procedure paragraph or intentionally preserved history without a local label.

**Direct observation versus inferred explanation:** Direct: all totals/wording. Derived: difference. Inferred: why748 remains.

**Exact remaining human question:** In version2.6, does section7.2 still prescribe748 or retain a historical paragraph; what current total was intended?

**Category:** Numeric or arithmetic inconsistency

**Compared document roles:** PLAN protocol current procedure total versus PLAN protocol revised sample/recruitment target; PLAN amendment corroborates. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** P_P

**All relationships:** P_P

**Review domain:** plan_material

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Historical intent of section7.2 is not stated; no REPORT comparator creates P_R.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Current source confirms future-tense748 alongside explicitly revised2013 in the same PLAN version.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C100 — Tabulated futility inequality versus central plotted region

**Cited location found:** Yes. [Look 1 futility cell — PDF p. 22](<../../../../joi190055supp1_prod_16092.pdf#page=22>); [Boundary figure at 956 — PDF p. 23](<../../../../joi190055supp1_prod_16092.pdf#page=23>); [Boundary-design amendment — PDF p. 3](<../../../../joi190055supp2_prod_16092.pdf#page=3>); [Repeated boundary graphic — PDF p. 31](<../../../../joi190055supp4_prod_16092.pdf#page=31>).

**Source printed value/text matched:** Yes. Table look1, N=956, futility Z<0.225.

**Comparator printed value/text matched:** Yes. Signed figure has central pink Futility region bounded on both sides of zero, with outer negative Efficacy and positive Harm regions.

**Consistency rule applicable:** Applicable only if table and figure intend the same signed statistic/decision mapping. Printed signed inequalities and displayed region orientation may be compared without reading an unprinted exact graph magnitude.

**Calculation or logical comparison reproduced:** Z=−4 satisfies Z<+0.225 but lies outside the pink central region at N956. Thus these sets differ under a common signed-Z interpretation.

**Necessary inputs available:** Exact table cell, signed axis, region labels and enrollment matching are available; amendment links the table/figure design.

**Exact missing inputs or definitions:** Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm).

**Source-grounded alternative interpretation:** Table may use a benefit-oriented statistic while figure uses signed treatment-risk Z. An explicit sign mapping, absolute-value convention or separate harm priority could reconcile intent.

**Direct observation versus inferred explanation:** Direct: positive table inequality, signed axis and colored/labeled region. Conditional inference: identical signed statistic; approximate magnitude alignment is not exact transcription.

**Exact remaining human question:** At look1 N956, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region?

**Category:** Statistical reporting inconsistency

**Compared document roles:** PLAN protocol monitoring table look1 versus PLAN protocol boundary figure at enrollment956; PLAN amendment and REPORT supplement repeated graphic corroborate. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** P_P

**All relationships:** P_P

**Review domain:** plan_material

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C101 — Tabulated futility inequality versus central plotted region

**Cited location found:** Yes. [Look 2 futility cell — PDF p. 22](<../../../../joi190055supp1_prod_16092.pdf#page=22>); [Boundary figure at 1434 — PDF p. 23](<../../../../joi190055supp1_prod_16092.pdf#page=23>); [Boundary-design amendment — PDF p. 3](<../../../../joi190055supp2_prod_16092.pdf#page=3>); [Repeated boundary graphic — PDF p. 31](<../../../../joi190055supp4_prod_16092.pdf#page=31>).

**Source printed value/text matched:** Yes. Table look2, N=1434, futility Z<0.929.

**Comparator printed value/text matched:** Yes. Signed figure has central pink Futility region bounded on both sides of zero, with outer negative Efficacy and positive Harm regions.

**Consistency rule applicable:** Applicable only if table and figure intend the same signed statistic/decision mapping. Printed signed inequalities and displayed region orientation may be compared without reading an unprinted exact graph magnitude.

**Calculation or logical comparison reproduced:** Z=−4 satisfies Z<+0.929 but lies outside the pink central region at N1434. Thus these sets differ under a common signed-Z interpretation.

**Necessary inputs available:** Exact table cell, signed axis, region labels and enrollment matching are available; amendment links the table/figure design.

**Exact missing inputs or definitions:** Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm).

**Source-grounded alternative interpretation:** Table may use a benefit-oriented statistic while figure uses signed treatment-risk Z. An explicit sign mapping, absolute-value convention or separate harm priority could reconcile intent.

**Direct observation versus inferred explanation:** Direct: positive table inequality, signed axis and colored/labeled region. Conditional inference: identical signed statistic; approximate magnitude alignment is not exact transcription.

**Exact remaining human question:** At look2 N1434, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region?

**Category:** Statistical reporting inconsistency

**Compared document roles:** PLAN protocol monitoring table look2 versus PLAN protocol boundary figure at enrollment1434; PLAN amendment and REPORT supplement repeated graphic corroborate. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** P_P

**All relationships:** P_P

**Review domain:** plan_material

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C102 — Tabulated futility inequality versus central plotted region

**Cited location found:** Yes. [Look 3 futility cell — PDF p. 22](<../../../../joi190055supp1_prod_16092.pdf#page=22>); [Boundary figure at 1912 — PDF p. 23](<../../../../joi190055supp1_prod_16092.pdf#page=23>); [Boundary-design amendment — PDF p. 3](<../../../../joi190055supp2_prod_16092.pdf#page=3>); [Repeated boundary graphic — PDF p. 31](<../../../../joi190055supp4_prod_16092.pdf#page=31>).

**Source printed value/text matched:** Yes. Table look3, N=1912, futility Z<2.012.

**Comparator printed value/text matched:** Yes. Signed figure has central pink Futility region bounded on both sides of zero, with outer negative Efficacy and positive Harm regions.

**Consistency rule applicable:** Applicable only if table and figure intend the same signed statistic/decision mapping. Printed signed inequalities and displayed region orientation may be compared without reading an unprinted exact graph magnitude.

**Calculation or logical comparison reproduced:** Z=−4 satisfies Z<+2.012 but lies outside the pink central region at N1912. Thus these sets differ under a common signed-Z interpretation.

**Necessary inputs available:** Exact table cell, signed axis, region labels and enrollment matching are available; amendment links the table/figure design.

**Exact missing inputs or definitions:** Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm).

**Source-grounded alternative interpretation:** Table may use a benefit-oriented statistic while figure uses signed treatment-risk Z. An explicit sign mapping, absolute-value convention or separate harm priority could reconcile intent.

**Direct observation versus inferred explanation:** Direct: positive table inequality, signed axis and colored/labeled region. Conditional inference: identical signed statistic; approximate magnitude alignment is not exact transcription.

**Exact remaining human question:** At look3 N1912, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region?

**Category:** Statistical reporting inconsistency

**Compared document roles:** PLAN protocol monitoring table look3 versus PLAN protocol boundary figure at enrollment1912; PLAN amendment and REPORT supplement repeated graphic corroborate. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** P_P

**All relationships:** P_P

**Review domain:** plan_material

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C103 — Primary-analysis phrase combines odds ratio and relative risks

**Cited location found:** Yes. [Primary efficacy-analysis sentence — PDF p. 23](<../../../../joi190055supp1_prod_16092.pdf#page=23>); [Original assumed probabilities — PDF p. 11](<../../../../joi190055supp1_prod_16092.pdf#page=11>); [Updated primary analysis — PDF p. 2](<../../../../joi190055supp3_prod_16092.pdf#page=2>).

**Source printed value/text matched:** Yes. Protocol: odds ratio relative risks with corresponding95% confidence levels interval, calculated using logistic regression.

**Comparator printed value/text matched:** Yes. Same sentence juxtaposes OR and RR terms; initial assumed risks .30 high/.40 low; later SAP names risk ratio.

**Consistency rule applicable:** Applicable: OR and RR are distinct measures; the original combined phrase does not uniquely label the intended estimate/interval.

**Calculation or logical comparison reproduced:** For supplied assumptions RR=.30/.40=.75; OR=(.30/.70)/(.40/.60)=.642857. This illustrates scale difference, not an observed-result recalculation.

**Necessary inputs available:** Exact phrase, supplied planning probabilities and updated SAP effect label are available.

**Exact missing inputs or definitions:** Intended measure(s), contrast and logistic postprocessing for original sentence.

**Source-grounded alternative interpretation:** Unfinished replacement of odds ratio by relative risks, intended dual reporting, or post-model standardization; logistic regression alone does not uniquely specify final effect scale.

**Direct observation versus inferred explanation:** Direct: adjacent measure words in native source and image. Derived: planning-risk illustration. Inferred: editorial history/actual intended estimator.

**Exact remaining human question:** Which measure(s), contrast and postprocessing did the original primary sentence intend, and which measure labels its interval?

**Category:** Measure, label, or scale inconsistency

**Compared document roles:** PLAN protocol primary-analysis sentence containing both measure terms; PLAN updated SAP is later explanatory context. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** P_P

**All relationships:** P_P

**Review domain:** plan_material

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Later SAP may supersede original wording; it does not remove the original PLAN-internal label question.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Current render confirms adjacent odds ratio relative risks; source-label ambiguity reproduces without relying on an OCR error.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C104 — Tabulated efficacy positive inequality versus negative plotted region

**Cited location found:** Yes. [Look 1 efficacy cell — PDF p. 22](<../../../../joi190055supp1_prod_16092.pdf#page=22>); [Boundary figure at 956 — PDF p. 23](<../../../../joi190055supp1_prod_16092.pdf#page=23>); [Boundary-design amendment — PDF p. 3](<../../../../joi190055supp2_prod_16092.pdf#page=3>); [Repeated boundary graphic — PDF p. 31](<../../../../joi190055supp4_prod_16092.pdf#page=31>).

**Source printed value/text matched:** Yes. Table look1, N=956, efficacy Z≥2.75.

**Comparator printed value/text matched:** Yes. Signed figure labels negative outer tail Efficacy and positive outer tail Harm; the efficacy boundary lies below zero.

**Consistency rule applicable:** Applicable only if table and figure intend the same signed statistic/decision mapping. Printed signed inequalities and displayed region orientation may be compared without reading an unprinted exact graph magnitude.

**Calculation or logical comparison reproduced:** Z≥+2.75 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value.

**Necessary inputs available:** Exact table cell, signed axis, region labels and enrollment matching are available; amendment links the table/figure design.

**Exact missing inputs or definitions:** Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm).

**Source-grounded alternative interpretation:** Table may use a benefit-oriented statistic while figure uses signed treatment-risk Z. An explicit sign mapping, absolute-value convention or separate harm priority could reconcile intent.

**Direct observation versus inferred explanation:** Direct: positive table inequality, signed axis and colored/labeled region. Conditional inference: identical signed statistic; approximate magnitude alignment is not exact transcription.

**Exact remaining human question:** At look1 N956, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail?

**Category:** Statistical reporting inconsistency

**Compared document roles:** PLAN protocol monitoring table look1 versus PLAN protocol boundary figure at enrollment956; PLAN amendment and REPORT supplement repeated graphic corroborate. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** P_P

**All relationships:** P_P

**Review domain:** plan_material

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C105 — Tabulated efficacy positive inequality versus negative plotted region

**Cited location found:** Yes. [Look 2 efficacy cell — PDF p. 22](<../../../../joi190055supp1_prod_16092.pdf#page=22>); [Boundary figure at 1434 — PDF p. 23](<../../../../joi190055supp1_prod_16092.pdf#page=23>); [Boundary-design amendment — PDF p. 3](<../../../../joi190055supp2_prod_16092.pdf#page=3>); [Repeated boundary graphic — PDF p. 31](<../../../../joi190055supp4_prod_16092.pdf#page=31>).

**Source printed value/text matched:** Yes. Table look2, N=1434, efficacy Z≥2.432.

**Comparator printed value/text matched:** Yes. Signed figure labels negative outer tail Efficacy and positive outer tail Harm; the efficacy boundary lies below zero.

**Consistency rule applicable:** Applicable only if table and figure intend the same signed statistic/decision mapping. Printed signed inequalities and displayed region orientation may be compared without reading an unprinted exact graph magnitude.

**Calculation or logical comparison reproduced:** Z≥+2.432 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value.

**Necessary inputs available:** Exact table cell, signed axis, region labels and enrollment matching are available; amendment links the table/figure design.

**Exact missing inputs or definitions:** Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm).

**Source-grounded alternative interpretation:** Table may use a benefit-oriented statistic while figure uses signed treatment-risk Z. An explicit sign mapping, absolute-value convention or separate harm priority could reconcile intent.

**Direct observation versus inferred explanation:** Direct: positive table inequality, signed axis and colored/labeled region. Conditional inference: identical signed statistic; approximate magnitude alignment is not exact transcription.

**Exact remaining human question:** At look2 N1434, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail?

**Category:** Statistical reporting inconsistency

**Compared document roles:** PLAN protocol monitoring table look2 versus PLAN protocol boundary figure at enrollment1434; PLAN amendment and REPORT supplement repeated graphic corroborate. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** P_P

**All relationships:** P_P

**Review domain:** plan_material

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.

## C106 — Tabulated efficacy positive inequality versus negative plotted region

**Cited location found:** Yes. [Look 3 efficacy cell — PDF p. 22](<../../../../joi190055supp1_prod_16092.pdf#page=22>); [Boundary figure at 1912 — PDF p. 23](<../../../../joi190055supp1_prod_16092.pdf#page=23>); [Boundary-design amendment — PDF p. 3](<../../../../joi190055supp2_prod_16092.pdf#page=3>); [Repeated boundary graphic — PDF p. 31](<../../../../joi190055supp4_prod_16092.pdf#page=31>).

**Source printed value/text matched:** Yes. Table look3, N=1912, efficacy Z≥2.012.

**Comparator printed value/text matched:** Yes. Signed figure labels negative outer tail Efficacy and positive outer tail Harm; the efficacy boundary lies below zero.

**Consistency rule applicable:** Applicable only if table and figure intend the same signed statistic/decision mapping. Printed signed inequalities and displayed region orientation may be compared without reading an unprinted exact graph magnitude.

**Calculation or logical comparison reproduced:** Z≥+2.012 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value.

**Necessary inputs available:** Exact table cell, signed axis, region labels and enrollment matching are available; amendment links the table/figure design.

**Exact missing inputs or definitions:** Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm).

**Source-grounded alternative interpretation:** Table may use a benefit-oriented statistic while figure uses signed treatment-risk Z. An explicit sign mapping, absolute-value convention or separate harm priority could reconcile intent.

**Direct observation versus inferred explanation:** Direct: positive table inequality, signed axis and colored/labeled region. Conditional inference: identical signed statistic; approximate magnitude alignment is not exact transcription.

**Exact remaining human question:** At look3 N1912, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail?

**Category:** Statistical reporting inconsistency

**Compared document roles:** PLAN protocol monitoring table look3 versus PLAN protocol boundary figure at enrollment1912; PLAN amendment and REPORT supplement repeated graphic corroborate. Roles confirmed by content: completed-trial results/methods are REPORT; prospective protocol, amendment and statistical plan are PLAN.

**Relationship type:** P_P

**All relationships:** P_P

**Review domain:** plan_material

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R. No document-role or relationship-code change from registration; role descriptions above make the substantive locations explicit.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Evidence state:** recorded_candidate

**Determining recheck fact:** Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition.

**Suggested review disposition:** retain (mechanical pre-fill only).

**Human review status:** Pending Human Adjudication.


