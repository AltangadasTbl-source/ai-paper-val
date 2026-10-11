# Statistical relationship inventory — support-003

**Scope:** DOC-002 PDF pp. 101-134 and DOC-003 PDF pp. 1-3. Each record is mapped for later independent statistical pass review; no candidate ID, conclusion, or adjudication is assigned here.

| ID | Exact source location(s) | Statistical relationship and supplied definition | Pass-1 coverage note |
|---|---|---|---|
| S3S001 | DOC-002 pp. 119-121, 128-130 (OCR duplicate) | Trial is multicentre, prospective, open, randomized, non-inferiority. Primary BVM-versus-TI aim: day-28 survival with favourable neurological function. H0: pi(BVM)-pi(TI) <= -0.01; H1: pi(BVM)-pi(TI) >= -0.01. | Assess only against matched result population/contrast. Current native SAP text on p. 121 controls over OCR character errors in duplicate p. 130. |
| S3S002 | DOC-002 p. 120; p. 129 OCR duplicate | Sample-size plan: BVM 3%, TI 2%, margin 1%, 956/group, 0.8 power, type-I error 0.025, total 2,000, 5,000 Newcombe-Wilson simulations. | Planning relationship, not a reported outcome. Retain the distinction between design alpha 0.025 and later all-tests alpha 0.05. |
| S3S003 | DOC-002 pp. 121, 123-124; pp. 130, 132-133 OCR duplicates | ITT, PP, and AT populations are defined; ITT missing primary endpoint=no success; no secondary imputation; sensitivity/multiple imputation is conditional on large PP/ITT difference. | Before a comparison, match analysis set and missing-data rule. |
| S3S004 | DOC-002 pp. 122, 131 OCR duplicate | Primary parameter: day-28 survival with favourable neurological function, CPC <=2. Secondary parameters: hospital-admission/day-28 survival, ROSC rate, and IDS for intubated patients. | Preserves outcome/timepoint/scale for exact cross-source matching. |
| S3S005 | DOC-002 pp. 123, 132 OCR duplicate | Continuous: n, mean, SD, extrema, quartiles, two-sided 95% CI; values presented to one additional decimal. Categorical: non-missing denominator=100%, one-decimal percentage rounding; totals may differ from 100% by rounding. | Apply stated rounding/denominator rule where a matching SAP-governed table is evaluated. |
| S3S006 | DOC-002 p. 124; p. 133 OCR duplicate | Primary non-inferiority: two-sided 95% CI for pi(BVM)-pi(tracheal); accept non-inferiority if lower limit > -0.01; exact rather than asymptotic CI if necessary; ITT/PP/AT. | Check point estimate/CI/direction only when an exact matched primary result supplies the same population and measure. |
| S3S007 | DOC-002 p. 124; p. 133 OCR duplicate | Secondary rate criteria: chi-square on proportions; 95% CI for OR and differences. Quantitative criteria: t test or Mann-Whitney by distribution. Tests two-tailed, type-I error 0.05, P<0.05 significant; SAS 9.4. Safety dichotomies: chi-square or Fisher exact, 95% OR CI. | Methods are alternative/conditional; do not infer which was used in an individual result without a source statement. |
| S3S008 | DOC-003 p. 2 | eTable 1 centre contributions: BMV N=1018 and ETI N=1022; all 21 centre counts and percentages. | Check counts against denominators and one-decimal percentage rounding; this table has no inferential statistic. |
| S3S009 | DOC-003 p. 3, ECMO/uncontrolled-donation exclusion row | BMV 43/971 (4.4%) versus ETI 39/978 (4.0%); P=0.63; BMV%-ETI%=0.4; 95% CI [-2.2, 1.3]. Footnote says chi-square or Fisher exact, without row-specific selection. | Check count/percentage/difference/CI containment with the printed post-hoc denominators; test assignment and CI method are unspecified. |
| S3S010 | DOC-003 p. 3, post-BMV-before-ROSC reclassification row | BMV 41/863 (4.8%) versus ETI 45/1174 (3.8%); P=0.31; BMV%-ETI%=0.9; 95% CI [-0.9, 2.7]. Footnote says chi-square or Fisher exact, without row-specific selection. | Check count/percentage/difference/CI containment with the printed reclassified denominators; test assignment and CI method are unspecified. |

## Explicit coverage status

- **S3S001-S3S010: PASS_1_COMPLETE mapping status.** Each relationship has a source location, population/contrast or definition where supplied, and any missing test-specific input identified above.
- No source page in this shard displays `P = 0` or an equivalent display zero.
- DOC-002 p. 134 is empty in both current-run text modes and has no authorized OCR; it supplies no statistical relationship.
