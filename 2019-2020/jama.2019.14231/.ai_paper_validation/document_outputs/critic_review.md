# Critic Review of Evidence-Verifier Output

## Scope and final disposition

This review considered only the four findings in `evidence_verification.md` and checked their cited items in the supplied PDFs. It did not search for additional issues and did not use external information.

| Verifier finding | Final disposition | Category | Final severity |
|---|---|---|---|
| 1. Five absolute 8-year risk differences | **Retained** | Arithmetic inconsistency | **Minor** |
| 2. Primary-composite E-values | **Not retained** | — | — |
| 3. Time-varying-HR table citation | **Retained** | Presentation inconsistency | **Minor** |
| 4. “5-component MACE” primary-outcome label | **Retained** | Presentation inconsistency | **Minor** |

Final retained issue count: **3**.

No retained issue is classified as Major because the supplied documents do not show that any discrepancy changes the primary HR, its confidence interval, event counts, direction of association, or overall conclusion.

## Retained finding 1 — Five Table 2 risk-difference point estimates do not equal the displayed incidences under the table’s stated subtraction

**Issue statement.** Five rows in main-article Table 2 report absolute 8-year risk-difference point estimates that do not equal the displayed nonsurgical-control minus metabolic-surgery cumulative incidences, despite footnote a defining that subtraction.

**Category and severity.** Arithmetic inconsistency; **Minor**.

**Exact locations and source evidence.**

- `jama2019-14231-main-article`, `jama_aminian_2019_oi_190103.pdf`, PDF p. 7 (printed p. 1277), Table 2, columns “Cumulative Incidence at 8 y” and “Absolute 8-Year Risk Difference,” rows Heart failure, Coronary artery disease, Cerebrovascular disease, Nephropathy, and Atrial fibrillation.
- Same table, footnote a: “95% bootstrap CIs (1000 samples) for the difference in 8-year absolute risk (nonsurgical control group − metabolic surgery) for each outcome and treatment group.”
- `jama2019-14231-supplement-1`, `joi190103supp1_prod.pdf`, PDF p. 7, eTable 5, the same five outcomes and Year 8 surgical/nonsurgical cumulative-incidence columns; these repeat the Table 2 incidence inputs.

**Reported-versus-calculated comparison.**

| Outcome | Surgical incidence | Nonsurgical incidence | Calculation required by footnote | Calculated difference | Reported difference |
|---|---:|---:|---|---:|---:|
| Heart failure | 6.8% | 18.9% | 18.9 − 6.8 | 12.1 percentage points | 12.9% (95% CI, 10.4-15.1) |
| Coronary artery disease | 7.9% | 11.6% | 11.6 − 7.9 | 3.7 percentage points | 4.2% (95% CI, 1.9-6.8) |
| Cerebrovascular disease | 4.1% | 5.6% | 5.6 − 4.1 | 1.5 percentage points | 1.8% (95% CI, −0.03 to 3.4) |
| Nephropathy | 6.1% | 16.3% | 16.3 − 6.1 | 10.2 percentage points | 11.1% (95% CI, 8.8-13.6) |
| Atrial fibrillation | 7.9% | 13.6% | 13.6 − 7.9 | 5.7 percentage points | 6.5% (95% CI, 4.4-8.7) |

Each incidence is displayed to 0.1 percentage point. Subtracting two independently rounded inputs can change the result by less than 0.1 percentage point relative to the subtraction of the unrounded inputs. The observed gaps between the displayed subtraction and reported point estimate are 0.8, 0.5, 0.3, 0.9, and 0.8 percentage point, respectively, so displayed-value rounding does not reconcile them.

**Bounded impact.** The five absolute-risk-difference point estimates are not reproducible from the values and rule printed in Table 2. This is a table-level numerical reporting problem; it does not establish which underlying estimate is correct and does not show that the cumulative incidences, bootstrap confidence intervals, hazard ratios, or association directions are wrong.

**Human verification steps.**

1. On main-article PDF p. 7, transcribe the five surgical and nonsurgical incidences, adjacent risk differences, and footnote a.
2. For each row, subtract the displayed surgical incidence from the displayed nonsurgical incidence.
3. Confirm on Supplement 1 PDF p. 7, eTable 5, that the Year 8 incidence pairs are repeated.
4. The display-level inconsistency is confirmed if the five reported point estimates remain different from the stated subtraction beyond displayed rounding. Author calculation output identifying an additional estimand or calculation would be needed to determine which values should be corrected or clarified.

## Retained finding 2 — The time-varying-HR narrative cites eTable 4 although the described results are in eTable 7

**Issue statement.** The supplement’s time-varying-HR paragraph directs readers to eTable 4, which reports event rates, while eTable 7 contains the described adjusted HRs and 95% CIs at 2, 5, and 8 years.

**Category and severity.** Presentation inconsistency; **Minor**.

**Exact locations and source evidence.**

- `jama2019-14231-supplement-1`, `joi190103supp1_prod.pdf`, PDF p. 19, section B, Time-varying hazard ratios: “eTable 4 displays adjusted hazard ratios and 95% confidence intervals at 2, 5, and 8 years after the index date.”
- Same document, PDF p. 6, eTable 4 title: “Cause-Specific Event Rates (%) per 100 Patient-Years of Follow-up at 8 Years”; its columns report surgical and nonsurgical rates and event-rate differences.
- Same document, PDF pp. 10 and 19, eTable 7 title: “Time-Varying Hazard Ratios and 95% CIs at 2, 5, and 8 Years After the Index Date”; its columns are the 2-, 5-, and 8-year HRs and CIs. For example, the Primary row reports 0.57 (0.49, 0.65), 0.78 (0.66, 0.93), and 0.79 (0.64, 0.97).

**Direct logical comparison.** The narrative identifies adjusted hazard ratios, 95% CIs, and three time points. eTable 4 has none of that three-time-point HR structure, whereas eTable 7 matches all three described features. The cross-reference should therefore point to eTable 7.

**Bounded impact.** Readers are directed to the wrong table, but the time-varying HR values remain available in eTable 7 and are not shown to be numerically wrong.

**Human verification steps.**

1. Read the table-reference sentence on Supplement 1 PDF p. 19.
2. Compare the titles and columns of eTable 4 on PDF p. 6 and eTable 7 on PDF pp. 10 and 19.
3. The issue is confirmed if eTable 7, rather than eTable 4, contains the described 2-, 5-, and 8-year HRs; replacing “eTable 4” with “eTable 7” resolves it.

## Retained finding 3 — The E-value interpretation calls the defined six-component primary composite “5-component MACE”

**Issue statement.** The supplement’s interpretation of the primary-endpoint E-value calls the endpoint “5-component MACE,” while the main article defines the corresponding primary composite as six named outcomes.

**Category and severity.** Presentation inconsistency; **Minor**.

**Exact locations and source evidence.**

- `jama2019-14231-supplement-1`, `joi190103supp1_prod.pdf`, PDF p. 19, section C, E-Value: “the calculated E-value of 2.15 would mean that residual confounding could explain the observed association if there exists an unmeasured covariate having a relative risk association at least as large as 2.15 with both 5-component MACE and with metabolic surgery.”
- The preceding paragraph on the same page calls HR 0.61 (95% CI, 0.55-0.69) the association for the “primary outcome” and calls 2.15 the E-value for the “primary end-point.”
- Same supplement, PDF p. 20, eTable 12, labels the 2.15/1.92 row “Primary composite.”
- `jama2019-14231-main-article`, `jama_aminian_2019_oi_190103.pdf`, PDF p. 3 (printed p. 1273), section Primary and Secondary End Points: “The primary end point was the incidence of extended major adverse cardiovascular events (MACE, composite of 6 outcomes),” followed by all-cause mortality, coronary artery events, cerebrovascular events, heart failure, nephropathy, and atrial fibrillation. The six-component definition also appears on PDF p. 1 under Main Outcomes and Measures and on PDF p. 7 in the Figure 2 caption.

**Direct logical comparison.** The defined primary composite contains six components: (1) all-cause mortality, (2) coronary artery events, (3) cerebrovascular events, (4) heart failure, (5) nephropathy, and (6) atrial fibrillation. The supplement links its E-value interpretation to that primary endpoint and its HR but calls the endpoint five-component MACE. The supplied results material does not identify a separate five-component outcome for that E-value.

**Bounded impact.** The wording creates endpoint-label ambiguity but does not itself change the reported primary HR, CI, event counts, or six-component endpoint definition.

**Human verification steps.**

1. On main-article PDF p. 3, confirm “composite of 6 outcomes” and count the six listed components.
2. On Supplement 1 PDF p. 19, confirm “5-component MACE” and the immediately preceding references to the primary outcome, primary endpoint, HR 0.61, and E-value 2.15.
3. On Supplement 1 PDF p. 20, confirm that 2.15/1.92 are assigned to the “Primary composite” row.
4. The label mismatch is confirmed unless the authors identify a distinct five-component endpoint and its associated calculation; otherwise the phrase should name the defined six-component primary composite.

## Nonretained verifier finding

### Primary-composite E-values — not retained

**Reason for nonretention.** The verifier applied

`E(r) = 1/r + sqrt[(1/r) × (1/r − 1)]`

directly to the protective HR and upper CI limit and inferred that this same transformation must govern the primary row because it approximately reproduces the other seven rows. The supplied PDFs, however, do not state that formula, do not state that every endpoint uses an identical HR-to-risk-ratio treatment, and do not provide the primary calculation inputs beyond HR 0.61 (95% CI, 0.55-0.69) and the reported E-values 2.15/1.92. Thus the package does not establish that 2.66/2.26 are the required comparators or that 2.15/1.92 are erroneous. The cross-row pattern is not enough to replace missing calculation documentation.

**Missing evidence needed to reconsider.** A formula or analysis specification in the supplied package requiring the verifier’s direct transformation for the primary HR and CI, or author calculation output showing the exact transformation and inputs.

**Disposition.** Rejected from the final issue list as insufficiently document-grounded. This is not a conclusion that the reported E-values are correct; it is a conclusion that the supplied package does not establish the claimed inconsistency.
