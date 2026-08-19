# Stable Candidate Ledger

All six distinct candidates below are **Pending Human Adjudication**. Duplicate proposals were merged only when they concerned the same printed values or labels, comparator, and consistency rule. Stable IDs are immutable. No candidate is based solely on a display-zero P value.

## C001 — Figure 1 allocation branches exceed the displayed available cohort by 10 participants

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source location:** `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf`, PDF p. 3, Figure 1 and adjoining Results text.
- **Printed evidence:** Figure 1 states `305 Available for long-term follow-up and randomized`, then branches to `193 Randomized to undergo bariatric surgery` and `122 Randomized to undergo medical/lifestyle intervention`. Enrolled counts are 166 and 96.
- **Rule and calculation:** Mutually exclusive branches of the displayed 305-person parent box should sum to the parent total. `193 + 122 = 315`; `315 - 305 = 10`. Enrolled counts separately reconcile: `166 + 96 = 262`.
- **Direct observation versus inference:** The 10-person printed mismatch is observed. It remains unresolved whether the branch counts refer to a different original-randomization cohort or whether a displayed count/label is incorrect.
- **Source-grounded alternatives:** The 193 and 122 counts may refer to a different population; the parent total may be wrong; one or both branch counts may be wrong.
- **Remaining human question:** Which population do the 193 and 122 branches represent, and which total/count or label should be aligned?
- **Checker provenance:** Numeric consistency proposal NC-04.

## C002 — Supplement eTable 2 mixes year-12 headings with year-7 quantitative footnote definitions

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** `joi240004supp2_prod_1721756962.82552.pdf`, PDF pp. 15-16, eTable 2 title, columns, and footnotes a-c; `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf`, PDF p. 3, the narrative pointer to the 12-year eTable 2 result.
- **Printed evidence:** The title and group columns state `year 12`. Footnotes describe baseline and `year-7 data`, `7-year over baseline` odds ratios, `7-year change`, and odds `at year 7`.
- **Rule and comparison:** A single result table's column timepoint and footnote definition of its changes/comparisons must agree. `year 12` and `year 7` are different estimand labels and cannot be reconciled by rounding.
- **Direct observation versus inference:** The internal label conflict is observed. It is only an inference that the year-7 wording may be copied residual text.
- **Source-grounded alternatives:** The footnotes may be wrong; the title/columns may be wrong; or the table may combine 12-year descriptive values with 7-year modeled comparisons without saying so.
- **Remaining human question:** Which timepoint was used for each eTable 2 descriptive value, change, group comparison, binary odds ratio, and P value?
- **Checker provenance:** Numeric NC-01; cross-source proposal 1; statistical pass-1 P1-01.

## C003 — Matched 12-year HbA1c result has incompatible printed P values

- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf`, PDF pp. 1 and 3; `joi240004supp2_prod_1721756962.82552.pdf`, PDF p. 15, eTable 2 HbA1c row.
- **Printed evidence:** The main article prints the stated 12-year difference as `-1.1%` with 95% CI `-1.7% to -0.5%` and `P = .002`. eTable 2 prints the same displayed difference and interval but `P < .001`.
- **Rule and comparison:** For a matched population, timepoint, contrast, estimate, and interval, repeated P values must match or be explicitly distinguished. `.002 < .001` is false.
- **Direct observation versus inference:** The incompatible displays are observed. A different unreported test, model, variance method, or the C002 timepoint ambiguity is only a possible explanation.
- **Source-grounded alternatives:** Either P value may be the intended value, or the supplement may represent a distinct analysis that is not labeled.
- **Remaining human question:** Do both locations report the same year-12 contrast; if yes, which P value is correct, and if not, what analytic distinction applies?
- **Checker provenance:** Numeric NC-02; cross-source proposal 2; statistical pass-1 P1-02.

## C004 — The same year-7 glycemic outcome is labeled as both HbA1c less than or equal to 6.5% and HbA1c below 6.5%

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf`, PDF p. 4, Results narrative; PDF p. 6, Table 2; `joi240004supp2_prod_1721756962.82552.pdf`, PDF p. 4, supporting analysis definition.
- **Printed evidence:** Narrative: HbA1c `less than or equal to 6.5%` with `P = .002; Table 2`. Table 2: `HbA1c <6.5%, %`, values 17.3% and 37.7%, OR 2.89 (95% CI 1.48-5.64), `P = .002`.
- **Rule and comparison:** `x <= 6.5` includes the boundary value; `x < 6.5` excludes it. The table citation and identical P value identify the same outcome while its operator differs.
- **Direct observation versus inference:** The label conflict is observed. Whether any participant was exactly 6.5% and whether the numeric result changes are unknown.
- **Source-grounded alternatives:** The prose may be imprecise, the table may omit equality, or an undocumented rounding/threshold rule may apply.
- **Remaining human question:** Was this binary outcome computed using `<6.5%` or `<=6.5%`, and which label should be aligned?
- **Checker provenance:** Numeric NC-03; cross-source proposal 4.

## C005 — Abstract percentage for four deaths does not reconcile with displayed group counts and denominators

- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf`, PDF p. 1, Abstract Results; PDF p. 3, enrolled group counts; PDF p. 7, Results death narrative; PDF p. 8, Table 3.
- **Printed evidence:** Abstract: `4 deaths (2.2%), 2 in each group`. Table 3: 2 (2.1%) of 96 medical/lifestyle and 2 (1.2%) of 166 surgery; combined displayed cohort is 262.
- **Rule and calculation:** The displayed counts total four and denominators total 262. `4 / 262 x 100 = 1.5267%`, which rounds to 1.5%, not 2.2%. The within-group percentages separately reconcile.
- **Direct observation versus inference:** The percentage mismatch is observed. A different unstated risk-set denominator is a possible explanation, not an established fact.
- **Source-grounded alternatives:** The abstract may use an unstated denominator near 182; the percentage may be a transcription error; or Table 3 may use a different population that is not distinguished in the abstract.
- **Remaining human question:** What denominator generated 2.2%, and how should the abstract and Table 3 populations or percentage be aligned?
- **Checker provenance:** Cross-source proposal 3.

## C006 — The same exploratory BMI subgroup boundary is labeled as both 35 or greater and greater than 35

- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** `jama_courcoulas_2024_oi_240004_1721756962.76052.pdf`, PDF p. 7, Results narrative defining BMI `27 to <35` versus `35 or greater` and citing eFigure 6; `joi240004supp2_prod_1721756962.82552.pdf`, PDF p. 13, eFigure 6 subgroup labels `BMI <35 kg/m2` and `BMI >35 kg/m2`.
- **Printed evidence:** The main text places BMI exactly 35 in the higher subgroup by stating `35 or greater`; the matched eFigure labels the higher subgroup `>35`, which excludes exactly 35. Both locations describe the same exploratory HbA1c and weight trajectories and year-7 subgroup comparison.
- **Rule and comparison:** A two-part subgroup partition for the same analysis must use complementary boundary operators. `x < 35` is complemented by `x >= 35`, not `x > 35`; the latter leaves `x = 35` unassigned.
- **Direct observation versus inference:** The inconsistent printed operators are observed. Whether any participant had BMI exactly 35 and which condition the analysis code used remain unknown.
- **Source-grounded alternatives:** The eFigure label may have omitted equality; the main narrative may be imprecise; or a separate handling rule for BMI exactly 35 may exist but is not printed.
- **Remaining human question:** Was the higher BMI subgroup computed as `>=35` or `>35`, and which main-text or eFigure label should be aligned?
- **Checker provenance:** Final evidence-quality coverage audit, relationships N041/N081 and S030/S134.
