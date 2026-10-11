# Stable Candidate Ledger

This ledger contains every distinct candidate consistency observation after merging only records that concern the same printed values, comparator, and rule. All candidates are **Pending Human Adjudication**. No severity, validity, acceptance, exclusion, or correction is assigned.

## C001 — Liberal walk-in transport percentage does not reconcile with 4/743

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [Supplement 2, eTable 2, PDF p. 15](../../joi240147supp2_prod_1738701765.29201.pdf#page=15), liberal oxygen group, walk-in transport row.
- **Printed evidence:** `4/743 (5.3)` under a `no./total no. (%)` format.
- **Rule and calculation:** `100 × 4 / 743 = 0.538...%`, which rounds to `0.5%`, not `5.3%`.
- **Direct observation versus inference:** The three printed values and arithmetic mismatch are directly observed. Which field is incorrect is unknown.
- **Alternative source-grounded interpretations:** The count, denominator, or percentage may be mistranscribed; adjacent transport rows use denominator 743 and do not supply a different denominator for this cell.
- **Remaining human question:** Which count, denominator, and percentage are authoritative for liberal-group walk-in transport?
- **Checker provenance:** numeric consistency reviewer; cross-source consistency reviewer.
- **Status:** Pending Human Adjudication

## C002 — Liberal vascular-surgery percentage is nonzero with a printed zero numerator

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [Supplement 2, eTable 2, PDF p. 15](../../joi240147supp2_prod_1738701765.29201.pdf#page=15), liberal oxygen group, vascular surgery row.
- **Printed evidence:** `0/747 (1.1)` under a `no./total no. (%)` format.
- **Rule and calculation:** `100 × 0 / 747 = 0.0%`; a zero numerator cannot yield `1.1%` under the displayed relationship.
- **Direct observation versus inference:** The cell and nonreconciliation are directly observed. Whether the count or percentage is erroneous is unknown.
- **Alternative source-grounded interpretations:** The numerator may be a typographic zero, the percentage may have carried over from another cell, or an unprinted qualifier may exist; no table footnote supplies one.
- **Remaining human question:** What numerator and percentage should be reported for liberal-group vascular surgery?
- **Checker provenance:** numeric consistency reviewer; cross-source consistency reviewer.
- **Status:** Pending Human Adjudication

## C003 — Matched all-patient adjusted confidence-interval upper limit differs between eTables 4 and 7

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [Supplement 2, eTable 4, PDF p. 17](../../joi240147supp2_prod_1738701765.29201.pdf#page=17), primary outcome further-adjusted odds ratio; [Supplement 2, eTable 7, PDF p. 20](../../joi240147supp2_prod_1738701765.29201.pdf#page=20), all-patient adjusted odds ratio.
- **Printed evidence:** eTable 4 prints `0.98 (0.68 to 1.41)`; eTable 7 prints `0.98 (0.68 to 1.39)` for 733 restrictive versus 724 liberal primary-analysis patients and the same 30-day composite outcome.
- **Rule and comparison:** The population, outcome, contrast, effect label, point estimate, and lower endpoint match, but the upper endpoint differs at the displayed two-decimal precision.
- **Direct observation versus inference:** The printed values and shared labels are directly observed. Equality of the underlying adjustment specifications cannot be inferred because eTable 7 does not define them fully.
- **Alternative source-grounded interpretations:** The tables may use different covariate models that are insufficiently distinguished by their labels; if the model is the same, one upper limit is inconsistent.
- **Remaining human question:** Do the two rows use the same model, and what is the authoritative upper confidence limit or distinguishing model label?
- **Checker provenance:** cross-source consistency reviewer; statistical pass 1 recorded the missing model definition.
- **Status:** Pending Human Adjudication

## C004 — AIS less-than-3 subgroup percentage conflicts with its count and matched Figure 4

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [Main article, Figure 4, PDF p. 8](../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8), AIS score less than 3; [Supplement 2, eTable 7, PDF p. 20](../../joi240147supp2_prod_1738701765.29201.pdf#page=20), AIS less than 3.
- **Printed evidence:** Figure 4 prints liberal `48/473 (10.1)`; eTable 7 prints liberal `48/473 (9.2)`.
- **Rule and calculation:** `100 × 48 / 473 = 10.148...%`, which rounds to `10.1%`, not `9.2%`.
- **Direct observation versus inference:** The matched printed numerator, denominator, and percentages are directly observed. The intended correction is unknown.
- **Alternative source-grounded interpretations:** eTable 7 may contain a transcription error or may have used an undisclosed denominator inconsistent with the printed 473.
- **Remaining human question:** What percentage and denominator are authoritative for the liberal AIS-less-than-3 subgroup?
- **Checker provenance:** cross-source consistency reviewer; statistical pass 1 (S018-A).
- **Status:** Pending Human Adjudication

## C005 — Known-lung-disease subgroup percentage conflicts with its count and matched Figure 4

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [Main article, Figure 4, PDF p. 8](../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8), known lung disease, yes; [Supplement 2, eTable 7, PDF p. 20](../../joi240147supp2_prod_1738701765.29201.pdf#page=20), known lung disease, yes.
- **Printed evidence:** Figure 4 prints liberal `14/69 (20.3)`; eTable 7 prints liberal `14/69 (20.2)`.
- **Rule and calculation:** `100 × 14 / 69 = 20.289...%`, which rounds to `20.3%`, not `20.2%`.
- **Direct observation versus inference:** The matched printed values and rounding mismatch are directly observed. The production mechanism is unknown.
- **Alternative source-grounded interpretations:** eTable 7 may contain a rounding/transcription error, or an unreported rounding convention may differ.
- **Remaining human question:** What displayed percentage and rounding convention are authoritative for this subgroup?
- **Checker provenance:** cross-source consistency reviewer; statistical pass 1 (S019-A).
- **Status:** Pending Human Adjudication

## C006 — Postrandomization-exclusion total and group counts do not reconcile across eTable 10 and Figure 1

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** [Supplement 2, eTable 10, PDF p. 24](../../joi240147supp2_prod_1738701765.29201.pdf#page=24), exclusion after randomization; [Main article, Figure 1, PDF p. 3](../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3), excluded after randomization.
- **Printed evidence:** eTable 10 states `N=130` and prints restrictive `55/750 (45)` plus liberal `67/758 (55)`; Figure 1 prints 59 restrictive plus 71 liberal exclusions, totaling 130.
- **Rule and calculation:** eTable 10 group counts sum to `122`, leaving an 8-person gap from its stated 130; Figure 1 counts sum to 130 and exceed each eTable group count by four.
- **Direct observation versus inference:** The totals, group counts, footnote scope, and arithmetic are directly observed. Whether eight Swiss-law consent-withdrawal omissions were intentionally excluded from the table is not stated.
- **Alternative source-grounded interpretations:** eTable 10 may intentionally omit four patients per group while retaining Figure 1's total, but no row label or footnote defines that restriction.
- **Remaining human question:** Does eTable 10 intentionally restrict the 130 exclusions to 122 classified patients, and if so what accounts for the eight and how should the population be labelled?
- **Checker provenance:** numeric consistency reviewer; cross-source consistency reviewer.
- **Status:** Pending Human Adjudication

## C007 — Secondary-exclusion cells pair within-group denominators with cross-group partition percentages

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** [Supplement 2, eTable 10, PDF p. 24](../../joi240147supp2_prod_1738701765.29201.pdf#page=24), secondary exclusion; count comparator [Main article, Figure 1, PDF p. 3](../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3).
- **Printed evidence:** eTable 10 states `N=341` and prints restrictive `174/750 (51)` plus liberal `165/758 (49)`; its footnote says two patients have missing randomized-oxygen data. Figure 1 matches the counts 174 and 165.
- **Rule and calculation:** `174/750 = 23.2%` and `165/758 = 21.8%`, not 51% and 49%. The printed percentages instead partition the 339 classified exclusions: `174/339 = 51.3%` and `165/339 = 48.7%`.
- **Direct observation versus inference:** The counts, denominators, percentages, and footnote are directly observed. The intended estimand is not stated.
- **Alternative source-grounded interpretations:** The table may intend either allocation distribution among 339 classified exclusions or within-group exclusion incidence; the printed cells combine the two denominator concepts.
- **Remaining human question:** Which denominator and estimand should eTable 10 present for secondary exclusions, and how should the two unassigned patients be shown?
- **Checker provenance:** cross-source consistency reviewer.
- **Status:** Pending Human Adjudication

## C008 — Missing-as-event primary count uses a doubled numerator/denominator separator

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** [Supplement 2, eTable 11, PDF p. 25](../../joi240147supp2_prod_1738701765.29201.pdf#page=25), primary outcome with missing counted as event.
- **Printed evidence:** The direct PDF visibly prints restrictive `135//750 (18.0)` under `no./total no. (%)`; the paired liberal cell prints `155/758 (20.4)`.
- **Rule and calculation:** `135/750 = 18.0%`, so the numeric relation reconciles; the doubled slash is inconsistent with the table's count/denominator notation and paired cell.
- **Direct observation versus inference:** The doubled separator is directly observed in the PDF. Its production cause and whether a publication correction is warranted are unknown.
- **Alternative source-grounded interpretations:** The doubled slash may be a typographic artifact that leaves human interpretation intact but can impair machine or manual extraction.
- **Remaining human question:** Is `135//750` present in the authoritative publication rendering, and should the notation be clarified?
- **Checker provenance:** statistical pass 1 (S026-A); numeric reviewer recorded it as a presentation note rather than an arithmetic candidate.
- **Status:** Pending Human Adjudication

## Candidate-set reconciliation

- **Stable candidate count:** 8
- **Merged duplicate observations:** C001 (numeric and cross-source); C002 (numeric and cross-source); C004 (cross-source and statistical); C005 (cross-source and statistical); C006 (numeric and cross-source).
- **Unmerged distinct observations:** C003, C007, and C008 concern different printed values and different consistency rules.
- **Display-zero rule:** No inferential P-value display zero was found, and no candidate is based on display-zero notation.
