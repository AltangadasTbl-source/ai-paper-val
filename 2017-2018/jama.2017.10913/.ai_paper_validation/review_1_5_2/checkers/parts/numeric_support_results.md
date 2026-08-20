# Numeric consistency review, shard B — DOC-003 support results

## Scope and method

Complete review of relationships `N600`–`N653` (54 relationships), against the supplied direct source `joi170091supp2_prod.pdf` (DOC-003), PDF pp. 2–10.  Native layout text was checked against the direct PDF; rendered table pages were available in the fresh evidence assets.  No old audit derivative was used as evidence.

For a displayed one-decimal percentage, the check accepts the printed numerator/denominator if its exact percentage rounds to that display under ordinary nearest-tenth rounding (interval `[display - 0.05, display + 0.05)`, allowing the source's displayed precision).  Counts and denominators are treated as exact unless the source expressly qualifies them.  Categories are not summed when the source says, or does not establish, mutual exclusivity.

## Relationship-level results

| ID | Direct-source location | Checks performed | Outcome |
|---|---|---|---|
| N600 | DOC-003 p. 2, Study Setting | Unit/scale and range review of beds, occupancy, prevalence, population, time, and round-frequency descriptors; no total or comparator is asserted. | **COMPLETE — no qualifying inconsistency.** |
| N601 | p. 2, Usual Care | Checked 1–4 L and 30–60 min are volume/time order descriptors; compared the absolute-volume definition with eTable 3's litre categories. | **COMPLETE — no qualifying inconsistency.** eTable 3 describes individual usual-care orders and does not purport to be limited to the stated common-order range. |
| N602 | p. 3, Safety elements | Checked threshold labels/units and distinguished per-litre monitoring, six hours after enrollment, and four litres in six hours after ED presentation. | **COMPLETE — no qualifying inconsistency.** |
| N603 | p. 4, Data Collection | Checked time labels, mL units, and the stated approximation (3 cm above sternal angle; approximately 8 cm above right atrium; CVP 10 mm Hg) as an explicitly approximate clinical mapping, not an arithmetic equality. | **COMPLETE — no qualifying inconsistency.** |
| N604 | p. 5, Model development | Recalculated 85/209 = 40.67% and 109/194 = 56.19%; distinguished in-hospital and 28-day outcomes and the follow-up denominator. | **COMPLETE — no qualifying inconsistency.** |
| N605 | p. 6, eTable 1 | Recalculated 15/103 = 14.56% -> 14.6%; 9/106 = 8.49% -> 8.5%. | **COMPLETE — denominators and displayed percentages reconcile.** |
| N606 | p. 6, eTable 1 | Recalculated 51/103 = 49.51% -> 49.5%; 52/106 = 49.06% -> 49.1%. | **COMPLETE — reconciles.** |
| N607 | p. 6, eTable 1 | Recalculated 63/103 = 61.17% -> 61.2%; 68/106 = 64.15% -> 64.2%; preserved inclusive tuberculosis definition. | **COMPLETE — reconciles.** |
| N608 | p. 6, eTable 1 | Recalculated 20/103 = 19.42% -> 19.4%; 15/106 = 14.15% -> 14.2%. | **COMPLETE — reconciles.** |
| N609 | p. 6, eTable 1 | Recalculated 9/103 = 8.74% -> 8.7%; 4/106 = 3.77% -> 3.8%. | **COMPLETE — reconciles.** |
| N610 | p. 6, eTable 1 | Recalculated CNS: 17/103 = 16.50% -> 16.5%, 12/106 = 11.32% -> 11.3%; UTI: 2/103 = 1.94% -> 1.9%, 2/106 = 1.89% -> 1.9%. | **COMPLETE — reconciles; overlapping diagnoses preclude row-total check.** |
| N611 | p. 7, eTable 2 | Recalculated 19/103 = 18.45% -> 18.4%; 24/106 = 22.64% -> 22.6%. | **COMPLETE — reconciles.** |
| N612 | p. 7, eTable 2 | Recalculated 6/103 = 5.83% -> 5.8%; 1/106 = 0.94% -> 0.9%; retained explicit exception to blood-culture wording. | **COMPLETE — reconciles.** |
| N613 | p. 7, eTable 2 | Recalculated 6/103 = 5.83% -> 5.8%; 2/106 = 1.89% -> 1.9%. | **COMPLETE — reconciles.** |
| N614 | p. 7, eTable 2 | Recalculated 2/103 = 1.94% -> 1.9%; 3/106 = 2.83% -> 2.8%. | **COMPLETE — reconciles.** |
| N615 | p. 7, eTable 2 | Recalculated 2/103 = 1.94% -> 1.9%; 2/106 = 1.89% -> 1.9%. | **COMPLETE — reconciles.** |
| N616 | p. 7, eTable 2 | Recalculated 1/103 = 0.97% -> 1.0%; 2/106 = 1.89% -> 1.9%. | **COMPLETE — reconciles.** |
| N617 | p. 7, eTable 2 | Recalculated 1/103 = 0.97% -> 1.0%; 1/106 = 0.94% -> 0.9%. | **COMPLETE — reconciles.** |
| N618 | p. 7, eTable 2 | Recalculated 4/103 = 3.88% -> 3.9%; 4/106 = 3.77% -> 3.8%. | **COMPLETE — reconciles.** |
| N619 | p. 7, eTable 2 | Recalculated 2/103 = 1.94% -> 1.9%; 1/106 = 0.94% -> 0.9%. | **COMPLETE — reconciles.** |
| N620 | p. 7, eTable 2 | Recalculated 1/103 = 0.97% -> 1.0%; 1/106 = 0.94% -> 0.9%. | **COMPLETE — reconciles.** |
| N621 | p. 7, eTable 2 | Recalculated 2/103 = 1.94% -> 1.9%; 1/106 = 0.94% -> 0.9%. | **COMPLETE — reconciles.** |
| N622 | p. 7, eTable 2 | Recalculated 1/103 = 0.97% -> 1.0%; 3/106 = 2.83% -> 2.8%. | **COMPLETE — reconciles.** |
| N623 | p. 7, eTable 2 | Recalculated 4/103 = 3.88% -> 3.9%; 1/106 = 0.94% -> 0.9%. | **COMPLETE — reconciles.** |
| N624 | p. 7, eTable 2 | Recalculated 2/103 = 1.94% -> 1.9%; 1/106 = 0.94% -> 0.9%; preserved mixed diagnostic ascertainment label. | **COMPLETE — reconciles.** |
| N625 | p. 7, eTable 2 and footnote | Recalculated group cells: 2/103 = 1.94% -> 1.9%, 1/106 = 0.94% -> 0.9%; availability: 47/209 = 22.49% -> 22.5%. | **COMPLETE — reconciles; slide availability is all-participant, not group-column, denominator.** |
| N626 | p. 7, eTable 2 | Recalculated 48/103 = 46.60% -> 46.6%; 58/106 = 54.72% -> 54.7%. | **COMPLETE — reconciles.** |
| N627 | p. 7, eTable 2 text | Checked medians lie within their printed IQRs (7.5 in 4.5–11.5; 7.0 in 5.0–10.0) and all values use days. | **COMPLETE — no qualifying inconsistency.** |
| N628 | p. 7, eTable 2 text | Recalculated 46/103 = 44.66% -> 44.7%, 46/106 = 43.40% -> 43.4%, 0/103 = 0.0%, 1/106 = 0.94% -> 0.9%; retained `P > 0.85` and `P > 0.99` as threshold displays rather than exact values. | **COMPLETE — reconciles; no display-zero candidate.** |
| N629 | p. 8, eTable 3 | Recalculated each no-bolus cell against n=103; counts 3+9+16+11+3 = 42 and 42/103 = 40.78% -> 40.8%. | **COMPLETE — row cells and stated no-bolus total reconcile.** |
| N630 | p. 8, eTable 3 | Recalculated 1/103, 5/103, 10/103, and 7/103 to 1.0%, 4.9%, 9.7%, and 6.8%; subtotal is 23. | **COMPLETE — reconciles.** |
| N631 | p. 8, eTable 3 | Recalculated 5/103, 1/103, 4/103, 2/103, 1/103, 1/103 to displayed 4.9%, 1.0%, 3.9%, 1.9%, 1.0%, 1.0%; subtotal is 14. | **COMPLETE — reconciles.** |
| N632 | p. 8, eTable 3 | Recalculated 3/103, 1/103, 1/103, 1/103 to 2.9%, 1.0%, 1.0%, 1.0%; 3-L-fast subtotal 5 and 4-L-fast subtotal 1. | **COMPLETE — reconciles.** |
| N633 | p. 8, eTable 3 | Recalculated 8/103 = 7.77% -> 7.8%; 10/103 = 9.71% -> 9.7%. | **COMPLETE — reconciles.** |
| N634 | p. 8, eTable 3 footnote | Checked available orders 103−10=93; category count total 42+23+14+5+1+8+10=103; available-category count 103−10=93; 7/8 other orders = 87.5% (no percent displayed). | **COMPLETE — all reported count relationships reconcile.** |
| N635 | p. 9, eTable 4 | Checked primary logistic population n=209 against its row label; distinguished effect estimate/CI/P as inferential inputs separately mapped at S400. | **COMPLETE — no population/label inconsistency.** |
| N636 | p. 9, eTable 4 | Checked worst-case n=212 against stated 1 excluded protocol patient plus 2 excluded usual-care patients: 209+1+2=212; preserved imputation direction. | **COMPLETE — reconciles.** |
| N637 | p. 9, eTable 4 | Checked n=209 and continuous SAPS-3/lactic-acid adjustment labels; compared with p. 5 model-development statement. | **COMPLETE — no qualifying inconsistency.** |
| N638 | p. 9, eTable 4 | Checked n=209, contrast (`>=3 L` versus `<3 L`), outcome (in-hospital mortality), and six-hours-after-ED-registration anchor. | **COMPLETE — no qualifying inconsistency.** |
| N639 | p. 9, eTable 4 | Checked n=209, same as-treated contrast/window, and adjustment labels (continuous SAPS-3 and suspected site). | **COMPLETE — no qualifying inconsistency.** |
| N640 | p. 9, eTable 4 | Checked n=209, Cox survival outcome, protocol-versus-usual-care comparator, HR label and direction footnote. | **COMPLETE — no qualifying inconsistency.** |
| N641 | p. 9, eTable 4 | Checked n=209, Cox survival comparator, and continuous baseline SAPS-3 adjustment against label. | **COMPLETE — no qualifying inconsistency.** |
| N642 | p. 9, eTable 4 | Checked n=209, Cox survival comparator, quartile SAPS-3 adjustment, HR/CI/P coherence; see provisional record NUM-B-001. | **COMPLETE — qualifying provisional candidate recorded.** |
| N643 | p. 9, eTable 4 footnote | Checked SAPS-3 stated possible range 0–217 and direction (higher score, higher in-hospital mortality risk) against all continuous/quartile labels. | **COMPLETE — no qualifying inconsistency.** |
| N644 | p. 9, eTable 4 footnote | Checked OR applies to logistic death odds and HR to Cox survival, both with protocol group as direction reference. | **COMPLETE — no label/scale inconsistency.** |
| N645 | p. 10, eTable 5 | Recalculated 0/103 and 0/106 to 0.0%; checked prospective six-hour post-enrollment ascertainment. | **COMPLETE — reconciles; coherent display zero is not a candidate.** |
| N646 | p. 10, eTable 5 | Recalculated 0/103 = 0.0%; 2/106 = 1.89% -> 1.9%; checked same ascertainment window. | **COMPLETE — reconciles.** |
| N647 | p. 10, eTable 5 | Recalculated 0/103 and 0/106 to 0.0%; checked prospective six-hour post-enrollment ascertainment. | **COMPLETE — reconciles; coherent display zero is not a candidate.** |
| N648 | p. 10, eTable 5 footnote | Checked the nurse-screening population, both-group qualifier, and six-hours-after-enrollment window against each adverse-event row. | **COMPLETE — no qualifying inconsistency.** |
| N649 | pp. 5 and 9 | Compared p. 5 totals (85/209 in-hospital; 109/194 28-day) with eTable 4's n=209 and n=212 model populations; did not equate outcome-specific follow-up or imputed as-randomized populations. | **COMPLETE — no qualifying inconsistency.** |
| N650 | pp. 3, 4, 8–10 | Cross-checked all six-hour uses: monitoring/AE after enrollment, protocol maximum after ED presentation, as-treated exposure after ED registration. | **COMPLETE — no inconsistency: anchors are expressly different and appropriately labelled.** |
| N651 | pp. 6–10 | Checked group total 103+106=209; preserved table-specific denominators 47/209 (malaria slides) and 93/103 (orders). | **COMPLETE — denominator provenance reconciles.** |
| N652 | p. 7, eTable 2 | Reviewed organism-row aggregation. Source does not establish mutual exclusivity and explicitly includes non-blood-culture exceptions; no row-sum-to-group-total rule applies. | **COMPLETE — no qualifying inconsistency.** |
| N653 | p. 6, eTable 1 footnote | Reviewed diagnosis-row aggregation. Direct footnote says each patient could have more than one diagnosis; no row-sum-to-group-total rule applies. | **COMPLETE — no qualifying inconsistency.** |

## Provisional candidate records

### NUM-B-001 — eTable 4 printed P value is not coherent with the printed adjusted-quartile Cox HR and 95% CI

- **Exact source location:** `joi170091supp2_prod.pdf#page=9`, DOC-003 PDF p. 9, eTable 4, last row: “Adjusted Cox proportional hazards model ... SAPS-3 score at baseline categorized by quartile.”
- **Printed comparator / inputs:** `n = 209`; hazard ratio `1.69`; 95% CI `1.14 – 2.51`; printed P value `0.001`. The immediately preceding adjusted Cox row prints HR `1.68`, CI `1.14 – 2.49`, P `0.009`.
- **Rule and reproducible calculation:** For a two-sided Wald-type 95% CI on log(HR), the standard error implied by the printed CI is `(ln(2.51) - ln(1.14)) / (2 × 1.96) = 0.201`.  The printed HR then gives `z = ln(1.69) / 0.201 = 2.61`, with two-sided P approximately `0.009` (about 0.0089), not 0.001.  Conversely, two-sided P = 0.001 implies |z| about 3.29, which is not compatible with a 95% CI as wide as 1.14–2.51 for HR 1.69 under the same Wald calculation. Tolerance: ordinary rounding of HR/CI endpoints to two decimals cannot bridge the roughly nine-fold P-value difference; using their rounding intervals produces an approximate P range near 0.007–0.011.
- **Direct observation versus inference:** Direct observation is the four printed values in the final eTable 4 row. The incompatibility is an inference from the conventional log-HR/Wald CI relationship. The PDF does not identify a different P-value test for this row.
- **Alternatives:** The P value may be a transcription/typographical error (for example, `0.009`), may refer to a different test or parameter than the displayed protocol-group HR, or the CI/HR may have been printed incorrectly. A multi-degree-of-freedom global test for the quartile covariate would not ordinarily be the P value for the displayed protocol-vs-usual-care HR, but the table does not state what test P=0.001 represents.
- **Quality-control relevance:** The table presents the P value alongside a specific effect estimate and CI. A mismatch can alter interpretation of the reported strength of evidence and should be checked before downstream quantitative use.
- **Exact human question:** *For the final adjusted Cox row, does P = 0.001 test the displayed protocol-versus-usual-care HR of 1.69 (95% CI, 1.14–2.51), and if so which printed value should be corrected or what non-Wald analysis produced these values?*

## Limitations

DOC-003 supplies only printed summaries; no patient-level data, model coefficient covariance matrix, or test specification is supplied. Therefore this shard can verify table arithmetic and identify the printed CI/P mismatch, but cannot determine which value, if any, is the intended corrected value. No severity, validity, disposition, C ID, or adjudication is assigned.
