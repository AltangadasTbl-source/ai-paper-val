# Current-run audit evidence shard

## C001 — abstract randomized-group populations equal analyzed populations

**Candidate statement:** abstract randomized-group populations equal analyzed populations; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Analysis-unit or population inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/numeric_consistency.md :: NB-ALLOC; checkers/cross_source_consistency.md :: XS02

- Relationships:N002,N007,N008.
- Compared locations and roles: REPORT [main PDF p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1), abstract INTERVENTIONS, “Patients were randomized” H n=989/L n=987; REPORT [main PDF p.3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), Figure1 allocated H1011/L1002 and primary-analysis H989/L987; REPORT [main PDF p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4), Results2013 randomized and1976 analyzed.
- Printed inputs:989,987 vs1011,1002;2013 randomized;1976 analyzed.
- Rule/calculation: randomized group counts should describe the same allocation population;989+987=1976 vs1011+1002=2013. Differences22 high and15 low sum37, equal2013−1976.
- Tolerance:zero for exact counts and population labels.
- Direct observation: identical abstract and Figure1 analysis counts are called randomized in the abstract; flow separately labels the larger randomized counts. Inference: abstract may have inserted analysis sizes into intervention description.
- Alternatives: abstract may conventionally summarize treatment groups using their analyzed sizes; that resolves the intended referent if expressly relabeled, but does not make the literal allocation populations equal.
- Quality-control relevance: extraction of allocated versus analyzed denominators may differ by37 patients.
- Exact human question: Should the abstract INTERVENTIONS group sizes describe randomized allocation1011/1002 or analyzed patients989/987?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Abstract INTERVENTIONS and RESULTS (p. 1); Figure 1 allocation and primary-analysis boxes (p. 3); Statistical Analysis and Results population descriptions (p. 4). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 1](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=1>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 3](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=3>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>)
- Printed inputs: Abstract: randomized high n=989 and low n=987; Figure 1: 1011 and 1002 randomized/allocated, 989 and 987 included in primary analysis; Results: 2013 randomized, 1976 analyzed.
- Registered comparator/rule: Explicit allocation counts 1011/1002 and total 2013 versus abstract randomized-labelled counts 989/987. Exact population-label and allocation-count identity; randomized denominators and analyzed denominators must be distinguished when their printed values differ.
- Reproduced calculation: 989 + 987 = 1976; 1011 + 1002 = 2013; high difference 22, low difference 15; 22 + 15 = 37 = 2013 − 1976.
- Determining fact/state: The exact source retains randomized wording with analysis sizes and separately prints larger allocation sizes. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: None for literal count/label comparison. Intended abstract referent remains unnamed. Should the abstract INTERVENTIONS n values describe the allocated groups (1011/1002) or the analyzed groups (989/987)?
- Alternative and direct-versus-inferred boundary: The abstract can be read as a compressed description of analyzed treatment groups; its RESULTS explicitly distinguishes 2013 randomized from 1976 completing the trial. That does not make the INTERVENTIONS n values the allocation counts. Direct: the population labels and four arm counts. Inferred: analyzed sizes may have been inserted into the allocation description; no production mechanism is established.

## C002 — matched hypoxemia confidence-limit sign differs

**Candidate statement:** matched hypoxemia confidence-limit sign differs; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Statistical reporting inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/numeric_consistency.md :: NB-HYPO-CI; checkers/statistical_pass_1.md :: CI-O39-ABSTRACT; checkers/cross_source_consistency.md :: XS01

- Relationship:N005.
- Compared locations and roles: REPORT [main PDF p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1), abstract Results hypoxemia difference−8.6%,95%CI−11.1% to positive6.1%,P<.001; REPORT [main PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), Table3 hypoxemia same difference−8.6%,95%CI−11.1 to−6.1,P<.001.
- Printed inputs:upper endpoint+6.1 versus−6.1; same outcome,groups,time,difference and P.
- Rule/calculation: matching confidence limits should agree at equal display precision;(+6.1)−(−6.1)=12.2 percentage points. Abstract interval crosses0 while Table3 interval does not.
- Tolerance:zero for matched signs; endpoint display±0.05 cannot reconcile12.2.
- Direct observation: sign mismatch; inference: a minus sign may have been omitted. No CI convention needs to be assumed for matched-source equality.
- Alternatives: no distinct model/population is labeled for the abstract estimate; a separate analysis would need identification. Source layout text expressly retains the positive sign.
- Quality-control relevance: interval crossing of the null differs for downstream extraction.
- Exact human question: Which signed upper confidence limit belongs to the abstract hypoxemia difference, and is the abstract intended to reproduce Table3?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Abstract RESULTS hypoxemia sentence (p. 1); Table 3 Intraoperative adverse events, Hypoxemia row (p. 9). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 1](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=1>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>)
- Printed inputs: Abstract difference −8.6%, 95% CI −11.1% to +6.1%, P<.001; Table 3 difference −8.6%, 95% CI −11.1 to −6.1, P<.001.
- Registered comparator/rule: Signed upper CI limit +6.1 in the abstract versus −6.1 in Table 3 for the matched outcome/contrast. Matched-report identity at equal precision; no CI/P convention is needed to compare the endpoint signs.
- Reproduced calculation: +6.1 − (−6.1) = 12.2 percentage points. The abstract interval includes zero and the table interval does not. Endpoint rounding cannot reconcile the sign difference.
- Determining fact/state: Fresh direct extraction and visual rendering both show positive 6.1 in the abstract and negative −6.1 in Table 3. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: None for the literal sign mismatch. A distinct abstract model/population is not identified. Which signed upper CI limit belongs to the abstract hypoxemia difference, and is the abstract intended to repeat Table 3?
- Alternative and direct-versus-inferred boundary: An omitted minus sign is a plausible explanation. If the abstract refers to a different analysis, its identity and model must be supplied; the printed point difference and P value match the table. Direct: both endpoints and matched contrast. Inferred: omitted minus sign; no inference that one CI must be adopted.

## C003 — complementary surgical-approach rows switch denominators — H arm

**Candidate statement:** complementary surgical-approach rows switch denominators — H arm; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/numeric_consistency.md :: NB-APPROACH

- Relationships:N098,N101; contextual N003,N099,N100.
- Compared locations and roles: REPORT [main PDF p.6](../../../jama_bluth_2019_oi_190055_16092.pdf#page=6), Table1 Surgical approach “Type of abdominal incision” H894/986(90.7),L884/987(89.6); REPORT same table “Nonabdominal” H92/987(9.3),L102/986(10.3); REPORT same footnotes a (some characteristics missing) and i (abdominal open/endoscopic definitions).
- Printed inputs:high denominators986 versus987;low987 versus986;high counts894+92;low884+102.
- Rule/calculation: abdominal and nonabdominal are complementary labels for one surgical-approach classification and would ordinarily share an observed-population denominator. Both count sums=986, while the displayed denominators alternate986/987. High count sum agrees abdominal denominator986 but differs nonabdominal987 by1; low count sum agrees nonabdominal986 but differs abdominal987 by1. Endoscopic+open sums exactly894/884.
- Tolerance:zero for exact denominators/sums.
- Direct observation: denominator switches and count sums. Inference: denominator transposition or differently missing category indicators; a common underlying population is a label-based assumption.
- Alternatives: independently missing category-specific binary indicators could legitimately use different denominators; footnote a permits missingness but does not describe such separate indicators or explain complementary rows.
- Quality-control relevance: denominator and missingness extraction for surgical approach becomes ambiguous.
- Exact human question: Were abdominal and nonabdominal surgery measured as one mutually exclusive classification; if so what common denominator applies in each group, and if not why do their category-specific denominators differ?
- Registered scope: this record compares only the H arm abdominal/nonabdominal denominators and count sum; the other arm is registered separately.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 1 Surgical approach, Type of abdominal incision and Nonabdominal H cells; footnotes a and i (p. 6). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 6](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=6>)
- Printed inputs: H: abdominal 894/986, nonabdominal 92/987. Footnote a permits characteristics not assessed in all patients; i defines abdominal open and endoscopic categories.
- Registered comparator/rule: The same arm's two printed denominators 986 and 987 and complementary-labelled category sum. A single mutually exclusive/exhaustive abdominal-versus-nonabdominal classification has one observed denominator. Applicability is conditional on these rows being one classification, rather than independently missing binary indicators.
- Reproduced calculation: 894 + 92 = 986; printed denominators differ by one (986 versus 987). The sum equals 986 and differs from 987 by one.
- Determining fact/state: The source reproduces the denominator switch and count sum; the same-classification question remains as registered pending its named definition. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Both printed fractions and footnotes are available. Missing: whether the two categories share one observed surgical-approach variable and, if so, its common denominator. For the H arm, are abdominal and nonabdominal entries categories of one mutually exclusive variable; if so, which common denominator applies, and if not, what explains the separate denominators?
- Alternative and direct-versus-inferred boundary: Footnote a allows missingness; independent category-specific indicators could have distinct observed denominators. It does not expressly define such separate indicators. A denominator transposition is an inferred explanation, not established. Direct: numerator/denominator cells, category labels and footnotes. Conditional derivation: one shared classification denominator. Inferred: transposed denominators or differently missing indicators.

## C004 — complementary surgical-approach rows switch denominators — L arm

**Candidate statement:** complementary surgical-approach rows switch denominators — L arm; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/numeric_consistency.md :: NB-APPROACH

- Relationships:N098,N101; contextual N003,N099,N100.
- Compared locations and roles: REPORT [main PDF p.6](../../../jama_bluth_2019_oi_190055_16092.pdf#page=6), Table1 Surgical approach “Type of abdominal incision” H894/986(90.7),L884/987(89.6); REPORT same table “Nonabdominal” H92/987(9.3),L102/986(10.3); REPORT same footnotes a (some characteristics missing) and i (abdominal open/endoscopic definitions).
- Printed inputs:high denominators986 versus987;low987 versus986;high counts894+92;low884+102.
- Rule/calculation: abdominal and nonabdominal are complementary labels for one surgical-approach classification and would ordinarily share an observed-population denominator. Both count sums=986, while the displayed denominators alternate986/987. High count sum agrees abdominal denominator986 but differs nonabdominal987 by1; low count sum agrees nonabdominal986 but differs abdominal987 by1. Endoscopic+open sums exactly894/884.
- Tolerance:zero for exact denominators/sums.
- Direct observation: denominator switches and count sums. Inference: denominator transposition or differently missing category indicators; a common underlying population is a label-based assumption.
- Alternatives: independently missing category-specific binary indicators could legitimately use different denominators; footnote a permits missingness but does not describe such separate indicators or explain complementary rows.
- Quality-control relevance: denominator and missingness extraction for surgical approach becomes ambiguous.
- Exact human question: Were abdominal and nonabdominal surgery measured as one mutually exclusive classification; if so what common denominator applies in each group, and if not why do their category-specific denominators differ?
- Registered scope: this record compares only the L arm abdominal/nonabdominal denominators and count sum; the other arm is registered separately.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 1 Surgical approach, Type of abdominal incision and Nonabdominal L cells; footnotes a and i (p. 6). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 6](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=6>)
- Printed inputs: L: abdominal 884/987, nonabdominal 102/986. Footnote a permits characteristics not assessed in all patients; i defines abdominal open and endoscopic categories.
- Registered comparator/rule: The same arm's two printed denominators 987 and 986 and complementary-labelled category sum. A single mutually exclusive/exhaustive abdominal-versus-nonabdominal classification has one observed denominator. Applicability is conditional on these rows being one classification, rather than independently missing binary indicators.
- Reproduced calculation: 884 + 102 = 986; printed denominators differ by one (987 versus 986). The sum equals 986 and differs from 987 by one.
- Determining fact/state: The source reproduces the denominator switch and count sum; the same-classification question remains as registered pending its named definition. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Both printed fractions and footnotes are available. Missing: whether the two categories share one observed surgical-approach variable and, if so, its common denominator. For the L arm, are abdominal and nonabdominal entries categories of one mutually exclusive variable; if so, which common denominator applies, and if not, what explains the separate denominators?
- Alternative and direct-versus-inferred boundary: Footnote a allows missingness; independent category-specific indicators could have distinct observed denominators. It does not expressly define such separate indicators. A denominator transposition is an inferred explanation, not established. Direct: numerator/denominator cells, category labels and footnotes. Conditional derivation: one shared classification denominator. Inferred: transposed denominators or differently missing indicators.

## C005 — Reflux,n/N(%), high group

**Candidate statement:** Reflux,n/N(%), high group; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/numeric_consistency.md :: NB-PCT-B32-H

- Relationship: N060; mapped B32. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Reflux,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 332/986 (33.6%); explicit denominator 986.
- Reproducible rule/calculation: patient percentage=100×n/N;100×332/986=33.671399594%, which rounds to33.7% under nearest-one-decimal rounding. Printed33.6% differs by0.071399594 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Reflux,n/N(%) percentage33.6%, and which printed component should be used when the cell is reconciled?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 1 Gastroesophageal reflux, H cell (p. 5). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=5>)
- Printed inputs: H cell 332/986 (33.6%); the row prints No./total No. (%) or inherits that explicit parent label.
- Registered comparator/rule: Printed percentage 33.6% versus the same cell's exact fraction 332/986. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.
- Reproduced calculation: 100 × 332/986 = 33.671399594%; nearest one-decimal = 33.7%; printed = 33.6%; absolute gap = 0.071399594 percentage point. One-decimal truncation gives 33.6%, reproducing this display.
- Determining fact/state: The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the H-group Gastroesophageal reflux percentage 33.6%, and which count/population definition should be used for extraction?
- Alternative and direct-versus-inferred boundary: The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

## C006 — Diabetes,n/N(%), high group

**Candidate statement:** Diabetes,n/N(%), high group; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/numeric_consistency.md :: NB-PCT-B33-H

- Relationship: N061; mapped B33. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Diabetes,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 294/988 (29.7%); explicit denominator 988.
- Reproducible rule/calculation: patient percentage=100×n/N;100×294/988=29.757085020%, which rounds to29.8% under nearest-one-decimal rounding. Printed29.7% differs by0.057085020 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Diabetes,n/N(%) percentage29.7%, and which printed component should be used when the cell is reconciled?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 1 Diabetes, H cell (p. 5). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=5>)
- Printed inputs: H cell 294/988 (29.7%); the row prints No./total No. (%) or inherits that explicit parent label.
- Registered comparator/rule: Printed percentage 29.7% versus the same cell's exact fraction 294/988. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.
- Reproduced calculation: 100 × 294/988 = 29.757085020%; nearest one-decimal = 29.8%; printed = 29.7%; absolute gap = 0.057085020 percentage point. One-decimal truncation gives 29.7%, reproducing this display.
- Determining fact/state: The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the H-group Diabetes percentage 29.7%, and which count/population definition should be used for extraction?
- Alternative and direct-versus-inferred boundary: The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

## C007 — Diabetes oral medication,n/N(%), high group

**Candidate statement:** Diabetes oral medication,n/N(%), high group; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/numeric_consistency.md :: NB-PCT-B34-H

- Relationship: N062; mapped B34. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Diabetes oral medication,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 209/294 (71.0%); explicit denominator 294.
- Reproducible rule/calculation: patient percentage=100×n/N;100×209/294=71.088435374%, which rounds to71.1% under nearest-one-decimal rounding. Printed71.0% differs by0.088435374 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Diabetes oral medication,n/N(%) percentage71.0%, and which printed component should be used when the cell is reconciled?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 1 Diabetes — Take oral medication, H cell (p. 5). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=5>)
- Printed inputs: H cell 209/294 (71.0%); the row prints No./total No. (%) or inherits that explicit parent label.
- Registered comparator/rule: Printed percentage 71.0% versus the same cell's exact fraction 209/294. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.
- Reproduced calculation: 100 × 209/294 = 71.088435374%; nearest one-decimal = 71.1%; printed = 71.0%; absolute gap = 0.088435374 percentage point. One-decimal truncation gives 71.0%, reproducing this display.
- Determining fact/state: The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the H-group Diabetes — Take oral medication percentage 71.0%, and which count/population definition should be used for extraction?
- Alternative and direct-versus-inferred boundary: The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

## C008 — Obstructive sleep apnea,No.(%), low group

**Candidate statement:** Obstructive sleep apnea,No.(%), low group; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** The registration assigned the group header as an exact row denominator despite source footnote a's missingness qualification; the residual percentage issue cannot be settled without the observed denominator.
**Checker provenance:** checkers/numeric_consistency.md :: NB-PCT-B36-L

- Relationship: N064; mapped B36. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Obstructive sleep apnea,No.(%), L cell numerator/denominator; REPORT same cell percentage; REPORT same-page group header L n=987 and footnote a on p.6.
- Printed inputs: 264 (26.8%); header population 987.
- Reproducible rule/calculation: patient percentage=100×n/N;100×264/987=26.747720365%, which rounds to26.7% under nearest-one-decimal rounding. Printed26.8% differs by0.052279635 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell and header values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: footnote a permits unreported variable-specific missingness; an undocumented denominator could account for a small display difference. Simple truncation does not reconcile this particular difference. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the low-group Obstructive sleep apnea,No.(%) percentage26.8%, and which printed component should be used when the cell is reconciled?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 1 Obstructive sleep apnea, L cell (p. 5); low-group n=987 header (p. 5) and missing-characteristics footnote a (p. 6). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=5>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 6](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=6>)
- Printed inputs: L cell 264 (26.8%); 987 is the group header, not an explicit cell denominator. Footnote a says some characteristics were not assessed in all patients.
- Registered comparator/rule: The registered comparator uses header n=987 as though it were the row's exact observed denominator. That alignment is not supplied. 100 × n/N is applicable only after the variable's observed denominator N is established. Header population cannot silently replace a variable denominator when the table explicitly permits missingness.
- Reproduced calculation: 100 × 264/987 = 26.747720365%; nearest one-decimal = 26.7%; printed = 26.8%; absolute gap = 0.052279635 percentage point. This reproduces only the header-denominator diagnostic, not a confirmed row-denominator contradiction. 100 × 264/986 = 26.774847870%, which rounds to 26.8%.
- Determining fact/state: The registration assigned the group header as an exact row denominator despite source footnote a's missingness qualification; the residual percentage issue cannot be settled without the observed denominator. Evidence state record_input_error.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Missing: exact observed denominator for obstructive sleep apnea and actual display rule. The source provides the count and overall group population, not that row denominator. What exact observed denominator and display rule generated the L-group Obstructive sleep apnea percentage 26.8%, and which count/population definition should be used for extraction?
- Alternative and direct-versus-inferred boundary: A variable-specific denominator of 986 is arithmetically compatible with the display and with footnote a's missingness allowance, but the source does not assert 986 for this row. Direct: 264 (26.8), header 987 and missingness footnote. Inferred: treating 987 as this variable's observed denominator; the alternative 986 is a diagnostic, not a source count.

## C009 — Tobacco never,n/N(%), high group

**Candidate statement:** Tobacco never,n/N(%), high group; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/numeric_consistency.md :: NB-PCT-B37-H

- Relationship: N065; mapped B37. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Tobacco never,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 549/987 (55.5%); explicit denominator 987.
- Reproducible rule/calculation: patient percentage=100×n/N;100×549/987=55.623100304%, which rounds to55.6% under nearest-one-decimal rounding. Printed55.5% differs by0.123100304 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Simple truncation does not reconcile this particular difference. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Tobacco never,n/N(%) percentage55.5%, and which printed component should be used when the cell is reconciled?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 1 Tobacco use — Never, H cell (p. 5). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=5>)
- Printed inputs: H cell 549/987 (55.5%); the row prints No./total No. (%) or inherits that explicit parent label.
- Registered comparator/rule: Printed percentage 55.5% versus the same cell's exact fraction 549/987. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.
- Reproduced calculation: 100 × 549/987 = 55.623100304%; nearest one-decimal = 55.6%; printed = 55.5%; absolute gap = 0.123100304 percentage point. One-decimal truncation gives 55.6%, and does not reproduce this display.
- Determining fact/state: The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the H-group Tobacco use — Never percentage 55.5%, and which count/population definition should be used for extraction?
- Alternative and direct-versus-inferred boundary: The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

## C010 — Tobacco never,n/N(%), low group

**Candidate statement:** Tobacco never,n/N(%), low group; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/numeric_consistency.md :: NB-PCT-B37-L

- Relationship: N065; mapped B37. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Tobacco never,n/N(%), L cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 525/985 (53.2%); explicit denominator 985.
- Reproducible rule/calculation: patient percentage=100×n/N;100×525/985=53.299492386%, which rounds to53.3% under nearest-one-decimal rounding. Printed53.2% differs by0.099492386 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the low-group Tobacco never,n/N(%) percentage53.2%, and which printed component should be used when the cell is reconciled?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 1 Tobacco use — Never, L cell (p. 5). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=5>)
- Printed inputs: L cell 525/985 (53.2%); the row prints No./total No. (%) or inherits that explicit parent label.
- Registered comparator/rule: Printed percentage 53.2% versus the same cell's exact fraction 525/985. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.
- Reproduced calculation: 100 × 525/985 = 53.299492386%; nearest one-decimal = 53.3%; printed = 53.2%; absolute gap = 0.099492386 percentage point. One-decimal truncation gives 53.2%, reproducing this display.
- Determining fact/state: The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the L-group Tobacco use — Never percentage 53.2%, and which count/population definition should be used for extraction?
- Alternative and direct-versus-inferred boundary: The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

## C011 — Tobacco previous,n/N(%), high group

**Candidate statement:** Tobacco previous,n/N(%), high group; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/numeric_consistency.md :: NB-PCT-B38-H

- Relationship: N066; mapped B38. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Tobacco previous,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 273/987 (27.6%); explicit denominator 987.
- Reproducible rule/calculation: patient percentage=100×n/N;100×273/987=27.659574468%, which rounds to27.7% under nearest-one-decimal rounding. Printed27.6% differs by0.059574468 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Tobacco previous,n/N(%) percentage27.6%, and which printed component should be used when the cell is reconciled?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 1 Tobacco use — Previous, H cell (p. 5). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=5>)
- Printed inputs: H cell 273/987 (27.6%); the row prints No./total No. (%) or inherits that explicit parent label.
- Registered comparator/rule: Printed percentage 27.6% versus the same cell's exact fraction 273/987. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.
- Reproduced calculation: 100 × 273/987 = 27.659574468%; nearest one-decimal = 27.7%; printed = 27.6%; absolute gap = 0.059574468 percentage point. One-decimal truncation gives 27.6%, reproducing this display.
- Determining fact/state: The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the H-group Tobacco use — Previous percentage 27.6%, and which count/population definition should be used for extraction?
- Alternative and direct-versus-inferred boundary: The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

## C012 — Tobacco current,n/N(%), low group

**Candidate statement:** Tobacco current,n/N(%), low group; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/numeric_consistency.md :: NB-PCT-B39-L

- Relationship: N067; mapped B39. Compared locations and roles: REPORT [main PDF p.5](../../../jama_bluth_2019_oi_190055_16092.pdf#page=5), Table1 Tobacco current,n/N(%), L cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 186/985 (18.8%); explicit denominator 985.
- Reproducible rule/calculation: patient percentage=100×n/N;100×186/985=18.883248731%, which rounds to18.9% under nearest-one-decimal rounding. Printed18.8% differs by0.083248731 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Truncation to one decimal reproduces this particular displayed percentage; no truncation rule is stated, and other rows round upwards. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the low-group Tobacco current,n/N(%) percentage18.8%, and which printed component should be used when the cell is reconciled?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 1 Tobacco use — Current, L cell (p. 5). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 5](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=5>)
- Printed inputs: L cell 186/985 (18.8%); the row prints No./total No. (%) or inherits that explicit parent label.
- Registered comparator/rule: Printed percentage 18.8% versus the same cell's exact fraction 186/985. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.
- Reproduced calculation: 100 × 186/985 = 18.883248731%; nearest one-decimal = 18.9%; printed = 18.8%; absolute gap = 0.083248731 percentage point. One-decimal truncation gives 18.8%, reproducing this display.
- Determining fact/state: The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the L-group Tobacco use — Current percentage 18.8%, and which count/population definition should be used for extraction?
- Alternative and direct-versus-inferred boundary: The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

## C013 — Antibiotic prophylaxis,n/N(%), high group

**Candidate statement:** Antibiotic prophylaxis,n/N(%), high group; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/numeric_consistency.md :: NB-PCT-B63-H

- Relationship: N091; mapped B63. Compared locations and roles: REPORT [main PDF p.6](../../../jama_bluth_2019_oi_190055_16092.pdf#page=6), Table1 Antibiotic prophylaxis,n/N(%), H cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 938/987 (94.8%); explicit denominator 987.
- Reproducible rule/calculation: patient percentage=100×n/N;100×938/987=95.035460993%, which rounds to95.0% under nearest-one-decimal rounding. Printed94.8% differs by0.235460993 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Simple truncation does not reconcile this particular difference. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the high-group Antibiotic prophylaxis,n/N(%) percentage94.8%, and which printed component should be used when the cell is reconciled?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 1 Antibiotic prophylaxis, H cell (p. 6). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 6](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=6>)
- Printed inputs: H cell 938/987 (94.8%); the row prints No./total No. (%) or inherits that explicit parent label.
- Registered comparator/rule: Printed percentage 94.8% versus the same cell's exact fraction 938/987. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.
- Reproduced calculation: 100 × 938/987 = 95.035460993%; nearest one-decimal = 95.0%; printed = 94.8%; absolute gap = 0.235460993 percentage point. One-decimal truncation gives 95.0%, and does not reproduce this display.
- Determining fact/state: The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the H-group Antibiotic prophylaxis percentage 94.8%, and which count/population definition should be used for extraction?
- Alternative and direct-versus-inferred boundary: The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

## C014 — Antibiotic prophylaxis,n/N(%), low group

**Candidate statement:** Antibiotic prophylaxis,n/N(%), low group; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/numeric_consistency.md :: NB-PCT-B63-L

- Relationship: N091; mapped B63. Compared locations and roles: REPORT [main PDF p.6](../../../jama_bluth_2019_oi_190055_16092.pdf#page=6), Table1 Antibiotic prophylaxis,n/N(%), L cell numerator/denominator; REPORT same cell percentage.
- Printed inputs: 949/985 (96.1%); explicit denominator 985.
- Reproducible rule/calculation: patient percentage=100×n/N;100×949/985=96.345177665%, which rounds to96.3% under nearest-one-decimal rounding. Printed96.1% differs by0.245177665 percentage point.
- Tolerance:±0.05 percentage point for nearest one-decimal display; difference exceeds it. Numerator and denominator are exact integers.
- Direct observation versus inference: cell values are directly printed and arithmetic is reproduced. A transcription error or denominator reuse mechanism is an inference, not established.
- Alternatives: An incorrectly displayed numerator or denominator, a percentage based on another population, or a different rounding convention could account for the difference. Simple truncation does not reconcile this particular difference. Do not infer a final corrected cell.
- Quality-control relevance: an extracted percentage and its printed count/population would represent different numerical summaries; a small display defect can propagate into baseline extraction without implying a change to conclusions.
- Exact human question: What denominator and rounding rule generated the low-group Antibiotic prophylaxis,n/N(%) percentage96.1%, and which printed component should be used when the cell is reconciled?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 1 Antibiotic prophylaxis, L cell (p. 6). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 6](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=6>)
- Printed inputs: L cell 949/985 (96.1%); the row prints No./total No. (%) or inherits that explicit parent label.
- Registered comparator/rule: Printed percentage 96.1% versus the same cell's exact fraction 949/985. Percentage identity 100 × printed numerator / printed denominator, followed by nearest one-decimal rounding (±0.05 percentage point). This tests the displayed n/N (%) cell; the actual production/display rule is not explicitly stated.
- Reproduced calculation: 100 × 949/985 = 96.345177665%; nearest one-decimal = 96.3%; printed = 96.1%; absolute gap = 0.245177665 percentage point. One-decimal truncation gives 96.3%, and does not reproduce this display.
- Determining fact/state: The exact printed n/N and percentage match the registration; the nearest-rounding mismatch reproduces and remains conditional on the named display rule. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Necessary fraction and printed percentage are available. Missing: actual rounding/truncation rule and whether any printed component uses a different population; no alternative denominator is assigned. What exact observed denominator and display rule generated the L-group Antibiotic prophylaxis percentage 96.1%, and which count/population definition should be used for extraction?
- Alternative and direct-versus-inferred boundary: The actual display might truncate rather than round, or the percentage might use a different population. Other explicit n/N rows round upward (for example reflux low 343/986 →34.8%), so a universal truncation convention is not supplied. Printed denominator/numerator reuse remains an inferred mechanism. Direct: all three components of the cell. Derived: division and nearest-rounding gap. Inferred: production/transcription cause; none is established.

## C015 — Monitoring displayed percentages versus absolute difference

**Candidate statement:** Monitoring displayed percentages versus absolute difference; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Numeric or arithmetic inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/statistical_pass_1.md :: DEN-T45

- Relationship IDs: S038.
- Candidate category: Denominator, proportion, or total inconsistency.
- Source printed evidence: H632/982(64.9%); L651/984(67.7%); difference−1.8(−6.0 to2.4), P.40.
- Compared locations/roles: REPORT [DOC-001 PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8) same Table2 row printed n/N versus REPORT [DOC-001 PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8) attached percentages; REPORT [DOC-001 PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8) difference column is a linked comparator. REPORT [DOC-001 PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8) preceding neuromuscular blockade counts974/961 corroborate a possible different denominator.
- Reproducible comparison: 100×632/982=64.358452%; 100×651/984=66.158537%. These do not produce attached 64.9%/67.7%. Using blockade denominators instead gives100×632/974=64.887064% and100×651/961=67.741935%, which round to the attached percentages. The printed fractions imply H−L=-1.800084 percentage points, compatible in precision with −1.8; the displayed percentages imply−2.8 percentage points.
- Direct versus diagnostic: fractions, percentages and difference are direct; fraction division is direct arithmetic. The alternative denominator974/961 is a diagnostic source-linked explanation, not an assigned replacement. P and CI are not recomputed because their row-population/test convention is unreported.
- Source-grounded alternatives/missing definition: percentages may use participants with blockade while fractions/difference use another evaluable population. That mixed denominator mapping is not explained by the printed n/N label or the monitoring footnote, which defines included monitoring methods only.
- Exact human question: Which denominator defines each row's percentage, absolute difference/interval and P, and which population should the printed n/N denote?
- Mechanical handoff: exact source page/label/value confirmation and any missing estimand/population/rounding definition remain for the fresh evidence-recheck stage. Pending Human Adjudication; no correction or current scientific disposition assigned.
- Registered comparator: subtraction of the two PRINTED percentages against the printed absolute difference. This is distinct from each n/N-to-percentage cell and the NUM exact-count RD comparison. 64.9−67.7=−2.8 pp versus −1.8 pp; difference 1.0 pp exceeds 0.15 pp joint rounding tolerance.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 2 Monitoring of neuromuscular function row, percentages and Absolute Difference column (p. 8); neighboring Neuromuscular blockade row and footnote d as context. [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>)
- Printed inputs: H 632/982 (64.9%); L 651/984 (67.7%); absolute difference -1.8 (−6.0 to 2.4), P=.40. Parent blockade counts H974/L961.
- Registered comparator/rule: Registered comparator: subtraction of the PRINTED percentages 64.9−67.7 versus reported absolute difference -1.8. For the same reported proportions and H-minus-L contrast, the absolute difference should agree with percentage subtraction within 0.15 percentage point joint rounding tolerance. Different populations/estimands can break the identity and must be named.
- Reproduced calculation: 64.9 − 67.7 = -2.8 percentage points; printed difference -1.8; gap 1.0 percentage points. Exact printed fractions give 100 × (632/982 − 651/984) = -1.800084 percentage points. Parent-population percentages 100 × 632/974 = 64.887064% and 100 × 651/961 = 67.741935% round to the attached percentages. The exact fraction difference rounds to −1.8.
- Determining fact/state: The registered PRINTED-percentage subtraction comparator reproduces beyond joint display tolerance; the required common-population definition remains unresolved. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Percentages, printed n/N, difference and neighboring counts are available. Missing: whether percentages and absolute difference use the same population/estimand; actual display rule and denominators for inference. For monitoring, which population and estimand define each displayed percentage and the absolute difference/CI/P, and are those quantities intended to be directly comparable?
- Alternative and direct-versus-inferred boundary: The percentages can use the blockade population while the fraction/difference uses another evaluable population. Neighboring counts support that arithmetic explanation, but source footnote d defines included monitoring methods only and does not define the denominator mapping. Direct: the same-row percentages, fractions, signed difference and parent counts. Derived: subtraction/division. Inferred: parent-denominator reuse or mixed populations; no production mechanism is asserted.

## C016 — Reversal displayed percentage direction versus absolute difference

**Candidate statement:** Reversal displayed percentage direction versus absolute difference; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Numeric or arithmetic inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/statistical_pass_1.md :: DEN-T46

- Relationship IDs: S039.
- Candidate category: Denominator, proportion, or total inconsistency.
- Source printed evidence: H724/982(74.3%); L723/984(75.2%); difference+0.2(−3.6 to4.1), P.90.
- Compared locations/roles: REPORT [DOC-001 PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8) same Table2 row printed n/N versus REPORT [DOC-001 PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8) attached percentages; REPORT [DOC-001 PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8) difference column is a linked comparator. REPORT [DOC-001 PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8) preceding neuromuscular blockade counts974/961 corroborate a possible different denominator.
- Reproducible comparison: 100×724/982=73.727088%; 100×723/984=73.475610%. These do not produce attached 74.3%/75.2%. Using blockade denominators instead gives100×724/974=74.332649% and100×723/961=75.234131%, which round to the attached percentages. The printed fractions imply H−L=0.251478 percentage points, compatible in precision with +0.2; the displayed percentages imply−0.9 percentage points, opposite to the reported+0.2 direction.
- Direct versus diagnostic: fractions, percentages and difference are direct; fraction division is direct arithmetic. The alternative denominator974/961 is a diagnostic source-linked explanation, not an assigned replacement. P and CI are not recomputed because their row-population/test convention is unreported.
- Source-grounded alternatives/missing definition: percentages may use participants with blockade while fractions/difference use another evaluable population. That mixed denominator mapping is not explained by the printed n/N label or the monitoring footnote, which defines included monitoring methods only.
- Exact human question: Which denominator defines each row's percentage, absolute difference/interval and P, and which population should the printed n/N denote?
- Mechanical handoff: exact source page/label/value confirmation and any missing estimand/population/rounding definition remain for the fresh evidence-recheck stage. Pending Human Adjudication; no correction or current scientific disposition assigned.
- Registered comparator: subtraction of the two PRINTED percentages against the printed absolute difference. This is distinct from each n/N-to-percentage cell and the NUM exact-count RD comparison. 74.3−75.2=−0.9 pp versus +0.2 pp; opposite signs and 1.1 pp gap exceed 0.15 pp joint rounding tolerance.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 2 Reversal row, percentages and Absolute Difference column (p. 8); neighboring Neuromuscular blockade row and footnote d as context. [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>)
- Printed inputs: H 724/982 (74.3%); L 723/984 (75.2%); absolute difference 0.2 (−3.6 to 4.1), P=.90. Parent blockade counts H974/L961.
- Registered comparator/rule: Registered comparator: subtraction of the PRINTED percentages 74.3−75.2 versus reported absolute difference 0.2. For the same reported proportions and H-minus-L contrast, the absolute difference should agree with percentage subtraction within 0.15 percentage point joint rounding tolerance. Different populations/estimands can break the identity and must be named.
- Reproduced calculation: 74.3 − 75.2 = -0.9 percentage points; printed difference 0.2; gap 1.1 percentage points, with opposite signs. Exact printed fractions give 100 × (724/982 − 723/984) = 0.251478 percentage points. Parent-population percentages 100 × 724/974 = 74.332649% and 100 × 723/961 = 75.234131% round to the attached percentages. The exact fraction difference rounds to +0.3, so the registration's separate statement that it is compatible with +0.2 under nearest rounding is not reproduced; C025 owns that comparator.
- Determining fact/state: The registered PRINTED-percentage subtraction comparator reproduces beyond joint display tolerance; the required common-population definition remains unresolved. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Percentages, printed n/N, difference and neighboring counts are available. Missing: whether percentages and absolute difference use the same population/estimand; actual display rule and denominators for inference. For reversal, which population and estimand define each displayed percentage and the absolute difference/CI/P, and are those quantities intended to be directly comparable?
- Alternative and direct-versus-inferred boundary: The percentages can use the blockade population while the fraction/difference uses another evaluable population. Neighboring counts support that arithmetic explanation, but source footnote d defines included monitoring methods only and does not define the denominator mapping. Direct: the same-row percentages, fractions, signed difference and parent counts. Derived: subtraction/division. Inferred: parent-denominator reuse or mixed populations; no production mechanism is asserted.

## C017 — Any recruitment,No.(%): absolute difference versus exact printed risks

**Candidate statement:** Any recruitment,No.(%): absolute difference versus exact printed risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Numeric or arithmetic inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-T07-RD

- **Numeric relationships:** N127.
- **Compared locations and content roles:** REPORT [PDF p. 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), T07 H/L counts, explicit denominators or H989/L987 headers; REPORT [PDF p. 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), same row Absolute Difference (95% CI) cell.
- **Printed inputs:** H 972(98.3); L 11(1.1); difference 97.1(96.1 to98.2). Complete source-row components: Any recruitment,No.(%); 972(98.3); 11(1.1); 97.1(96.1 to98.2); <.001.
- **Reproducible rule and calculation:** 100*(972/989−11/987)=97.166604 pp; printed 97.1 pp; discrepancy=-0.066604 pp; nearest one-decimal value=97.2 pp. Displayed percentage subtraction=97.200000 pp.
- **Tolerance:** 0.05 percentage point for an exact count-defined risk difference. The looser0.15 bound applies only when subtracting two already rounded percentages and does not alter the exact integer-count calculation.
- **Direct observation versus inference:** Direct: the two event cells and signed difference are in the same row. Derived: the printed count/denominator risks give a different nearest one-decimal effect. Comparator is H−L, consistent with the surrounding signed differences.
- **Source-grounded alternatives:** Truncation toward zero can reproduce several small boundary discrepancies. Model-based/adjusted absolute differences or a different denominator could also explain them; a row-specific computation/display rule is not supplied. These possibilities are the human question, not assumed corrections.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Any recruitment,No.(%), was the absolute difference 97.1 calculated from the printed exact risks and then truncated, or from a different estimand/denominator? What computation and display rule should be used when extracting this result?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 2 Received alveolar recruitment maneuvers row and H989/L987 headers (p. 7); any-recruitment definition footnote b (p. 8). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 7](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=7>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>)
- Printed inputs: H972 (98.3%), L11 (1.1%); headers H989/L987; difference97.1 (96.1 to98.2), P<.001.
- Registered comparator/rule: Reported absolute difference97.1 versus count/header-defined H-minus-L risk difference. Conditional identity of count/header-defined risk difference with the displayed difference under nearest one-decimal rounding. Group-header denominators and an unadjusted effect are required; actual computation/display convention is unnamed.
- Reproduced calculation: 100 × (972/989 − 11/987) = 97.166603664 percentage points, nearest97.2; printed97.1; gap 0.066603664 exceeds0.05. Subtracting already-rounded98.3−1.1=97.2 yields a0.1 gap, within the separate0.15 joint-rounding bound. Truncation of the exact calculation yields97.1.
- Determining fact/state: The named count/header nearest-rounding comparator reproduces the small registered gap; the actual computation/display rule remains the registered missing definition. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Displayed counts, group headers and difference available. Missing: exact procedure-row analysis denominators, whether the effect is a raw risk difference, and its display rule. Was recruitment difference97.1 calculated from972/989 and11/987 then truncated, or from different denominators/estimand? Which computation/display rule defines this reported difference?
- Alternative and direct-versus-inferred boundary: Truncation reproduces97.1; a different complete-case denominator or effect estimator could also explain it. The displayed-count diagnostic does not determine which explanation applies. Direct: counts/header/difference and any-recruitment definition. Derived: exact arithmetic and rounding. Inferred: truncation or other computation; no fitted quantity is replaced.

## C018 — Heat rate label versus beats-per-minute measurements

**Candidate statement:** Heat rate label versus beats-per-minute measurements; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-T30-LABEL; checkers/statistical_pass_1.md :: LABEL-T30-T32

- **Numeric relationships:** N150, N151, N152.
- **Compared locations and content roles:** REPORT [PDF p. 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), Table 2 heading and T30–T32 numeric rows; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnote k heart-rate definition.
- **Printed inputs:** Table 2 row heading Heat rate, mean(SD),beats/min; H/L after intubation76.5(15.8)/76.0(14.3), first hour72.6(13.4)/73.1(14.0), last hour73.5(13.0)/74.9(13.8).. Complete source-row components: Printed “Heat rate”/intubation,beats/min; 76.5(15.8); 76.0(14.3); 0.6(−0.7 to1.9); .38 / Printed “Heat rate”/first hour; 72.6(13.4); 73.1(14.0); −0.6(−1.8 to0.6); .36 / Printed “Heat rate”/last hour; 73.5(13.0); 74.9(13.8); −1.4(−2.6 to−0.2); .02.
- **Reproducible rule and calculation:** A beat count per minute is a cardiac rate measurement; the printed label Heat rate denotes a different physical quantity and is incompatible with beats/min. The same article explicitly calls bradycardia a heart rate measurement in beats/min.
- **Tolerance:** Exact label/unit identity; no rounding tolerance. No numerical value is re-estimated.
- **Direct observation versus inference:** Direct: the Table 2 heading spells Heat rate, and its unit is beats/min. The Table 3 bradycardia definition explicitly says heart rate less than50beats/min. Inference: the missing r is plausibly a typographic error, not a new heat measurement.
- **Source-grounded alternatives:** Readers can infer the intended heart-rate quantity from units/context. This is a bounded measure-label proofreading candidate, not an additional physiologic numerical discrepancy.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Is the Table 2 Heat rate heading intended to read Heart rate, and should all three beats/min rows be indexed under that measurement label?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 2 Heat rate heading and its three rows (p. 7); Table 3 bradycardia footnote k (p. 10). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 7](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=7>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>)
- Printed inputs: Heading Heat rate, mean(SD), beats/min; H/L after intubation76.5(15.8)/76.0(14.3), first hour72.6(13.4)/73.1(14.0), last hour73.5(13.0)/74.9(13.8). Footnote k defines bradycardia as heart rate<50beats/min or relative decrease.
- Registered comparator/rule: Printed Heat rate spelling/unit versus the article's heart-rate definition in beats/min. Measurement-label/unit identity; the physiological rate indexed by beats/min and bradycardia is heart rate.
- Reproduced calculation: No numeric estimate is recomputed. The printed label lacks the r in Heart while accompanying beat/min measurements and bradycardia definition specify heart rate.
- Determining fact/state: Fresh text and current-source rendering confirm Heat rate in the heading; footnote k explicitly states heart rate with the same unit. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; report_internal_inconsistency.
- Missing definition and human question: All label/unit/definition inputs available. Author-intended heading is the remaining confirmation. Is Table 2 Heat rate intended as Heart rate, with all three rows indexed under that measure?
- Alternative and direct-versus-inferred boundary: Readers can recover heart rate from the unit and context. A dropped letter is plausible but is an inferred explanation, not a separate numerical finding. Direct: Heat rate spelling, beats/min, numeric rows and heart rate wording in footnote k. Inferred: missing-letter mechanism.

## C019 — Noninvasive ventilation,No.(%): L printed percentage identity

**Candidate statement:** Noninvasive ventilation,No.(%): L printed percentage identity; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-T38-PCT-L

- **Numeric relationships:** N158.
- **Compared locations and content roles:** REPORT [PDF p. 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), T38 L count/denominator cell and L n987 header; REPORT [PDF p. 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), same cell printed percentage and No./total No. (%) or No. (%) row label.
- **Printed inputs:** L 264/987 (26.8%) using header L n987. Complete source-row components: Noninvasive ventilation,No.(%); 274(27.7); 264(26.8); 0.9(−3.0 to4.9); .64.
- **Reproducible rule and calculation:** 100*264/987=26.747720%; printed 26.8%; discrepancy=0.052280 pp; nearest one-decimal value=26.7%.
- **Tolerance:** 0.05 percentage point inclusive at ties; printed integer numerator/denominator exact. This mismatch crosses that tolerance; no requirement that subcategory percentages sum exactly100 after rounding.
- **Direct observation versus inference:** Direct: source cell/header shows numerator, denominator and percentage. Derived: the printed denominator does not give the printed percentage under nearest rounding.
- **Source-grounded alternatives:** An unstated complete-case/parent denominator, denominator transcription, or truncation/other display convention may explain the mismatch. Source footnotes do not identify a replacement denominator for this cell. Differences close to a rounding boundary remain bounded display questions, not evidence of a changed conclusion.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Which denominator and display rule produced 26.8% for L 264/987 in Noninvasive ventilation,No.(%), and should the printed denominator or percentage be interpreted differently?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 2 Use of noninvasive ventilation, low cell and low-group header (p. 7); completed-analysis complete-case statement (p. 4) as context. [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 7](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=7>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>)
- Printed inputs: Low cell264(26.8%); low-group header n987. The source does not print264/987 in the cell.
- Registered comparator/rule: 26.8% versus264/header987; the registered fraction is explicitly reconstructed using the header, as the original card says. Percentage identity using the displayed group header as the default reference, conditional on987 being the row denominator; nearest one-decimal rounding.
- Reproduced calculation: 100 ×264/987=26.747720365%, nearest26.7%; printed26.8; gap0.052279635 percentage point exceeds0.05 by0.002279635. At denominator986,100 ×264/986=26.774847870%, rounding26.8.
- Determining fact/state: The source confirms264(26.8) and header987; the original record explicitly uses the header rather than claiming an explicit slash denominator. Its conditional header-denominator discrepancy reproduces and remains as registered pending the row denominator. No original transcription or location is disproven, so repaired_residual does not apply. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Count, percentage and header available. Missing: variable-specific complete-case denominator and rounding rule. Table 2 supplies no denominator override for this row; complete-case methods do not identify one. What exact denominator and display rule produced26.8% for264 noninvasive-ventilation users, and is the printed header987 intended as this row's reference population?
- Alternative and direct-versus-inferred boundary: An unreported row denominator986 would reconcile nearest rounding. It is an arithmetic possibility, not a supplied observed denominator; no production method is inferred. Direct:264(26.8) and header987. Derived: header-denominator diagnostic. Inferred: row-specific986 or alternate display; neither is asserted as actual.

## C020 — Noninvasive ventilation,No.(%): absolute difference versus exact printed risks

**Candidate statement:** Noninvasive ventilation,No.(%): absolute difference versus exact printed risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Numeric or arithmetic inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-T38-RD

- **Numeric relationships:** N158.
- **Compared locations and content roles:** REPORT [PDF p. 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), T38 H/L counts, explicit denominators or H989/L987 headers; REPORT [PDF p. 7](../../../jama_bluth_2019_oi_190055_16092.pdf#page=7), same row Absolute Difference (95% CI) cell.
- **Printed inputs:** H 274(27.7); L 264(26.8); difference 0.9(−3.0 to4.9). Complete source-row components: Noninvasive ventilation,No.(%); 274(27.7); 264(26.8); 0.9(−3.0 to4.9); .64.
- **Reproducible rule and calculation:** 100*(274/989−264/987)=0.957032 pp; printed 0.9 pp; discrepancy=-0.057032 pp; nearest one-decimal value=1.0 pp. Displayed percentage subtraction=0.900000 pp.
- **Tolerance:** 0.05 percentage point for an exact count-defined risk difference. The looser0.15 bound applies only when subtracting two already rounded percentages and does not alter the exact integer-count calculation.
- **Direct observation versus inference:** Direct: the two event cells and signed difference are in the same row. Derived: the printed count/denominator risks give a different nearest one-decimal effect. Comparator is H−L, consistent with the surrounding signed differences.
- **Source-grounded alternatives:** Truncation toward zero can reproduce several small boundary discrepancies. Model-based/adjusted absolute differences or a different denominator could also explain them; a row-specific computation/display rule is not supplied. These possibilities are the human question, not assumed corrections.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Noninvasive ventilation,No.(%), was the absolute difference 0.9 calculated from the printed exact risks and then truncated, or from a different estimand/denominator? What computation and display rule should be used when extracting this result?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 2 Use of noninvasive ventilation row and headers (p. 7); complete-case analysis statement (p. 4). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 7](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=7>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>)
- Printed inputs: H274(27.7%), L264(26.8%); headers989/987; difference0.9(−3.0 to4.9), P.64.
- Registered comparator/rule: 0.9 versus raw H-minus-L count/header-defined risk difference. Conditional raw risk-difference identity with nearest one-decimal display; group-header denominators and raw-difference estimator must apply.
- Reproduced calculation: 100 × (274/989−264/987)=0.957031910 percentage points; nearest1.0; printed0.9; gap0.057031910 exceeds0.05. Printed27.7−26.8=0.9 agrees exactly with the reported difference. Truncation of the exact count/header calculation yields0.9.
- Determining fact/state: The registered exact count/header nearest-rounding gap reproduces; a different displayed-percentage comparator reconciles, and actual computation remains unspecified. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Counts, header populations and difference available. Missing: exact row-specific analysis populations and raw-versus-other difference/display convention. Was0.9 computed from exact274/989 and264/987 risks, from rounded percentages, or from another population/estimand; what display rule applies?
- Alternative and direct-versus-inferred boundary: Subtraction of displayed percentages, truncation of raw risks, or another complete-case population could produce0.9. The printed-percentage subtraction is coherent and does not disprove the separate exact count/header rounding comparison. Direct: row counts, percentages, headers and signed difference. Derived: exact arithmetic. Inferred: display/analysis mechanism; none is assigned.

## C021 — Monitoring neuromuscular function,n/N(%): H printed percentage identity

**Candidate statement:** Monitoring neuromuscular function,n/N(%): H printed percentage identity; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-T45-PCT-H; checkers/statistical_pass_1.md :: DEN-T45

- **Numeric relationships:** N165.
- **Compared locations and content roles:** REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), T45 H count/denominator cell; REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), same cell printed percentage and No./total No. (%) or No. (%) row label.
- **Printed inputs:** H 632/982 (64.9%). Complete source-row components: Monitoring neuromuscular function,n/N(%); 632/982(64.9); 651/984(67.7); −1.8(−6.0 to2.4); .40.
- **Reproducible rule and calculation:** 100*632/982=64.358452%; printed 64.9%; discrepancy=0.541548 pp; nearest one-decimal value=64.4%.
- **Tolerance:** 0.05 percentage point inclusive at ties; printed integer numerator/denominator exact. This mismatch crosses that tolerance; no requirement that subcategory percentages sum exactly100 after rounding.
- **Direct observation versus inference:** Direct: source cell/header shows numerator, denominator and percentage. Derived: the printed denominator does not give the printed percentage under nearest rounding. The alternate parent blockade denominator is 974; its use would approximately reproduce this percentage, but it is not the denominator printed in the cell.
- **Source-grounded alternatives:** An unstated complete-case/parent denominator, denominator transcription, or truncation/other display convention may explain the mismatch. Source footnotes do not identify a replacement denominator for this cell. Differences close to a rounding boundary remain bounded display questions, not evidence of a changed conclusion.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Which denominator and display rule produced 64.9% for H 632/982 in Monitoring neuromuscular function,n/N(%), and should the printed denominator or percentage be interpreted differently?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 2 Monitoring of neuromuscular function, H No./total No.(%) cell; preceding Neuromuscular blockade row; footnote d (p. 8). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>)
- Printed inputs: H 632/982 (64.9%); neighboring H blockade count974.
- Registered comparator/rule: Same-cell printed64.9% versus exact explicit fraction632/982. 100 × printed n/N identity and nearest one-decimal display (±0.05 percentage point); explicit n/N cell supplies the comparison denominator.
- Reproduced calculation: 100 ×632/982=64.358452138%; nearest64.4%; printed64.9%; gap0.541547862 percentage point. Alternative parent calculation100 ×632/974=64.887063655%, rounding64.9%.
- Determining fact/state: Direct extraction and rendering reproduce explicit n/N and its incompatible attached percentage; the parent-denominator calculation does not change what is printed. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: All explicit cell inputs are available. Missing: actual percent denominator and display rule; whether the percentage intentionally uses the parent blockade population although the slash fraction has a different denominator. Which denominator generated64.9% forH 632/982 inMonitoring of neuromuscular function, and does the n/N cell intentionally combine a different reference population with a parent-blockade percentage?
- Alternative and direct-versus-inferred boundary: The parent blockade count reproduces the percentage under nearest rounding. Source footnote d only defines monitoring methods and does not specify the percent denominator; parent reuse remains diagnostic. Direct: explicit n/N, attached percentage and parent count. Derived: the two division results. Inferred: mixed-denominator generation or transcription; none is asserted.

## C022 — Monitoring neuromuscular function,n/N(%): L printed percentage identity

**Candidate statement:** Monitoring neuromuscular function,n/N(%): L printed percentage identity; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-T45-PCT-L; checkers/statistical_pass_1.md :: DEN-T45

- **Numeric relationships:** N165.
- **Compared locations and content roles:** REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), T45 L count/denominator cell; REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), same cell printed percentage and No./total No. (%) or No. (%) row label.
- **Printed inputs:** L 651/984 (67.7%). Complete source-row components: Monitoring neuromuscular function,n/N(%); 632/982(64.9); 651/984(67.7); −1.8(−6.0 to2.4); .40.
- **Reproducible rule and calculation:** 100*651/984=66.158537%; printed 67.7%; discrepancy=1.541463 pp; nearest one-decimal value=66.2%.
- **Tolerance:** 0.05 percentage point inclusive at ties; printed integer numerator/denominator exact. This mismatch crosses that tolerance; no requirement that subcategory percentages sum exactly100 after rounding.
- **Direct observation versus inference:** Direct: source cell/header shows numerator, denominator and percentage. Derived: the printed denominator does not give the printed percentage under nearest rounding. The alternate parent blockade denominator is 961; its use would approximately reproduce this percentage, but it is not the denominator printed in the cell.
- **Source-grounded alternatives:** An unstated complete-case/parent denominator, denominator transcription, or truncation/other display convention may explain the mismatch. Source footnotes do not identify a replacement denominator for this cell. Differences close to a rounding boundary remain bounded display questions, not evidence of a changed conclusion.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Which denominator and display rule produced 67.7% for L 651/984 in Monitoring neuromuscular function,n/N(%), and should the printed denominator or percentage be interpreted differently?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 2 Monitoring of neuromuscular function, L No./total No.(%) cell; preceding Neuromuscular blockade row; footnote d (p. 8). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>)
- Printed inputs: L 651/984 (67.7%); neighboring L blockade count961.
- Registered comparator/rule: Same-cell printed67.7% versus exact explicit fraction651/984. 100 × printed n/N identity and nearest one-decimal display (±0.05 percentage point); explicit n/N cell supplies the comparison denominator.
- Reproduced calculation: 100 ×651/984=66.158536585%; nearest66.2%; printed67.7%; gap1.541463415 percentage point. Alternative parent calculation100 ×651/961=67.741935484%, rounding67.7%.
- Determining fact/state: Direct extraction and rendering reproduce explicit n/N and its incompatible attached percentage; the parent-denominator calculation does not change what is printed. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: All explicit cell inputs are available. Missing: actual percent denominator and display rule; whether the percentage intentionally uses the parent blockade population although the slash fraction has a different denominator. Which denominator generated67.7% forL 651/984 inMonitoring of neuromuscular function, and does the n/N cell intentionally combine a different reference population with a parent-blockade percentage?
- Alternative and direct-versus-inferred boundary: The parent blockade count reproduces the percentage under nearest rounding. Source footnote d only defines monitoring methods and does not specify the percent denominator; parent reuse remains diagnostic. Direct: explicit n/N, attached percentage and parent count. Derived: the two division results. Inferred: mixed-denominator generation or transcription; none is asserted.

## C023 — Reversal,n/N(%): H printed percentage identity

**Candidate statement:** Reversal,n/N(%): H printed percentage identity; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-T46-PCT-H; checkers/statistical_pass_1.md :: DEN-T46

- **Numeric relationships:** N166.
- **Compared locations and content roles:** REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), T46 H count/denominator cell; REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), same cell printed percentage and No./total No. (%) or No. (%) row label.
- **Printed inputs:** H 724/982 (74.3%). Complete source-row components: Reversal,n/N(%); 724/982(74.3); 723/984(75.2); 0.2(−3.6 to4.1); .90.
- **Reproducible rule and calculation:** 100*724/982=73.727088%; printed 74.3%; discrepancy=0.572912 pp; nearest one-decimal value=73.7%.
- **Tolerance:** 0.05 percentage point inclusive at ties; printed integer numerator/denominator exact. This mismatch crosses that tolerance; no requirement that subcategory percentages sum exactly100 after rounding.
- **Direct observation versus inference:** Direct: source cell/header shows numerator, denominator and percentage. Derived: the printed denominator does not give the printed percentage under nearest rounding. The alternate parent blockade denominator is 974; its use would approximately reproduce this percentage, but it is not the denominator printed in the cell.
- **Source-grounded alternatives:** An unstated complete-case/parent denominator, denominator transcription, or truncation/other display convention may explain the mismatch. Source footnotes do not identify a replacement denominator for this cell. Differences close to a rounding boundary remain bounded display questions, not evidence of a changed conclusion.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Which denominator and display rule produced 74.3% for H 724/982 in Reversal,n/N(%), and should the printed denominator or percentage be interpreted differently?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 2 Reversal, H No./total No.(%) cell; preceding Neuromuscular blockade row; footnote d (p. 8). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>)
- Printed inputs: H 724/982 (74.3%); neighboring H blockade count974.
- Registered comparator/rule: Same-cell printed74.3% versus exact explicit fraction724/982. 100 × printed n/N identity and nearest one-decimal display (±0.05 percentage point); explicit n/N cell supplies the comparison denominator.
- Reproduced calculation: 100 ×724/982=73.727087576%; nearest73.7%; printed74.3%; gap0.572912424 percentage point. Alternative parent calculation100 ×724/974=74.332648871%, rounding74.3%.
- Determining fact/state: Direct extraction and rendering reproduce explicit n/N and its incompatible attached percentage; the parent-denominator calculation does not change what is printed. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: All explicit cell inputs are available. Missing: actual percent denominator and display rule; whether the percentage intentionally uses the parent blockade population although the slash fraction has a different denominator. Which denominator generated74.3% forH 724/982 inReversal, and does the n/N cell intentionally combine a different reference population with a parent-blockade percentage?
- Alternative and direct-versus-inferred boundary: The parent blockade count reproduces the percentage under nearest rounding. Source footnote d only defines monitoring methods and does not specify the percent denominator; parent reuse remains diagnostic. Direct: explicit n/N, attached percentage and parent count. Derived: the two division results. Inferred: mixed-denominator generation or transcription; none is asserted.

## C024 — Reversal,n/N(%): L printed percentage identity

**Candidate statement:** Reversal,n/N(%): L printed percentage identity; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-T46-PCT-L; checkers/statistical_pass_1.md :: DEN-T46

- **Numeric relationships:** N166.
- **Compared locations and content roles:** REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), T46 L count/denominator cell; REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), same cell printed percentage and No./total No. (%) or No. (%) row label.
- **Printed inputs:** L 723/984 (75.2%). Complete source-row components: Reversal,n/N(%); 724/982(74.3); 723/984(75.2); 0.2(−3.6 to4.1); .90.
- **Reproducible rule and calculation:** 100*723/984=73.475610%; printed 75.2%; discrepancy=1.724390 pp; nearest one-decimal value=73.5%.
- **Tolerance:** 0.05 percentage point inclusive at ties; printed integer numerator/denominator exact. This mismatch crosses that tolerance; no requirement that subcategory percentages sum exactly100 after rounding.
- **Direct observation versus inference:** Direct: source cell/header shows numerator, denominator and percentage. Derived: the printed denominator does not give the printed percentage under nearest rounding. The alternate parent blockade denominator is 961; its use would approximately reproduce this percentage, but it is not the denominator printed in the cell.
- **Source-grounded alternatives:** An unstated complete-case/parent denominator, denominator transcription, or truncation/other display convention may explain the mismatch. Source footnotes do not identify a replacement denominator for this cell. Differences close to a rounding boundary remain bounded display questions, not evidence of a changed conclusion.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** Which denominator and display rule produced 75.2% for L 723/984 in Reversal,n/N(%), and should the printed denominator or percentage be interpreted differently?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 2 Reversal, L No./total No.(%) cell; preceding Neuromuscular blockade row; footnote d (p. 8). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>)
- Printed inputs: L 723/984 (75.2%); neighboring L blockade count961.
- Registered comparator/rule: Same-cell printed75.2% versus exact explicit fraction723/984. 100 × printed n/N identity and nearest one-decimal display (±0.05 percentage point); explicit n/N cell supplies the comparison denominator.
- Reproduced calculation: 100 ×723/984=73.475609756%; nearest73.5%; printed75.2%; gap1.724390244 percentage point. Alternative parent calculation100 ×723/961=75.234131113%, rounding75.2%.
- Determining fact/state: Direct extraction and rendering reproduce explicit n/N and its incompatible attached percentage; the parent-denominator calculation does not change what is printed. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: All explicit cell inputs are available. Missing: actual percent denominator and display rule; whether the percentage intentionally uses the parent blockade population although the slash fraction has a different denominator. Which denominator generated75.2% forL 723/984 inReversal, and does the n/N cell intentionally combine a different reference population with a parent-blockade percentage?
- Alternative and direct-versus-inferred boundary: The parent blockade count reproduces the percentage under nearest rounding. Source footnote d only defines monitoring methods and does not specify the percent denominator; parent reuse remains diagnostic. Direct: explicit n/N, attached percentage and parent count. Derived: the two division results. Inferred: mixed-denominator generation or transcription; none is asserted.

## C025 — Reversal,n/N(%): absolute difference versus exact printed risks

**Candidate statement:** Reversal,n/N(%): absolute difference versus exact printed risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Numeric or arithmetic inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-T46-RD; checkers/statistical_pass_1.md :: DEN-T46

- **Numeric relationships:** N166.
- **Compared locations and content roles:** REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), T46 H/L counts, explicit denominators or H989/L987 headers; REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), same row Absolute Difference (95% CI) cell.
- **Printed inputs:** H 724/982(74.3); L 723/984(75.2); difference 0.2(−3.6 to4.1). Complete source-row components: Reversal,n/N(%); 724/982(74.3); 723/984(75.2); 0.2(−3.6 to4.1); .90.
- **Reproducible rule and calculation:** 100*(724/982−723/984)=0.251478 pp; printed 0.2 pp; discrepancy=-0.051478 pp; nearest one-decimal value=0.3 pp. Displayed percentage subtraction=-0.900000 pp. It is negative while the reported difference is positive; the count-defined difference itself is positive.
- **Tolerance:** 0.05 percentage point for an exact count-defined risk difference. The looser0.15 bound applies only when subtracting two already rounded percentages and does not alter the exact integer-count calculation.
- **Direct observation versus inference:** Direct: the two event cells and signed difference are in the same row. Derived: the printed count/denominator risks give a different nearest one-decimal effect. Comparator is H−L, consistent with the surrounding signed differences.
- **Source-grounded alternatives:** Truncation toward zero can reproduce several small boundary discrepancies. Model-based/adjusted absolute differences or a different denominator could also explain them; a row-specific computation/display rule is not supplied. These possibilities are the human question, not assumed corrections.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** For Reversal,n/N(%), was the absolute difference 0.2 calculated from the printed exact risks and then truncated, or from a different estimand/denominator? What computation and display rule should be used when extracting this result?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 2 Reversal H/L explicit n/N cells and Absolute Difference column (p. 8). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>)
- Printed inputs: H724/982(74.3%); L723/984(75.2%); difference+0.2(−3.6 to4.1), P.90.
- Registered comparator/rule: +0.2 versus difference of the two exact printed fractions. H-minus-L raw risk difference, nearest one-decimal display (±0.05 percentage point), conditional on that being the difference estimand. Explicit slash denominators, rather than overall headers, define this arithmetic comparator.
- Reproduced calculation: 100 ×(724/982−723/984)=0.251477820 percentage points; nearest+0.3; printed+0.2; gap0.051477820 exceeds0.05 by0.001477820. Truncation yields+0.2. The printed-percentage difference74.3−75.2=−0.9 is the separate C016 comparator.
- Determining fact/state: The exact fraction comparison reproduces the registered small nearest-rounding gap; the separate registration statement calling it nearest-rounding compatible is not sustained. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; statistical_results.
- Missing definition and human question: Exact fractions and effect available. Missing: row effect estimand and display/truncation rule. Was reversal difference+0.2 calculated from724/982 and723/984 then truncated, or from another effect/population; what computation and display rule defines it?
- Alternative and direct-versus-inferred boundary: Truncation toward zero reconciles the exact count-defined difference; an estimator with different denominators could also yield0.2. Neither mechanism is source-stated. Direct: exact fractions and+0.2. Derived: risk difference and nearest-rounding boundary. Inferred: actual truncation or alternative estimator.

## C026 — Total fluids: difference estimand accompanying median summaries

**Candidate statement:** Total fluids: difference estimand accompanying median summaries; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** report_internal_inconsistency
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** The comparison aligns a generic effect cell to median subtraction without source support; no literal median-difference claim exists, and the residual cannot be settled without the estimand.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-T47-ESTIMAND

- **Numeric relationships:** N167.
- **Compared locations and content roles:** REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), Table 2 Total fluids median(IQR), L H/L cells; REPORT [PDF p. 8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), same row Absolute Difference cell and Table 2 footnotes.
- **Printed inputs:** H median1.5L (IQR1.0–2.5); L median1.6L (IQR1.0–2.5); Absolute Difference+0.02L (95%CI−0.11 to0.14),P=.79. Complete source-row components: Total fluid,median(IQR),L; 1.5(1.0 to2.5); 1.6(1.0 to2.5); 0.02(−0.11 to0.14); .79.
- **Reproducible rule and calculation:** If the difference column subtracts the displayed central statistic, medianH−medianL=1.5−1.6=−0.10L. One-decimal rounded medians permit true median difference from−0.20 to0.00L; the two-decimal+0.02 permits0.015 to0.025L. Those ranges do not overlap.
- **Tolerance:** 0.05L for each one-decimal median and0.005L for the two-decimal difference. Applicability is explicitly conditional on a median-difference estimand.
- **Direct observation versus inference:** Direct: median/IQR labels accompany a positive absolute-difference point estimate. Derived diagnostic: it is incompatible with a literal difference of those medians under rounding. No Table 2 footnote defines whether this effect is a mean difference, rank-based shift, or median difference.
- **Source-grounded alternatives:** A mean difference or rank-based location shift can legitimately coexist with differently signed group median subtraction. This candidate is the concrete displayed estimand/summary mismatch requiring its rule to be named; it does not assert that a difference of medians was actually estimated.
- **Quality-control relevance:** The printed comparator or measurement label can be copied into downstream evidence extraction; recording the exact rule/definition prevents propagation. This does not establish a changed paper conclusion.
- **Exact human question:** What estimand and calculation produced+0.02L for total fluids: mean difference, rank-based location shift, or difference of medians? How should the absolute-difference column be interpreted alongside the two reported medians?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 2 Total fluids median(IQR),L and Absolute Difference cell; full Table 2 footnotes (p. 8); Statistical Analysis (p. 4) as context. [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>)
- Printed inputs: Medians H1.5L (IQR1.0–2.5), L1.6L (IQR1.0–2.5); Absolute Difference+0.02L (95%CI−0.11 to0.14), P.79. Column/footnotes do not say difference of medians.
- Registered comparator/rule: Registered subtraction of displayed medians1.5−1.6 versus+0.02, conditional on an assumed median-difference estimand. Subtracting medians is applicable only if the effect is a difference of group medians. The source does not supply that alignment; an absolute difference can instead target a mean or other location contrast.
- Reproduced calculation: Median subtraction gives−0.10L. Nearest-rounding bins for1.5 and1.6 permit a true median difference in approximately(−0.20,0.00)L; the+0.02 effect bin is[0.015,0.025)L. These do not overlap IF the effect is a median difference. This cannot test a mean or rank-shift contrast.
- Determining fact/state: The comparison aligns a generic effect cell to median subtraction without source support; no literal median-difference claim exists, and the residual cannot be settled without the estimand. Evidence state record_input_error.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; report_internal_inconsistency.
- Missing definition and human question: Printed medians and effect available; necessary missing input is the total-fluids effect estimand and procedure. Group means/distributions or rank-shift inputs are absent, so an alternative effect cannot be reconstructed. What estimand and procedure generated+0.02L for total fluids, and is it intended as a mean difference, rank-based shift, or difference of medians?
- Alternative and direct-versus-inferred boundary: A mean difference or rank-based shift can coexist with opposite-signed displayed median subtraction. Neither the Table 2 footnotes nor the main statistical description assigns total-fluids effects a median-difference meaning. Direct: median/IQR labels and generic Absolute Difference header. Derived: conditional median arithmetic. Unsupported inference: that the effect must subtract those medians; this is not stated.

## C027 — Primary PPC within5days: labeled RR versus printed patient risks

**Candidate statement:** Primary PPC within5days: labeled RR versus printed patient risks; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT main article versus REPORT main article
**Review domain:** report_internal_inconsistency
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** All discrepancy locations are in the main trial REPORT, including its completed-analysis methods and results footnotes. Primary type and all relationships remain S_W. No PLAN or other REPORT document supplies a substantive conflicting comparator; corroboration does not add a relationship. Precedence P_R > P_P > S_C > S_W therefore leaves S_W.
**Classification ambiguity:** None for document role or relationship type; bounded computation/population/display questions are recorded in the evidence card.
**Checker provenance:** checkers/parts/numeric_outcomes.md :: NUM-O01-RR; checkers/parts/numeric_outcomes.md :: NUM-F11-RR; checkers/numeric_consistency.md :: NB-RR-PPC; checkers/statistical_pass_1.md :: RR-O01; checkers/cross_source_consistency.md :: XR01; checkers/cross_source_consistency.md :: XR44

- **Numeric relationships:** N180.
- **Compared locations and content roles:** REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), O01 row event cells and H/L population headers; REPORT [PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), same row RR label/point/interval; REPORT [PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), Table 3 footnotes a/b.
- **Printed inputs:** H 211/989; L 233/987; printed RR0.93(0.83 to1.04). Complete source-row components: Primary PPC within5days; 211(21.3); 233(23.6); −2.3(−5.9 to1.4); RR0.93(0.83 to1.04); .23.
- **Reproducible rule and calculation:** RR of PPC or the named binary event for H relative to L = (H events/H patients)/(L events/L patients). (211/989)/(233/987) = 0.903748; printed point = 0.93. Nearest two-decimal identity display would be 0.90; discrepancy=0.026252.
- **Tolerance:** 0.005 at the two-decimal point-estimate scale; integer event counts and denominators exact. CI/P checks belong to statistical relationships, not used to reconstruct or replace a risk estimate here.
- **Exact human question:** For Primary PPC within5days, what exact event orientation, reference group, denominator and point-estimate estimator produced 0.93, and is this value intended as the H/L event risk ratio from 211/989 and 233/987 or a differently defined model quantity?
- Direct versus diagnostic: inputs and RR label are printed; crude RR is derived and does not substitute a fitted estimate.
- Alternatives: adjusted/standardized RR, different event/reference coding, zero-cell correction, or truncation could explain the result. No row-specific estimator is supplied. Wald interval approximation alone does not redefine a point risk ratio.
Additional matched report locations and inputs from NB-RR-PPC:
- Printed inputs:H211/989,L233/987;RR0.93.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Locations: Table 3 Primary postoperative pulmonary complications within five days row, No.of Events(%), H989/L987 headers and Risk Ratio column (p. 9); footnotes a/b (p. 10); completed-analysis RR statement (p. 4); abstract RESULTS(p. 1), Primary Outcome narrative(p. 8), Figure 2 All patients row(p. 10). [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 1](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=1>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 4](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=4>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 8](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=8>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 9](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=9>); [jama_bluth_2019_oi_190055_16092.pdf — PDF p. 10](<../../../jama_bluth_2019_oi_190055_16092.pdf#page=10>)
- Printed inputs: H events211; L events233; reference populations H989/L987; printed RR0.93 (95%CI0.83 to1.04). Footnote a: number of reference patients unless otherwise indicated. Footnote b: data are risk ratios unless otherwise indicated; RRs/CIs calculated using the Wald likelihood ratio approximation test.
- Registered comparator/rule: Printed outcome risk-ratio label/point0.93 versus same-row H/L event-risk ratio(211/989)/(233/987). For the stated event, high-versus-low patient risk ratio divides high event risk by low event risk. Identity follows the event/reference labels and Table 3 reference-patient footnote. A different adjusted/standardized estimand or reversed conditioning requires its definition; no interval/P diagnostic is used to replace the point estimate.
- Reproduced calculation: (211/989)/(233/987)=0.903748096, nearest two-decimal0.90; printed0.93; signed gap0.026251904 exceeds0.005. Reverse-conditioning diagnostic: [211/(211+233)]/[(778)/(1532)]=0.935790546; truncating THAT quantity to two decimals gives0.93, exactly the printed point. This is risk of high-group membership conditional on event versus no event, a different contrast from event risk conditional on treatment.
- Determining fact/state: The direct source reproduces the labeled point and exact reference counts; the event-risk identity discrepancy remains. An alternative reverse-conditioning diagnostic reproduces the display but does not reconcile its stated event-risk interpretation. Evidence state recorded_candidate.
- Roles/type/all/domain: REPORT main article versus REPORT main article; S_W; S_W; report_internal_inconsistency.
- Missing definition and human question: Counts, reference populations, label, CI, and generic named approximation available. Missing: exact point-estimate formula, event/reference coding, whether an adjusted/standardized estimand is intended, and display rule. No row-specific covariate adjustment is identified for this Table 3 point. For Primary postoperative pulmonary complications within five days, what exact formula, outcome/reference orientation and display rule produced RR0.93? Is it intended as H/L event risk, a reversed-conditioning contrast, or a specifically defined adjusted/model quantity?
- Alternative and direct-versus-inferred boundary: The reverse-conditioning diagnostic computed solely from the printed 2×2 counts plus truncation reproduces this point. It is a source-grounded numerical explanation, not evidence that the authors used that coding. A differently defined adjusted/standardized RR could also differ from the crude event ratio, but its target/formula must be supplied. The Wald-approximation wording alone does not define a different point contrast. Direct: count/reference cells, risk-ratio heading, point/interval and generic calculation wording. Derived: event-risk identity and reverse-conditioning diagnostic. Inferred: swapped coding, truncation, or adjustment; no production cause is asserted.

