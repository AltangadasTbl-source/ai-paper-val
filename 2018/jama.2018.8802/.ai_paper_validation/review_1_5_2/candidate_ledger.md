# Stable Candidate Ledger

Eight distinct quality-control candidates were registered after merging only genuine duplicate proposals. `NCAND002` and `P1CAND002` concerned the same printed LDL threshold contrast and were merged as C002 with both provenances retained. All other proposals concern different printed values, comparators, or rules. Stable IDs will not be deleted, merged, or renumbered. Every entry remains **Pending Human Adjudication**.

## C001 — Table 1 CAD/previous-myocardial-infarction percentage does not reproduce

- **Candidate statement:** The intervention cell prints `311 (13.05)` under a 2,400-patient column, but the displayed fraction does not yield 13.05%.
- **Category:** Numeric or arithmetic inconsistency
- **Exact source locations:** DOC-001, `jama_wang_2018_oi_180070.pdf`, PDF p. 6, Table 1, `CAD/previous myocardial infarction`, intervention column and `Patients, No. 2400` header.
- **Source evidence:** Numerator 311; denominator 2,400; percentage 13.05.
- **Reported-versus-comparator:** Reported 13.05%; exact fraction 311/2,400.
- **Consistency rule:** A printed percentage should reproduce from its printed numerator and denominator within its displayed precision.
- **Calculation:** `311 / 2400 × 100 = 12.9583%`, which rounds to 13.0% at one decimal or 12.96% at two decimals, not 13.05%.
- **Alternative source-grounded interpretations:** No alternative denominator or calculation is printed; a typographic error or unprinted rule remains possible but unestablished.
- **Provenance:** N030; NCAND001.
- **Exact remaining human question:** Does 13.05 use an unprinted denominator/calculation, or which displayed element is intended?
- **Status:** Pending Human Adjudication

## C002 — LDL eligibility boundary differs between result labels and supplied measure definition

- **Candidate statement:** The main and sensitivity result rows use `LDL >100 mg/dL`, while the supplied formal measure definition uses `LDL ≥100 mg/dL`.
- **Category:** Measure, label, or scale inconsistency
- **Exact source locations:** DOC-001, `jama_wang_2018_oi_180070.pdf`, PDF p. 7, Table 2 lipid-lowering row; DOC-002, `joi180070supp1_prod.pdf`, PDF p. 15, lipid-lowering definition; DOC-003, `joi180070supp2_prod.pdf`, PDF p. 3, eTable 1 definition, and PDF p. 8, eTable 4 result label.
- **Source evidence:** Result labels state `>100 mg/dL`; definition states `≥100 mg/dL`, with other separately stated eligibility conditions.
- **Reported-versus-comparator:** A strict threshold excludes LDL exactly 100 mg/dL; an inclusive threshold includes it.
- **Consistency rule:** Matched measure labels and definitions should identify the same boundary and resulting eligibility population.
- **Calculation:** Discrete-symbol comparison: `>100 ≠ ≥100`; no rounding tolerance applies.
- **Alternative source-grounded interpretations:** The result-row wording may be an abbreviated display while the formal definition controlled eligibility, but the supplied package does not say so.
- **Provenance:** N023, N044, S009, S059; NCAND002 and P1CAND002 merged as a genuine duplicate.
- **Exact remaining human question:** Which threshold governed the reported denominators, particularly for LDL exactly 100 mg/dL?
- **Status:** Pending Human Adjudication

## C003 — eTable 4 discharge-antithrombotics control percentage does not reproduce

- **Candidate statement:** The control cell prints `2141/2400 (89.3)`, but the fraction rounds to 89.2% at one decimal.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** DOC-003, `joi180070supp2_prod.pdf`, PDF p. 8, eTable 4, `Antithrombotics`, control cell.
- **Source evidence:** 2,141 numerator; 2,400 denominator; 89.3% percentage.
- **Reported-versus-comparator:** Reported 89.3%; fraction-derived 89.2083%.
- **Consistency rule:** A percentage printed beside a fraction should equal the fraction after ordinary rounding to the displayed precision.
- **Calculation:** `2141 / 2400 × 100 = 89.2083%`, which rounds to 89.2%; the nearest-tenth interval for 89.3% begins at 89.25%.
- **Alternative source-grounded interpretations:** The overall-population sensitivity label does not replace the printed denominator; no nonstandard rounding rule is supplied.
- **Provenance:** N065; NCAND003.
- **Exact remaining human question:** Which of the count, denominator, or percentage represents the intended control result?
- **Status:** Pending Human Adjudication

## C004 — eTable 4 AF-anticoagulation control percentage does not reproduce

- **Candidate statement:** The control cell prints `39/174 (22.5)`, but the fraction rounds to 22.4% at one decimal.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** DOC-003, `joi180070supp2_prod.pdf`, PDF p. 8, eTable 4, `Anticoagulation for Atrial Fibrillation`, control cell.
- **Source evidence:** 39 numerator; 174 denominator; 22.5% percentage.
- **Reported-versus-comparator:** Reported 22.5%; fraction-derived 22.4138%.
- **Consistency rule:** A percentage printed beside a fraction should reproduce after ordinary rounding.
- **Calculation:** `39 / 174 × 100 = 22.4138%`, which rounds to 22.4%; it is below the 22.45% lower boundary for a one-decimal display of 22.5%.
- **Alternative source-grounded interpretations:** No alternative denominator or rounding convention is supplied.
- **Provenance:** N066; NCAND004.
- **Exact remaining human question:** Which printed control value represents the intended AF-anticoagulation proportion?
- **Status:** Pending Human Adjudication

## C005 — eTable 4 lipid-lowering control percentage does not reproduce

- **Candidate statement:** The control cell prints `1439/1586 (90.8)`, but the fraction rounds to 90.7% at one decimal.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** DOC-003, `joi180070supp2_prod.pdf`, PDF p. 8, eTable 4, lipid-lowering row, control cell.
- **Source evidence:** 1,439 numerator; 1,586 denominator; 90.8% percentage.
- **Reported-versus-comparator:** Reported 90.8%; fraction-derived 90.7314%.
- **Consistency rule:** A percentage printed beside a fraction should reproduce after ordinary rounding.
- **Calculation:** `1439 / 1586 × 100 = 90.7314%`, which rounds to 90.7%; it is below the 90.75% lower boundary for a one-decimal display of 90.8%.
- **Alternative source-grounded interpretations:** No alternative denominator or rounding convention is supplied; the LDL boundary issue is separately registered as C002 because it uses a different comparator and rule.
- **Provenance:** N067; NCAND005.
- **Exact remaining human question:** Which of the count, denominator, or percentage represents the intended sensitivity result?
- **Status:** Pending Human Adjudication

## C006 — eTable 4 antidiabetic-medication control percentage does not reproduce

- **Candidate statement:** The control cell prints `557/688 (81.1)`, but the fraction rounds to 81.0% at one decimal.
- **Category:** Denominator, proportion, or total inconsistency
- **Exact source locations:** DOC-003, `joi180070supp2_prod.pdf`, PDF p. 8, eTable 4, `Antidiabetic Medication`, control cell.
- **Source evidence:** 557 numerator; 688 denominator; 81.1% percentage.
- **Reported-versus-comparator:** Reported 81.1%; fraction-derived 80.9593%.
- **Consistency rule:** A percentage printed beside a fraction should reproduce after ordinary rounding.
- **Calculation:** `557 / 688 × 100 = 80.9593%`, which rounds to 81.0%; it is below the 81.05% lower boundary for a one-decimal display of 81.1%.
- **Alternative source-grounded interpretations:** No alternative denominator or rounding convention is supplied.
- **Provenance:** N069; NCAND006.
- **Exact remaining human question:** Which printed value represents the intended antidiabetic-medication proportion?
- **Status:** Pending Human Adjudication

## C007 — baseline-survey patient total does not reconcile with stated per-cluster inclusion

- **Candidate statement:** The main Table 1 baseline-survey column reports `Patients, No.` = 801, whereas the supplement says 20 patients per cluster were included and the same table reports 40 survey hospitals, implying 800 under an exact fixed-count reading.
- **Category:** Cross-document numeric inconsistency
- **Exact source locations:** DOC-001, `jama_wang_2018_oi_180070.pdf`, PDF p. 6, Table 1 `Baseline Survey, No. (%)` column, `Hospitals, No.` = 40 and `Patients, No.` = 801 rows; DOC-003, `joi180070supp2_prod.pdf`, PDF p. 2, eAppendix baseline-survey statement; DOC-001 PDF p. 5 Figure 1 and DOC-002, `joi180070supp1_prod.pdf`, PDF pp. 4 and 7, 40-cluster statements.
- **Source evidence:** Baseline-survey patient total 801; baseline-survey hospital total 40; statement that 20 patients per cluster were prospectively included.
- **Reported-versus-comparator:** Reported total 801 versus `20 × 40 = 800` under the stated same-survey interpretation.
- **Consistency rule:** A fixed per-cluster inclusion count multiplied by the complete cluster count should equal the matched survey total.
- **Calculation:** `20 × 40 = 800`; difference from reported 801 is one patient.
- **Alternative source-grounded interpretations:** One cluster may have contributed 21 patients, or 20 may have been an operational target rather than an exact realized count, but neither qualification is supplied.
- **Provenance:** N025, N028, N042, N072; XCAND001.
- **Exact remaining human question:** Did all 40 clusters contribute exactly 20 baseline-survey patients, and if so why is the table denominator 801?
- **Status:** Pending Human Adjudication

## C008 — in-hospital death absolute-difference CI and P value do not reconcile

- **Candidate statement:** The in-hospital-death adjusted absolute-difference 95% CI contains zero, while the corresponding adjacent absolute-difference P-value cell is `.009` under the article's two-sided testing statement.
- **Category:** Statistical reporting inconsistency
- **Exact source locations:** DOC-001, `jama_wang_2018_oi_180070.pdf`, PDF p. 8, Table 3 in-hospital death row and absolute-difference/P columns; DOC-001 PDF p. 4, two-sided-test and adjusted-absolute-difference reporting statements.
- **Source evidence:** Adjusted absolute difference `−0.7%`; 95% CI `−1.1% to 0.2%`; adjacent P value `.009`; tests described as two-sided.
- **Reported-versus-comparator:** The interval includes the null, while `.009 < .05` for the displayed same-column result.
- **Consistency rule:** Under a supplied same-estimand two-sided 95% CI/P pairing, an interval containing zero is not compatible with P below .05.
- **Calculation:** `−1.1 < 0 < 0.2`, so zero lies inside the printed interval; `.009 < .05`.
- **Alternative source-grounded interpretations:** The P value could arise from a different estimand/model, but the supplied table places it in the absolute-difference P-value column and states no such distinction. The adjacent HR is a separate effect-measure column and is not the comparator.
- **Provenance:** S019; P1CAND001.
- **Exact remaining human question:** Does `.009` belong to this adjusted absolute-difference CI, or is the CI, P value, or table-column pairing different from what is printed?
- **Status:** Pending Human Adjudication
