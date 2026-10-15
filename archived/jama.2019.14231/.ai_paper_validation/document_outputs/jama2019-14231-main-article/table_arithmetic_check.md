# Table arithmetic and internal-consistency check

## Scope and sources inspected

- **Document ID:** `jama2019-14231-main-article`
- **Source PDF:** `jama_aminian_2019_oi_190103.pdf`
- **Scope:** PDF pages 1-12, restricted to result-relevant Table 2 and the visible result-table values cross-referenced in Supplement 1.
- **Supplementary comparator used:** `jama2019-14231-supplement-1`, `joi190103supp1_prod.pdf`, PDF page 7, eTable 5.
- **Not audited:** protocol and SAP material; no raw data were inferred or requested.

## Candidate 1 — five reported absolute 8-year risk differences conflict with the printed cumulative incidences

- **Category:** Arithmetic inconsistency
- **Severity:** Moderate (local numerical reporting error; direction and reported hazard ratios are unchanged)
- **Exact locations:**
  - `jama2019-14231-main-article`, `jama_aminian_2019_oi_190103.pdf`, PDF p7 (printed p1277), **Table 2**, rows *Heart failure*, *Coronary artery disease*, *Cerebrovascular disease*, *Nephropathy*, and *Atrial fibrillation*; columns *Cumulative Incidence at 8 y* and *Absolute 8-Year Risk Difference, % (95% CI)*.
  - Confirming repeated incidence values: `jama2019-14231-supplement-1`, `joi190103supp1_prod.pdf`, PDF p7, **eTable 5**, same five outcome rows and *Year 8* surgical/nonsurgical columns.
- **Source values and reproducible calculation:** Table 2 footnote a defines the risk difference as **nonsurgical control group − metabolic surgery**. Applying that displayed rule to the displayed estimates:

  | Outcome | Surgical 8-y incidence | Nonsurgical 8-y incidence | Calculation | Calculated difference | Reported Table 2 difference |
  |---|---:|---:|---|---:|---:|
  | Heart failure | 6.8% | 18.9% | 18.9 − 6.8 | 12.1 percentage points | 12.9% (95% CI, 10.4-15.1) |
  | Coronary artery disease | 7.9% | 11.6% | 11.6 − 7.9 | 3.7 percentage points | 4.2% (95% CI, 1.9-6.8) |
  | Cerebrovascular disease | 4.1% | 5.6% | 5.6 − 4.1 | 1.5 percentage points | 1.8% (95% CI, −0.03 to 3.4) |
  | Nephropathy | 6.1% | 16.3% | 16.3 − 6.1 | 10.2 percentage points | 11.1% (95% CI, 8.8-13.6) |
  | Atrial fibrillation | 7.9% | 13.6% | 13.6 − 7.9 | 5.7 percentage points | 6.5% (95% CI, 4.4-8.7) |

- **Rounding check:** Every incidence is printed to one decimal place. Treating each as rounded to the nearest 0.1 percentage point allows a displayed subtraction to differ from the exact subtraction by at most 0.1 percentage point. The observed discrepancies are 0.8, 0.5, 0.3, 0.9, and 0.8 percentage point, respectively; each exceeds that tolerance.
- **Reasoning:** These rows are inconsistent with the explicitly printed definition of their adjacent absolute-risk-difference column. The same 8-year incidence inputs are independently repeated in eTable 5, so the conflict is not attributable to one text-extraction artifact.
- **Bounded impact:** The affected local absolute-risk-difference point estimates require confirmation/correction. This check does not challenge the incidence values, their CIs, the hazard ratios, or the direction of the reported associations.
- **Human verification steps:**
  1. Read Table 2 footnote a and confirm that the displayed direction is nonsurgical control minus metabolic surgery.
  2. For each listed row, subtract the two Table 2 8-year incidences using the values above.
  3. Confirm the same incidence inputs in Supplement 1 eTable 5, PDF p7.
  4. Resolve the candidate if an author-supplied unprinted estimation rule produces the reported point estimates; otherwise the printed absolute-risk-difference values are inconsistent with their stated comparator rule.

## Checks completed without a candidate

- Table 2 primary, secondary, and all-cause-mortality rows: displayed risk differences equal the displayed nonsurgical minus surgical incidences (16.9, 10.6, and 7.8 percentage points).
- Supplement 1 eTable 4: all eight displayed rate-difference point estimates equal nonsurgical minus surgical rates to displayed precision.
- Supplement 1 eTables 5, 7 (including its exact duplicate on PDF p19), 8, 9, 10, and 11: no document-verifiable numerator/denominator, total, repeated-value, adjacent-column, or visible unit-conversion inconsistency was identified in the audited material.
- The eTable 10 baseline nonsurgical sample size (11,433) differs from the matched-cohort size (11,435), but the table identifies this as a medication-proportion sample size and supplies no rule requiring equality; no error is inferred.
- eTable 12 E-values were not treated as arithmetic candidates because the provided materials do not state the calculation formula or any required transformation from the displayed hazard ratios; raw-data or external-method assumptions were not made.
