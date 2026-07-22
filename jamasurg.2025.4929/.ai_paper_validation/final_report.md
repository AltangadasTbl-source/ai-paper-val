# Package Manifest

| ID | Source file | Classification | Scientific-audit scope |
|---|---|---|---|
| DOC-001 | `jamasurgery_dat_2025_oi_250075_1767031598.03318.pdf` (10 pp.) | Main article | pp. 1-9. PDF p. 10 begins an invited commentary and is excluded from main-study evidence. |
| DOC-002 | `soi250075supp1_prod_1767031598.04818.pdf` (49 pp.) | Study protocol | **Not Audited by Design.** Excluded from routine extraction, rendering, and scientific checks; open only for a specific protocol-to-report comparison. |
| DOC-003 | `soi250075supp2_prod_1767031598.05318.pdf` (3 pp.) | Results supplement | pp. 1-3; priority p. 3, eTable 2. |

# AI Training Restriction Summary

This is a separate document-use screen, not a scientific finding or legal opinion.

| Document ID | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|
| DOC-001 | **Explicit AI Training Restriction** | PDF p. 10 footer: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” PDF p. 8 Article Information states CC-BY open-access status. | **Yes.** User authorization to continue this workflow was recorded in `human_compliance_review_record.md`; the explicit restriction status remains retained. |
| DOC-002 | **No AI Training Restriction Located in Provided Materials** | PDF p. 1: “This trial protocol has been provided by the authors to give readers additional information about the work.” Screened native text, targeted visual pages 1, 2, and 49, and embedded metadata; no AI-training term located. | No. |
| DOC-003 | **No AI Training Restriction Located in Provided Materials** | PDF pp. 1 and 3 footer: “© 2025 Dat TQ et al. *JAMA Surgery*.” PDF p. 1 describes the supplement’s informational purpose. Screened all pages and embedded metadata; no AI-training term located. | No. |

# Scientific Findings

## F-01 — Internally incompatible pN N3 regression row

- **Category:** Statistical reporting inconsistency
- **Severity:** Major
- **Location:** DOC-003, PDF p. 3, eTable 2, pN/N3 row; cross-check DOC-001, PDF p. 7, Table 4.
- **Compared values:** N0 `10/51 (19.6%)`; N1-2 `16/83 (19.3%)`; N3 `29/74 (25.7%), OR 0.431 (95% CI, 0.60-3.37), P=.431`; Table 4 total morbidity `23 + 22 = 45`.
- **Calculation/logical basis:** `29/74 = 39.2%`; pN events total `10 + 16 + 29 = 55`, not 45; OR 0.431 lies outside the printed CI and conflicts directionally with the displayed rates.
- **Verification instruction:** Check source regression output and table-production cells for the N3 numerator, percentage, OR, CI, and P value; do not infer replacements.

## F-02 — Age-row percentage and univariate OR do not reproduce

- **Category:** Statistical reporting inconsistency
- **Severity:** Minor
- **Location:** DOC-003, PDF p. 3, eTable 2, Age.
- **Compared values:** `<60: 13/88 (14.8%), reference`; `≥60: 32/120 (27.7%), OR 2.28 (1.12-4.64), P=.040`.
- **Calculation/logical basis:** `32/120 = 26.7%`; displayed cells yield OR `(32/88)/(13/75) = 2.10`, not 2.28.
- **Verification instruction:** Compare the cells with source univariate output and confirm identical coding and analysis set.

## F-03 — Five additional univariate ORs do not reproduce

- **Category:** Statistical reporting inconsistency
- **Severity:** Minor
- **Location:** DOC-003, PDF p. 3, eTable 2, Sex, Approach, BMI, Comorbidity, and ASA blocks.
- **Compared values:** Reported versus displayed-cell ORs: Sex `0.97 vs 0.903`; Approach `0.85 vs 0.945`; BMI `0.64 vs 0.593`; Comorbidity `3.10 vs 2.853`; ASA grade 3 `2.76 vs 2.512`.
- **Calculation/logical basis:** Recalculation from each displayed two-level categorical event/denominator cell set produces the listed displayed-cell ORs.
- **Verification instruction:** Compare each categorical cell set with source univariate output and document any intended coding or analysis-set difference.

## F-04 — Main text presents a univariate approach estimate as multivariable

- **Category:** Cross-document inconsistency
- **Severity:** Major
- **Location:** DOC-001, PDF p. 6, “Risk Factors Related to Postoperative Morbidity”; DOC-003, PDF p. 3, eTable 2, Approach.
- **Compared statements:** DOC-001 introduces multivariate analyses and characterizes approach as an independent-predictor result: OR `0.85 (95% CI, 0.44-1.63), P=.62`. DOC-003 places the identical estimate under Univariate and leaves multivariable cells blank.
- **Calculation/logical basis:** The same estimate is assigned to incompatible analysis labels across the supplied documents.
- **Verification instruction:** Check the final multivariable model and determine whether the main-text characterization or table placement is incorrect.

## F-05 — CONSORT refusal label conflicts with postrandomization placement

- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Location:** DOC-001, PDF p. 3, CONSORT Figure; related flow prose, PDF p. 4.
- **Compared statements:** The figure shows all 240 participants willing to consent and randomized, then labels exclusions of 3 LDG and 2 ODG participants “Refused trial enrollment.” The prose describes patients who “refused or withdrew.”
- **Calculation/logical basis:** Counts reconcile, but the refusal label is positioned after consent and randomization, creating an internally confusing sequence.
- **Verification instruction:** Confirm the intended postrandomization disposition and align the figure label with the prose.

# Rejected and Uncertain Candidates

| Candidate | Status | Basis |
|---|---|---|
| C-05 | Rejected | Trivial grouped 0.1- to 0.2-point rounding discrepancies. |
| C-06 | Rejected | Trivial isolated 0.1-point percentage discrepancy (`35/148`). |
| C-07 | Rejected | Unsupported: continuous rows explicitly identify mean (SD) or median (IQR). |
| C-09 | Rejected | Trivial spelling errors without scientific ambiguity. |
| Uncertain candidates | None | No uncertain candidate was retained after critique. |

# Human Adjudication Checklist

- [ ] Review F-01 against source regression output and eTable production cells.
- [ ] Confirm the analysis set and coding for F-02 and F-03.
- [ ] Resolve whether DOC-001 text or DOC-003 table placement is correct for F-04.
- [ ] Confirm the intended CONSORT disposition wording for F-05.
- [ ] Retain DOC-002 as **Not Audited by Design** unless a specific protocol-to-report comparison is requested.
- [ ] Verify that the recorded DOC-001 Human Compliance Review authorization satisfies the applicable institutional process; the restriction status remains separate from scientific findings.

**Workflow status:** Submitted for Human Adjudication.
