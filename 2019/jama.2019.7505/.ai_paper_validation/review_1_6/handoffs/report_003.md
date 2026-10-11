# Current source-confirmed report evidence shard

## C055 — Impaired postoperative wound healing: labeled RR versus printed patient risks

**Candidate statement:** Impaired postoperative wound healing: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Impaired postoperative wound healing event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O35-RR; checkers/statistical_pass_1.md :: RR-O35; checkers/cross_source_consistency.md :: XR26

- **Numeric relationships:** N214.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O35 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 22/989; L 26/987; printed RR0.91(0.66 to1.24). Complete source-row components: Impaired postoperative wound healing; 22(2.2); 26(2.6); −0.4(−1.8 to0.9); RR0.91(0.66 to1.24); .55.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (22/989)/(26/987) = 0.844443; printed point = 0.91. Nearest two-decimal identity display would be 0.84; discrepancy=0.065557.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Impaired postoperative wound healing, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.91, and is this value intended as the H/L event risk ratio from 22/989 and 26/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 22/989; Low PEEP 26/987; Risk Ratio 0.91 (0.66–1.24); P .55.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (22/989)/(26/987) = 0.844443; nearest two-decimal display 0.84; printed RR 0.91 differs by 0.065557.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.844443, outside the nearest-rounding interval for printed 0.91. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Impaired postoperative wound healing event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Impaired postoperative wound healing, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.91 (0.66–1.24)? Is it the High/Low PEEP event-risk contrast from 22/989 and 26/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[22/(22+26)]/[(989−22)/(989+987−22−26)]=0.913823; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C056 — UnexpectedICU admission/readmission: labeled RR versus printed patient risks

**Candidate statement:** UnexpectedICU admission/readmission: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Unexpected need for ICU admission or readmission event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O36-RR; checkers/statistical_pass_1.md :: RR-O36; checkers/cross_source_consistency.md :: XR27

- **Numeric relationships:** N215.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O36 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 41/989; L 32/987; printed RR1.12(0.91 to1.38). Complete source-row components: UnexpectedICU admission/readmission; 41(4.1); 32(3.2); 0.9(−0.8 to2.6); RR1.12(0.91 to1.38); .29.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (41/989)/(32/987) = 1.278659; printed point = 1.12. Nearest two-decimal identity display would be 1.28; discrepancy=-0.158659.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For UnexpectedICU admission/readmission, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.12, and is this value intended as the H/L event risk ratio from 41/989 and 32/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 41/989; Low PEEP 32/987; Risk Ratio 1.12 (0.91–1.38); P .29.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (41/989)/(32/987) = 1.278659; nearest two-decimal display 1.28; printed RR 1.12 differs by -0.158659.
- Determining fact/state: The directly confirmed event counts and denominators yield 1.278659, outside the nearest-rounding interval for printed 1.12. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Unexpected need for ICU admission or readmission event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Unexpected need for ICU admission or readmission, what exact event/reference orientation, population denominator, estimator and display rule produced RR 1.12 (0.91–1.38)? Is it the High/Low PEEP event-risk contrast from 41/989 and 32/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[41/(41+32)]/[(989−41)/(989+987−41−32)]=1.127435; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C057 — Intraoperative hypoxemia: labeled RR versus printed patient risks

**Candidate statement:** Intraoperative hypoxemia: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Intraoperative hypoxemia event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O39-RR; checkers/numeric_consistency.md :: NB-RR-HYPO; checkers/statistical_pass_1.md :: RR-O39; checkers/cross_source_consistency.md :: XR28

- **Numeric relationships:** N218.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O39 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 49/989; L 134/987; printed RR0.51(0.40 to0.65). Complete source-row components: Intraoperative hypoxemia; 49(5.0); 134(13.6); −8.6(−11.1 to−6.1); RR0.51(0.40 to0.65); <.001.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (49/989)/(134/987) = 0.364932; printed point = 0.51. Nearest two-decimal identity display would be 0.36; discrepancy=0.145068.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Intraoperative hypoxemia, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.51, and is this value intended as the H/L event risk ratio from 49/989 and 134/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.
Additional matched report locations and inputs from NB-RR-HYPO:
- Printed inputs:H49/989,L134/987;RR0.51.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 49/989; Low PEEP 134/987; Risk Ratio 0.51 (0.40–0.65); P <.001.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (49/989)/(134/987) = 0.364932; nearest two-decimal display 0.36; printed RR 0.51 differs by 0.145068.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.364932, outside the nearest-rounding interval for printed 0.51. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Intraoperative hypoxemia event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Intraoperative hypoxemia, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.51 (0.40–0.65)? Is it the High/Low PEEP event-risk contrast from 49/989 and 134/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[49/(49+134)]/[(989−49)/(989+987−49−134)]=0.510737; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C058 — Intraoperative hypotension: labeled RR versus printed patient risks

**Candidate statement:** Intraoperative hypotension: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Intraoperative hypotension event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O40-RR; checkers/statistical_pass_1.md :: RR-O40; checkers/cross_source_consistency.md :: XR29

- **Numeric relationships:** N219.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O40 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 313/989; L 170/987; printed RR1.43(1.31 to1.56). Complete source-row components: Intraoperative hypotension; 313(31.6); 170(17.2); 14.4(10.7 to18.2); RR1.43(1.31 to1.56); <.001.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (313/989)/(170/987) = 1.837453; printed point = 1.43. Nearest two-decimal identity display would be 1.84; discrepancy=-0.407453.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Intraoperative hypotension, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.43, and is this value intended as the H/L event risk ratio from 313/989 and 170/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 313/989; Low PEEP 170/987; Risk Ratio 1.43 (1.31–1.56); P <.001.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (313/989)/(170/987) = 1.837453; nearest two-decimal display 1.84; printed RR 1.43 differs by -0.407453.
- Determining fact/state: The directly confirmed event counts and denominators yield 1.837453, outside the nearest-rounding interval for printed 1.43. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Intraoperative hypotension event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Intraoperative hypotension, what exact event/reference orientation, population denominator, estimator and display rule produced RR 1.43 (1.31–1.56)? Is it the High/Low PEEP event-risk contrast from 313/989 and 170/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[313/(313+170)]/[(989−313)/(989+987−313−170)]=1.431233; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C059 — Intraoperative bradycardia: labeled RR versus printed patient risks

**Candidate statement:** Intraoperative bradycardia: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Intraoperative bradycardia event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O41-RR; checkers/statistical_pass_1.md :: RR-O41; checkers/cross_source_consistency.md :: XR30

- **Numeric relationships:** N220.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O41 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 98/989; L 59/987; printed RR1.27(1.11 to1.45). Complete source-row components: Intraoperative bradycardia; 98(9.9); 59(6.0); 3.9(1.5 to6.3); RR1.27(1.11 to1.45); .001.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (98/989)/(59/987) = 1.657658; printed point = 1.27. Nearest two-decimal identity display would be 1.66; discrepancy=-0.387658.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Intraoperative bradycardia, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.27, and is this value intended as the H/L event risk ratio from 98/989 and 59/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 98/989; Low PEEP 59/987; Risk Ratio 1.27 (1.11–1.45); P .001.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (98/989)/(59/987) = 1.657658; nearest two-decimal display 1.66; printed RR 1.27 differs by -0.387658.
- Determining fact/state: The directly confirmed event counts and denominators yield 1.657658, outside the nearest-rounding interval for printed 1.27. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Intraoperative bradycardia event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Intraoperative bradycardia, what exact event/reference orientation, population denominator, estimator and display rule produced RR 1.27 (1.11–1.45)? Is it the High/Low PEEP event-risk contrast from 98/989 and 59/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[98/(98+59)]/[(989−98)/(989+987−98−59)]=1.274329; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C060 — Mortality during hospital stay: labeled RR versus printed patient risks

**Candidate statement:** Mortality during hospital stay: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Mortality during hospital stay event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O42-RR; checkers/statistical_pass_1.md :: RR-O42; checkers/cross_source_consistency.md :: XR31

- **Numeric relationships:** N221.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O42 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 12/989; L 5/987; printed RR1.41(0.95 to1.81). Complete source-row components: Mortality during hospital stay; 12(1.2); 5(0.5); 0.7(−0.1 to1.5); RR1.41(0.95 to1.81); .09.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (12/989)/(5/987) = 2.395147; printed point = 1.41. Nearest two-decimal identity display would be 2.40; discrepancy=-0.985147.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Mortality during hospital stay, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.41, and is this value intended as the H/L event risk ratio from 12/989 and 5/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 12/989; Low PEEP 5/987; Risk Ratio 1.41 (0.95–1.81); P .09.
- Location: [main PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (12/989)/(5/987) = 2.395147; nearest two-decimal display 2.40; printed RR 1.41 differs by -0.985147.
- Determining fact/state: The directly confirmed event counts and denominators yield 2.395147, outside the nearest-rounding interval for printed 1.41. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Mortality during hospital stay event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Mortality during hospital stay, what exact event/reference orientation, population denominator, estimator and display rule produced RR 1.41 (0.95–1.81)? Is it the High/Low PEEP event-risk contrast from 12/989 and 5/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[12/(12+5)]/[(989−12)/(989+987−12−5)]=1.415377; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C061 — Post hoc rescue strategy for desaturation: absolute difference versus exact printed risks

**Candidate statement:** Post hoc rescue strategy for desaturation: absolute difference versus exact printed risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Numeric or arithmetic inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 continued rescue-strategy counts/denominators versus REPORT main article same row Absolute Difference; REPORT main article footnote a supplies reference-denominator context
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O43-RD

- **Numeric relationships:** N222.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), O43 H/L counts, explicit denominators or H989/L987 headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row Absolute Difference (95% CI) cell.
- **Printed inputs:** H 59(6.0); L 166(16.8); difference −10.8(−13.6 to−8.1). Complete source-row components: Post hoc rescue strategy for desaturation; 59(6.0); 166(16.8); −10.8(−13.6 to−8.1); RR0.49(0.39 to0.62); <.001.
- **Reproducible rule and calculation:** 100*(59/989−166/987)=-10.853021 pp; printed -10.8 pp; discrepancy=0.053021 pp; nearest one-decimal value=-10.9 pp. Displayed percentage subtraction=-10.800000 pp.
- **Tolerance:** 0.05 percentage point for an exact count-defined risk difference. The looser0.15 bound applies only when subtracting two already rounded percentages and does not alter the exact integer-count calculation.
- **Direct observation versus inference:** Direct: the two event cells and signed difference are in the same row. Derived: the printed count/denominator risks give a different nearest one-decimal effect. Comparator is H−L, consistent with the surrounding signed differences.
- **Source-grounded alternatives:** Truncation toward zero can reproduce several small boundary discrepancies. Model-based/adjusted absolute differences or a different denominator could also explain them; a row-specific computation/display rule is not supplied. These possibilities are the human question, not assumed corrections.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Post hoc rescue strategy for desaturation, was the absolute difference -10.8 calculated from the printed exact risks and then truncated, or from a different estimand/denominator? What computation and display rule should be used when extracting this result?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 59/989 (6.0%); Low PEEP 166/987 (16.8%); Absolute Difference −10.8 (−13.6 to −8.1) percentage points.
- Location: [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: 100 × (59/989 − 166/987) = −10.853021 percentage points; nearest one-decimal display −10.9, printed −10.8; difference +0.053021 percentage points. The nearest-rounding interval for −10.8 is approximately [−10.85, −10.75), which excludes the exact difference. Subtraction of the displayed risks, 6.0 − 16.8, equals −10.8.
- Determining fact/state: The direct source confirms the registered cells and −10.8 difference. Exact count-based nearest rounding gives −10.9, but displayed-percentage subtraction/truncation gives −10.8; the original conditional display question remains. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Numeric or arithmetic inconsistency; S_W; all S_W; REPORT main article Table 3 continued rescue-strategy counts/denominators versus REPORT main article same row Absolute Difference; REPORT main article footnote a supplies reference-denominator context; statistical_results.
- Missing definition and human question: Was the rescue-strategy absolute difference −10.8 calculated by subtracting the displayed percentages, truncating the exact count-defined difference toward zero, or using a different denominator/estimand? What computation and display rule should an extractor apply?

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C062 — Post hoc rescue strategy for desaturation: labeled RR versus printed patient risks

**Candidate statement:** Post hoc rescue strategy for desaturation: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Post hoc rescue strategy for desaturation event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O43-RR; checkers/statistical_pass_1.md :: RR-O43; checkers/cross_source_consistency.md :: XR32

- **Numeric relationships:** N222.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), O43 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 59/989; L 166/987; printed RR0.49(0.39 to0.62). Complete source-row components: Post hoc rescue strategy for desaturation; 59(6.0); 166(16.8); −10.8(−13.6 to−8.1); RR0.49(0.39 to0.62); <.001.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (59/989)/(166/987) = 0.354703; printed point = 0.49. Nearest two-decimal identity display would be 0.35; discrepancy=0.135297.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Post hoc rescue strategy for desaturation, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.49, and is this value intended as the H/L event risk ratio from 59/989 and 166/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 59/989; Low PEEP 166/987; Risk Ratio 0.49 (0.39–0.62); P <.001.
- Location: [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (59/989)/(166/987) = 0.354703; nearest two-decimal display 0.35; printed RR 0.49 differs by 0.135297.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.354703, outside the nearest-rounding interval for printed 0.49. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Post hoc rescue strategy for desaturation event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Post hoc rescue strategy for desaturation, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.49 (0.39–0.62)? Is it the High/Low PEEP event-risk contrast from 59/989 and 166/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[59/(59+166)]/[(989−59)/(989+987−59−166)]=0.493711; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C063 — Post hoc vasoactive drugs: labeled RR versus printed patient risks

**Candidate statement:** Post hoc vasoactive drugs: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Table 3 Post hoc need for vasoactive drugs event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O44-RR; checkers/statistical_pass_1.md :: RR-O44; checkers/cross_source_consistency.md :: XR33

- **Numeric relationships:** N223.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), O44 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 491/989; L 439/987; printed RR1.10(1.01 to1.21). Complete source-row components: Post hoc vasoactive drugs; 491(49.6); 439(44.5); 5.2(0.8 to9.6); RR1.10(1.01 to1.21); .02.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (491/989)/(439/987) = 1.116189; printed point = 1.10. Nearest two-decimal identity display would be 1.12; discrepancy=-0.016189.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Post hoc vasoactive drugs, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.10, and is this value intended as the H/L event risk ratio from 491/989 and 439/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 491/989; Low PEEP 439/987; Risk Ratio 1.10 (1.01–1.21); P .02.
- Location: [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3; method/footnotes [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10).
- Reproduced calculation: (491/989)/(439/987) = 1.116189; nearest two-decimal display 1.12; printed RR 1.10 differs by -0.016189.
- Determining fact/state: The directly confirmed event counts and denominators yield 1.116189, outside the nearest-rounding interval for printed 1.10. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Table 3 Post hoc need for vasoactive drugs event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Table 3 footnotes PDF p. 10 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Post hoc need for vasoactive drugs, what exact event/reference orientation, population denominator, estimator and display rule produced RR 1.10 (1.01–1.21)? Is it the High/Low PEEP event-risk contrast from 491/989 and 439/987, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[491/(491+439)]/[(989−491)/(989+987−491−439)]=1.108922; transposed conditioning compares High PEEP allocation by event status. Generic Wald approximation/χ² text does not supply table orientation, exact estimator, row-specific complete-case denominator or display rule.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C064 — Nonlaparoscopic: labeled RR versus printed patient risks

**Candidate statement:** Nonlaparoscopic: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Figure 2 Nonlaparoscopic surgery event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-F01-RR; checkers/statistical_pass_1.md :: RR-F01; checkers/cross_source_consistency.md :: XR34

- **Numeric relationships:** N225.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F01 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 79/240; L 74/253; printed 1.09(0.90-1.32). Complete source-row components: Nonlaparoscopic; 79/240; 74/253; 1.09(0.90-1.32); .08 shared withF02.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (79/240)/(74/253) = 1.125394; printed point = 1.09. Nearest two-decimal identity display would be 1.13; discrepancy=-0.035394.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Nonlaparoscopic, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.09, and is this value intended as the H/L event risk ratio from 79/240 and 74/253 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 79/240; Low PEEP 74/253; Risk Ratio 1.09 (0.90–1.32); P .08 interaction.
- Location: [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Figure 2; method/footnotes [main PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4).
- Reproduced calculation: (79/240)/(74/253) = 1.125394; nearest two-decimal display 1.13; printed RR 1.09 differs by -0.035394.
- Determining fact/state: The directly confirmed event counts and denominators yield 1.125394, outside the nearest-rounding interval for printed 1.09. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Figure 2 Nonlaparoscopic surgery event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Nonlaparoscopic surgery, what exact event/reference orientation, population denominator, estimator and display rule produced RR 1.09 (0.90–1.32)? Is it the High/Low PEEP event-risk contrast from 79/240 and 74/253, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[79/(79+74)]/[(240−79)/(240+253−79−74)]=1.090407; transposed conditioning compares High PEEP allocation by event status. Methods p.4 states binomialGLM interactions for heterogeneity but does not fix subgroup point-estimate link/adjustment; no equality to fitted RR or interaction-P/CI pairing is assumed.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C065 — Laparoscopic: labeled RR versus printed patient risks

**Candidate statement:** Laparoscopic: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Figure 2 Laparoscopic surgery event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-F02-RR; checkers/statistical_pass_1.md :: RR-F02; checkers/cross_source_consistency.md :: XR35

- **Numeric relationships:** N226.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F02 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 130/740; L 156/727; printed 0.88(0.77-1.01). Complete source-row components: Laparoscopic; 130/740; 156/727; 0.88(0.77-1.01); same.08.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (130/740)/(156/727) = 0.818694; printed point = 0.88. Nearest two-decimal identity display would be 0.82; discrepancy=0.061306.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Laparoscopic, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.88, and is this value intended as the H/L event risk ratio from 130/740 and 156/727 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 130/740; Low PEEP 156/727; Risk Ratio 0.88 (0.77–1.01); P .08 interaction.
- Location: [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Figure 2; method/footnotes [main PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4).
- Reproduced calculation: (130/740)/(156/727) = 0.818694; nearest two-decimal display 0.82; printed RR 0.88 differs by 0.061306.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.818694, outside the nearest-rounding interval for printed 0.88. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Figure 2 Laparoscopic surgery event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Laparoscopic surgery, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.88 (0.77–1.01)? Is it the High/Low PEEP event-risk contrast from 130/740 and 156/727, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[130/(130+156)]/[(740−130)/(740+727−130−156)]=0.880030; transposed conditioning compares High PEEP allocation by event status. Methods p.4 states binomialGLM interactions for heterogeneity but does not fix subgroup point-estimate link/adjustment; no equality to fitted RR or interaction-P/CI pairing is assumed.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C066 — BMI<40: labeled RR versus printed patient risks

**Candidate statement:** BMI<40: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Figure 2 Body mass index <40 event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-F03-RR; checkers/statistical_pass_1.md :: RR-F03; checkers/cross_source_consistency.md :: XR36

- **Numeric relationships:** N227.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F03 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 76/336; L 94/376; printed 0.93(0.77-1.13). Complete source-row components: BMI<40; 76/336; 94/376; 0.93(0.77-1.13); .97 shared withF04.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (76/336)/(94/376) = 0.904762; printed point = 0.93. Nearest two-decimal identity display would be 0.90; discrepancy=0.025238.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For BMI<40, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.93, and is this value intended as the H/L event risk ratio from 76/336 and 94/376 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 76/336; Low PEEP 94/376; Risk Ratio 0.93 (0.77–1.13); P .97 interaction.
- Location: [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Figure 2; method/footnotes [main PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4).
- Reproduced calculation: (76/336)/(94/376) = 0.904762; nearest two-decimal display 0.90; printed RR 0.93 differs by 0.025238.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.904762, outside the nearest-rounding interval for printed 0.93. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Figure 2 Body mass index <40 event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Body mass index <40, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.93 (0.77–1.13)? Is it the High/Low PEEP event-risk contrast from 76/336 and 94/376, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[76/(76+94)]/[(336−76)/(336+376−76−94)]=0.931946; transposed conditioning compares High PEEP allocation by event status. Methods p.4 states binomialGLM interactions for heterogeneity but does not fix subgroup point-estimate link/adjustment; no equality to fitted RR or interaction-P/CI pairing is assumed.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C067 — BMI≥40: labeled RR versus printed patient risks

**Candidate statement:** BMI≥40: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Figure 2 Body mass index ≥40 event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-F04-RR; checkers/statistical_pass_1.md :: RR-F04; checkers/cross_source_consistency.md :: XR37

- **Numeric relationships:** N228.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F04 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 135/653; L 139/611; printed 0.94(0.82-1.08). Complete source-row components: BMI≥40; 135/653; 139/611; 0.94(0.82-1.08); same.97.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (135/653)/(139/611) = 0.908755; printed point = 0.94. Nearest two-decimal identity display would be 0.91; discrepancy=0.031245.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For BMI≥40, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.94, and is this value intended as the H/L event risk ratio from 135/653 and 139/611 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 135/653; Low PEEP 139/611; Risk Ratio 0.94 (0.82–1.08); P .97 interaction.
- Location: [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Figure 2; method/footnotes [main PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4).
- Reproduced calculation: (135/653)/(139/611) = 0.908755; nearest two-decimal display 0.91; printed RR 0.94 differs by 0.031245.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.908755, outside the nearest-rounding interval for printed 0.94. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Figure 2 Body mass index ≥40 event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Body mass index ≥40, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.94 (0.82–1.08)? Is it the High/Low PEEP event-risk contrast from 135/653 and 139/611, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[135/(135+139)]/[(653−135)/(653+611−135−139)]=0.941648; transposed conditioning compares High PEEP allocation by event status. Methods p.4 states binomialGLM interactions for heterogeneity but does not fix subgroup point-estimate link/adjustment; no equality to fitted RR or interaction-P/CI pairing is assumed.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C068 — SpO2<96%: labeled RR versus printed patient risks

**Candidate statement:** SpO2<96%: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Figure 2 Peripheral oxygen saturation <96% event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-F05-RR; checkers/statistical_pass_1.md :: RR-F05; checkers/cross_source_consistency.md :: XR38

- **Numeric relationships:** N229.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F05 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 88/317; L 112/342; printed 0.88(0.74-1.06). Complete source-row components: SpO2<96%; 88/317; 112/342; 0.88(0.74-1.06); .35 shared withF06.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (88/317)/(112/342) = 0.847679; printed point = 0.88. Nearest two-decimal identity display would be 0.85; discrepancy=0.032321.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For SpO2<96%, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.88, and is this value intended as the H/L event risk ratio from 88/317 and 112/342 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 88/317; Low PEEP 112/342; Risk Ratio 0.88 (0.74–1.06); P .35 interaction.
- Location: [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Figure 2; method/footnotes [main PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4).
- Reproduced calculation: (88/317)/(112/342) = 0.847679; nearest two-decimal display 0.85; printed RR 0.88 differs by 0.032321.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.847679, outside the nearest-rounding interval for printed 0.88. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Figure 2 Peripheral oxygen saturation <96% event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Peripheral oxygen saturation <96%, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.88 (0.74–1.06)? Is it the High/Low PEEP event-risk contrast from 88/317 and 112/342, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[88/(88+112)]/[(317−88)/(317+342−88−112)]=0.881921; transposed conditioning compares High PEEP allocation by event status. Methods p.4 states binomialGLM interactions for heterogeneity but does not fix subgroup point-estimate link/adjustment; no equality to fitted RR or interaction-P/CI pairing is assumed.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C069 — SpO2≥96%: labeled RR versus printed patient risks

**Candidate statement:** SpO2≥96%: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Figure 2 Peripheral oxygen saturation ≥96% event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-F06-RR; checkers/statistical_pass_1.md :: RR-F06; checkers/cross_source_consistency.md :: XR39

- **Numeric relationships:** N230.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F06 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 123/672; L 121/645; printed 0.99(0.86-1.13). Complete source-row components: SpO2≥96%; 123/672; 121/645; 0.99(0.86-1.13); same.35.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (123/672)/(121/645) = 0.975686; printed point = 0.99. Nearest two-decimal identity display would be 0.98; discrepancy=0.014314.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For SpO2≥96%, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.99, and is this value intended as the H/L event risk ratio from 123/672 and 121/645 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 123/672; Low PEEP 121/645; Risk Ratio 0.99 (0.86–1.13); P .35 interaction.
- Location: [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Figure 2; method/footnotes [main PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4).
- Reproduced calculation: (123/672)/(121/645) = 0.975686; nearest two-decimal display 0.98; printed RR 0.99 differs by 0.014314.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.975686, outside the nearest-rounding interval for printed 0.99. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Figure 2 Peripheral oxygen saturation ≥96% event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Peripheral oxygen saturation ≥96%, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.99 (0.86–1.13)? Is it the High/Low PEEP event-risk contrast from 123/672 and 121/645, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[123/(123+121)]/[(672−123)/(672+645−123−121)]=0.985241; transposed conditioning compares High PEEP allocation by event status. Methods p.4 states binomialGLM interactions for heterogeneity but does not fix subgroup point-estimate link/adjustment; no equality to fitted RR or interaction-P/CI pairing is assumed.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C070 — Peripheral incision: labeled RR versus printed patient risks

**Candidate statement:** Peripheral incision: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Figure 2 Peripheral incision event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-F07-RR; checkers/statistical_pass_1.md :: RR-F07; checkers/cross_source_consistency.md :: XR40

- **Numeric relationships:** N231.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F07 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 32/126; L 25/126; printed 1.16(0.89-1.53). Complete source-row components: Peripheral incision; 32/126; 25/126; 1.16(0.89-1.53); .11 shared withF08.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (32/126)/(25/126) = 1.280000; printed point = 1.16. Nearest two-decimal identity display would be 1.28; discrepancy=-0.120000.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Peripheral incision, what exact event orientation, reference group, denominator and point-estimate estimator produced 1.16, and is this value intended as the H/L event risk ratio from 32/126 and 25/126 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 32/126; Low PEEP 25/126; Risk Ratio 1.16 (0.89–1.53); P .11 interaction.
- Location: [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Figure 2; method/footnotes [main PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4).
- Reproduced calculation: (32/126)/(25/126) = 1.280000; nearest two-decimal display 1.28; printed RR 1.16 differs by -0.120000.
- Determining fact/state: The directly confirmed event counts and denominators yield 1.280000, outside the nearest-rounding interval for printed 1.16. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Figure 2 Peripheral incision event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Peripheral incision, what exact event/reference orientation, population denominator, estimator and display rule produced RR 1.16 (0.89–1.53)? Is it the High/Low PEEP event-risk contrast from 32/126 and 25/126, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[32/(32+25)]/[(126−32)/(126+126−32−25)]=1.164614; transposed conditioning compares High PEEP allocation by event status. Methods p.4 states binomialGLM interactions for heterogeneity but does not fix subgroup point-estimate link/adjustment; no equality to fitted RR or interaction-P/CI pairing is assumed.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C071 — Upper abdominal: labeled RR versus printed patient risks

**Candidate statement:** Upper abdominal: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Figure 2 Upper abdominal incision event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-F08-RR; checkers/statistical_pass_1.md :: RR-F08; checkers/cross_source_consistency.md :: XR41

- **Numeric relationships:** N232.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F08 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 179/863; L 208/861; printed 0.90(0.80-1.02). Complete source-row components: Upper abdominal; 179/863; 208/861; 0.90(0.80-1.02); same.11.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (179/863)/(208/861) = 0.858583; printed point = 0.90. Nearest two-decimal identity display would be 0.86; discrepancy=0.041417.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Upper abdominal, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.90, and is this value intended as the H/L event risk ratio from 179/863 and 208/861 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 179/863; Low PEEP 208/861; Risk Ratio 0.90 (0.80–1.02); P .11 interaction.
- Location: [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Figure 2; method/footnotes [main PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4).
- Reproduced calculation: (179/863)/(208/861) = 0.858583; nearest two-decimal display 0.86; printed RR 0.90 differs by 0.041417.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.858583, outside the nearest-rounding interval for printed 0.90. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Figure 2 Upper abdominal incision event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Upper abdominal incision, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.90 (0.80–1.02)? Is it the High/Low PEEP event-risk contrast from 179/863 and 208/861, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[179/(179+208)]/[(863−179)/(863+861−179−208)]=0.904102; transposed conditioning compares High PEEP allocation by event status. Methods p.4 states binomialGLM interactions for heterogeneity but does not fix subgroup point-estimate link/adjustment; no equality to fitted RR or interaction-P/CI pairing is assumed.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C072 — Waist-to-hip<1.0: labeled RR versus printed patient risks

**Candidate statement:** Waist-to-hip<1.0: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article Figure 2 Waist-to-hip ratio <1.0 event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Compared counts, labels and completed-analysis descriptions are REPORT content within the main article. S_W is the sole discrepancy relationship; no conflicting PLAN or separate REPORT comparator. Registered primary category and mechanical domain confirmed.
**Classification ambiguity:** None about roles or relationship; exact estimator/display definitions remain named scientific input limitations.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-F09-RR; checkers/statistical_pass_1.md :: RR-F09; checkers/cross_source_consistency.md :: XR42

- **Numeric relationships:** N233.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F09 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 97/467; L 100/457; printed 0.97(0.83-1.13). Complete source-row components: Waist-to-hip<1.0; 97/467; 100/457; 0.97(0.83-1.13); .65 shared withF10.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (97/467)/(100/457) = 0.949229; printed point = 0.97. Nearest two-decimal identity display would be 0.95; discrepancy=0.020771.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Waist-to-hip<1.0, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.97, and is this value intended as the H/L event risk ratio from 97/467 and 100/457 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Exact current values: High PEEP 97/467; Low PEEP 100/457; Risk Ratio 0.97 (0.83–1.13); P .65 interaction.
- Location: [main PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Figure 2; method/footnotes [main PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4).
- Reproduced calculation: (97/467)/(100/457) = 0.949229; nearest two-decimal display 0.95; printed RR 0.97 differs by 0.020771.
- Determining fact/state: The directly confirmed event counts and denominators yield 0.949229, outside the nearest-rounding interval for printed 0.97. The registered label/estimator/display question remains pending its named definition. Evidence state recorded_candidate, mechanical suggestion retain.
- Classification: Measure, label, or scale inconsistency; S_W; all S_W; REPORT main article Figure 2 Waist-to-hip ratio <1.0 event counts/denominators versus REPORT main article same row Risk Ratio point/interval; REPORT main article Methods PDF p. 4 provides analysis/label context; report_internal_inconsistency.
- Missing definition and human question: For Waist-to-hip ratio <1.0, what exact event/reference orientation, population denominator, estimator and display rule produced RR 0.97 (0.83–1.13)? Is it the High/Low PEEP event-risk contrast from 97/467 and 100/457, a fitted contrast, or the differently conditioned quantity shown in the diagnostic?
- Alternative diagnostic: q=[97/(97+100)]/[(467−97)/(467+457−97−100)]=0.967472; transposed conditioning compares High PEEP allocation by event status. Methods p.4 states binomialGLM interactions for heterogeneity but does not fix subgroup point-estimate link/adjustment; no equality to fitted RR or interaction-P/CI pairing is assumed.

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C073 — Waist-to-hip ratio assigned a length unit

**Candidate statement:** Waist-to-hip ratio assigned a length unit; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main Figure 2 heading and REPORT main Table 1 ratio row
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.
**Classification ambiguity:** None
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-F09-UNIT; checkers/statistical_pass_1.md :: UNIT-F09-F10; checkers/cross_source_consistency.md :: XS05

- **Numeric relationships:** N233, N234.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Figure 2 waist-to-hip ratio,cm heading and F09/F10 rows; REPORT [PDF p. 5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table 1 waist-to-hip ratio row and<1.0/≥1.0 classifications.
- **Printed inputs:** Figure 2 heading Waist-to-hip ratio,cm; thresholds<1.0/≥1.0; H97/467 and98/447; L100/457 and112/449.. Complete source-row components: Waist-to-hip<1.0; 97/467; 100/457; 0.97(0.83-1.13); .65 shared withF10 / Waist-to-hip≥1.0; 98/447; 112/449; 0.92(0.78-1.08); same.65.
- **Reproducible rule and calculation:** A waist-to-hip ratio equals waist circumference/hip circumference; common length units cancel. Its unit is dimensionless, so cm is incompatible with the ratio label and threshold1.0.
- **Tolerance:** Exact dimensional identity; no numeric rounding tolerance.
- **Direct observation versus inference:** Direct: Figure 2 attaches cm to the named ratio. Derived: length divided by length is dimensionless. The main Table 1 waist-to-hip ratio also uses values1.01/1.00 rather than a length threshold.
- **Source-grounded alternatives:** cm may be a stray inherited circumference unit; threshold1.0 and subgroup denominators identify the intended dimensionless ratio. Actual circumference lengths in cm would require a different variable definition.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Is cm an unintended unit on the Figure 2 waist-to-hip ratio heading, or does the figure use a different waist measurement than the stated ratio?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. The directly printed ratio heading carries cm; the dimensional comparison reproduces. Diagnostic: Length/length has dimension 1; cm is a length unit, so it cannot denote that ratio. Classification S_W; all S_W; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: No raw measurement is needed; exact construction is not stated independently. Human question: Does cm belong to a different variable, or is the Figure 2 ratio intended to be dimensionless?

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C074 — Waist-to-hip≥1.0: labeled RR versus printed patient risks

**Candidate statement:** Waist-to-hip≥1.0: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main Figure 2 subgroup counts/point and REPORT main Methods model
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.
**Classification ambiguity:** Point-estimator alignment is unresolved; document roles/type remain within one REPORT.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-F10-RR; checkers/statistical_pass_1.md :: RR-F10; checkers/cross_source_consistency.md :: XR43

- **Numeric relationships:** N234.
- **Compared locations and content roles:** REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), F10 row event cells and H/L population headers; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), same row RR label/point/interval; REPORT [PDF p. 4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Methods subgroup model.
- **Printed inputs:** H 98/447; L 112/449; printed 0.92(0.78-1.08). Complete source-row components: Waist-to-hip≥1.0; 98/447; 112/449; 0.92(0.78-1.08); same.65.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (98/447)/(112/449) = 0.878915; printed point = 0.92. Nearest two-decimal identity display would be 0.88; discrepancy=0.041085.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Waist-to-hip≥1.0, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.92, and is this value intended as the H/L event risk ratio from 98/447 and 112/449 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Counts, RR label and point are confirmed; the registered conditional point-estimator/label question remains. The Methods GLM sentence explicitly concerns heterogeneity, so it does not independently identify or disprove the row-point estimator. Diagnostic: (98/447)/(112/449) = 0.878915; rounds to 0.88, versus 0.92. Classification S_W; all S_W; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Link, model formula, covariates, point-estimator derivation/standardization and whether plotted RR is marginal or conditional. Human question: Which link, contrast, adjustment and postprocessing generated 0.92, and does that point purport to equal the two displayed crude arm risks?

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C075 — Mortality figure caption attaches percentages to extrapulmonary complications

**Candidate statement:** Mortality figure caption attaches percentages to extrapulmonary complications; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT results supplement eFigure 11 title/axis/caption and eFigure 10; REPORT main mortality row corroborates
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.
**Classification ambiguity:** None
**Checker provenance:** checkers/cross_source_consistency.md :: XS03; checkers/parts/statistical_pass_1_planplots.md :: RF-DEATH; checkers/parts/numeric_planplots.md :: NP-F01

Compared locations: REPORT [eFigure11 p.41, title/axis/HR](../../../joi190055supp4_prod_16092.pdf#page=41) probability of death/5-day mortality,HR1.67(0.40–6.97),P.484; REPORT [same page caption](../../../joi190055supp4_prod_16092.pdf#page=41) calls0.5%H/0.3%L the “rate of postoperative extra-pulmonary complications”; REPORT [main Table3 p.10 mortality5day](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10)5(0.5)/3(0.3),HR1.67(0.40–6.97),P.48; REPORT [eFigure10 caption p.40](../../../joi190055supp4_prod_16092.pdf#page=40) actual extra-pulmonary percentages16.9/15.2. Identity: figure11 percentages/HR match5day mortality, whereas extrapulmonary outcome has a different label and values. The primary mismatch is internal to the results supplement; main merely corroborates mortality. Alternative: copied caption outcome wording versus mislabeled figure/title; no adjudication. Human verification: compare figure11 underlying endpoint coding/caption with figure10 and main mortality row.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Direct render shows mortality title/axis and an extra-pulmonary caption on the same page. Diagnostic: 0.5%/0.3% and HR/CI match mortality; extra-pulmonary comparator is 16.9%/15.2%. Classification S_W; all S_W; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Underlying endpoint code is absent; it is not needed to observe the literal label mismatch. Human question: Which endpoint was plotted in eFigure 11, and should its caption name mortality or extra-pulmonary complications?

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C076 — Collapsed-composite effect labeled OR in supplement and RR in main

**Candidate statement:** Collapsed-composite effect labeled OR in supplement and RR in main; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT supplement eFigure 12 global heading versus REPORT main primary table/abstract; PLAN final SAP corroborates RR
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** Cross-report estimator identity is conditional; SAP corroborates RR and creates no P_R discrepancy.
**Checker provenance:** checkers/cross_source_consistency.md :: XS04; checkers/parts/statistical_pass_1_planplots.md :: RF-COLLAPSED; checkers/parts/numeric_planplots.md :: NP-F03

Compared locations: REPORT [eFigure12 lower Global Tests p.42](../../../joi190055supp4_prod_16092.pdf#page=42), “Odds Ratio(95%CI)”, Collapsed Composite0.93[0.83,1.04]; REPORT [main Table3 primary p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), “Risk Ratio(95%CI)”, PPC0.93(0.83–1.04); REPORT [abstract p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1) also labelsRR. Both full-arm989/987 collapsed five-day composite, high versus low, identical point/interval. PLAN [finalSAP p.2](../../../joi190055supp3_prod_16092.pdf#page=2) corroborates intended primaryRR but does not add a separate discrepancy relationship. Identity rule: OR and RR are different measures; identical copied values do not justify interchangeable labeling. Alternative: forest-plot global heading applies only to other rows and collapsed row retainsRR, or separately fittedOR happens to coincide; no row exception/model is stated. Human verification: identify actual estimator for collapsed-composite row and its heading scope. Keep this distinct from count-derivedRR diagnostic below.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. The literal OR header above collapsed composite is confirmed in the current render; main labels identical display RR. Diagnostic: RR=pH/pL; OR=[pH/(1−pH)]/[pL/(1−pL)]. Identical point and CI are printed under the two headings. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Which estimator the collapsed-composite row actually uses; whether global header has a row exception. Human question: Does the Global Tests OR heading apply to Collapsed Composite, and what estimator produced that row versus main Table 3?

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C077 — Synthetic-colloid count comparison P differs

**Candidate statement:** Synthetic-colloid count comparison P differs; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Statistical reporting inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT main Table 2 receipt row versus REPORT results supplement eTable 3 receipt row
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** None
**Checker provenance:** checkers/cross_source_consistency.md :: XS06; checkers/parts/statistical_pass_1_tables.md :: TS1; checkers/parts/numeric_support_tables.md :: SUPPORT-NUM-01

Compared locations: REPORT [main Table2 p.8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8) binary Synthetic colloids74(7.5%) versus56(5.7%),P.09; REPORT [eTable3 p.24](../../../joi190055supp4_prod_16092.pdf#page=24) same count74/56, same full-arm989/987, P0.10. Both displayed to two decimals. Adjacent amount row is different: supplement50(211) versus35(171),P.09; main recipient medians0.5/0.5,P.50. Comparison deliberately matches only binary receipt, not quantities or medians. Direct observation: matched binary counts have different displayedP. Alternative: different χ² continuity corrections/Fisher conventions versus a copied adjacent-rowP; the exact Table2/eTable3 test convention is not supplied. Human verification: identify test/continuity correction and analysis set for each binary row, inspect original output, determine whether both values intentionally arise from different tests. An unstated test convention is a limitation, not an asserted method violation.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Direct native source confirms different P values for the same printed binary receipt counts. Diagnostic: 0.10−0.09 = 0.01; displays have the same two-decimal precision. No tail test is substituted. Classification S_C; all S_C; statistical_results; no role/type code correction.
- Missing definition and human question: Exact test and continuity correction/Fisher convention for each row; exact unrounded output. Human question: Were the two binary receipt P values generated with the same test/analysis set; if different, what conventions produced .09 and .10?

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C078 — Mild respiratory-failure oxygen boundary equals2 versus at most2

**Candidate statement:** Mild respiratory-failure oxygen boundary equals2 versus at most2; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Analysis-unit or population inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT main Table 3 footnote versus REPORT supplement eMethods definition
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** Operational equivalence of an exact-2 L test and a ≤2 response criterion is unresolved.
**Checker provenance:** checkers/cross_source_consistency.md :: XS07; checkers/parts/numeric_planplots.md :: NP-M01

Compared locations: REPORT [main Table3 footnote d p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), mild if responding to “2 L or less” supplemental oxygen; REPORT [results eMethods p.20](../../../joi190055supp4_prod_16092.pdf#page=20), mild if responding to supplemental oxygen **=2L/min** (direct PDF/image confirms equality sign), moderate responding only to>2L/min. Matched numerator labels are main135/989 versus154/987 and the12-component composite. Equality and≤ are different criteria for response below2L/min; this changes which patients qualify for the named mild component. Alternative: equality glyph is a typographic substitution for≤, or an exact2L test response was operationally required. Human verification: inspect source CRF/endpoint dictionary and confirm how patients responding below2L/min were classified; do not infer a revised count from unavailable raw data.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Current source image confirms =2, while main prints 2 L or less. Diagnostic: A response at 1 L/min satisfies ≤2 but not =2. No revised count is inferable. Classification S_C; all S_C; statistical_results; no role/type code correction.
- Missing definition and human question: Operational oxygen test and endpoint dictionary; classification below 2 L/min. Human question: How were patients responding below 2 L/min classified, and which boundary generated the mild respiratory-failure counts?

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C079 — Emergency-procedure counts differ between main and surgical supplement

**Candidate statement:** Emergency-procedure counts differ between main and surgical supplement; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Cross-document numeric inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT main baseline Table 1 emergency procedure versus REPORT supplement surgical priority eTable 6
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** Emergency timing/category and available-case identity remain unconfirmed.
**Checker provenance:** checkers/cross_source_consistency.md :: XS08

Compared locations: REPORT [Table1 p.5 Emergency procedure](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5)21(2.1%)H/20(2.0%)L; REPORT [eTable6 p.27 Priority of surgery](../../../joi190055supp4_prod_16092.pdf#page=27) Emergency13(1.3%)/11(1.1%), Urgent9(0.9%)/13(1.3%), Elective962/958, headings989/987. Direct numeric differences:8H and9L; merging emergency+urgent yields22H/24L, still not21/20. Whole priority groups sum984/982 and indicate different observed completeness. Identity matches treatment groups and surgical emergency label, but baseline-versus-final priority timing and urgency mapping are not explicitly linked. Alternative: different assessment times/categories or available-case subsets, versus inconsistent repeated label/count. Human verification: locate emergency definition, timing, analysis subset and cross-tabulation; determine whether main label intentionally pools an urgent subgroup. No claim that observed counts must be identical absent that missing mapping.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Exact repeated emergency counts differ as registered; the missing mapping remains the named conditional question. Diagnostic: Main−supplement emergency =8 high/9 low; emergency+urgent =22/24; priority totals =984/982. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Baseline versus surgical-time definition, urgency crosswalk, missing records and actual observed denominators. Human question: Are main emergency procedure and supplemental emergency priority the same field/time; if so, how are 21/20 reconciled with 13/11, and if not, what mapping defines them?

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C080 — Hypoxemia count has duration-qualified and unqualified definitions

**Candidate statement:** Hypoxemia count has duration-qualified and unqualified definitions; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Analysis-unit or population inconsistency
**Relationship type:** S_C
**All relationships:** S_C, S_W
**Compared document roles:** REPORT main Methods/count footnote versus REPORT supplement eMethods; PLAN protocol duration/RM fields corroborate the two descriptions
**Review domain:** statistical_results
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. A within-main REPORT comparison is also registered; S_C takes precedence over S_W.
**Classification ambiguity:** Original S_C plus S_W comparison is retained as the registered relationship; plan corroboration adds no P_R/P_P discrepancy.
**Checker provenance:** checkers/cross_source_consistency.md :: XS10

Compared locations: REPORT [main secondary Methods p.3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), SpO2≤92% for>1minute; REPORT [abstract p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1) same>1minute; REPORT [Table3 p.9 hypoxemia count](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9)49(5.0%)H/134(13.6%)L, linked footnotei on REPORT [p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) “SpO2 of92% or less; or any decline ... greater than5% if ... previously less than92%,” with no duration stated. REPORT [eMethods p.21](../../../joi190055supp4_prod_16092.pdf#page=21) defines hypoxemia≤92%, also without duration. PLAN [protocol p.12](../../../joi190055supp1_prod_16092.pdf#page=12) corroborates>1min while PLAN [p.19](../../../joi190055supp1_prod_16092.pdf#page=19) RM-event field is threshold/drop-based without duration. Concrete issue: the same reported adverse-event numerator is attached to definitions that do not expressly share the duration qualifier. Below92 baseline relative-decline clause is not treated as a separate candidate because a further decline also satisfies≤92. Alternative: footnote/eMethods are abbreviated summaries retaining the body duration versus a different operational event field. Human verification: identify the exact event variable counted49/134, whether brief episodes are excluded, and whether body and footnote describe the same event window. This is conditional numerator-definition inconsistency, not proof of different raw counts. Plan's two definitions mirror report alternatives, so classification must consider substantive comparison rather than merely plan corroboration.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: record_input_error. The comparison treats omission of a qualifier as a different operational rule, but source supplies no affirmative no-duration rule or field identity; residual count discrepancy cannot be settled. Diagnostic: Printed duration appears in body and is not repeated in footnote/eMethods. No count change can be calculated. The below-baseline drop clause does not itself contradict the threshold because the patient remains below it. Classification S_C; all S_C, S_W; statistical_results; no role/type code correction.
- Missing definition and human question: Counted event field, duration filtering, whole-intraoperative versus recruitment-only window, and whether footnote/eMethods abbreviate the Methods. Human question: Which exact variable/window generated 49/134 hypoxemia, did it apply the Methods duration, and are footnote/eMethods abbreviated descriptions of that same variable?

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

## C081 — Hypotension count has duration-qualified and unqualified definitions

**Candidate statement:** Hypotension count has duration-qualified and unqualified definitions; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Analysis-unit or population inconsistency
**Relationship type:** S_C
**All relationships:** S_C, S_W
**Compared document roles:** REPORT main Methods/count footnote versus REPORT supplement eMethods; PLAN protocol duration/RM fields corroborate the two descriptions
**Review domain:** statistical_results
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. A within-main REPORT comparison is also registered; S_C takes precedence over S_W.
**Classification ambiguity:** Original S_C plus S_W comparison is retained as the registered relationship; plan corroboration adds no P_R/P_P discrepancy.
**Checker provenance:** checkers/cross_source_consistency.md :: XS11

Compared locations: REPORT [main secondary Methods p.3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), systolic<90mmHg for>2minutes; REPORT [Table3 p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9)313(31.6%)H/170(17.2%)L, footnotej REPORT [p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) systolic<90 or decrease>10mmHg if previously<90, without duration; REPORT [eMethods p.21](../../../joi190055supp4_prod_16092.pdf#page=21) systolic<90 only. PLAN [protocol p.12](../../../joi190055supp1_prod_16092.pdf#page=12) has<90 for>2min during recruitment, and PLAN [p.19](../../../joi190055supp1_prod_16092.pdf#page=19) RM-event field threshold/drop rule without duration. Same printed numerator therefore lacks a single expressly consistent duration/window definition. Alternative: abbreviated footnote retaining duration versus different RM-event/intraoperative episode fields. A further decrease from already<90 also satisfies<90 and is not an independent threshold contradiction. Human verification: confirm exact counted313/170 variable, duration, recruitment-only versus whole intraoperative window, and how definitions were abbreviated. No reconstructed count or protocol violation is asserted.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: record_input_error. The comparison treats omission of a qualifier as a different operational rule, but source supplies no affirmative no-duration rule or field identity; residual count discrepancy cannot be settled. Diagnostic: Printed duration appears in body and is not repeated in footnote/eMethods. No count change can be calculated. The below-baseline drop clause does not itself contradict the threshold because the patient remains below it. Classification S_C; all S_C, S_W; statistical_results; no role/type code correction.
- Missing definition and human question: Counted event field, duration filtering, whole-intraoperative versus recruitment-only window, and whether footnote/eMethods abbreviate the Methods. Human question: Which exact variable/window generated 313/170 hypotension, did it apply the Methods duration, and are footnote/eMethods abbreviated descriptions of that same variable?

**Audited reporting guidance:** The source-confirmed recheck governs the current interpretation. See [audit wording requirements](../quality/audit_wording_amendments.md) for candidate-specific precision, denominator, estimator and input-error safeguards; original checker prose is preserved as registration provenance.

