# Human Adjudication Report — JAMA-2019-10517

## Package and document scope

This report contains the three findings retained by the critic after one verification stage; no new findings were added. Source PDFs were not modified. Scientific audit scope: D01 main article, PDF pages 1–10; D03 results supplement, PDF pages 1–10. D02 (protocol) and D04 (administrative data-sharing statement) were **Not Audited by Design** for scientific findings; their explicit records are [D02 record](document_outputs/JAMA2019-10517-D02/not_audited_by_design.md) and [D04 record](document_outputs/JAMA2019-10517-D04/not_audited_by_design.md).

| Document ID | Filename | Classification | Scientific-processing status |
|---|---|---|---|
| JAMA2019-10517-D01 | `jama_flint_2019_oi_190079.pdf` | Main article | Targeted preprocessing and scientific audit completed (PDF pages 1–10). |
| JAMA2019-10517-D02 | `joi190079supp1_prod.pdf` | Protocol / data analytic plan | Not Audited by Design; protocol excluded from default scientific audit. |
| JAMA2019-10517-D03 | `joi190079supp2_prod.pdf` | Results supplement | Targeted preprocessing and scientific audit completed (PDF pages 1–10). |
| JAMA2019-10517-D04 | `joi190079supp3_prod.pdf` | Administrative data-sharing statement | Not Audited by Design; administrative material excluded from default scientific audit. |

## Scientific issues for adjudication

### 1. Table 5 displays an absolute unadjusted difference 0.1 percentage point below the exact-count rounded value in two rows

**Category:** Arithmetic inconsistency  
**Severity:** Minor

**Issue statement:** In Table 5, the total-cholesterol and LDL rows each report an absolute unadjusted difference of `4.3%` for `9/64` versus `6/62`, although the exact percentage-point difference rounds to `4.4%` at the table’s one-decimal precision; this affects the displayed point estimates in both rows.

**Evidence and exact locations**

- **Total cholesterol — reported:** D01, `jama_flint_2019_oi_190079.pdf`, PDF page 9 (printed p 630), Table 5, row `Cholesterol—Total (≥1 value above both participant's RCT baseline and 240 mg/dL)`, columns `Sertraline Plus, No. (%)—Olanzapine (n = 64)`, `Placebo (n = 62)`, and `Absolute Unadjusted Difference Between Groups, % (95% CI)`: olanzapine `9 (14.1)`, placebo `6 (9.7)`, difference `4.3 (−8 to 17.2)`.
- **LDL — reported:** D01, same file/page/table/columns, row `LDL (≥1 value above both participant's RCT baseline and 160 mg/dL)`: olanzapine `9 (14.1)`, placebo `6 (9.7)`, difference `4.3 (−8 to 17.2)`.

**Direct comparison:** Reported in each row: `4.3%`. Comparator from the displayed counts and denominators: `4.385080645` percentage points, which rounds to `4.4%` at one decimal. Discrepancy: reported value is `0.1` percentage point lower.

**Reproducible calculation and tolerance:** Inputs `9/64` and `6/62`; formula `100 × [(9/64) − (6/62)]`; result `100 × (0.140625 − 0.0967741935) = 4.385080645` percentage points. Component check: `100 × 9/64 = 14.0625% → 14.1%`; `100 × 6/62 = 9.677419% → 9.7%`. Under nearest-tenth rounding, `4.4` represents `[4.35, 4.45)` and contains `4.385080645`; `4.3` represents `[4.25, 4.35)` and excludes it.

**Bounded impact:** Correction or confirmation is needed for the two displayed Table 5 point differences only. This evidence does not challenge the displayed event counts, denominators, confidence intervals, or the article’s no-significant-group-difference statement.

**Verification instructions**

1. Check D01 PDF page 9 (printed p 630), Table 5, and confirm both cited rows display `9 (14.1)`, `6 (9.7)`, and `4.3 (−8 to 17.2)` under denominators `64` and `62`.
2. Calculate `100 × [(9/64) − (6/62)]`; approximately `4.38508` percentage points confirms the exact-count comparator.
3. Round once to one decimal; `4.4`, rather than `4.3`, confirms the display inconsistency. A documented estimator or rounding convention that validly yields `4.3` from these reported inputs resolves it.

### 2. The placebo hospitalization percentage among relapse participants is rounded 0.1 percentage point below the exact proportion

**Category:** Arithmetic inconsistency  
**Severity:** Minor

**Issue statement:** The article reports `11 (32.3%) of 34` placebo-group participants who relapsed required psychiatric hospitalization, although `11/34` rounds to `32.4%` at one decimal; this affects the reported placebo percentage only.

**Evidence and exact location:** D01, `jama_flint_2019_oi_190079.pdf`, PDF page 8 (printed p 629), `Adverse Effects`, paragraph continuing at the top of the right column immediately before `Discussion`: `“6 (46.2%) of 13 in the olanzapine group and 11 (32.3%) of 34 in the placebo group”` required psychiatric hospitalization because of relapse.

**Direct comparison:** Reported placebo percentage: `32.3%`. Comparator from the numerator and denominator in the sentence: `32.35294118%`, which rounds to `32.4%` at one decimal. Discrepancy: reported value is `0.1` percentage point lower. Internal comparison: the sentence’s olanzapine value is consistent with nearest-tenth rounding: `6/13 × 100 = 46.15384615% → 46.2%`.

**Reproducible calculation and tolerance:** Inputs `11` hospitalizations among `34` placebo-group relapse participants; formula `100 × 11/34`; result `32.35294118%`. Under nearest-tenth rounding, `32.4` represents `[32.35, 32.45)` and contains the result; `32.3` represents `[32.25, 32.35)` and excludes it.

**Bounded impact:** Correction or confirmation is needed for the placebo percentage. The reported numerator, denominator, hospitalization count, and substantive statement are not changed by this evidence.

**Verification instructions**

1. Check D01 PDF page 8 (printed p 629), top of the right column immediately before `Discussion`, and confirm `11 (32.3%) of 34` for placebo and `6 (46.2%) of 13` for olanzapine.
2. Calculate `100 × 11/34`; approximately `32.35294%` confirms the comparator.
3. Round once to one decimal; `32.4%`, rather than `32.3%`, confirms the inconsistency. Confirming `100 × 6/13 = 46.15385% → 46.2%` corroborates nearest-tenth rounding; a documented alternate convention resolves the issue otherwise.

### 3. The HbA1c treatment-by-time estimate has conflicting displayed units

**Category:** Presentation inconsistency  
**Severity:** Minor

**Issue statement:** The abstract and Results label the HbA1c treatment-by-linear-time estimate and confidence interval in `mg/dL`, while Table 4 and eFigure 8 label the same HbA1c outcome in `%`; this creates a unit-label conflict for a repeated secondary-outcome estimate.

**Evidence and exact locations**

- **Main-text unit, abstract:** D01, `jama_flint_2019_oi_190079.pdf`, PDF page 1 (printed p 622), abstract, `RESULTS`: `“HbA1c levels (−0.0002 mg/dL; 95% CI, −0.0021 to 0.0016)”`.
- **Main-text unit, Results:** D01, same file, PDF page 7 (printed p 628), `Secondary Outcomes`, right-column paragraph: `“HbA1c levels (−0.0002 mg/dL [95% CI, −0.0021 to 0.0016], adjusted P = .99)”`. The paragraph identifies this quantity as the effect on the `daily rate` and the `treatment × linear time interaction`.
- **Comparator scale, table:** D01, same file, PDF page 8 (printed p 629), Table 4, row `HbA1c, %`: olanzapine baseline `5.9 (1.5)`, termination `5.7 (1.1)`; placebo baseline `5.9 (1.2)`, termination `5.9 (1.0)`.
- **Comparator scale, figure:** D03, `joi190079supp2_prod.pdf`, PDF page 9, `eFigure8. Mixed Model Estimated Least Square Means of HbA1c in Randomized Groups in the STOP-PD II Clinical Trial`: y-axis `HbA1c (%)`; x-axis `Day`.

**Direct comparison:** Reported coefficient and CI unit in two main-text locations: `mg/dL`. Comparator unit for the named outcome in Table 4 and corresponding eFigure 8: `%`. The package supplies no conversion reconciling these dimensions.

**Reproducible logical chain and tolerance:** (1) D01 page 7 defines `−0.0002` as a treatment-by-linear-time effect on the daily rate of HbA1c. (2) D01 Table 4 labels HbA1c `%`. (3) D03 eFigure 8 plots `HbA1c (%)` against `Day`. (4) A rate coefficient inherits the modeled outcome dimension per time dimension unless a conversion is stated; the package does not state one. Therefore the supplied evidence establishes a unit-label conflict. Numerical rounding tolerance is not applicable to a categorical unit conflict.

**Bounded impact:** Correction or confirmation is needed for the unit of one secondary-outcome estimate and CI repeated in two main-text locations. The supplied package does not establish whether the correction is label-only or requires numerical rescaling; it does not establish that the numerical estimate, CI, adjusted `P = .99`, or no-difference conclusion is wrong.

**Verification instructions**

1. Check D01 PDF page 1, abstract `RESULTS`, and D01 PDF page 7, `Secondary Outcomes`; confirm the identical `−0.0002` estimate and `−0.0021 to 0.0016` CI are labeled `mg/dL`, and the latter describes a daily-rate treatment-by-linear-time effect.
2. Check D01 PDF page 8, Table 4, row `HbA1c, %`, and D03 PDF page 9, eFigure 8; confirm the percentage row label and `HbA1c (%)` y-axis over `Day`.
3. Confirm that all locations concern the same HbA1c outcome. The conflicting displayed dimensions confirm the presentation inconsistency.
4. To determine the correction, check the model-output variable definition or an authoritative publisher correction: a stated conversion could support rescaling, while confirmation that the outcome was modeled directly in percentage units supports a percentage-scale rate label. Without that evidence, do not decide between label-only correction and numerical rescaling.

## AI Training Restriction Summary

This separate compliance screen is not a legal opinion and is not part of the scientific issue list. It searches supplied PDFs and embedded metadata only. No permission is inferred from silence.

| Document ID | Status | Exact evidence location and supplied-file evidence | Human Compliance Review |
|---|---|---|---|
| JAMA2019-10517-D01 | No AI Training Restriction Located in Provided Materials | `jama_flint_2019_oi_190079.pdf`, PDF page 1 footer (repeated on PDF pages 2–10): `© 2019 American Medical Association. All rights reserved.`; PDF page 10 end matter/footer; document-information and XMP metadata. The record states this general copyright language does not expressly address AI training, fine-tuning, or model improvement. | No — no explicit restriction or permission-required condition located; not an affirmative permission determination. |
| JAMA2019-10517-D02 | No AI Training Restriction Located in Provided Materials | `joi190079supp1_prod.pdf`, PDF page 1 title/contents; PDF page 42 end matter; embedded document-information and XMP metadata; targeted search of the 42-page text layer. No supplied-file language addressing AI training, fine-tuning, or model improvement was located. | No — no explicit restriction or permission-required condition located; no permission inferred from silence. |
| JAMA2019-10517-D03 | No AI Training Restriction Located in Provided Materials | `joi190079supp2_prod.pdf`, PDF page 1 and footers on PDF pages 2–10: `© 2019 American Medical Association. All rights reserved.`; embedded document-information/XMP metadata. The record classifies this as general copyright, not an express AI-training restriction or condition. | No — no explicit or conditional restriction located; not an affirmative permission determination. |
| JAMA2019-10517-D04 | No AI Training Restriction Located in Provided Materials | `joi190079supp3_prod.pdf`, PDF page 1, `Data Sharing Statement`, `Additional Information`: `Who can access the data: Researchers whose proposed use of the data has been approved.` and `Mechanisms of data availability: With investigator support. After approval of a proposal. With a signed data access agreement.` Embedded metadata was also screened. These are data-access conditions, not express terms on AI training, fine-tuning, or model improvement. | No — no explicit or conditional AI-training restriction located; no permission inferred from silence. |

## Submission status

**Submitted for Human Adjudication.** Three Minor scientific issues require the specified checks. No issue is classified `Uncertain`; the HbA1c card expressly leaves the intended numerical remedy unresolved because the supplied package does not determine it.
