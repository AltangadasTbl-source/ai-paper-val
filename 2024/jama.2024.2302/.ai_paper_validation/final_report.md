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
- **Issue in one sentence:** Figure 1 contains a 9-infant category in each randomized arm, but labels it only as “Did not undergo treatment as randomized” and does not explicitly identify those infants as postrandomization withdrawals who were excluded from the primary analysis. Consequently, the figure alone does not fully explain the transition from the randomized populations (`172` and `166`) to the primary-analysis populations (`159` and `149`).
- **Exact source locations and statements:**

  | Source location | Reported statement or value | Relevance to participant flow |
  |---|---|---|
  | `jama_blakely_2024_oi_240020_1710443209.74411.pdf`, PDF p. 3 (journal p. 1037), Figure 1, early arm | `172 Randomized`; `163 Received treatment as randomized`; `9 Did not undergo treatment as randomized`; `4 Lost to follow-up`; `159 Included in primary analysis` | The figure displays the matching 9-infant category but does not call it a withdrawal or show it leaving the analysis pathway through a separate exclusion branch. |
  | Same figure, late arm | `166 Randomized`; `157 Received treatment as randomized`; `9 Did not undergo treatment as randomized`; `8 Lost to follow-up`; `149 Included in primary analysis` | The same labeling and branch omission occurs in the late arm. |
  | PDF p. 4 (journal p. 1038), Results—Patient Characteristics | “After randomization, 9 infants were withdrawn from each treatment group ... leaving 163 in the early ... group and 157 in the late ... group.” | The Results text identifies the two 9-infant categories as postrandomization withdrawals, not merely as treatment nonadherence. |
  | PDF p. 4, Statistical Analysis | The intention-to-treat analyses included all randomized infants “except those withdrawn from the study.” | This statement establishes that withdrawal determined analysis exclusion. Failure to receive treatment as randomized, by itself, does not state whether a participant was excluded from analysis. |
  | PDF p. 6 (journal p. 1040), Table 2 note a | “Excludes 9 infants (in each group) who were withdrawn after randomization and 12 who were lost to follow-up (4 in the early repair group and 8 in the late repair group).” | The table note explicitly distinguishes withdrawal from loss to follow-up and identifies both as reductions from the randomized populations to the primary-analysis populations. |

- **Arm-level reconciliation:**

  | Arm | Randomized | Postrandomization withdrawals | Remaining after withdrawal | Lost to follow-up | Included in primary analysis |
  |---|---:|---:|---:|---:|---:|
  | Early repair | 172 | 9 | `172 - 9 = 163` | 4 | `163 - 4 = 159` |
  | Late repair | 166 | 9 | `166 - 9 = 157` | 8 | `157 - 8 = 149` |
  | Total | 338 | 18 | 320 | 12 | 308 |

- **Why the figure is incomplete:** If a reader follows only the explicitly labeled postallocation exclusion boxes in Figure 1, the visible calculations would be `172 - 4 = 168` and `166 - 8 = 158`, which do not produce the displayed analysis totals of 159 and 149. Reconciliation requires the unstated additional step of treating each “9 Did not undergo treatment as randomized” category as a postrandomization withdrawal excluded from analysis. The Results text and Table 2 note supply that information, but Figure 1 does not.
- **Why the terminology matters:** “Did not undergo treatment as randomized” describes treatment receipt or adherence, whereas “withdrawn after randomization and excluded from analysis” describes study/analysis status. A participant may deviate from assigned treatment yet remain in the randomized analysis group; therefore, the Figure 1 wording does not independently communicate the analysis exclusion documented elsewhere in the article.
- **Nature and limit of the finding:** This is a flow-label/branch omission, not an arithmetic error. The final primary-analysis counts are internally reconcilable and agree with Table 2. The issue is Minor because the missing status is recoverable from the Results text and Table 2 note and does not, by itself, demonstrate that the outcome calculations or trial conclusion are incorrect.
- **Suggested figure clarification:** Add a separate branch in each arm labeled `Withdrawn after randomization and excluded from primary analysis (n = 9)`, followed by `Remaining after withdrawal (n = 163 early; n = 157 late)`, before the `Lost to follow-up` and `Included in primary analysis` boxes.
- **Verification instruction:** On PDF p. 3, trace each arm from randomization to the primary-analysis box and note that only loss to follow-up is explicitly shown as a subsequent exclusion. Then compare the two 9-infant categories with the explicit withdrawal statement on PDF p. 4 and the exclusion wording in Table 2 note a on PDF p. 6; verify `172 - 9 - 4 = 159` and `166 - 9 - 8 = 149`.

### C5 — Enrollment-details cross-reference incorrectly includes outcome-analysis eTable 2

- **Category / severity:** Presentation inconsistency — Minor.
- **Issue in one sentence:** In the Patient Characteristics section, the article directs readers seeking “additional enrollment details” to “eTables 1-2,” but only eTable 1 contains the referenced enrollment, eligibility, and refusal information; eTable 2 reports frequentist primary and secondary outcome analyses.
- **Exact source locations and statements:**

  | Source location | Reported statement or content | Relevance to the cross-reference |
  |---|---|---|
  | Main article, `jama_blakely_2024_oi_240020_1710443209.74411.pdf`, PDF p. 4 (journal p. 1038), Results—Patient Characteristics | After reporting why 613 parents or guardians refused participation, the text states that “additional enrollment details appear in eTables 1-2” and separately states that randomization-by-site details appear in eTable 3. | The plural range “eTables 1-2” represents the cross-reference under review and indicates that both eTable 1 and eTable 2 provide additional enrollment information. |
  | Results supplement, `joi240020supp3_prod_1710443209.75411.pdf`, PDF pp. 2-4, eTable 1 | Title: “Additional information related to trial enrollment.” The table lists factors affecting eligibility or repair timing, reasons for refusal by parents/guardians (`n = 613`), reasons for refusal by physicians (`n = 37`), and other reasons eligible infants were not consented (`n = 16`). | This table directly supplies the additional enrollment and nonparticipation details promised by the main-text citation. |
  | Results supplement, PDF p. 5, eTable 2 | Title: “Frequentist primary and major secondary outcome analyses.” It reports serious-adverse-event counts (`44/159` early vs `27/149` late), risk difference, relative risk, confidence intervals, P values, hospital-day summaries, and the fitted statistical models. | These are outcome-analysis results, not the enrollment and refusal details discussed in the cited Patient Characteristics paragraph. |
  | Main article, PDF p. 3 (journal p. 1037), Figure 1 note b | “Additional information appears in eTable 1 in Supplement 3.” | Figure 1 directs the same type of enrollment information to eTable 1 alone, consistent with the supplement’s actual contents. |
  | Main article, PDF p. 6 (journal p. 1040), Primary Outcome | “The frequentist analyses were consistent with these findings (eTable 2 in Supplement 3).” | This is the content-appropriate cross-reference for eTable 2 and confirms its role as an outcome-analysis table. |

- **Content-to-reference comparison:**

  | Information sought by the reader | eTable 1 | eTable 2 |
  |---|:---:|:---:|
  | Additional trial-enrollment information | Yes | No |
  | Reasons for parent/guardian refusal | Yes | No |
  | Reasons for physician refusal | Yes | No |
  | Other reasons eligible infants were not consented | Yes | No |
  | Primary serious-adverse-event outcome analysis | No | Yes |
  | Major secondary hospital-days analysis | No | Yes |
  | Frequentist effect estimates, confidence intervals, and P values | No | Yes |

- **Direct numerical linkage to the cited paragraph:** The Patient Characteristics paragraph summarizes the 613 parent/guardian refusals as `280` preferring early repair, `196` preferring late repair, `71` preferring that the clinician decide, and `66` giving other reasons. eTable 1 reproduces and expands this exact enrollment breakdown, and the components reconcile as `280 + 196 + 71 + 66 = 613`. eTable 2 does not report these values or any comparable refusal breakdown.
- **Why the cross-reference is mismatched:** The phrase “additional enrollment details appear in eTables 1-2” assigns an enrollment-information function to both tables in the cited range. The source package supports that function for eTable 1 but not for eTable 2. The correct semantic mapping is `enrollment/refusal details -> eTable 1` and `frequentist outcome analyses -> eTable 2`.
- **Qualification regarding text below eTable 2:** A short paragraph below eTable 2 describes participating centers and notes that site-level randomization counts are provided below. It does not provide the enrollment-refusal breakdown discussed in the Patient Characteristics paragraph. Moreover, the main article separately directs randomization-by-site details to eTable 3. This paragraph therefore does not resolve the mismatch between “additional enrollment details” and the substantive contents of eTable 2.
- **Nature and limit of the finding:** This is a cross-reference/presentation error, not a numerical or statistical-result error. eTable 1—the correct destination—is already included in the printed citation, so a reader can still locate the relevant information. eTable 2 itself is not erroneous and is correctly cited elsewhere for the frequentist outcome analyses. These factors support Minor severity.
- **Suggested correction:** Replace “additional enrollment details appear in eTables 1-2” with “additional enrollment details appear in eTable 1.” A fully clarified sentence would distinguish the destinations as follows: `Additional enrollment details appear in eTable 1, and details of randomization by study site appear in eTable 3 in Supplement 3.`
- **Verification instruction:** Read the cross-reference in the Patient Characteristics paragraph on main-article PDF p. 4. Compare it with the titles and substantive rows of eTable 1 on supplement PDF pp. 2-4 and eTable 2 on supplement PDF p. 5. Confirm that the enrollment/refusal counts summarized in the main text occur in eTable 1, while eTable 2 contains frequentist outcome analyses; then confirm that Figure 1 note b cites eTable 1 alone and that the Primary Outcome text on main-article PDF p. 6 cites eTable 2 for its appropriate purpose.

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
