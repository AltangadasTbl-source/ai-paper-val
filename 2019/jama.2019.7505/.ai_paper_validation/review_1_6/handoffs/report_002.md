# Current source-confirmed report evidence shard

## C028 — Mild respiratory failure: absolute difference versus exact printed risks

**Candidate statement:** Mild respiratory failure: absolute difference versus exact printed risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Numeric or arithmetic inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O02-RD; checkers/numeric_consistency.md :: NB-MILD-DIFF

- **Numeric relationships:** N181.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O02 H/L counts, explicit denominators or H989/L987 headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row Absolute Difference (95% CI) cell.
- **Printed inputs:** H 135(13.7); L 154(15.6); difference −1.9(−5.1 to1.2). Complete source-row components: Mild respiratory failure; 135(13.7); 154(15.6); −1.9(−5.1 to1.2); RR0.92(0.80 to1.05); .22.
- **Reproducible rule and calculation:** 100*(135/989−154/987)=-1.952685 pp; printed -1.9 pp; discrepancy=0.052685 pp; nearest one-decimal value=-2.0 pp. Displayed percentage subtraction=-1.900000 pp.
- **Tolerance:** 0.05 percentage point for an exact count-defined risk difference. The looser0.15 bound applies only when subtracting two already rounded percentages and does not alter the exact integer-count calculation.
- **Direct observation versus inference:** Direct: the two event cells and signed difference are in the same row. Derived: the printed count/denominator risks give a different nearest one-decimal effect. Comparator is H−L, consistent with the surrounding signed differences.
- **Source-grounded alternatives:** Truncation toward zero can reproduce several small boundary discrepancies. Model-based/adjusted absolute differences or a different denominator could also explain them; a row-specific computation/display rule is not supplied. These possibilities are the human question, not assumed corrections.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Mild respiratory failure, was the absolute difference -1.9 calculated from the printed exact risks and then truncated, or from a different estimand/denominator? What computation and display rule should be used when extracting this result?
Additional matched report locations and inputs from NB-MILD-DIFF:
- Relationship:N022. Compared locations and roles: REPORT [main PDF p.8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), Primary Outcome narrative mild respiratory failure135(13.7%) vs154(15.6%), difference−1.9%; REPORT [main PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table3 same counts,headers989/987,and difference−1.9%.
- Printed inputs:135/989,154/987,−1.9 percentage points.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Primary Outcome narrative mild respiratory failure(p. 8); Table 3 Mild row, H989/L987 headers and Absolute Difference column(p. 9); reference-patients footnote a(p. 10). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>)
- Printed inputs: H135(13.7%), L154(15.6%); reference populations989/987; difference−1.9%(95%CI−5.1 to1.2), RR0.92, P.22; same effect in narrative.
- Registered comparator/rule: Reported−1.9 percentage points versus exact count/reference-patient-defined H-minus-L risk difference. Raw risk-difference identity with nearest one-decimal display(±0.05 percentage point), conditional on raw count-defined rather than model effect and nearest rounding.
- Reproduced calculation: 100 ×(135/989−154/987)=-1.952685211 percentage points; nearest−2.0; printed−1.9; gap0.052685211 exceeds0.05 by0.002685211. Printed13.7−15.6=−1.9 agrees. Truncation toward zero of the exact risk difference yields−1.9.
- Determining fact/state: Exact source matches all registered inputs and the tiny nearest-rounding gap; the printed-percentage comparator reconciles but is a different rule. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Counts, explicitly footnoted reference populations and difference are available. Missing: whether point difference is raw/adjusted and the display/truncation rule. Was mild respiratory failure difference−1.9 calculated from135/989 and154/987 then truncated, from rounded13.7%/15.6%, or from another estimand; what calculation/display rule applies?
- Alternative and direct-versus-inferred boundary: Subtracting displayed percentages or truncating exact raw risks reproduces−1.9; a model-based effect could also differ. No row-specific display/computation rule is stated. Direct: counts, labels, population footnote and matching narrative/table effect. Derived: exact arithmetic and tolerance. Inferred: actual rounding/estimator mechanism; none is assigned.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C029 — Mild respiratory failure: labeled RR versus printed patient risks

**Candidate statement:** Mild respiratory failure: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O02-RR; checkers/numeric_consistency.md :: NB-RR-MILD; checkers/statistical_pass_1.md :: RR-O02; checkers/cross_source_consistency.md :: XR02

- **Numeric relationships:** N181.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O02 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 135/989; L 154/987; printed RR0.92(0.80 to1.05). Complete source-row components: Mild respiratory failure; 135(13.7); 154(15.6); −1.9(−5.1 to1.2); RR0.92(0.80 to1.05); .22.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (135/989)/(154/987) = 0.874851; printed point = 0.92. Nearest two-decimal identity display would be 0.87; discrepancy=0.045149.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Mild respiratory failure, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.92, and is this value intended as the H/L event risk ratio from 135/989 and 154/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.
Additional matched report locations and inputs from NB-RR-MILD:
- Printed inputs:H135/989,L154/987;RR0.92.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 3 Mild respiratory failure row, No.of Events(%), H989/L987 headers and Risk Ratio column (p. 9); footnotes a/b (p. 10); completed-analysis RR statement (p. 4); Primary Outcome narrative(p. 8). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>)
- Printed inputs: H events135; L events154; reference populations H989/L987; printed RR0.92 (95%CI0.80 to1.05). Footnote a: number of reference patients unless otherwise indicated. Footnote b: data are risk ratios unless otherwise indicated; RRs/CIs calculated using the Wald likelihood ratio approximation test.
- Registered comparator/rule: Printed outcome risk-ratio label/point0.92 versus same-row H/L event-risk ratio(135/989)/(154/987). For the stated event, high-versus-low patient risk ratio divides high event risk by low event risk. Identity follows the event/reference labels and Table 3 reference-patient footnote. A different adjusted/standardized estimand or reversed conditioning requires its definition; no interval/P diagnostic is used to replace the point estimate.
- Reproduced calculation: (135/989)/(154/987)=0.874850630, nearest two-decimal0.87; printed0.92; signed gap0.045149370 exceeds0.005. Reverse-conditioning diagnostic: [135/(135+154)]/[(854)/(1687)]=0.922769301; truncating THAT quantity to two decimals gives0.92, exactly the printed point. This is risk of high-group membership conditional on event versus no event, a different contrast from event risk conditional on treatment.
- Determining fact/state: The direct source reproduces the labeled point and exact reference counts; the event-risk identity discrepancy remains. An alternative reverse-conditioning diagnostic reproduces the display but does not reconcile its stated event-risk interpretation. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; report_internal_inconsistency.
- Missing definition and human question: Counts, reference populations, label, CI, and generic named approximation available. Missing: exact point-estimate formula, event/reference coding, whether an adjusted/standardized estimand is intended, and display rule. No row-specific covariate adjustment is identified for this Table 3 point. For Mild respiratory failure, what exact formula, outcome/reference orientation and display rule produced RR0.92? Is it intended as H/L event risk, a reversed-conditioning contrast, or a specifically defined adjusted/model quantity?
- Alternative and direct-versus-inferred boundary: The reverse-conditioning diagnostic computed solely from the printed 2×2 counts plus truncation reproduces this point. It is a source-grounded numerical explanation, not evidence that the authors used that coding. A differently defined adjusted/standardized RR could also differ from the crude event ratio, but its target/formula must be supplied. The Wald-approximation wording alone does not define a different point contrast. Direct: count/reference cells, risk-ratio heading, point/interval and generic calculation wording. Derived: event-risk identity and reverse-conditioning diagnostic. Inferred: swapped coding, truncation, or adjustment; no production cause is asserted.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C030 — Moderate respiratory failure: labeled RR versus printed patient risks

**Candidate statement:** Moderate respiratory failure: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O03-RR; checkers/statistical_pass_1.md :: RR-O03; checkers/cross_source_consistency.md :: XR03

- **Numeric relationships:** N182.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O03 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 42/989; L 58/987; printed RR0.83(0.65 to1.05). Complete source-row components: Moderate respiratory failure; 42(4.2); 58(5.9); −1.6(−3.6 to0.3); RR0.83(0.65 to1.05); .10.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (42/989)/(58/987) = 0.722674; printed point = 0.83. Nearest two-decimal identity display would be 0.72; discrepancy=0.107326.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Moderate respiratory failure, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.83, and is this value intended as the H/L event risk ratio from 42/989 and 58/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 3 Moderate respiratory failure row, No.of Events(%), H989/L987 headers and Risk Ratio column (p. 9); footnotes a/b (p. 10); completed-analysis RR statement (p. 4). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>)
- Printed inputs: H events42; L events58; reference populations H989/L987; printed RR0.83 (95%CI0.65 to1.05). Footnote a: number of reference patients unless otherwise indicated. Footnote b: data are risk ratios unless otherwise indicated; RRs/CIs calculated using the Wald likelihood ratio approximation test.
- Registered comparator/rule: Printed outcome risk-ratio label/point0.83 versus same-row H/L event-risk ratio(42/989)/(58/987). For the stated event, high-versus-low patient risk ratio divides high event risk by low event risk. Identity follows the event/reference labels and Table 3 reference-patient footnote. A different adjusted/standardized estimand or reversed conditioning requires its definition; no interval/P diagnostic is used to replace the point estimate.
- Reproduced calculation: (42/989)/(58/987)=0.722673547, nearest two-decimal0.72; printed0.83; signed gap0.107326453 exceeds0.005. Reverse-conditioning diagnostic: [42/(42+58)]/[(947)/(1876)]=0.832016895; truncating THAT quantity to two decimals gives0.83, exactly the printed point. This is risk of high-group membership conditional on event versus no event, a different contrast from event risk conditional on treatment.
- Determining fact/state: The direct source reproduces the labeled point and exact reference counts; the event-risk identity discrepancy remains. An alternative reverse-conditioning diagnostic reproduces the display but does not reconcile its stated event-risk interpretation. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; report_internal_inconsistency.
- Missing definition and human question: Counts, reference populations, label, CI, and generic named approximation available. Missing: exact point-estimate formula, event/reference coding, whether an adjusted/standardized estimand is intended, and display rule. No row-specific covariate adjustment is identified for this Table 3 point. For Moderate respiratory failure, what exact formula, outcome/reference orientation and display rule produced RR0.83? Is it intended as H/L event risk, a reversed-conditioning contrast, or a specifically defined adjusted/model quantity?
- Alternative and direct-versus-inferred boundary: The reverse-conditioning diagnostic computed solely from the printed 2×2 counts plus truncation reproduces this point. It is a source-grounded numerical explanation, not evidence that the authors used that coding. A differently defined adjusted/standardized RR could also differ from the crude event ratio, but its target/formula must be supplied. The Wald-approximation wording alone does not define a different point contrast. Direct: count/reference cells, risk-ratio heading, point/interval and generic calculation wording. Derived: event-risk identity and reverse-conditioning diagnostic. Inferred: swapped coding, truncation, or adjustment; no production cause is asserted.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C031 — Severe respiratory failure: labeled RR versus printed patient risks

**Candidate statement:** Severe respiratory failure: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O04-RR; checkers/statistical_pass_1.md :: RR-O04; checkers/cross_source_consistency.md :: XR04

- **Numeric relationships:** N183.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O04 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 30/989; L 36/987; printed RR0.90(0.69 to1.18). Complete source-row components: Severe respiratory failure; 30(3.0); 36(3.6); −0.6(−2.2 to1.0); RR0.90(0.69 to1.18); .45.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (30/989)/(36/987) = 0.831648; printed point = 0.90. Nearest two-decimal identity display would be 0.83; discrepancy=0.068352.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Severe respiratory failure, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.90, and is this value intended as the H/L event risk ratio from 30/989 and 36/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 3 Severe respiratory failure row, No.of Events(%), H989/L987 headers and Risk Ratio column (p. 9); footnotes a/b (p. 10); completed-analysis RR statement (p. 4). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>)
- Printed inputs: H events30; L events36; reference populations H989/L987; printed RR0.90 (95%CI0.69 to1.18). Footnote a: number of reference patients unless otherwise indicated. Footnote b: data are risk ratios unless otherwise indicated; RRs/CIs calculated using the Wald likelihood ratio approximation test.
- Registered comparator/rule: Printed outcome risk-ratio label/point0.90 versus same-row H/L event-risk ratio(30/989)/(36/987). For the stated event, high-versus-low patient risk ratio divides high event risk by low event risk. Identity follows the event/reference labels and Table 3 reference-patient footnote. A different adjusted/standardized estimand or reversed conditioning requires its definition; no interval/P diagnostic is used to replace the point estimate.
- Reproduced calculation: (30/989)/(36/987)=0.831648129, nearest two-decimal0.83; printed0.90; signed gap0.068351871 exceeds0.005. Reverse-conditioning diagnostic: [30/(30+36)]/[(959)/(1910)]=0.905299080; truncating THAT quantity to two decimals gives0.90, exactly the printed point. This is risk of high-group membership conditional on event versus no event, a different contrast from event risk conditional on treatment.
- Determining fact/state: The direct source reproduces the labeled point and exact reference counts; the event-risk identity discrepancy remains. An alternative reverse-conditioning diagnostic reproduces the display but does not reconcile its stated event-risk interpretation. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; report_internal_inconsistency.
- Missing definition and human question: Counts, reference populations, label, CI, and generic named approximation available. Missing: exact point-estimate formula, event/reference coding, whether an adjusted/standardized estimand is intended, and display rule. No row-specific covariate adjustment is identified for this Table 3 point. For Severe respiratory failure, what exact formula, outcome/reference orientation and display rule produced RR0.90? Is it intended as H/L event risk, a reversed-conditioning contrast, or a specifically defined adjusted/model quantity?
- Alternative and direct-versus-inferred boundary: The reverse-conditioning diagnostic computed solely from the printed 2×2 counts plus truncation reproduces this point. It is a source-grounded numerical explanation, not evidence that the authors used that coding. A differently defined adjusted/standardized RR could also differ from the crude event ratio, but its target/formula must be supplied. The Wald-approximation wording alone does not define a different point contrast. Direct: count/reference cells, risk-ratio heading, point/interval and generic calculation wording. Derived: event-risk identity and reverse-conditioning diagnostic. Inferred: swapped coding, truncation, or adjustment; no production cause is asserted.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C032 — Atelectasis: labeled RR versus printed patient risks

**Candidate statement:** Atelectasis: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O05-RR; checkers/statistical_pass_1.md :: RR-O05; checkers/cross_source_consistency.md :: XR05

- **Numeric relationships:** N184.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O05 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 44/989; L 55/987; printed RR0.88(0.70 to1.10). Complete source-row components: Atelectasis; 44(4.4); 55(5.6); −1.1(−3.0 to0.8); RR0.88(0.70 to1.10); .25.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (44/989)/(55/987) = 0.798382; printed point = 0.88. Nearest two-decimal identity display would be 0.80; discrepancy=0.081618.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Atelectasis, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.88, and is this value intended as the H/L event risk ratio from 44/989 and 55/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 3 Atelectasis row, No.of Events(%), H989/L987 headers and Risk Ratio column (p. 9); footnotes a/b (p. 10); completed-analysis RR statement (p. 4). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>)
- Printed inputs: H events44; L events55; reference populations H989/L987; printed RR0.88 (95%CI0.70 to1.10). Footnote a: number of reference patients unless otherwise indicated. Footnote b: data are risk ratios unless otherwise indicated; RRs/CIs calculated using the Wald likelihood ratio approximation test.
- Registered comparator/rule: Printed outcome risk-ratio label/point0.88 versus same-row H/L event-risk ratio(44/989)/(55/987). For the stated event, high-versus-low patient risk ratio divides high event risk by low event risk. Identity follows the event/reference labels and Table 3 reference-patient footnote. A different adjusted/standardized estimand or reversed conditioning requires its definition; no interval/P diagnostic is used to replace the point estimate.
- Reproduced calculation: (44/989)/(55/987)=0.798382204, nearest two-decimal0.80; printed0.88; signed gap0.081617796 exceeds0.005. Reverse-conditioning diagnostic: [44/(44+55)]/[(945)/(1877)]=0.882774838; truncating THAT quantity to two decimals gives0.88, exactly the printed point. This is risk of high-group membership conditional on event versus no event, a different contrast from event risk conditional on treatment.
- Determining fact/state: The direct source reproduces the labeled point and exact reference counts; the event-risk identity discrepancy remains. An alternative reverse-conditioning diagnostic reproduces the display but does not reconcile its stated event-risk interpretation. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; report_internal_inconsistency.
- Missing definition and human question: Counts, reference populations, label, CI, and generic named approximation available. Missing: exact point-estimate formula, event/reference coding, whether an adjusted/standardized estimand is intended, and display rule. No row-specific covariate adjustment is identified for this Table 3 point. For Atelectasis, what exact formula, outcome/reference orientation and display rule produced RR0.88? Is it intended as H/L event risk, a reversed-conditioning contrast, or a specifically defined adjusted/model quantity?
- Alternative and direct-versus-inferred boundary: The reverse-conditioning diagnostic computed solely from the printed 2×2 counts plus truncation reproduces this point. It is a source-grounded numerical explanation, not evidence that the authors used that coding. A differently defined adjusted/standardized RR could also differ from the crude event ratio, but its target/formula must be supplied. The Wald-approximation wording alone does not define a different point contrast. Direct: count/reference cells, risk-ratio heading, point/interval and generic calculation wording. Derived: event-risk identity and reverse-conditioning diagnostic. Inferred: swapped coding, truncation, or adjustment; no production cause is asserted.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C033 — Pleural effusion: labeled RR versus printed patient risks

**Candidate statement:** Pleural effusion: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O06-RR; checkers/numeric_consistency.md :: NB-RR-EFFUSION; checkers/statistical_pass_1.md :: RR-O06; checkers/cross_source_consistency.md :: XR06

- **Numeric relationships:** N185.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O06 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 43/989; L 21/987; printed RR1.35(1.14 to1.62). Complete source-row components: Pleural effusion; 43(4.3); 21(2.1); 2.2(0.7 to3.8); RR1.35(1.14 to1.62); .005.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (43/989)/(21/987) = 2.043478; printed point = 1.35. Nearest two-decimal identity display would be 2.04; discrepancy=-0.693478.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Pleural effusion, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.35, and is this value intended as the H/L event risk ratio from 43/989 and 21/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.
Additional matched report locations and inputs from NB-RR-EFFUSION:
- Printed inputs:H43/989,L21/987;RR1.35.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 3 Pleural effusion row, No.of Events(%), H989/L987 headers and Risk Ratio column (p. 9); footnotes a/b (p. 10); completed-analysis RR statement (p. 4); Primary Outcome narrative(p. 8). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>)
- Printed inputs: H events43; L events21; reference populations H989/L987; printed RR1.35 (95%CI1.14 to1.62). Footnote a: number of reference patients unless otherwise indicated. Footnote b: data are risk ratios unless otherwise indicated; RRs/CIs calculated using the Wald likelihood ratio approximation test.
- Registered comparator/rule: Printed outcome risk-ratio label/point1.35 versus same-row H/L event-risk ratio(43/989)/(21/987). For the stated event, high-versus-low patient risk ratio divides high event risk by low event risk. Identity follows the event/reference labels and Table 3 reference-patient footnote. A different adjusted/standardized estimand or reversed conditioning requires its definition; no interval/P diagnostic is used to replace the point estimate.
- Reproduced calculation: (43/989)/(21/987)=2.043478261, nearest two-decimal2.04; printed1.35; signed gap-0.693478261 exceeds0.005. Reverse-conditioning diagnostic: [43/(43+21)]/[(946)/(1912)]=1.357954545; truncating THAT quantity to two decimals gives1.35, exactly the printed point. This is risk of high-group membership conditional on event versus no event, a different contrast from event risk conditional on treatment.
- Determining fact/state: The direct source reproduces the labeled point and exact reference counts; the event-risk identity discrepancy remains. An alternative reverse-conditioning diagnostic reproduces the display but does not reconcile its stated event-risk interpretation. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; report_internal_inconsistency.
- Missing definition and human question: Counts, reference populations, label, CI, and generic named approximation available. Missing: exact point-estimate formula, event/reference coding, whether an adjusted/standardized estimand is intended, and display rule. No row-specific covariate adjustment is identified for this Table 3 point. For Pleural effusion, what exact formula, outcome/reference orientation and display rule produced RR1.35? Is it intended as H/L event risk, a reversed-conditioning contrast, or a specifically defined adjusted/model quantity?
- Alternative and direct-versus-inferred boundary: The reverse-conditioning diagnostic computed solely from the printed 2×2 counts plus truncation reproduces this point. It is a source-grounded numerical explanation, not evidence that the authors used that coding. A differently defined adjusted/standardized RR could also differ from the crude event ratio, but its target/formula must be supplied. The Wald-approximation wording alone does not define a different point contrast. Direct: count/reference cells, risk-ratio heading, point/interval and generic calculation wording. Derived: event-risk identity and reverse-conditioning diagnostic. Inferred: swapped coding, truncation, or adjustment; no production cause is asserted.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C034 — New pulmonary infiltrates: labeled RR versus printed patient risks

**Candidate statement:** New pulmonary infiltrates: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O07-RR; checkers/statistical_pass_1.md :: RR-O07; checkers/cross_source_consistency.md :: XR07

- **Numeric relationships:** N186.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O07 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 14/989; L 18/987; printed RR0.87(0.59 to1.29). Complete source-row components: New pulmonary infiltrates; 14(1.4); 18(1.8); −0.4(−1.5 to0.7); RR0.87(0.59 to1.29); .47.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (14/989)/(18/987) = 0.776205; printed point = 0.87. Nearest two-decimal identity display would be 0.78; discrepancy=0.093795.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For New pulmonary infiltrates, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.87, and is this value intended as the H/L event risk ratio from 14/989 and 18/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 3 New pulmonary infiltrates row, No.of Events(%), H989/L987 headers and Risk Ratio column (p. 9); footnotes a/b (p. 10); completed-analysis RR statement (p. 4). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>)
- Printed inputs: H events14; L events18; reference populations H989/L987; printed RR0.87 (95%CI0.59 to1.29). Footnote a: number of reference patients unless otherwise indicated. Footnote b: data are risk ratios unless otherwise indicated; RRs/CIs calculated using the Wald likelihood ratio approximation test.
- Registered comparator/rule: Printed outcome risk-ratio label/point0.87 versus same-row H/L event-risk ratio(14/989)/(18/987). For the stated event, high-versus-low patient risk ratio divides high event risk by low event risk. Identity follows the event/reference labels and Table 3 reference-patient footnote. A different adjusted/standardized estimand or reversed conditioning requires its definition; no interval/P diagnostic is used to replace the point estimate.
- Reproduced calculation: (14/989)/(18/987)=0.776204921, nearest two-decimal0.78; printed0.87; signed gap0.093795079 exceeds0.005. Reverse-conditioning diagnostic: [14/(14+18)]/[(975)/(1944)]=0.872307692; truncating THAT quantity to two decimals gives0.87, exactly the printed point. This is risk of high-group membership conditional on event versus no event, a different contrast from event risk conditional on treatment.
- Determining fact/state: The direct source reproduces the labeled point and exact reference counts; the event-risk identity discrepancy remains. An alternative reverse-conditioning diagnostic reproduces the display but does not reconcile its stated event-risk interpretation. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; report_internal_inconsistency.
- Missing definition and human question: Counts, reference populations, label, CI, and generic named approximation available. Missing: exact point-estimate formula, event/reference coding, whether an adjusted/standardized estimand is intended, and display rule. No row-specific covariate adjustment is identified for this Table 3 point. For New pulmonary infiltrates, what exact formula, outcome/reference orientation and display rule produced RR0.87? Is it intended as H/L event risk, a reversed-conditioning contrast, or a specifically defined adjusted/model quantity?
- Alternative and direct-versus-inferred boundary: The reverse-conditioning diagnostic computed solely from the printed 2×2 counts plus truncation reproduces this point. It is a source-grounded numerical explanation, not evidence that the authors used that coding. A differently defined adjusted/standardized RR could also differ from the crude event ratio, but its target/formula must be supplied. The Wald-approximation wording alone does not define a different point contrast. Direct: count/reference cells, risk-ratio heading, point/interval and generic calculation wording. Derived: event-risk identity and reverse-conditioning diagnostic. Inferred: swapped coding, truncation, or adjustment; no production cause is asserted.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C035 — Cardiopulmonary edema: labeled RR versus printed patient risks

**Candidate statement:** Cardiopulmonary edema: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O08-RR; checkers/statistical_pass_1.md :: RR-O08; checkers/cross_source_consistency.md :: XR08

- **Numeric relationships:** N187.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O08 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 17/989; L 9/987; printed RR1.31(0.99 to1.74). Complete source-row components: Cardiopulmonary edema; 17(1.7); 9(0.9); 0.8(−0.2 to1.8); RR1.31(0.99 to1.74); .12.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (17/989)/(9/987) = 1.885069; printed point = 1.31. Nearest two-decimal identity display would be 1.89; discrepancy=-0.575069.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Cardiopulmonary edema, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.31, and is this value intended as the H/L event risk ratio from 17/989 and 9/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 3 Cardiopulmonary edema row, No.of Events(%), H989/L987 headers and Risk Ratio column (p. 9); footnotes a/b (p. 10); completed-analysis RR statement (p. 4). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>)
- Printed inputs: H events17; L events9; reference populations H989/L987; printed RR1.31 (95%CI0.99 to1.74). Footnote a: number of reference patients unless otherwise indicated. Footnote b: data are risk ratios unless otherwise indicated; RRs/CIs calculated using the Wald likelihood ratio approximation test.
- Registered comparator/rule: Printed outcome risk-ratio label/point1.31 versus same-row H/L event-risk ratio(17/989)/(9/987). For the stated event, high-versus-low patient risk ratio divides high event risk by low event risk. Identity follows the event/reference labels and Table 3 reference-patient footnote. A different adjusted/standardized estimand or reversed conditioning requires its definition; no interval/P diagnostic is used to replace the point estimate.
- Reproduced calculation: (17/989)/(9/987)=1.885069093, nearest two-decimal1.89; printed1.31; signed gap-0.575069093 exceeds0.005. Reverse-conditioning diagnostic: [17/(17+9)]/[(972)/(1950)]=1.311728395; truncating THAT quantity to two decimals gives1.31, exactly the printed point. This is risk of high-group membership conditional on event versus no event, a different contrast from event risk conditional on treatment.
- Determining fact/state: The direct source reproduces the labeled point and exact reference counts; the event-risk identity discrepancy remains. An alternative reverse-conditioning diagnostic reproduces the display but does not reconcile its stated event-risk interpretation. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; report_internal_inconsistency.
- Missing definition and human question: Counts, reference populations, label, CI, and generic named approximation available. Missing: exact point-estimate formula, event/reference coding, whether an adjusted/standardized estimand is intended, and display rule. No row-specific covariate adjustment is identified for this Table 3 point. For Cardiopulmonary edema, what exact formula, outcome/reference orientation and display rule produced RR1.31? Is it intended as H/L event risk, a reversed-conditioning contrast, or a specifically defined adjusted/model quantity?
- Alternative and direct-versus-inferred boundary: The reverse-conditioning diagnostic computed solely from the printed 2×2 counts plus truncation reproduces this point. It is a source-grounded numerical explanation, not evidence that the authors used that coding. A differently defined adjusted/standardized RR could also differ from the crude event ratio, but its target/formula must be supplied. The Wald-approximation wording alone does not define a different point contrast. Direct: count/reference cells, risk-ratio heading, point/interval and generic calculation wording. Derived: event-risk identity and reverse-conditioning diagnostic. Inferred: swapped coding, truncation, or adjustment; no production cause is asserted.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C036 — Bronchospasm: labeled RR versus printed patient risks

**Candidate statement:** Bronchospasm: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O09-RR; checkers/statistical_pass_1.md :: RR-O09; checkers/cross_source_consistency.md :: XR09

- **Numeric relationships:** N188.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O09 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 12/989; L 10/987; printed RR1.09(0.74 to1.60). Complete source-row components: Bronchospasm; 12(1.2); 10(1.0); 0.2(−0.7 to1.1); RR1.09(0.74 to1.60); .67.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (12/989)/(10/987) = 1.197573; printed point = 1.09. Nearest two-decimal identity display would be 1.20; discrepancy=-0.107573.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Bronchospasm, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.09, and is this value intended as the H/L event risk ratio from 12/989 and 10/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 3 Bronchospasm row, No.of Events(%), H989/L987 headers and Risk Ratio column (p. 9); footnotes a/b (p. 10); completed-analysis RR statement (p. 4). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>)
- Printed inputs: H events12; L events10; reference populations H989/L987; printed RR1.09 (95%CI0.74 to1.60). Footnote a: number of reference patients unless otherwise indicated. Footnote b: data are risk ratios unless otherwise indicated; RRs/CIs calculated using the Wald likelihood ratio approximation test.
- Registered comparator/rule: Printed outcome risk-ratio label/point1.09 versus same-row H/L event-risk ratio(12/989)/(10/987). For the stated event, high-versus-low patient risk ratio divides high event risk by low event risk. Identity follows the event/reference labels and Table 3 reference-patient footnote. A different adjusted/standardized estimand or reversed conditioning requires its definition; no interval/P diagnostic is used to replace the point estimate.
- Reproduced calculation: (12/989)/(10/987)=1.197573306, nearest two-decimal1.20; printed1.09; signed gap-0.107573306 exceeds0.005. Reverse-conditioning diagnostic: [12/(12+10)]/[(977)/(1954)]=1.090909091; truncating THAT quantity to two decimals gives1.09, exactly the printed point. This is risk of high-group membership conditional on event versus no event, a different contrast from event risk conditional on treatment.
- Determining fact/state: The direct source reproduces the labeled point and exact reference counts; the event-risk identity discrepancy remains. An alternative reverse-conditioning diagnostic reproduces the display but does not reconcile its stated event-risk interpretation. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; report_internal_inconsistency.
- Missing definition and human question: Counts, reference populations, label, CI, and generic named approximation available. Missing: exact point-estimate formula, event/reference coding, whether an adjusted/standardized estimand is intended, and display rule. No row-specific covariate adjustment is identified for this Table 3 point. For Bronchospasm, what exact formula, outcome/reference orientation and display rule produced RR1.09? Is it intended as H/L event risk, a reversed-conditioning contrast, or a specifically defined adjusted/model quantity?
- Alternative and direct-versus-inferred boundary: The reverse-conditioning diagnostic computed solely from the printed 2×2 counts plus truncation reproduces this point. It is a source-grounded numerical explanation, not evidence that the authors used that coding. A differently defined adjusted/standardized RR could also differ from the crude event ratio, but its target/formula must be supplied. The Wald-approximation wording alone does not define a different point contrast. Direct: count/reference cells, risk-ratio heading, point/interval and generic calculation wording. Derived: event-risk identity and reverse-conditioning diagnostic. Inferred: swapped coding, truncation, or adjustment; no production cause is asserted.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C037 — Pulmonary infection: labeled RR versus printed patient risks

**Candidate statement:** Pulmonary infection: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Pulmonary infection event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O10-RR; checkers/statistical_pass_1.md :: RR-O10; checkers/cross_source_consistency.md :: XR10

- **Numeric relationships:** N189.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O10 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 10/989; L 10/987; printed RR0.99(0.64 to1.55). Complete source-row components: Pulmonary infection; 10(1.0); 10(1.0); 0(−0.9 to0.9); RR0.99(0.64 to1.55); >.99.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (10/989)/(10/987) = 0.997978; printed point = 0.99. Nearest two-decimal identity display would be 1.00; discrepancy=-0.007978.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Pulmonary infection, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.99, and is this value intended as the H/L event risk ratio from 10/989 and 10/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 10/989; Low PEEP 10/987; Risk Ratio 0.99 (0.64–1.55); P >.99.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (10/989)/(10/987) = 0.997978; nearest two-decimal display 1.00; printed RR 0.99 differs by -0.007978.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.997978, outside the nearest-rounding interval for printed 0.99. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Pulmonary infection event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Pulmonary infection, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.99 (0.64–1.55)? Is it the High/Low PEEP event-risk contrast from 10/989 and 10/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[10/(10+10)]/[(989−10)/(989+987−10−10)]=0.998979; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C038 — Aspiration pneumonitis: labeled RR versus printed patient risks

**Candidate statement:** Aspiration pneumonitis: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Aspiration pneumonitis event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O11-RR; checkers/statistical_pass_1.md :: RR-O11; checkers/cross_source_consistency.md :: XR11

- **Numeric relationships:** N190.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O11 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 2/989; L 1/987; printed RR1.33(0.60 to2.97). Complete source-row components: Aspiration pneumonitis; 2(0.2); 1(0.1); 0.1(−0.2 to0.4); RR1.33(0.60 to2.97); >.99.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (2/989)/(1/987) = 1.995956; printed point = 1.33. Nearest two-decimal identity display would be 2.00; discrepancy=-0.665956.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Aspiration pneumonitis, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.33, and is this value intended as the H/L event risk ratio from 2/989 and 1/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 2/989; Low PEEP 1/987; Risk Ratio 1.33 (0.60–2.97); P >.99.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (2/989)/(1/987) = 1.995956; nearest two-decimal display 2.00; printed RR 1.33 differs by -0.665956.
- Determining fact/state: The directly confirmed event counts and denominators yield 1.995956, outside the nearest-rounding interval for printed 1.33. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Aspiration pneumonitis event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Aspiration pneumonitis, what exact event/reference orientation, population denominator, estimator and display rule produced RR 1.33 (0.60–2.97)? Is it the High/Low PEEP event-risk contrast from 2/989 and 1/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[2/(2+1)]/[(989−2)/(989+987−2−1)]=1.332658; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C039 — ARDS: labeled RR versus printed patient risks

**Candidate statement:** ARDS: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Acute respiratory distress syndrome event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O12-RR; checkers/statistical_pass_1.md :: RR-O12; checkers/cross_source_consistency.md :: XR12

- **Numeric relationships:** N191.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O12 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 3/989; L 1/987; printed RR1.50(0.85 to2.64). Complete source-row components: ARDS; 3(0.3); 1(0.1); 0.2(−0.2 to0.6); RR1.50(0.85 to2.64); .62.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (3/989)/(1/987) = 2.993933; printed point = 1.50. Nearest two-decimal identity display would be 2.99; discrepancy=-1.493933.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For ARDS, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.50, and is this value intended as the H/L event risk ratio from 3/989 and 1/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 3/989; Low PEEP 1/987; Risk Ratio 1.50 (0.85–2.64); P .62.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (3/989)/(1/987) = 2.993933; nearest two-decimal display 2.99; printed RR 1.50 differs by -1.493933.
- Determining fact/state: The directly confirmed event counts and denominators yield 2.993933, outside the nearest-rounding interval for printed 1.50. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Acute respiratory distress syndrome event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Acute respiratory distress syndrome, what exact event/reference orientation, population denominator, estimator and display rule produced RR 1.50 (0.85–2.64)? Is it the High/Low PEEP event-risk contrast from 3/989 and 1/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[3/(3+1)]/[(989−3)/(989+987−3−1)]=1.500000; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C040 — Pneumothorax: labeled RR versus printed patient risks

**Candidate statement:** Pneumothorax: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Pneumothorax event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O13-RR; checkers/statistical_pass_1.md :: RR-O13; checkers/cross_source_consistency.md :: XR13

- **Numeric relationships:** N192.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O13 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 1/989; L 3/987; printed RR0.50(0.09 to2.72). Complete source-row components: Pneumothorax; 1(0.1); 3(0.3); −0.2(−0.6 to0.2); RR0.50(0.09 to2.72); .37.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (1/989)/(3/987) = 0.332659; printed point = 0.50. Nearest two-decimal identity display would be 0.33; discrepancy=0.167341.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Pneumothorax, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.50, and is this value intended as the H/L event risk ratio from 1/989 and 3/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 1/989; Low PEEP 3/987; Risk Ratio 0.50 (0.09–2.72); P .37.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (1/989)/(3/987) = 0.332659; nearest two-decimal display 0.33; printed RR 0.50 differs by 0.167341.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.332659, outside the nearest-rounding interval for printed 0.50. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Pneumothorax event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Pneumothorax, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.50 (0.09–2.72)? Is it the High/Low PEEP event-risk contrast from 1/989 and 3/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[1/(1+3)]/[(989−1)/(989+987−1−3)]=0.498988; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C041 — Severe postoperative PPC: labeled RR versus printed patient risks

**Candidate statement:** Severe postoperative PPC: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Severe postoperative pulmonary complications event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O14-RR; checkers/statistical_pass_1.md :: RR-O14; checkers/cross_source_consistency.md :: XR14

- **Numeric relationships:** N193.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O14 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 116/989; L 134/987; printed RR0.91(0.80 to1.05). Complete source-row components: Severe postoperative PPC; 116(11.7); 134(13.6); −1.8(−4.8 to1.1); RR0.91(0.80 to1.05); .22.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (116/989)/(134/987) = 0.863921; printed point = 0.91. Nearest two-decimal identity display would be 0.86; discrepancy=0.046079.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Severe postoperative PPC, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.91, and is this value intended as the H/L event risk ratio from 116/989 and 134/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 116/989; Low PEEP 134/987; Risk Ratio 0.91 (0.80–1.05); P .22.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (116/989)/(134/987) = 0.863921; nearest two-decimal display 0.86; printed RR 0.91 differs by 0.046079.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.863921, outside the nearest-rounding interval for printed 0.91. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Severe postoperative pulmonary complications event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Severe postoperative pulmonary complications, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.91 (0.80–1.05)? Is it the High/Low PEEP event-risk contrast from 116/989 and 134/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[116/(116+134)]/[(989−116)/(989+987−116−134)]=0.917370; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C042 — Postoperative extrapulmonary composite: labeled RR versus printed patient risks

**Candidate statement:** Postoperative extrapulmonary composite: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Postoperative extrapulmonary complications event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O15-RR; checkers/statistical_pass_1.md :: RR-O15; checkers/cross_source_consistency.md :: XR15

- **Numeric relationships:** N194.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O15 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 167/989; L 150/987; printed RR1.06(0.95 to1.19). Complete source-row components: Postoperative extrapulmonary composite; 167(16.9); 150(15.2); 1.7(−1.5 to4.9); RR1.06(0.95 to1.19); .31.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (167/989)/(150/987) = 1.111082; printed point = 1.06. Nearest two-decimal identity display would be 1.11; discrepancy=-0.051082.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Postoperative extrapulmonary composite, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.06, and is this value intended as the H/L event risk ratio from 167/989 and 150/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 167/989; Low PEEP 150/987; Risk Ratio 1.06 (0.95–1.19); P .31.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (167/989)/(150/987) = 1.111082; nearest two-decimal display 1.11; printed RR 1.06 differs by -0.051082.
- Determining fact/state: The directly confirmed event counts and denominators yield 1.111082, outside the nearest-rounding interval for printed 1.06. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Postoperative extrapulmonary complications event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Postoperative extrapulmonary complications, what exact event/reference orientation, population denominator, estimator and display rule produced RR 1.06 (0.95–1.19)? Is it the High/Low PEEP event-risk contrast from 167/989 and 150/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[167/(167+150)]/[(989−167)/(989+987−167−150)]=1.063241; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C043 — Systemic inflammatory response syndrome: labeled RR versus printed patient risks

**Candidate statement:** Systemic inflammatory response syndrome: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Systemic inflammatory response syndrome event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O16-RR; checkers/statistical_pass_1.md :: RR-O16; checkers/cross_source_consistency.md :: XR16

- **Numeric relationships:** N195.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O16 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 93/989; L 83/987; printed RR1.06(0.91 to1.22). Complete source-row components: Systemic inflammatory response syndrome; 93(9.4); 83(8.4); 1.0(−1.5 to3.5); RR1.06(0.91 to1.22); .44.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (93/989)/(83/987) = 1.118216; printed point = 1.06. Nearest two-decimal identity display would be 1.12; discrepancy=-0.058216.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Systemic inflammatory response syndrome, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.06, and is this value intended as the H/L event risk ratio from 93/989 and 83/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 93/989; Low PEEP 83/987; Risk Ratio 1.06 (0.91–1.22); P .44.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (93/989)/(83/987) = 1.118216; nearest two-decimal display 1.12; printed RR 1.06 differs by -0.058216.
- Determining fact/state: The directly confirmed event counts and denominators yield 1.118216, outside the nearest-rounding interval for printed 1.06. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Systemic inflammatory response syndrome event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Systemic inflammatory response syndrome, what exact event/reference orientation, population denominator, estimator and display rule produced RR 1.06 (0.91–1.22)? Is it the High/Low PEEP event-risk contrast from 93/989 and 83/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[93/(93+83)]/[(989−93)/(989+987−93−83)]=1.061536; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C044 — Sepsis: labeled RR versus printed patient risks

**Candidate statement:** Sepsis: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Sepsis event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O17-RR; checkers/statistical_pass_1.md :: RR-O17; checkers/cross_source_consistency.md :: XR17

- **Numeric relationships:** N196.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O17 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 18/989; L 15/987; printed RR1.09(0.79 to1.49). Complete source-row components: Sepsis; 18(1.8); 15(1.5); 0.3(−0.8 to1.4); RR1.09(0.79 to1.49); .60.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (18/989)/(15/987) = 1.197573; printed point = 1.09. Nearest two-decimal identity display would be 1.20; discrepancy=-0.107573.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Sepsis, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.09, and is this value intended as the H/L event risk ratio from 18/989 and 15/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 18/989; Low PEEP 15/987; Risk Ratio 1.09 (0.79–1.49); P .60.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (18/989)/(15/987) = 1.197573; nearest two-decimal display 1.20; printed RR 1.09 differs by -0.107573.
- Determining fact/state: The directly confirmed event counts and denominators yield 1.197573, outside the nearest-rounding interval for printed 1.09. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Sepsis event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Sepsis, what exact event/reference orientation, population denominator, estimator and display rule produced RR 1.09 (0.79–1.49)? Is it the High/Low PEEP event-risk contrast from 18/989 and 15/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[18/(18+15)]/[(989−18)/(989+987−18−15)]=1.091471; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C045 — Severe sepsis: labeled RR versus printed patient risks

**Candidate statement:** Severe sepsis: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Severe sepsis event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O18-RR; checkers/statistical_pass_1.md :: RR-O18; checkers/cross_source_consistency.md :: XR18

- **Numeric relationships:** N197.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O18 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 7/989; L 10/987; printed RR0.82(0.46 to1.45). Complete source-row components: Severe sepsis; 7(0.7); 10(1.0); −0.3(−1.1 to0.5); RR0.82(0.46 to1.45); .46.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (7/989)/(10/987) = 0.698584; printed point = 0.82. Nearest two-decimal identity display would be 0.70; discrepancy=0.121416.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Severe sepsis, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.82, and is this value intended as the H/L event risk ratio from 7/989 and 10/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 7/989; Low PEEP 10/987; Risk Ratio 0.82 (0.46–1.45); P .46.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (7/989)/(10/987) = 0.698584; nearest two-decimal display 0.70; printed RR 0.82 differs by 0.121416.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.698584, outside the nearest-rounding interval for printed 0.82. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Severe sepsis event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Severe sepsis, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.82 (0.46–1.45)? Is it the High/Low PEEP event-risk contrast from 7/989 and 10/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[7/(7+10)]/[(989−7)/(989+987−7−10)]=0.821433; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C046 — Septic shock: labeled RR versus printed patient risks

**Candidate statement:** Septic shock: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Septic shock event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O19-RR; checkers/statistical_pass_1.md :: RR-O19; checkers/cross_source_consistency.md :: XR19

- **Numeric relationships:** N198.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O19 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 7/989; L 8/987; printed RR0.93(0.54 to1.60). Complete source-row components: Septic shock; 7(0.7); 8(0.8); −0.1(−0.9 to0.7); RR0.93(0.54 to1.60); .79.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (7/989)/(8/987) = 0.873231; printed point = 0.93. Nearest two-decimal identity display would be 0.87; discrepancy=0.056769.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Septic shock, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.93, and is this value intended as the H/L event risk ratio from 7/989 and 8/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 7/989; Low PEEP 8/987; Risk Ratio 0.93 (0.54–1.60); P .79.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (7/989)/(8/987) = 0.873231; nearest two-decimal display 0.87; printed RR 0.93 differs by 0.056769.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.873231, outside the nearest-rounding interval for printed 0.93. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Septic shock event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Septic shock, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.93 (0.54–1.60)? Is it the High/Low PEEP event-risk contrast from 7/989 and 8/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[7/(7+8)]/[(989−7)/(989+987−7−8)]=0.931908; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C047 — Gastrointestinal failure: labeled RR versus printed patient risks

**Candidate statement:** Gastrointestinal failure: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Gastrointestinal failure event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O20-RR; checkers/statistical_pass_1.md :: RR-O20; checkers/cross_source_consistency.md :: XR20

- **Numeric relationships:** N199.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O20 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 65/989; L 56/987; printed RR1.07(0.90 to1.28). Complete source-row components: Gastrointestinal failure; 65(6.6); 56(5.7); 0.9(−1.2 to3.0); RR1.07(0.90 to1.28); .40.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (65/989)/(56/987) = 1.158367; printed point = 1.07. Nearest two-decimal identity display would be 1.16; discrepancy=-0.088367.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Gastrointestinal failure, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.07, and is this value intended as the H/L event risk ratio from 65/989 and 56/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 65/989; Low PEEP 56/987; Risk Ratio 1.07 (0.90–1.28); P .40.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (65/989)/(56/987) = 1.158367; nearest two-decimal display 1.16; printed RR 1.07 differs by -0.088367.
- Determining fact/state: The directly confirmed event counts and denominators yield 1.158367, outside the nearest-rounding interval for printed 1.07. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Gastrointestinal failure event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Gastrointestinal failure, what exact event/reference orientation, population denominator, estimator and display rule produced RR 1.07 (0.90–1.28)? Is it the High/Low PEEP event-risk contrast from 65/989 and 56/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[65/(65+56)]/[(989−65)/(989+987−65−56)]=1.078450; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C048 — Acute kidney failure: labeled RR versus printed patient risks

**Candidate statement:** Acute kidney failure: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Acute kidney failure event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O25-RR; checkers/statistical_pass_1.md :: RR-O25; checkers/cross_source_consistency.md :: XR21

- **Numeric relationships:** N204.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O25 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 31/989; L 32/987; printed RR0.98(0.76 to1.26). Complete source-row components: Acute kidney failure; 31(3.1); 32(3.2); −0.1(−1.6 to1.4); RR0.98(0.76 to1.26); .89.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (31/989)/(32/987) = 0.966791; printed point = 0.98. Nearest two-decimal identity display would be 0.97; discrepancy=0.013209.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Acute kidney failure, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.98, and is this value intended as the H/L event risk ratio from 31/989 and 32/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 31/989; Low PEEP 32/987; Risk Ratio 0.98 (0.76–1.26); P .89.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (31/989)/(32/987) = 0.966791; nearest two-decimal display 0.97; printed RR 0.98 differs by 0.013209.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.966791, outside the nearest-rounding interval for printed 0.98. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Acute kidney failure event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Acute kidney failure, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.98 (0.76–1.26)? Is it the High/Low PEEP event-risk contrast from 31/989 and 32/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[31/(31+32)]/[(989−31)/(989+987−31−32)]=0.982586; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C049 — Kidney failure,n/N(%): H printed percentage identity

**Candidate statement:** Kidney failure,n/N(%): H printed percentage identity; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Failure count/denominator versus REPORT main article same-cell percentage; REPORT main article PDF p. 10 footnotes f/g define the row
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O28-PCT-H

- **Numeric relationships:** N207.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O28 H count/denominator cell; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same cell printed percentage and No./total No. (%) or No. (%) row label.
- **Printed inputs:** H 7/31 (22.5%). Complete source-row components: Kidney failure,n/N(%); 7/31(22.5); 5/32(15.6); not printed; not printed; same.97.
- **Reproducible rule and calculation:** 100*7/31=22.580645%; printed 22.5%; discrepancy=-0.080645 pp; nearest one-decimal value=22.6%.
- **Tolerance:** 0.05 percentage point inclusive at ties; printed integer numerator/denominator exact. This mismatch crosses that tolerance; no requirement that subcategory percentages sum exactly100 after rounding.
- **Direct observation versus inference:** Direct: source cell/header shows numerator, denominator and percentage. Derived: the printed denominator does not give the printed percentage under nearest rounding.
- **Source-grounded alternatives:** An unstated complete-case/parent denominator, denominator transcription, or truncation/other display convention may explain the mismatch. Source footnotes do not identify a replacement denominator for this cell. Differences close to a rounding boundary remain bounded display questions, not evidence of a changed conclusion.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Which denominator and display rule produced 22.5% for H 7/31 in Kidney failure,n/N(%), and should the printed denominator or percentage be interpreted differently?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP Failure 7/31 (22.5%); Low PEEP 5/32 (15.6%).
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: 100 × 7/31 = 22.580645%; nearest one-decimal display 22.6%, whereas 22.5% is printed; difference −0.080645 percentage points. The nearest-rounding interval for 22.5% is [22.45%, 22.55%), which excludes the exact quotient.
- Determining fact/state: The direct source confirms 7/31 (22.5%); the nearest-rounding discrepancy remains exactly as registered, pending the display convention. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Denominator, proportion, or total inconsistency; S_W; all S_W; REPORT main article Table 3 Failure count/denominator versus REPORT main article same-cell percentage; REPORT main article PDF p. 10 footnotes f/g define the row; statistical_results.
- Missing definition and human question: Was High PEEP Failure 22.5% calculated from the printed 7/31 and truncated toward zero, or from a different denominator/display procedure? Which definition should a data extractor use?

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C050 — Kidney loss,n/N(%): H printed percentage identity

**Candidate statement:** Kidney loss,n/N(%): H printed percentage identity; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Loss count/denominator versus REPORT main article same-cell percentage; REPORT main article PDF p. 10 footnotes f/g define the row
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O29-PCT-H

- **Numeric relationships:** N208.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O29 H count/denominator cell; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same cell printed percentage and No./total No. (%) or No. (%) row label.
- **Printed inputs:** H 2/31 (6.4%). Complete source-row components: Kidney loss,n/N(%); 2/31(6.4); 2/32(6.2); not printed; not printed; same.97.
- **Reproducible rule and calculation:** 100*2/31=6.451613%; printed 6.4%; discrepancy=-0.051613 pp; nearest one-decimal value=6.5%.
- **Tolerance:** 0.05 percentage point inclusive at ties; printed integer numerator/denominator exact. This mismatch crosses that tolerance; no requirement that subcategory percentages sum exactly100 after rounding.
- **Direct observation versus inference:** Direct: source cell/header shows numerator, denominator and percentage. Derived: the printed denominator does not give the printed percentage under nearest rounding.
- **Source-grounded alternatives:** An unstated complete-case/parent denominator, denominator transcription, or truncation/other display convention may explain the mismatch. Source footnotes do not identify a replacement denominator for this cell. Differences close to a rounding boundary remain bounded display questions, not evidence of a changed conclusion.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Which denominator and display rule produced 6.4% for H 2/31 in Kidney loss,n/N(%), and should the printed denominator or percentage be interpreted differently?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP Loss 2/31 (6.4%); Low PEEP 2/32 (6.2%).
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: 100 × 2/31 = 6.451613%; nearest one-decimal display 6.5%, whereas 6.4% is printed; difference −0.051613 percentage points. The nearest-rounding interval for 6.4% is [6.35%, 6.45%), which excludes the exact quotient.
- Determining fact/state: The direct source confirms 2/31 (6.4%); the nearest-rounding discrepancy remains exactly as registered, pending the display convention. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Denominator, proportion, or total inconsistency; S_W; all S_W; REPORT main article Table 3 Loss count/denominator versus REPORT main article same-cell percentage; REPORT main article PDF p. 10 footnotes f/g define the row; statistical_results.
- Missing definition and human question: Was High PEEP Loss 6.4% calculated from the printed 2/31 and truncated toward zero, or from a different denominator/display procedure? Which definition should a data extractor use?

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C051 — Extrapulmonary infection: labeled RR versus printed patient risks

**Candidate statement:** Extrapulmonary infection: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Extrapulmonary infection event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O30-RR; checkers/statistical_pass_1.md :: RR-O30; checkers/cross_source_consistency.md :: XR22

- **Numeric relationships:** N209.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O30 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 29/989; L 23/987; printed RR1.11(0.87 to1.42). Complete source-row components: Extrapulmonary infection; 29(2.9); 23(2.3); 0.6(−0.8 to2.0); RR1.11(0.87 to1.42); .40.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (29/989)/(23/987) = 1.258320; printed point = 1.11. Nearest two-decimal identity display would be 1.26; discrepancy=-0.148320.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Extrapulmonary infection, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.11, and is this value intended as the H/L event risk ratio from 29/989 and 23/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 29/989; Low PEEP 23/987; Risk Ratio 1.11 (0.87–1.42); P .40.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (29/989)/(23/987) = 1.258320; nearest two-decimal display 1.26; printed RR 1.11 differs by -0.148320.
- Determining fact/state: The directly confirmed event counts and denominators yield 1.258320, outside the nearest-rounding interval for printed 1.11. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Extrapulmonary infection event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Extrapulmonary infection, what exact event/reference orientation, population denominator, estimator and display rule produced RR 1.11 (0.87–1.42)? Is it the High/Low PEEP event-risk contrast from 29/989 and 23/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[29/(29+23)]/[(989−29)/(989+987−29−23)]=1.117708; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C052 — Hepatic failure: labeled RR versus printed patient risks

**Candidate statement:** Hepatic failure: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Hepatic failure event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O31-RR; checkers/statistical_pass_1.md :: RR-O31; checkers/cross_source_consistency.md :: XR23

- **Numeric relationships:** N210.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O31 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 9/989; L 9/987; printed RR0.99(0.63 to1.59). Complete source-row components: Hepatic failure; 9(0.9); 9(0.9); 0(−0.8 to0.8); RR0.99(0.63 to1.59); >.99.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (9/989)/(9/987) = 0.997978; printed point = 0.99. Nearest two-decimal identity display would be 1.00; discrepancy=-0.007978.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Hepatic failure, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.99, and is this value intended as the H/L event risk ratio from 9/989 and 9/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 9/989; Low PEEP 9/987; Risk Ratio 0.99 (0.63–1.59); P >.99.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (9/989)/(9/987) = 0.997978; nearest two-decimal display 1.00; printed RR 0.99 differs by -0.007978.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.997978, outside the nearest-rounding interval for printed 0.99. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Hepatic failure event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Hepatic failure, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.99 (0.63–1.59)? Is it the High/Low PEEP event-risk contrast from 9/989 and 9/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[9/(9+9)]/[(989−9)/(989+987−9−9)]=0.998980; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C053 — Coma: labeled RR versus printed patient risks

**Candidate statement:** Coma: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Coma event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O32-RR; checkers/statistical_pass_1.md :: RR-O32; checkers/cross_source_consistency.md :: XR24

- **Numeric relationships:** N211.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O32 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 2/989; L 2/987; printed RR0.99(0.37 to2.66). Complete source-row components: Coma; 2(0.2); 2(0.2); 0(−0.4 to0.4); RR0.99(0.37 to2.66); >.99.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (2/989)/(2/987) = 0.997978; printed point = 0.99. Nearest two-decimal identity display would be 1.00; discrepancy=-0.007978.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Coma, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.99, and is this value intended as the H/L event risk ratio from 2/989 and 2/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 2/989; Low PEEP 2/987; Risk Ratio 0.99 (0.37–2.66); P >.99.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (2/989)/(2/987) = 0.997978; nearest two-decimal display 1.00; printed RR 0.99 differs by -0.007978.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.997978, outside the nearest-rounding interval for printed 0.99. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Coma event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Coma, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.99 (0.37–2.66)? Is it the High/Low PEEP event-risk contrast from 2/989 and 2/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[2/(2+2)]/[(989−2)/(989+987−2−2)]=0.998987; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C054 — Disseminated intravascular coagulation: labeled RR versus printed patient risks

**Candidate statement:** Disseminated intravascular coagulation: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Disseminated intravascular coagulation event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O33-RR; checkers/statistical_pass_1.md :: RR-O33; checkers/cross_source_consistency.md :: XR25

- **Numeric relationships:** N212.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O33 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 1/989; L 0/987; printed RR2.00(1.91 to2.09). Complete source-row components: Disseminated intravascular coagulation; 1(0.1); 0; 0.1(−0.1 to0.3); RR2.00(1.91 to2.09); >.99.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (1/989)/(0/987) = undefined because the control-event risk is zero; printed point = 2.00. A finite value2.00 requires an additional estimator/continuity rule.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Disseminated intravascular coagulation, what exact event orientation, reference group, denominator and point-estimate estimator produced 2.00, and is this value intended as the H/L event risk ratio from 1/989 and 0/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 1/989; Low PEEP 0/987; Risk Ratio 2.00 (1.91–2.09); P >.99.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (1/989)/(0/987) is undefined because the Low PEEP event risk is zero.
- Determining fact/state: The directly confirmed 1/989 and 0/987 make a crude event RR undefined while 2.00 is printed. The undisclosed estimator/orientation is still the registered question. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Disseminated intravascular coagulation event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Disseminated intravascular coagulation, what exact event/reference orientation, population denominator, estimator and display rule produced RR 2.00 (1.91–2.09)? Is it the High/Low PEEP event-risk contrast from 1/989 and 0/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[1/(1+0)]/[(989−1)/(989+987−1−0)]=1.998988; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

