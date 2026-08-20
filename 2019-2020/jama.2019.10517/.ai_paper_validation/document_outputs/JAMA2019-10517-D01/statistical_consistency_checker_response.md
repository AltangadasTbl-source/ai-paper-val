# Statistical consistency checker response

## Scope and evidence used

- Main-text evidence map: `JAMA2019-10517-D01/main_text_extractor_response.yaml`.
- Results-supplement evidence map: `JAMA2019-10517-D03/results_supplement_extractor_response.md`.
- Page-linked native text and rendered pages for D01 PDF pages 1, 6–9 and D03 PDF pages 2–10.
- Protocol/SAP material was not opened or used.
- Checks covered point estimate versus confidence interval, confidence interval versus the applicable null and reported P value, effect direction, repeated estimates/CIs/P values, group and subgroup labels, and directly calculable count/percentage relationships.

## Candidate 1

**Issue statement.** In Table 5, each of the total-cholesterol and LDL rows reports an absolute unadjusted between-group difference of 4.3%, although the displayed counts/denominators yield 4.4% after rounding to the table's one-decimal precision.

- **Category:** Arithmetic inconsistency
- **Severity:** Low
- **Status:** Candidate for evidence verification

### Exact evidence

1. **Reported values:** JAMA2019-10517-D01, `jama_flint_2019_oi_190079.pdf`, PDF p9 (printed p630), Table 5, columns “Sertraline Plus, No. (%)” and “Absolute Unadjusted Difference Between Groups, % (95% CI)”:
   - Total cholesterol row: olanzapine `9 (14.1)`, placebo `6 (9.7)`, reported difference `4.3 (−8 to 17.2)`.
   - LDL row: olanzapine `9 (14.1)`, placebo `6 (9.7)`, reported difference `4.3 (−8 to 17.2)`.
   - The column denominators are olanzapine `n = 64` and placebo `n = 62`.
2. **Comparator derived from the same table:** for either row, the unadjusted absolute risk difference from the displayed counts is

   `100 × [(9/64) − (6/62)]`

   `= 100 × (0.140625 − 0.09677419)`

   `= 4.38508 percentage points`

   `= 4.4 percentage points` at one decimal.

   Direct subtraction of the table's displayed percentages also gives `14.1 − 9.7 = 4.4` percentage points.

### Reasoning and tolerance

The table labels the quantity as the **absolute unadjusted difference between groups**, so the direct difference in the two displayed proportions is the document-grounded comparator. At one-decimal precision, 4.38508 rounds to 4.4, not 4.3. The discrepancy is 0.1 percentage point and is repeated in two rows with identical inputs. No confidence-interval symmetry assumption is used; the reported 95% CI is not recalculated.

### Bounded impact

The point difference is understated by 0.1 percentage point in two Table 5 rows. This does not change the accompanying “no statistically significant differences” statement because each reported CI spans the null value of 0; the finding is limited to the displayed point difference.

### Human verification steps

1. Open D01 PDF p9 (printed p630), Table 5, and confirm the two rows, denominators, percentages, and reported `4.3` values.
2. Compute `100 × [(9/64) − (6/62)]`.
3. **Confirm** the issue if the unadjusted difference is 4.38508 percentage points and the intended display precision is one decimal (4.4). **Resolve/reject** it if the authors used a different explicitly documented estimator for the point difference; no such documentation was located in the audited article/results-supplement evidence.

## Candidate 2

**Issue statement.** The HbA1c treatment-by-linear-time estimate and CI are labeled in `mg/dL` in the abstract and Results, whereas the same outcome is labeled in `%` in Table 4 and the results supplement's eFigure 8.

- **Category:** Presentation inconsistency
- **Severity:** Low
- **Status:** Candidate for evidence verification

### Exact evidence

1. **Reported unit in abstract:** JAMA2019-10517-D01, `jama_flint_2019_oi_190079.pdf`, PDF p1 (printed p622), abstract, Results: `“or HbA1c levels (−0.0002 mg/dL; 95% CI, −0.0021 to 0.0016).”`
2. **Repeated reported unit in main Results:** D01, PDF p7 (printed p628), Secondary Outcomes: `“or HbA1c levels (−0.0002 mg/dL [95% CI, −0.0021 to 0.0016], adjusted P = .99).”`
3. **Comparator unit in the main article:** D01, PDF p8 (printed p629), Table 4, HbA1c row label: `“HbA1c, %”`.
4. **Comparator unit in the results supplement:** JAMA2019-10517-D03, `joi190079supp2_prod.pdf`, PDF p9, eFigure 8, y-axis label: `“HbA1c (%)”`.

### Reasoning and tolerance

The same named outcome is assigned two different dimensions within the supplied article package: `mg/dL` for the model estimate/CI and `%` for the main-article table and supplementary model-trajectory axis. An effect estimate and its CI must be labeled in the modeled outcome's unit. This is a direct unit-label comparison and does not depend on a model form, confidence-interval symmetry, or external clinical knowledge. The package does not establish whether only the unit label is wrong or whether any numerical rescaling is also required.

### Bounded impact

The inconsistency makes the scale of the HbA1c treatment-by-time effect ambiguous. It does not, by itself, challenge the numerical estimate, CI, direction, or nonsignificance: the point estimate lies inside the CI, the CI includes the null value 0, and adjusted `P = .99` is directionally consistent with that interval.

### Human verification steps

1. Compare the HbA1c result in D01 PDF p1 and PDF p7 with the HbA1c row label in D01 Table 4 (PDF p8).
2. Open D03 PDF p9, eFigure 8, and confirm that its y-axis is labeled `HbA1c (%)`.
3. **Confirm** the issue if the abstract/Results say `mg/dL` while Table 4 and eFigure 8 say `%`. **Resolve** it by consulting the authors' intended model output/unit; the supplied results package does not identify whether the correction is label-only.

## Checks with no additional candidate

- The primary HR `0.25` lies within `0.13–0.48`; the CI excludes the HR null of 1 and `P < .001` is concordant. The repeated abstract and Results values agree.
- The sensitivity HR `0.22` lies within `0.11–0.43`; the CI excludes 1 and `P < .001` is concordant.
- Covariate HRs and labels are internally concordant: young vs old `0.78 (0.42–1.46), P=.44`; remission vs near-remission `2.45 (0.98–6.13), P=.06`; and the three site-vs-Cornell contrasts all have CIs spanning 1 with nonsignificant P values.
- Each anthropometric/metabolic point estimate lies within its reported CI. Outcomes whose CIs exclude 0 (weight, waist circumference, total cholesterol) have significant adjusted P values and reported directions matching their signs; outcomes whose CIs include 0 have nonsignificant adjusted P values. The HbA1c unit issue above is separate.
- Simpson-Angus `0.022 (0.009–0.036), adjusted P=.009` is internally concordant and its positive direction matches D03 eFigure 9.
- D03 eFigures 1–5 and 7–9 do not supply exact point labels or identify the shaded-band statistic, so no numerical CI reconstruction was attempted. Their displayed group labels and qualitative directions do not add another verifiable inconsistency after accounting for the main article's stated linear-plus-quadratic time model.

**Candidate count:** 2
