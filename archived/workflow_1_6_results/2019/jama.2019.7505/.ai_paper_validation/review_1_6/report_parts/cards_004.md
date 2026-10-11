## C082 — conditional thoracic VAS mean/SD bound

Pending Human Adjudication.

**Candidate statement:** Conditional on zero-origin 0–10 cm scores on the same postoperative VAS, the low-PEEP Day 2 thoracic mean/SD tuple exceeds the bounded-support moment limit even after rounding. A 10 cm line length alone does not establish those endpoints or the postoperative scale identity.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** REPORT supplement eTable 7 thoracic summary versus PLAN protocol VAS scale/assessment

**Review domain:** protocol_report

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** The reported completed-trial summary is REPORT and the prospective measurement definition is PLAN; the substantive conditional scale comparison is P_R.

**Classification ambiguity:** P_R is conditional scale-to-report comparison; numerical endpoints and postoperative identity are not printed.

**Exact source locations:**

- [joi190055supp4_prod_16092.pdf results supplement, physical PDF p.28](../../../joi190055supp4_prod_16092.pdf#page=28), eTable 7, VAS thoracic – cm, mean (SD), No., Day 2, low PEEP cell: REPORT.
- [joi190055supp1_prod_16092.pdf protocol, physical PDF p.17](../../../joi190055supp1_prod_16092.pdf#page=17), printed protocol p.16, version 2.6, actual organ function evaluation bullet defining “Visual Analogue Scale (10 cm): evaluation for dyspnea, thoracic and abdominal rest and incident pain”: PLAN.
- [joi190055supp1_prod_16092.pdf protocol, physical PDF p.20](../../../joi190055supp1_prod_16092.pdf#page=20), printed protocol p.19, postoperative assessment continuation bullet “VAS evaluation for dyspnea, thoracic and abdominal rest and incident pain”: PLAN.

**Source evidence:** eTable 7 low PEEP day-2 thoracic VAS mean 1.4 cm, SD 3.9 cm, n = 841; high PEEP mean 1.3 cm, SD 0.8 cm, n = 838; P = .34. Arm headings are high989 and low987. The protocol specifies a 10 cm VAS for the same named symptoms and repeats the assessment postoperatively. It does not explicitly print the numerical scoring endpoints or a normalization rule.

**Reported-versus-comparator:** eTable 7 low PEEP day-2 thoracic VAS mean 1.4 cm, SD 3.9 cm, n = 841; high PEEP mean 1.3 cm, SD 0.8 cm, n = 838; P = .34. Arm headings are high989 and low987. The protocol specifies a 10 cm VAS for the same named symptoms and repeats the assessment postoperatively. It does not explicitly print the numerical scoring endpoints or a normalization rule. 

**Reasoning procedure:** The mean, SD, n, cm unit, mean(SD) header and protocol 10 cm scale wording are direct source observations. The numerical 0–10 support and zero-origin scoring convention are explicitly conditional inferences from that supplied line-length and cm-unit description. They are not independently printed endpoints. Protocol p.17 describes baseline organ-function assessment; p.20 repeats the same named VAS postoperatively but does not restate its length. Applying the 10 cm definition to eTable 7 is an identity question retained for human review. Numerical scoring origin/endpoints, postoperative identity with the baseline-defined scale, transformation and SD convention. Human question: Were postoperative thoracic scores zero-origin 0–10 cm scores on the protocol line, and does the low Day 2 tuple correctly read mean1.4, SD3.9, n841; if different, what origin/range/transformation was used?

**Calculation:** Conditional on the reported cm scores being distance along the supplied 10 cm line, measured from a zero origin and bounded 0–10 cm, any sample with mean m and sample SD s obeys s² ≤ n/(n−1) × m × (10−m). At the printed mean, the maximum sample SD is sqrt(841/840 × 1.4 × 8.6) = 3.47194 cm, below 3.9 cm. With rounding admitted, m can range from 1.35 to 1.45; the largest permitted bound on that interval is sqrt(841/840 × 1.45 × 8.55) = 3.52310 cm. The printed SD interval begins at 3.85 cm. Thus even the most permissive rounding leaves a gap of at least 3.85 − 3.52310 = 0.32690 cm. Display tolerance: Mean/SD displayed to one decimal permit ±0.05 cm; n = 841 is exact. The n/(n−1) factor allows the usual sample SD convention and is slightly more permissive than population SD. This calculation is a moment bound, not a reconstructed P value.

**Alternative source-grounded interpretations:** A transformed or shifted scoring convention, a differently normalized postoperative scale, a larger allowed range, a different underlying statistic despite the mean(SD) label, or a transcription error could explain the display. Without zero origin, a line of length10 alone permits SD up to about5.00 cm and does not establish the mean-dependent contradiction. An alternative 0-based scale would need an upper endpoint at least11.66026 cm even with the rounding allowances, to accommodate the minimum printed SD3.85 at mean1.45. No external VAS convention is used.

**Mechanical evidence recheck:** recorded_candidate. Direct source confirms the tuple and 10 cm plan description; the registered bounded-support question remains conditional on its explicitly missing origin/scale identity. Diagnostic: At m1.4,n841, maximum SD=3.47194. Allowing mean rounding up to1.45 gives 3.52310, below minimum rounding-consistent SD3.85 by 0.32690 cm. Classification P_R; all P_R; protocol_report; no role/type code correction. Necessary missing inputs: Numerical scoring origin/endpoints, postoperative identity with the baseline-defined scale, transformation and SD convention. Human question: Were postoperative thoracic scores zero-origin 0–10 cm scores on the protocol line, and does the low Day 2 tuple correctly read mean1.4, SD3.9, n841; if different, what origin/range/transformation was used? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** The reported dispersion may be reused as a summary SD in quantitative evidence synthesis. The candidate is confined to the consistency of that reported summary with the supplied scale definition; it is not a raw-data or clinical plausibility audit.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the thoracic VAS SD into a quantitative synthesis. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: “Were the postoperative thoracic VAS scores in eTable 7 recorded as 0–10 cm distance scores on the protocol’s 10 cm scale, and does the low-PEEP Day 2 cell correctly report mean 1.4 cm, SD 3.9 cm and n = 841; if a different origin, range or transformation was used, what was it?” Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C083 — conditional event-count mean versus component total

Pending Human Adjudication.

**Candidate statement:** The high-arm count summary 0.35 differs from the nearest-rounded mean 353/989 = 0.36 only if the unlabeled first statistic is the mean of the same twelve component indicators in the displayed population. The summary statistic, aggregation and realized denominator are not supplied; randomized denominators provide a coherent alternative.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT supplement eTable 9 count summary versus REPORT main Table 3 component numerators; REPORT main randomized denominator is an alternative; PLAN SAP count definition corroborates

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** First summary and realized count aggregation are not explicitly defined. SAP corroborates count concept without a P_R discrepancy.

**Exact source locations:**

- [joi190055supp4_prod_16092.pdf results supplement, physical PDF p.30](../../../joi190055supp4_prod_16092.pdf#page=30), eTable 9, Sensitivity analysis for the primary outcome, Count events row, high/low summary cells and n = 989/987 headings: REPORT.
- [jama_bluth_2019_oi_190055_16092.pdf main article, physical PDF p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), printed p.2300, Table 3, all 12 Components of the Primary Outcome, high/low No. of Events columns and n = 989/987 headings: REPORT.
- DOC-005 p.30 model footnotes referring to all12 components are corroborative REPORT context, not a new discrepancy relationship.
- [jama_bluth_2019_oi_190055_16092.pdf main article, physical PDF p.3](../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), Figure 1 randomized high 1011/low 1002, REPORT: source-grounded alternative denominator, not an additional discrepancy relationship. Corroborative PLAN count-definition context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3), sensitivity-analysis paragraph.

**Source evidence:** eTable 9 Count events row gives high0.35 (0.88), low0.38 (0.86), above separately labeled Median (IQR)0 (0–0) for both arms. The Count events row does not explicitly say mean(SD). Main Table 3 high component counts, in its printed order, are mild135, moderate42, severe30, atelectasis44, pleural effusion43, new infiltrates14, cardiopulmonary edema17, bronchospasm12, pulmonary infection10, aspiration2, ARDS3, pneumothorax1. Low counts in the same order are154,58,36,55,21,18,9,10,10,1,1,3.

**Reported-versus-comparator:** eTable 9 Count events row gives high0.35 (0.88), low0.38 (0.86), above separately labeled Median (IQR)0 (0–0) for both arms. The Count events row does not explicitly say mean(SD). Main Table 3 high component counts, in its printed order, are mild135, moderate42, severe30, atelectasis44, pleural effusion43, new infiltrates14, cardiopulmonary edema17, bronchospasm12, pulmonary infection10, aspiration2, ARDS3, pneumothorax1. Low counts in the same order are154,58,36,55,21,18,9,10,10,1,1,3. 

**Reasoning procedure:** Direct images confirm all12 main component counts, populations, and the eTable 9 summary0.35 (0.88). The arithmetic sum and conditional mean identity are derived. Interpreting the unlabeled first summary as mean(SD), and interpreting “Count events” as counting each of the same12 binary components, are named inferences rather than printed definitions. First summary statistic label, actual event grouping/time rule, analysis n, missing-participant treatment and rounding convention. Human question: Is 0.35(0.88) the mean(SD) of these twelve component counts among989 high participants; if so how does353/989 reconcile, and otherwise what statistic/grouping/window/denominator and participant handling define it?

**Calculation:** Conditional on “Count events” summary0.35/0.38 being the arithmetic mean of the number of these same12 binary components per participant in the displayed full-arm populations, the mean must equal the sum of all component numerators divided by n. Overlap between components does not defeat this identity; each counted component contributes separately. High sum135 + 42 + 30 + 44 + 43 + 14 + 17 + 12 + 10 + 2 + 3 + 1 = 353; 353 / 989 = 0.356926, which rounds to0.36. Low sum154 + 58 + 36 + 55 + 21 + 18 + 9 + 10 + 10 + 1 + 1 + 3 = 376; 376 / 987 = 0.380952, which rounds to0.38 and reconciles. Display tolerance: At two-decimal rounding,0.35 ordinarily implies a mean in [0.345,0.355), hence a total in [341.205,351.095) at n989; integer totals compatible with that interval are342–351. The printed component total353 exceeds the largest compatible integer total by2. The exact mean exceeds the upper rounding boundary0.355 by0.001926. Counts and denominator have zero tolerance. The low-arm summary is within its rounding interval.

**Alternative source-grounded interpretations:** The summary may use a different statistic, component grouping (for example collapsing multiple respiratory-failure severities to one event), time rule, population, event definition, weighting or complete-case denominator. Main Figure 1 supplies randomized high 1011/low 1002: 353/1011 = 0.349159 and 376/1002 = 0.375250, which round to 0.35/0.38. Thus a count calculation using all randomized participants could explain both summary means, but that denominator differs from eTable 9 headings 989/987 and requires the population and missing-participant handling to be named. This is an arithmetic alternative, not proof that the authors used it. Truncation rather than rounding would also produce 0.35 from 0.356926 but is not stated. Different component overlap is not by itself an explanation if the count is the sum of those same 12 indicators; alternative grouping would change the count definition and should be specified.

**Mechanical evidence recheck:** recorded_candidate. Count tuple and component totals are confirmed; arithmetic reproduces the registered conditional high-arm rounding question. Diagnostic: High sum353;353/989=0.356926→0.36, versus0.35. Low sum376;376/987=0.380952→0.38. High two-decimal0.35 permits integer totals342–351 under ordinary rounding. Alternative353/1011=0.349159→0.35 and376/1002=0.375250→0.38. Classification S_C; all S_C; statistical_results; no role/type code correction. Necessary missing inputs: First summary statistic label, actual event grouping/time rule, analysis n, missing-participant treatment and rounding convention. Human question: Is 0.35(0.88) the mean(SD) of these twelve component counts among989 high participants; if so how does353/989 reconcile, and otherwise what statistic/grouping/window/denominator and participant handling define it? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Event burden means and their dispersions can be extracted separately from binary-composite risks; a missing aggregation definition or mismatched displayed mean can lead to an incorrect extracted endpoint. No claim about treatment effect or conclusion follows.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the count-burden summary with the wrong statistic or population. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: “Is 0.35 (0.88) in the high-PEEP Count events row the mean (SD) of the count of the same 12 primary-outcome components reported in main Table 3 among 989 participants; if so, how does it reconcile with 353 component occurrences and 353/989 = 0.356926, and if not, what statistic, grouping, time rule and denominator does it represent?” Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C084 — Conditional follow-up/time-origin reconciliation question — eFigure8

Pending Human Adjudication.

**Candidate statement:** The median follow-up and day-five risk counts require reconciliation only under an assumed common time origin and follow-up convention; the missing definitions prevent an unconditional incompatibility claim.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT supplement eFigure 8 PPC caption versus same-page risk table

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.

**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.

**Exact source locations:** [joi190055supp4_prod_16092.pdf — physical PDF p. 38](../../../joi190055supp4_prod_16092.pdf#page=38), eFigure 8 PPC, caption median follow-up and same-page baseline/day-5 risk-table cells (REPORT). This card concerns this endpoint alone.

**Source evidence:** The caption prints median follow-up 4 (2–5) days. Baseline high/low risk counts are 989/987 (total 1976); at day 5 they are 785/756 (total 1541).

**Reported-versus-comparator:** The day-5 risk total 1541 is compared with the conditional upper count 988 beyond four elapsed days if the caption is an ordinary median of the same observed follow-up variable on the same time origin.

**Reasoning procedure:** The caption and risk cells are direct observations. The order-statistic comparison is derived and conditional: caption follow-up, risk-table time, origin and inclusive-day convention must identify the same observed-time variable. Without that mapping, incompatibility is not established.

**Calculation:** 1976 / 2 = 988; 785 + 756 = 1541; 1541 − 988 = 553. Under the shared elapsed-time interpretation, a median of four days cannot coexist with more than half observed beyond day 4. Counts are exact; ordinary integer rounding of median 4 remains below 4.5 elapsed days. This diagnostic does not apply unchanged if postoperative day 5 corresponds to four elapsed days.

**Alternative source-grounded interpretations:** Inclusive postoperative numbering may label four elapsed days as day 5. The caption may summarize assessment duration while endpoint ascertainment continues, or may use a different follow-up statistic. The risk table may use a different removal rule. The caption statistic, origin/inclusiveness, assessment-versus-ascertainment mapping, and endpoint-specific event/censor/risk definitions are missing. No patient-level trajectory is reconstructed.

**Mechanical evidence recheck:** recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1541 exceeds988 by553. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction. Necessary missing inputs: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 8 PPC, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Time-dependent denominators and follow-up summaries could be reused under incompatible definitions.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the follow-up duration or time-dependent risk denominator into an endpoint summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open eFigure 8 on physical PDF p. 38; confirm the caption and baseline/day-5 risk cells. Ask which variable and calculation define median 4 (2–5), what time origin and inclusive convention define day 5, and which endpoint-specific events or censoring remove patients. Determine whether caption and risk-table times refer to the same observed-time summary before applying the conditional bound. Record the assessment below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C085 — Conditional follow-up/time-origin reconciliation question — eFigure9

Pending Human Adjudication.

**Candidate statement:** The median follow-up and day-five risk counts require reconciliation only under an assumed common time origin and follow-up convention; the missing definitions prevent an unconditional incompatibility claim.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT supplement eFigure 9 severe PPC caption versus same-page risk table

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.

**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.

**Exact source locations:** [joi190055supp4_prod_16092.pdf — physical PDF p. 39](../../../joi190055supp4_prod_16092.pdf#page=39), eFigure 9 severe PPC, caption median follow-up and same-page baseline/day-5 risk-table cells (REPORT). This card concerns this endpoint alone.

**Source evidence:** The caption prints median follow-up 4 (2–5) days. Baseline high/low risk counts are 989/987 (total 1976); at day 5 they are 785/756 (total 1541).

**Reported-versus-comparator:** The day-5 risk total 1541 is compared with the conditional upper count 988 beyond four elapsed days if the caption is an ordinary median of the same observed follow-up variable on the same time origin.

**Reasoning procedure:** The caption and risk cells are direct observations. The order-statistic comparison is derived and conditional: caption follow-up, risk-table time, origin and inclusive-day convention must identify the same observed-time variable. Without that mapping, incompatibility is not established.

**Calculation:** 1976 / 2 = 988; 785 + 756 = 1541; 1541 − 988 = 553. Under the shared elapsed-time interpretation, a median of four days cannot coexist with more than half observed beyond day 4. Counts are exact; ordinary integer rounding of median 4 remains below 4.5 elapsed days. This diagnostic does not apply unchanged if postoperative day 5 corresponds to four elapsed days.

**Alternative source-grounded interpretations:** Inclusive postoperative numbering may label four elapsed days as day 5. The caption may summarize assessment duration while endpoint ascertainment continues, or may use a different follow-up statistic. The risk table may use a different removal rule. The caption statistic, origin/inclusiveness, assessment-versus-ascertainment mapping, and endpoint-specific event/censor/risk definitions are missing. No patient-level trajectory is reconstructed.

**Mechanical evidence recheck:** recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1541 exceeds988 by553. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction. Necessary missing inputs: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 9 severe PPC, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Time-dependent denominators and follow-up summaries could be reused under incompatible definitions.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the follow-up duration or time-dependent risk denominator into an endpoint summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open eFigure 9 on physical PDF p. 39; confirm the caption and baseline/day-5 risk cells. Ask which variable and calculation define median 4 (2–5), what time origin and inclusive convention define day 5, and which endpoint-specific events or censoring remove patients. Determine whether caption and risk-table times refer to the same observed-time summary before applying the conditional bound. Record the assessment below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C086 — Conditional follow-up/time-origin reconciliation question — eFigure10

Pending Human Adjudication.

**Candidate statement:** The median follow-up and day-five risk counts require reconciliation only under an assumed common time origin and follow-up convention; the missing definitions prevent an unconditional incompatibility claim.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT supplement eFigure 10 extrapulmonary caption versus same-page risk table

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.

**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.

**Exact source locations:** [joi190055supp4_prod_16092.pdf — physical PDF p. 40](../../../joi190055supp4_prod_16092.pdf#page=40), eFigure 10 extrapulmonary complications, caption median follow-up and same-page baseline/day-5 risk-table cells (REPORT). This card concerns this endpoint alone.

**Source evidence:** The caption prints median follow-up 4 (2–5) days. Baseline high/low risk counts are 989/987 (total 1976); at day 5 they are 828/845 (total 1673).

**Reported-versus-comparator:** The day-5 risk total 1673 is compared with the conditional upper count 988 beyond four elapsed days if the caption is an ordinary median of the same observed follow-up variable on the same time origin.

**Reasoning procedure:** The caption and risk cells are direct observations. The order-statistic comparison is derived and conditional: caption follow-up, risk-table time, origin and inclusive-day convention must identify the same observed-time variable. Without that mapping, incompatibility is not established.

**Calculation:** 1976 / 2 = 988; 828 + 845 = 1673; 1673 − 988 = 685. Under the shared elapsed-time interpretation, a median of four days cannot coexist with more than half observed beyond day 4. Counts are exact; ordinary integer rounding of median 4 remains below 4.5 elapsed days. This diagnostic does not apply unchanged if postoperative day 5 corresponds to four elapsed days.

**Alternative source-grounded interpretations:** Inclusive postoperative numbering may label four elapsed days as day 5. The caption may summarize assessment duration while endpoint ascertainment continues, or may use a different follow-up statistic. The risk table may use a different removal rule. The caption statistic, origin/inclusiveness, assessment-versus-ascertainment mapping, and endpoint-specific event/censor/risk definitions are missing. No patient-level trajectory is reconstructed.

**Mechanical evidence recheck:** recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1673 exceeds988 by685. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction. Necessary missing inputs: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 10 extrapulmonary, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Time-dependent denominators and follow-up summaries could be reused under incompatible definitions.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the follow-up duration or time-dependent risk denominator into an endpoint summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open eFigure 10 on physical PDF p. 40; confirm the caption and baseline/day-5 risk cells. Ask which variable and calculation define median 4 (2–5), what time origin and inclusive convention define day 5, and which endpoint-specific events or censoring remove patients. Determine whether caption and risk-table times refer to the same observed-time summary before applying the conditional bound. Record the assessment below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C087 — Conditional follow-up/time-origin reconciliation question — eFigure11

Pending Human Adjudication.

**Candidate statement:** The median follow-up and day-five risk counts require reconciliation only under an assumed common time origin and follow-up convention; the missing definitions prevent an unconditional incompatibility claim.

**Category:** Denominator, proportion, or total inconsistency

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT supplement eFigure 11 mortality caption versus same-page risk table

**Review domain:** statistical_results

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary discrepancy locations are completed-trial content within one REPORT document, so S_W applies. Corroborating documents do not add a discrepancy relationship.

**Classification ambiguity:** Caption and risk-table times may use different inclusive origins or assessment summaries; no raw follow-up reconstruction is possible.

**Exact source locations:** [joi190055supp4_prod_16092.pdf — physical PDF p. 41](../../../joi190055supp4_prod_16092.pdf#page=41), eFigure 11 mortality, caption median follow-up and same-page baseline/day-5 risk-table cells (REPORT). This card concerns this endpoint alone.

**Source evidence:** The caption prints median follow-up 4 (2–5) days. Baseline high/low risk counts are 989/987 (total 1976); at day 5 they are 985/986 (total 1971).

**Reported-versus-comparator:** The day-5 risk total 1971 is compared with the conditional upper count 988 beyond four elapsed days if the caption is an ordinary median of the same observed follow-up variable on the same time origin.

**Reasoning procedure:** The caption and risk cells are direct observations. The order-statistic comparison is derived and conditional: caption follow-up, risk-table time, origin and inclusive-day convention must identify the same observed-time variable. Without that mapping, incompatibility is not established.

**Calculation:** 1976 / 2 = 988; 985 + 986 = 1971; 1971 − 988 = 983. Under the shared elapsed-time interpretation, a median of four days cannot coexist with more than half observed beyond day 4. Counts are exact; ordinary integer rounding of median 4 remains below 4.5 elapsed days. This diagnostic does not apply unchanged if postoperative day 5 corresponds to four elapsed days.

**Alternative source-grounded interpretations:** Inclusive postoperative numbering may label four elapsed days as day 5. The caption may summarize assessment duration while endpoint ascertainment continues, or may use a different follow-up statistic. The risk table may use a different removal rule. The caption statistic, origin/inclusiveness, assessment-versus-ascertainment mapping, and endpoint-specific event/censor/risk definitions are missing. No patient-level trajectory is reconstructed.

**Mechanical evidence recheck:** recorded_candidate. Both cited displays are confirmed; registered conditional time-definition question remains, and the missing definition prevents an unconditional incompatibility claim. Diagnostic: 1976/2=988; day-five total1971 exceeds988 by983. This is a conditional order-statistic diagnostic; inclusive postoperative day numbering can map four elapsed days to day5. Classification S_W; all S_W; statistical_results; no role/type code correction. Necessary missing inputs: Caption variable and calculation (ordinary or another follow-up summary), origin, inclusive-day convention, risk-time mapping and whether assessment duration differs from endpoint ascertainment. Human question: For eFigure 11 mortality, what variable/origin/inclusiveness defines median4(2–5), what time is day5 in the risk table, and are both the same observed-time summary? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Time-dependent denominators and follow-up summaries could be reused under incompatible definitions.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the follow-up duration or time-dependent risk denominator into an endpoint summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open eFigure 11 on physical PDF p. 41; confirm the caption and baseline/day-5 risk cells. Ask which variable and calculation define median 4 (2–5), what time origin and inclusive convention define day 5, and which endpoint-specific events or censoring remove patients. Determine whether caption and risk-table times refer to the same observed-time summary before applying the conditional bound. Record the assessment below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C088 — Mild respiratory failure: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Mild respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR0.92[0.76,1.12],99.58%CI; matched main events high135/989,low154/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR0.92[0.76,1.12],99.58%CI; matched main events high135/989,low154/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(135/989)/(154/987)=0.874851. Printed 0.92 differs by0.045149. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (135/989)/(154/987)=0.874851; absolute distance from0.92=0.045149, larger than .005. Interval is positive, ordered and contains its printed point (0.76≤0.92≤1.12). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Mild respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.92, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Mild respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.92, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C089 — Moderate respiratory failure: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Moderate respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR0.83[0.59,1.17],99.58%CI; matched main events high42/989,low58/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR0.83[0.59,1.17],99.58%CI; matched main events high42/989,low58/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(42/989)/(58/987)=0.722674. Printed 0.83 differs by0.107326. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (42/989)/(58/987)=0.722674; absolute distance from0.83=0.107326, larger than .005. Interval is positive, ordered and contains its printed point (0.59≤0.83≤1.17). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Moderate respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.83, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Moderate respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.83, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C090 — Severe respiratory failure: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Severe respiratory failure row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR0.91[0.61,1.34],99.58%CI; matched main events high30/989,low36/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR0.91[0.61,1.34],99.58%CI; matched main events high30/989,low36/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(30/989)/(36/987)=0.831648. Printed 0.91 differs by0.078352. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (30/989)/(36/987)=0.831648; absolute distance from0.91=0.078352, larger than .005. Interval is positive, ordered and contains its printed point (0.61≤0.91≤1.34). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Severe respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.91, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Severe respiratory failure, what realized GLM/link/contrast/adjustment/population produced0.91, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C091 — Aspiration: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Aspiration row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR1.33[0.41,4.30],99.58%CI; matched main events high2/989,low1/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR1.33[0.41,4.30],99.58%CI; matched main events high2/989,low1/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(2/989)/(1/987)=1.995956. Printed 1.33 differs by0.665956. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (2/989)/(1/987)=1.995956; absolute distance from1.33=0.665956, larger than .005. Interval is positive, ordered and contains its printed point (0.41≤1.33≤4.30). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Aspiration, what realized GLM/link/contrast/adjustment/population produced1.33, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Aspiration, what realized GLM/link/contrast/adjustment/population produced1.33, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C092 — Bronchospasm: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Bronchospasm row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR1.09[0.62,1.91],99.58%CI; matched main events high12/989,low10/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR1.09[0.62,1.91],99.58%CI; matched main events high12/989,low10/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(12/989)/(10/987)=1.197573. Printed 1.09 differs by0.107573. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (12/989)/(10/987)=1.197573; absolute distance from1.09=0.107573, larger than .005. Interval is positive, ordered and contains its printed point (0.62≤1.09≤1.91). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Bronchospasm, what realized GLM/link/contrast/adjustment/population produced1.09, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Bronchospasm, what realized GLM/link/contrast/adjustment/population produced1.09, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C093 — ARDS: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 ARDS row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR1.50[0.65,3.44],99.58%CI; matched main events high3/989,low1/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR1.50[0.65,3.44],99.58%CI; matched main events high3/989,low1/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(3/989)/(1/987)=2.993933. Printed 1.50 differs by1.493933. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (3/989)/(1/987)=2.993933; absolute distance from1.50=1.493933, larger than .005. Interval is positive, ordered and contains its printed point (0.65≤1.50≤3.44). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For ARDS, what realized GLM/link/contrast/adjustment/population produced1.50, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For ARDS, what realized GLM/link/contrast/adjustment/population produced1.50, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C094 — Atelectasis: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Atelectasis row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR0.88[0.64,1.23],99.58%CI; matched main events high44/989,low55/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR0.88[0.64,1.23],99.58%CI; matched main events high44/989,low55/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(44/989)/(55/987)=0.798382. Printed 0.88 differs by0.081618. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (44/989)/(55/987)=0.798382; absolute distance from0.88=0.081618, larger than .005. Interval is positive, ordered and contains its printed point (0.64≤0.88≤1.23). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Atelectasis, what realized GLM/link/contrast/adjustment/population produced0.88, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Atelectasis, what realized GLM/link/contrast/adjustment/population produced0.88, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C095 — Cardiopulmonary edema: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Cardiopulmonary edema row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR1.31[0.87,1.98],99.58%CI; matched main events high17/989,low9/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR1.31[0.87,1.98],99.58%CI; matched main events high17/989,low9/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(17/989)/(9/987)=1.885069. Printed 1.31 differs by0.575069. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (17/989)/(9/987)=1.885069; absolute distance from1.31=0.575069, larger than .005. Interval is positive, ordered and contains its printed point (0.87≤1.31≤1.98). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Cardiopulmonary edema, what realized GLM/link/contrast/adjustment/population produced1.31, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Cardiopulmonary edema, what realized GLM/link/contrast/adjustment/population produced1.31, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C096 — Pleural effusion: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pleural effusion row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR1.36[1.05,1.76],99.58%CI; matched main events high43/989,low21/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR1.36[1.05,1.76],99.58%CI; matched main events high43/989,low21/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(43/989)/(21/987)=2.043478. Printed 1.36 differs by0.683478. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (43/989)/(21/987)=2.043478; absolute distance from1.36=0.683478, larger than .005. Interval is positive, ordered and contains its printed point (1.05≤1.36≤1.76). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Pleural effusion, what realized GLM/link/contrast/adjustment/population produced1.36, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Pleural effusion, what realized GLM/link/contrast/adjustment/population produced1.36, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C097 — Pneumothorax: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pneumothorax row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR0.50[0.04,5.96],99.58%CI; matched main events high1/989,low3/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR0.50[0.04,5.96],99.58%CI; matched main events high1/989,low3/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(1/989)/(3/987)=0.332659. Printed 0.50 differs by0.167341. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (1/989)/(3/987)=0.332659; absolute distance from0.50=0.167341, larger than .005. Interval is positive, ordered and contains its printed point (0.04≤0.50≤5.96). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Pneumothorax, what realized GLM/link/contrast/adjustment/population produced0.50, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Pneumothorax, what realized GLM/link/contrast/adjustment/population produced0.50, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C098 — Pulmonary infiltrates: modeled-versus-crude comparator input error

Pending Human Adjudication.

**Candidate statement:** This retained record has evidence state record_input_error: its original comparator equated a planned GLM sensitivity estimate with a crude arm risk ratio without a supplied equivalence rule.

**Category:** Measure, label, or scale inconsistency

**Relationship type:** S_C

**All relationships:** S_C

**Compared document roles:** REPORT results supplement eFigure 12 component sensitivity estimate versus REPORT main Table 3 event counts/footnote; PLAN final SAP specifies sensitivity GLM and corroborates context

**Review domain:** report_internal_inconsistency

**Evidence state:** record_input_error

**Suggested review disposition:** discuss

**Classification rationale:** Completed-trial article and non-plan results supplement are REPORT content. The registered primary comparison crosses these REPORT documents; any PLAN context corroborates and creates no P_R.

**Classification ambiguity:** Registered cross-REPORT relation retained; missing estimator/population alignment is explicit. PLAN specifies model context and corroborates, creating no P_R discrepancy.

**Exact source locations:** [joi190055supp4_prod_16092.pdf, PDF p. 42](../../../joi190055supp4_prod_16092.pdf#page=42) eFigure12 Pulmonary infiltrates row and “Risk Ratio (99.58% CI)” header, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9) Table3 matched component row and n989/n987, REPORT; [jama_bluth_2019_oi_190055_16092.pdf, PDF p. 10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10) footnote b, REPORT. Corroborative PLAN context: [joi190055supp3_prod_16092.pdf — physical PDF p. 3](../../../joi190055supp3_prod_16092.pdf#page=3), sensitivity analysis specifying individual-component generalized linear models and Bonferroni confidence intervals.

**Source evidence:** Forest RR0.87[0.49,1.55],99.58%CI; matched main events high14/989,low18/987. The SAP explicitly specifies a GLM sensitivity analysis; the realized link, formula, adjustment/standardization, event and contrast coding, population and estimator output are not supplied.

**Reported-versus-comparator:** Original registered comparison, retained as history: Forest RR0.87[0.49,1.55],99.58%CI; matched main events high14/989,low18/987. The comparator is the crude ratio of these main-table risks; its identity with the sensitivity estimate is an unsupported premise.

**Reasoning procedure:** The forest tuple, risk-ratio header and main event counts are direct observations. The SAP independently identifies a planned sensitivity GLM. Calculate the crude ratio only as a diagnostic; matching endpoint names does not establish the same model, estimand or population. The original registration assumed that equivalence without a supplied rule, so this is record_input_error rather than an established contradiction of the fitted estimate.

**Calculation:** Historical conditional crude diagnostic: Under an explicitly crude arm-risk definition RR=(high events/high n)/(low events/low n)=(14/989)/(18/987)=0.776205. Printed 0.87 differs by0.093795. All CIs are ordered, positive and contain their printed point estimates. The99.58% interval adjustment changes coverage, not the arithmetic definition of marginal RR. Estimate rounding ±.005; exact event integers and displayed arm denominators. The diagnostic difference exceeds.005. Confidence-level adjustment does not turn a fitted model estimate into a crude ratio; the arithmetic difference does not reproduce or disprove the GLM output.

**Alternative source-grounded interpretations:** A model-defined ratio, adjustment or probability standardization, different event/contrast coding, or a different realized analysis population may explain the difference. The supplied SAP provides the GLM context, but not the realized link/formula, adjustment, population, coding or output. A crude mismatch alone therefore does not establish a wrong estimate or label. Forest intervals are positive, ordered and contain the printed points; their display width or clipping is not a separate contradiction.

**Mechanical evidence recheck:** record_input_error. The registered mismatch requires unsupported identity between a separately planned GLM sensitivity estimate and the crude main-count ratio; no literal source states that identity and a residual label discrepancy cannot be settled. Diagnostic: (14/989)/(18/987)=0.776205; absolute distance from0.87=0.093795, larger than .005. Interval is positive, ordered and contains its printed point (0.49≤0.87≤1.55). This diagnostic does not reproduce a fitted GLM. Classification S_C; all S_C; report_internal_inconsistency; no role/type code correction. Necessary missing inputs: Sensitivity model link/formula, adjustment or standardization, event/contrast coding, realized analysis population/denominators and point-estimator output. Human question: For Pulmonary infiltrates, what realized GLM/link/contrast/adjustment/population produced0.87, and does its RR mean the crude main-arm ratio or a model-defined ratio? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (discuss) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** This stable record documents an unsupported estimator-alignment input in the original registration and the remaining estimand-definition question. Human review must distinguish a modeled sensitivity effect from a crude main-table risk ratio before extraction.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the modeled sensitivity estimate as a crude arm risk ratio. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Confirm the endpoint-specific forest tuple on supplement p. 42 and matched component counts on main p. 9, including footnote b on p. 10. Read the SAP sensitivity paragraph on p. 3. Ask For Pulmonary infiltrates, what realized GLM/link/contrast/adjustment/population produced0.87, and does its RR mean the crude main-arm ratio or a model-defined ratio? Obtain the realized model specification and output, then assess whether any like-for-like discrepancy remains. The mechanical discuss suggestion does not fill the human Action field.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C099 — Revised PLAN target versus retained procedural total

Pending Human Adjudication.

**Candidate statement:** The same protocol version explicitly revises the total to 2013 but retains a future-tense procedure statement of 748. The initial 748 is historical in section 6.4; whether section 7.2 intentionally retains historical wording requires human confirmation.

**Category:** Numeric or arithmetic inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol current procedure total versus PLAN protocol revised sample/recruitment target; PLAN amendment corroborates

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Historical intent of section7.2 is not stated; no REPORT comparator creates P_R.

**Exact source locations:** PLAN [joi190055supp1_prod_16092.pdf — physical PDF p. 10, printed p. 9](../../../joi190055supp1_prod_16092.pdf#page=10), current recruitment target; [physical PDF p. 11, printed p. 10](../../../joi190055supp1_prod_16092.pdf#page=11), version 2.6 section 6.4; [physical PDF p. 12, printed p. 11](../../../joi190055supp1_prod_16092.pdf#page=12), section 7.2. Corroborative PLAN [joi190055supp2_prod_16092.pdf — physical PDF p. 2](../../../joi190055supp2_prod_16092.pdf#page=2), revised sample target.

**Source evidence:** The current recruitment statement gives 2013. Section 6.4 explicitly distinguishes initial 748 from revised total 2013. Section 7.2 states, “In total,748 patients will be included.” The amendment corroborates the revised total.

**Reported-versus-comparator:** Section 7.2 future-tense total 748 versus the same version’s explicitly revised total 2013; the historical 748 in section 6.4 is not itself conflicting.

**Reasoning procedure:** Directly compare the same-version current-total statements and their historical qualifiers. The rule is identity of the intended current planned enrollment total, conditional on section 7.2 remaining an operative procedure. No REPORT conflict or actual enrollment error is inferred.

**Calculation:** 2013 − 748 = 1265 participants. Both printed totals are exact integers; no rounding tolerance applies. The subtraction quantifies the displayed difference and does not establish the historical intent of section 7.2.

**Alternative source-grounded interpretations:** Section 7.2 may be an unupdated procedural paragraph or an intentionally retained historical passage without an explicit historical label. The intended status of that future-tense paragraph is missing. The amendment supplies the revision; this record does not accuse an unlogged amendment.

**Mechanical evidence recheck:** recorded_candidate. Current source confirms future-tense748 alongside explicitly revised2013 in the same PLAN version. Diagnostic: 2013−748=1265. The initial748 is explicitly historical in section6.4, but section7.2 retains a current future-tense total. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Whether section7.2 was intended as retained historical text despite future tense. Human question: In version2.6, does section7.2 still prescribe748 or retain a historical paragraph; what current total was intended? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** A plan summary requires a distinguishable current sample target and historical procedure wording.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the retained enrollment target into a plan summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Read version 2.6 sections 6.4 and 7.2 alongside the current recruitment statement and amendment. Ask whether section 7.2 was intended to prescribe 748 or retain a historical paragraph, and which current target was intended. Record the answer below; do not change an actual enrolled total based on this wording comparison.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C100 — Conditional futility-region comparison at look 1

Pending Human Adjudication.

**Candidate statement:** Under a common signed-Z definition, the look-1 table inequality Z < 0.225 differs from the central graphical futility set. Missing contrast, sign/magnitude mapping and rule priority prevent an unconditional monitoring-error inference.

**Category:** Statistical reporting inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol monitoring table look1 versus PLAN protocol boundary figure at enrollment956; PLAN amendment and REPORT supplement repeated graphic corroborate

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Exact source locations:** [joi190055supp1_prod_16092.pdf PDF p.22](../../../joi190055supp1_prod_16092.pdf#page=22), PLAN, look1 Z-futility cell; [joi190055supp1_prod_16092.pdf PDF p.23](../../../joi190055supp1_prod_16092.pdf#page=23), PLAN, central pink Futility region at enrollment956. [joi190055supp4_prod_16092.pdf PDF p.31](../../../joi190055supp4_prod_16092.pdf#page=31), REPORT, corroborates the central graphical region. [joi190055supp2_prod_16092.pdf PDF p.3](../../../joi190055supp2_prod_16092.pdf#page=3), PLAN, confirms that the table and figure were introduced for the same revised monitoring design.

**Source evidence:** The table gives Z<0.225. The plot marks the pink Futility area between a negative inner boundary and its positive counterpart. Values below the negative inner boundary are outside the graphical futility area.

**Reported-versus-comparator:** Look 1, N = 956: printed table futility Z < 0.225, versus a central pink graphical Futility region between negative and positive inner boundaries. The plot does not independently print exact boundary coordinates.

**Reasoning procedure:** The inequality, signed axis and colored region are direct. Any statement that the graphical boundary is exactly±0.225 is a magnitude alignment only. Apply the logical comparison only if table and plot use the same signed statistic and contrast. Contrast/sign definitions, efficacy-oriented versus risk-oriented convention, magnitude transformation and harm/futility/efficacy priority are missing. No observed stopping Z path is supplied, so no actual trial decision is inferred.

**Calculation:** Witness Z = −4 satisfies −4 < 0.225, but is outside the central pink graphical region at N = 956. Under a common signed Z, the sets differ. The witness avoids exact boundary digitization; no numerical tolerance is assigned to an unprinted graphical coordinate.

**Alternative source-grounded interpretations:** The table could summarize a one-sided alternative-oriented rule, while the figure additionally partitions efficacy/harm; it might also intend |Z| in the table. No absolute-value notation or rule-priority/sign-conversion explanation is supplied. At look3 the efficacy and futility table entries form complementary regions of a single signed statistic, whereas the figure includes both harm and efficacy outer tails.

**Mechanical evidence recheck:** recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z=−4 satisfies Z<+0.225 but lies outside the pink central region at N956. Thus these sets differ under a common signed-Z interpretation. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look1 N956, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Extraction of a futility stopping region requires the sign and rule definition. This is distinct from PP-Z1's efficacy-tail sign comparison because it compares a different cell and interval-region rule.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the stopping-boundary sign or region into a monitoring-plan summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: Is the table's Z a signed statistic, a magnitude, or a one-sided alternative-oriented convention? What mapping/rule priority relates the tabulated futility inequality to the figure's central region? Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C101 — Conditional futility-region comparison at look 2

Pending Human Adjudication.

**Candidate statement:** Under a common signed-Z definition, the look-2 table inequality Z < 0.929 differs from the central graphical futility set. Missing contrast, sign/magnitude mapping and rule priority prevent an unconditional monitoring-error inference.

**Category:** Statistical reporting inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol monitoring table look2 versus PLAN protocol boundary figure at enrollment1434; PLAN amendment and REPORT supplement repeated graphic corroborate

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Exact source locations:** [joi190055supp1_prod_16092.pdf PDF p.22](../../../joi190055supp1_prod_16092.pdf#page=22), PLAN, look2 Z-futility cell; [joi190055supp1_prod_16092.pdf PDF p.23](../../../joi190055supp1_prod_16092.pdf#page=23), PLAN, central pink Futility region at enrollment1434. [joi190055supp4_prod_16092.pdf PDF p.31](../../../joi190055supp4_prod_16092.pdf#page=31), REPORT, corroborates the central graphical region. [joi190055supp2_prod_16092.pdf PDF p.3](../../../joi190055supp2_prod_16092.pdf#page=3), PLAN, confirms that the table and figure were introduced for the same revised monitoring design.

**Source evidence:** The table gives Z<0.929. The plot marks the pink Futility area between a negative inner boundary and its positive counterpart. Values below the negative inner boundary are outside the graphical futility area.

**Reported-versus-comparator:** Look 2, N = 1434: printed table futility Z < 0.929, versus a central pink graphical Futility region between negative and positive inner boundaries. The plot does not independently print exact boundary coordinates.

**Reasoning procedure:** The inequality, signed axis and colored region are direct. Any statement that the graphical boundary is exactly±0.929 is a magnitude alignment only. Apply the logical comparison only if table and plot use the same signed statistic and contrast. Contrast/sign definitions, efficacy-oriented versus risk-oriented convention, magnitude transformation and harm/futility/efficacy priority are missing. No observed stopping Z path is supplied, so no actual trial decision is inferred.

**Calculation:** Witness Z = −4 satisfies −4 < 0.929, but is outside the central pink graphical region at N = 1434. Under a common signed Z, the sets differ. The witness avoids exact boundary digitization; no numerical tolerance is assigned to an unprinted graphical coordinate.

**Alternative source-grounded interpretations:** The table could summarize a one-sided alternative-oriented rule, while the figure additionally partitions efficacy/harm; it might also intend |Z| in the table. No absolute-value notation or rule-priority/sign-conversion explanation is supplied. At look3 the efficacy and futility table entries form complementary regions of a single signed statistic, whereas the figure includes both harm and efficacy outer tails.

**Mechanical evidence recheck:** recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z=−4 satisfies Z<+0.929 but lies outside the pink central region at N1434. Thus these sets differ under a common signed-Z interpretation. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look2 N1434, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Extraction of a futility stopping region requires the sign and rule definition. This is distinct from PP-Z2's efficacy-tail sign comparison because it compares a different cell and interval-region rule.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the stopping-boundary sign or region into a monitoring-plan summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: Is the table's Z a signed statistic, a magnitude, or a one-sided alternative-oriented convention? What mapping/rule priority relates the tabulated futility inequality to the figure's central region? Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C102 — Conditional futility-region comparison at look 3

Pending Human Adjudication.

**Candidate statement:** Under a common signed-Z definition, the look-3 table inequality Z < 2.012 differs from the central graphical futility set. Missing contrast, sign/magnitude mapping and rule priority prevent an unconditional monitoring-error inference.

**Category:** Statistical reporting inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol monitoring table look3 versus PLAN protocol boundary figure at enrollment1912; PLAN amendment and REPORT supplement repeated graphic corroborate

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Exact source locations:** [joi190055supp1_prod_16092.pdf PDF p.22](../../../joi190055supp1_prod_16092.pdf#page=22), PLAN, look3 Z-futility cell; [joi190055supp1_prod_16092.pdf PDF p.23](../../../joi190055supp1_prod_16092.pdf#page=23), PLAN, central pink Futility region at enrollment1912. [joi190055supp4_prod_16092.pdf PDF p.31](../../../joi190055supp4_prod_16092.pdf#page=31), REPORT, corroborates the central graphical region. [joi190055supp2_prod_16092.pdf PDF p.3](../../../joi190055supp2_prod_16092.pdf#page=3), PLAN, confirms that the table and figure were introduced for the same revised monitoring design.

**Source evidence:** The table gives Z<2.012. The plot marks the pink Futility area between a negative inner boundary and its positive counterpart. Values below the negative inner boundary are outside the graphical futility area.

**Reported-versus-comparator:** Look 3, N = 1912: printed table futility Z < 2.012, versus a central pink graphical Futility region between negative and positive inner boundaries. The plot does not independently print exact boundary coordinates.

**Reasoning procedure:** The inequality, signed axis and colored region are direct. Any statement that the graphical boundary is exactly±2.012 is a magnitude alignment only. Apply the logical comparison only if table and plot use the same signed statistic and contrast. Contrast/sign definitions, efficacy-oriented versus risk-oriented convention, magnitude transformation and harm/futility/efficacy priority are missing. No observed stopping Z path is supplied, so no actual trial decision is inferred.

**Calculation:** Witness Z = −4 satisfies −4 < 2.012, but is outside the central pink graphical region at N = 1912. Under a common signed Z, the sets differ. The witness avoids exact boundary digitization; no numerical tolerance is assigned to an unprinted graphical coordinate.

**Alternative source-grounded interpretations:** The table could summarize a one-sided alternative-oriented rule, while the figure additionally partitions efficacy/harm; it might also intend |Z| in the table. No absolute-value notation or rule-priority/sign-conversion explanation is supplied. At look3 the efficacy and futility table entries form complementary regions of a single signed statistic, whereas the figure includes both harm and efficacy outer tails.

**Mechanical evidence recheck:** recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z=−4 satisfies Z<+2.012 but lies outside the pink central region at N1912. Thus these sets differ under a common signed-Z interpretation. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look3 N1912, are table and plot the same signed Z; if different, what contrasts/sign transformation and futility/harm rule priority map the one-sided inequality to central region? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Extraction of a futility stopping region requires the sign and rule definition. This is distinct from PP-Z3's efficacy-tail sign comparison because it compares a different cell and interval-region rule.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the stopping-boundary sign or region into a monitoring-plan summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: Is the table's Z a signed statistic, a magnitude, or a one-sided alternative-oriented convention? What mapping/rule priority relates the tabulated futility inequality to the figure's central region? Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C103 — Original primary-analysis effect label combines OR and RR

Pending Human Adjudication.

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

**Exact source locations:** [joi190055supp1_prod_16092.pdf PDF p.23](../../../joi190055supp1_prod_16092.pdf#page=23), PLAN, same primary-efficacy-analysis sentence. Both compared labels are PLAN content. [joi190055supp3_prod_16092.pdf PDF p.2](../../../joi190055supp3_prod_16092.pdf#page=2), PLAN, subsequently specifies risk ratio and is an explanatory later-plan comparator; it does not remove the original sentence's displayed labels. Planning probabilities for the illustration: PLAN [joi190055supp1_prod_16092.pdf — physical PDF p. 11, printed p. 10](../../../joi190055supp1_prod_16092.pdf#page=11), sample-size assumptions.

**Source evidence:** Original primary phrase is “odds ratio relative risks” with corresponding95% confidence interval calculated using logistic regression. The adjacent words were confirmed in the PDF image; they are not a locator/OCR repair.

**Reported-versus-comparator:** Original primary phrase is “odds ratio relative risks” with corresponding95% confidence interval calculated using logistic regression. The adjacent words were confirmed in the PDF image; they are not a locator/OCR repair. 

**Reasoning procedure:** Two different effect-measure terms printed together are direct. The planned-probability calculation illustrates distinction; it does not establish which effect was intended. Intended measure(s), contrast and logistic postprocessing for original sentence. Human question: Which measure(s), contrast and postprocessing did the original primary sentence intend, and which measure labels its interval?

**Calculation:** OR=[pH/(1−pH)]/[pL/(1−pL)] and RR=pH/pL are distinct scales. Within the original declared sample assumptions pH=.30,pL=.40, RR=.75 while OR=(.30/.70)/(.40/.60)=.642857. This illustrative calculation uses supplied planning probabilities; it is not an observed-result recalculation. The probabilities are supplied planning assumptions, not observed trial rates. Arithmetic is exact at the supplied two-decimal inputs; 0.642857 is a rounded diagnostic. Logistic regression alone does not determine whether a postprocessed estimate is an OR or RR.

**Alternative source-grounded interpretations:** The phrase may represent an unfinished replacement of OR by RR, or may intend two effects. Logistic regression can be followed by probability standardization, so its mention alone does not identify the effect.

**Mechanical evidence recheck:** recorded_candidate. Current render confirms adjacent odds ratio relative risks; source-label ambiguity reproduces without relying on an OCR error. Diagnostic: For supplied assumptions RR=.30/.40=.75; OR=(.30/.70)/(.40/.60)=.642857. This illustrates scale difference, not an observed-result recalculation. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Intended measure(s), contrast and logistic postprocessing for original sentence. Human question: Which measure(s), contrast and postprocessing did the original primary sentence intend, and which measure labels its interval? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** A reader extracting the original plan cannot uniquely label the effect from this sentence.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the effect-measure label into an extraction of the original plan. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: Which measure(s), contrast and logistic postprocessing were intended by the original sentence, and which label belongs to the associated interval? The later SAP gives RR but should not silently rewrite the preserved original source. Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C104 — Conditional efficacy-sign comparison at look 1

Pending Human Adjudication.

**Candidate statement:** Under a common signed-Z definition, the look-1 table inequality Z ≥ 2.75 has the opposite orientation to the negative graphical Efficacy region. Missing contrast, sign/magnitude mapping and rule priority prevent an unconditional monitoring-error inference.

**Category:** Statistical reporting inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol monitoring table look1 versus PLAN protocol boundary figure at enrollment956; PLAN amendment and REPORT supplement repeated graphic corroborate

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Exact source locations:** [joi190055supp1_prod_16092.pdf PDF p.22](../../../joi190055supp1_prod_16092.pdf#page=22), PLAN, statistical-analysis table, look1 efficacy; [joi190055supp1_prod_16092.pdf PDF p.23](../../../joi190055supp1_prod_16092.pdf#page=23), PLAN, stopping-boundary figure, Efficacy region at enrollment956. [joi190055supp4_prod_16092.pdf PDF p.31](../../../joi190055supp4_prod_16092.pdf#page=31), REPORT, reproduces the negative-Z efficacy graphical orientation and corroborates the figure side; [joi190055supp2_prod_16092.pdf PDF p.3](../../../joi190055supp2_prod_16092.pdf#page=3), PLAN, amendment explicitly introduces the same table/figure but adds no signed contrast definition. The REPORT location corroborates rather than creates an additional discrepancy.

**Source evidence:** The table calls the look1 efficacy boundary Z≥2.75. The plotted region labelled Efficacy lies below zero and its corresponding outer boundary is at a negative ordinate. Harm lies above zero. Exact graphical ordinate coordinates are not independently printed; the sign is directly visible.

**Reported-versus-comparator:** Look 1, N = 956: printed table efficacy Z ≥ 2.75, versus a graphical Efficacy region below zero, with Harm above zero. The plot does not independently print exact boundary coordinates.

**Reasoning procedure:** Printed positive table inequality and negative labelled region are direct source observations. Interpreting the plotted magnitude as exactly2.75 is diagnostic only. Apply the logical comparison only if table and plot use the same signed statistic and contrast. Contrast/sign definitions, efficacy-oriented versus risk-oriented convention, magnitude transformation and harm/futility/efficacy priority are missing. No observed stopping Z path is supplied, so no actual trial decision is inferred.

**Calculation:** The table inequality Z ≥ +2.75 points toward positive Z. The graph labels the negative outer region Efficacy and the positive region Harm. Those orientations differ if the same signed statistic is intended. No exact negative boundary magnitude is claimed from the plot; this is a sign comparison without a P-tail reconstruction or graphical-digitization tolerance.

**Alternative source-grounded interpretations:** The table may use an efficacy-oriented Z and the figure may use a treatment-risk-oriented Z. That can reconcile the intended design, but neither the table nor figure declares this sign reversal. A nonnegative absolute statistic would require a distinct labelled convention because the figure is explicitly signed.

**Mechanical evidence recheck:** recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z≥+2.75 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look1 N956, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Sign conventions can affect extraction of efficacy versus harm boundaries. No conclusion about the actual trial decision follows because no observed stopping Z path is supplied.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the stopping-boundary sign or region into a monitoring-plan summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: Are the table and figure meant to use the same signed Z? If different, what are the two contrast/sign definitions? Review the source generating table and plot rather than assume high-minus-low or low-minus-high. Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C105 — Conditional efficacy-sign comparison at look 2

Pending Human Adjudication.

**Candidate statement:** Under a common signed-Z definition, the look-2 table inequality Z ≥ 2.432 has the opposite orientation to the negative graphical Efficacy region. Missing contrast, sign/magnitude mapping and rule priority prevent an unconditional monitoring-error inference.

**Category:** Statistical reporting inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol monitoring table look2 versus PLAN protocol boundary figure at enrollment1434; PLAN amendment and REPORT supplement repeated graphic corroborate

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Exact source locations:** [joi190055supp1_prod_16092.pdf PDF p.22](../../../joi190055supp1_prod_16092.pdf#page=22), PLAN, statistical-analysis table, look2 efficacy; [joi190055supp1_prod_16092.pdf PDF p.23](../../../joi190055supp1_prod_16092.pdf#page=23), PLAN, stopping-boundary figure, Efficacy region at enrollment1434. [joi190055supp4_prod_16092.pdf PDF p.31](../../../joi190055supp4_prod_16092.pdf#page=31), REPORT, reproduces the negative-Z efficacy graphical orientation and corroborates the figure side; [joi190055supp2_prod_16092.pdf PDF p.3](../../../joi190055supp2_prod_16092.pdf#page=3), PLAN, amendment explicitly introduces the same table/figure but adds no signed contrast definition. The REPORT location corroborates rather than creates an additional discrepancy.

**Source evidence:** The table calls the look2 efficacy boundary Z≥2.432. The plotted region labelled Efficacy lies below zero and its corresponding outer boundary is at a negative ordinate. Harm lies above zero. Exact graphical ordinate coordinates are not independently printed; the sign is directly visible.

**Reported-versus-comparator:** Look 2, N = 1434: printed table efficacy Z ≥ 2.432, versus a graphical Efficacy region below zero, with Harm above zero. The plot does not independently print exact boundary coordinates.

**Reasoning procedure:** Printed positive table inequality and negative labelled region are direct source observations. Interpreting the plotted magnitude as exactly2.432 is diagnostic only. Apply the logical comparison only if table and plot use the same signed statistic and contrast. Contrast/sign definitions, efficacy-oriented versus risk-oriented convention, magnitude transformation and harm/futility/efficacy priority are missing. No observed stopping Z path is supplied, so no actual trial decision is inferred.

**Calculation:** The table inequality Z ≥ +2.432 points toward positive Z. The graph labels the negative outer region Efficacy and the positive region Harm. Those orientations differ if the same signed statistic is intended. No exact negative boundary magnitude is claimed from the plot; this is a sign comparison without a P-tail reconstruction or graphical-digitization tolerance.

**Alternative source-grounded interpretations:** The table may use an efficacy-oriented Z and the figure may use a treatment-risk-oriented Z. That can reconcile the intended design, but neither the table nor figure declares this sign reversal. A nonnegative absolute statistic would require a distinct labelled convention because the figure is explicitly signed.

**Mechanical evidence recheck:** recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z≥+2.432 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look2 N1434, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Sign conventions can affect extraction of efficacy versus harm boundaries. No conclusion about the actual trial decision follows because no observed stopping Z path is supplied.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the stopping-boundary sign or region into a monitoring-plan summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: Are the table and figure meant to use the same signed Z? If different, what are the two contrast/sign definitions? Review the source generating table and plot rather than assume high-minus-low or low-minus-high. Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __

## C106 — Conditional efficacy-sign comparison at look 3

Pending Human Adjudication.

**Candidate statement:** Under a common signed-Z definition, the look-3 table inequality Z ≥ 2.012 has the opposite orientation to the negative graphical Efficacy region. Missing contrast, sign/magnitude mapping and rule priority prevent an unconditional monitoring-error inference.

**Category:** Statistical reporting inconsistency

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol monitoring table look3 versus PLAN protocol boundary figure at enrollment1912; PLAN amendment and REPORT supplement repeated graphic corroborate

**Review domain:** plan_material

**Evidence state:** recorded_candidate

**Suggested review disposition:** retain

**Classification rationale:** Both primary compared locations are prospective protocol content and therefore PLAN; the discrepancy is plan-internal. A repeated REPORT plot, where cited, corroborates rather than conflicts and adds no P_R.

**Classification ambiguity:** Different benefit-oriented and treatment-risk-oriented Z can reconcile design. Corroborating REPORT graphic does not add P_R; both discrepancy locations remain PLAN.

**Exact source locations:** [joi190055supp1_prod_16092.pdf PDF p.22](../../../joi190055supp1_prod_16092.pdf#page=22), PLAN, statistical-analysis table, look3 efficacy; [joi190055supp1_prod_16092.pdf PDF p.23](../../../joi190055supp1_prod_16092.pdf#page=23), PLAN, stopping-boundary figure, Efficacy region at enrollment1912. [joi190055supp4_prod_16092.pdf PDF p.31](../../../joi190055supp4_prod_16092.pdf#page=31), REPORT, reproduces the negative-Z efficacy graphical orientation and corroborates the figure side; [joi190055supp2_prod_16092.pdf PDF p.3](../../../joi190055supp2_prod_16092.pdf#page=3), PLAN, amendment explicitly introduces the same table/figure but adds no signed contrast definition. The REPORT location corroborates rather than creates an additional discrepancy.

**Source evidence:** The table calls the look3 efficacy boundary Z≥2.012. The plotted region labelled Efficacy lies below zero and its corresponding outer boundary is at a negative ordinate. Harm lies above zero. Exact graphical ordinate coordinates are not independently printed; the sign is directly visible.

**Reported-versus-comparator:** Look 3, N = 1912: printed table efficacy Z ≥ 2.012, versus a graphical Efficacy region below zero, with Harm above zero. The plot does not independently print exact boundary coordinates.

**Reasoning procedure:** Printed positive table inequality and negative labelled region are direct source observations. Interpreting the plotted magnitude as exactly2.012 is diagnostic only. Apply the logical comparison only if table and plot use the same signed statistic and contrast. Contrast/sign definitions, efficacy-oriented versus risk-oriented convention, magnitude transformation and harm/futility/efficacy priority are missing. No observed stopping Z path is supplied, so no actual trial decision is inferred.

**Calculation:** The table inequality Z ≥ +2.012 points toward positive Z. The graph labels the negative outer region Efficacy and the positive region Harm. Those orientations differ if the same signed statistic is intended. No exact negative boundary magnitude is claimed from the plot; this is a sign comparison without a P-tail reconstruction or graphical-digitization tolerance.

**Alternative source-grounded interpretations:** The table may use an efficacy-oriented Z and the figure may use a treatment-risk-oriented Z. That can reconcile the intended design, but neither the table nor figure declares this sign reversal. A nonnegative absolute statistic would require a distinct labelled convention because the figure is explicitly signed.

**Mechanical evidence recheck:** recorded_candidate. Current table and render reproduce the registered conditional direction/region comparison; sign-convention mapping remains the precise missing definition. Diagnostic: Z≥+2.012 points toward positive values while the graphical Efficacy region is negative. Exact plotted magnitude is not independently printed and is not asserted as a numeric source value. Classification P_P; all P_P; plan_material; no role/type code correction. Necessary missing inputs: Z contrast/sign definition in each display, efficacy-oriented versus risk-oriented convention, magnitude/absolute-value transformation and rule priority (including harm). Human question: At look3 N1912, are table and plot the same signed Z; if different, what contrasts/sign transformation and efficacy/harm rule priority map the positive tabulated efficacy inequality to negative graphical efficacy tail? The classification codes above agree with the source-confirmed recheck. The suggested review disposition (retain) is a mechanical pre-fill for human review and is not an adjudication.

**Quality-control relevance:** Sign conventions can affect extraction of efficacy versus harm boundaries. No conclusion about the actual trial decision follows because no observed stopping Z path is supplied.

**Potential downstream evidence impact:** If this question is confirmed as a reporting defect, an evidence extractor could copy the stopping-boundary sign or region into a monitoring-plan summary. Small preventable reporting defects can matter for downstream evidence extraction. No propagation, conclusion change or serious harm is established by this record.

**Human verification steps:** Open the exact source pages above and compare the cited cells or statements. Recompute the stated arithmetic or logical diagnostic using the printed inputs, retaining the named conditions and display tolerance. Resolve this source-specific question: Are the table and figure meant to use the same signed Z? If different, what are the two contrast/sign definitions? Review the source generating table and plot rather than assume high-minus-low or low-minus-high. Record the human assessment in the five blank fields below.

**Human adjudication fields:** 

- **Validity:** __
- **Importance:** __
- **Action:** __
- **Initials:** __
- **Notes:** __
