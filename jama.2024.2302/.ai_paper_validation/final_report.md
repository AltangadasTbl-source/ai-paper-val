# Human Adjudication Report — jama.2024.2302

**Report status:** Submitted for Human Adjudication  
**Scientific findings:** 3 accepted; 2 rejected; 1 uncertain.  
**Source handling:** Four supplied PDFs; source PDFs unchanged. No external sources used.

## Package Manifest

| Document ID | Source PDF | Classification | Scientific processing / scope |
|---|---|---|---|
| jama-2024-2302-main-article | `jama_blakely_2024_oi_240020_1710443209.74411.pdf` (10 pp) | Main article | Audit target, pp. 1-10; preprocessing complete. |
| jama-2024-2302-supp1-protocol | `joi240020supp1_prod_1710443209.74911.pdf` (25 pp) | Protocol | **Not Audited by Design** for scientific review; retained for rights screening and any parent-requested specific comparison. |
| jama-2024-2302-supp2-sap | `joi240020supp2_prod_1710443209.75411.pdf` (10 pp) | Statistical analysis plan | **Not Audited by Design** for scientific review; retained for rights screening and any parent-requested specific comparison. |
| jama-2024-2302-supp3-results | `joi240020supp3_prod_1710443209.75411.pdf` (8 pp) | Results supplement | Audit target, pp. 2-5 only. P. 1 and pp. 6-8 are **Not Audited by Design**. |

**Processing limitations:** Native text extraction was used first; selective source-page renders supported figures/tables; no OCR was used. Supplement pp. 2-5 had corrupted native glyph mappings (and p. 4 sparse text); visual page renders were used for verification. Protocol and SAP were not opened for scientific review.

## AI Training Restriction Summary

This is a supplied-materials compliance screen, separate from the scientific findings. It is not a legal opinion. Generic copyright notices are distinguished from AI-specific restrictions; silence is not permission.

| Document ID | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|
| jama-2024-2302-main-article | No AI Training Restriction Located in Provided Materials | `jama_blakely_2024_oi_240020_1710443209.74411.pdf`, PDF pp. 1-10 footers: “© 2024 American Medical Association. All rights reserved.” Embedded PDF/XMP metadata screened. Notice is generic copyright language, not AI-training language. | No |
| jama-2024-2302-supp1-protocol | No AI Training Restriction Located in Provided Materials | `joi240020supp1_prod_1710443209.74911.pdf`, PDF pp. 1 and 25; native-text rights/AI-term screen across pp. 1-25; embedded document metadata. No applicable rights or AI-use language located. | No |
| jama-2024-2302-supp2-sap | No AI Training Restriction Located in Provided Materials | `joi240020supp2_prod_1710443209.75411.pdf`, PDF pp. 1 and 10; native-text rights/AI-term screen across pp. 1-10; embedded document-information metadata. No applicable rights or AI-use language located. | No |
| jama-2024-2302-supp3-results | No AI Training Restriction Located in Provided Materials | `joi240020supp3_prod_1710443209.75411.pdf`, PDF p. 1 and footers on pp. 1-8: “© 2024 American Medical Association. All rights reserved.” Embedded metadata screened. Notice is generic copyright language, not AI-training language. | No |

No supplied-file language expressly restricted or conditioned AI training, fine-tuning, or model improvement. No permission is inferred from that absence.

## Scientific Findings

### C1 — Abstract misstates the number of infants who underwent operative repair

- **Category / severity:** Presentation inconsistency — Major.
- **Exact location:** `jama_blakely_2024_oi_240020_1710443209.74411.pdf`, PDF p. 1 (journal p. 1035), Abstract—Results; compared with PDF p. 3 (Figure 1), p. 4 (Surgery Characteristics), p. 5 (Surgery Characteristics and Table 1).
- **Compared values/statements:** Abstract: “320 underwent operative repair.” Surgery Characteristics: 152/163 early and 129/157 late underwent repair. Figure 1: `(147 + 5)` early and `(90 + 39)` late repairs. Table 1 postwithdrawal denominators: 163 early and 157 late.
- **Calculation / logical basis:** `152 + 129 = 281`; Figure 1 independently gives `(147 + 5) + (90 + 39) = 281`. The abstract’s 320 equals the postwithdrawal cohort: `163 + 157 = 320` and `338 - 9 - 9 = 320`, not the reported repair total.
- **Verification instruction:** Read the PDF p. 1 abstract sentence; sum repair counts on pp. 4-5 or Figure 1 branches on p. 3; compare with the Table 1 postwithdrawal total.

### C3 — Figure 1 omits explicit withdrawal/exclusion branches needed to reconcile primary-analysis populations

- **Category / severity:** Participant flow inconsistency — Minor.
- **Exact location:** `jama_blakely_2024_oi_240020_1710443209.74411.pdf`, PDF p. 3 (journal p. 1037), Figure 1; compared with PDF p. 4, Results—Patient Characteristics, and PDF p. 6, Table 2 note a.
- **Compared values/statements:** Figure 1: early `172 randomized`, `163 received treatment as randomized`, `9 did not undergo treatment as randomized`, `4 lost to follow-up`, `159 included`; late `166`, `157`, `9`, `8`, `149`, respectively. Results: 9 infants withdrawn from each group after randomization. Table 2 note a: excludes 9 withdrawn per group plus 4 early/8 late lost to follow-up.
- **Calculation / logical basis:** `172 - 9 - 4 = 159`; `166 - 9 - 8 = 149`. Figure 1 contains matching 9-count categories but labels them only as not undergoing treatment as randomized and provides no explicit withdrawal/exclusion branch before the analysis boxes.
- **Verification instruction:** Trace each Figure 1 arm on p. 3 to the primary-analysis box; reconcile with the withdrawal statement on p. 4 and Table 2 note a on p. 6.

### C5 — Enrollment-details cross-reference incorrectly includes outcome-analysis eTable 2

- **Category / severity:** Presentation inconsistency — Minor.
- **Exact location:** Main article, `jama_blakely_2024_oi_240020_1710443209.74411.pdf`, PDF p. 4 (journal p. 1038), Results—Patient Characteristics; compared with `joi240020supp3_prod_1710443209.75411.pdf`, PDF pp. 2-4 (eTable 1) and p. 5 (eTable 2), and main-article PDF p. 3, Figure 1 note b.
- **Compared values/statements:** Main Results: “additional enrollment details appear in eTables 1-2.” eTable 1: “Additional information related to trial enrollment.” eTable 2: “Frequentist primary and major secondary outcome analyses.” Figure 1 note b directs additional enrollment information to eTable 1 alone.
- **Calculation / logical basis:** eTable 1 contains enrollment details; eTable 2 contains outcome analyses. The Results citation therefore includes a table that does not supply the stated enrollment material.
- **Verification instruction:** Follow the p. 4 citation and compare eTable 1 (supplement pp. 2-4) with eTable 2 (p. 5); confirm the Figure 1 note b reference on main-article p. 3.

## Rejected and Uncertain Candidates

| Candidate | Disposition | Reason |
|---|---|---|
| C2 | Rejected | Methods explicitly anticipates clinically driven timing variation within the randomized timing strategies; repairs outside planned timing do not establish an internal contradiction. |
| C4 | Uncertain | The interval difference is documented, but the supplied reporting pages do not establish that Table 2 and Figure 3 used the same model/posterior standardization. Underlying model output is needed to distinguish model dependence from rounding or transcription. |
| C6 | Rejected | eTable 2 gives a general mixed-effects-model statement followed by an explicit GEE exception for the frequentist primary analysis; together, the statements are not contradictory. |

## Human Adjudication Checklist

- [ ] C1: Confirm the abstract’s “320 underwent operative repair” against the 281 repair total and 320 postwithdrawal cohort.
- [ ] C3: Confirm whether Figure 1 should display explicit withdrawal/exclusion branches for the 9 infants per arm.
- [ ] C5: Confirm whether the Results cross-reference should identify eTable 1 only for enrollment details.
- [ ] Compliance: Confirm review of the four AI Training Restriction records; no supplied-materials AI-specific restriction or conditional permission term was located, and silence was not treated as permission.
- [ ] Scope: Confirm protocol and SAP were Not Audited by Design; results supplement p. 1 and pp. 6-8 were Not Audited by Design; no OCR, external sources, or source-PDF changes occurred.
