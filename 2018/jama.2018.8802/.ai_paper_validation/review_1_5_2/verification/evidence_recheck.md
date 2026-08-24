# Mechanical Evidence Recheck

This source-first recheck covers every stable candidate ID `C001` through `C011` separately. Supplied PDFs are the final authority. Fresh native text, coordinate-layout text, and source-page rasters under `preprocessing/` were used only to locate and visually confirm the exact PDF evidence. Every ID remains **Pending Human Adjudication**; no ID is deleted, renumbered, merged, or suppressed here.

## C001 — Table 1 CAD/previous-MI percentage does not reconcile with 311/2400

- **Cited location found:** Yes. DOC-001, [jama_wang_2018_oi_180070.pdf — PDF p. 6](<../../../jama_wang_2018_oi_180070.pdf#page=6>), Table 1, `CAD/previous myocardial infarction`, intervention column. The same table identifies 2400 intervention patients.
- **Source printed value/text matched:** Yes. The direct PDF visibly prints `311 (13.05)`.
- **Comparator matched:** Yes. The intervention column is headed `No. (%)`, and the table prints `Patients, No.` as 2400 for the intervention group.
- **Consistency rule applicable:** Yes, conditional on the group total 2400 being the row denominator: the displayed percentage should equal the displayed count divided by its denominator, subject to the chosen decimal precision.
- **Calculation or logical comparison reproduced:** `311 / 2400 × 100 = 12.958333...%`; nearest rounding gives `13.0%` at one decimal or `12.96%` at two decimals, not `13.05%`.
- **Necessary inputs available:** The printed count, group total, percentage, column identity, and table precision are available.
- **Exact missing inputs or definitions:** The package does not state a CAD-row-specific denominator, CAD-row missingness count, or a nonstandard percentage convention. An integer denominator of 2383 or 2384 could round `311/n × 100` to `13.05%`, but neither denominator is printed for this row.
- **Source-grounded alternative interpretation:** The 2400 may be the group total while an unstated smaller nonmissing denominator was used for this characteristic; alternatively, one of the three printed quantities may reflect a production transcription. The supplied table gives no row-level denominator that distinguishes these interpretations.
- **Direct observation:** `311`, `13.05`, and the intervention total `2400` are visibly printed in Table 1.
- **Inferred explanation:** A hidden nonmissing denominator or a production transcription is an explanation, not a direct source statement.
- **Exact remaining human question:** Was 2400 the denominator used for the CAD/previous-MI percentage; if not, what exact row denominator or missingness count produced `13.05`?
- **Adjudication state:** Pending Human Adjudication.

## C002 — LDL eligibility threshold is printed as both >100 and ≥100 mg/dL

- **Cited location found:** Yes. DOC-001, [PDF p. 3](<../../../jama_wang_2018_oi_180070.pdf#page=3>) Outcomes and [PDF p. 7](<../../../jama_wang_2018_oi_180070.pdf#page=7>) Table 2; DOC-002, [joi180070supp1_prod.pdf — PDF p. 14](<../../../joi180070supp1_prod.pdf#page=14>) Table 2 and [PDF p. 15](<../../../joi180070supp1_prod.pdf#page=15>) Table 3 continuation; DOC-003, [joi180070supp2_prod.pdf — PDF p. 3](<../../../joi180070supp2_prod.pdf#page=3>) eTable 1.
- **Source printed value/text matched:** Yes. DOC-001 p. 3 says LDL `more than 100 mg/dL` or undocumented, and DOC-001 p. 7 labels the row `LDL >100 mg/dL`.
- **Comparator matched:** Yes. DOC-002 p. 14 prints `LDL ≥ 100 mg/dL`; DOC-002 p. 15 and DOC-003 p. 3 also print `LDL ≥ 100 mg/dL` and add prior lipid-lowering treatment and undocumented LDL as eligibility routes.
- **Consistency rule applicable:** Yes. For a value exactly equal to 100 mg/dL, the predicate `LDL > 100` is false while `LDL ≥ 100` is true; therefore the printed boundary definitions are not set-equivalent.
- **Calculation or logical comparison reproduced:** At `LDL = 100 mg/dL`: `100 > 100` is false and `100 ≥ 100` is true. The definitions can therefore select different patients and denominators.
- **Necessary inputs available:** The exact inequality signs, unit, measure label, and additional eligibility text are available.
- **Exact missing inputs or definitions:** The package does not identify which boundary was implemented in the analysis dataset, how many patients had LDL exactly 100 mg/dL, or whether the abbreviated article row label was intended to incorporate every prior-treatment and undocumented-LDL route in the detailed definition.
- **Source-grounded alternative interpretation:** The main article may use `>100` as a shortened label for the detailed specification cited in Supplement 2 rather than as executable eligibility logic.
- **Direct observation:** The supplied documents visibly use different inequality signs and the detailed sources list additional eligibility conditions.
- **Inferred explanation:** Treating the main wording as shorthand is interpretive; the package does not explicitly say that `>` means `≥`.
- **Exact remaining human question:** Which boundary and complete set of eligibility routes were applied to construct the lipid-lowering denominators and results in the article tables?
- **Adjudication state:** Pending Human Adjudication.

## C003 — Exact 20-patients-per-cluster statement conflicts with the 801 baseline total

- **Cited location found:** Yes. DOC-003, [joi180070supp2_prod.pdf — PDF p. 2](<../../../joi180070supp2_prod.pdf#page=2>) eAppendix; DOC-001, [jama_wang_2018_oi_180070.pdf — PDF p. 3](<../../../jama_wang_2018_oi_180070.pdf#page=3>) and [PDF p. 6](<../../../jama_wang_2018_oi_180070.pdf#page=6>) Table 1.
- **Source printed value/text matched:** Yes. DOC-003 p. 2 visibly says `(20 patients per cluster were prospectively included in this phase)`.
- **Comparator matched:** Yes. DOC-001 states that 40 hospitals were included, and Table 1 prints 40 baseline-survey hospitals and `Patients, No.` of 801 in the baseline-survey column.
- **Consistency rule applicable:** Yes, if `20 patients per cluster` is an exact count for each of the 40 baseline clusters: equal per-cluster counts must sum to the reported total.
- **Calculation or logical comparison reproduced:** `20 × 40 = 800`, whereas Table 1 prints 801, a difference of one patient.
- **Necessary inputs available:** The per-cluster count, number of baseline hospitals/clusters, and baseline patient total are available.
- **Exact missing inputs or definitions:** Cluster-specific baseline counts, whether `20` was a target rather than an achieved exact count, and whether all 40 Table 1 hospitals correspond one-for-one to the clusters described in the eAppendix are not supplied.
- **Source-grounded alternative interpretation:** One cluster may have included 21 patients, or `20 patients per cluster` may describe the recruitment target. Neither qualification appears in the printed eAppendix sentence.
- **Direct observation:** The source prints `20 patients per cluster`, 40 baseline-survey hospitals, and 801 baseline-survey patients.
- **Inferred explanation:** An extra patient in one cluster, a target-based reading, or a cluster-set difference is inferred because no cluster-level listing is supplied.
- **Exact remaining human question:** Did every baseline cluster contribute exactly 20 patients, and, if so, what supplied count or cluster definition accounts for the 801st baseline patient?
- **Adjudication state:** Pending Human Adjudication.

## C004 — eTable 4 rtPA control percentage does not reconcile with 23/238

- **Cited location found:** Yes. DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../../../joi180070supp2_prod.pdf#page=8>), eTable 4, `IV rt-PA 2 Hour`, control column.
- **Source printed value/text matched:** The candidate-ledger transcription does not match the direct PDF. The PDF visibly prints `23/238 (9.66)`, not `23/238 (9.6)`.
- **Comparator matched:** Yes. The count and denominator visibly print as `23/238`; the displayed percentage visibly has two decimal places, `9.66`.
- **Consistency rule applicable:** The count/denominator percentage rule applies, but it must be applied at the two-decimal precision actually printed in this cell rather than the one-decimal value recorded in the ledger.
- **Calculation or logical comparison reproduced:** `23 / 238 × 100 = 9.663865...%`, which rounds to `9.66%` at two decimals. The paired intervention cell prints `46/254 (18.11)`, and `46 / 254 × 100 = 18.110236...%`, also matching two-decimal nearest rounding.
- **Necessary inputs available:** The exact visible count, denominator, percentage, and a same-row paired cell demonstrating two-decimal display are available.
- **Exact missing inputs or definitions:** No mathematical input is needed to reproduce `9.66`. The package does not state whether this row-specific two-decimal display was intentional or whether the repeated final digits are a production-formatting artifact.
- **Source-grounded alternative interpretation:** Both rtPA cells on this row use two decimals and reconcile under nearest rounding, supporting a row-specific precision interpretation.
- **Direct observation:** Direct source-page rendering visibly shows `46/254 (18.11)` and `23/238 (9.66)`.
- **Inferred explanation:** Intentional row-specific precision or a production duplication of the final digit are possible explanations; neither is stated by the source.
- **Exact remaining human question:** Should the rtPA row be read and adjudicated using its visibly printed two-decimal values `18.11` and `9.66`, and was that row-specific precision intentional?
- **Adjudication state:** Pending Human Adjudication.

## C005 — eTable 4 discharge-antithrombotics control percentage does not reconcile with 2141/2400

- **Cited location found:** Yes. DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../../../joi180070supp2_prod.pdf#page=8>), eTable 4, `Antithrombotics` under performance measures at discharge, control column.
- **Source printed value/text matched:** Yes. The direct PDF visibly prints `2141/2400 (89.3)`.
- **Comparator matched:** Yes. Count 2141, denominator 2400, and percentage 89.3 are in the same control cell.
- **Consistency rule applicable:** Yes. A displayed numerator/denominator percentage should reconcile under the table's one-decimal display convention.
- **Calculation or logical comparison reproduced:** `2141 / 2400 × 100 = 89.208333...%`, which rounds to `89.2%`, not `89.3%`, at one decimal.
- **Necessary inputs available:** The printed numerator, denominator, percentage, and one-decimal precision are available.
- **Exact missing inputs or definitions:** No alternate denominator or explicit non-nearest rounding rule is supplied.
- **Source-grounded alternative interpretation:** The cell could reflect an unprinted underlying denominator or a value carried from a different analysis version, but no supplied table note identifies either.
- **Direct observation:** `2141/2400 (89.3)` is visibly printed in one cell.
- **Inferred explanation:** A hidden denominator, alternate rounding convention, or production transcription is inferred rather than stated.
- **Exact remaining human question:** Which of the displayed count, denominator, or percentage was used to generate this control-cell result, and what rounding rule was applied?
- **Adjudication state:** Pending Human Adjudication.

## C006 — eTable 4 AF-anticoagulation control percentage does not reconcile with 39/174

- **Cited location found:** Yes. DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../../../joi180070supp2_prod.pdf#page=8>), eTable 4, `Anticoagulation for Atrial Fibrillation`, control column.
- **Source printed value/text matched:** Yes. The direct PDF visibly prints `39/174 (22.5)`.
- **Comparator matched:** Yes. Count 39, denominator 174, and percentage 22.5 are in the same control cell.
- **Consistency rule applicable:** Yes. The displayed percentage should equal the displayed numerator divided by the displayed denominator at one decimal.
- **Calculation or logical comparison reproduced:** `39 / 174 × 100 = 22.413793...%`, which rounds to `22.4%`, not `22.5%`.
- **Necessary inputs available:** The printed numerator, denominator, percentage, and precision are available.
- **Exact missing inputs or definitions:** The package supplies no alternate denominator or non-nearest rounding convention for this cell.
- **Source-grounded alternative interpretation:** A different unprinted eligible denominator or a value from a different table version could yield the percentage, but neither is documented in the supplied package.
- **Direct observation:** `39/174 (22.5)` is visibly printed in one cell.
- **Inferred explanation:** Any hidden denominator or production mechanism is inferred.
- **Exact remaining human question:** Which exact numerator, eligible denominator, and percentage were intended to describe control-group anticoagulation adherence in this eTable 4 row?
- **Adjudication state:** Pending Human Adjudication.

## C007 — eTable 4 lipid-lowering control percentage does not reconcile with 1439/1586

- **Cited location found:** Yes. DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../../../joi180070supp2_prod.pdf#page=8>), eTable 4, `Lipid-lowering for LDL >100 mg/dL`, control column.
- **Source printed value/text matched:** Yes. The direct PDF visibly prints `1439/1586 (90.8)`.
- **Comparator matched:** Yes. Count 1439, denominator 1586, and percentage 90.8 are in the same control cell.
- **Consistency rule applicable:** Yes. The displayed percentage should reconcile with its displayed numerator and denominator at one decimal.
- **Calculation or logical comparison reproduced:** `1439 / 1586 × 100 = 90.731399...%`, which rounds to `90.7%`, not `90.8%`.
- **Necessary inputs available:** The printed numerator, denominator, percentage, and precision are available.
- **Exact missing inputs or definitions:** No alternate denominator or non-nearest rounding rule is supplied. The `>` versus `≥` eligibility-definition issue is recorded separately as C002 and does not, by itself, reconcile this displayed cell.
- **Source-grounded alternative interpretation:** An unprinted denominator or a value carried from a different eligibility implementation could explain the percentage, but the package does not identify one for this cell.
- **Direct observation:** `1439/1586 (90.8)` is visibly printed in one cell.
- **Inferred explanation:** Linking the mismatch to an eligibility implementation or production version is inferential.
- **Exact remaining human question:** Which exact count, eligible denominator, and percentage were used for this control lipid-lowering sensitivity-analysis cell?
- **Adjudication state:** Pending Human Adjudication.

## C008 — eTable 4 antidiabetic-medication control percentage does not reconcile with 557/688

- **Cited location found:** Yes. DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../../../joi180070supp2_prod.pdf#page=8>), eTable 4, `Antidiabetic Medication`, control column.
- **Source printed value/text matched:** Yes. The direct PDF visibly prints `557/688 (81.1)`.
- **Comparator matched:** Yes. Count 557, denominator 688, and percentage 81.1 are in the same control cell.
- **Consistency rule applicable:** Yes. The displayed percentage should reconcile with its displayed numerator and denominator at one decimal.
- **Calculation or logical comparison reproduced:** `557 / 688 × 100 = 80.959302...%`, which rounds to `81.0%`, not `81.1%`.
- **Necessary inputs available:** The printed numerator, denominator, percentage, and precision are available.
- **Exact missing inputs or definitions:** No alternate denominator or non-nearest rounding rule is supplied.
- **Source-grounded alternative interpretation:** An unprinted eligible denominator or a value from a different analysis version could explain the cell, but no such version or denominator is supplied.
- **Direct observation:** `557/688 (81.1)` is visibly printed in one cell.
- **Inferred explanation:** A hidden denominator or production transcription is inferred.
- **Exact remaining human question:** Which of `557`, `688`, and `81.1%` corresponds to the analysis value intended for this control row, and under what rounding rule?
- **Adjudication state:** Pending Human Adjudication.

## C009 — In-hospital-death absolute-difference P value conflicts with its displayed 95% CI

- **Cited location found:** Yes. DOC-001, [jama_wang_2018_oi_180070.pdf — PDF p. 8](<../../../jama_wang_2018_oi_180070.pdf#page=8>), Table 3, `Death` → `In hospital` row.
- **Source printed value/text matched:** Yes. The direct PDF visibly prints adjusted absolute difference `−0.7` and `95% CI, −1.1 to 0.2`. The upper endpoint is an unsigned positive `0.2`, not `−0.2`.
- **Comparator matched:** Yes. The adjacent absolute-difference P-value column visibly prints `.009`. The separately headed hazard-ratio block prints `0.96 (0.90 to 1.02)` with its own P value `.14`; that `.14` is not the absolute-difference P-value cell.
- **Consistency rule applicable:** The article states that all tests were two-sided and that P below .05 was considered statistically significant. Under a compatible two-sided test/95% CI pair for the same null, a CI containing 0 and P below .05 do not give the same null-boundary decision. Exact numerical inversion additionally requires the same estimator, variance method, degrees of freedom, and CI/test construction.
- **Calculation or logical comparison reproduced:** The interval `[−1.1, 0.2]` contains 0, while `.009 < .05`. As a diagnostic only, the endpoint midpoint is `(−1.1 + 0.2)/2 = −0.45`, half-width is `0.65`, and a symmetric normal 95% approximation gives `SE ≈ 0.65/1.96 = 0.3316`; this rough construction does not reproduce `.009` and is not a replacement analysis.
- **Necessary inputs available:** The point estimate, confidence level, endpoints, P value, column headings, and the article's two-sided-test statement are available.
- **Exact missing inputs or definitions:** The exact estimator for the absolute difference, covariance/standard error, CI construction, test statistic, reference distribution or degrees of freedom, and an explicit statement that the displayed CI and P value invert the same test are not supplied. The package also does not state whether `.009` was shifted from another result during table production.
- **Source-grounded alternative interpretation:** The CI and P value might derive from different adjusted procedures or non-inverting methods, or `.009` might be a table-placement value. The source supplies no named special procedure that establishes one of these readings.
- **Direct observation:** The source visibly pairs `−0.7 (−1.1 to 0.2)` with `.009` in the absolute-difference columns; the CI crosses 0.
- **Inferred explanation:** Any different-test, non-Wald, or table-placement explanation is inferred because the required method mapping is absent.
- **Exact remaining human question:** Does `.009` test the same adjusted absolute-difference null represented by the printed `95% CI, −1.1 to 0.2`; if so, what exact estimator, variance, and interval/test rule reconciles them?
- **Adjudication state:** Pending Human Adjudication.

## C010 — Composite adherence has conflicting patient-level and care-opportunity analysis descriptions

- **Cited location found:** Yes. DOC-001, [jama_wang_2018_oi_180070.pdf — PDF p. 3](<../../../jama_wang_2018_oi_180070.pdf#page=3>) Outcomes, [PDF p. 4](<../../../jama_wang_2018_oi_180070.pdf#page=4>) Data Analysis, and [PDF p. 7](<../../../jama_wang_2018_oi_180070.pdf#page=7>) Table 2; DOC-002, [joi180070supp1_prod.pdf — PDF p. 18](<../../../joi180070supp1_prod.pdf#page=18>) and [PDF p. 19](<../../../joi180070supp1_prod.pdf#page=19>); DOC-003, [joi180070supp2_prod.pdf — PDF p. 2](<../../../joi180070supp2_prod.pdf#page=2>) eAppendix.
- **Source printed value/text matched:** Yes. DOC-001 p. 3 defines a patient ratio and says it was calculated for each patient and then averaged. Table 2 labels `Composite measure, mean (SD)` and prints `88.2 (15.1)` and `84.8 (18.2)`.
- **Comparator matched:** Yes. DOC-001 p. 4 and DOC-002 pp. 18-19 say each eligible care opportunity contributed a binary observation for analysis and identify a population-average odds ratio. DOC-003 p. 2 defines the baseline-survey composite as total interventions performed among eligible patients divided by total possible interventions among eligible patients.
- **Consistency rule applicable:** A mean of patient-specific ratios, `mean_i(performed_i/eligible_i)`, weights patients equally; a pooled opportunity proportion, `sum_i(performed_i)/sum_i(eligible_i)`, weights patients by their eligible-opportunity counts. They are generally different estimands unless every patient has the same eligible count or the ratios align in a way that makes the weighting irrelevant. However, the article explicitly distinguishes a descriptive mean from an opportunity-level ORPA, so same-estimand matching cannot be assumed for every Table 2 column.
- **Calculation or logical comparison reproduced:** The two formulas above are algebraically nonidentical when eligible counts vary. The source's example of one patient eligible for 5 measures and meeting 3 gives 5 binary opportunity observations, three coded 1 and two coded 0; for that one patient both representations equal `3/5`, but aggregation across patients can differ because the weights differ.
- **Necessary inputs available:** The patient-level descriptive definition, care-opportunity model description, pooled baseline definition, Table 2 labels, group means, adjusted difference, and ORPA are available.
- **Exact missing inputs or definitions:** The package does not state the exact estimator and analysis unit used for Table 2's adjusted absolute difference `3.5 (0.7 to 6.4)`, does not map each displayed composite column to a formula in one place, and does not provide patient-level eligible-opportunity counts needed to reproduce the two aggregations.
- **Source-grounded alternative interpretation:** The `88.2%`/`84.8%` mean (SD) values may intentionally be equal-weight patient summaries, while ORPA intentionally comes from opportunity-level binary observations; the pooled baseline-survey definition may apply only to that baseline appendix summary. Under this reading, different units serve separately labeled descriptive and inferential outputs rather than one common numerical estimand.
- **Direct observation:** The sources print all three descriptions and Table 2 separately labels mean (SD), adjusted absolute difference, and ORPA.
- **Inferred explanation:** Whether these are intentionally distinct estimands and which method generated the adjusted difference cannot be determined from the supplied formula mapping.
- **Exact remaining human question:** Were the `88.2%`/`84.8%` values intentionally patient-level means and the ORPA intentionally opportunity-level, and which exact unit, weights, and estimator generated the adjusted absolute difference `3.5`?
- **Adjudication state:** Pending Human Adjudication.

## C011 — DVT-prophylaxis window is labeled as both within 48 hours and by end of hospital day 2

- **Cited location found:** Yes. DOC-002, [joi180070supp1_prod.pdf — PDF p. 13](<../../../joi180070supp1_prod.pdf#page=13>) protocol Table 2, [PDF p. 14](<../../../joi180070supp1_prod.pdf#page=14>) Table 3, and [PDF p. 15](<../../../joi180070supp1_prod.pdf#page=15>) its DVT-definition continuation; DOC-003, [joi180070supp2_prod.pdf — PDF p. 3](<../../../joi180070supp2_prod.pdf#page=3>) eTable 1; DOC-001, [jama_wang_2018_oi_180070.pdf — PDF p. 7](<../../../jama_wang_2018_oi_180070.pdf#page=7>) Table 2 footnote e.
- **Source printed value/text matched:** Yes. DOC-002 p. 13 visibly defines DVT prophylaxis as `within 48 hours of admission`.
- **Comparator matched:** Yes. DOC-002 pp. 14-15, DOC-003 p. 3, and DOC-001 p. 7 visibly use `by end of hospital day two` or `by end of hospital day 2` for DVT prophylaxis.
- **Consistency rule applicable:** The two timing predicates are equivalent only if `hospital day 2` is operationally defined as the first 48 elapsed hours after admission. Under an ordinary calendar-hospital-day interpretation, the elapsed duration to the end of day 2 depends on admission time and need not equal 48 hours.
- **Calculation or logical comparison reproduced:** For an admission late on calendar day 1, the end of calendar hospital day 2 can occur substantially earlier than 48 elapsed hours; therefore an event can satisfy `within 48 hours` but fail `by end of hospital day 2`. This is a logical boundary comparison, not a claim about the trial's unstated implementation.
- **Necessary inputs available:** Both printed timing labels, the admission anchor in the 48-hour wording, and the displayed Table 2 DVT counts/denominators `178/645` and `66/592` are available.
- **Exact missing inputs or definitions:** The package does not define when a hospital day begins or ends, whether hospital day 2 was implemented as an elapsed-hour window, the timestamp inclusion rule at the boundary, or which operational predicate constructed the displayed DVT denominators.
- **Source-grounded alternative interpretation:** `Hospital day 2` may have been a label for the same 48-hour abstraction used in protocol Table 2. No supplied definition explicitly equates them.
- **Direct observation:** The supplied documents visibly use both timing phrases for the DVT measure.
- **Inferred explanation:** Treating hospital day 2 as either a calendar boundary or an elapsed 48-hour window is inferential until the operational definition is supplied.
- **Exact remaining human question:** Which timestamp rule was applied to generate the DVT-prophylaxis eligibility and adherence values `178/645` and `66/592`, and did `hospital day 2` mean 48 elapsed hours after admission?
- **Adjudication state:** Pending Human Adjudication.

## Recheck completion

- **Stable IDs covered:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011.
- **Stable ID count:** 11.
- **Direct-source limitation requiring attention:** C004's ledger transcription `9.6` is not the visible PDF value; the supplied PDF prints `9.66`, which reconciles with `23/238` at two decimals. The ID is preserved for human adjudication.
- **Other exact glyph checks:** C001 visibly prints `13.05`; C005-C008 visibly print `89.3`, `22.5`, `90.8`, and `81.1`; C009's CI upper endpoint is visibly positive `0.2`, and its absolute-difference P-value cell is visibly `.009`.
- **Overall adjudication state:** Pending Human Adjudication for every stable ID.
