# Table Arithmetic and Internal-Consistency Check

## Scope and method

- Audited only result-relevant tables designated in the package manifest and evidence maps: DOC-001 Tables 3 and 4 (source-PDF pp. 7-8); DOC-004 Supplementary Tables 1-3 (source-PDF pp. 2-6).
- Used the retained native-text extracts and rendered page images; rendered values were checked against the table layout where text extraction was ambiguous.
- Checked visible numerators, denominators, displayed percentages, within-table component sums, selected raw risk-ratio/difference arithmetic, and duplicated results across DOC-001 and DOC-004. Model-derived estimates were not treated as discrepant solely because they differ from unadjusted arithmetic when the table identifies the model.

## Candidate issues

None identified. No document-verifiable arithmetic, denominator, percentage, component-total, or duplicated-value inconsistency met the reporting threshold.

## Checked items that passed

| Location | Check and source values | Calculation / result |
|---|---|---|
| DOC-001 PDF p. 7, Table 3, primary outcome | 83/1625 (5.1%) vs 84/1625 (5.2%). | 83/1625 = 5.108% -> 5.1%; 84/1625 = 5.169% -> 5.2%; displayed absolute difference rounds to -0.1 percentage points. The reported RR 1.02 is explicitly GEE-adjusted, so it need not equal the crude ratio (0.988). |
| DOC-001 PDF p. 7, Table 3, all secondary rows | Each displayed numerator/denominator percentage was recalculated, including 5/1629, 12/1629, 50/1629, 37/1629, 9/1629, and the matching placebo values. | All displayed one-decimal percentages match ordinary rounding; displayed absolute differences agree with the rounded group percentages/counts. Rows labelled `NA` have zero events in both columns. |
| DOC-001 PDF p. 7, Table 3 vs DOC-001 PDF p. 8, Table 4 | Emergency cesarean delivery or IVB for fetal distress: 343/1629 vs 307/1637 in Table 3; Table 4 components are cesarean 142/1629 vs 129/1637 and IVB 201/1629 vs 178/1637. | 142 + 201 = 343 and 129 + 178 = 307; denominators agree. |
| DOC-001 PDF p. 8, Table 4 | Infant-level rows: emergency operative birth with fetal distress a factor 471/1629 vs 431/1637, split into cesarean 233/1629 vs 201/1637 and IVB 238/1629 vs 230/1637. | 233 + 238 = 471 and 201 + 230 = 431. Other displayed percentages and crude risk/difference directions are consistent with their values. |
| DOC-001 PDF p. 8, Table 4 vs DOC-004 PDF pp. 4-5, Supplementary Table 2 | Site-stratified tertiary results: spontaneous vaginal birth 494 + 370 = 864 and 521 + 410 = 931; postpartum hemorrhage 73 + 91 = 164 and 72 + 56 = 128. Corresponding denominators: 883 + 746 = 1629, 887 + 750 = 1637; postpartum denominators 880 + 741 = 1621 and 882 + 745 = 1627. | Reconciles exactly to DOC-001 Table 4. E.g., 91/741 = 12.28% -> 12.3%; 56/745 = 7.52% -> 7.5%; crude RR = 1.634 -> 1.63. |
| DOC-004 PDF p. 2, Supplementary Table 1 | Imputed 10-component composite: 85 + 1540 = 1625 and 87 + 1538 = 1625; each group has 9 and 16 additional missing records, respectively. Nine-component and 10-component GLM rows similarly show 75 + 1550 = 1625 / 80 + 1545 = 1625 and 83 + 1542 = 1625 / 84 + 1541 = 1625. | Category totals and percentages reconcile; 1625 + 9 = 1634 and 1625 + 16 = 1641. Cord-pH categories also reconcile: 14 + 1211 + 404 = 1629 and 8 + 1154 + 475 = 1637, plus 5 and 4 missing records. |
| DOC-004 PDF pp. 3-5, Supplementary Table 2 vs DOC-001 PDF p. 7, Table 3 | Primary outcome: 16 + 67 = 83 / 883 + 742 = 1625 and 24 + 60 = 84 / 887 + 738 = 1625. Secondary outcomes reconcile to Table 3: Apgar 1 + 4 = 5 and 1 + 2 = 3; cord pH 2 + 10 = 12 and 2 + 3 = 5; respiratory support 5 + 32 = 37 and 17 + 30 = 47; unit admission 11 + 39 = 50 and 13 + 48 = 61; pulmonary hypertension 0 + 1 = 1 and 1 + 2 = 3; meconium 1 + 8 = 9 and 2 + 3 = 5. | All numerators and the outcome-specific denominators reconcile exactly. Reported site-specific RRs are consistent with raw counts to displayed precision (for example 16/883 divided by 24/887 = 0.670 -> 0.67; 91/741 divided by 56/745 = 1.634 -> 1.63). |
| DOC-004 PDF p. 6, Supplementary Table 3 | Every yes/no pair was checked against N=1552 sildenafil and N=1557 placebo, including headache 3 + 1549 / 7 + 1550, dizziness 0 + 1552 / 5 + 1552, reflux 2 + 1550 / 1 + 1556, and hypo/paraesthesia 1 + 1551 / 1 + 1556. | All category counts equal the stated treatment-group denominator and visible percentages are correctly rounded. Zero-event rows correctly display 100.0% in the complementary `No` row. |

## Notes for downstream review

- DOC-001 Table 3 identifies generalized estimating equations adjusted for multiple births; DOC-004 Supplementary Table 1 distinguishes GEE from GLM; DOC-004 Supplementary Table 2 identifies log-binomial regression. Small differences between crude count ratios and reported model estimates are therefore explained by table footnotes and are not candidates.
- No protocol, SAP, or administrative table was opened or audited.

