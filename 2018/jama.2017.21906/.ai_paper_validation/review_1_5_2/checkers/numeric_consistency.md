# Numeric Consistency Review

## Scope

Reviewed all 53 mapped N relationships: N001--N037 in DOC-001 and N300--N315 in DOC-002--DOC-004. The full record-by-record status, printed inputs, and non-candidate checks are in `relationships/numeric_relationship_inventory.md`. Checks covered arithmetic, totals, subgroup sums, numerator/denominator/percentage relations, missingness, population identity, rounding, units/scales, rate-versus-count labels, repeated values, and directly matched cross-document values.

Rounding rule: for percentages printed to one decimal, the value calculated from the displayed numerator and denominator was accepted when it rounded to that tenth (absolute tolerance 0.05 percentage point before ordinary display rounding). Whole percentages used ordinary nearest-integer rounding. Model-adjusted risk differences, odds ratios, CIs, medians, and quantile-regression coefficients were not required to equal crude displayed differences unless the source stated that identity.

## Results

- Relationships checked: 53
- PASS: 50
- LIMITED by absent exact plotted values or a non-arithmetic planning/toolkit definition: 1 (N315)
- PROVISIONAL CANDIDATE records: 2 (NC-001, NC-002)

### NC-001 — Discharge beta-blocker adjusted point estimates conflict across main-article locations

**Status:** PROVISIONAL CANDIDATE — Pending Human Adjudication

**Category:** Cross-document numeric inconsistency
**Relationship:** N036

**Exact source locations and printed inputs:**

- DOC-001 PDF p.6, Table 2, `Discharge beta-blocker`: control 5,808/8,894 (65.3%), intervention 6,799/10,178 (66.8%), adjusted difference **6.69% (95% CI, 4.43% to 8.95%)**, adjusted OR **1.48 (95% CI, 1.30 to 1.68)**.
- DOC-001 PDF p.7, Results narrative: beta-blocker use `67% vs 65%`; adjusted difference **6.63% (95% CI, 4.43% to 8.95%)**, adjusted OR **1.47 (95% CI, 1.30 to 1.68)**.

**Comparator and reproducible rule:** These are the same explicitly named discharge beta-blocker outcome, intervention-versus-control contrast, and adjusted effect presentation. Exact repeated point estimates should agree unless the source identifies different models, populations, or versions. The printed RD differs by 0.06 percentage point (6.69 versus 6.63), and the OR differs by 0.01 (1.48 versus 1.47), while both CI pairs are identical.

**Tolerance:** Exact-repetition tolerance is zero after matching outcome, contrast, and CI. Ordinary rounding could explain a difference only if the two occurrences state different decimal precision or different underlying analysis; neither is stated at these locations.

**Direct observation versus inference:** Directly observed are the two different printed pairs of point estimates and the identical printed CIs. The inference is only that the occurrences are intended to report the same result, based on the identical named discharge outcome, contrast, and CI endpoints; it does not establish which occurrence is correct.

**Source-grounded alternatives:** The narrative may have been produced from a distinct unlabelled analytic run, or one location may be a transcription/rounding discrepancy. The supplied article does not define a separate discharge-beta-blocker model or population that would account for the difference.

**Quality-control relevance:** A small discordance in a named adjusted effect can lead a structured data extractor to record different effect estimates depending on whether Table 2 or the narrative is used. This is bounded reporting-consistency risk only; no conclusion change is asserted.

**Exact human question:** Do the Table 2 and narrative beta-blocker statements refer to the same adjusted analysis and eligible discharge population; if so, which adjusted RD and OR should be retained?

### NC-002 — eTable 1 footnote labels a comparator not represented by its columns

**Status:** PROVISIONAL CANDIDATE — Pending Human Adjudication

**Category:** Measure, label, or scale inconsistency
**Relationship:** N308

**Exact source locations and printed inputs:**

- DOC-004 (`joi170166supp3_prod.pdf`) PDF p.17, eTable 1 title: `Baseline Characteristics in ACS QUIK Patients by Complete and Missing Follow-up`.
- The two table columns are **Complete Follow Up n=21,079** and **Missing Follow Up n=295**, followed by `Difference (95% CI)`.
- The p.17 footnote `a` states: **`Difference = intervention minus control`**.

**Comparator and reproducible rule:** A difference-definition footnote must name the groups displayed in the columns for that table. The only displayed groups are complete and missing follow-up, whereas intervention and control are absent from eTable 1 and are the groups used in p.18 eTable 2.

**Tolerance:** This is a categorical comparator-label identity check; no numeric rounding tolerance applies.

**Direct observation versus inference:** The title, columns, sample sizes, and footnote are directly printed. The inference is that the footnote is incongruent with this table's displayed contrast; it does not establish the intended subtraction order (missing minus complete or complete minus missing).

**Source-grounded alternatives:** The footnote may have been carried over from eTable 2, where it is consistent with the columns. It could also be a generic wording error. The supplied source lacks a corrected comparator definition for eTable 1.

**Quality-control relevance:** The wrong comparator label can reverse interpretation of the reported numerical differences, including the 3.3-ng/mL initial-troponin contrast cited in the main text. This is a reporting-label consistency issue only; no clinical or study-validity conclusion is asserted.

**Exact human question:** What contrast and subtraction order define the `Difference (95% CI)` column in eTable 1, and should footnote `a` be corrected to name complete and missing follow-up?

## Non-candidate boundaries and limitations

All count/total and percentage checks listed in the inventory reconciled at stated precision. The main article's adjusted effects were kept distinct from crude percentages. Planning figures in DOC-002/DOC-003 and illustrative toolkit numeric content in DOC-004 were not treated as final trial denominators or outcome estimates. eFigures 1A--2B have no exact plotted point labels, so N315 cannot be arithmetically reproduced; the supplied labels do distinguish rates, residuals, and within-hospital differences. No candidate was based on a displayed zero P value; none of the assigned N relationships presents a `P=0` display.
