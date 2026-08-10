# Human Adjudication Report

Package `jama.2025.4390`. Final scientific findings: 7 (1 Major; 6 Minor). This report presents accepted document-grounded findings only.

## Package Manifest

| Document ID | Source PDF | Classification | Scientific-audit scope/status |
|---|---|---|---|
| JAMA2025-4390-MAIN | `jama_garrison_2025_oi_250019_1749674951.29054.pdf` | Main article (12 pp.) | Audited, pp. 1-12 |
| JAMA2025-4390-SUPP1-PROTOCOL | `joi250019supp1_prod_1749674951.29554.pdf` | Protocol (18 pp.) | Not Audited by Design |
| JAMA2025-4390-SUPP2-SAP | `joi250019supp2_prod_1749674951.30054.pdf` | Statistical analysis plan (7 pp.) | Not Audited by Design |
| JAMA2025-4390-SUPP3-RESULTS | `joi250019supp3_prod_1749674951.30054.pdf` | Results supplement (49 pp.) | Audited: pp. 11-12, 19, 22-49; pp. 20-21 targeted context only |

## AI Training Restriction Summary

This separate compliance screen is not part of the scientific issue list and is not legal advice. Where flagged, the prompt states that permissions were already given and processing continued.

| Document ID | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|
| JAMA2025-4390-MAIN | Explicit AI Training Restriction | PDF p. 1 footer (also pp. 2-12): “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Required / flagged; permissions assumed given and processing continued |
| JAMA2025-4390-SUPP1-PROTOCOL | No AI Training Restriction Located in Provided Materials | No training-related language located in supplied PDF or metadata; adjacent non-training data-sharing statement at PDF p. 18. | No |
| JAMA2025-4390-SUPP2-SAP | No AI Training Restriction Located in Provided Materials | No training-related language located in supplied PDF or metadata; pp. 1-7 screened. | No |
| JAMA2025-4390-SUPP3-RESULTS | Explicit AI Training Restriction | PDF p. 1 footer (also pp. 2-49): “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Required / flagged; permissions assumed given and processing continued |

## Scientific Findings

### 1. SCI-01 — Figure 3 rate columns contain person-time values

- **Category / severity:** Presentation inconsistency / Major.
- **Location:** Main article, PDF p. 9 (printed p. 2069), Figure 3, both columns headed `Rate per 100 patient-years`; compare Table 2, PDF p. 8 (printed p. 2068), primary-outcome row.
- **Compared values:** Figure 3 gives bedtime `163` events and `71.0`, and morning `173` events and `71.0`; Table 2 gives rates `2.30` and `2.44` per 100 patient-years, respectively. Bedtime sex subgroup values `30.5 + 40.5 = 71.0`.
- **Basis:** `163 / 2.30 × 100 = 7087.0` and `173 / 2.44 × 100 = 7090.2` patient-years, approximately 70.9 hundreds of patient-years. Thus `71.0` behaves as person-time in hundreds of patient-years, not as a rate.
- **Verification:** Compare Figure 3 with Table 2 and inspect figure-generation data; correct the heading or displayed values.

### 2. TAC-01 — Duplicated ethnicity row in eTable 5

- **Category / severity:** Presentation inconsistency / Minor.
- **Location:** Results supplement, PDF p. 37, eTable 5, `Ethnicity - no. (%)`, `White/Caucasian` and `Other`; compare eTable 3, PDF p. 29.
- **Compared values:** Morning (n=44): `White/Caucasian 40 (90.9)` and `Other 40 (90.9)`; bedtime (n=57): `White/Caucasian 53 (93.0)` and `Other 53 (93.0)`. No eTable 5 footnote authorizes overlapping categories.
- **Basis:** Eight displayed ethnicity counts total `85/44 = 193.2%` (morning) and `111/57 = 194.7%` (bedtime); `Other` exactly duplicates `White/Caucasian`.
- **Verification:** Compare the two rows and inspect the source export for the intended `Other` values or row placement.

### 3. SCI-02 — Figure 3 footnote misstates the all-patients CI as unadjusted

- **Category / severity:** Statistical reporting inconsistency / Minor.
- **Location:** Main article, PDF p. 9 (printed p. 2069), Figure 3 all-patients row and footnote; compare Results text, PDF p. 6 (printed p. 2066), and Table 2, PDF p. 8 (printed p. 2068).
- **Compared statements:** Figure 3 reports `HR 0.96 (95% CI, 0.77-1.19)` and says, `All confidence intervals are unadjusted.` Results text identifies `0.96 (95% CI, 0.77-1.19)` as adjusted and `0.94 (95% CI, 0.76-1.17)` as unadjusted; Table 2 repeats the adjusted value.
- **Basis:** The displayed all-patients estimate exactly matches the adjusted, not unadjusted, analysis; the universal footnote is false for that row.
- **Verification:** Compare the Figure 3 row/footnote with pp. 6 and 8; limit the footnote to subgroup rows or amend the all-patients row.

### 4. SCI-03 — Identical displayed binary comparisons have different P values

- **Category / severity:** Statistical reporting inconsistency / Minor.
- **Location:** Results supplement, PDF p. 39, eTable 5, `Type of BP-lowering med - no. (%)`, `Diuretic` and `Combination BP med`; denominators on PDF p. 37.
- **Compared values:** Morning n=44 and bedtime n=57. `Diuretic`: `9 (20.5)` vs `16 (28.1)`, `P=.34`; `Combination BP med`: identical `9 (20.5)` vs `16 (28.1)`, `P=.38`.
- **Basis:** Both displayed comparisons are 9 yes/35 no versus 16 yes/41 no. The table states no different denominator, adjustment, or procedure; identical displayed comparisons cannot yield different P values under the same comparison.
- **Verification:** Re-run or inspect source output for both rows using n=44 and n=57; identify the incorrect count or P value.

### 5. FFC-01 — British Columbia city counts exceed the province header

- **Category / severity:** Arithmetic inconsistency / Minor.
- **Location:** Results supplement, PDF p. 22, eFigure 1, `Location of Participating Practices`, British Columbia; compare eTable 1, PDF p. 27.
- **Compared values:** BC header `43`; city counts `12+1+1+1+1+1+1+1+4+12+1+3+3+2`. Province headers are BC 43, Alberta 326, Saskatchewan 22, Manitoba 29, Ontario 16; eTable 1 reports 436 PCPs.
- **Basis:** BC city counts total `44`, not 43. Province headers total `43+326+22+29+16=436`, matching eTable 1; the BC listing is internally off by one.
- **Verification:** Recount the BC entries and inspect figure source data to determine whether the header or a city count is incorrect.

### 6. FFC-02 — Bedtime diuretic adherence differs between eFigure 4 and eTable 6

- **Category / severity:** Presentation inconsistency / Minor.
- **Location:** Results supplement, PDF p. 26, eFigure 4 bedtime/PM `Diuretic` bar; compare eTable 6, PDF p. 42, bedtime `Diuretic` rows.
- **Compared values:** Figure: `278` as allocated, `138` off allocation, `8` twice or more daily. Table: n=424, `277/424` as allocated, `139/424` off allocation, `8/424` twice or more daily.
- **Basis:** Both displays total 424 (`278+138+8` and `277+139+8`) but allocate one medication differently between the first two categories.
- **Verification:** Compare both displays and inspect the 6-month medication-timing source export to determine the correct categorization.

### 7. FFC-03 — Calcium-channel-blocker percentage is arithmetically wrong in two tables

- **Category / severity:** Arithmetic inconsistency / Minor.
- **Location:** Main article, PDF p. 6 (printed p. 2066), Table 1 continued, `Calcium channel blocker`; repeated in results supplement, PDF p. 32, eTable 3.
- **Compared values:** Bedtime n=1677, `479 (28.2)` in both tables; morning `489/1680 (29.1)` and overall `968/3357 (28.8)`.
- **Basis:** `479/1677×100=28.5629%`, which rounds to `28.6%`, not `28.2%`, to one decimal. The comparison cells reconcile.
- **Verification:** Check the intended numerator and denominator in the source table; correct the repeated percentage or source count.

## Rejected and Uncertain Candidates

Rejected: 0. Uncertain: 0. All seven submitted candidates were verified and retained by the critic.

## Human Adjudication Checklist

- [ ] Confirm the seven findings against the cited source pages and underlying table/figure outputs.
- [ ] Resolve the Major Figure 3 column-label/value inconsistency before publication action.
- [ ] Record the correction, rationale, and disposition for each Minor finding.
- [ ] Complete the flagged Human Compliance Review records for the main article and results supplement; permissions are assumed given for this completed workflow.
- [ ] Retain protocol and SAP as Not Audited by Design unless a specific report comparison is requested.
