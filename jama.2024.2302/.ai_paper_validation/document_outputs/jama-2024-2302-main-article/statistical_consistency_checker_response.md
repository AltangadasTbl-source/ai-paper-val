# Statistical consistency checker response

## Scope

- Main article: `jama_blakely_2024_oi_240020_1710443209.74411.pdf`, PDF pp. 1–10.
- Results supplement: `joi240020supp3_prod_1710443209.75411.pdf`, result-relevant PDF pp. 2–5 only.
- Evidence used: the retained main-text evidence map, results-supplement evidence map, source-linked normalized text, and retained page renders. A 200-dpi render of main-article PDF p. 1 was additionally retained as `preprocessing/page_images/page-001.png` to verify the abstract wording.
- Protocol and SAP were not opened.
- Classification: 3 local candidates (1 definite count inconsistency, 1 model-dependent presentation ambiguity, and 1 minor cross-reference mismatch). No external evidence was used.

## Local candidates

### SC-1 — Abstract mislabels 320 infants as having undergone operative repair

- **Category:** Presentation inconsistency
- **Confidence:** High
- **Locations and source values:**
  - Main article, PDF p. 1 (journal p. 1035), Abstract, Results: “Among the 338 randomized infants (172 in the early repair group and 166 in the late repair group), **320 underwent operative repair** …”
  - Main article, PDF p. 4 (journal p. 1038), Surgery Characteristics: **152/163** early-group infants underwent repair.
  - Main article, PDF p. 5 (journal p. 1039), Surgery Characteristics: **129/157** late-group infants underwent repair.
  - Main article, PDF p. 3 (journal p. 1037), Figure 1: early repairs are **147 before discharge + 5 after discharge = 152**; late repairs are **90 after 55 weeks + 39 before 55 weeks = 129**.
  - Main article, PDF p. 5 (journal p. 1039), Table 1 headers: **163 early + 157 late = 320**, after excluding 9 withdrawals in each randomized group.
- **Calculation / logical basis:** The reported operative-repair total from the treatment-pathway counts is **152 + 129 = 281**, not 320. The number 320 instead equals the postwithdrawal cohort, **338 − 18 = 320**. The abstract’s adjacent 86% male value also matches **274/320 = 85.6%**, reinforcing that 320 is the Table 1/postwithdrawal population rather than the operative-repair population.
- **Uncertainty:** Low. The abstract wording and repair counts were verified directly from source-linked page evidence. The issue is the population label, not a dispute about the arm-specific repair counts.
- **Verification instruction:** On PDF pp. 1, 3–5, verify the abstract phrase “320 underwent operative repair,” then sum the two explicitly reported repair counts (152 and 129) and confirm that 320 is instead 163 + 157 after withdrawals.

### SC-2 — The repeated overall risk-difference credible interval has different upper limits without an explicit reconciliation

- **Category:** Presentation inconsistency
- **Confidence:** Moderate; model-dependent
- **Locations and source values:**
  - Main article, PDF p. 1 (journal p. 1035), Abstract, Results; and PDF p. 6 (journal p. 1040), Primary Outcome/Table 2: absolute risk difference **−7.9% (95% CrI, −16.9% to 0%)**.
  - Main article, PDF p. 8 (journal p. 1042), Figure 3, Overall row: risk difference **−0.08 (95% CrI, −0.17 to 0.002)**.
  - These locations repeat the same event counts (**44/159 vs 27/149**), RR (**0.68; 95% CrI, 0.45–1.01**), and favorable-outcome probability (**97%**).
- **Calculation / logical basis:** On the percentage scale, the Figure 3 interval is **−17% to +0.2%**, whereas Table 2/abstract report **−16.9% to 0%**. The positive upper endpoint of +0.2 percentage points does not reproduce the printed 0% endpoint at the displayed one-decimal percentage precision. The article does not explicitly state why the repeated “Overall” risk-difference interval changes while the RR interval and posterior probability remain identical.
- **Uncertainty:** Material. Table 2 says its estimates come from the primary Bayesian logistic model; Figure 3 says its estimates come from Bayesian logistic models that also include a subgroup variable and interaction. Different posterior standardization or model output could legitimately produce slightly different risk-difference intervals. Confidence-interval/credible-interval symmetry was not assumed, and this is retained only as a presentation ambiguity pending model-level verification.
- **Verification instruction:** Compare the underlying posterior summaries used for Table 2 and the Figure 3 Overall row. Determine whether the Figure 3 overall risk difference intentionally comes from a subgroup interaction model or whether one printed upper endpoint/precision is erroneous; if model-specific, add or confirm an explanatory label.

### SC-3 — Main Results text points enrollment details to eTable 2, which contains outcome analyses

- **Category:** Presentation inconsistency
- **Confidence:** High, but minor
- **Locations and source values:**
  - Main article, PDF p. 4 (journal p. 1038), Results—Patient Characteristics: “additional enrollment details appear in **eTables 1-2** …”
  - Results supplement, PDF pp. 2–4, eTable 1: additional trial-enrollment and refusal details.
  - Results supplement, PDF p. 5, eTable 2 title: “**Frequentist primary and major secondary outcome analyses**”; its rows report the primary SAE outcome and hospital days, not enrollment details.
  - Main article, PDF p. 3 (journal p. 1037), Figure 1 note b correctly directs additional enrollment information to **eTable 1**.
- **Calculation / logical basis:** The cross-reference label includes eTable 2 in an enrollment-details citation, but eTable 2 is an outcome-analysis table. The source package supports eTable 1, not eTables 1–2, for the stated enrollment details.
- **Uncertainty:** Low. This is a cross-reference mismatch, not a numerical outcome discrepancy.
- **Verification instruction:** Follow the PDF p. 4 cross-reference and confirm that only eTable 1 (supplement pp. 2–4) contains the referenced enrollment details; inspect eTable 2 on supplement p. 5 to confirm its outcome-analysis content.

## Verified passes

1. **Primary outcome counts and denominators repeat consistently.** Main abstract, Results, Table 2, Figure 3, and supplement eTable 2 report 44/159 (28%) early versus 27/149 (18%) late. The displayed percentages agree with the fractions after rounding.
2. **Frequentist point estimates, confidence intervals, null values, and P values are coherent.** Supplement eTable 2 reports risk difference −9.0% (95% CI, −16.5% to −2.0%), P=.01, and RR 0.65 (95% CI, 0.46–0.92), P=.01; both intervals exclude their respective nulls (0 and 1). Hospital days RR 0.91 (95% CI, 0.74–1.12), P=.36 contains 1 and is compatible with a nonsignificant two-sided P value.
3. **Bayesian point estimates lie within their credible intervals.** This holds for the overall primary outcome, hospital-days outcome, and every Figure 3 subgroup estimate.
4. **Bayesian null-value relationships and posterior probabilities are directionally coherent.** Overall RR 0.68 (95% CrI, 0.45–1.01) with 97% probability favoring late repair is compatible with a percentile interval slightly crossing 1. The Figure 3 subgroup intervals excluding 1 (<28 weeks and bronchopulmonary dysplasia “yes”) have 99% favorable probabilities; intervals crossing 1 have favorable probabilities from 61% to 96%.
5. **No conflict was assigned to Bayesian versus frequentist estimates.** The main analysis reports Bayesian RD −7.9% and RR 0.68, while supplement eTable 2 reports frequentist RD −9.0% and RR 0.65. The package states that the frequentist primary model used a GEE logistic model because the mixed-effects model did not converge; the estimates therefore need not be identical.
6. **Hospital-days estimates repeat consistently apart from expected Bayesian/frequentist interval differences.** Both sources report medians 19.0 (IQR 9.8–35.0) versus 16.0 (7.0–38.0) and RR 0.91; the Bayesian 95% CrI is 0.74–1.11 and frequentist 95% CI is 0.74–1.12.
7. **Effect direction is consistent.** Main Table 2/Figure 3 define late relative to early as favorable for RD <0 and RR <1. The event rates, Bayesian effects, frequentist effects, posterior probabilities, text, abstract, and conclusions all follow that orientation. Although supplement eTable 2 does not restate the contrast direction, its negative RD and RR below 1 align with the same late-versus-early comparison.
8. **Subgroup labels, counts, and denominators align.** Gestational-age totals are 102+57=159 early and 99+50=149 late; bronchopulmonary-dysplasia totals are 81+78=159 and 73+76=149. Text and Figure 3 consistently use <28 versus ≥28 weeks and bronchopulmonary dysplasia yes versus no, with the same RRs, credible intervals, and posterior probabilities.
9. **Enrollment accounting checked against supplement eTable 1.** Parent/guardian refusal reasons sum to 613; physician refusal reasons sum to 37; “other reasons” sum to 16; the “associated factor affecting timing” rows sum to 51, matching the Figure 1 category. Main flow totals also reconcile: 442 ineligible + 734 eligible but not randomized + 338 randomized = 1514 assessed.
10. **Repeated P values do not conflict.** The only outcome P values in scope are in supplement eTable 2. P=.01 is repeated for the two effect scales of the same primary comparison and is compatible with both reported confidence intervals; P=.36 for hospital days is compatible with its confidence interval.

## Rejected / not retained

- **Credible-interval symmetry checks:** Not performed; the article reports percentile-based Bayesian intervals, so symmetry is not a valid default assumption.
- **Raw subgroup rate versus model-estimate differences:** Not treated as errors. Figure 3 states that hierarchical logistic models with subgroup interactions generated the effects, so adjusted/shrunken estimates need not equal crude ratios or differences from displayed cell counts.
- **Primary-model wording in eTable 2:** The note first describes the common mixed-model framework and then explicitly identifies the frequentist primary-analysis GEE exception. The exception is sufficient to avoid treating the wording as a model-result contradiction.
- **Surgical-approach subgroup totals below all repaired infants:** Not retained. Figure 3 is based on the 308 complete primary-outcome cases; its approach totals can therefore be smaller than the repair counts in the 320 postwithdrawal cohort.

