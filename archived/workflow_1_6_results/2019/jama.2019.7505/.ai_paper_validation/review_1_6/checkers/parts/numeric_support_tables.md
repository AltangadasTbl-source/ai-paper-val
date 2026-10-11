# Numeric consistency checker: results-supplement tables

Status: COMPLETE. Runtime ID: 01a1286e-c7cc-7cd0-a901-f092deade378. Exact owned scope: DOC-005 eTables 1–9, physical PDF pages 22–30. All nine table pages and all 119 compound relationships N241–N359 were checked. Every numeric table cell, reference category, denominator, dispersion, estimate, interval, P value, unit, model and footnote is retained in the companion inventory. No target, minimum, maximum or top-N finding rule was applied. Three distinct document-grounded local candidates are emitted below. These keys are handoff identifiers, not stable C IDs.

## Candidate index

| Local key | Relationship | Exact question scope | Compared document locations and roles |
|---|---|---|---|
| SUPPORT-NUM-01 | N269 | Different P values for the matched synthetic-colloid participant-count comparison | DOC-001 Table 2 p.8 REPORT; DOC-005 eTable 3 p.24 REPORT |
| SUPPORT-NUM-02 | N327 | Conditional mean/SD inconsistency on the supplied 10 cm VAS scale | DOC-005 eTable 7 p.28 REPORT; DOC-002 protocol p.17 and p.20 PLAN |
| SUPPORT-NUM-03 | N355 | Conditional mismatch of the high-arm mean event count with the sum of 12 component counts | DOC-005 eTable 9 p.30 REPORT; DOC-001 Table 3 p.9 REPORT |

## SUPPORT-NUM-01 — matched synthetic-colloid count P values

**Assigned relationship:** N269.

**Compared locations and document roles:**

- [DOC-001 main article, physical PDF p.8](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), printed p.2299, Table 2 continued, Synthetic colloids, No. (%), H/L participant counts and its P-value column: REPORT.
- [DOC-005 results supplement, physical PDF p.24](../../../../joi190055supp4_prod_16092.pdf#page=24), eTable 3, Synthetic colloids, No. (%), H/L participant counts and its P-value column: REPORT.
- Same DOC-005 p.24 immediately following synthetic-colloid quantity row is a local alternative-check location, REPORT; it prints a separate continuous summary, not the count row.

**Printed inputs:** Both matched count rows use high n = 989 and low n = 987, with 74 (7.5%) versus 56 (5.7%). Main Table 2 prints P = .09; eTable 3 prints P = 0.10. The eTable 3 quantity row immediately below prints 50 (211) versus 35 (171), P = 0.09. Main Table 2 quantity summary instead uses median (IQR), 0.5 (0.5–0.7) versus 0.5 (0.5–0.5) L, P = .50.

**Reproducible rule and calculation:** A matched result means the same participant numerator, denominator, comparison, and count label. Compare the two count-row P cells: 0.10 − 0.09 = 0.01. Count percentages separately reconcile: 100 × 74 / 989 = 7.48231%, and 100 × 56 / 987 = 5.67376%, rounding to 7.5% and 5.7%. The quantity summaries and their P values are not substituted for the count comparison.

**Tolerance:** Each P is printed to two decimal places, ordinarily allowing ±0.005. Rounding intervals [0.085, 0.095) and [0.095, 0.105) do not share an interior; a value exactly at 0.095 with different tie handling is an explicit alternative. The discrepancy is a printed repeated-value difference, not an attempt to reconstruct either test.

**Direct observation versus inference:** Direct source images confirm the same displayed counts, percentage labels, populations and different printed P values. The hypothesis that one P was copied from the neighboring continuous row is inference only, not a finding. The article does not supply a table-specific test rule establishing that both count comparisons used exactly the same test.

**Alternatives and missing definition:** Different tests, continuity corrections, exact versus asymptotic calculations, an unreported effective denominator, or exact-boundary rounding could produce different P values. Identical printed inputs and labels do not identify a disclosed reason. The row with 50 (211) and 35 (171) is a distinct quantity comparison, so its P = .09 is not proof of copying.

**Quality-control relevance:** A small matched P-value discrepancy can propagate as conflicting extracted comparison metadata. No claim about study conclusions follows.

**Exact human question:** “Do the P = .09 in main Table 2 and P = .10 in eTable 3 refer to the same synthetic-colloid participant-count comparison of 74/989 versus 56/987; if so, which test, denominator and rounding convention generated each displayed P value?”

## SUPPORT-NUM-02 — conditional thoracic VAS mean/SD bound

**Assigned relationship:** N327.

**Compared locations and document roles:**

- [DOC-005 results supplement, physical PDF p.28](../../../../joi190055supp4_prod_16092.pdf#page=28), eTable 7, VAS thoracic – cm, mean (SD), No., Day 2, low PEEP cell: REPORT.
- [DOC-002 protocol, physical PDF p.17](../../../../joi190055supp1_prod_16092.pdf#page=17), printed protocol p.16, version 2.6, actual organ function evaluation bullet defining “Visual Analogue Scale (10 cm): evaluation for dyspnea, thoracic and abdominal rest and incident pain”: PLAN.
- [DOC-002 protocol, physical PDF p.20](../../../../joi190055supp1_prod_16092.pdf#page=20), printed protocol p.19, postoperative assessment continuation bullet “VAS evaluation for dyspnea, thoracic and abdominal rest and incident pain”: PLAN.

**Printed inputs:** eTable 7 low PEEP day-2 thoracic VAS mean 1.4 cm, SD 3.9 cm, n = 841; high PEEP mean 1.3 cm, SD 0.8 cm, n = 838; P = .34. Arm headings are high989 and low987. The protocol specifies a 10 cm VAS for the same named symptoms and repeats the assessment postoperatively. It does not explicitly print the numerical scoring endpoints or a normalization rule.

**Reproducible rule and calculation:** Conditional on the reported cm scores being distance along the supplied 10 cm line, measured from a zero origin and bounded 0–10 cm, any sample with mean m and sample SD s obeys s² ≤ n/(n−1) × m × (10−m). At the printed mean, the maximum sample SD is sqrt(841/840 × 1.4 × 8.6) = 3.47194 cm, below 3.9 cm. With rounding admitted, m can range from 1.35 to 1.45; the largest permitted bound on that interval is sqrt(841/840 × 1.45 × 8.55) = 3.52310 cm. The printed SD interval begins at 3.85 cm. Thus even the most permissive rounding leaves a gap of at least 3.85 − 3.52310 = 0.32690 cm.

**Tolerance:** Mean/SD displayed to one decimal permit ±0.05 cm; n = 841 is exact. The n/(n−1) factor allows the usual sample SD convention and is slightly more permissive than population SD. This calculation is a moment bound, not a reconstructed P value.

**Direct observation versus inference:** The mean, SD, n, cm unit, mean(SD) header and protocol 10 cm scale wording are direct source observations. The numerical 0–10 support and zero-origin scoring convention are explicitly conditional inferences from that supplied line-length and cm-unit description. They are not independently printed endpoints. Protocol p.17 describes baseline organ-function assessment; p.20 repeats the same named VAS postoperatively but does not restate its length. Applying the 10 cm definition to eTable 7 is an identity question retained for human review.

**Alternatives and missing definition:** A transformed or shifted scoring convention, a differently normalized postoperative scale, a larger allowed range, a different underlying statistic despite the mean(SD) label, or a transcription error could explain the display. Without zero origin, a line of length10 alone permits SD up to about5.00 cm and does not establish the mean-dependent contradiction. An alternative 0-based scale would need an upper endpoint at least11.66026 cm even with the rounding allowances, to accommodate the minimum printed SD3.85 at mean1.45. No external VAS convention is used.

**Quality-control relevance:** The reported dispersion may be reused as a summary SD in quantitative evidence synthesis. The candidate is confined to the consistency of that reported summary with the supplied scale definition; it is not a raw-data or clinical plausibility audit.

**Exact human question:** “Were the postoperative thoracic VAS scores in eTable 7 recorded as 0–10 cm distance scores on the protocol’s 10 cm scale, and does the low-PEEP Day 2 cell correctly report mean 1.4 cm, SD 3.9 cm and n = 841; if a different origin, range or transformation was used, what was it?”

## SUPPORT-NUM-03 — conditional event-count mean versus component total

**Assigned relationship:** N355.

**Compared locations and document roles:**

- [DOC-005 results supplement, physical PDF p.30](../../../../joi190055supp4_prod_16092.pdf#page=30), eTable 9, Sensitivity analysis for the primary outcome, Count events row, high/low summary cells and n = 989/987 headings: REPORT.
- [DOC-001 main article, physical PDF p.9](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), printed p.2300, Table 3, all 12 Components of the Primary Outcome, high/low No. of Events columns and n = 989/987 headings: REPORT.
- DOC-005 p.30 model footnotes referring to all12 components are corroborative REPORT context, not a new discrepancy relationship.
- [DOC-001 main article, physical PDF p.3](../../../../jama_bluth_2019_oi_190055_16092.pdf#page=3), Figure 1 randomized high 1011/low 1002, REPORT: source-grounded alternative denominator, not an additional discrepancy relationship.

**Printed inputs:** eTable 9 Count events row gives high0.35 (0.88), low0.38 (0.86), above separately labeled Median (IQR)0 (0–0) for both arms. The Count events row does not explicitly say mean(SD). Main Table 3 high component counts, in its printed order, are mild135, moderate42, severe30, atelectasis44, pleural effusion43, new infiltrates14, cardiopulmonary edema17, bronchospasm12, pulmonary infection10, aspiration2, ARDS3, pneumothorax1. Low counts in the same order are154,58,36,55,21,18,9,10,10,1,1,3.

**Reproducible rule and calculation:** Conditional on “Count events” summary0.35/0.38 being the arithmetic mean of the number of these same12 binary components per participant in the displayed full-arm populations, the mean must equal the sum of all component numerators divided by n. Overlap between components does not defeat this identity; each counted component contributes separately. High sum135 + 42 + 30 + 44 + 43 + 14 + 17 + 12 + 10 + 2 + 3 + 1 = 353; 353 / 989 = 0.356926, which rounds to0.36. Low sum154 + 58 + 36 + 55 + 21 + 18 + 9 + 10 + 10 + 1 + 1 + 3 = 376; 376 / 987 = 0.380952, which rounds to0.38 and reconciles.

**Tolerance:** At two-decimal rounding,0.35 ordinarily implies a mean in [0.345,0.355), hence a total in [341.205,351.095) at n989; integer totals compatible with that interval are342–351. The printed component total353 exceeds the largest compatible integer total by2. The exact mean exceeds the upper rounding boundary0.355 by0.001926. Counts and denominator have zero tolerance. The low-arm summary is within its rounding interval.

**Direct observation versus inference:** Direct images confirm all12 main component counts, populations, and the eTable 9 summary0.35 (0.88). The arithmetic sum and conditional mean identity are derived. Interpreting the unlabeled first summary as mean(SD), and interpreting “Count events” as counting each of the same12 binary components, are named inferences rather than printed definitions.

**Alternatives and missing definition:** The summary may use a different statistic, component grouping (for example collapsing multiple respiratory-failure severities to one event), time rule, population, event definition, weighting or complete-case denominator. Main Figure 1 supplies randomized high 1011/low 1002: 353/1011 = 0.349159 and 376/1002 = 0.375250, which round to 0.35/0.38. Thus a count calculation using all randomized participants could explain both summary means, but that denominator differs from eTable 9 headings 989/987 and requires the population and missing-participant handling to be named. This is an arithmetic alternative, not proof that the authors used it. Truncation rather than rounding would also produce 0.35 from 0.356926 but is not stated. Different component overlap is not by itself an explanation if the count is the sum of those same 12 indicators; alternative grouping would change the count definition and should be specified.

**Quality-control relevance:** Event burden means and their dispersions can be extracted separately from binary-composite risks; a missing aggregation definition or mismatched displayed mean can lead to an incorrect extracted endpoint. No claim about treatment effect or conclusion follows.

**Exact human question:** “Is 0.35 (0.88) in the high-PEEP Count events row the mean (SD) of the count of the same 12 primary-outcome components reported in main Table 3 among 989 participants; if so, how does it reconcile with 353 component occurrences and 353/989 = 0.356926, and if not, what statistic, grouping, time rule and denominator does it represent?”

## Complete noncandidate checks and limitations

The companion numeric inventory gives an explicit checked result for each of119 relationships. Count/percentage rows in eTables3–5 and8 reconcile at their displayed precision. eTable6 category sums reconstruct available denominators984/982 for priority,985/986 for position,986/986 for wound; all printed percentages then reconcile. Missing counts are5/5,4/1 and3/1 respectively. Every VAS observed n is within its arm population; each scale/day missing count is retained, with no inferred cause.

All11 nonreference ARISCAT coefficients reproduce their integer scores and are compatible with printed ORs after beta/OR rounding. Four reference categories have absent coefficient/score cells, not printed zeros. Maximum component score123 agrees with the main scale range. Rescue sequences retain all19 populated arm-step pairs, FiO2 as fractions and PEEP as cmH2O; the absent low-arm step10 is not zero. Continuous amount rows remain distinct from main medians and from count rows. Overlapping drug/solution/component counts are not forced to sum to binary totals.

Per-protocol917 + 912 =1829 matches main flow; losses72/75 sum147, matching1976 −1829. Each per-protocol component/composite numerator is within its matched full-analysis numerator. “Effect Estimate” in eTable8 remains a generic effect label; raw RR arithmetic is not imposed without a supplied measure definition. All point estimates are within ordered intervals, and directions/units remain compatible. Statistical same-test CI/P reconstruction is referred to the independently assigned statistical checkers, particularly eTable8 cardiopulmonary edema and eTable9 average relative effect. Proportional-odds CI and Wilcoxon P are explicitly distinct calculations. No person-time rate is supplied. No display-zero P appears; printed zero doses and medians are retained as finite-precision quantities.

Tool engines: Poppler26.01.0 pdftotext/pdftoppm, reusable source-matched native/layout text, five rendered candidate/comparator pages. Unique derivatives are under preprocessing/numeric_support_tables/. Fresh source extraction includes assigned tables22–30 and targeted protocol17/20. Complete scientific coverage of the assigned scope; no missing source unit. Named unresolved definitions are only the specific candidate alternatives above. Sources and reused assets preserved; no old candidate/report conclusions, web, external literature, Python scientific orchestration, or GPU used. No stable C IDs, severity, validity, evidence disposition or adjudication assigned.

