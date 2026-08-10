# Human Adjudication Report — LEVOECMO / JAMA 2025.19843

**Package status:** Human Adjudication (next action)  
**Scientific issues retained:** 1  
**Scope:** One critic-retained, evidence-verified finding only. This report does not determine which source item requires correction.

## Scientific evidence cards

### 1. Day-30 MACE definition and placebo count cannot be reconciled

**Issue statement:** The main article defines dialysis as a day-30 MACE component, but the results supplement reports fewer placebo MACE cases than dialysis cases and separately displays the same MACE count under a definition omitting dialysis; this prevents the secondary composite’s definition and reported count from being jointly verified.

**Category:** Cross-document inconsistency  
**Secondary descriptor:** Statistical reporting inconsistency  
**Severity:** Major

**Evidence A — stated composite definition**

- **Location:** DOC-001, `jama_combes_2025_oi_250087_1766516490.94011.pdf`, PDF p. 3 (journal p. 62), Methods—Outcomes.
- **Source excerpt:** “major adverse cardiovascular events (death, heart transplant, escalation to need for left ventricular assist device, stroke, dialysis, or heart failure rehospitalization) at days 30 and 60”.

**Evidence B — placebo day-30 table values**

- **Location:** DOC-004, `joi250087supp3_prod_1766516490.97011.pdf`, PDF p. 5, eTable 3—Secondary End Points, placebo column, rows “D30 MACE” and “Dialysis by D30”.
- **Reported values:** D30 MACE: **36/104 (34.6%)**; dialysis by D30: **38/104 (36.5%)**.

**Evidence C — figure definition and count**

- **Location:** DOC-004, `joi250087supp3_prod_1766516490.97011.pdf`, PDF p. 13, eFigure 4—D30 and D60 Cumulative Incidence of MACE, definition and D30 placebo curve/count.
- **Source excerpt/value:** MACE is defined as “death, cardiac transplant, permanent LVAD escalation, stroke, or heart-failure rehospitalization”; **D30 placebo cumulative events: 36**. Dialysis is not listed in this figure definition.

**Direct comparison**

- **Reported composite under DOC-001 definition:** placebo D30 MACE = **36 participants (34.6%)**.
- **Comparator required by that definition:** dialysis by D30 = **38 participants (36.5%)**; because dialysis is named as a MACE component, every dialysis case must be included in MACE.
- **Discrepancy:** MACE is **2 participants lower** than the stated component (**36 − 38 = −2**), or **1.9 percentage points lower** (**34.6% − 36.5% = −1.9 percentage points**). eFigure 4 repeats 36 placebo events but uses a MACE definition that omits dialysis.

**Reproducible calculation / rule**

- **Inputs:** DOC-001 includes dialysis in MACE; DOC-004 eTable 3 reports placebo D30 MACE = 36 and dialysis by D30 = 38, both with denominator 104.
- **Rule:** If a component is included in a composite, \(n(\mathrm{composite}) \ge n(\mathrm{component})\).
- **Calculation:** \(n(\mathrm{MACE}) - n(\mathrm{dialysis}) = 36 - 38 = -2\) participants; \(34.6\% - 36.5\% = -1.9\) percentage points.
- **Rounding tolerance:** None for the count comparison: 36 and 38 are reported integer numerators, so percentage rounding cannot reconcile the failed nesting rule.

**Bounded impact:** The day-30 MACE definition, placebo count, associated effect estimates, and eFigure 4 display cannot be jointly verified. The evidence does not establish whether dialysis was incorrectly included in DOC-001’s written definition or excluded from the supplement’s composite derivation; no primary-outcome error or overall-trial-conclusion effect is established.

**Verification instruction**

1. Check DOC-001 PDF p. 3, Methods—Outcomes, and confirm that dialysis is listed in the day-30/60 MACE definition.
2. Check DOC-004 PDF p. 5, eTable 3 placebo column, and confirm D30 MACE = 36/104 (34.6%) and dialysis by D30 = 38/104 (36.5%).
3. Apply the component-nesting rule: if dialysis belongs to the composite, confirmation requires MACE to be at least 38; a confirmed numerator of 36 does not satisfy the DOC-001 definition.
4. Check DOC-004 PDF p. 13, eFigure 4, and confirm its definition omits dialysis while its D30 placebo event count is 36.
5. Check the authors’ intended composite specification and prespecified derivation. Confirmation that dialysis is excluded resolves the count nesting only by confirming a written-definition discrepancy; confirmation that dialysis is included requires corrected MACE reporting or a reconciled derivation.

## AI Training Restriction Summary

This is a document-rights screen, separate from the scientific issue list and not a legal opinion. For records flagged for review, the user-provided-permissions assumption was applied as directed.

| Document ID | Filename | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|---|
| DOC-001 | `jama_combes_2025_oi_250087_1766516490.94011.pdf` | Explicit AI Training Restriction | PDF p. 1 footer (repeated pp. 2–10): “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Required; **user-provided permissions assumed**. |
| DOC-002 | `joi250087supp1_prod_1766516490.96011.pdf` | Conditional / Permission Required | PDF p. 3 footer (repeated): “This document is the property of DRCI / AP-HP. All reproduction is strictly prohibited.” Section 11.5, PDF pp. 35, 81, 127: “AP-HP is the owner of the data. The data cannot be used or disclosed to a third party without its prior permission.” | Required; **user-provided permissions assumed**. |
| DOC-003 | `joi250087supp2_prod_1766516490.96511.pdf` | No AI Training Restriction Located in Provided Materials | Screened PDF pp. 1 and 9; document/XMP metadata; raw-PDF keyword screen; embedded-file inventory (0); URL inventory (none). No responsive rights/AI-use language located. | Not required on the basis of supplied document. |
| DOC-004 | `joi250087supp3_prod_1766516490.97011.pdf` | Explicit AI Training Restriction | PDF p. 1 footer (repeated pp. 2–18): “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Required; **user-provided permissions assumed**. |
| DOC-005 | `joi250087supp4_prod_1766516490.97511.pdf` | No AI Training Restriction Located in Provided Materials | Screened PDF pp. 1–3; document/XMP metadata; embedded-file inventory (0); URL inventory (none). No responsive rights/AI-use language located. | Not required on the basis of supplied document. |
| DOC-006 | `joi250087supp5_prod_1766516490.97511.pdf` | No AI Training Restriction Located in Provided Materials | PDF p. 1 and embedded metadata. No responsive rights or AI-use language located; visible page is a Data Sharing Statement. | Not required on the basis of supplied document. |

