# Human Adjudication Report

## Package Manifest

| Document ID | Source PDF | Classification | Pages | Scientific-content status |
|---|---|---|---:|---|
| JAMA2024-24764-MAIN | `jama_atherton_2025_oi_240145_1741627844.85412.pdf` | Main article | 11 | Audited |
| JAMA2024-24764-SUPP1 | `joi240145supp1_prod_1741627844.87412.pdf` | Statistical analysis plan (SAP) | 46 | Not Audited by Design; used only for the authorized p. 28 comparison |
| JAMA2024-24764-SUPP3 | `joi240145supp3_prod_1741627844.89412.pdf` | Results-relevant supplement | 9 | Audited |
| JAMA2024-24764-SUPP4 | `joi240145supp4_prod_1741627844.90412.pdf` | Protocol | 48 | Not Audited by Design |

Source PDFs were preserved unchanged. The MAIN document carried an explicit restriction; per the project instruction, permission was assumed for continuation of this workflow, with Human Compliance Review flagged below.

## AI Training Restriction Summary

This separate screen reports only rights-related language located in the supplied documents; it is not part of the scientific issue list.

| Document ID | Status | Exact evidence location and evidence | Human Compliance Review |
|---|---|---|---|
| JAMA2024-24764-MAIN | Explicit AI Training Restriction | PDF p. 1 footer; repeated on pp. 2-11: Copyright 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies. | Required |
| JAMA2024-24764-SUPP1 | No AI Training Restriction Located in Provided Materials | PDF pp. 1-2 and native-text/metadata screen of pp. 1-46: no relevant rights or AI-use statement located. | No |
| JAMA2024-24764-SUPP3 | No AI Training Restriction Located in Provided Materials | PDF p. 2 and headers on pp. 3-9: Copyright 2024 American Medical Association. All rights reserved. The notice does not expressly address AI training; metadata screen located no relevant AI-use term. | No |
| JAMA2024-24764-SUPP4 | No AI Training Restriction Located in Provided Materials | PDF pp. 1, 2, 43, and 48 and native-text/metadata screen of pp. 1-48: no relevant rights or AI-use statement located. | No |

## Scientific Findings

All retained findings are Minor. They are limited to reporting or presentation and do not establish an error in the primary treatment-effect result.

### 1. Participant-count framing does not disclose multiple responses

- **Category / severity:** Presentation inconsistency / Minor (V1 / TAC-01).
- **Exact location:** `jama_atherton_2025_oi_240145_1741627844.85412.pdf`, PDF p. 7 (printed p. 859), Table 2: Level of operating surgeon, Level of surgeon closing fascia, and Level of surgeon closing skin.
- **Compared values/statements:** Header: No. of participants (%); iNPWT `n=411`, surgeon's preference `n=410`. Operating-surgeon counts: `319, 123, 4` and `318, 110, 1`; fascia: `201, 218, 26` and `193, 225, 15`; skin: `115, 214, 96` and `102, 241, 73`. Footnote f defines seniority equivalents but does not state that categories are non-mutually exclusive.
- **Calculation/logical basis:** Totals are `446` vs `411` and `429` vs `410` (operating); `445` vs `411` and `433` vs `410` (fascia); `425` vs `411` and `416` vs `410` (skin). Each block exceeds its stated participant denominator and its percentages exceed 100%; the table does not disclose a multiple-response rule.
- **Verification instruction:** Confirm whether more than one surgeon or level could be recorded per operation. If so, add a multiple-response/non-mutually-exclusive note; otherwise recheck counts.

### 2. Pandemic-subgroup population is incompletely stated in Methods

- **Category / severity:** Statistical reporting inconsistency / Minor (V3 / FFC-2).
- **Exact location:** MAIN PDF p. 4 (printed p. 856), Statistical Analysis; MAIN PDF p. 9 (printed p. 861), Figure 2 pandemic rows and footnote a; SAP `joi240145supp1_prod_1741627844.87412.pdf`, PDF p. 28, section 9.9.
- **Compared statements/values:** Methods describes randomization before or after March 11, 2020 without a country restriction. Figure 2 footnote a states UK-based patients only; its pandemic-row events are `60 + 19 = 79` and `55 + 18 = 73`, matching the Figure 2 UK-row events `79` and `73`. SAP section 9.9 specifies the pandemic subgroup For UK patients only.
- **Calculation/logical basis:** The figure and SAP identify a UK-only analysis, whereas the Methods population description omits that restriction.
- **Verification instruction:** Reconcile the Methods wording with the SAP and Figure 2; explicitly state the UK-only restriction.

### 3. Figure 2 lacks category denominators and missing-classification disclosure

- **Category / severity:** Presentation inconsistency / Minor (V4 / FFC-3).
- **Exact location:** MAIN PDF p. 9 (printed p. 861), Figure 2.
- **Compared values/statements:** Figure 2 provides overall `n=394` per group and primary events `112` and `108`, but no category denominators, missing/unknown categories, or complete-case note. BMI events total `109` and `103`; incision-length events `111` and `103`; assessment-method events `101` and `107`.
- **Calculation/logical basis:** Shortfalls from primary events are BMI `3/5`, incision length `1/5`, and assessment method `11/1` (iNPWT/control). Missing subgroup data may explain the shortfalls, but the figure does not quantify or disclose it.
- **Verification instruction:** Total each category's event numerators against `112/108`; provide category denominators and missing/unknown counts, or add a complete-case subgroup-analysis note.

### 4. Unqualified quality-of-life narrative conflicts with the displayed day-7 contrast

- **Category / severity:** Statistical reporting inconsistency / Minor (V5 / SCC-01).
- **Exact location:** MAIN PDF p. 1 (printed p. 853), Abstract Results; MAIN PDF p. 6 (printed p. 858), Secondary Outcomes; results supplement `joi240145supp3_prod_1741627844.89412.pdf`, PDF p. 4, eTable 3, EQ5D-5L EuroQol score, Day 7.
- **Compared statements/values:** The Abstract says quality of life showed no significant difference; Results says there were no differences in quality of life between the 2 groups. eTable 3 Day 7 reports `N=292/283`, means `0.44 (SD 0.32)` vs `0.49 (SD 0.30)`, adjusted mean difference `-0.057 (95% CI, -0.104 to -0.010)`, `P=.02`; treatment-by-time interaction `P=.10`.
- **Calculation/logical basis:** The day-7 CI excludes 0 and the displayed time-specific P value is below .05, which conflicts with the unqualified narrative. The nonsignificant interaction may be the intended global basis, but the narrative does not state that qualification.
- **Verification instruction:** Confirm whether the conclusion relies on the global interaction or time-specific contrasts, then qualify the Abstract and Results accordingly.

## Rejected and Uncertain Candidates

| ID | Disposition | Location and basis | Verification instruction |
|---|---|---|---|
| V2 | Rejected | MAIN pp. 2-4 and 9; SAP p. 28 section 9.9. Figure 2's `<15 cm`/`>=15 cm` incision subgroup matches the SAP-prespecified Size of wound; recruiting center is absent from the SAP planned list. | Compare Methods/Figure 2 with SAP section 9.9; no scientific issue retained. |
| U1 | Uncertain | MAIN p. 8, Table 3. Readmission is `11/399` vs `11/398` (crude RD about `-0.000069`), while adjusted RD is `0.010` (95% CI, `-0.014` to `0.034`) and adjusted RR `1.02` (95% CI, `0.45` to `2.31`), `P=.96`. Separate adjusted models are reported; model outputs are not supplied. | Inspect original model output or typesetting source for adjusted RD `0.010`. |
| U2 | Uncertain | MAIN p. 3, Figure 1 footnote b, reports `25` deaths (`10/15`); MAIN pp. 6 and 8 report 30-day mortality `10/411` and `14/410` (`24`). The Figure 1 death time window is not stated. | Confirm the time window for all 15 control deaths; reconcile only if all occurred within 30 days. |

## Human Adjudication Checklist

- Confirm the four retained findings, their exact locations, and Minor severity.
- Resolve Table 2's surgeon-category recording rule and Figure 2's subgroup denominators/missing classifications.
- Reconcile the pandemic subgroup wording and qualify the quality-of-life narrative as appropriate.
- Keep V2 rejected and U1-U2 uncertain unless the specified source material resolves them.
- Complete Human Compliance Review for JAMA2024-24764-MAIN; retain the four-document rights screen separately from scientific findings.
