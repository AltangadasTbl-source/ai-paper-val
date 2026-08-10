# Human Adjudication Report

## Package Manifest

| Document ID | Filename | PDF pages | Classification | Audit disposition |
|---|---|---:|---|---|
| DOC-001 | `jama_flint_2019_oi_190079.pdf` | 10 | Main article | Scientific audit target |
| DOC-002 | `joi180151supp1_prod.pdf` | 7 | Protocol | Not Audited by Design: unrelated DOI/main-article linkage |
| DOC-003 | `joi180151supp2_prod.pdf` | 29 | Results supplement | Not Audited by Design: unrelated DOI/main-article linkage |

DOC-001 is the 2019 STOP-PD II psychotic-depression trial (DOI `10.1001/jama.2019.10517`). DOC-002 and DOC-003 identify a different aspirin primary-prevention meta-analysis (DOI `10.1001/jama.2018.20578`), so they were retained but not used as supporting evidence for DOC-001.

## AI Training Restriction Summary

This compliance screen is separate from the scientific findings and is not a legal opinion.

| Document ID | Status | Exact evidence location and quotation | Human Compliance Review |
|---|---|---|---|
| DOC-001 | No AI Training Restriction Located in Provided Materials | PDF pp. 1-10, footer: “© 2019 American Medical Association. All rights reserved.” | No |
| DOC-002 | Not Stated / Undetermined | PDF p. 1: “This supplementary material has been provided by the authors to give readers additional information about their work.” No rights, license, terms, AI-use, or text-and-data-mining statement was located. | No |
| DOC-003 | No AI Training Restriction Located in Provided Materials | PDF pp. 1-29, footer: “© 2019 American Medical Association. All rights reserved.” | No |

## Scientific Findings

### 1. HbA1c has inconsistent stated units in the results narrative and Table 4.

- **Category and severity:** Presentation inconsistency; Minor.
- **Exact evidence locations:** DOC-001, `jama_flint_2019_oi_190079.pdf`, PDF p. 7 (printed p. 628), Results, “Secondary Outcomes”; PDF p. 8 (printed p. 629), Table 4, HbA1c row.
- **Source evidence:** The narrative reports “HbA1c levels (−0.0002 mg/dL [95% CI, −0.0021 to 0.0016], adjusted P = .99).” Table 4 labels the corresponding outcome “HbA1c, %.”
- **Reported-versus-comparator comparison:** The stated narrative unit is `mg/dL`; the table's stated unit is `%`. No conversion is supplied.
- **Reproducible logical chain:** (1) Both cited locations identify HbA1c. (2) A repeated outcome requires a consistent unit or an explained conversion. (3) The stated units differ. Rounding tolerance is not applicable.
- **Bounded impact:** This affects interpretation of the HbA1c treatment-by-time estimate and CI only; it does not change their numerals, adjusted P value, or the reported nonsignificant result. The supplied materials do not establish the intended replacement unit.
- **Human verification steps:**
  1. Compare the quoted Results sentence on PDF p. 7 with the Table 4 row label on PDF p. 8.
  2. Check the underlying analysis output for the intended daily-rate unit. The finding is resolved if the report uses a consistent, confirmed unit or explicitly explains the conversion.

### 2. Table 5's repeated 4.3-percentage-point difference does not match its displayed counts and precision.

- **Category and severity:** Arithmetic inconsistency; Minor.
- **Exact evidence locations:** DOC-001, `jama_flint_2019_oi_190079.pdf`, PDF p. 9 (printed p. 630), Table 5, Cholesterol “Total” and “LDL” rows; columns for olanzapine (n = 64), placebo (n = 62), and absolute unadjusted difference.
- **Source evidence:** Each row reports `9 (14.1)` versus `6 (9.7)` and `4.3 (−8 to 17.2)`.
- **Reported-versus-comparator comparison:** Reported difference: `4.3` percentage points. Comparator: `14.1% − 9.7% = 4.4` percentage points; the exact-count calculation also rounds to `4.4`. The reported point estimate is `0.1` percentage point lower. These are one repeated issue, not two independent findings.
- **Reproducible calculation:** `100 × (9/64 − 6/62) = 100 × (0.140625 − 0.09677419) = 4.3850806` percentage points, which rounds to `4.4` at one decimal. Standard one-decimal rounding tolerance: values from `4.35` to `<4.45` round to `4.4`; `4.3` does not.
- **Bounded impact:** Only the displayed absolute unadjusted difference for the two repeated rows requires correction or confirmation. This finding does not assess the reported CI or the table's statistical interpretation.
- **Human verification steps:**
  1. Recalculate both rows from `9/64` and `6/62` and inspect the table-production values.
  2. Confirm the intended calculation and rounding rule. The finding is resolved if `4.3` is documented by that rule or the displayed value is corrected accordingly.

## Rejected and Uncertain Candidates

None after verification. DOC-002 and DOC-003 were scope exclusions due to their unrelated article linkage, not scientific candidates.

## Human Adjudication Checklist

1. Confirm and harmonize the intended HbA1c unit in the Results narrative and Table 4.
2. Confirm the Table 5 calculation/rounding rule for the repeated `4.3` values.
3. Record the outcome for each finding and any correction.
