## C028 — Mild respiratory failure: absolute difference versus exact printed risks

**Candidate statement:** For mild respiratory failure, the printed −1.9 percentage-point difference differs slightly from the nearest one-decimal display of the exact High-minus-Low count-defined difference. The observation depends on the computation and display convention: subtracting the displayed percentages or truncating the exact difference reproduces −1.9. Status: Pending Human Adjudication.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>), Primary Outcome narrative, mild respiratory failure counts/percentages and signed difference; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3 Mild respiratory failure row and High PEEP 989/Low PEEP 987 headers; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnote a on reference patients.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Mild respiratory failure; 135(13.7); 154(15.6); −1.9(−5.1 to1.2); RR0.92(0.80 to1.05); .22. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O02-RD; checkers/numeric_consistency.md :: NB-MILD-DIFF. Numeric relationship: N181. Additional matched narrative relationship: N022.

**Reported-versus-comparator:** Reported −1.9 percentage points (95% CI −5.1 to 1.2), repeated in the narrative, versus the derived count-defined High-minus-Low risk difference −1.952685211 percentage points, whose nearest one-decimal display is −2.0. The separate displayed-percentage comparator, 13.7−15.6, equals −1.9.

**Reasoning procedure:** Use the exact printed integers and reference populations to compute 100×(135/989−154/987). Under nearest one-decimal display, the absolute tolerance is 0.05 percentage point. This rule is conditional on a raw count-defined difference and nearest rounding; neither the exact difference estimator nor the display convention is fully specified. The 0.15-percentage-point allowance when comparing already rounded summaries does not change the exact integer calculation.

**Calculation:** 100×(135/989−154/987)=−1.952685211 percentage points; printed-minus-derived=+0.052685211 percentage point. The gap exceeds 0.05 by only 0.002685211. Nearest rounding gives −2.0; truncation toward zero gives −1.9; 13.7−15.6=−1.9.

**Alternative source-grounded interpretations:** Displayed-percentage subtraction and truncation toward zero both reconcile the printed −1.9. A specifically defined fitted or adjusted difference or different analysis denominator could also differ from the crude calculation, but the package does not give a row-specific point formula/display rule. These are alternatives for human reconciliation, not identified production mechanisms or proposed corrections.

**Mechanical evidence recheck:** The direct-source recheck found the narrative and Table 3 cells, matched 135 (13.7%), 154 (15.6%), −1.9 (−5.1 to 1.2), and the reference populations, and reproduced the tiny conditional nearest-rounding gap. The named missing inputs are the raw-versus-model difference formula and rounding/truncation convention. State recorded_candidate records that comparison pending the definition; it does not establish an arithmetic error. The suggested retain disposition is a mechanical pre-fill for human review. Document roles and S_W classification were confirmed.

**Quality-control relevance:** Clarifying the mild respiratory failure difference −1.9 percentage points and its interpretation as an exact count-defined effect supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the mild respiratory failure difference −1.9 percentage points and its interpretation as an exact count-defined effect. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and confirm the matched row, narrative and reference-patient rule.
2. Recompute the exact count-defined difference, displayed-percentage subtraction and truncation alternatives.
3. Determine whether −1.9 was obtained from exact risks, rounded summaries or a fitted estimand, and identify its actual display convention.
4. Decide which calculation and value an extractor should use; record the human decision in the fields below.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C029 — Mild respiratory failure: labeled RR versus printed patient risks

**Candidate statement:** For mild respiratory failure, the printed risk ratio 0.92 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Mild respiratory failure row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description. REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>), Primary Outcome narrative, additionally matched mild respiratory failure counts and reported effect.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Mild respiratory failure; 135(13.7); 154(15.6); −1.9(−5.1 to1.2); RR0.92(0.80 to1.05); .22. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O02-RR; checkers/numeric_consistency.md :: NB-RR-MILD; checkers/statistical_pass_1.md :: RR-O02; checkers/cross_source_consistency.md :: XR02. Numeric relationship: N181. The direct-source recheck additionally confirmed the matched Primary Outcome narrative on PDF p. 8.

**Reported-versus-comparator:** Reported risk ratio 0.92 (95% CI 0.80 to1.05) versus the derived clinical event-risk ratio (135/989)/(154/987)=0.874850630, nearest display 0.87. Printed-minus-derived=0.045149370; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (135/989)/(154/987)=0.874850630; nearest 0.87; printed 0.92; signed gap 0.045149370. Reverse-conditioning diagnostic q=[135/(135+154)]/[(854)/(1687)]=0.922769301; nearest 0.92, truncation 0.92.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 135, Low PEEP 154, reference patients 989/987, risk ratio 0.92 (0.80 to1.05) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the mild respiratory failure risk ratio 0.92, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the mild respiratory failure risk ratio 0.92, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Mild respiratory failure row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (135/989)/(154/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.92. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C030 — Moderate respiratory failure: labeled RR versus printed patient risks

**Candidate statement:** For moderate respiratory failure, the printed risk ratio 0.83 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Moderate respiratory failure row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Moderate respiratory failure; 42(4.2); 58(5.9); −1.6(−3.6 to0.3); RR0.83(0.65 to1.05); .10. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O03-RR; checkers/statistical_pass_1.md :: RR-O03; checkers/cross_source_consistency.md :: XR03. Numeric relationship: N182.

**Reported-versus-comparator:** Reported risk ratio 0.83 (95% CI 0.65 to1.05) versus the derived clinical event-risk ratio (42/989)/(58/987)=0.722673547, nearest display 0.72. Printed-minus-derived=0.107326453; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (42/989)/(58/987)=0.722673547; nearest 0.72; printed 0.83; signed gap 0.107326453. Reverse-conditioning diagnostic q=[42/(42+58)]/[(947)/(1876)]=0.832016895; nearest 0.83, truncation 0.83.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 42, Low PEEP 58, reference patients 989/987, risk ratio 0.83 (0.65 to1.05) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the moderate respiratory failure risk ratio 0.83, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the moderate respiratory failure risk ratio 0.83, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Moderate respiratory failure row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (42/989)/(58/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.83. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C031 — Severe respiratory failure: labeled RR versus printed patient risks

**Candidate statement:** For severe respiratory failure, the printed risk ratio 0.90 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Severe respiratory failure row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Severe respiratory failure; 30(3.0); 36(3.6); −0.6(−2.2 to1.0); RR0.90(0.69 to1.18); .45. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O04-RR; checkers/statistical_pass_1.md :: RR-O04; checkers/cross_source_consistency.md :: XR04. Numeric relationship: N183.

**Reported-versus-comparator:** Reported risk ratio 0.90 (95% CI 0.69 to1.18) versus the derived clinical event-risk ratio (30/989)/(36/987)=0.831648129, nearest display 0.83. Printed-minus-derived=0.068351871; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (30/989)/(36/987)=0.831648129; nearest 0.83; printed 0.90; signed gap 0.068351871. Reverse-conditioning diagnostic q=[30/(30+36)]/[(959)/(1910)]=0.905299080; nearest 0.91, truncation 0.90.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 30, Low PEEP 36, reference patients 989/987, risk ratio 0.90 (0.69 to1.18) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the severe respiratory failure risk ratio 0.90, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the severe respiratory failure risk ratio 0.90, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Severe respiratory failure row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (30/989)/(36/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.90. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C032 — Atelectasis: labeled RR versus printed patient risks

**Candidate statement:** For atelectasis, the printed risk ratio 0.88 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Atelectasis row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Atelectasis; 44(4.4); 55(5.6); −1.1(−3.0 to0.8); RR0.88(0.70 to1.10); .25. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O05-RR; checkers/statistical_pass_1.md :: RR-O05; checkers/cross_source_consistency.md :: XR05. Numeric relationship: N184.

**Reported-versus-comparator:** Reported risk ratio 0.88 (95% CI 0.70 to1.10) versus the derived clinical event-risk ratio (44/989)/(55/987)=0.798382204, nearest display 0.80. Printed-minus-derived=0.081617796; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (44/989)/(55/987)=0.798382204; nearest 0.80; printed 0.88; signed gap 0.081617796. Reverse-conditioning diagnostic q=[44/(44+55)]/[(945)/(1877)]=0.882774838; nearest 0.88, truncation 0.88.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 44, Low PEEP 55, reference patients 989/987, risk ratio 0.88 (0.70 to1.10) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the atelectasis risk ratio 0.88, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the atelectasis risk ratio 0.88, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Atelectasis row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (44/989)/(55/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.88. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C033 — Pleural effusion: labeled RR versus printed patient risks

**Candidate statement:** For pleural effusion, the printed risk ratio 1.35 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Pleural effusion row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description. REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>), Primary Outcome narrative, additionally matched pleural effusion counts and reported effect.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Pleural effusion; 43(4.3); 21(2.1); 2.2(0.7 to3.8); RR1.35(1.14 to1.62); .005. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O06-RR; checkers/numeric_consistency.md :: NB-RR-EFFUSION; checkers/statistical_pass_1.md :: RR-O06; checkers/cross_source_consistency.md :: XR06. Numeric relationship: N185. The direct-source recheck additionally confirmed the matched Primary Outcome narrative on PDF p. 8.

**Reported-versus-comparator:** Reported risk ratio 1.35 (95% CI 1.14 to1.62) versus the derived clinical event-risk ratio (43/989)/(21/987)=2.043478261, nearest display 2.04. Printed-minus-derived=-0.693478261; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (43/989)/(21/987)=2.043478261; nearest 2.04; printed 1.35; signed gap -0.693478261. Reverse-conditioning diagnostic q=[43/(43+21)]/[(946)/(1912)]=1.357954545; nearest 1.36, truncation 1.35.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 43, Low PEEP 21, reference patients 989/987, risk ratio 1.35 (1.14 to1.62) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the pleural effusion risk ratio 1.35, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the pleural effusion risk ratio 1.35, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Pleural effusion row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (43/989)/(21/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.35. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C034 — New pulmonary infiltrates: labeled RR versus printed patient risks

**Candidate statement:** For new pulmonary infiltrates, the printed risk ratio 0.87 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, New pulmonary infiltrates row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: New pulmonary infiltrates; 14(1.4); 18(1.8); −0.4(−1.5 to0.7); RR0.87(0.59 to1.29); .47. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O07-RR; checkers/statistical_pass_1.md :: RR-O07; checkers/cross_source_consistency.md :: XR07. Numeric relationship: N186.

**Reported-versus-comparator:** Reported risk ratio 0.87 (95% CI 0.59 to1.29) versus the derived clinical event-risk ratio (14/989)/(18/987)=0.776204921, nearest display 0.78. Printed-minus-derived=0.093795079; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (14/989)/(18/987)=0.776204921; nearest 0.78; printed 0.87; signed gap 0.093795079. Reverse-conditioning diagnostic q=[14/(14+18)]/[(975)/(1944)]=0.872307692; nearest 0.87, truncation 0.87.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 14, Low PEEP 18, reference patients 989/987, risk ratio 0.87 (0.59 to1.29) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the new pulmonary infiltrates risk ratio 0.87, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the new pulmonary infiltrates risk ratio 0.87, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named New pulmonary infiltrates row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (14/989)/(18/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.87. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C035 — Cardiopulmonary edema: labeled RR versus printed patient risks

**Candidate statement:** For cardiopulmonary edema, the printed risk ratio 1.31 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Cardiopulmonary edema row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Cardiopulmonary edema; 17(1.7); 9(0.9); 0.8(−0.2 to1.8); RR1.31(0.99 to1.74); .12. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O08-RR; checkers/statistical_pass_1.md :: RR-O08; checkers/cross_source_consistency.md :: XR08. Numeric relationship: N187.

**Reported-versus-comparator:** Reported risk ratio 1.31 (95% CI 0.99 to1.74) versus the derived clinical event-risk ratio (17/989)/(9/987)=1.885069093, nearest display 1.89. Printed-minus-derived=-0.575069093; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (17/989)/(9/987)=1.885069093; nearest 1.89; printed 1.31; signed gap -0.575069093. Reverse-conditioning diagnostic q=[17/(17+9)]/[(972)/(1950)]=1.311728395; nearest 1.31, truncation 1.31.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 17, Low PEEP 9, reference patients 989/987, risk ratio 1.31 (0.99 to1.74) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the cardiopulmonary edema risk ratio 1.31, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the cardiopulmonary edema risk ratio 1.31, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Cardiopulmonary edema row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (17/989)/(9/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.31. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C036 — Bronchospasm: labeled RR versus printed patient risks

**Candidate statement:** For bronchospasm, the printed risk ratio 1.09 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article versus REPORT main article

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.

**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Bronchospasm row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Bronchospasm; 12(1.2); 10(1.0); 0.2(−0.7 to1.1); RR1.09(0.74 to1.60); .67. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O09-RR; checkers/statistical_pass_1.md :: RR-O09; checkers/cross_source_consistency.md :: XR09. Numeric relationship: N188.

**Reported-versus-comparator:** Reported risk ratio 1.09 (95% CI 0.74 to1.60) versus the derived clinical event-risk ratio (12/989)/(10/987)=1.197573306, nearest display 1.20. Printed-minus-derived=-0.107573306; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (12/989)/(10/987)=1.197573306; nearest 1.20; printed 1.09; signed gap -0.107573306. Reverse-conditioning diagnostic q=[12/(12+10)]/[(977)/(1954)]=1.090909091; nearest 1.09, truncation 1.09.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 12, Low PEEP 10, reference patients 989/987, risk ratio 1.09 (0.74 to1.60) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the bronchospasm risk ratio 1.09, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the bronchospasm risk ratio 1.09, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Bronchospasm row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (12/989)/(10/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.09. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C037 — Pulmonary infection: labeled RR versus printed patient risks

**Candidate statement:** For pulmonary infection, the printed risk ratio 0.99 differs from nearest rounding of the count-defined High/Low event-risk ratio, but truncation of that clinical ratio itself reproduces 0.99. This remains a conditional display/definition question. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Pulmonary infection event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Pulmonary infection row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Pulmonary infection; 10(1.0); 10(1.0); 0(−0.9 to0.9); RR0.99(0.64 to1.55); >.99. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O10-RR; checkers/statistical_pass_1.md :: RR-O10; checkers/cross_source_consistency.md :: XR10. Numeric relationship: N189.

**Reported-versus-comparator:** Reported risk ratio 0.99 (95% CI 0.64 to1.55) versus the derived clinical event-risk ratio (10/989)/(10/987)=0.997977755, nearest display 1.00. Printed-minus-derived=-0.007977755; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (10/989)/(10/987)=0.997977755; nearest 1.00; printed 0.99; signed gap -0.007977755. Reverse-conditioning diagnostic q=[10/(10+10)]/[(979)/(1956)]=0.998978550; nearest 1.00, truncation 0.99. Truncating the clinical ratio 0.997977755 itself gives 0.99.

**Alternative source-grounded interpretations:** Truncation of the clinical event-risk ratio itself reproduces 0.99, so reversed conditioning is not required to explain this display. The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 10, Low PEEP 10, reference patients 989/987, risk ratio 0.99 (0.64 to1.55) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. It also confirmed that clinical-ratio truncation reconciles the printed point. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the pulmonary infection risk ratio 0.99, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the pulmonary infection risk ratio 0.99, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Pulmonary infection row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (10/989)/(10/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.99. Check specifically whether the clinical ratio was truncated to 0.99. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C038 — Aspiration pneumonitis: labeled RR versus printed patient risks

**Candidate statement:** For aspiration pneumonitis, the printed risk ratio 1.33 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Aspiration pneumonitis event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Aspiration pneumonitis row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Aspiration pneumonitis; 2(0.2); 1(0.1); 0.1(−0.2 to0.4); RR1.33(0.60 to2.97); >.99. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O11-RR; checkers/statistical_pass_1.md :: RR-O11; checkers/cross_source_consistency.md :: XR11. Numeric relationship: N190.

**Reported-versus-comparator:** Reported risk ratio 1.33 (95% CI 0.60 to2.97) versus the derived clinical event-risk ratio (2/989)/(1/987)=1.995955511, nearest display 2.00. Printed-minus-derived=-0.665955511; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (2/989)/(1/987)=1.995955511; nearest 2.00; printed 1.33; signed gap -0.665955511. Reverse-conditioning diagnostic q=[2/(2+1)]/[(987)/(1973)]=1.332657886; nearest 1.33, truncation 1.33.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 2, Low PEEP 1, reference patients 989/987, risk ratio 1.33 (0.60 to2.97) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the aspiration pneumonitis risk ratio 1.33, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the aspiration pneumonitis risk ratio 1.33, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Aspiration pneumonitis row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (2/989)/(1/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.33. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C039 — ARDS: labeled RR versus printed patient risks

**Candidate statement:** For ards, the printed risk ratio 1.50 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Acute respiratory distress syndrome event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, ARDS row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: ARDS; 3(0.3); 1(0.1); 0.2(−0.2 to0.6); RR1.50(0.85 to2.64); .62. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O12-RR; checkers/statistical_pass_1.md :: RR-O12; checkers/cross_source_consistency.md :: XR12. Numeric relationship: N191.

**Reported-versus-comparator:** Reported risk ratio 1.50 (95% CI 0.85 to2.64) versus the derived clinical event-risk ratio (3/989)/(1/987)=2.993933266, nearest display 2.99. Printed-minus-derived=-1.493933266; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (3/989)/(1/987)=2.993933266; nearest 2.99; printed 1.50; signed gap -1.493933266. Reverse-conditioning diagnostic q=[3/(3+1)]/[(986)/(1972)]=1.500000000; nearest 1.50, truncation 1.50.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 3, Low PEEP 1, reference patients 989/987, risk ratio 1.50 (0.85 to2.64) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the ards risk ratio 1.50, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the ards risk ratio 1.50, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named ARDS row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (3/989)/(1/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.50. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C040 — Pneumothorax: labeled RR versus printed patient risks

**Candidate statement:** For pneumothorax, the printed risk ratio 0.50 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Pneumothorax event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Pneumothorax row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Pneumothorax; 1(0.1); 3(0.3); −0.2(−0.6 to0.2); RR0.50(0.09 to2.72); .37. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O13-RR; checkers/statistical_pass_1.md :: RR-O13; checkers/cross_source_consistency.md :: XR13. Numeric relationship: N192.

**Reported-versus-comparator:** Reported risk ratio 0.50 (95% CI 0.09 to2.72) versus the derived clinical event-risk ratio (1/989)/(3/987)=0.332659252, nearest display 0.33. Printed-minus-derived=0.167340748; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (1/989)/(3/987)=0.332659252; nearest 0.33; printed 0.50; signed gap 0.167340748. Reverse-conditioning diagnostic q=[1/(1+3)]/[(988)/(1972)]=0.498987854; nearest 0.50, truncation 0.49.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. Here q=0.498987854 nearest-rounds to 0.50 and truncates to 0.49. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 1, Low PEEP 3, reference patients 989/987, risk ratio 0.50 (0.09 to2.72) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the pneumothorax risk ratio 0.50, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the pneumothorax risk ratio 0.50, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Pneumothorax row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (1/989)/(3/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.50. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C041 — Severe postoperative PPC: labeled RR versus printed patient risks

**Candidate statement:** For severe postoperative ppc, the printed risk ratio 0.91 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Severe postoperative pulmonary complications event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Severe postoperative PPC row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Severe postoperative PPC; 116(11.7); 134(13.6); −1.8(−4.8 to1.1); RR0.91(0.80 to1.05); .22. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O14-RR; checkers/statistical_pass_1.md :: RR-O14; checkers/cross_source_consistency.md :: XR14. Numeric relationship: N193.

**Reported-versus-comparator:** Reported risk ratio 0.91 (95% CI 0.80 to1.05) versus the derived clinical event-risk ratio (116/989)/(134/987)=0.863921042, nearest display 0.86. Printed-minus-derived=0.046078958; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (116/989)/(134/987)=0.863921042; nearest 0.86; printed 0.91; signed gap 0.046078958. Reverse-conditioning diagnostic q=[116/(116+134)]/[(873)/(1726)]=0.917369989; nearest 0.92, truncation 0.91.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 116, Low PEEP 134, reference patients 989/987, risk ratio 0.91 (0.80 to1.05) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the severe postoperative ppc risk ratio 0.91, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the severe postoperative ppc risk ratio 0.91, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Severe postoperative PPC row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (116/989)/(134/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.91. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C042 — Postoperative extrapulmonary composite: labeled RR versus printed patient risks

**Candidate statement:** For postoperative extrapulmonary composite, the printed risk ratio 1.06 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Postoperative extrapulmonary complications event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Postoperative extrapulmonary composite row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Postoperative extrapulmonary composite; 167(16.9); 150(15.2); 1.7(−1.5 to4.9); RR1.06(0.95 to1.19); .31. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O15-RR; checkers/statistical_pass_1.md :: RR-O15; checkers/cross_source_consistency.md :: XR15. Numeric relationship: N194.

**Reported-versus-comparator:** Reported risk ratio 1.06 (95% CI 0.95 to1.19) versus the derived clinical event-risk ratio (167/989)/(150/987)=1.111081901, nearest display 1.11. Printed-minus-derived=-0.051081901; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (167/989)/(150/987)=1.111081901; nearest 1.11; printed 1.06; signed gap -0.051081901. Reverse-conditioning diagnostic q=[167/(167+150)]/[(822)/(1659)]=1.063241152; nearest 1.06, truncation 1.06.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 167, Low PEEP 150, reference patients 989/987, risk ratio 1.06 (0.95 to1.19) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the postoperative extrapulmonary composite risk ratio 1.06, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the postoperative extrapulmonary composite risk ratio 1.06, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Postoperative extrapulmonary composite row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (167/989)/(150/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.06. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C043 — Systemic inflammatory response syndrome: labeled RR versus printed patient risks

**Candidate statement:** For systemic inflammatory response syndrome, the printed risk ratio 1.06 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Systemic inflammatory response syndrome event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Systemic inflammatory response syndrome row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Systemic inflammatory response syndrome; 93(9.4); 83(8.4); 1.0(−1.5 to3.5); RR1.06(0.91 to1.22); .44. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O16-RR; checkers/statistical_pass_1.md :: RR-O16; checkers/cross_source_consistency.md :: XR16. Numeric relationship: N195.

**Reported-versus-comparator:** Reported risk ratio 1.06 (95% CI 0.91 to1.22) versus the derived clinical event-risk ratio (93/989)/(83/987)=1.118216039, nearest display 1.12. Printed-minus-derived=-0.058216039; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (93/989)/(83/987)=1.118216039; nearest 1.12; printed 1.06; signed gap -0.058216039. Reverse-conditioning diagnostic q=[93/(93+83)]/[(896)/(1800)]=1.061536120; nearest 1.06, truncation 1.06.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 93, Low PEEP 83, reference patients 989/987, risk ratio 1.06 (0.91 to1.22) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the systemic inflammatory response syndrome risk ratio 1.06, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the systemic inflammatory response syndrome risk ratio 1.06, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Systemic inflammatory response syndrome row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (93/989)/(83/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.06. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C044 — Sepsis: labeled RR versus printed patient risks

**Candidate statement:** For sepsis, the printed risk ratio 1.09 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Sepsis event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Sepsis row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Sepsis; 18(1.8); 15(1.5); 0.3(−0.8 to1.4); RR1.09(0.79 to1.49); .60. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O17-RR; checkers/statistical_pass_1.md :: RR-O17; checkers/cross_source_consistency.md :: XR17. Numeric relationship: N196.

**Reported-versus-comparator:** Reported risk ratio 1.09 (95% CI 0.79 to1.49) versus the derived clinical event-risk ratio (18/989)/(15/987)=1.197573306, nearest display 1.20. Printed-minus-derived=-0.107573306; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (18/989)/(15/987)=1.197573306; nearest 1.20; printed 1.09; signed gap -0.107573306. Reverse-conditioning diagnostic q=[18/(18+15)]/[(971)/(1943)]=1.091470836; nearest 1.09, truncation 1.09.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 18, Low PEEP 15, reference patients 989/987, risk ratio 1.09 (0.79 to1.49) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the sepsis risk ratio 1.09, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the sepsis risk ratio 1.09, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Sepsis row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (18/989)/(15/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.09. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C045 — Severe sepsis: labeled RR versus printed patient risks

**Candidate statement:** For severe sepsis, the printed risk ratio 0.82 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Severe sepsis event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Severe sepsis row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Severe sepsis; 7(0.7); 10(1.0); −0.3(−1.1 to0.5); RR0.82(0.46 to1.45); .46. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O18-RR; checkers/statistical_pass_1.md :: RR-O18; checkers/cross_source_consistency.md :: XR18. Numeric relationship: N197.

**Reported-versus-comparator:** Reported risk ratio 0.82 (95% CI 0.46 to1.45) versus the derived clinical event-risk ratio (7/989)/(10/987)=0.698584429, nearest display 0.70. Printed-minus-derived=0.121415571; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (7/989)/(10/987)=0.698584429; nearest 0.70; printed 0.82; signed gap 0.121415571. Reverse-conditioning diagnostic q=[7/(7+10)]/[(982)/(1959)]=0.821432850; nearest 0.82, truncation 0.82.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 7, Low PEEP 10, reference patients 989/987, risk ratio 0.82 (0.46 to1.45) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the severe sepsis risk ratio 0.82, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the severe sepsis risk ratio 0.82, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Severe sepsis row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (7/989)/(10/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.82. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C046 — Septic shock: labeled RR versus printed patient risks

**Candidate statement:** For septic shock, the printed risk ratio 0.93 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Septic shock event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Septic shock row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Septic shock; 7(0.7); 8(0.8); −0.1(−0.9 to0.7); RR0.93(0.54 to1.60); .79. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O19-RR; checkers/statistical_pass_1.md :: RR-O19; checkers/cross_source_consistency.md :: XR19. Numeric relationship: N198.

**Reported-versus-comparator:** Reported risk ratio 0.93 (95% CI 0.54 to1.60) versus the derived clinical event-risk ratio (7/989)/(8/987)=0.873230536, nearest display 0.87. Printed-minus-derived=0.056769464; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (7/989)/(8/987)=0.873230536; nearest 0.87; printed 0.93; signed gap 0.056769464. Reverse-conditioning diagnostic q=[7/(7+8)]/[(982)/(1961)]=0.931907671; nearest 0.93, truncation 0.93.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 7, Low PEEP 8, reference patients 989/987, risk ratio 0.93 (0.54 to1.60) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the septic shock risk ratio 0.93, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the septic shock risk ratio 0.93, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Septic shock row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (7/989)/(8/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.93. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C047 — Gastrointestinal failure: labeled RR versus printed patient risks

**Candidate statement:** For gastrointestinal failure, the printed risk ratio 1.07 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Gastrointestinal failure event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Gastrointestinal failure row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Gastrointestinal failure; 65(6.6); 56(5.7); 0.9(−1.2 to3.0); RR1.07(0.90 to1.28); .40. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O20-RR; checkers/statistical_pass_1.md :: RR-O20; checkers/cross_source_consistency.md :: XR20. Numeric relationship: N199.

**Reported-versus-comparator:** Reported risk ratio 1.07 (95% CI 0.90 to1.28) versus the derived clinical event-risk ratio (65/989)/(56/987)=1.158367037, nearest display 1.16. Printed-minus-derived=-0.088367037; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (65/989)/(56/987)=1.158367037; nearest 1.16; printed 1.07; signed gap -0.088367037. Reverse-conditioning diagnostic q=[65/(65+56)]/[(924)/(1855)]=1.078449787; nearest 1.08, truncation 1.07.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 65, Low PEEP 56, reference patients 989/987, risk ratio 1.07 (0.90 to1.28) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the gastrointestinal failure risk ratio 1.07, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the gastrointestinal failure risk ratio 1.07, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Gastrointestinal failure row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (65/989)/(56/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.07. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C048 — Acute kidney failure: labeled RR versus printed patient risks

**Candidate statement:** For acute kidney failure, the printed risk ratio 0.98 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Acute kidney failure event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Acute kidney failure row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Acute kidney failure; 31(3.1); 32(3.2); −0.1(−1.6 to1.4); RR0.98(0.76 to1.26); .89. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O25-RR; checkers/statistical_pass_1.md :: RR-O25; checkers/cross_source_consistency.md :: XR21. Numeric relationship: N204.

**Reported-versus-comparator:** Reported risk ratio 0.98 (95% CI 0.76 to1.26) versus the derived clinical event-risk ratio (31/989)/(32/987)=0.966790950, nearest display 0.97. Printed-minus-derived=0.013209050; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (31/989)/(32/987)=0.966790950; nearest 0.97; printed 0.98; signed gap 0.013209050. Reverse-conditioning diagnostic q=[31/(31+32)]/[(958)/(1913)]=0.982586075; nearest 0.98, truncation 0.98.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 31, Low PEEP 32, reference patients 989/987, risk ratio 0.98 (0.76 to1.26) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the acute kidney failure risk ratio 0.98, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the acute kidney failure risk ratio 0.98, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Acute kidney failure row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (31/989)/(32/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.98. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C049 — Kidney failure,n/N(%): H printed percentage identity

**Candidate statement:** For the nested kidney failure category, the High PEEP cell 7/31 (22.5%) does not match nearest one-decimal rounding of its explicit quotient. Truncation reproduces the printed percentage, so this is a conditional display-rule question. Status: Pending Human Adjudication.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Failure count/denominator versus REPORT main article same-cell percentage; REPORT main article PDF p. 10 footnotes f/g define the row

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3 Acute kidney failure subcategory Failure, explicit High PEEP 7/31 (22.5%) cell compared with its own numerator/denominator; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), footnotes f/g defining No./total No. and kidney stage categories.

**Source evidence:** Direct printed nested row: Failure; High PEEP 7/31 (22.5%); Low PEEP 5/32 (15.6%). No separate risk ratio or absolute difference is printed for this subcategory; the class comparison P .97 is shared by the kidney-stage block. The denominator here is explicitly 31 for High PEEP and 32 for Low PEEP, not the randomized reference population. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O28-PCT-H. Numeric relationship: N207.

**Reported-versus-comparator:** Reported High PEEP 22.5% versus 100×7/31=22.580645161%, nearest one-decimal 22.6%. The signed printed-minus-exact gap is -0.080645161 percentage point.

**Reasoning procedure:** Divide the explicit nested numerator 7 by its explicit denominator 31 and multiply by 100. Nearest one-decimal rounding permits 0.05 percentage point at a tie; the observed non-tie gap exceeds that bound. Applicability is conditional on nearest rounding. No requirement that rounded subcategory percentages sum exactly to 100 is imposed.

**Calculation:** 100×7/31=22.580645161%; nearest 22.6%; truncation 22.5%; printed 22.5%; absolute gap 0.080645161 percentage point, exceeding 0.05 by 0.030645161. The nearest-rounding interval for 22.5% is [22.45%,22.55%), excluding the exact quotient.

**Alternative source-grounded interpretations:** Truncation of the explicit 7/31 quotient gives the printed 22.5% and coherently reconciles the display. A differently defined denominator or a transcribed cell would require supporting information; the supplied row already specifies 31 and gives no replacement denominator. The actual display rule is missing, so no percentage correction is assigned.

**Mechanical evidence recheck:** The direct-source recheck matched the Failure cell, explicit 7/31 fraction, printed 22.5% and location, and reproduced the registered nearest-rounding comparison. The quotient inputs are available; the missing input is the calculation/display convention. State recorded_candidate retains that conditional question, with suggested retain disposition as a mechanical pre-fill for human review. The roles are REPORT/REPORT within Table 3; classification S_W was confirmed.

**Quality-control relevance:** Clarifying the kidney failure category percentage 22.5% or the explicit 7/31 denominator supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the kidney failure category percentage 22.5% or the explicit 7/31 denominator. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and confirm the Failure row and its explicit nested denominator 31.
2. Calculate 100×7/31 and compare nearest rounding with truncation.
3. Establish whether 22.5% was deliberately truncated or arose from a different documented denominator/display procedure.
4. Choose the documented interpretation for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C050 — Kidney loss,n/N(%): H printed percentage identity

**Candidate statement:** For the nested kidney loss category, the High PEEP cell 2/31 (6.4%) does not match nearest one-decimal rounding of its explicit quotient. Truncation reproduces the printed percentage, so this is a conditional display-rule question. Status: Pending Human Adjudication.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Loss count/denominator versus REPORT main article same-cell percentage; REPORT main article PDF p. 10 footnotes f/g define the row

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3 Acute kidney failure subcategory Loss, explicit High PEEP 2/31 (6.4%) cell compared with its own numerator/denominator; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), footnotes f/g defining No./total No. and kidney stage categories.

**Source evidence:** Direct printed nested row: Loss; High PEEP 2/31 (6.4%); Low PEEP 2/32 (6.2%). No separate risk ratio or absolute difference is printed for this subcategory; the class comparison P .97 is shared by the kidney-stage block. The denominator here is explicitly 31 for High PEEP and 32 for Low PEEP, not the randomized reference population. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O29-PCT-H. Numeric relationship: N208.

**Reported-versus-comparator:** Reported High PEEP 6.4% versus 100×2/31=6.451612903%, nearest one-decimal 6.5%. The signed printed-minus-exact gap is -0.051612903 percentage point.

**Reasoning procedure:** Divide the explicit nested numerator 2 by its explicit denominator 31 and multiply by 100. Nearest one-decimal rounding permits 0.05 percentage point at a tie; the observed non-tie gap exceeds that bound. Applicability is conditional on nearest rounding. No requirement that rounded subcategory percentages sum exactly to 100 is imposed.

**Calculation:** 100×2/31=6.451612903%; nearest 6.5%; truncation 6.4%; printed 6.4%; absolute gap 0.051612903 percentage point, exceeding 0.05 by 0.001612903. The nearest-rounding interval for 6.4% is [6.35%,6.45%), excluding the exact quotient by only 0.001612903 percentage point. The Low PEEP 2/32=6.25% permits tie conventions displaying 6.2%; it is not an additional contradiction.

**Alternative source-grounded interpretations:** Truncation of the explicit 2/31 quotient gives the printed 6.4% and coherently reconciles the display. A differently defined denominator or a transcribed cell would require supporting information; the supplied row already specifies 31 and gives no replacement denominator. The actual display rule is missing, so no percentage correction is assigned.

**Mechanical evidence recheck:** The direct-source recheck matched the Loss cell, explicit 2/31 fraction, printed 6.4% and location, and reproduced the registered nearest-rounding comparison. The quotient inputs are available; the missing input is the calculation/display convention. State recorded_candidate retains that conditional question, with suggested retain disposition as a mechanical pre-fill for human review. The roles are REPORT/REPORT within Table 3; classification S_W was confirmed.

**Quality-control relevance:** Clarifying the kidney loss category percentage 6.4% or the explicit 2/31 denominator supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the kidney loss category percentage 6.4% or the explicit 2/31 denominator. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and confirm the Loss row and its explicit nested denominator 31.
2. Calculate 100×2/31 and compare nearest rounding with truncation.
3. Establish whether 6.4% was deliberately truncated or arose from a different documented denominator/display procedure.
4. Choose the documented interpretation for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C051 — Extrapulmonary infection: labeled RR versus printed patient risks

**Candidate statement:** For extrapulmonary infection, the printed risk ratio 1.11 does not equal the count-defined High/Low event-risk ratio under the Table 3 reference-patient rule and nearest two-decimal display. The unresolved question is the intended point estimand, orientation, denominator, estimator and display convention. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Extrapulmonary infection event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Extrapulmonary infection row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Extrapulmonary infection; 29(2.9); 23(2.3); 0.6(−0.8 to2.0); RR1.11(0.87 to1.42); .40. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O30-RR; checkers/statistical_pass_1.md :: RR-O30; checkers/cross_source_consistency.md :: XR22. Numeric relationship: N209.

**Reported-versus-comparator:** Reported risk ratio 1.11 (95% CI 0.87 to1.42) versus the derived clinical event-risk ratio (29/989)/(23/987)=1.258319778, nearest display 1.26. Printed-minus-derived=-0.148319778; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (29/989)/(23/987)=1.258319778; nearest 1.26; printed 1.11; signed gap -0.148319778. Reverse-conditioning diagnostic q=[29/(29+23)]/[(960)/(1924)]=1.117708333; nearest 1.12, truncation 1.11.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 29, Low PEEP 23, reference patients 989/987, risk ratio 1.11 (0.87 to1.42) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the extrapulmonary infection risk ratio 1.11, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the extrapulmonary infection risk ratio 1.11, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Extrapulmonary infection row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (29/989)/(23/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 1.11. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C052 — Hepatic failure: labeled RR versus printed patient risks

**Candidate statement:** For hepatic failure, the printed risk ratio 0.99 differs from nearest rounding of the count-defined High/Low event-risk ratio, but truncation of that clinical ratio itself reproduces 0.99. This remains a conditional display/definition question. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Hepatic failure event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Hepatic failure row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Hepatic failure; 9(0.9); 9(0.9); 0(−0.8 to0.8); RR0.99(0.63 to1.59); >.99. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O31-RR; checkers/statistical_pass_1.md :: RR-O31; checkers/cross_source_consistency.md :: XR23. Numeric relationship: N210.

**Reported-versus-comparator:** Reported risk ratio 0.99 (95% CI 0.63 to1.59) versus the derived clinical event-risk ratio (9/989)/(9/987)=0.997977755, nearest display 1.00. Printed-minus-derived=-0.007977755; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (9/989)/(9/987)=0.997977755; nearest 1.00; printed 0.99; signed gap -0.007977755. Reverse-conditioning diagnostic q=[9/(9+9)]/[(980)/(1958)]=0.998979592; nearest 1.00, truncation 0.99. Truncating the clinical ratio 0.997977755 itself gives 0.99.

**Alternative source-grounded interpretations:** Truncation of the clinical event-risk ratio itself reproduces 0.99, so reversed conditioning is not required to explain this display. The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 9, Low PEEP 9, reference patients 989/987, risk ratio 0.99 (0.63 to1.59) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. It also confirmed that clinical-ratio truncation reconciles the printed point. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the hepatic failure risk ratio 0.99, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the hepatic failure risk ratio 0.99, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Hepatic failure row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (9/989)/(9/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.99. Check specifically whether the clinical ratio was truncated to 0.99. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C053 — Coma: labeled RR versus printed patient risks

**Candidate statement:** For coma, the printed risk ratio 0.99 differs from nearest rounding of the count-defined High/Low event-risk ratio, but truncation of that clinical ratio itself reproduces 0.99. This remains a conditional display/definition question. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Coma event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Coma row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Coma; 2(0.2); 2(0.2); 0(−0.4 to0.4); RR0.99(0.37 to2.66); >.99. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O32-RR; checkers/statistical_pass_1.md :: RR-O32; checkers/cross_source_consistency.md :: XR24. Numeric relationship: N211.

**Reported-versus-comparator:** Reported risk ratio 0.99 (95% CI 0.37 to2.66) versus the derived clinical event-risk ratio (2/989)/(2/987)=0.997977755, nearest display 1.00. Printed-minus-derived=-0.007977755; its magnitude exceeds the 0.005 two-decimal nearest-rounding bound.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** (2/989)/(2/987)=0.997977755; nearest 1.00; printed 0.99; signed gap -0.007977755. Reverse-conditioning diagnostic q=[2/(2+2)]/[(987)/(1972)]=0.998986829; nearest 1.00, truncation 0.99. Truncating the clinical ratio 0.997977755 itself gives 0.99.

**Alternative source-grounded interpretations:** Truncation of the clinical event-risk ratio itself reproduces 0.99, so reversed conditioning is not required to explain this display. The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 2, Low PEEP 2, reference patients 989/987, risk ratio 0.99 (0.37 to2.66) and the method/footnote locations. It reproduced the registered conditional nearest-rounding point-identity comparison. It also confirmed that clinical-ratio truncation reconciles the printed point. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the coma risk ratio 0.99, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the coma risk ratio 0.99, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Coma row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (2/989)/(2/987), applying the stated 0.005 nearest-rounding tolerance; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, fitted adjustment and display convention produced 0.99. Check specifically whether the clinical ratio was truncated to 0.99. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C054 — Disseminated intravascular coagulation: labeled RR versus printed patient risks

**Candidate statement:** For disseminated intravascular coagulation, Table 3 prints a finite risk ratio 2.00 although the printed Low PEEP event risk is zero. The crude High/Low event-risk quotient has no finite value; interpreting the reported estimate requires its point formula, outcome/reference orientation and zero-cell or fitted-estimator rule. Status: Pending Human Adjudication.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 3 Disseminated intravascular coagulation event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context

**Review domain:** report_internal_inconsistency

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.

**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.

**Exact source locations:** REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), Table 3, Disseminated intravascular coagulation row: High PEEP and Low PEEP event cells, reference-population headers and the compared effect cell; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>), Table 3 footnotes a/b/c defining reference patients, RR/CI approximation and hypothesis testing; REPORT [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>), completed-analysis Statistical Analysis description.

**Source evidence:** Table 3 row tuple, in order outcome; High PEEP events (%); Low PEEP events (%); absolute difference (95% CI); risk ratio (95% CI); P value: Disseminated intravascular coagulation; 1(0.1); 0; 0.1(−0.1 to0.3); RR2.00(1.91 to2.09); >.99. Reference patients: High PEEP 989 and Low PEEP 987 unless otherwise indicated (footnote a). The RR/CI method is described as the Wald likelihood ratio approximation; the χ² hypothesis-test procedure is separately described. These printed values and labels are observations; calculations below are derived comparisons. Current checker provenance: checkers/parts/numeric_outcomes.md :: NUM-O33-RR; checkers/statistical_pass_1.md :: RR-O33; checkers/cross_source_consistency.md :: XR25. Numeric relationship: N212.

**Reported-versus-comparator:** Reported risk ratio 2.00 (95% CI 1.91 to2.09) versus (1/989)/(0/987), which has no finite crude event-risk value because its denominator risk is zero. A finite fitted or corrected estimate requires an additional stated procedure.

**Reasoning procedure:** Compare event risk conditional on treatment: RR=(High PEEP events/High PEEP reference patients)/(Low PEEP events/Low PEEP reference patients). Table 3 footnote a supplies 989/987 unless otherwise indicated. The integer inputs are exact; nearest two-decimal display allows 0.005 on the ratio scale. The comparison is conditional on this raw clinical estimand and nearest rounding; a fitted or standardized quantity must have its own stated definition. Direct observations are the event cells, reference headers, RR label, point and interval. The point-identity arithmetic and reverse-conditioning diagnostic are derived, not reported model fits. The RR/CI approximation and χ² P procedure are separately named, so no identical-test CI/P contradiction is assumed.

**Calculation:** High event risk=1/989; Low event risk=0/987=0; their quotient is undefined as a finite number (unbounded in an extended ratio interpretation). No rounding tolerance can turn this crude quotient into 2.00. Diagnostic q=[1/(1+0)]/[(989−1)/(1976−1−0)]=1.998987854, nearest 2.00, truncation 1.99.

**Alternative source-grounded interpretations:** The diagnostic q compares High PEEP membership conditional on event versus no event, a different contrast from event risk conditional on treatment. Its numerical display can resemble the reported point, but does not establish author coding, estimator choice or production mechanism. Here q=1.998987854 nearest-rounds to 2.00 and truncates to 1.99. A defined fitted/standardized estimand, different event/reference coding or an explicitly supported row-specific analysis denominator could differ from the crude ratio; the generic Wald wording alone does not define those choices. A continuity or fitted zero-cell procedure could provide a finite estimate but its exact rule and variance method are not supplied. The exact point formula, orientation, adjustment mapping and row-specific display rule remain missing. No uniform display convention is established across rows.

**Mechanical evidence recheck:** The direct-source recheck found this Table 3 row, matched High PEEP 1, Low PEEP 0, reference patients 989/987, risk ratio 2.00 (1.91 to2.09) and the method/footnote locations. It reproduced the registered nonfinite crude quotient versus finite reported-point comparison. Available inputs are the printed counts, reference populations, point, interval and generic method wording; the exact point estimator, orientation, analysis denominator/adjustment mapping and display convention remain named missing definitions, together with the zero-cell and variance procedures. Evidence state recorded_candidate preserves the observation pending those definitions; mechanical suggestion retain is a pre-fill for human review. REPORT/REPORT roles and S_W were confirmed; no production cause or final validity decision was assigned.

**Quality-control relevance:** Clarifying the disseminated intravascular coagulation risk ratio 2.00, its interval and its treatment-versus-event interpretation supports reproducible quantitative reporting and avoids ambiguity in extraction. Small preventable display or definition defects can matter for downstream evidence extraction if confirmed; their presence or importance remains for human adjudication.

**Potential downstream evidence impact:** A systematic-review or meta-analysis extractor could copy the disseminated intravascular coagulation risk ratio 2.00, its interval and its treatment-versus-event interpretation. If human review confirms a reporting defect, that copied quantity or label could require reconciliation. The supplied record establishes neither actual propagation nor a change in the paper's conclusion or serious harm.

**Human verification steps:**

1. Open [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>), [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>) and [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); confirm the named Disseminated intravascular coagulation row, reference-patient rule and RR/CI versus χ² procedures.
2. Recalculate (1/989)/(0/987) and identify the zero-denominator issue; compare the diagnostic q only as a different conditioning.
3. Ask which exact event/reference orientation, population denominator, point formula, zero-cell rule, variance method, fitted adjustment and display convention produced 2.00. Resolve those definitions before interpreting either derived comparator as a correction.
4. Decide the documented estimand and value suitable for extraction and complete the human adjudication fields.

**Human adjudication fields:**

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
