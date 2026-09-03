# Numeric consistency review — Workflow 1.5.1

## Scope and method

This is an independent numeric/reporting check of every relationship in the current global inventories: **N001–N068 (68/68)** and **S001–S036 (36/36)**. I used the current 1.5.1 maps as locators and checked relevant printed values in the supplied PDFs; direct PDF page evidence controls over OCR and layout text. I did not use legacy candidate, queue, disposition, verifier, critic, quality, or final-report records.

Checks included exact/subtotal arithmetic, numerator/denominator/percentage reconciliation, rounding, participant/population identity, mutually exclusive category totals, units and labels, repeated values, effect direction, point/interval containment, rate/count distinctions, and matched cross-document statements. Percentages are accepted when the printed count divided by the stated denominator rounds to the displayed precision (normally one decimal percentage point; half-unit rounding tolerance 0.05 percentage points). Model-derived effects were not recomputed from aggregate tables when the supplied package does not provide a compatible estimator or fitted-object inputs.

## Complete relationship coverage

| Inventory IDs checked | Principal checks and result |
|---|---|
| N001–N007; S001–S007 | Main abstract, Results narrative, and Table 2: population/contrast matching; 3397 = 1681 + 1716; survival, tracheostomy and KRT counts/percentages; matched effects, intervals, directions and P values. All reconciled except the separately recorded ventilation-summary label/display issue in NC01. |
| N008–N016; S008 | Eligibility, exposure and 0–90-day definitions; four-period cluster flow; 3599 screened/eligible context, 3411 enrolled, 14 withdrawals, 3397 ITT; Figure 1 row/column totals; zero-day percentages (497/1681 = 29.57%, 475/1716 = 27.68%). Reconciled under the printed definitions. |
| N017–N024; S012–S013 | Main Table 1, Figure 2, Results narrative and Figure 3: sex/admission/source/category totals, individual denominators, missing ideal-weight counts, units/scales, adverse-event totals, time-specific display populations, and subgroup partitions. All printed arithmetic/labels reconcile. |
| N025–N028; S009–S011, S014–S015 | Main Table 2/Figure 3: sensitivity exclusions (144 + 90 = 234; 17 + 10 = 27), discharge-destination totals (1681 and 1716), readmission proportions, subgroup Ns, interval ordering/point containment and model-specific mean/median/CrI labels. NC01 is the sole exception. |
| N029–N032; S016–S021 | Results-supplement pp3–8: feeding and audit time windows, outcome populations/scales, final model changes, bootstrap/Bayesian sample conventions, binary/discharge and subgroup framework. No numeric inconsistency found. |
| N033–N039 | Results-supplement pp9–15: sequence total 2044 + 1353 = 3397; eight period/treatment Ns sum to ITT totals; category denominators; delivery Ns; 49 + 54 = 103 exclusions; all-feeding and post-enrolment populations/missingness. Reconciled. |
| N040–N046 | Results-supplement pp16–22: protocol-deviation participant/event counts; audit 292 + 224 + 52 = 568; period-by-treatment descriptive counts; biochemistry available-N context; AE/SAE treatment and period totals; readmission distributions. Arithmetic reconciled. NC02 is the sole numeric-rendering exception. |
| N047–N052 | Results-supplement pp24–32: figure-specific IBW/ABW populations, histogram interpretation, and ICEMAN-linked subgroup figures/forms. All relevant numeric identity checks reconciled. The direct page-28 figure reads `p<0.001`, not `p>0.001`; it matches p31, so the retained RRT seed is not a candidate. |
| N053–N058; S022–S027 | Protocol pp8–21: planned definitions, formula units, horizons, power/model statements, and external feasibility result. Planning versus achieved-result contexts were kept separate; no matched source contradiction found. |
| N059–N067; S028–S032 | Protocol pp35–39 PRO-SCAN background/prospective subset material: thresholds, time windows, formula units, projected totals and prospective analysis terminology. Internally coherent; not conflated with final TARGET results. |
| N068; S033–S036 | SAP pp2, 8–23: prospective 3412-enrolment statement, formula and outcome definitions, planned model/effect-measure descriptions. The planned count/model differs in context from final reporting and is not a direct inconsistency. |

## Candidate records

### NC01 — Table 2 labels invasive-ventilation summaries as mean (SD), while the printed parentheses are range-form values

- **Category:** Measure, label, or scale inconsistency.
- **Exact source location:** [main article PDF p7, Table 2](../../../jama_summers_2025_oi_250040_1753124024.36498.pdf#page=7), row `Duration of invasive ventilation, mean (SD), h`.
- **Printed inputs:** Augmented protein `84.0 (35.0 to 178.9)`; usual protein `78.0 (33.2 to 161.0)`. The same row prints an adjusted `Mean difference, 6.8 (−3.0 to 16.5)` hours.
- **Rule and calculation:** An SD is one nonnegative dispersion number, conventionally printed as `mean (SD)` such as `84.0 (35.0)`. Each descriptive parenthesis here contains two ordered values joined by `to` (`35.0 < 178.9`; `33.2 < 161.0`), the form used for a range or an IQR, not an SD. This requires no rounding tolerance: the issue is a categorical label/display-form mismatch.
- **Direct observation vs diagnostic inference:** Directly observed are the row label and both two-endpoint parenthetical displays. The inference is that at least one of the label `mean (SD)` or the descriptive parenthetical format is not the intended summary. The supplied record does not establish whether the values are ranges, IQRs, or another interval.
- **Alternative interpretation:** The word `to` might be a production error in values otherwise intended as SDs, or the label might be the production error while the estimates/results-supplement ventilation summaries are medians (IQR). Neither alternative resolves the printed mismatch.
- **Quality-control relevance:** A reader extracting the descriptive distribution for synthesis or comparison cannot tell whether the reported numbers are means/SDs or interval endpoints; this can propagate a wrong variance or summary type.
- **Human question:** What descriptive statistic was intended for each ventilation group, and should Table 2 show one SD per mean or be relabeled to the actual two-endpoint summary?
- **Status:** Pending Human Adjudication.

### NC02 — One eTable 10 alive-at-day-90 percentage uses a comma where all comparable values use a decimal point

- **Category:** Measure, label, or scale inconsistency.
- **Exact source location:** [results supplement PDF p18, eTable 10](../../../joi250040supp3_prod_1753124024.38098.pdf#page=18), `Alive at day 90 [n (%)]`, `Period 2 – Usual Protein (4 units, n = 530)`.
- **Printed inputs:** `383 (72, 3%)`. Comparable cells in the same row use decimal points, including `323 (67.3%)`, `258 (77.0%)`, `229 (76.8%)`, and `408 (74.0%)`.
- **Rule and calculation:** `383 / 530 × 100 = 72.2641509…%`, which rounds to **72.3%** to one decimal place (accepted rounding interval 72.25% to <72.35%). The printed comma separates `72` and `3` rather than following the table's decimal-point convention.
- **Direct observation vs diagnostic inference:** Directly observed are the comma-bearing cell and the displayed denominator. The calculation supports the diagnostic inference that the intended rendering is likely `72.3%`; it does not prove the production mechanism.
- **Alternative interpretation:** A comma can be a decimal separator in some locales, so the numeric value may still be understood as 72.3%. In this English table, the surrounding point-decimal cells make the mixed notation a source-grounded consistency issue.
- **Quality-control relevance:** It creates avoidable ambiguity for automated or manual numeric extraction from a period-specific survival result, although it does not by itself alter the trial conclusion.
- **Human question:** Should the Period 2 usual-protein value be standardized to `383 (72.3%)`?
- **Status:** Pending Human Adjudication.

## Seed disposition within this checker (not a candidate)

The relationship inventories retain an RRT/renal-failure interaction seed. Direct visual inspection of [results supplement PDF p28, eFigure 7](../../../joi250040supp3_prod_1753124024.38098.pdf#page=28) shows `p<0.001`; [p31 ICEMAN](../../../joi250040supp3_prod_1753124024.38098.pdf#page=31) also prints `P<0.001`. Thus the source pages agree and no interaction-P candidate is recorded. No inspected relationship relied on a coherent display-zero P value.

## Counts and limitations

- **Relationships checked:** 104/104 (N001–N068 and S001–S036).
- **Distinct candidate records:** 2 (NC01–NC02); neither has a stable C ID, severity, validity determination, or disposition beyond Pending Human Adjudication.
- **Limitations:** Aggregate descriptive tables cannot reproduce mixed-model estimates. The protocol, SAP, PRO-SCAN and external-feasibility materials are prospective or contextual where labeled, so they were not treated as final-result comparators absent matched population/time/estimand evidence. Exact page images were used to resolve the two retained seeds and the P-value transcription question.
