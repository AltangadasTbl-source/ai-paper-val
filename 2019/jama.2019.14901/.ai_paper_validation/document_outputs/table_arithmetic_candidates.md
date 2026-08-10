# Result-relevant table arithmetic check

**Scope.** DOC-001-main-article, `jama_thille_2019_oi_190108.pdf`, PDF pp. 1-9; and DOC-003-results-supplement, `joi190108supp2_prod.pdf`, PDF pp. 1-9. Only manifest-designated result-relevant tables were inspected. Protocol and administrative documents were not inspected.

**Method.** Checked displayed numerators, denominators, rounded percentages, row/column totals, subgroup aggregation, repeated outcome values, and directly repeated main-article/supplement comparisons. Percentages were considered consistent when the displayed integer percentage equals the count divided by the displayed denominator rounded to the nearest whole percent.

## Candidate issues (1)

### TC-01 — Discordant P values for the same displayed postextubation-respiratory-failure comparison

- **Category:** Presentation inconsistency / cross-document inconsistency
- **Severity:** Minor (candidate; requires verification of the analysis output or editorial source table)
- **Exact locations:**
  - **DOC-001-main-article** (`jama_thille_2019_oi_190108.pdf`), PDF p. 8 / printed p. 1472, **Table 2**, *Secondary Outcomes* row “Postextubation respiratory failure at day 7.”
  - **DOC-003-results-supplement** (`joi190108supp2_prod.pdf`), PDF p. 2, **eTable 1**, first data row “Post-extubation respiratory failure at day 7, No. (%).”
- **Verbatim displayed source values:** Both tables report HFNO alone **88/302 (29%)** and HFNO with NIV **70/339 (21%)**. Table 2 reports absolute difference **−8.5% (95% CI, −15.2 to −1.8)** and **P = .01**. eTable 1 reports **P = .02** for its identically labelled comparison.
- **Reproducible calculation:**
  - HFNO alone: \(88 / 302 \times 100 = 29.14\%\), displayed as 29%.
  - HFNO with NIV: \(70 / 339 \times 100 = 20.65\%\), displayed as 21%.
  - Direct displayed-count risk difference: \(20.65\% - 29.14\% = -8.49\) percentage points, which rounds to the Table 2 value **−8.5** percentage points.
  - Thus the event counts, denominators, percentages, and effect-size display describe the same comparison; the P-value displays conflict (**.01** vs **.02**).
- **Reasoning and bounded impact:** The inconsistency is directly observable and does not establish that either P value is incorrect: different stated or unstated test procedures could yield different values. It affects only the reported numerical P value for this secondary outcome; both displayed P values remain below .05.
- **Human verification steps:**
  1. Locate the statistical-analysis output and the production source for Table 2 and eTable 1 for the 88/302 vs 70/339 comparison.
  2. Confirm whether the two tables intentionally used different test procedures (for example, an uncorrected versus continuity-corrected test) and whether that distinction was specified.
  3. If the same procedure was intended, recompute the P value from the analysis dataset and correct whichever table does not match the prespecified analysis.

## Checks with no candidate issue

- **DOC-001 Table 1 (PDF pp. 5-6):** displayed mutually exclusive main-intubation-reason and weaning-difficulty rows sum to their displayed arm denominators; checked denominators and percentages are compatible with whole-number rounding.
- **DOC-001 Table 2 (PDF p. 8):** all displayed No. (%) values are compatible with n=302 or n=339; the mortality-or-reintubation rows reconcile with the component counts and displayed mortality-among-reintubated numerators (HFNO: 26 + 59 − 21 = 64; HFNO+NIV: 21 + 41 − 11 = 51).
- **DOC-003 eTable 1 (PDF p. 2):** all displayed No. (%) values are compatible with n=302 or n=339. Component criteria/reasons are not treated as mutually exclusive totals.
- **DOC-003 eTable 2 (PDF pp. 3-5):** PaCO2 subgroup counts sum to the main arm totals (254 + 48 = 302; 276 + 63 = 339); mutually exclusive intubation-reason and weaning-difficulty rows reconcile within each subgroup.
- **DOC-003 eTables 3-4 (PDF pp. 6-7):** subgroup outcome counts aggregate to DOC-001 Table 2 for each count-based shared outcome; e.g., day-7 reintubation: 10 + 45 = 55 and 5 + 35 = 40; postextubation respiratory failure: 24 + 64 = 88 and 14 + 56 = 70. Their displayed percentages and absolute differences are compatible with the displayed counts/denominators within rounding.
- **DOC-003 eTable 5 (PDF p. 8):** center-level event counts and denominators reconcile with the displayed Total row (95/641; 55/302; 40/339); each center's overall numerator/denominator equals the sum of its two arm-specific values, and percentages are compatible with whole-number rounding.

**Result:** 1 document-verifiable candidate issue; no other local candidate was identified from the permitted result-relevant tables.
