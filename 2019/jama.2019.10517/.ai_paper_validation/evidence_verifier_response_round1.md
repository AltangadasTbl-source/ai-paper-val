# Evidence verifier response — round 1

Scope: verification of only the 3 candidates supplied by the coordinator. No new issues were searched for or added. Source PDFs were not modified. Exact pages were re-rendered directly from the supplied original PDFs and checked against the page-linked preprocessing artifacts/manifests.

## Candidate 1 — Verified (accept)

**Issue statement.** In both the total-cholesterol and LDL rows of Table 5, the reported absolute unadjusted difference of 4.3% for 9/64 versus 6/62 does not match the exact percentage-point difference, which rounds to 4.4 at the table's one-decimal precision.

- **Category:** Arithmetic inconsistency
- **Severity:** Minor
- **Source location:** JAMA2019-10517-D01, `jama_flint_2019_oi_190079.pdf`, PDF page 9 (printed page 630), Table 5, columns `Sertraline Plus, No. (%)` and `Absolute Unadjusted Difference Between Groups, % (95% CI)`.
- **Reported source values:**
  - Cholesterol, `Total (≥1 value above both participant’s RCT baseline and 240 mg/dL)`: olanzapine `9 (14.1)`, placebo `6 (9.7)`, reported difference `4.3 (−8 to 17.2)`.
  - `LDL (≥1 value above both participant’s RCT baseline and 160 mg/dL)`: olanzapine `9 (14.1)`, placebo `6 (9.7)`, reported difference `4.3 (−8 to 17.2)`.
- **Comparator/calculation:**  
  `100 × [(9 / 64) − (6 / 62)]`  
  `= 100 × (0.140625 − 0.0967741935)`  
  `= 4.385080645 percentage points`  
  At one decimal, conventional nearest-tenth rounding gives `4.4 percentage points`, not `4.3`. The displayed component percentages are themselves consistent with nearest-tenth rounding: `100 × 9/64 = 14.0625% → 14.1%` and `100 × 6/62 = 9.677419% → 9.7%`. As an internal rounding check, the table's triglyceride difference is `100 × [(4/64) − (2/62)] = 3.02419 → 3.0`, and its glucose difference is `100 × [(4/64) − (4/62)] = −0.20161 → −0.2`.
- **Rounding tolerance:** A value in `[4.35, 4.45)` rounds to `4.4` at one decimal; the exact value `4.38508` is inside that interval. A displayed value of `4.3` would require an underlying value below `4.35` under the same rule.
- **Bounded impact:** The displayed point difference is understated by `0.1 percentage point` in two rows that contain the same counts. The participant counts, displayed group percentages, confidence intervals, and the article's statement that no statistically significant group differences were observed are not changed by this correction.

**Human verification steps**

1. Open JAMA2019-10517-D01, `jama_flint_2019_oi_190079.pdf`, PDF page 9 (printed page 630), Table 5.
2. Confirm that both the total-cholesterol and LDL rows show `9 (14.1)`, `6 (9.7)`, and `4.3 (−8 to 17.2)`.
3. Calculate `100 × [(9/64) − (6/62)]`; a result of `4.385080645` confirms the exact percentage-point difference.
4. Round that result to one decimal; `4.4`, rather than `4.3`, confirms the inconsistency. If a documented nonstandard rounding/calculation rule producing 4.3 from these counts is found, the issue should be resolved against that rule.

## Candidate 2 — Verified (accept), with corrected PDF page

**Issue statement.** The placebo-group hospitalization percentage is reported as 32.3% for 11 of 34 relapse participants, although the exact proportion rounds to 32.4% at one decimal.

- **Category:** Arithmetic inconsistency
- **Severity:** Minor
- **Corrected source location:** JAMA2019-10517-D01, `jama_flint_2019_oi_190079.pdf`, **PDF page 8** (printed page 629), `Adverse Effects`, paragraph continuing at the top of the right column immediately before `Discussion`. The candidate supplied PDF page 9, but direct inspection places the statement on PDF page 8.
- **Reported statement:** `“Of the participants who experienced a relapse, 6 (46.2%) of 13 in the olanzapine group and 11 (32.3%) of 34 in the placebo group required psychiatric hospitalization because of the relapse.”`
- **Comparator/calculation:**  
  Placebo: `100 × 11 / 34 = 32.35294118%`, which rounds to `32.4%` at one decimal.  
  The same sentence provides an internal rounding comparator: `100 × 6 / 13 = 46.15384615%`, which rounds to the reported `46.2%`.
- **Rounding tolerance:** A value in `[32.35, 32.45)` rounds to `32.4` at one decimal; `32.35294118` is inside that interval. It does not round to `32.3` under conventional nearest-tenth rounding.
- **Bounded impact:** The placebo percentage is understated by `0.1 percentage point`. The numerator (`11`), denominator (`34`), hospitalization event count, and substantive statement that these participants required psychiatric hospitalization are unchanged.

**Human verification steps**

1. Open JAMA2019-10517-D01, `jama_flint_2019_oi_190079.pdf`, PDF page 8 (printed page 629), top of the right column immediately before the `Discussion` heading.
2. Confirm the reported values `11 (32.3%) of 34` and, in the same sentence, `6 (46.2%) of 13`.
3. Calculate `100 × 11/34`; `32.35294118%` confirms the exact placebo proportion.
4. Round to one decimal; `32.4%` confirms the inconsistency. Confirming that `100 × 6/13 = 46.15384615% → 46.2%` establishes that the adjacent percentage uses nearest-tenth rounding.

## Candidate 3 — Verified (accept)

**Issue statement.** The HbA1c treatment-effect estimate and confidence interval are labeled `mg/dL` in two main-text locations even though the same HbA1c outcome is labeled as a percentage in Table 4 and eFigure 8; for a daily-rate contrast plotted against Day, the compatible effect unit is percentage units per day, not mg/dL.

- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Reported-unit locations:**
  1. JAMA2019-10517-D01, `jama_flint_2019_oi_190079.pdf`, PDF page 1 (printed page 622), abstract, `RESULTS`: `“or HbA1c levels (−0.0002 mg/dL; 95% CI, −0.0021 to 0.0016).”`
  2. JAMA2019-10517-D01, `jama_flint_2019_oi_190079.pdf`, PDF page 7 (printed page 628), `Secondary Outcomes`, right-column paragraph: `“or HbA1c levels (−0.0002 mg/dL [95% CI, −0.0021 to 0.0016], adjusted P = .99).”` The surrounding text identifies these estimates as effects on the `daily rate` and as the `treatment × linear time interaction`.
- **Comparator-unit locations:**
  1. JAMA2019-10517-D01, `jama_flint_2019_oi_190079.pdf`, PDF page 8 (printed page 629), Table 4, row label: `“HbA1c, %”`. The row reports values on that scale, including olanzapine baseline `5.9 (1.5)` and termination `5.7 (1.1)`, and placebo baseline `5.9 (1.2)` and termination `5.9 (1.0)`.
  2. JAMA2019-10517-D03, `joi190079supp2_prod.pdf`, PDF page 9, `eFigure8. Mixed Model Estimated Least Square Means of HbA1c in Randomized Groups in the STOP-PD II Clinical Trial`, y-axis label `“HbA1c (%)”`; x-axis label `“Day”`.
- **Logical/dimensional basis:** All four locations name the outcome as HbA1c. Table 4 and eFigure 8 explicitly define its plotted/raw scale as `%`. eFigure 8 plots that percentage scale against `Day`, and D01 page 7 describes the reported estimate as a between-group difference in the daily rate (the treatment-by-linear-time interaction). Therefore the rate contrast must have dimensions of HbA1c percentage units per day (often expressed as percentage points/day). `mg/dL` is dimensionally incompatible with the `%` outcome scale shown in both the main table and the corresponding supplement figure. The identical estimate and CI in the abstract and Results repeat the same unit-label error.
- **Tolerance:** No numerical rounding tolerance resolves a categorical unit mismatch. The numerical estimate `−0.0002` and CI `−0.0021 to 0.0016` can remain unchanged while the unit label is corrected.
- **Bounded impact:** The error affects the stated unit of one secondary-outcome effect and CI in two main-text locations. It can cause readers to interpret an HbA1c percentage-scale daily-rate contrast as a mass-concentration difference. It does not alter the estimate, CI limits, adjusted `P = .99`, or the conclusion that the between-group daily rates were not statistically different.

**Human verification steps**

1. Open D01 PDF page 1, abstract `RESULTS`, and confirm that the HbA1c estimate and CI are followed by `mg/dL`.
2. Open D01 PDF page 7, `Secondary Outcomes`, and confirm the identical estimate/CI, the `mg/dL` label, and the surrounding description of a daily-rate treatment-by-time effect.
3. Open D01 PDF page 8, Table 4, and confirm the row label `HbA1c, %`.
4. Open D03, `joi190079supp2_prod.pdf`, PDF page 9, eFigure 8, and confirm y-axis `HbA1c (%)` and x-axis `Day`.
5. Confirm that these locations concern the same HbA1c outcome. A percent-scale outcome plotted over days confirms that its daily-rate contrast cannot have units of `mg/dL`; discovery of a source-specific transformation explicitly redefining this HbA1c outcome in mg/dL would be needed to resolve the issue otherwise.

## Round-1 disposition summary

| Candidate | Classification | Coordinator disposition |
|---|---|---|
| 1. Table 5 total cholesterol/LDL difference | Verified | Accept |
| 2. Placebo-relapse hospitalization percentage | Verified, with source corrected from PDF p9 to PDF p8 | Accept |
| 3. HbA1c effect/CI unit | Verified | Accept |

