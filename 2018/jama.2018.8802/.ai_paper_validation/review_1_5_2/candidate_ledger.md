# Stable Candidate Ledger

All checker outputs were merged before stable IDs. Records were merged only when they concern the same printed values or statements, comparator, and rule. `NC002` and `XC001` are one genuine duplicate; all other provisional records remain distinct. Every candidate is **Pending Human Adjudication**.

## C001 — Table 1 CAD/previous-MI percentage does not reconcile with 311/2400

- **Discovery provenance:** NC001.
- **Category:** Numeric or arithmetic inconsistency.
- **Exact source locations:** DOC-001, [jama_wang_2018_oi_180070.pdf — PDF p. 6](<../../jama_wang_2018_oi_180070.pdf#page=6>), Table 1, `CAD/previous myocardial infarction`, intervention column.
- **Direct source evidence:** The cell prints `311 (13.05)` and the intervention denominator is 2400.
- **Rule/calculation:** `311 / 2400 × 100 = 12.9583%`, which rounds to `13.0%` at one decimal or `12.96%` at two decimals, not `13.05%`.
- **Alternative source-grounded interpretation:** An unstated denominator or a transcription issue could explain the cell; neither is supplied.
- **Human question:** Does the direct PDF intentionally report `13.05`, and which count, denominator, or percentage is intended?

## C002 — LDL eligibility threshold is printed as both >100 and ≥100 mg/dL

- **Discovery provenance:** NC002 and XC001, merged as the same comparator/rule.
- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-001, [PDF p. 3](<../../jama_wang_2018_oi_180070.pdf#page=3>) Outcomes and [PDF p. 7](<../../jama_wang_2018_oi_180070.pdf#page=7>) Table 2; DOC-002, [PDF p. 14](<../../joi180070supp1_prod.pdf#page=14>) and [PDF p. 15](<../../joi180070supp1_prod.pdf#page=15>); DOC-003, [PDF p. 3](<../../joi180070supp2_prod.pdf#page=3>) eTable 1.
- **Direct source evidence:** The article uses `LDL >100 mg/dL`; the protocol and eTable definition use `LDL ≥100 mg/dL` and state additional eligibility conditions.
- **Rule/calculation:** `>100` excludes exactly 100 mg/dL, whereas `≥100` includes it, so the eligible denominator definitions are not identical.
- **Alternative source-grounded interpretation:** The main article may abbreviate the full specification; the package does not identify the rule used to construct the displayed denominators.
- **Human question:** Which boundary and eligibility conditions governed the reported lipid-lowering denominators?

## C003 — Exact 20-patients-per-cluster statement conflicts with the 801 baseline total

- **Discovery provenance:** NC003.
- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-003, [joi180070supp2_prod.pdf — PDF p. 2](<../../joi180070supp2_prod.pdf#page=2>), baseline-survey statement; DOC-001, [PDF p. 3](<../../jama_wang_2018_oi_180070.pdf#page=3>), 40 hospitals, and [PDF p. 6](<../../jama_wang_2018_oi_180070.pdf#page=6>), Table 1 header reporting 801 baseline patients.
- **Direct source evidence:** The supplement states that 20 patients per cluster were prospectively included; the package reports 40 clusters and 801 baseline-survey patients.
- **Rule/calculation:** `20 × 40 = 800`, one fewer than the printed 801 total.
- **Alternative source-grounded interpretation:** One cluster may have included an extra patient, or 20 may describe a target, but the source does not qualify the statement as approximate.
- **Human question:** Was 20 exact for every cluster, and if so why is the baseline denominator 801?

## C004 — Direct recheck finds the rtPA cell prints 9.66 and reconciles with 23/238

- **Discovery provenance:** NC004.
- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../../joi180070supp2_prod.pdf#page=8>), eTable 4, `IV rt-PA 2 Hour`, control column.
- **Direct source evidence:** Mechanical direct-PDF recheck found that the cell visibly prints `23/238 (9.66)`, not the discovery transcription `9.6`; the paired intervention cell prints `46/254 (18.11)`.
- **Rule/calculation:** `23 / 238 × 100 = 9.6639%`, which rounds to the printed `9.66%` at two decimals. Likewise, `46 / 254 × 100 = 18.1102%`, which rounds to `18.11%`.
- **Alternative source-grounded interpretation:** Both cells support intentional row-specific two-decimal precision; the source does not say whether that precision was intentional or a production-formatting artifact.
- **Human question:** Should the rtPA row be read using the visibly printed two-decimal values, and was its row-specific precision intentional? The stable ID is retained as required after registration; this mechanical fact is not an AI adjudication.

## C005 — eTable 4 discharge-antithrombotics control percentage does not reconcile with 2141/2400

- **Discovery provenance:** NC005.
- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../../joi180070supp2_prod.pdf#page=8>), eTable 4, discharge-antithrombotics control cell.
- **Direct source evidence:** The cell prints `2141/2400 (89.3)`.
- **Rule/calculation:** `2141 / 2400 × 100 = 89.2083%`, which rounds to `89.2%`, not `89.3%`.
- **Alternative source-grounded interpretation:** The package gives no alternate denominator or rounding rule.
- **Human question:** Which count, denominator, or percentage is intended?

## C006 — eTable 4 AF-anticoagulation control percentage does not reconcile with 39/174

- **Discovery provenance:** NC006.
- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../../joi180070supp2_prod.pdf#page=8>), eTable 4, atrial-fibrillation/flutter anticoagulation control cell.
- **Direct source evidence:** The cell prints `39/174 (22.5)`.
- **Rule/calculation:** `39 / 174 × 100 = 22.4138%`, which rounds to `22.4%`, not `22.5%`.
- **Alternative source-grounded interpretation:** The package supplies no alternate denominator or percentage convention.
- **Human question:** Which displayed value is intended for the control adherence proportion?

## C007 — eTable 4 lipid-lowering control percentage does not reconcile with 1439/1586

- **Discovery provenance:** NC007.
- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../../joi180070supp2_prod.pdf#page=8>), eTable 4, lipid-lowering control cell.
- **Direct source evidence:** The cell prints `1439/1586 (90.8)`.
- **Rule/calculation:** `1439 / 1586 × 100 = 90.7314%`, which rounds to `90.7%`, not `90.8%`.
- **Alternative source-grounded interpretation:** The threshold-definition issue is separately C002; no alternate denominator or rounding rule explains this percentage cell.
- **Human question:** Which of 1439, 1586, or 90.8% is intended?

## C008 — eTable 4 antidiabetic-medication control percentage does not reconcile with 557/688

- **Discovery provenance:** NC008.
- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** DOC-003, [joi180070supp2_prod.pdf — PDF p. 8](<../../joi180070supp2_prod.pdf#page=8>), eTable 4, hypoglycemic-therapy control cell.
- **Direct source evidence:** The cell prints `557/688 (81.1)`.
- **Rule/calculation:** `557 / 688 × 100 = 80.9593%`, which rounds to `81.0%`, not `81.1%`.
- **Alternative source-grounded interpretation:** The package supplies no alternate denominator or rounding rule.
- **Human question:** Which printed value is intended for this control row?

## C009 — In-hospital-death absolute-difference P value conflicts with its displayed 95% CI

- **Discovery provenance:** SP1-001.
- **Category:** Statistical reporting inconsistency.
- **Exact source locations:** DOC-001, [jama_wang_2018_oi_180070.pdf — PDF p. 8](<../../jama_wang_2018_oi_180070.pdf#page=8>), Table 3, Death—In hospital row.
- **Direct source evidence:** The adjusted absolute difference is `−0.7` with `95% CI, −1.1 to 0.2`, while the adjacent P value is `.009`; the separately labeled HR is `.96 (95% CI, .90 to 1.02)` with P=.14.
- **Rule/calculation:** The displayed absolute-difference 95% CI includes 0, while its same-column P=.009 is below .05. A rough CI-based diagnostic gives midpoint −0.45, half-width 0.65, SE about 0.33, and |z| about 1.36; this is not a replacement analysis.
- **Alternative source-grounded interpretation:** The source does not give a special non-common CI/P construction, estimator, or degrees-of-freedom rule that would reconcile the pair.
- **Human question:** Does `.009` belong to this absolute-difference row and, if so, what stated analysis rule reconciles it with the printed CI?

## C010 — Composite adherence has conflicting patient-level and care-opportunity analysis descriptions

- **Discovery provenance:** XC002.
- **Category:** Analysis-unit or population inconsistency.
- **Exact source locations:** DOC-001, [PDF p. 3](<../../jama_wang_2018_oi_180070.pdf#page=3>) Outcomes, [PDF p. 4](<../../jama_wang_2018_oi_180070.pdf#page=4>) analysis unit, and [PDF p. 7](<../../jama_wang_2018_oi_180070.pdf#page=7>) Table 2; DOC-002, [PDF p. 18](<../../joi180070supp1_prod.pdf#page=18>) and [PDF p. 19](<../../joi180070supp1_prod.pdf#page=19>); DOC-003, [PDF p. 2](<../../joi180070supp2_prod.pdf#page=2>).
- **Direct source evidence:** The article says the composite was calculated for each patient and averaged; the protocol says each eligible care opportunity contributed a binary observation; the appendix gives a pooled performed/possible-interventions definition.
- **Rule/calculation:** A mean of patient percentages weights patients equally; a pooled opportunity proportion weights patients according to eligible opportunities. These can produce different reported composite percentages, differences, and model interpretations.
- **Alternative source-grounded interpretation:** Descriptive and inferential summaries may intentionally use different units, but the supplied package does not reconcile them under the common composite label.
- **Human question:** Which unit generated the printed 88.2%/84.8%, adjusted difference, and ORPA?

## C011 — DVT-prophylaxis window is labeled as both within 48 hours and by end of hospital day 2

- **Discovery provenance:** XC003.
- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** DOC-002, [PDF p. 13](<../../joi180070supp1_prod.pdf#page=13>) protocol Table 2, [PDF p. 14](<../../joi180070supp1_prod.pdf#page=14>) Table 3, and [PDF p. 15](<../../joi180070supp1_prod.pdf#page=15>) continuation; DOC-003, [PDF p. 3](<../../joi180070supp2_prod.pdf#page=3>) eTable 1; DOC-001, [PDF p. 7](<../../jama_wang_2018_oi_180070.pdf#page=7>) Table 2 footnote.
- **Direct source evidence:** Protocol Table 2 says `within 48 hours of admission`; the detailed specification, eTable, and reported-table footnote say `by end of hospital day 2`.
- **Rule/calculation:** An elapsed 48-hour window and a calendar hospital-day-2 boundary can include different events unless the operational definition explicitly equates them.
- **Alternative source-grounded interpretation:** Hospital day 2 may have been operationalized as 48 elapsed hours; no such definition is supplied.
- **Human question:** Which timing rule generated the displayed 178/645 and 66/592 denominators and percentages?

**Stable candidate count:** 11. No candidate is based on a display-zero P value.
