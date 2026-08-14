# Main-article result-claim source verification — DOC-001

## Scope and source control

- **Document ID:** DOC-001.
- **Source:** `jama_giamarellosbourboulis_2025_oi_250116_1771885794.23757.pdf` (12 PDF pages; journal pp. 775-786).
- **Hash check:** the source PDF SHA-256 calculated in this review was `197405b4717695cdc5f5b4a1b3823ff9cb47944041e808c8bbb1aa2546a43997`, identical to `.ai_paper_validation/preprocessing/source_pdf_sha256.txt`.
- **Materials reviewed:** native derived text for PDF pp. 1-12 and retained page images for PDF pp. 3 and 6-8. Visual inspection confirmed the locations and values below. This response verifies only the already-recorded six accepted findings and the two rejected interpretations; it does not add or re-adjudicate a candidate.

## Participant flow and analysis denominators

| Direct source evidence | Location | Reproducible comparison |
|---|---|---|
| “672 Adults with presumed infectious sepsis were screened for eligibility”; “391 Excluded”; “281 Randomized.” | PDF p. 3 / journal p. 777, Figure 1 | 672 − 391 = **281** randomized. The nine shown exclusion counts sum to 355 + 14 + 8 + 5 + 2 + 2 + 2 + 2 + 1 = **391**. |
| “135 Randomized to receive standard care and precision immunotherapy” and “146 Randomized to receive standard care and placebo.” | PDF p. 3 / journal p. 777, Figure 1 | 135 + 146 = **281**. |
| Precision: “131 Received intervention as randomized”; “4 Withdrew consent and requested removal of all data.” Placebo: “145 Received intervention as randomized”; “1 Withdrew consent and requested removal of all data.” | PDF p. 3 / journal p. 777, Figure 1 | 131 + 4 = 135 and 145 + 1 = 146. Hence 131 + 145 = **276** analysis participants, and 281 − 5 = **276**. |
| “Five patients withdrew consent and requested removal of all their data, 4 in the precision immunotherapy group and 1 in the placebo group, leaving 276 patients … in the primary analysis population.” | PDF p. 6 / journal p. 780, Results—Patients | Narrative independently supplies the same 4 + 1 = 5 and 276 total. |
| “131 Included in the primary analysis (blood sampling for evaluation of restoration of immune dysfunction = 59)” and “145 Included … (= 66).” | PDF p. 3 / journal p. 777, Figure 1 | The immune-restoration subset is 59 + 66 = **125**, which is the denominator stated for the day-28 SIDF-reversal outcome below. |

**Limit:** Figure 1 labels discontinuations but does not identify them as mutually exclusive in a footnote. Within each arm the displayed components nevertheless sum to the displayed discontinued-intervention total: 35 + 18 + 8 + 1 = 62 and 51 + 19 + 2 = 72. These figures are context for the reported analysis denominators, not a new flow finding.

## Primary and key secondary outcome evidence

| Outcome and direct reported values | Exact location | Direct/derived check |
|---|---|---|
| **Primary outcome:** “≥1.4-Point decrease of mean SOFA score d 2 to 9,” precision immunotherapy 46/131 (35.1), placebo 26/145 (17.9), difference 17.2 (6.8 to 27.2), unadjusted OR 2.48 (1.42 to 4.32), P=.002. | PDF p. 6 / journal p. 780, Table 2, primary-end-point row; also Results—Primary End Point: “46 of 131 … (35.1%)” and “26 of 145 … (17.9%).” | 46/131 = 35.1145% → 35.1%; 26/145 = 17.9310% → 17.9%; 35.1145 − 17.9310 = 17.1835 percentage points → 17.2. Diagnostic unadjusted cross-product OR = (46×119)/(85×26) = 2.477 → 2.48. |
| **28-day mortality:** precision 57/131 (43.5), placebo 72/145 (49.7), difference **6.1** (−5.6 to 17.6), unadjusted OR 0.78 (0.49 to 1.26), P=.34. The results text says: “28-day mortality occurred in 57 of 131 patients (43.5%) … and 72 of 145 patients … (49.7%), a difference that did not reach statistical significance (P = .34, Table 2; eFigure 3 in Supplement 2).” | PDF p. 6 / journal p. 780, Table 2, main-secondary-outcome row; PDF p. 7 / journal p. 781, Results—Secondary End Points | Direct figures and P value agree between Table 2 and narrative. Directional arithmetic supporting the locked presentation-inconsistency finding is given below. |
| **90-day mortality:** precision 90/131 (68.7), placebo 98/145 (67.6), difference 1.1 (−9.8 to 11.9), unadjusted OR 1.05 (0.63 to 1.75), P=.90. | PDF p. 6 / journal p. 780, Table 2, main-secondary-outcome row | 90/131 = 68.7023% and 98/145 = 67.5862%; precision minus placebo = 1.1161 percentage points → 1.1. |
| **Day-15 SOFA response:** precision 52/131 (39.7), placebo 34/145 (23.4), difference 16.3 (5.3 to 26.8), unadjusted OR 2.15 (1.28 to 3.61), P=.004. | PDF p. 6 / journal p. 780, Table 2, main-secondary-outcome row | 52/131 = 39.6947% → 39.7%; 34/145 = 23.4483% → 23.4%; difference = 16.2464 percentage points → 16.3. |
| **SIDF reversal by day 28:** precision 46/59 (78.0), placebo 32/66 (48.5), difference 29.5 (12.6 to 44.0), unadjusted OR 3.76 (1.72 to 8.22), P=.001. | PDF p. 6 / journal p. 780, Table 2; PDF p. 7 / journal p. 781, Results—Secondary End Points | 46/59 = 77.9661% → 78.0%; 32/66 = 48.4848% → 48.5%; difference = 29.4813 percentage points → 29.5. The stated denominators reconcile to the Figure 1 restoration subset (59 + 66 = 125). |
| **Infection assessment at day 15:** precision: resolution 58/131 (44.3), intermediate 11/131 (8.4), failure 32/131 (24.4), superinfection 30/131 (22.9); placebo: 46/145 (31.7), 9/145 (6.2), 44/145 (30.3), 46/145 (31.7). Printed ordinal-model OR for a worse outcome: 0.59 (0.38 to 0.91), P=.02. | PDF p. 6 / journal p. 780, Table 2, Assessment of infection by d 15 rows and footnote c; PDF p. 7 / journal p. 781, Results—Secondary End Points | The four counts sum to 131 in the precision group (58+11+32+30) and 145 in placebo (46+9+44+46). Footnote c specifies that this OR “expresses the risk of worse outcome of the precision immunotherapy group vs the placebo group”; a simple binary recomputation would not be an equivalent substitute for the stated ordinal analysis. |

## Source verification for the locked findings

### Accepted finding 1 — Day-15 SOFA narrative/table numerator mismatch

- **Narrative evidence:** PDF p. 7 / journal p. 781, Results—Secondary End Points: “the attainment of at least a 1.4-point decrease of the mean SOFA score by day 15 was greater in the group of precision immunotherapy **(39.7%; 51 of 131)** than in the placebo group (23.4%; 34 of 145; P = .004).”
- **Table evidence:** PDF p. 6 / journal p. 780, Table 2, “≥1.4-Point decrease of mean SOFA score d 2 to 15”: precision **52/131 (39.7)** and placebo **34/145 (23.4)**, difference **16.3 (5.3 to 26.8)**, OR **2.15 (1.28 to 3.61)**, P=.004.
- **Comparison inputs and calculation:** 52/131 × 100 = 39.6947%, which rounds to 39.7%; 51/131 × 100 = 38.9313%, which rounds to 38.9%. The narrative percentage agrees with the table numerator 52, not with its own printed numerator 51. Placebo counts, percentage, and P value agree in the two main-article locations.
- **Limitation:** The main article cannot establish which source was intended to control; the already-recorded cross-document confirmation comes from Supplement 2, not from the main article. This response does not infer a correction.

### Accepted finding 5 — Table 2 28-day mortality difference direction

- **Source evidence:** PDF p. 6 / journal p. 780, Table 2, column order is “Precision immunotherapy,” then “Placebo,” then “Difference, % (95% CI).” In the 28-d Mortality row the printed values are 57/131 (43.5), 72/145 (49.7), and **6.1 (−5.6 to 17.6)**. The immediately following 90-d Mortality row has 90/131 (68.7), 98/145 (67.6), and **1.1 (−9.8 to 11.9)**.
- **Diagnostic comparison:** using the displayed column order, (57/131 − 72/145) × 100 = (0.4351145 − 0.4965517) × 100 = **−6.1437 percentage points**, which rounds to −6.1%, not the printed +6.1%. For the next row, (90/131 − 98/145) × 100 = **+1.1161 percentage points**, which rounds to its printed +1.1%.
- **Limit:** The main article contains no Table 2 header or footnote defining an alternative direction for the 28-day row. It also does not provide the method output needed to determine whether the CI endpoints were displayed under another contrast; no corrected CI or value is inferred here.

### Accepted finding 6 — Abstract percentage attached grammatically to event count

- **Abstract:** PDF p. 1 / journal p. 775, Abstract—Results: “A total of **1069 serious treatment-emergent adverse events (88.8%)** were reported.”
- **Body:** PDF p. 8 / journal p. 782, Results—Adverse Events: “A total of **1069 serious treatment-emergent adverse events were reported in 245 patients (88.8%)**.”
- **Relevant denominators:** Figure 1 reports 131 + 145 = 276 in the primary analysis (PDF p. 3 / journal p. 777); p. 6 narrative likewise states that five withdrawals left 276 in the primary analysis (journal p. 780).
- **Calculation:** 245/276 × 100 = **88.7681%**, which rounds to 88.8%. The body assigns the percentage to patient incidence, while the abstract syntactically places it immediately after the event total. This main article does not state a denominator under which 1069 events equal 88.8%.
- **Limit:** The source distinguishes events from patients but does not give an event-level denominator in these locations. The response therefore preserves the locked presentation finding and makes no claim about a corrected abstract wording.

### Accepted findings 2-4 — Main-article cross-references and subgroup claims only

The printed challenged estimates are in Supplement 2; no main-article table or figure reproduces those numerical rows. The following direct main-article text establishes the claims and links to the cited supplemental displays without independently confirming the supplemental values.

| Locked finding | Main-article source evidence | Limitation |
|---|---|---|
| 2. eTable 10 unadjusted OR | PDF p. 7 / journal p. 781, Results—Secondary End Points: “the decrease of mean SOFA score of 1.4-points or more by day 9 was attained in both states of immune dysregulation (**eTable 10 in Supplement 2**).” The text gives day-9 strata: macrophage activation–like syndrome 12/25 vs 4/23 (P=.04), and sepsis-induced immunoparalysis 34/106 vs 22/122 (P=.02). | It contains neither the challenged day-15 row nor its unadjusted OR/CI. Counts and statistical verification of that locked finding must remain attributed to Supplement 2. |
| 3. eFigure 9 OR/CI pairing | PDF p. 8 / journal p. 782, Results—Post Hoc and Subgroup Analyses: “No significant interactions were found between any subgroup and precision immunotherapy for an effect on 90-day mortality (**eFigure 9 in Supplement 2**).” | The main article reports no eFigure 9 OR, CI, or P value. It cannot source-verify the challenged numerical pairing. |
| 4. eFigure 7/eFigure 8 duplicate statistics | PDF p. 8 / journal p. 782, Results—Post Hoc and Subgroup Analyses: “Interaction tests showed statistical significance of interaction of the precision immunotherapy group with a CCI of 5 or higher and a SOFA score 10 or higher for the achievement of primary end point (**eFigures 7 in Supplement 2**); and … with a CCI of 5 or higher and a SOFA score 10 or higher for the decrease of 28-day mortality (**eFigure 8 in Supplement 2**).” | The main article establishes that eFigure 7 concerns the primary endpoint and eFigure 8 concerns 28-day mortality, but does not print the respective OR/CI/P triplets. No model interpretation beyond this direct reference is made. |

## Rejected interpretations: main-article evidence boundaries

| Rejected interpretation in the package report | Direct main-article reference | Evidence boundary |
|---|---|---|
| Localized terminology slip in eFigure 6 | PDF p. 8 / journal p. 782, Results—Post Hoc and Subgroup Analyses: “The time to reversal of SIDF was significantly shorter in the precision immunotherapy group (**eFigure 6 in Supplement 2**).” | eFigure 6 itself is not reproduced in DOC-001. The main article provides no disputed terminology to inspect; it only identifies the outcome and source. |
| Two readily recoverable malformed eTable 14 cells | PDF p. 9 / journal p. 783, Adverse Events continuation: “Comparisons of the nonserious treatment-emergent adverse events indicated decreased incidence of bradycardia in the recombinant human interferon gamma group; decreased signs of ileus in the anakinra group; and more creatinine increase, fibrinogen decrease, and γ-glutamyl transferase increase in the recombinant human interferon gamma group (**eTable 14 in Supplement 2**).” | eTable 14 is not reproduced in DOC-001. The article supplies the results claim but cannot verify cell formatting or offer an independent corrective value. |

## Additional direct subgroup and adverse-event claims relevant to the report

- **Subgroups (PDF p. 7 / journal p. 781):** the day-9 SOFA response was reported as 12/25 (48.0%) vs 4/23 (17.4%), P=.04, in macrophage activation–like syndrome, and 34/106 (32.1%) vs 22/122 (18.0), P=.02, in sepsis-induced immunoparalysis. The printed precision for the last placebo percentage omits a percent symbol in the derived text/image location; it is reproduced above as printed and is not normalized.
- **Adverse-event table (PDF p. 8 / journal p. 782, Table 3):** “Any serious adverse event” is displayed as patients with at least one event, per footnote b: precision 8 (6.1) probably/possibly related plus 108 (82.4) probably not related/unrelated; placebo 3 (2.1) plus 126 (86.9). Footnote a says classification covers events “captured during the 90 days of follow-up for the enrolled 276 patients,” and footnote b distinguishes the any-event patient counts from event counts in other table cells. This supports, but does not replace, the adverse-event numerator/denominator clarification above.

