# Current-run audit evidence shard

## C082 — conditional thoracic VAS mean/SD bound

**Candidate statement:** conditional thoracic VAS mean/SD bound; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Numeric or arithmetic inconsistency
**Relationship type:** P_R
**All relationships:** P_R
**Compared document roles:** REPORT supplement eTable 7 thoracic summary versus PLAN protocol VAS scale/assessment
**Review domain:** protocol_report
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** The reported completed-trial summary is REPORT and the prospective measurement definition is PLAN; the substantive conditional scale comparison is P_R.
**Classification ambiguity:** P_R is conditional scale-to-report comparison; numerical endpoints and postoperative identity are not printed.
**Checker provenance:** checkers/parts/numeric_support_tables.md :: SUPPORT-NUM-02

**Assigned relationship:** N327.

**Compared locations and document roles:**

- [DOC-005 results supplement, physical PDF p.28](../../../joi190055supp4_prod_16092.pdf#page=28), eTable 7, VAS thoracic – cm, mean (SD), No., Day 2, low PEEP cell: REPORT.
- [DOC-002 protocol, physical PDF p.17](../../../joi190055supp1_prod_16092.pdf#page=17), printed protocol p.16, version 2.6, actual organ function evaluation bullet defining “Visual Analogue Scale (10 cm): evaluation for dyspnea, thoracic and abdominal rest and incident pain”: PLAN.
- [DOC-002 protocol, physical PDF p.20](../../../joi190055supp1_prod_16092.pdf#page=20), printed protocol p.19, postoperative assessment continuation bullet “VAS evaluation for dyspnea, thoracic and abdominal rest and incident pain”: PLAN.

**Printed inputs:** eTable 7 low PEEP day-2 thoracic VAS mean 1.4 cm, SD 3.9 cm, n = 841; high PEEP mean 1.3 cm, SD 0.8 cm, n = 838; P = .34. Arm headings are high989 and low987. The protocol specifies a 10 cm VAS for the same named symptoms and repeats the assessment postoperatively. It does not explicitly print the numerical scoring endpoints or a normalization rule.

**Reproducible rule and calculation:** Conditional on the reported cm scores being distance along the supplied 10 cm line, measured from a zero origin and bounded 0–10 cm, any sample with mean m and sample SD s obeys s² ≤ n/(n−1) × m × (10−m). At the printed mean, the maximum sample SD is sqrt(841/840 × 1.4 × 8.6) = 3.47194 cm, below 3.9 cm. With rounding admitted, m can range from 1.35 to 1.45; the largest permitted bound on that interval is sqrt(841/840 × 1.45 × 8.55) = 3.52310 cm. The printed SD interval begins at 3.85 cm. Thus even the most permissive rounding leaves a gap of at least 3.85 − 3.52310 = 0.32690 cm.

**Tolerance:** Mean/SD displayed to one decimal permit ±0.05 cm; n = 841 is exact. The n/(n−1) factor allows the usual sample SD convention and is slightly more permissive than population SD. This calculation is a moment bound, not a reconstructed P value.

**Direct observation versus inference:** The mean, SD, n, cm unit, mean(SD) header and protocol 10 cm scale wording are direct source observations. The numerical 0–10 support and zero-origin scoring convention are explicitly conditional inferences from that supplied line-length and cm-unit description. They are not independently printed endpoints. Protocol p.17 describes baseline organ-function assessment; p.20 repeats the same named VAS postoperatively but does not restate its length. Applying the 10 cm definition to eTable 7 is an identity question retained for human review.

**Alternatives and missing definition:** A transformed or shifted scoring convention, a differently normalized postoperative scale, a larger allowed range, a different underlying statistic despite the mean(SD) label, or a transcription error could explain the display. Without zero origin, a line of length10 alone permits SD up to about5.00 cm and does not establish the mean-dependent contradiction. An alternative 0-based scale would need an upper endpoint at least11.66026 cm even with the rounding allowances, to accommodate the minimum printed SD3.85 at mean1.45. No external VAS convention is used.

**Quality-control relevance:** The reported dispersion may be reused as a summary SD in quantitative evidence synthesis. The candidate is confined to the consistency of that reported summary with the supplied scale definition; it is not a raw-data or clinical plausibility audit.

**Exact human question:** “Were the postoperative thoracic VAS scores in eTable 7 recorded as 0–10 cm distance scores on the protocol’s 10 cm scale, and does the low-PEEP Day 2 cell correctly report mean 1.4 cm, SD 3.9 cm and n = 841; if a different origin, range or transformation was used, what was it?”

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Direct source confirms the tuple and 10 cm plan description; the registered bounded-support question remains conditional on its explicitly missing origin/scale identity. Diagnostic: At m1.4,n841, maximum SD=3.47194. Allowing mean rounding up to1.45 gives 3.52310, below minimum rounding-consistent SD3.85 by 0.32690 cm. Classification P_R; all P_R; protocol_report; no role/type code correction.
- Missing definition and human question: Numerical scoring origin/endpoints, postoperative identity with the baseline-defined scale, transformation and SD convention. Human question: Were postoperative thoracic scores zero-origin 0–10 cm scores on the protocol line, and does the low Day 2 tuple correctly read mean1.4, SD3.9, n841; if different, what origin/range/transformation was used?

## C083 — conditional event-count mean versus component total

**Candidate statement:** conditional event-count mean versus component total; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT supplement eTable 9 count summary versus REPORT main Table 3 component numerators; REPORT main randomized denominator is an alternative; PLAN SAP count definition corroborates
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** First summary and realized count aggregation are not explicitly defined. SAP corroborates count concept without a P_R discrepancy.
**Checker provenance:** checkers/parts/numeric_support_tables.md :: SUPPORT-NUM-03

**Assigned relationship:** N355.

**Compared locations and document roles:**

- [DOC-005 results supplement, physical PDF p.30](../../../joi190055supp4_prod_16092.pdf#page=30), eTable 9, Sensitivity analysis for the primary outcome, Count events row, high/low summary cells and n = 989/987 headings: REPORT.
- [DOC-001 main article, physical PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), printed p.2300, Table 3, all 12 Components of the Primary Outcome, high/low No. of Events columns and n = 989/987 headings: REPORT.
- DOC-005 p.30 model footnotes referring to all12 components are corroborative REPORT context, not a new discrepancy relationship.
- [DOC-001 main article, physical PDF p.3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), Figure 1 randomized high 1011/low 1002, REPORT: source-grounded alternative denominator, not an additional discrepancy relationship.

**Printed inputs:** eTable 9 Count events row gives high0.35 (0.88), low0.38 (0.86), above separately labeled Median (IQR)0 (0–0) for both arms. The Count events row does not explicitly say mean(SD). Main Table 3 high component counts, in its printed order, are mild135, moderate42, severe30, atelectasis44, pleural effusion43, new infiltrates14, cardiopulmonary edema17, bronchospasm12, pulmonary infection10, aspiration2, ARDS3, pneumothorax1. Low counts in the same order are154,58,36,55,21,18,9,10,10,1,1,3.

**Reproducible rule and calculation:** Conditional on “Count events” summary0.35/0.38 being the arithmetic mean of the number of these same12 binary components per participant in the displayed full-arm populations, the mean must equal the sum of all component numerators divided by n. Overlap between components does not defeat this identity; each counted component contributes separately. High sum135 + 42 + 30 + 44 + 43 + 14 + 17 + 12 + 10 + 2 + 3 + 1 = 353; 353 / 989 = 0.356926, which rounds to0.36. Low sum154 + 58 + 36 + 55 + 21 + 18 + 9 + 10 + 10 + 1 + 1 + 3 = 376; 376 / 987 = 0.380952, which rounds to0.38 and reconciles.

**Tolerance:** At two-decimal rounding,0.35 ordinarily implies a mean in [0.345,0.355), hence a total in [341.205,351.095) at n989; integer totals compatible with that interval are342–351. The printed component total353 exceeds the largest compatible integer total by2. The exact mean exceeds the upper rounding boundary0.355 by0.001926. Counts and denominator have zero tolerance. The low-arm summary is within its rounding interval.

**Direct observation versus inference:** Direct images confirm all12 main component counts, populations, and the eTable 9 summary0.35 (0.88). The arithmetic sum and conditional mean identity are derived. Interpreting the unlabeled first summary as mean(SD), and interpreting “Count events” as counting each of the same12 binary components, are named inferences rather than printed definitions.

**Alternatives and missing definition:** The summary may use a different statistic, component grouping (for example collapsing multiple respiratory-failure severities to one event), time rule, population, event definition, weighting or complete-case denominator. Main Figure 1 supplies randomized high 1011/low 1002: 353/1011 = 0.349159 and 376/1002 = 0.375250, which round to 0.35/0.38. Thus a count calculation using all randomized participants could explain both summary means, but that denominator differs from eTable 9 headings 989/987 and requires the population and missing-participant handling to be named. This is an arithmetic alternative, not proof that the authors used it. Truncation rather than rounding would also produce 0.35 from 0.356926 but is not stated. Different component overlap is not by itself an explanation if the count is the sum of those same 12 indicators; alternative grouping would change the count definition and should be specified.

**Quality-control relevance:** Event burden means and their dispersions can be extracted separately from binary-composite risks; a missing aggregation definition or mismatched displayed mean can lead to an incorrect extracted endpoint. No claim about treatment effect or conclusion follows.

**Exact human question:** “Is 0.35 (0.88) in the high-PEEP Count events row the mean (SD) of the count of the same 12 primary-outcome components reported in main Table 3 among 989 participants; if so, how does it reconcile with 353 component occurrences and 353/989 = 0.356926, and if not, what statistic, grouping, time rule and denominator does it represent?”
**Additional source-grounded denominator alternative:** REPORT [main Figure1 p.3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3) randomized arm counts1011/1002 yield353/1011=.349159→.35 and376/1002=.375250→.38. All-randomized denominators with zero-filled exclusions could explain the displays, although eTable9 headings are989/987. This is an alternative to verify, not a separate candidate.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Count tuple and component totals are confirmed; arithmetic reproduces the registered conditional high-arm rounding question. Diagnostic: High sum353;353/989=0.356926→0.36, versus0.35. Low sum376;376/987=0.380952→0.38. High two-decimal0.35 permits integer totals342–351 under ordinary rounding. Alternative353/1011=0.349159→0.35 and376/1002=0.375250→0.38. Classification S_C; all S_C; statistical_results; no role/type code correction.
- Missing definition and human question: First summary statistic label, actual event grouping/time rule, analysis n, missing-participant treatment and rounding convention. Human question: Is 0.35(0.88) the mean(SD) of these twelve component counts among989 high participants; if so how does353/989 reconcile, and otherwise what statistic/grouping/window/denominator and participant handling define it?

## C084 — Four-day median follow-up and day-five numbers at risk require incompatible time definitions — eFigure8

**Candidate statement:** Four-day median follow-up and day-five numbers at risk require incompatible time definitions — eFigure8; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT supplement eFigure 8 PPC caption versus same-page risk table
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.
**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-F02

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 38](../../../joi190055supp4_prod_16092.pdf#page=38) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 39](../../../joi190055supp4_prod_16092.pdf#page=39) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 40](../../../joi190055supp4_prod_16092.pdf#page=40) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 41](../../../joi190055supp4_prod_16092.pdf#page=41) caption and all risk-table cells, REPORT.

**Printed inputs:** Each caption states median follow-up4 (2–5) days. Day5 low/high at-risk counts are756/785,756/785,845/828,986/985. Baseline counts are987/989, total1976.

**Reproducible rule and calculation:** If follow-up means the observed time governing those risk tables, at least half of1976 follow-up times must be ≤4 for median4. Thus at most988 can remain at risk on day5 (even allowing both central order statistics and ties). Printed day5 sums1541,1541,1673,1971 exceed988 by553,553,685,983. Even within arms every listed day5 count exceeds half the baseline arm.

**Tolerance:** Counts exact. A median rounded to integer4 would ordinarily lie below4.5, still below5; it cannot explain >half at risk at day5. A distinct follow-up variable could reconcile the statements.

**Direct observation versus inference:** The caption and all48 risk counts are directly printed and checked. The incompatibility is conditional inference that caption follow-up and risk-table follow-up refer to the same observed time.

**Alternatives:** Median4 may refer to postoperative assessment duration while risk tables retain patients through administrative day5, or “number at risk” may be a different denominator. Neither alternative is defined locally. Event/censor timing need not be reconstructed. Identical primary/severe rows alone were not used as a candidate.

**Quality-control relevance:** Time-dependent denominators and follow-up summaries could be reused under incompatible definitions.

**Exact human question:** What exact follow-up duration has median4 (2–5), what removes patients from each Figure8–11 risk table, and how can more than half remain at risk on day5 under that duration?
**Registered comparison scope:** eFigure8 only: PDF p.38, day5 H/L at risk 785/756, total 1541, versus at most988 under shared observed-time interpretation of median4. Other figures are separate IDs because endpoint-specific event/censor/risk definitions may differ.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1541 exceeds988 by553. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction.
- Missing definition and human question: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 8 PPC, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary?

## C085 — Four-day median follow-up and day-five numbers at risk require incompatible time definitions — eFigure9

**Candidate statement:** Four-day median follow-up and day-five numbers at risk require incompatible time definitions — eFigure9; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT supplement eFigure 9 severe PPC caption versus same-page risk table
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.
**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-F02

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 38](../../../joi190055supp4_prod_16092.pdf#page=38) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 39](../../../joi190055supp4_prod_16092.pdf#page=39) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 40](../../../joi190055supp4_prod_16092.pdf#page=40) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 41](../../../joi190055supp4_prod_16092.pdf#page=41) caption and all risk-table cells, REPORT.

**Printed inputs:** Each caption states median follow-up4 (2–5) days. Day5 low/high at-risk counts are756/785,756/785,845/828,986/985. Baseline counts are987/989, total1976.

**Reproducible rule and calculation:** If follow-up means the observed time governing those risk tables, at least half of1976 follow-up times must be ≤4 for median4. Thus at most988 can remain at risk on day5 (even allowing both central order statistics and ties). Printed day5 sums1541,1541,1673,1971 exceed988 by553,553,685,983. Even within arms every listed day5 count exceeds half the baseline arm.

**Tolerance:** Counts exact. A median rounded to integer4 would ordinarily lie below4.5, still below5; it cannot explain >half at risk at day5. A distinct follow-up variable could reconcile the statements.

**Direct observation versus inference:** The caption and all48 risk counts are directly printed and checked. The incompatibility is conditional inference that caption follow-up and risk-table follow-up refer to the same observed time.

**Alternatives:** Median4 may refer to postoperative assessment duration while risk tables retain patients through administrative day5, or “number at risk” may be a different denominator. Neither alternative is defined locally. Event/censor timing need not be reconstructed. Identical primary/severe rows alone were not used as a candidate.

**Quality-control relevance:** Time-dependent denominators and follow-up summaries could be reused under incompatible definitions.

**Exact human question:** What exact follow-up duration has median4 (2–5), what removes patients from each Figure8–11 risk table, and how can more than half remain at risk on day5 under that duration?
**Registered comparison scope:** eFigure9 only: PDF p.39, day5 H/L at risk 785/756, total 1541, versus at most988 under shared observed-time interpretation of median4. Other figures are separate IDs because endpoint-specific event/censor/risk definitions may differ.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1541 exceeds988 by553. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction.
- Missing definition and human question: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 9 severe PPC, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary?

## C086 — Four-day median follow-up and day-five numbers at risk require incompatible time definitions — eFigure10

**Candidate statement:** Four-day median follow-up and day-five numbers at risk require incompatible time definitions — eFigure10; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT supplement eFigure 10 extrapulmonary caption versus same-page risk table
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.
**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-F02

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 38](../../../joi190055supp4_prod_16092.pdf#page=38) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 39](../../../joi190055supp4_prod_16092.pdf#page=39) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 40](../../../joi190055supp4_prod_16092.pdf#page=40) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 41](../../../joi190055supp4_prod_16092.pdf#page=41) caption and all risk-table cells, REPORT.

**Printed inputs:** Each caption states median follow-up4 (2–5) days. Day5 low/high at-risk counts are756/785,756/785,845/828,986/985. Baseline counts are987/989, total1976.

**Reproducible rule and calculation:** If follow-up means the observed time governing those risk tables, at least half of1976 follow-up times must be ≤4 for median4. Thus at most988 can remain at risk on day5 (even allowing both central order statistics and ties). Printed day5 sums1541,1541,1673,1971 exceed988 by553,553,685,983. Even within arms every listed day5 count exceeds half the baseline arm.

**Tolerance:** Counts exact. A median rounded to integer4 would ordinarily lie below4.5, still below5; it cannot explain >half at risk at day5. A distinct follow-up variable could reconcile the statements.

**Direct observation versus inference:** The caption and all48 risk counts are directly printed and checked. The incompatibility is conditional inference that caption follow-up and risk-table follow-up refer to the same observed time.

**Alternatives:** Median4 may refer to postoperative assessment duration while risk tables retain patients through administrative day5, or “number at risk” may be a different denominator. Neither alternative is defined locally. Event/censor timing need not be reconstructed. Identical primary/severe rows alone were not used as a candidate.

**Quality-control relevance:** Time-dependent denominators and follow-up summaries could be reused under incompatible definitions.

**Exact human question:** What exact follow-up duration has median4 (2–5), what removes patients from each Figure8–11 risk table, and how can more than half remain at risk on day5 under that duration?
**Registered comparison scope:** eFigure10 only: PDF p.40, day5 H/L at risk 828/845, total 1673, versus at most988 under shared observed-time interpretation of median4. Other figures are separate IDs because endpoint-specific event/censor/risk definitions may differ.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1673 exceeds988 by685. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction.
- Missing definition and human question: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 10 extrapulmonary, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary?

## C087 — Four-day median follow-up and day-five numbers at risk require incompatible time definitions — eFigure11

**Candidate statement:** Four-day median follow-up and day-five numbers at risk require incompatible time definitions — eFigure11; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Denominator, proportion, or total inconsistency
**Relationship type:** S_W
**All relationships:** S_W
**Compared document roles:** REPORT supplement eFigure 11 mortality caption versus same-page risk table
**Review domain:** statistical_results
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.
**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-F02

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 38](../../../joi190055supp4_prod_16092.pdf#page=38) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 39](../../../joi190055supp4_prod_16092.pdf#page=39) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 40](../../../joi190055supp4_prod_16092.pdf#page=40) caption and all risk-table cells, REPORT; [joi190055supp4_prod_16092.pdf, PDF p. 41](../../../joi190055supp4_prod_16092.pdf#page=41) caption and all risk-table cells, REPORT.

**Printed inputs:** Each caption states median follow-up4 (2–5) days. Day5 low/high at-risk counts are756/785,756/785,845/828,986/985. Baseline counts are987/989, total1976.

**Reproducible rule and calculation:** If follow-up means the observed time governing those risk tables, at least half of1976 follow-up times must be ≤4 for median4. Thus at most988 can remain at risk on day5 (even allowing both central order statistics and ties). Printed day5 sums1541,1541,1673,1971 exceed988 by553,553,685,983. Even within arms every listed day5 count exceeds half the baseline arm.

**Tolerance:** Counts exact. A median rounded to integer4 would ordinarily lie below4.5, still below5; it cannot explain >half at risk at day5. A distinct follow-up variable could reconcile the statements.

**Direct observation versus inference:** The caption and all48 risk counts are directly printed and checked. The incompatibility is conditional inference that caption follow-up and risk-table follow-up refer to the same observed time.

**Alternatives:** Median4 may refer to postoperative assessment duration while risk tables retain patients through administrative day5, or “number at risk” may be a different denominator. Neither alternative is defined locally. Event/censor timing need not be reconstructed. Identical primary/severe rows alone were not used as a candidate.

**Quality-control relevance:** Time-dependent denominators and follow-up summaries could be reused under incompatible definitions.

**Exact human question:** What exact follow-up duration has median4 (2–5), what removes patients from each Figure8–11 risk table, and how can more than half remain at risk on day5 under that duration?
**Registered comparison scope:** eFigure11 only: PDF p.41, day5 H/L at risk 985/986, total 1971, versus at most988 under shared observed-time interpretation of median4. Other figures are separate IDs because endpoint-specific event/censor/risk definitions may differ.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1971 exceeds988 by983. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction.
- Missing definition and human question: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 11 mortality, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary?

## C088 — Mild respiratory failure: forest risk-ratio label does not reconcile with arm event proportions

**Candidate statement:** Mild respiratory failure: forest risk-ratio label does not reconcile with arm event proportions; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context
**Review domain:** report_internal_inconsistency
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-R01

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Mild respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.92[0.76,1.12],99.58%CI; matched main events high135/989,low154/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(135/989)/(154/987)=0.874851. Printed 0.92 differs by0.045149. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Mild respiratory failure forest row, what population, contrast, numerator/denominator and estimator produced0.92, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (135/989)/(154/987)=0.874851; absolute distance from0.92=0.045149, larger than .005. Interval is positive, ordered and contains its printed point (0.76≤0.92≤1.12). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Mild respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.92, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C089 — Moderate respiratory failure: forest risk-ratio label does not reconcile with arm event proportions

**Candidate statement:** Moderate respiratory failure: forest risk-ratio label does not reconcile with arm event proportions; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context
**Review domain:** report_internal_inconsistency
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-R02

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Moderate respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.83[0.59,1.17],99.58%CI; matched main events high42/989,low58/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(42/989)/(58/987)=0.722674. Printed 0.83 differs by0.107326. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Moderate respiratory failure forest row, what population, contrast, numerator/denominator and estimator produced0.83, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (42/989)/(58/987)=0.722674; absolute distance from0.83=0.107326, larger than .005. Interval is positive, ordered and contains its printed point (0.59≤0.83≤1.17). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Moderate respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.83, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C090 — Severe respiratory failure: forest risk-ratio label does not reconcile with arm event proportions

**Candidate statement:** Severe respiratory failure: forest risk-ratio label does not reconcile with arm event proportions; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context
**Review domain:** report_internal_inconsistency
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-R03

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Severe respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.91[0.61,1.34],99.58%CI; matched main events high30/989,low36/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(30/989)/(36/987)=0.831648. Printed 0.91 differs by0.078352. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Severe respiratory failure forest row, what population, contrast, numerator/denominator and estimator produced0.91, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (30/989)/(36/987)=0.831648; absolute distance from0.91=0.078352, larger than .005. Interval is positive, ordered and contains its printed point (0.61≤0.91≤1.34). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Severe respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.91, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C091 — Aspiration: forest risk-ratio label does not reconcile with arm event proportions

**Candidate statement:** Aspiration: forest risk-ratio label does not reconcile with arm event proportions; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context
**Review domain:** report_internal_inconsistency
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-R04

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Aspiration row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.33[0.41,4.30],99.58%CI; matched main events high2/989,low1/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(2/989)/(1/987)=1.995956. Printed 1.33 differs by0.665956. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Aspiration forest row, what population, contrast, numerator/denominator and estimator produced1.33, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (2/989)/(1/987)=1.995956; absolute distance from1.33=0.665956, larger than .005. Interval is positive, ordered and contains its printed point (0.41≤1.33≤4.30). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Aspiration, what realized GLM/link/contrast/adjustment/population produced1.33, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C092 — Bronchospasm: forest risk-ratio label does not reconcile with arm event proportions

**Candidate statement:** Bronchospasm: forest risk-ratio label does not reconcile with arm event proportions; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context
**Review domain:** report_internal_inconsistency
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-R05

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Bronchospasm row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.09[0.62,1.91],99.58%CI; matched main events high12/989,low10/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(12/989)/(10/987)=1.197573. Printed 1.09 differs by0.107573. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Bronchospasm forest row, what population, contrast, numerator/denominator and estimator produced1.09, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (12/989)/(10/987)=1.197573; absolute distance from1.09=0.107573, larger than .005. Interval is positive, ordered and contains its printed point (0.62≤1.09≤1.91). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Bronchospasm, what realized GLM/link/contrast/adjustment/population produced1.09, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C093 — ARDS: forest risk-ratio label does not reconcile with arm event proportions

**Candidate statement:** ARDS: forest risk-ratio label does not reconcile with arm event proportions; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context
**Review domain:** report_internal_inconsistency
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-R06

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 ARDS row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.50[0.65,3.44],99.58%CI; matched main events high3/989,low1/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(3/989)/(1/987)=2.993933. Printed 1.50 differs by1.493933. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the ARDS forest row, what population, contrast, numerator/denominator and estimator produced1.50, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (3/989)/(1/987)=2.993933; absolute distance from1.50=1.493933, larger than .005. Interval is positive, ordered and contains its printed point (0.65≤1.50≤3.44). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For ARDS, what realized GLM/link/contrast/adjustment/population produced1.50, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C094 — Atelectasis: forest risk-ratio label does not reconcile with arm event proportions

**Candidate statement:** Atelectasis: forest risk-ratio label does not reconcile with arm event proportions; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context
**Review domain:** report_internal_inconsistency
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-R08

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Atelectasis row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.88[0.64,1.23],99.58%CI; matched main events high44/989,low55/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(44/989)/(55/987)=0.798382. Printed 0.88 differs by0.081618. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Atelectasis forest row, what population, contrast, numerator/denominator and estimator produced0.88, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (44/989)/(55/987)=0.798382; absolute distance from0.88=0.081618, larger than .005. Interval is positive, ordered and contains its printed point (0.64≤0.88≤1.23). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Atelectasis, what realized GLM/link/contrast/adjustment/population produced0.88, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C095 — Cardiopulmonary edema: forest risk-ratio label does not reconcile with arm event proportions

**Candidate statement:** Cardiopulmonary edema: forest risk-ratio label does not reconcile with arm event proportions; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context
**Review domain:** report_internal_inconsistency
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-R09

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Cardiopulmonary edema row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.31[0.87,1.98],99.58%CI; matched main events high17/989,low9/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(17/989)/(9/987)=1.885069. Printed 1.31 differs by0.575069. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Cardiopulmonary edema forest row, what population, contrast, numerator/denominator and estimator produced1.31, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (17/989)/(9/987)=1.885069; absolute distance from1.31=0.575069, larger than .005. Interval is positive, ordered and contains its printed point (0.87≤1.31≤1.98). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Cardiopulmonary edema, what realized GLM/link/contrast/adjustment/population produced1.31, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C096 — Pleural effusion: forest risk-ratio label does not reconcile with arm event proportions

**Candidate statement:** Pleural effusion: forest risk-ratio label does not reconcile with arm event proportions; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context
**Review domain:** report_internal_inconsistency
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-R10

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pleural effusion row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR1.36[1.05,1.76],99.58%CI; matched main events high43/989,low21/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(43/989)/(21/987)=2.043478. Printed 1.36 differs by0.683478. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Pleural effusion forest row, what population, contrast, numerator/denominator and estimator produced1.36, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (43/989)/(21/987)=2.043478; absolute distance from1.36=0.683478, larger than .005. Interval is positive, ordered and contains its printed point (1.05≤1.36≤1.76). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Pleural effusion, what realized GLM/link/contrast/adjustment/population produced1.36, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C097 — Pneumothorax: forest risk-ratio label does not reconcile with arm event proportions

**Candidate statement:** Pneumothorax: forest risk-ratio label does not reconcile with arm event proportions; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context
**Review domain:** report_internal_inconsistency
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-R11

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pneumothorax row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.50[0.04,5.96],99.58%CI; matched main events high1/989,low3/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(1/989)/(3/987)=0.332659. Printed 0.50 differs by0.167341. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Pneumothorax forest row, what population, contrast, numerator/denominator and estimator produced0.50, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (1/989)/(3/987)=0.332659; absolute distance from0.50=0.167341, larger than .005. Interval is positive, ordered and contains its printed point (0.04≤0.50≤5.96). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Pneumothorax, what realized GLM/link/contrast/adjustment/population produced0.50, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C098 — Pulmonary infiltrates: forest risk-ratio label does not reconcile with arm event proportions

**Candidate statement:** Pulmonary infiltrates: forest risk-ratio label does not reconcile with arm event proportions; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** S_C
**All relationships:** S_C
**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context
**Review domain:** report_internal_inconsistency
**Evidence state:** record_input_error
**Suggested review disposition:** discuss
**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R. 
**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.
**Checker provenance:** checkers/parts/numeric_planplots.md :: NP-R12

**Compared locations and document roles:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pulmonary infiltrates row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT.

**Printed inputs:** Forest RR0.87[0.49,1.55],99.58%CI; matched main events high14/989,low18/987.

**Reproducible rule and calculation:** Under the displayed arm-specific risk definition RR=(high events/high n)/(low events/low n)=(14/989)/(18/987)=0.776205. Printed 0.87 differs by0.093795. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR.

**Tolerance:** Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005.

**Direct observation versus inference:** The estimate, header and comparator counts are directly printed. Linking the sensitivity forest to the main full population is an inference supported by matching component names and the SAP component sensitivity analysis; it must be confirmed if another model/population was used.

**Alternatives:** An adjusted or differently oriented/model-based ratio may differ from the raw marginal RR. The forest does not print population-specific denominators or a separate adjusted-model label; such a model would require an explicit effect definition. No choice of corrected value is proposed.

**Quality-control relevance:** A component effect may be reused as a risk ratio under a denominator definition it does not reproduce.

**Exact human question:** For the Pulmonary infiltrates forest row, what population, contrast, numerator/denominator and estimator produced0.87, and should its “Risk Ratio” label mean the ratio of the printed trial-arm event risks?

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (14/989)/(18/987)=0.776205; absolute distance from0.87=0.093795, larger than .005. Interval is positive, ordered and contains its printed point (0.49≤0.87≤1.55). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction.
- Missing definition and human question: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Pulmonary infiltrates, what realized GLM/link/contrast/adjustment/population produced0.87, and does its RR mean the crude main-arm ratio or a model-defined ratio?

## C099 — Current protocol procedure total still says748 after revised2013 target

**Candidate statement:** Current protocol procedure total still says748 after revised2013 target; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Numeric or arithmetic inconsistency
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN protocol current procedure total versus PLAN protocol revised sample/recruitment target; PLAN amendment corroborates
**Review domain:** plan_material
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.
**Classification ambiguity:** Historical intent of section7.2 is not stated; no REPORT comparator creates P_R.
**Checker provenance:** checkers/cross_source_consistency.md :: XS09; checkers/parts/numeric_planplots.md :: NP-P01

Compared locations: PLAN [protocol v2.6 section6.4 p.11](../../../joi190055supp1_prod_16092.pdf#page=11) explicitly distinguishes initial748 and revised total2013; PLAN [same v2.6 section7.2 p.12](../../../joi190055supp1_prod_16092.pdf#page=12) prospective current statement “In total,748 patients will be included.” PLAN [p.10](../../../joi190055supp1_prod_16092.pdf#page=10) current recruitment2013; PLAN [amendment p.2](../../../joi190055supp2_prod_16092.pdf#page=2) corroborates revised2013. Rule: current total planned enrollment within same version should use the current revised target or explicitly label historical748. Alternative: unupdated procedural paragraph versus a retained historical statement without its time label. Human verification: compare version2.6 sections6.4/7.2 and approved amendment to determine intended current target. Main actual2013 only corroborates revised target; no REPORT discrepancy relationship is introduced.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Current source confirms future-tense748 alongside explicitly revised2013 in the same PLAN version. Diagnostic: 2013−748=1265. The initial748 is explicitly historical in section6.4, but section7.2 retains a current future-tense total. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Whether section7.2 was intended as retained historical text despite future tense. Human question: In version2.6, does section7.2 still prescribe748 or retain a historical paragraph; what current total was intended?

## C100 — One-sided tabulated futility region versus central two-sided graphical region

**Candidate statement:** One-sided tabulated futility region versus central two-sided graphical region; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Statistical reporting inconsistency
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN protocol monitoring table look1 versus PLAN protocol boundary figure at enrollment956; PLAN amendment and REPORT supplement repeated graphic corroborate
**Review domain:** plan_material
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.
**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.
**Checker provenance:** checkers/parts/statistical_pass_1_planplots.md :: PP-FUT1

**S relationship:** S277.
**Compared locations and document roles:** [DOC-002 PDF p.22](../../../joi190055supp1_prod_16092.pdf#page=22), PLAN, look1 Z-futility cell; [DOC-002 PDF p.23](../../../joi190055supp1_prod_16092.pdf#page=23), PLAN, central pink Futility region at enrollment956. [DOC-005 PDF p.31](../../../joi190055supp4_prod_16092.pdf#page=31), REPORT, corroborates the central graphical region. [DOC-003 PDF p.3](../../../joi190055supp2_prod_16092.pdf#page=3), PLAN, confirms that the table and figure were introduced for the same revised monitoring design.
**Printed evidence:** The table gives Z<0.225. The plot marks the pink Futility area between a negative inner boundary and its positive counterpart. Values below the negative inner boundary are outside the graphical futility area.
**Rule and calculation:** A signed inequality Z<+0.225 includes every negative ordinate. A central graphical region excludes negative ordinates sufficiently far below zero. For a witness that avoids reading an exact plotted coordinate, Z=−4 satisfies the tabulated inequality and lies outside the pink region. The two regions are therefore different if the same signed statistic is intended.
**Direct observation versus diagnostic:** The inequality, signed axis and colored region are direct. Any statement that the graphical boundary is exactly±0.225 is a magnitude alignment only.
**Alternative source-grounded interpretations:** The table could summarize a one-sided alternative-oriented rule, while the figure additionally partitions efficacy/harm; it might also intend |Z| in the table. No absolute-value notation or rule-priority/sign-conversion explanation is supplied. At look3 the efficacy and futility table entries form complementary regions of a single signed statistic, whereas the figure includes both harm and efficacy outer tails.
**Named uncertainty and human question:** Is the table's Z a signed statistic, a magnitude, or a one-sided alternative-oriented convention? What mapping/rule priority relates the tabulated futility inequality to the figure's central region?
**Quality-control relevance:** Extraction of a futility stopping region requires the sign and rule definition. This is distinct from PP-Z1's efficacy-tail sign comparison because it compares a different cell and interval-region rule.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z=−4 satisfies Z<+0.225 but lies outside the pink central region at N956. Thus these sets differ under a common signed-Z interpretation. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look1 N956, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region?

## C101 — One-sided tabulated futility region versus central two-sided graphical region

**Candidate statement:** One-sided tabulated futility region versus central two-sided graphical region; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Statistical reporting inconsistency
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN protocol monitoring table look2 versus PLAN protocol boundary figure at enrollment1434; PLAN amendment and REPORT supplement repeated graphic corroborate
**Review domain:** plan_material
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.
**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.
**Checker provenance:** checkers/parts/statistical_pass_1_planplots.md :: PP-FUT2

**S relationship:** S279.
**Compared locations and document roles:** [DOC-002 PDF p.22](../../../joi190055supp1_prod_16092.pdf#page=22), PLAN, look2 Z-futility cell; [DOC-002 PDF p.23](../../../joi190055supp1_prod_16092.pdf#page=23), PLAN, central pink Futility region at enrollment1434. [DOC-005 PDF p.31](../../../joi190055supp4_prod_16092.pdf#page=31), REPORT, corroborates the central graphical region. [DOC-003 PDF p.3](../../../joi190055supp2_prod_16092.pdf#page=3), PLAN, confirms that the table and figure were introduced for the same revised monitoring design.
**Printed evidence:** The table gives Z<0.929. The plot marks the pink Futility area between a negative inner boundary and its positive counterpart. Values below the negative inner boundary are outside the graphical futility area.
**Rule and calculation:** A signed inequality Z<+0.929 includes every negative ordinate. A central graphical region excludes negative ordinates sufficiently far below zero. For a witness that avoids reading an exact plotted coordinate, Z=−4 satisfies the tabulated inequality and lies outside the pink region. The two regions are therefore different if the same signed statistic is intended.
**Direct observation versus diagnostic:** The inequality, signed axis and colored region are direct. Any statement that the graphical boundary is exactly±0.929 is a magnitude alignment only.
**Alternative source-grounded interpretations:** The table could summarize a one-sided alternative-oriented rule, while the figure additionally partitions efficacy/harm; it might also intend |Z| in the table. No absolute-value notation or rule-priority/sign-conversion explanation is supplied. At look3 the efficacy and futility table entries form complementary regions of a single signed statistic, whereas the figure includes both harm and efficacy outer tails.
**Named uncertainty and human question:** Is the table's Z a signed statistic, a magnitude, or a one-sided alternative-oriented convention? What mapping/rule priority relates the tabulated futility inequality to the figure's central region?
**Quality-control relevance:** Extraction of a futility stopping region requires the sign and rule definition. This is distinct from PP-Z2's efficacy-tail sign comparison because it compares a different cell and interval-region rule.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z=−4 satisfies Z<+0.929 but lies outside the pink central region at N1434. Thus these sets differ under a common signed-Z interpretation. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look2 N1434, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region?

## C102 — One-sided tabulated futility region versus central two-sided graphical region

**Candidate statement:** One-sided tabulated futility region versus central two-sided graphical region; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Statistical reporting inconsistency
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN protocol monitoring table look3 versus PLAN protocol boundary figure at enrollment1912; PLAN amendment and REPORT supplement repeated graphic corroborate
**Review domain:** plan_material
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.
**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.
**Checker provenance:** checkers/parts/statistical_pass_1_planplots.md :: PP-FUT3

**S relationship:** S281.
**Compared locations and document roles:** [DOC-002 PDF p.22](../../../joi190055supp1_prod_16092.pdf#page=22), PLAN, look3 Z-futility cell; [DOC-002 PDF p.23](../../../joi190055supp1_prod_16092.pdf#page=23), PLAN, central pink Futility region at enrollment1912. [DOC-005 PDF p.31](../../../joi190055supp4_prod_16092.pdf#page=31), REPORT, corroborates the central graphical region. [DOC-003 PDF p.3](../../../joi190055supp2_prod_16092.pdf#page=3), PLAN, confirms that the table and figure were introduced for the same revised monitoring design.
**Printed evidence:** The table gives Z<2.012. The plot marks the pink Futility area between a negative inner boundary and its positive counterpart. Values below the negative inner boundary are outside the graphical futility area.
**Rule and calculation:** A signed inequality Z<+2.012 includes every negative ordinate. A central graphical region excludes negative ordinates sufficiently far below zero. For a witness that avoids reading an exact plotted coordinate, Z=−4 satisfies the tabulated inequality and lies outside the pink region. The two regions are therefore different if the same signed statistic is intended.
**Direct observation versus diagnostic:** The inequality, signed axis and colored region are direct. Any statement that the graphical boundary is exactly±2.012 is a magnitude alignment only.
**Alternative source-grounded interpretations:** The table could summarize a one-sided alternative-oriented rule, while the figure additionally partitions efficacy/harm; it might also intend |Z| in the table. No absolute-value notation or rule-priority/sign-conversion explanation is supplied. At look3 the efficacy and futility table entries form complementary regions of a single signed statistic, whereas the figure includes both harm and efficacy outer tails.
**Named uncertainty and human question:** Is the table's Z a signed statistic, a magnitude, or a one-sided alternative-oriented convention? What mapping/rule priority relates the tabulated futility inequality to the figure's central region?
**Quality-control relevance:** Extraction of a futility stopping region requires the sign and rule definition. This is distinct from PP-Z3's efficacy-tail sign comparison because it compares a different cell and interval-region rule.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z=−4 satisfies Z<+2.012 but lies outside the pink central region at N1912. Thus these sets differ under a common signed-Z interpretation. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look3 N1912, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region?

## C103 — Original primary-analysis effect label combines OR and RR

**Candidate statement:** Original primary-analysis effect label combines OR and RR; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Measure, label, or scale inconsistency
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN protocol primary-analysis sentence containing both measure terms; PLAN updated SAP is later explanatory context
**Review domain:** plan_material
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.
**Classification ambiguity:** Later SAP may supersede original wording; it does not remove the original PLAN-internal label question.
**Checker provenance:** checkers/parts/statistical_pass_1_planplots.md :: PP-LABEL

**S relationship:** S286.
**Compared locations and document roles:** [DOC-002 PDF p.23](../../../joi190055supp1_prod_16092.pdf#page=23), PLAN, same primary-efficacy-analysis sentence. Both compared labels are PLAN content. [DOC-004 PDF p.2](../../../joi190055supp3_prod_16092.pdf#page=2), PLAN, subsequently specifies risk ratio and is an explanatory later-plan comparator; it does not remove the original sentence's displayed labels.
**Printed evidence:** Original primary phrase is “odds ratio relative risks” with corresponding95% confidence interval calculated using logistic regression. The adjacent words were confirmed in the PDF image; they are not a locator/OCR repair.
**Rule and calculation:** OR=[pH/(1−pH)]/[pL/(1−pL)] and RR=pH/pL are distinct scales. Within the original declared sample assumptions pH=.30,pL=.40, RR=.75 while OR=(.30/.70)/(.40/.60)=.642857. This illustrative calculation uses supplied planning probabilities; it is not an observed-result recalculation.
**Direct observation versus diagnostic:** Two different effect-measure terms printed together are direct. The planned-probability calculation illustrates distinction; it does not establish which effect was intended.
**Alternative source-grounded interpretations:** The phrase may represent an unfinished replacement of OR by RR, or may intend two effects. Logistic regression can be followed by probability standardization, so its mention alone does not identify the effect.
**Named uncertainty and human question:** Which measure(s), contrast and logistic postprocessing were intended by the original sentence, and which label belongs to the associated interval? The later SAP gives RR but should not silently rewrite the preserved original source.
**Quality-control relevance:** A reader extracting the original plan cannot uniquely label the effect from this sentence.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Current render confirms adjacent odds ratio relative risks; source-label ambiguity reproduces without relying on an OCR error. Diagnostic: For supplied assumptions RR=.30/.40=.75; OR=(.30/.70)/(.40/.60)=.642857. This illustrates scale difference, not an observed-result recalculation. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Intended measure(s), contrast and logistic postprocessing for original sentence. Human question: Which measure(s), contrast and postprocessing did the original primary sentence intend, and which measure labels its interval?

## C104 — Efficacy boundary has opposite signed direction in table and figure

**Candidate statement:** Efficacy boundary has opposite signed direction in table and figure; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Statistical reporting inconsistency
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN protocol monitoring table look1 versus PLAN protocol boundary figure at enrollment956; PLAN amendment and REPORT supplement repeated graphic corroborate
**Review domain:** plan_material
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.
**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.
**Checker provenance:** checkers/parts/statistical_pass_1_planplots.md :: PP-Z1

**S relationship:** S276.
**Compared locations and document roles:** [DOC-002 PDF p.22](../../../joi190055supp1_prod_16092.pdf#page=22), PLAN, statistical-analysis table, look1 efficacy; [DOC-002 PDF p.23](../../../joi190055supp1_prod_16092.pdf#page=23), PLAN, stopping-boundary figure, Efficacy region at enrollment956. [DOC-005 PDF p.31](../../../joi190055supp4_prod_16092.pdf#page=31), REPORT, reproduces the negative-Z efficacy graphical orientation and corroborates the figure side; [DOC-003 PDF p.3](../../../joi190055supp2_prod_16092.pdf#page=3), PLAN, amendment explicitly introduces the same table/figure but adds no signed contrast definition. The REPORT location corroborates rather than creates an additional discrepancy.
**Printed evidence:** The table calls the look1 efficacy boundary Z≥2.75. The plotted region labelled Efficacy lies below zero and its corresponding outer boundary is at a negative ordinate. Harm lies above zero. Exact graphical ordinate coordinates are not independently printed; the sign is directly visible.
**Rule and calculation:** If these are the same signed statistic, Z≥+2.75 and an efficacy region Z≤−2.75 are opposite directions. The negative boundary magnitude is a graphical alignment to the table, not a new exact numeric transcription. No P-tail reconstruction is required.
**Direct observation versus diagnostic:** Printed positive table inequality and negative labelled region are direct source observations. Interpreting the plotted magnitude as exactly2.75 is diagnostic only.
**Alternative source-grounded interpretations:** The table may use an efficacy-oriented Z and the figure may use a treatment-risk-oriented Z. That can reconcile the intended design, but neither the table nor figure declares this sign reversal. A nonnegative absolute statistic would require a distinct labelled convention because the figure is explicitly signed.
**Named uncertainty and human question:** Are the table and figure meant to use the same signed Z? If different, what are the two contrast/sign definitions? Review the source generating table and plot rather than assume high-minus-low or low-minus-high.
**Quality-control relevance:** Sign conventions can affect extraction of efficacy versus harm boundaries. No conclusion about the actual trial decision follows because no observed stopping Z path is supplied.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z≥+2.75 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look1 N956, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail?

## C105 — Efficacy boundary has opposite signed direction in table and figure

**Candidate statement:** Efficacy boundary has opposite signed direction in table and figure; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Statistical reporting inconsistency
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN protocol monitoring table look2 versus PLAN protocol boundary figure at enrollment1434; PLAN amendment and REPORT supplement repeated graphic corroborate
**Review domain:** plan_material
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.
**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.
**Checker provenance:** checkers/parts/statistical_pass_1_planplots.md :: PP-Z2

**S relationship:** S278.
**Compared locations and document roles:** [DOC-002 PDF p.22](../../../joi190055supp1_prod_16092.pdf#page=22), PLAN, statistical-analysis table, look2 efficacy; [DOC-002 PDF p.23](../../../joi190055supp1_prod_16092.pdf#page=23), PLAN, stopping-boundary figure, Efficacy region at enrollment1434. [DOC-005 PDF p.31](../../../joi190055supp4_prod_16092.pdf#page=31), REPORT, reproduces the negative-Z efficacy graphical orientation and corroborates the figure side; [DOC-003 PDF p.3](../../../joi190055supp2_prod_16092.pdf#page=3), PLAN, amendment explicitly introduces the same table/figure but adds no signed contrast definition. The REPORT location corroborates rather than creates an additional discrepancy.
**Printed evidence:** The table calls the look2 efficacy boundary Z≥2.432. The plotted region labelled Efficacy lies below zero and its corresponding outer boundary is at a negative ordinate. Harm lies above zero. Exact graphical ordinate coordinates are not independently printed; the sign is directly visible.
**Rule and calculation:** If these are the same signed statistic, Z≥+2.432 and an efficacy region Z≤−2.432 are opposite directions. The negative boundary magnitude is a graphical alignment to the table, not a new exact numeric transcription. No P-tail reconstruction is required.
**Direct observation versus diagnostic:** Printed positive table inequality and negative labelled region are direct source observations. Interpreting the plotted magnitude as exactly2.432 is diagnostic only.
**Alternative source-grounded interpretations:** The table may use an efficacy-oriented Z and the figure may use a treatment-risk-oriented Z. That can reconcile the intended design, but neither the table nor figure declares this sign reversal. A nonnegative absolute statistic would require a distinct labelled convention because the figure is explicitly signed.
**Named uncertainty and human question:** Are the table and figure meant to use the same signed Z? If different, what are the two contrast/sign definitions? Review the source generating table and plot rather than assume high-minus-low or low-minus-high.
**Quality-control relevance:** Sign conventions can affect extraction of efficacy versus harm boundaries. No conclusion about the actual trial decision follows because no observed stopping Z path is supplied.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z≥+2.432 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look2 N1434, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail?

## C106 — Efficacy boundary has opposite signed direction in table and figure

**Candidate statement:** Efficacy boundary has opposite signed direction in table and figure; the compared display or definition requires human reconciliation under the stated rule.
**Category:** Statistical reporting inconsistency
**Relationship type:** P_P
**All relationships:** P_P
**Compared document roles:** PLAN protocol monitoring table look3 versus PLAN protocol boundary figure at enrollment1912; PLAN amendment and REPORT supplement repeated graphic corroborate
**Review domain:** plan_material
**Evidence state:** recorded_candidate
**Suggested review disposition:** retain
**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.
**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.
**Checker provenance:** checkers/parts/statistical_pass_1_planplots.md :: PP-Z3

**S relationship:** S280.
**Compared locations and document roles:** [DOC-002 PDF p.22](../../../joi190055supp1_prod_16092.pdf#page=22), PLAN, statistical-analysis table, look3 efficacy; [DOC-002 PDF p.23](../../../joi190055supp1_prod_16092.pdf#page=23), PLAN, stopping-boundary figure, Efficacy region at enrollment1912. [DOC-005 PDF p.31](../../../joi190055supp4_prod_16092.pdf#page=31), REPORT, reproduces the negative-Z efficacy graphical orientation and corroborates the figure side; [DOC-003 PDF p.3](../../../joi190055supp2_prod_16092.pdf#page=3), PLAN, amendment explicitly introduces the same table/figure but adds no signed contrast definition. The REPORT location corroborates rather than creates an additional discrepancy.
**Printed evidence:** The table calls the look3 efficacy boundary Z≥2.012. The plotted region labelled Efficacy lies below zero and its corresponding outer boundary is at a negative ordinate. Harm lies above zero. Exact graphical ordinate coordinates are not independently printed; the sign is directly visible.
**Rule and calculation:** If these are the same signed statistic, Z≥+2.012 and an efficacy region Z≤−2.012 are opposite directions. The negative boundary magnitude is a graphical alignment to the table, not a new exact numeric transcription. No P-tail reconstruction is required.
**Direct observation versus diagnostic:** Printed positive table inequality and negative labelled region are direct source observations. Interpreting the plotted magnitude as exactly2.012 is diagnostic only.
**Alternative source-grounded interpretations:** The table may use an efficacy-oriented Z and the figure may use a treatment-risk-oriented Z. That can reconcile the intended design, but neither the table nor figure declares this sign reversal. A nonnegative absolute statistic would require a distinct labelled convention because the figure is explicitly signed.
**Named uncertainty and human question:** Are the table and figure meant to use the same signed Z? If different, what are the two contrast/sign definitions? Review the source generating table and plot rather than assume high-minus-low or low-minus-high.
**Quality-control relevance:** Sign conventions can affect extraction of efficacy versus harm boundaries. No conclusion about the actual trial decision follows because no observed stopping Z path is supplied.

**Neutral quality-control scope:** This is a source-grounded reporting consistency question. An extractor could copy the reported number or label; no propagation or conclusion change is asserted.
**Human review status:** Pending Human Adjudication.

### Mechanical evidence recheck update

The original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.


- Determining fact/state: recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z≥+2.012 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value. Classification P_P; all P_P; plan_material; no role/type code correction.
- Missing definition and human question: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look3 N1912, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail?

