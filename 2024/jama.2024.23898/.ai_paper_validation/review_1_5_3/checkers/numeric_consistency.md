# Numeric Consistency Review

## Scope and method

This review covered every relationship in `relationships/numeric_relationship_inventory.md` (`N001`-`N065`) over all 119 mapped supplied-PDF pages. Direct PDF text and, for the graphical eFigure, direct rendered-page inspection were used to confirm the two candidates below. No web or earlier candidate, checker, queue, verifier, critic, or report conclusion was used.

For counts and percentages, the arithmetic rule was `printed percentage = 100 × printed numerator / printed denominator`, with a rounding tolerance of 0.05 percentage point for a one-decimal printed percentage (and ordinary sum tolerance from separately rounded components). For exclusive categories, the rule was `sum of printed subgroup counts = stated population` unless the source explicitly states overlap, missingness, censoring, or a different analysis set. For reported differences, the diagnostic rule was the unadjusted displayed group value difference; it was not used to reject an adjusted model estimate. For rates, risk, proportions, event counts, person-time quantities, and time-to-event displays, labels and declared analysis sets were checked before arithmetic comparison. Exact source definitions were required before identifying a cross-document window, measure, unit, or reference-group contradiction.

## Completed relationship checks

| Relationship IDs | Checks completed | Outcome |
|---|---|---|
| N001-N006, N047-N049, N058-N061 | Population, allocation, endpoint-time, model/measure-label, planned-versus-observed, reference-group, and scale checks. | Checked; two document-grounded discrepancies are recorded below. |
| N007-N010, N019-N021, N029, N036-N042 | Numerator/denominator/percentage, unadjusted-difference diagnostic, repeated-value, interval-label, narrative, and matched-result checks. | Checked; the eFigure interval-level conflict is recorded below. |
| N011-N014 | Flow, exclusion, treatment-receipt, questionnaire missingness, and subgroup-sum checks. | Checked; printed arm arithmetic reconciles. Screening reasons are expressly nonexclusive. |
| N015-N018, N045 | Baseline subgroup sums, count-percentage calculations, denominator changes, units, scale/direction, and rounded repeated-value checks. | Checked; categorical totals reconcile within rounding and stated denominators. |
| N022-N025, N050-N054 | Repeated-score population, time point, scale/range/direction, unit, missing-item, and displayed-difference diagnostic checks. | Checked; adjusted time-by-treatment estimates were not required to equal raw mean differences. |
| N023, N052 | Dose, OME, mg/mcg, 24-h/72-h window, median/IQR, and analysis-denominator checks. | Checked; no concrete numeric contradiction identified. |
| N026-N028, N055-N056 | Recovery-variable numerator/percentage, time-window, threshold, label, and discharge-readiness checks. | Checked; eFigure itself says its enhanced-recovery categories were not predefined, so the protocol's example graded proportions do not establish a candidate. |
| N030-N032 | Kaplan-Meier at-risk/event, count-versus-risk/proportion, and repeated-value checks. | Checked; interval event totals need not equal baseline minus later at-risk values because censoring and further event intervals are possible and no contradictory rule is printed. |
| N033-N035, N057, N064 | Total-stay composite, rate-versus-count, participant-versus-event, safety-population, mortality/readmission/complication denominators, and reported time-window checks. | Checked; the readmission-window conflict is recorded below. |
| N043-N044, N062-N065 | Criteria/threshold, contextual-versus-result, formula, projected-versus-observed, template, and no-applicable-unit checks. | Checked; no candidate from templates, projections, or contextual citations. |

## Candidate 1: eFigure confidence-interval level has incompatible printed labels

**Relationship IDs:** N037-N042 and N061.

**Exact source location:** DOC-004, [eFigure p. 2](joi240139supp3_prod_1741633738.18862.pdf#page=2); corroborating planned subgroup convention: DOC-003, [p. 14](joi240139supp2_prod_1741633738.17362.pdf#page=14).

**Printed inputs:** In the eFigure legend, the horizontal-line key is printed `99% CI`. The eFigure caption immediately below the plot states: `The numbers on the right are the within-subgroup relative risks and 95% confidence interval.` The right-hand entries include, for example, intended 6 hours `0.92 (0.73, 1.15)` and intended 12 hours `1.03 (0.82, 1.28)`. The SAP prints that subgroup analyses use a two-sided 1% significance level and `Corresponding 99% confidence intervals`.

**Reproducible rule and calculation:** For one set of plotted horizontal intervals and their printed right-hand numerical intervals, the stated confidence level must be one unambiguous level. Direct text comparison gives `99%` (legend) versus `95%` (caption), a difference of 4 percentage points in the reported confidence level. No rounding tolerance applies to an explicit confidence-level label; tolerance is exactly 0 percentage points.

**Direct observation versus inference:** Direct observation is the 99% legend and 95% caption on the same supplied PDF page. The inference is that at least one label is inconsistent; the supplied page alone does not establish which label was intended for every displayed interval.

**Source-grounded alternatives:** The caption could contain a proofreading error while the legend is correct; the legend could be wrong; or the overall result may have a 95% CI while subgroup intervals use 99% CIs, but the caption's plural wording does not say that distinction. The SAP supports, but does not by itself prove, the 99% subgroup convention.

**Quality-control relevance:** A confidence-interval level changes the uncertainty conveyed by a forest plot and can affect extraction of subgroup estimates for downstream evidence products.

**Exact human question:** Which confidence level applies to each eFigure interval, and should the legend, caption, or both be corrected to state that level unambiguously?

## Candidate 2: unplanned-readmission reporting window differs between the published table and supplied protocol/SAP

**Relationship IDs:** N035 and N057.

**Exact source locations:** Published Table 3: DOC-001, [p. 8](jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8). Protocol Version 8: DOC-002, [p. 18](joi240139supp1_prod_1741633738.16362.pdf#page=18). SAP Version 2: DOC-003, [p. 10](joi240139supp2_prod_1741633738.17362.pdf#page=10).

**Printed inputs:** Table 3 reports `Unplanned readmission after discharge and within 90 d of operation`: IV lidocaine `31 (11.1%)`, placebo `34 (12.2%)`. The protocol calls the endpoint `Unplanned re-admissions within 30 days of date of operation` and specifies `30 days from date of operation`. The SAP lists `Unplanned re-admissions within 30 days of date of operation` among tertiary outcomes.

**Reproducible rule and calculation:** A matched endpoint must retain the same printed measurement window unless a supplied amendment or explicit redefinition identifies a changed endpoint. The published table's window is 90 days after operation; the protocol/SAP window is 30 days after operation. The direct window comparison is `90 days − 30 days = 60 days`; tolerance is 0 days because these are explicit endpoint definitions, not rounded measurements.

**Direct observation versus inference:** Direct observation is the 90-day wording and counts in Table 3 and the 30-day wording in both supporting documents. The inference is that the reported table may reflect an unreported endpoint-window change, a table-label error, or a supported but not located amendment. The counts cannot determine which explanation is correct.

**Source-grounded alternatives:** A later amendment, analysis-plan update, or prespecified publication-specific definition may have changed readmission follow-up to 90 days; the supplied protocol/SAP might not be the final governing version; or Table 3's `90 d` label may be erroneous. The package does not supply a document resolving these alternatives.

**Quality-control relevance:** A 30-day readmission proportion and a 90-day readmission proportion are different measures. Confusing them can misstate the follow-up window in evidence extraction and comparisons.

**Exact human question:** Was unplanned readmission intentionally redefined from within 30 to within 90 days of operation before final analysis, and if so, where is that change documented; otherwise, which printed window and associated counts are correct?

## Non-candidate decisions and limitations

No display-zero P-value relationship was present in the mapped numeric scope; none was registered. The eFigure intended-duration subgroup totals 532, whereas its other subgroup totals are 557; the supplied Figure 1 records 532 treatment recipients, so the figure's printed evidence does not establish a contradiction without a statement that every 557 primary-analysis participant should have an intended-duration value. The enhanced-recovery footnote explicitly says high/moderate/low definitions were not predefined, so the earlier protocol's example percentage categories do not by themselves prove a contradictory category assignment.

The supplied protocol and SAP are planned-analysis documents and cannot alone establish that a later published endpoint change was invalid. This review records the printed discrepancy and leaves its resolution to human adjudication. No candidate identifier, severity, validity finding, or disposition has been assigned.

## Counts

Relationships checked: 65. Distinct candidates emitted: 2. Candidate identifiers assigned: 0.
