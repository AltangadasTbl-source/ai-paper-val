# Package Manifest

| Document ID | Source file | Classification | Pages | Scientific-audit status |
|---|---|---|---:|---|
| DOC-001 | `jama_kumar_2025_oi_250034_1750956984.08518.pdf` | Main article | 11 | Audited, PDF pp. 1-11 |
| DOC-002 | `joi250034supp1_prod_1750956984.09018.pdf` | Protocol | 26 | **Not Audited by Design** |
| DOC-003 | `joi250034supp2_prod_1750956984.11521.pdf` | Statistical analysis plan | 29 | **Not Audited by Design** |
| DOC-004 | `joi250034supp3_prod_1750956984.12018.pdf` | Results supplement | 6 | Audited, PDF pp. 1-6 |

Scientific audit was restricted to the main article and results supplement. DOC-002 and DOC-003 were screened for AI-training restrictions but not scientifically audited.

# AI Training Restriction Summary

This is a document-use compliance screen, separate from the scientific findings and not a legal opinion. Institutional permission was provided and processing continued.

| Document ID | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|
| DOC-001 | **Explicit AI Training Restriction** | PDF p. 1 footer, repeated pp. 2-11: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | **Required** |
| DOC-002 | **No AI Training Restriction Located in Provided Materials** | Metadata; PDF p. 1; pp. 22-23 administrative/end matter; pp. 24-26 reference end matter; full native-text rights-keyword screen. The reviewed confidentiality and publication-approval statements do not state AI-training terms. | No |
| DOC-003 | **No AI Training Restriction Located in Provided Materials** | Metadata; PDF p. 1; p. 29; full native-text and PDF-byte screen for rights, licensing, AI-training, fine-tuning, and model-improvement terms. No relevant statement located. | No |
| DOC-004 | **Explicit AI Training Restriction** | PDF p. 1 footer, repeated pp. 2-6: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | **Required** |

For DOC-001 and DOC-004, the Human Compliance Review flag applies because the supplied PDFs expressly reference AI training; institutional permission was provided and processing continued. For DOC-002 and DOC-003, absence of located restriction language is not treated as permission.

# Scientific Findings

## 1. Primary composite outcome analysis-unit labels conflict

- **Category:** Presentation inconsistency
- **Severity:** Major
- **Exact location:** DOC-001, `jama_kumar_2025_oi_250034_1750956984.08518.pdf`: PDF p. 1, Abstract Results; p. 4, Results and Figure 1 terminal boxes; p. 6, “Primary and Secondary Outcomes”; p. 7, Table 3 and site-specific reporting; p. 8, Figure 2. DOC-004, `joi250034supp3_prod_1750956984.12018.pdf`: PDF p. 3, eTable 2 primary-outcome rows.
- **Compared values/statements:** DOC-001 p. 1 and p. 6 report 83/1625 and 84/1625 as **women**. DOC-001 p. 4 states that the primary end point was available for **3250 infants** and Figure 1 labels **1625 infants with primary outcome** in each group. DOC-001 p. 8 Figure 2 uses the same 83/1625 and 84/1625 totals under “total No. of patients.” DOC-004 p. 3 eTable 2 partitions the same values: 16+67=83 and 24+60=84; 883+742=1625 and 887+738=1625.
- **Calculation/logical basis:** Identical primary-outcome records and denominators are labeled infants, women, and patients. The article separately enumerates randomized women and infants.
- **Verification instruction:** Confirm the intended primary-outcome analysis unit in the cited source pages; harmonize the Abstract, Results, Table 3/site-specific reporting, and Figure 2 labels.

## 2. Placebo ethnicity percentages use different denominator conventions

- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Exact location:** DOC-001, `jama_kumar_2025_oi_250034_1750956984.08518.pdf`, PDF p. 4, Results “Participants and Adherence” ethnicity paragraph; PDF p. 5, Table 1 ethnicity rows.
- **Compared values/statements:** Table 1 uses placebo ethnicity n=1629 and reports Australia/New Zealand as 874 (53.7%) and Pacific Islander as 53 (3.3%). The adjacent prose uses the full placebo cohort n=1631, including 2 missing observations, and reports the same counts as 874 (53.6%) and 53 (3.2%).
- **Calculation/logical basis:** 874/1629=53.65%, displayed as 53.7%; 53/1629=3.25%, displayed as 3.3%. Using all randomized placebo participants, 874/1631=53.59%, displayed as 53.6%; 53/1631=3.25%, displayed as 3.2% at the shown precision. The counts agree, but the denominator convention is not explained consistently.
- **Verification instruction:** Confirm whether ethnicity percentages should use nonmissing observations (n=1629) or all randomized placebo participants (n=1631, including missing observations), then apply or explicitly state that convention consistently.

# Rejected and Uncertain Candidates

- **Rejected — statistical reporting inconsistency not supported:** DOC-004, `joi250034supp3_prod_1750956984.12018.pdf`, PDF p. 5, eTable 2, other-site spontaneous vaginal birth: 370/746 (49.6%) vs 410/750 (54.7%), RR 0.91 (95% CI, 0.82-1.00), P=.050. The article’s stated significance rule is two-tailed P<.05 (DOC-001 PDF p. 4). At printed precision, .050 is not less than .05 and the confidence interval includes 1.00; no contradictory significance claim is reported, and unrounded values are unavailable. **Verification instruction:** Confirm the printed eTable row and stated significance rule; no correction is supported from the supplied documents.
- **Uncertain final candidates:** None.

# Human Adjudication Checklist

- Confirm the intended analysis unit for the primary composite outcome and approve harmonized terminology across the cited main-article and supplement locations.
- Confirm the intended placebo ethnicity denominator convention and approve consistent table/text presentation.
- Confirm that the rejected rounded eTable 2 item requires no correction on the supplied evidence.
- Record adjudication for both retained findings: uphold, revise, or reject.
- Complete Human Compliance Review documentation for DOC-001 and DOC-004; retain the separate restriction-screen records for all four documents.
