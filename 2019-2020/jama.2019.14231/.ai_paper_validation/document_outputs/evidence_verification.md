# Evidence Verification

## Verification scope and disposition

- Verification stage: one.
- Verification rounds: two per candidate (native PDF text followed by visual confirmation of the cited original PDF pages).
- Sources: only the supplied article package and its page-linked derived artifacts; no external retrieval.
- Source PDFs were not modified.

| Candidate | Disposition | Category | Severity |
|---|---|---|---|
| 1. Five absolute 8-year risk differences | **Verified** | Arithmetic inconsistency | Moderate |
| 2. Primary-composite E-values | **Verified** | Statistical reporting inconsistency | Moderate |
| 3. Time-varying-HR table citation | **Verified** | Presentation inconsistency | Minor |
| 4. “5-component MACE” primary-outcome label | **Verified** | Presentation inconsistency | Moderate |

## Verified finding 1 — Five absolute 8-year risk differences conflict with the displayed inputs and stated subtraction

**Issue statement.** In five rows of Table 2, the reported absolute 8-year risk-difference point estimate does not equal the displayed nonsurgical minus surgical 8-year cumulative incidences, although the table footnote defines that subtraction and Supplement 1 eTable 5 repeats the incidence inputs.

**Category and severity.** Arithmetic inconsistency; Moderate.

**Exact locations.**

- `jama2019-14231-main-article`, `jama_aminian_2019_oi_190103.pdf`, PDF p. 7 (printed p. 1277), Table 2, rows Heart failure, Coronary artery disease, Cerebrovascular disease, Nephropathy, and Atrial fibrillation; columns “Cumulative Incidence at 8 y” and “Absolute 8-Year Risk Difference.”
- Same page, Table 2 footnote a: “difference in 8-year absolute risk (nonsurgical control group − metabolic surgery).”
- Confirming repeated inputs: `jama2019-14231-supplement-1`, `joi190103supp1_prod.pdf`, PDF p. 7, eTable 5, the same five rows, Year 8 Surgical Group and Nonsurgical Group columns.

**Reported values, comparators, and reproducible calculation.**

| Outcome | Surgical incidence | Nonsurgical incidence | Stated calculation | Calculated difference | Reported difference |
|---|---:|---:|---|---:|---:|
| Heart failure | 6.8% | 18.9% | 18.9 − 6.8 | 12.1 percentage points | 12.9% (95% CI, 10.4-15.1) |
| Coronary artery disease | 7.9% | 11.6% | 11.6 − 7.9 | 3.7 percentage points | 4.2% (95% CI, 1.9-6.8) |
| Cerebrovascular disease | 4.1% | 5.6% | 5.6 − 4.1 | 1.5 percentage points | 1.8% (95% CI, −0.03 to 3.4) |
| Nephropathy | 6.1% | 16.3% | 16.3 − 6.1 | 10.2 percentage points | 11.1% (95% CI, 8.8-13.6) |
| Atrial fibrillation | 7.9% | 13.6% | 13.6 − 7.9 | 5.7 percentage points | 6.5% (95% CI, 4.4-8.7) |

Supplement 1 eTable 5 repeats, respectively, the same Year 8 surgical/nonsurgical pairs: 6.8/18.9, 7.9/11.6, 4.1/5.6, 6.1/16.3, and 7.9/13.6.

**Rounding tolerance.** Each input is shown to 0.1 percentage point. Two independently rounded inputs can make their displayed subtraction differ from the unrounded subtraction by less than 0.1 percentage point. The observed absolute gaps are 0.8, 0.5, 0.3, 0.9, and 0.8 percentage point, so ordinary rounding cannot reconcile any row.

**Bounded impact.** The five local absolute-risk-difference point estimates require confirmation or correction. This finding does not establish that the cumulative incidences, their confidence intervals, Cox hazard ratios, or direction of association are wrong.

**Human verification steps.**

1. On main-article PDF p. 7, confirm the five pairs of cumulative incidences, the adjacent reported risk differences, and footnote a’s subtraction direction.
2. Repeat each displayed subtraction and apply a maximum 0.1-percentage-point rounding tolerance.
3. On Supplement 1 PDF p. 7, confirm that eTable 5 repeats the incidence inputs.
4. The finding is confirmed if no documented, unprinted estimator explains why the Table 2 point estimates differ from the stated subtraction; author analysis output showing a different valid estimand would resolve it.

## Verified finding 2 — Primary-composite E-values do not reproduce from the reported HR and upper CI limit

**Issue statement.** Supplement 1 reports primary-composite E-values of 2.15 and 1.92 for HR 0.61 and its upper 95% CI limit 0.69, but the risk-ratio-scale transformation that reproduces all seven other eTable 12 outcome rows yields approximately 2.66 and 2.26.

**Category and severity.** Statistical reporting inconsistency; Moderate.

**Exact locations.**

- `jama2019-14231-supplement-1`, `joi190103supp1_prod.pdf`, PDF p. 19, section C, E-Value: “the observed association ... on the primary outcome was HR of 0.61 [95% CI 0.55 to 0.69]”; the paragraph then gives risk-ratio E-values 2.15-fold for the estimate and 1.92-fold for the upper CI limit.
- Same document, PDF p. 20, eTable 12, Primary composite row: E-value for HR estimate **2.15** and E-value for upper limit of 95% CI **1.92**.
- Same document, PDF p. 9, eTable 6, Primary composite row: HR **0.61 (95% CI, 0.55-0.69)**. The remaining seven outcome HRs and upper limits used for the internal replication are in this table; their E-values are on PDF p. 20.

**Reported-versus-calculated comparison.** For a protective ratio `r < 1`, the transformation evidenced by the other rows is:

`E(r) = 1/r + sqrt[(1/r) × (1/r − 1)]`.

- Primary HR: `E(0.61) = 1/0.61 + sqrt[(1/0.61) × (1/0.61 − 1)] = 2.663`, or **2.66**, versus reported **2.15**.
- Primary upper CI limit: `E(0.69) = 2.256`, or **2.26**, versus reported **1.92**.

**Internal reproducibility basis.** Applying that same transformation to the seven other eTable 6 HR/upper-limit pairs produces values matching their eTable 12 entries to displayed-input rounding:

| Outcome | Calculated E-values | Reported eTable 12 E-values |
|---|---:|---:|
| Secondary composite, 0.62 / 0.72 | 2.607 / 2.124 | 2.62 / 2.11 |
| All-cause mortality, 0.59 / 0.72 | 2.780 / 2.124 | 2.81 / 2.13 |
| Heart failure, 0.38 / 0.49 | 4.704 / 3.498 | 4.69 / 3.52 |
| Coronary artery disease, 0.69 / 0.87 | 2.256 / 1.564 | 2.27 / 1.55 |
| Cerebrovascular disease, 0.67 / 0.94 | 2.350 / 1.324 | 2.35 / 1.31 |
| Nephropathy, 0.40 / 0.52 | 4.436 / 3.255 | 4.46 / 3.29 |
| Atrial fibrillation, 0.78 / 0.97 | 1.883 / 1.209 | 1.90 / 1.21 |

The primary discrepancies are much larger: 0.513 and 0.336. Rounding cannot reconcile them. Values that round to HR 0.61 yield E-values from approximately 2.635 to 2.692; values that round to upper limit 0.69 yield approximately 2.233 to 2.279.

**Logical basis.** The supplement says the E-value is expressed on the risk-ratio scale and identifies the two quantities as E-values for the HR and upper CI limit. The same transformation is empirically supported by all seven comparator rows. No primary-specific transformation is described in the supplied materials.

**Bounded impact.** The printed primary E-values portray less robustness to unmeasured confounding than the values implied by the reported primary HR/CI under the internally evidenced calculation. This finding does not alter the primary HR, CI, event counts, or direction of association.

**Human verification steps.**

1. Confirm HR 0.61 (95% CI, 0.55-0.69) on Supplement 1 pp. 9 and 19 and E-values 2.15/1.92 on pp. 19-20.
2. Apply the displayed formula to 0.61 and 0.69, then repeat it for the other seven eTable 6/eTable 12 rows.
3. Values near 2.66/2.26 for the primary row, together with replication of the other rows, confirm the reporting inconsistency.
4. A documented primary-specific HR-to-risk-ratio transformation or author calculation yielding 2.15/1.92 would resolve the finding.

## Verified finding 3 — The time-varying-HR narrative cites eTable 4 instead of eTable 7

**Issue statement.** The time-varying-HR paragraph points readers to eTable 4, but eTable 4 is an event-rate table and the described 2-, 5-, and 8-year hazard ratios are in eTable 7.

**Category and severity.** Presentation inconsistency; Minor.

**Exact locations and statements.**

- `jama2019-14231-supplement-1`, `joi190103supp1_prod.pdf`, PDF p. 19, section B, Time-varying hazard ratios: “**eTable 4 displays adjusted hazard ratios and 95% confidence intervals at 2, 5, and 8 years after the index date.**”
- Same page, immediately below that sentence, eTable 7 title: “**Time-Varying Hazard Ratios and 95% CIs at 2, 5, and 8 Years After the Index Date**”; it reports, for example, primary HRs 0.57 (0.49, 0.65), 0.78 (0.66, 0.93), and 0.79 (0.64, 0.97).
- Same document, PDF p. 6, eTable 4 title: “**Cause-Specific Event Rates (%) per 100 Patient-Years of Follow-up at 8 Years**”; its columns contain surgical/nonsurgical rates and event-rate differences, not time-varying HRs.
- Same document, PDF p. 10, eTable 7 contains the same time-varying-HR table reproduced on p. 19.

**Logical comparison.** The narrative specifies (1) adjusted hazard ratios, (2) 95% CIs, and (3) estimates at 2, 5, and 8 years. Only eTable 7 has all three features; eTable 4 has event rates only at 8 years. Therefore the cited table number is wrong.

**Bounded impact.** The values are available and consistently labeled in eTable 7, but the incorrect cross-reference directs readers to the wrong evidence. It does not change the reported time-varying HR values.

**Human verification steps.**

1. Read the table-reference sentence on Supplement 1 p. 19.
2. Compare the titles and columns of eTable 4 on p. 6 and eTable 7 on pp. 10 and 19.
3. The finding is confirmed if eTable 7, not eTable 4, contains the described HRs; changing “eTable 4” to “eTable 7” resolves it.

## Verified finding 4 — The E-value interpretation mislabels the six-component primary outcome as “5-component MACE”

**Issue statement.** The E-value interpretation calls the primary outcome “5-component MACE,” whereas the main article defines that primary outcome as a composite of six named outcomes and the same supplement ties the E-value paragraph to the primary-composite HR.

**Category and severity.** Presentation inconsistency; Moderate.

**Exact locations and statements.**

- `jama2019-14231-supplement-1`, `joi190103supp1_prod.pdf`, PDF p. 19, section C, E-Value: “the calculated E-value of 2.15 would mean ... an unmeasured covariate having a relative risk association at least as large as 2.15 with both **5-component MACE** and with metabolic surgery.”
- The preceding paragraph on the same page identifies this as the “primary outcome,” gives HR 0.61 (95% CI, 0.55-0.69), and calls 2.15 the “calculated E-value for the primary end-point.”
- Same document, PDF p. 20, eTable 12 labels the corresponding 2.15/1.92 row “Primary composite.”
- Comparator: `jama2019-14231-main-article`, `jama_aminian_2019_oi_190103.pdf`, PDF p. 3 (printed p. 1273), section Primary and Secondary End Points: “The primary end point was ... MACE, **composite of 6 outcomes**,” followed by all-cause mortality, coronary artery events, cerebrovascular events, heart failure, nephropathy, and atrial fibrillation.
- The six-component definition is repeated in the main article on PDF p. 1, Main Outcomes and Measures, and PDF p. 7, Figure 2 caption.

**Logical comparison.** The named primary components count to six: (1) all-cause mortality, (2) coronary artery events, (3) cerebrovascular events, (4) heart failure, (5) nephropathy, and (6) atrial fibrillation. The p. 19 E-value text explicitly links its interpretation to the primary HR and primary-endpoint E-value, yet calls that outcome five-component MACE. No separate five-component primary outcome or corresponding HR/E-value is identified in the supplied results material.

**Bounded impact.** The wording creates ambiguity about which endpoint the E-value interpretation concerns and could imply an unreported five-component outcome. It does not by itself alter the six-component primary-outcome HR or CI.

**Human verification steps.**

1. On main-article PDF p. 3, confirm “composite of 6 outcomes” and count the six named components.
2. On Supplement 1 p. 19, confirm “5-component MACE” and the preceding link to primary HR 0.61 and primary-endpoint E-value 2.15.
3. On Supplement 1 p. 20, confirm that 2.15/1.92 are labeled for the Primary composite.
4. The mismatch confirms the finding unless the authors identify a separate five-component endpoint and its calculation; changing the phrase to the defined six-component primary composite resolves the presentation inconsistency.
