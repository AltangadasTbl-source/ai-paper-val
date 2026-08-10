# Figure, Flow, Caption, and Visible-Annotation Check

## Scope and method

- Audited DOC-001 main-article Figure 1, Figure 2, and result-relevant Tables 1-4 on source-PDF pages 4-8, using the retained original-resolution page renders and native/OCR text maps.
- Audited DOC-004 Supplementary Tables 1-3 on source-PDF pages 2-6, including the three-page continuation of Supplementary Table 2.
- Compared visible labels, captions, legends, denominators, participant-flow counts, subgroup partitions, plot direction, and cross-referenced main-text claims.
- No protocol, SAP, or administrative pages were opened. Source PDFs were not modified.

## Candidate issues

### FFC-01 - Primary composite outcome analysis unit is labeled inconsistently

- **Category:** Presentation inconsistency
- **Locations:**
  - DOC-001, `jama_kumar_2025_oi_250034_1750956984.08518.pdf`, source-PDF p. 4, Figure 1, terminal boxes.
  - DOC-001, source-PDF p. 6, Results, "Primary and Secondary Outcomes," first sentence.
  - DOC-001, source-PDF p. 8, Figure 2, column header and Overall row.
  - DOC-004, `joi250034supp3_prod_1750956984.12018.pdf`, source-PDF p. 3, Supplementary Table 2, Primary outcome rows; compare DOC-001 p. 7, "Site-Specific Differences."
- **Source evidence:** Figure 1 labels the final analysis counts as **"1625 Infants with primary outcome"** in each arm. The p. 6 prose reports the identical outcome counts as **"83 of 1625 women (5.1%)"** and **"84 of 1625 women (5.2%)."** Figure 2 again displays 83/1625 and 84/1625, but its header calls the denominator **"total No. of patients."** Supplementary Table 2 partitions those same primary-outcome denominators into 883 + 742 = 1625 and 887 + 738 = 1625, while the linked DOC-001 p. 7 prose describes the site-specific values as 16/883 and 24/887 **women**.
- **Logical basis:** The same 1625-per-arm primary-outcome denominators are explicitly identified as infants in Figure 1 but as women/patients in nearby reporting. The distinction is material because the article separately reports 1626 and 1631 randomized women and 1634 and 1641 infants, and models infant outcomes with adjustment for multiple births. This is a document-verifiable unit-label conflict, not an inference from the plot pattern.
- **Verification instruction:** On the cited original pages, confirm the intended analysis unit for the primary composite and harmonize "infants," "women," and "patients" in the Results prose, Figure 2 header, and site-specific prose/table labeling.

### FFC-02 - Table 1 and nearby prose use different denominators for two placebo ethnicity percentages

- **Category:** Presentation inconsistency
- **Locations:**
  - DOC-001, `jama_kumar_2025_oi_250034_1750956984.08518.pdf`, source-PDF p. 5, Table 1, Ethnicity rows.
  - DOC-001, source-PDF p. 4, Results, "Participants and Adherence," ethnicity paragraph.
- **Source evidence:** Table 1 labels placebo ethnicity data as **n = 1629** and reports Australia/New Zealand as **874 (53.7%)** and Pacific Islander as **53 (3.3%)**. The nearby prose describes the full placebo cohort of **1631 participants**, includes **2 (0.1%) missing**, and reports the same category counts as **874 (53.6%)** and **53 (3.2%)**.
- **Logical basis:** The displayed percentage pairs correspond to different visible denominators: 874/1629 = 53.65% and 53/1629 = 3.25% (Table 1 rounding), whereas 874/1631 = 53.59% and 53/1631 = 3.25% (prose rounding to 53.6% and 3.2%). Counts agree, but the denominator convention and resulting percentages are not harmonized between the table and text.
- **Verification instruction:** Confirm whether ethnicity percentages should use nonmissing n = 1629 or the randomized placebo total n = 1631 including the 2 missing observations, then make the table and prose use one stated convention.

## Checked items that passed

| Location | Visual/count check | Result |
|---|---|---|
| DOC-001 p. 4, Figure 1 | Recruitment and allocation: 3748 eligible - 491 excluded = 3257 randomized; 1626 + 1631 = 3257. | Passed. |
| DOC-001 p. 4, Figure 1 | Assigned-treatment counts: 1552 + 74 = 1626 and 1555 + 76 = 1631. The sildenafil no-treatment reasons sum to 16 + 11 + 4 + 2 + 2 + 39 = 74; placebo reasons sum to 14 + 10 + 6 + 2 + 44 = 76. | Passed. |
| DOC-001 p. 4, Figure 1 and adjacent Results | Consent/follow-up pathway: complete withdrawals 4 + 2 and future-data withdrawals 1 + 2 total 9, matching 3257 - 9 = 3248 women in the text. Starting infant totals 1634 and 1641 reconcile to 1625 and 1627 followed infants when the displayed complete withdrawals, losses, and future-data withdrawals are applied; 2 incomplete placebo records then yield 1625 primary-outcome records. | Passed. |
| DOC-001 p. 8, Figure 2 | Every subgroup pair partitions the overall 1625-per-arm denominator and event total: for example, small-for-gestational-age denominators 106 + 1519 = 1625 and 105 + 1520 = 1625, with events 10 + 73 = 83 and 13 + 71 = 84. The same reconciliation holds for multiple pregnancy, preeclampsia, preceding cesarean, noncephalic presentation, and postnatal fetal anomaly. | Passed. |
| DOC-001 p. 8, Figure 2 | Forest-plot direction and labels: the effect is sildenafil/placebo RR; values below 1 are plotted on the "Favors sildenafil citrate" side and values above 1 on the "Favors placebo" side. Visible points and CIs align with the printed estimates, including wide CIs for sparse subgroups. | Passed. |
| DOC-001 pp. 5-8, Tables 1-4 | Titles, row labels, units, footnote markers, and table boundaries are legible and not visibly clipped. Table 2 birth-mode counts partition 1629 sildenafil infants and 1637 placebo infants; Table 3/Table 4 secondary and tertiary outcome counts align with nearby prose apart from the unit-label issue above. | Passed. |
| DOC-004 p. 2, Supplementary Table 1 | Header totals 1634 and 1641 reconcile with outcome denominators plus displayed missing values; model and imputation footnotes are present and attached to the visible markers. Main-text sensitivity estimates match the table. | Passed. |
| DOC-004 pp. 3-5, Supplementary Table 2 | The continuation preserves the same columns and site labels. Site-stratified counts sum to the corresponding DOC-001 totals, including primary outcome 16 + 67 = 83 and 24 + 60 = 84, spontaneous vaginal birth 494 + 370 = 864 and 521 + 410 = 931, and postpartum hemorrhage 73 + 91 = 164 and 72 + 56 = 128. | Passed. |
| DOC-004 p. 6, Supplementary Table 3 vs DOC-001 p. 4, Figure 1 | Safety denominators are coherent with treatment received: sildenafil N = 1552; placebo N = 1557 equals 1555 assigned placebo plus 2 sildenafil-assigned participants who received placebo by mistake. The footnoted 148 untreated women equals 74 + 76 - 2 crossover recipients. | Passed. |

## Handoff

- Candidate issues returned: **2**, both within the allowed `Presentation inconsistency` category.
- No ambiguous visual pattern was treated as contradictory.
