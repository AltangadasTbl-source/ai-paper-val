# AI Paper Validation Final Report

**Article package:** *An mHealth (Mobile Health) Intervention for Smoking Cessation in People With Tuberculosis—A Cluster Randomized Clinical Trial*

**Detailed-report revision date:** 2026-08-13

**Decision status:** Verification and explanation only; all evidence-verifier dispositions and critic decisions are locked.

This report is a source-verifiable expansion of the completed validation workflow. It does not reassess the science, introduce new candidates, or change a disposition, category, severity, candidate scope, or critic inclusion decision. “Verified” means that the completed evidence-verification stage found the candidate’s cited comparison reproducible from the supplied files. “Uncertain” means that the supplied package lacked information needed to resolve the candidate. Critic exclusion is reported separately and does not alter the evidence verifier’s disposition.

# 1. Package Manifest

| Source file | Pages | Classification | Scientific audit scope | Processing disposition | SHA-256 confirmed 2026-08-13 |
|---|---:|---|---|---|---|
| [jama_zahid_2025_oi_250093_1768590553.08463.pdf](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1) | 9 | Main article | PDF pp. 1–9 | Audited after institutional approval recorded 2026-07-21 | `08d435cbc9ce99ba2e85de0a0edb7ee8e5015f3970a42550420ac3f9ae4cf103` |
| [joi250093supp1_prod_1768590553.08963.pdf](../joi250093supp1_prod_1768590553.08963.pdf#page=1) | 109 | Composite non-results supplement: protocol, statistical analysis plan, intervention materials | Not Audited by Design; no result-relevant pages identified and no parent-requested protocol comparison | Rights screen only | `0dcbfdf53363088fa65146d05d2f0e58b9c9f2fa001c9d60232207bbdec440a1` |
| [joi250093supp2_prod_1768590553.09463.pdf](../joi250093supp2_prod_1768590553.09463.pdf#page=1) | 16 | Results supplement | PDF pp. 3–16; pp. 1–2 excluded from scientific audit | Audited after institutional approval recorded 2026-07-21 | `a2b6c06f49f22bf3c5557b7943804c7598154d2e7ca40e7fcbad4dc32bed25e6` |

The hashes, byte sizes, and modification times of all three source PDFs match the workflow integrity record. No workbook was supplied. All derived text, OCR, page renders, checker responses, and review records remain under `.ai_paper_validation/`; the source PDFs were treated as read-only.

# 2. AI Training Restriction Summary

This compliance screen is separate from the scientific findings, does not count toward the candidate limit, is not legal advice, and does not infer permission from silence.

| Source file | Status | Exact supplied-file evidence | Human compliance status |
|---|---|---|---|
| [jama_zahid_2025_oi_250093_1768590553.08463.pdf](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=1) | Explicit AI Training Restriction | PDF p. 1 footer: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” Embedded metadata contained no separate AI-use permission. | Human Compliance Review required; institutional approval recorded 2026-07-21. |
| [joi250093supp1_prod_1768590553.08963.pdf](../joi250093supp1_prod_1768590553.08963.pdf#page=1) | No AI Training Restriction Located in Provided Materials | All 109 pages were screened through the native text layer. Visual review covered [PDF p. 1](../joi250093supp1_prod_1768590553.08963.pdf#page=1), [p. 2](../joi250093supp1_prod_1768590553.08963.pdf#page=2), [p. 41](../joi250093supp1_prod_1768590553.08963.pdf#page=41), [p. 77](../joi250093supp1_prod_1768590553.08963.pdf#page=77), [p. 78](../joi250093supp1_prod_1768590553.08963.pdf#page=78), [p. 101](../joi250093supp1_prod_1768590553.08963.pdf#page=101), and [p. 109](../joi250093supp1_prod_1768590553.08963.pdf#page=109); document information and XMP metadata were also inspected. No applicable AI-training, fine-tuning, model-improvement, rights, licence, permissions, or text-and-data-mining language was located. | Not required by this record; permission is not inferred. |
| [joi250093supp2_prod_1768590553.09463.pdf](../joi250093supp2_prod_1768590553.09463.pdf#page=1) | Explicit AI Training Restriction | PDF p. 1 footer: “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” Embedded metadata contained no separate AI-use permission. | Human Compliance Review required; institutional approval recorded 2026-07-21. |

# 3. Audit Method and Revision Status

The completed workflow inventoried all supplied PDFs, retained one rights record per PDF, preprocessed only the main article and result-relevant supplement pages, extracted result claims, ran arithmetic, figure/flow, and statistical checks, and advanced ten formal candidates to one evidence-verification stage. The evidence verifier recorded 9 Verified, 1 Uncertain, and 0 Rejected candidates. The critic retained eight Verified candidates as scientific findings, retained the one Uncertain candidate for adjudication, and excluded one verifier-Verified candidate from the final scientific finding list. This revision re-opened every cited original page and visually checked the cited tables and text. It is the second and final source-verification round for report-detailing purposes.

The prior short report described C09 as “Rejected.” The authoritative records are more specific: the evidence verifier classified C09 as **Verified**, while the critic **rejected/excluded it from the final scientific finding list** because treating the documented difference as a reporting error would be speculative. This report preserves both locked decisions and does not convert the critic’s inclusion decision into a verifier disposition.

## Source-verification exception requiring Human Adjudication

For C06, the authoritative verifier record states that every complete adverse-event symptom block totals 699 mHealth and 334 control observations. Direct re-addition of the source rows confirms 699/334 for ten of eleven symptoms, but the mHealth epigastric-pain block totals `505 + 143 + 43 + 7 = 698`, while its control block totals 334. The any-grade mHealth count is `143 + 43 + 7 = 193`, and `193/698 = 27.6504%`, which rounds to the reported 27.7%. The exception concerns one detail in the verifier’s generalized denominator statement; it does **not** change C06’s locked Verified disposition because the table still does not identify its analysis population or symptom-specific missingness. Human adjudicators should verify this 698 total directly in [joi250093supp2_prod_1768590553.09463.pdf](../joi250093supp2_prod_1768590553.09463.pdf#page=15), PDF p. 15, eTable 10, Epigastric pain block.

No other cited location, quotation, value, or calculation failed source verification.

# 4. Candidate Disposition Summary

Candidate order and count are preserved from the authoritative workflow. Severity is shown only where the critic assigned one.

| Candidate | Disposition | Category | Severity |
|---|---|---|---|
| C01 | Verified | Cross-document inconsistency | Major |
| C02 | Verified | Arithmetic inconsistency | Minor |
| C03 | Verified | Arithmetic inconsistency | Minor |
| C04 | Verified | Statistical reporting inconsistency | Minor |
| C05 | Verified | Cross-document inconsistency | Major |
| C06 | Verified | Presentation inconsistency | Minor |
| C07 | Uncertain | Statistical reporting inconsistency | Not assigned |
| C08 | Verified | Statistical reporting inconsistency | Minor |
| C09 | Verified | Cross-document inconsistency | Not assigned |
| C10 | Verified | Presentation inconsistency | Minor |

The critic accepted C01–C06, C08, and C10 as final scientific findings, retained C07 as Uncertain, and rejected/excluded C09 from the final scientific finding list. These critic decisions do not alter the verifier dispositions in the table.

# 5. Verified Scientific Findings

The eight entries in this section are exactly the verifier-Verified candidates accepted by the critic.

## C01 — Omitted mHealth cluster in the prior-quit-attempt table

- **Evidence status:** Verified
- **Category:** Cross-document inconsistency
- **Severity:** Major
- **Exact source locations:** [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 4](../joi250093supp2_prod_1768590553.09463.pdf#page=4), eTable 2, both study-arm blocks; [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 8](../joi250093supp2_prod_1768590553.09463.pdf#page=8), eTable 5, site 2012 row. [jama_zahid_2025_oi_250093_1768590553.08463.pdf, PDF p. 5](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5), journal p. 340, Table 1, cluster totals, participant totals, and “Attempted to quit in past” row.
- **Reported values/statements:** Table 1 reports 18 mHealth clusters of size 40, 720 mHealth participants, and 178 (24.7%) who had attempted to quit. eTable 2 displays only 17 mHealth site rows. eTable 5 identifies site 2012 as mHealth and reports a 40-person recruited/ITT denominator.

**Reasoning procedure**

1. The 17 mHealth rows in eTable 2 list these Yes counts: `13 + 0 + 7 + 0 + 23 + 9 + 16 + 11 + 1 + 4 + 9 + 11 + 19 + 18 + 5 + 6 + 16 = 168`.
2. Their No counts are `27 + 40 + 33 + 40 + 17 + 31 + 24 + 29 + 39 + 36 + 31 + 29 + 21 + 22 + 35 + 34 + 24 = 512`.
3. Each displayed row has Yes + No = 40, and `168 + 512 = 680 = 17 × 40`.
4. Compare those direct eTable 2 totals with direct Table 1 totals: participant shortfall `720 − 680 = 40`; Yes shortfall `178 − 168 = 10`; implied No shortfall `(720 − 178) − 512 = 542 − 512 = 30`.
5. The implied `10 Yes + 30 No = 40` is a **derived reconciliation**, not a printed site-2012 observation. It yields `10/40 = 25.0%` only under the table’s binary Yes/No structure.
6. eTable 5 independently identifies the absent site: its final row reads mHealth, site 2012, recruitment `40/239 (16.7%)`, and ITT quitter `20/40 (50)`.
7. As a negative-control check, the nine usual-care eTable 2 rows yield Yes `10 + 1 + 0 + 0 + 5 + 3 + 0 + 4 + 10 = 33`, No `327`, and total `360`, exactly reproducing Table 1. The omission is therefore confined to the mHealth block.
8. The displayed percentages conceal the discrepancy: `168/680 = 24.7059%` and `178/720 = 24.7222%` both round to 24.7%.

- **Existing supported conclusion:** eTable 2 omits one mHealth cluster relative to Table 1 and eTable 5, displaying 680 participants and 168 prior-attempt Yes responses rather than 720 and 178.
- **Limit on interpretation:** The files establish the table-level omission but do not print site 2012’s prior-attempt values. The derived 10/30 split must not be treated as observed site data, and the production mechanism is unknown.
- **Verification instruction:** In [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 4](../joi250093supp2_prod_1768590553.09463.pdf#page=4), eTable 2, tick off and sum all mHealth and usual-care rows separately. Compare them with [jama_zahid_2025_oi_250093_1768590553.08463.pdf, PDF p. 5](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5), journal p. 340, Table 1, then locate mHealth site 2012 and its denominator 40 in [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 8](../joi250093supp2_prod_1768590553.09463.pdf#page=8), eTable 5. Reproduce all four differences above.

## C02 — Site 2008 death percentage is incompatible with its cluster denominator

- **Evidence status:** Verified
- **Category:** Arithmetic inconsistency
- **Severity:** Minor
- **Exact source locations:** [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 9](../joi250093supp2_prod_1768590553.09463.pdf#page=9), eTable 6, Control/site 2008 row; [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 8](../joi250093supp2_prod_1768590553.09463.pdf#page=8), eTable 5, Control/site 2008 row. Corroborating cluster size: [jama_zahid_2025_oi_250093_1768590553.08463.pdf, PDF p. 5](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5), journal p. 340, Table 1.
- **Reported values/statements:** eTable 6 prints `Control | 2008 | 5 (7.5)` under Deaths `n(%)`. eTable 5 prints site 2008 with recruitment `40/484 (8.2%)` and ITT quitter `12/40 (30)`.

**Reasoning procedure**

1. The direct denominator evidence is 40 participants for site 2008.
2. Recalculate the displayed rate: `(5/40) × 100 = 12.5%`.
3. The printed percentage differs by `12.5 − 7.5 = 5.0` percentage points. Conversely, `7.5% × 40 = 3` deaths, not the printed count of 5.
4. The within-table denominator rule is consistent elsewhere: 1, 2, 3, 4, and 6 deaths correspond to 2.5%, 5.0%, 7.5%, 10.0%, and 15.0% of 40. Site 2012 is an especially direct comparison: 5 deaths are printed as 12.5%.
5. The nine control counts sum to `1 + 0 + 4 + 2 + 2 + 3 + 4 + 5 + 6 = 27`; the 18 mHealth counts sum to 25. These reproduce the arm totals in eTable 4 and support the transcribed count of 5, without establishing which source field should be edited.

- **Existing supported conclusion:** The displayed `5 (7.5)` is arithmetically inconsistent with the 40-person site denominator; the diagnostic percentage is 12.5%.
- **Limit on interpretation:** The table does not print denominators in its own body. The denominator is established by eTable 5, Table 1, and consistent neighboring rows. The package does not establish whether the count or percentage should be corrected or how the inconsistency arose.
- **Verification instruction:** Read site 2008 in [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 8](../joi250093supp2_prod_1768590553.09463.pdf#page=8), eTable 5, and [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 9](../joi250093supp2_prod_1768590553.09463.pdf#page=9), eTable 6; calculate `5 ÷ 40 × 100`, compare it with a 3-death/7.5% row and site 2012’s 5/12.5% row, and sum both arm counts.

## C03 — Death-cause percentages do not reproduce from the printed column totals

- **Evidence status:** Verified
- **Category:** Arithmetic inconsistency
- **Severity:** Minor
- **Exact source location:** [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 6](../joi250093supp2_prod_1768590553.09463.pdf#page=6), eTable 4, “Causes of deaths among two study groups.”
- **Reported values/statements:** Column totals are 52 overall, 25 mHealth, and 27 usual care. In usual care, “Drug user” and “Severe pneumonia” are each printed `1 (7.4%)`.

**Reasoning procedure**

1. Count partitions reconcile exactly. Overall: `32 + 3 + 8 + 2 + 2 + 2 + 1 + 1 + 1 = 52`; mHealth: `16 + 0 + 5 + 1 + 0 + 2 + 0 + 1 + 0 = 25`; usual care: `16 + 3 + 3 + 1 + 2 + 0 + 1 + 0 + 1 = 27`; and `25 + 27 = 52`.
2. Because each column is labeled `n(%)`, calculate each percentage against that column’s total.
3. The primary direct discrepancies are `1/27 × 100 = 3.7037%`, conventionally 3.7%, for both Drug user and Severe pneumonia—not 7.4%. The printed 7.4% equals `2/27` and is correctly paired with the Stroke count of 2.
4. Additional one-decimal deviations retained by the verifier and critic are:

   - Usual-care death due to TB: `16/27 = 59.2593% → 59.3%`, printed 59.2%.
   - Overall cancer: `3/52 = 5.7692% → 5.8%`, printed 5.7%.
   - Overall heart attack: `8/52 = 15.3846% → 15.4%`, printed 15.2%.

5. Other examples reproduce normally: `32/52 = 61.5%`, `16/25 = 64.0%`, `3/27 = 11.1%`, `2/27 = 7.4%`, and `1/25 = 4.0%`.
6. The printed usual-care percentages sum to 107.3%, while the unrounded count-derived shares sum to 100%. This is corroborative only, because independently rounded percentages need not sum to exactly 100%.

- **Existing supported conclusion:** eTable 4 contains arithmetic inconsistencies, most clearly the two usual-care `1 (7.4%)` cells, for which conventional one-decimal calculation gives 3.7% each.
- **Limit on interpretation:** The check establishes incompatibility among displayed counts, totals, and percentages. It does not validate underlying causes of death, identify which field should be corrected, or establish a row-shift or rounding mechanism.
- **Verification instruction:** Transcribe all three totals and nine cause rows from [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 6](../joi250093supp2_prod_1768590553.09463.pdf#page=6), eTable 4; sum every count column, then calculate `n ÷ column total × 100` for each cell. Compare the two one-count/7.4% rows directly with the two-count Stroke/7.4% row.

## C04 — Main-text nausea and diarrhoea percentages do not reproduce from eTable 10

- **Evidence status:** Verified
- **Category:** Statistical reporting inconsistency
- **Severity:** Minor
- **Exact source locations:** [jama_zahid_2025_oi_250093_1768590553.08463.pdf, PDF p. 5](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5), journal p. 340, Adverse Events; [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 15](../joi250093supp2_prod_1768590553.09463.pdf#page=15), eTable 10, Nausea and Diarrhoea blocks.
- **Reported values/statements:** The main text reports “nausea (23.0% for mHealth vs 22.3% for usual care), diarrhea (7.5% vs 7.5%).” eTable 10 prints all four severity counts for each symptom and arm.

**Reasoning procedure**

1. Define any-grade occurrence from the displayed mutually exclusive severity rows as Mild + Moderate + Severe; obtain the represented denominator by adding None.
2. Nausea, mHealth: numerator `124 + 31 + 6 = 161`; denominator `538 + 124 + 31 + 6 = 699`; `161/699 = 23.0329% → 23.0%`. This reproduces the prose.
3. Nausea, control: numerator `64 + 7 + 0 = 71`; denominator `263 + 64 + 7 + 0 = 334`; `71/334 = 21.2575% → 21.3%`, not 22.3%.
4. Diarrhoea, mHealth: numerator `43 + 6 + 2 = 51`; denominator `648 + 43 + 6 + 2 = 699`; `51/699 = 7.2961% → 7.3%`, not 7.5%.
5. Diarrhoea, control: numerator `22 + 3 + 0 = 25`; denominator `309 + 22 + 3 + 0 = 334`; `25/334 = 7.4850% → 7.5%`. This reproduces the prose.
6. Diagnostic coincidences do not resolve the discrepancy: `71/318 = 22.3%`, where 318 is a primary-outcome complete-case/PP denominator elsewhere; `51/680 = 7.5%`, where 680 is the incomplete mHealth total in eTable 2. eTable 10 identifies neither 318 nor 680 as an adverse-event denominator.

- **Existing supported conclusion:** The eTable 10 counts reproduce the main-text mHealth nausea and control diarrhoea percentages, but yield 21.3% rather than 22.3% for control nausea and 7.3% rather than 7.5% for mHealth diarrhoea.
- **Limit on interpretation:** The diagnostic alternative denominators are numerical coincidences, not evidence of intended denominators or a production mechanism. The finding is limited to the cross-presentation mismatch.
- **Verification instruction:** Transcribe the main-text sentence. For both symptoms and arms, sum the three non-None categories, add None for the represented denominator, calculate and round to one decimal, then mark which two prose values reproduce.

## C05 — The adverse-event direction statement is reversed for irritability and anxiety

- **Evidence status:** Verified
- **Category:** Cross-document inconsistency
- **Severity:** Major
- **Exact source locations:** [jama_zahid_2025_oi_250093_1768590553.08463.pdf, PDF p. 5](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5), journal p. 340, Adverse Events; [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 15](../joi250093supp2_prod_1768590553.09463.pdf#page=15), eTable 10, Dry mouth, Irritability, and Anxiety blocks.
- **Reported values/statements:** After reporting dry mouth `62.7% vs 55.7%`, irritability `40.5% vs 43.4%`, and anxiety `33.3% vs 36.8%`, the main text states: “Of these, dry mouth, irritability, and anxiety were more common in the mHealth group.”

**Reasoning procedure**

1. Dry mouth any-grade occurrence: mHealth `(267 + 116 + 55)/699 = 438/699 = 62.6609% → 62.7%`; control `(154 + 23 + 9)/334 = 186/334 = 55.6886% → 55.7%`. Dry mouth is 7.0 percentage points higher in mHealth and follows the stated direction.
2. Irritability: mHealth `(175 + 78 + 30)/699 = 283/699 = 40.4864% → 40.5%`; control `(117 + 24 + 4)/334 = 145/334 = 43.4132% → 43.4%`. Any-grade irritability is 2.93 percentage points lower in mHealth.
3. Anxiety: mHealth `(168 + 48 + 17)/699 = 233/699 = 33.3333% → 33.3%`; control `(110 + 12 + 1)/334 = 123/334 = 36.8263% → 36.8%`. Any-grade anxiety is 3.49 percentage points lower in mHealth.
4. Thus, both the table-derived rates and the percentages printed immediately before the statement contradict “more common” for irritability and anxiety; only dry mouth follows it.
5. An alternative pattern exists for moderate-or-severe events: irritability is `108/699 = 15.5%` versus `28/334 = 8.4%`, and anxiety is `65/699 = 9.3%` versus `13/334 = 3.9%`. The omnibus tests may concern the complete four-level severity distribution. This can explain a possible intended severity statement, but the source says “more common,” not “more severe.”

- **Existing supported conclusion:** The main-text direction statement is inconsistent with any-grade irritability and anxiety occurrence, both of which are lower in mHealth; dry mouth alone has the stated direction.
- **Limit on interpretation:** The finding does not challenge the severity-distribution counts, reported tests, causal attribution, or clinical meaning. The package does not establish the intended replacement wording.
- **Verification instruction:** Read the full adverse-event paragraph, sum Mild + Moderate + Severe for all three named symptoms in each arm, divide by each represented symptom total, and compare the resulting directions with the sentence. Calculate Moderate + Severe separately only as an alternative explanatory check.

## C06 — Adverse-event analysis population and missingness are not identified

- **Evidence status:** Verified
- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Exact source locations:** [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 15](../joi250093supp2_prod_1768590553.09463.pdf#page=15) and [PDF p. 16](../joi250093supp2_prod_1768590553.09463.pdf#page=16), eTable 10, header, all symptom blocks, and sole footnote. Comparator populations: [jama_zahid_2025_oi_250093_1768590553.08463.pdf, PDF p. 3](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3), journal p. 338, Statistical Analysis; [PDF p. 4](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4), journal p. 339, Figure 1; [PDF p. 6](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6), journal p. 341, Table 2; and [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 13](../joi250093supp2_prod_1768590553.09463.pdf#page=13), eTable 9.
- **Reported values/statements:** eTable 10 labels arm values only as `n (%)`; its sole note is “a: based on Exact test.” It supplies no adverse-event population, assessment time, denominator, or missing-data rule.

**Reasoning procedure**

1. Add None + Mild + Moderate + Severe within each symptom and arm. Ten of eleven mHealth blocks total 699. The mHealth epigastric-pain block totals 698, as disclosed in the source-verification exception. Every control block totals 334.
2. The documented randomized populations are 720 mHealth and 360 usual care. Relative to those totals, the dominant adverse-event denominators are `720 − 699 = 21` and `360 − 334 = 26` fewer observations.
3. The complete-case/PP denominators in Table 2 are 667 and 318. The dominant adverse-event totals exceed these by `699 − 667 = 32` and `334 − 318 = 16`.
4. The death-excluded eTable 9 denominators are 695 and 333. The dominant adverse-event totals exceed these by `699 − 695 = 4` and `334 − 333 = 1`.
5. The mHealth epigastric-pain block differs from the dominant mHealth total by one observation: `699 − 698 = 1`. No note identifies symptom-specific missingness.
6. Therefore, neither 699/334 nor the single 698/334 block matches the randomized, primary-outcome complete-case, or death-excluded populations, and the table does not reconcile the differences.

- **Existing supported conclusion:** eTable 10 does not identify the adverse-event analysis population or missingness rules needed to interpret its represented denominators.
- **Limit on interpretation:** Events may have been collected from participants contributing data at another time or from another subset, but the package does not say so. The report does not infer the correct population or the cause of the 698 block.
- **Verification instruction:** Add all four severity rows for every symptom in [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 15](../joi250093supp2_prod_1768590553.09463.pdf#page=15) and [PDF p. 16](../joi250093supp2_prod_1768590553.09463.pdf#page=16), including the continuation on p. 16. Record ten mHealth totals of 699, one of 698, and eleven control totals of 334. Compare them with the page-targeted comparator populations cited above, then confirm the absence of a population or missingness note.

## C08 — “Intention to treat” label is retained after deaths are excluded

- **Evidence status:** Verified
- **Category:** Statistical reporting inconsistency
- **Severity:** Minor
- **Exact source locations:** [jama_zahid_2025_oi_250093_1768590553.08463.pdf, PDF p. 3](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3), journal p. 338, Statistical Analysis; [PDF p. 4](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4), journal p. 339, Figure 1; [PDF p. 6](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6), journal p. 341, Table 2. [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 13](../joi250093supp2_prod_1768590553.09463.pdf#page=13) and [PDF p. 14](../joi250093supp2_prod_1768590553.09463.pdf#page=14), eTable 9 and notes.
- **Reported values/statements:** The Methods distinguish the ITT and complete-case analyses from “A post hoc sensitivity analysis ... after excluding deaths.” Table 2’s primary ITT row uses `300/720` and `55/360`. eTable 9 is titled “Post-hoc sensitivity analysis (intention to treat) after excluding deaths” and uses `300/695` and `55/333`.

**Reasoning procedure**

1. Figure 1 directly reports 25 mHealth deaths and 27 usual-care deaths.
2. Subtract deaths from randomized denominators: `720 − 25 = 695`; `360 − 27 = 333`.
3. These are precisely eTable 9’s denominators. Its primary percentages also reproduce: `300/695 = 43.1655% → 43.2%`; `55/333 = 16.5165% → 16.5%`.
4. The same 695/333 denominators recur for the less-than-6-ppm, week-9, month-6, successful-treatment, default, and failure rows.
5. The notes on p. 14 define `n/N` and model abbreviations but do not redefine or qualify the parenthetical “intention to treat.”
6. The directly observed inconsistency is therefore between the retained label and the demonstrably death-excluded population, in a package that separately describes primary ITT and death-excluded post hoc analyses.

- **Existing supported conclusion:** eTable 9 labels a population from which precisely the reported deaths were removed as “intention to treat,” despite the main article presenting death exclusion as a distinct post hoc analysis.
- **Limit on interpretation:** This is an internal labeling finding. It does not assess the validity of the sensitivity estimates or impose an external methodological standard.
- **Verification instruction:** Follow the page-targeted links above to compare the Methods’ analysis descriptions, Figure 1 deaths, Table 2 ITT denominators, eTable 9 title and repeated denominators, and p. 14 notes. Independently reproduce both subtractions.

## C10 — eTable 6 title promises an outcome absent from its body

- **Evidence status:** Verified
- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Exact source location:** [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 9](../joi250093supp2_prod_1768590553.09463.pdf#page=9), eTable 6; [PDF p. 10](../joi250093supp2_prod_1768590553.09463.pdf#page=10) confirms that eTable 7 begins on the next page.
- **Reported values/statements:** The title is “eTable 6. Cluster-wise death rates and unsuccessful TB treatment outcomes.” The body contains study-arm labels, `Site IDs`, and `Deaths n(%)` only.

**Reasoning procedure**

1. Inventory the complete displayed table: it has 27 site rows, comprising 18 mHealth and 9 control clusters.
2. The only numeric outcome column is Deaths `n(%)`; there is no unsuccessful-treatment column, row, definition, statistic, or note.
3. The death counts sum to 25 in mHealth and 27 in control, or 52 overall, confirming that the displayed body is a complete cluster-level death table.
4. PDF p. 10 begins eTable 7, so the promised unsuccessful-treatment content is not a continuation of eTable 6.

- **Existing supported conclusion:** The complete body of eTable 6 does not contain the unsuccessful tuberculosis-treatment outcome named in its title.
- **Limit on interpretation:** The evidence does not establish whether the title is overinclusive, the body is incomplete, or how the mismatch arose.
- **Verification instruction:** Use the separate page-targeted links above to read the full title, inventory every header, row, and note on p. 9, confirm that p. 10 begins eTable 7, and record the absence of any unsuccessful-treatment field.

# 6. Uncertain Candidates

## C07 — “PP” versus complete-case analysis label

- **Evidence status:** Uncertain
- **Category:** Statistical reporting inconsistency
- **Potential severity:** Not assigned by the completed workflow
- **Exact source locations:** [jama_zahid_2025_oi_250093_1768590553.08463.pdf, PDF p. 3](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3), journal p. 338, Statistical Analysis; [PDF p. 4](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=4), journal p. 339, Figure 1; [PDF p. 6](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=6), journal p. 341, Table 2 and abbreviation note.
- **Reported values/statements:** Methods state that effects were assessed through ITT and “complete case analyses (those with missing primary outcome data were discarded).” Table 2 labels two rows `(PP)`, and the note defines PP as per-protocol analysis. Figure 1 shows 53 missing primary outcomes in mHealth and 42 in usual care; the PP denominators are 667 and 318.

**Reasoning procedure**

1. Reconcile the missing counts from Figure 1: mHealth `25 deaths + 18 no contact + 10 withdrew = 53`; usual care `27 + 9 + 6 = 42`.
2. Subtract them from randomized totals: `720 − 53 = 667`; `360 − 42 = 318`.
3. Those results exactly equal both Table 2 PP denominators.
4. Printed PP percentages reproduce from them: `300/667 = 44.98% → 45.0%`; `55/318 = 17.30%`; `264/667 = 39.58% → 39.6%`; `38/318 = 11.95% → 11.9%` as displayed.
5. Direct source observations therefore show that the rows labeled PP use the population obtained by discarding participants with missing primary outcomes, matching the Methods’ complete-case description.
6. The missing inferential definition is an authoritative analysis-population specification stating whether per-protocol status imposed any criteria beyond observed primary-outcome availability. Denominator equality alone cannot establish whether “PP” is erroneous or intentionally names the same population.

- **Existing supported conclusion:** The PP denominators exactly reproduce the described complete-case population, but the package does not resolve whether the PP label is erroneous.
- **Limit on interpretation:** No separate per-protocol eligibility criteria are reported in the audited result materials. The locked disposition remains Uncertain; this report does not use the protocol/SAP exemption to perform a new comparison.
- **Verification instruction:** Follow the three page-targeted main-article links above to read the complete-case definition, sum each arm’s missing categories, subtract from randomized totals, and compare with every PP denominator and the PP abbreviation. Then obtain an authoritative analysis-population specification defining any additional per-protocol criteria before adjudicating the label.

# 7. Rejected and Excluded Interpretations

The evidence verifier rejected **zero** candidates. The critic excluded one verifier-Verified candidate from the final scientific finding list. That inclusion decision is preserved below. It is not reported as an evidence-verifier rejection.

## C09 — Subgroup scheme differs from the stated prespecified list

- **Evidence status:** Verified by the evidence verifier
- **Category:** Cross-document inconsistency
- **Severity:** Not assigned
- **Critic decision:** Rejected/excluded from final scientific findings
- **Exact source locations:** [jama_zahid_2025_oi_250093_1768590553.08463.pdf, PDF p. 3](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=3), journal p. 338, Statistical Analysis; [PDF p. 5](../jama_zahid_2025_oi_250093_1768590553.08463.pdf#page=5), journal p. 340, Results. [joi250093supp2_prod_1768590553.09463.pdf, PDF p. 12](../joi250093supp2_prod_1768590553.09463.pdf#page=12), eTable 8.
- **Reported values/statements:** Methods list prespecified subgroups for age (`<40`, `≥40`), education (no formal, primary, secondary or higher), employment (active, dependent, retired), and smoking duration (`<24`, `≥24 years`). eTable 8 displays age, education, occupation, smoking duration, and Reading SMS; it combines “Dependent or retired.” The Results summarize effects across all five displayed variables without calling SMS-reading post hoc.

**Reasoning procedure**

1. Age categories agree between Methods and eTable 8: `<40` and `≥40`.
2. Education is presented compatibly at a broad level: no formal, primary years 1–5, and secondary or above year ≥6.
3. Employment differs in granularity: Methods list active, dependent, and retired; eTable 8 combines dependent or retired.
4. Smoking-duration categories agree: `<24` and `≥24 years`.
5. Reading SMS Yes/No is present in eTable 8 and the Results summary but absent from the stated prespecified list.
6. These documentary differences support the verifier’s locked Verified comparison.
7. The critic’s locked exclusion rests on a different question: the package does not say that every subgroup displayed in eTable 8 was required to be prespecified or labeled post hoc. Treating the additional, unlabeled SMS-reading analysis as a reporting error would therefore be speculative.

- **Existing supported conclusion:** The evidence verifier confirmed that the displayed subgroup scheme differs from the stated prespecified list; the critic nevertheless excluded it from final findings because the package does not establish that this difference constitutes an error.
- **Limit on interpretation:** Do not call the verifier disposition Rejected, do not promote the candidate into the final findings, and do not infer that the SMS-reading analysis was improperly conducted or that the employment combination was prohibited.
- **Verification instruction:** Follow the separate page-targeted links above to transcribe every variable and category from Methods and eTable 8, confirm the employment combination and added SMS variable, then confirm that neither eTable 8 nor the Results says every displayed subgroup was prespecified. Preserve both locked decisions.

# 8. Human Adjudication Checklist

- [ ] Confirm that all three source filenames, page counts, file sizes, and SHA-256 hashes match the package manifest and integrity record.
- [ ] Confirm the separate compliance dispositions: explicit AI-training language in the main article and results supplement, institutional approval recorded 2026-07-21, and no applicable restriction located in the composite non-results supplement without inferring permission.
- [ ] Adjudicate the eight critic-accepted findings C01, C02, C03, C04, C05, C06, C08, and C10 at their cited pages using the displayed calculations and stated interpretation limits.
- [ ] For C01, distinguish printed observations from the derived 10 Yes/30 No reconciliation; do not treat the latter as observed site-2012 data.
- [ ] For C03, distinguish conventional one-decimal recalculation from any claim about the intended rounding or production mechanism.
- [ ] For C05, preserve the alternative moderate-or-severe calculation as explanatory only; do not substitute it for the locked any-grade direction finding.
- [ ] For C06, verify the source-detail exception: ten mHealth symptom blocks total 699, mHealth epigastric pain totals 698, and all control blocks total 334. Confirm that no population or missingness rule is supplied. Preserve the Verified disposition.
- [ ] Resolve C07 only after obtaining an authoritative analysis-population specification defining whether per-protocol criteria differed from complete-case availability. Until then, retain Uncertain.
- [ ] For C09, preserve the evidence-verifier disposition Verified and the separate critic decision rejected/excluded; do not add it to the final scientific findings.
- [ ] Confirm that there are 10 formal candidates only: 9 Verified, 1 Uncertain, and 0 Rejected by the evidence verifier; 8 of the Verified candidates were accepted by the critic.
- [ ] Confirm that no disposition, category, severity, candidate scope, or critic decision was changed during report detailing.
- [ ] Confirm that every source link is relative, includes a valid `#page=N` fragment matching the cited PDF page, opens the corresponding source location, and that source PDFs remain unchanged.

**Submission status:** Ready for Human Adjudication, subject to the C06 source-verification exception and the unresolved C07 analysis-population definition.
