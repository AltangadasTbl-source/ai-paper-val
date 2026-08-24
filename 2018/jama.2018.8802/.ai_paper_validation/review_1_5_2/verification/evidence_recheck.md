# Mechanical Evidence Recheck

This artifact records a separate source-first mechanical recheck for every stable candidate ID in `candidate_ledger.md`. The supplied PDFs are the authority. Fresh native/layout text and rendered pages were used only as locators and visual aids. No source was modified, no old audit derivative or disposition was used, and every ID remains **Pending Human Adjudication**.

## C001 — Table 1 CAD/previous-myocardial-infarction percentage does not reproduce

- **Cited location found:** Yes. DOC-001, [`jama_wang_2018_oi_180070.pdf` — PDF p. 6](../../../jama_wang_2018_oi_180070.pdf#page=6), Table 1, `Patients, No.` row and `CAD/previous myocardial infarction` row, intervention column.
- **Source printed value/text matched:** Yes. The intervention cell prints `311 (13.05)`.
- **Comparator printed value/text matched:** Yes. The same intervention column prints `2400` in the `Patients, No.` row.
- **Consistency rule applicable:** Yes. Table 1 labels categorical cells as `No. (%)`; therefore the parenthetical percentage should reproduce from the displayed count and applicable displayed total at its stated precision.
- **Calculation or logical comparison reproduced:** Yes. `311 / 2400 × 100 = 12.9583333333%`. This rounds to `12.96%` at two decimal places, not `13.05%`.
- **Necessary inputs available:** Partial. The printed count, whole-column patient total, and percentage are available. Missing: any row-specific denominator different from 2,400 and any nonstandard calculation or rounding rule.
- **Source-grounded alternative interpretation:** The table gives 2,400 as the whole intervention-column patient total but does not repeat a denominator in the CAD row. A row-specific denominator could make the printed percentage arithmetically possible, but no such denominator or exclusion is printed for that row.
- **Direct observation:** The direct PDF prints `2400` for intervention patients and `311 (13.05)` for intervention CAD/previous myocardial infarction.
- **Inferred explanation:** A typographic error or an unprinted row-specific denominator could explain the mismatch; neither explanation is established by the supplied source.
- **Exact remaining human question:** Was 2,400 the intended denominator for this row, and if so which element of `311 (13.05)` should have been printed differently?
- **Status:** Pending Human Adjudication

## C002 — LDL eligibility boundary differs between result labels and supplied measure definition

- **Cited location found:** Yes. DOC-001, [`jama_wang_2018_oi_180070.pdf` — PDF p. 7](../../../jama_wang_2018_oi_180070.pdf#page=7), Table 2 lipid-lowering row; DOC-002, [`joi180070supp1_prod.pdf` — PDF p. 15](../../../joi180070supp1_prod.pdf#page=15), discharge performance-measure definition; DOC-003, [`joi180070supp2_prod.pdf` — PDF p. 3](../../../joi180070supp2_prod.pdf#page=3), eTable 1 LDL definition, and [`joi180070supp2_prod.pdf` — PDF p. 8](../../../joi180070supp2_prod.pdf#page=8), eTable 4 lipid-lowering row.
- **Source printed value/text matched:** Yes. The two result labels print `Lipid-lowering for LDL >100 mg/dL`.
- **Comparator printed value/text matched:** Yes. DOC-002 p. 15 prints `LDL ≥ 100 mg/dL`; DOC-003 p. 3 prints `Low-density lipoprotein (LDL) ≥100 mg/dL`.
- **Consistency rule applicable:** Yes. A strict and an inclusive eligibility boundary define different populations when a patient value equals 100 mg/dL.
- **Calculation or logical comparison reproduced:** Yes. `LDL > 100 mg/dL` excludes an LDL value exactly equal to 100 mg/dL, whereas `LDL ≥ 100 mg/dL` includes it; therefore `>100` and `≥100` are not logically equivalent boundaries.
- **Necessary inputs available:** Partial. All four printed symbols and their measure context are available, which is sufficient for the boundary comparison. Missing: the count of patients with LDL exactly 100 mg/dL, the operational eligibility code, and an explicit statement that the formal definition rather than the abbreviated row label governed each reported denominator.
- **Source-grounded alternative interpretation:** The result-row text may be an abbreviated display while the formal `≥100 mg/dL` definition controlled eligibility. The package presents the formal definition twice, but it does not explicitly identify the `>100 mg/dL` row wording as an abbreviation.
- **Direct observation:** The direct PDFs print `>100 mg/dL` in the main and sensitivity result rows and `≥100 mg/dL` in both supplied measure definitions.
- **Inferred explanation:** Abbreviation or transcription in the result labels could explain the symbol difference; the supplied sources do not establish that production history.
- **Exact remaining human question:** Which boundary was applied to the Table 2 and eTable 4 denominators, especially for patients whose LDL was exactly 100 mg/dL?
- **Status:** Pending Human Adjudication

## C003 — eTable 4 discharge-antithrombotics control percentage does not reproduce

- **Cited location found:** Yes. DOC-003, [`joi180070supp2_prod.pdf` — PDF p. 8](../../../joi180070supp2_prod.pdf#page=8), eTable 4, performance measures at discharge, `Antithrombotics`, control cell.
- **Source printed value/text matched:** Yes. The control cell prints `2141/2400 (89.3)`.
- **Comparator printed value/text matched:** Yes. The same cell explicitly prints numerator `2141` and denominator `2400` under the `No. / Total (%)` header.
- **Consistency rule applicable:** Yes. A percentage printed next to its explicit numerator and denominator should equal that fraction after ordinary rounding to one decimal place.
- **Calculation or logical comparison reproduced:** Yes. `2141 / 2400 × 100 = 89.2083333333%`, which rounds to `89.2%`, not `89.3%`.
- **Necessary inputs available:** Yes for the displayed arithmetic. The numerator, denominator, percentage, and table definition are printed. Missing for production-history explanation: unrounded analysis data, calculation code, or a stated nonstandard rounding rule.
- **Source-grounded alternative interpretation:** None is supplied for the arithmetic identity: the table header explicitly defines the cell as `No. / Total (%)`. A percentage calculated from a different unprinted denominator would not describe the printed fraction.
- **Direct observation:** The direct PDF prints `2141/2400 (89.3)` in one control cell.
- **Inferred explanation:** A transcription, stale percentage, or unreported calculation convention could explain the one-tenth difference; none is demonstrated by the supplied source.
- **Exact remaining human question:** Which of `2141`, `2400`, or `89.3` is the intended control result, and was any rule other than ordinary one-decimal rounding used?
- **Status:** Pending Human Adjudication

## C004 — eTable 4 AF-anticoagulation control percentage does not reproduce

- **Cited location found:** Yes. DOC-003, [`joi180070supp2_prod.pdf` — PDF p. 8](../../../joi180070supp2_prod.pdf#page=8), eTable 4, `Anticoagulation for Atrial Fibrillation`, control cell.
- **Source printed value/text matched:** Yes. The control cell prints `39/174 (22.5)`.
- **Comparator printed value/text matched:** Yes. The same cell explicitly prints numerator `39` and denominator `174` under the `No. / Total (%)` header.
- **Consistency rule applicable:** Yes. A percentage printed next to its explicit numerator and denominator should equal that fraction after ordinary rounding to one decimal place.
- **Calculation or logical comparison reproduced:** Yes. `39 / 174 × 100 = 22.4137931034%`, which rounds to `22.4%`, not `22.5%`.
- **Necessary inputs available:** Yes for the displayed arithmetic. The numerator, denominator, percentage, and table definition are printed. Missing for production-history explanation: unrounded analysis data, calculation code, or a stated nonstandard rounding rule.
- **Source-grounded alternative interpretation:** None is supplied for the arithmetic identity: the table header explicitly defines the cell as `No. / Total (%)`. A percentage calculated from a different unprinted denominator would not describe the printed fraction.
- **Direct observation:** The direct PDF prints `39/174 (22.5)` in one control cell.
- **Inferred explanation:** A transcription, stale percentage, or unreported calculation convention could explain the one-tenth difference; none is demonstrated by the supplied source.
- **Exact remaining human question:** Which of `39`, `174`, or `22.5` is the intended control result, and was any rule other than ordinary one-decimal rounding used?
- **Status:** Pending Human Adjudication

## C005 — eTable 4 lipid-lowering control percentage does not reproduce

- **Cited location found:** Yes. DOC-003, [`joi180070supp2_prod.pdf` — PDF p. 8](../../../joi180070supp2_prod.pdf#page=8), eTable 4, `Lipid-lowering for LDL >100 mg/dL`, control cell.
- **Source printed value/text matched:** Yes. The control cell prints `1439/1586 (90.8)`.
- **Comparator printed value/text matched:** Yes. The same cell explicitly prints numerator `1439` and denominator `1586` under the `No. / Total (%)` header.
- **Consistency rule applicable:** Yes. A percentage printed next to its explicit numerator and denominator should equal that fraction after ordinary rounding to one decimal place.
- **Calculation or logical comparison reproduced:** Yes. `1439 / 1586 × 100 = 90.7313997478%`, which rounds to `90.7%`, not `90.8%`.
- **Necessary inputs available:** Yes for the displayed arithmetic. The numerator, denominator, percentage, and table definition are printed. Missing for production-history explanation: unrounded analysis data, calculation code, or a stated nonstandard rounding rule.
- **Source-grounded alternative interpretation:** None is supplied for the arithmetic identity: the table header explicitly defines the cell as `No. / Total (%)`. C002's eligibility-boundary question does not change the arithmetic of the numerator and denominator printed in this cell.
- **Direct observation:** The direct PDF prints `1439/1586 (90.8)` in one control cell.
- **Inferred explanation:** A transcription, stale percentage, or unreported calculation convention could explain the one-tenth difference; none is demonstrated by the supplied source.
- **Exact remaining human question:** Which of `1439`, `1586`, or `90.8` is the intended control result, and was any rule other than ordinary one-decimal rounding used?
- **Status:** Pending Human Adjudication

## C006 — eTable 4 antidiabetic-medication control percentage does not reproduce

- **Cited location found:** Yes. DOC-003, [`joi180070supp2_prod.pdf` — PDF p. 8](../../../joi180070supp2_prod.pdf#page=8), eTable 4, `Antidiabetic Medication`, control cell.
- **Source printed value/text matched:** Yes. The control cell prints `557/688 (81.1)`.
- **Comparator printed value/text matched:** Yes. The same cell explicitly prints numerator `557` and denominator `688` under the `No. / Total (%)` header.
- **Consistency rule applicable:** Yes. A percentage printed next to its explicit numerator and denominator should equal that fraction after ordinary rounding to one decimal place.
- **Calculation or logical comparison reproduced:** Yes. `557 / 688 × 100 = 80.9593023256%`, which rounds to `81.0%`, not `81.1%`.
- **Necessary inputs available:** Yes for the displayed arithmetic. The numerator, denominator, percentage, and table definition are printed. Missing for production-history explanation: unrounded analysis data, calculation code, or a stated nonstandard rounding rule.
- **Source-grounded alternative interpretation:** None is supplied for the arithmetic identity: the table header explicitly defines the cell as `No. / Total (%)`. A percentage calculated from a different unprinted denominator would not describe the printed fraction.
- **Direct observation:** The direct PDF prints `557/688 (81.1)` in one control cell.
- **Inferred explanation:** A transcription, stale percentage, or unreported calculation convention could explain the one-tenth difference; none is demonstrated by the supplied source.
- **Exact remaining human question:** Which of `557`, `688`, or `81.1` is the intended control result, and was any rule other than ordinary one-decimal rounding used?
- **Status:** Pending Human Adjudication

## C007 — baseline-survey total does not reconcile with stated per-cluster inclusion

- **Cited location found:** Yes. DOC-001, [`jama_wang_2018_oi_180070.pdf` — PDF p. 6](../../../jama_wang_2018_oi_180070.pdf#page=6), Table 1 baseline-survey `Hospitals, No.` and `Patients, No.` rows; DOC-003, [`joi180070supp2_prod.pdf` — PDF p. 2](../../../joi180070supp2_prod.pdf#page=2), eAppendix baseline-survey description; DOC-001, [`jama_wang_2018_oi_180070.pdf` — PDF p. 5](../../../jama_wang_2018_oi_180070.pdf#page=5), Figure 1; and DOC-002, [`joi180070supp1_prod.pdf` — PDF p. 4](../../../joi180070supp1_prod.pdf#page=4), design lines 71-74, and [`joi180070supp1_prod.pdf` — PDF p. 7](../../../joi180070supp1_prod.pdf#page=7), cluster-randomization lines 93-100.
- **Source printed value/text matched:** Partial. The value `801` is matched, but its exact printed form is Table 1's `Patients, No.` row under the `Baseline Survey, No. (%)` column; the direct source does not literally print the ledger shorthand `Survey (n=801)`.
- **Comparator printed value/text matched:** Yes. The same Table 1 baseline-survey column prints `40` hospitals; DOC-003 p. 2 states `20 patients per cluster were prospectively included in this phase`; DOC-001 p. 5 and DOC-002 pp. 4 and 7 identify 40 hospitals/clusters.
- **Consistency rule applicable:** Partial. If `20 patients per cluster` is an exact fixed count and the baseline survey comprised the same 40 clusters, multiplication should equal the survey patient total. The sources do not explicitly state whether 20 was an exact cap or an operational target, although the phrase `were prospectively included` is presented without approximation.
- **Calculation or logical comparison reproduced:** Yes under the stated fixed-count reading. `20 patients/cluster × 40 clusters = 800 patients`; Table 1 prints 801, a difference of one patient.
- **Necessary inputs available:** Partial. The reported patient total, baseline-survey hospital count, per-cluster count, and trial cluster count are available. Missing: cluster-level baseline-survey counts, confirmation that every one of the 40 Table 1 survey hospitals contributed exactly 20 patients, and whether one over-enrollment or replacement record was included.
- **Source-grounded alternative interpretation:** The eAppendix may be describing the intended sampling target rather than an exact realized count, allowing one cluster to contribute 21 patients. The package supplies no cluster-level counts or explicit qualification of `20 patients per cluster` to establish this interpretation.
- **Direct observation:** Table 1 prints 40 baseline-survey hospitals and 801 baseline-survey patients; the eAppendix prints 20 patients per cluster; the article and protocol print 40 hospitals/clusters.
- **Inferred explanation:** One extra patient, a target-versus-realized distinction, or a replacement/duplicate record could explain the difference; none is directly documented in the supplied sources.
- **Exact remaining human question:** Did each of the 40 baseline-survey clusters contribute exactly 20 included patients, and if so what accounts for the 801st Table 1 patient?
- **Transcription limitation:** The ledger's phrase `Survey (n=801)` is a shorthand rather than a verbatim Table 1 header. The source-confirmed locator is `Baseline Survey, No. (%)` column, `Patients, No.` row = `801`. This recheck does not alter the stable ledger.
- **Status:** Pending Human Adjudication

## C008 — in-hospital death absolute-difference CI and P value do not reconcile

- **Cited location found:** Yes. DOC-001, [`jama_wang_2018_oi_180070.pdf` — PDF p. 8](../../../jama_wang_2018_oi_180070.pdf#page=8), Table 3, `Death` / `In hospital` row, `Absolute Difference (95% CI), %` and adjacent `P Value` columns; and [`jama_wang_2018_oi_180070.pdf` — PDF p. 4](../../../jama_wang_2018_oi_180070.pdf#page=4), Data Analysis statements.
- **Source printed value/text matched:** Yes. Table 3 prints absolute difference `−0.7` with 95% CI `−1.1 to 0.2` in a column headed percent.
- **Comparator printed value/text matched:** Yes. The adjacent absolute-difference `P Value` cell prints `.009`. Page 4 states that comparative outcomes were presented as adjusted absolute differences with 95% CIs and that all tests were two-sided.
- **Consistency rule applicable:** Partial. For a two-sided test and 95% CI of the same estimand from the same model, variance estimate, and inferential method, the CI/test duality rule applies at the `.05` level. The package does not explicitly state the exact test statistic, CI construction, or whether this P value and CI use identical inferential machinery.
- **Calculation or logical comparison reproduced:** Yes. `−1.1 < 0 < 0.2`, so the printed 95% CI contains the null absolute difference of zero. The adjacent `.009` is less than `.05`; under a matched two-sided 95% CI/P pairing, those two threshold conclusions differ.
- **Necessary inputs available:** Partial. The point estimate, CI, P value, confidence level, two-sided statement, adjustment statement, and table-column pairing are available. Missing: the exact test used for `.009`, the CI construction method, standard error/test statistic, and explicit confirmation that the P value tests the identical adjusted absolute-difference estimand rather than another group-effect parameter.
- **Source-grounded alternative interpretation:** The P value could come from a different but adjacent group-comparison test while the CI describes the adjusted absolute difference. The table places `.009` in the P-value column immediately following the absolute-difference column, but it does not define that P value's exact test. The HR and its P value are printed in separate columns and are not the comparator used here.
- **Direct observation:** One Table 3 row prints `−0.7 (−1.1 to 0.2)` and adjacent `.009`; the methods print `95% CIs`, adjustment, and `all tests were 2-sided`.
- **Inferred explanation:** A different test/estimand, a transposed P value, or a misprinted CI could explain the threshold conflict; none is established by the supplied package.
- **Exact remaining human question:** Does `.009` test the same adjusted absolute-difference estimand represented by `−0.7% (95% CI, −1.1% to 0.2%)`; if yes, which printed inferential element or method definition accounts for the non-duality?
- **Status:** Pending Human Adjudication

## Recheck limitations

- Source confirmation was limited to the three supplied PDFs and the exact cited pages; no external literature, raw data, analysis code, or web source was used.
- Fresh native/layout extraction and rendered pages were only locators and viewing aids. The direct PDF page content controlled every transcription above.
- The supplied package lacks raw or cluster-level records, operational eligibility code, unrounded analysis data, and detailed test/CI construction for the unresolved questions named above.
- No stable ID was deleted, merged, renumbered, or assigned an AI disposition.
