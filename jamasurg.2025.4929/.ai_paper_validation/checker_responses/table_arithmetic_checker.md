# Table Arithmetic and Internal-Consistency Check

## Scope and method

- **Audited documents:** DOC-001 (main article) and DOC-003 (results supplement), as classified in the package manifest and extractor evidence maps.
- **Audited result-relevant tables:** DOC-001 Tables 1-4 (PDF pp. 4-7) and DOC-003 eTable 2 (PDF p. 3). DOC-003 eTable 1 is eligibility context, not an outcome/results table, and was not audited.
- **Evidence used:** canonical native-text derivatives, checked against the rendered table pages where cell placement or symbols mattered. OCR was not used as canonical evidence.
- **Not assessed:** protocol/SAP DOC-002; raw-data-dependent claims; test-method-dependent P values where the document permits either a t test/Mann-Whitney U test or chi-square/Fisher exact test.

## Candidate findings

All candidates are directly verifiable from visible table cells. Percentages below are recalculated from the displayed numerator and denominator, rounded to one decimal place.

| ID | Category / severity | Exact location | Visible source values | Calculation / logical basis | Concise reasoning and verification instruction |
|---|---|---|---|---|---|
| TAC-01 | Arithmetic inconsistency / **moderate** | DOC-003, `soi250075supp2_prod_1767031598.05318.pdf`, PDF p. 3, eTable 2, Age, `>=60` | `32/120 (27.7)` | 32 / 120 x 100 = 26.666...%, which rounds to **26.7%**, not 27.7%. | The printed numerator/denominator and percentage disagree by 1.0 percentage point. Verify the displayed percentage against the analysis table/export. |
| TAC-02 | Arithmetic inconsistency / **moderate** | DOC-003, PDF p. 3, eTable 2, pN, `N3` | `29/74 (25.7)` | 29 / 74 x 100 = 39.189...%, which rounds to **39.2%**, not 25.7%. | The visible percentage disagrees materially with the displayed fraction (13.5 percentage points). Verify both the numerator and percentage in the source analysis output. |
| TAC-03 | Statistical reporting inconsistency / **moderate** | DOC-003, PDF p. 3, eTable 2, pN, `N3`, univariate result | OR `0.431` (95% CI, `0.60-3.37`); P = `.431` | A confidence interval from 0.60 to 3.37 does **not** contain the printed point estimate 0.431. | The displayed OR and its displayed 95% CI are mutually incompatible. Verify the univariate OR, CI bounds, and P-value cells; no corrected value is inferred here. |
| TAC-04 | Arithmetic inconsistency / **minor** | DOC-003, PDF p. 3, eTable 2, GOO, `No` | `35/148 (23.7)` | 35 / 148 x 100 = 23.648...%, which rounds to **23.6%**, not 23.7%. | Visible fraction and one-decimal percentage differ by 0.1 percentage point. Verify the percentage display. |
| TAC-05 | Arithmetic inconsistency / **minor** | DOC-001, `jamasurgery_dat_2025_oi_250075_1767031598.03318.pdf`, PDF p. 4, Table 1, Anemia, LDG | `30 (28.9)` of LDG n = 104 | 30 / 104 x 100 = 28.846...%, which rounds to **28.8%**, not 28.9%. | Visible count and percentage differ by 0.1 percentage point. Verify the displayed percentage. |
| TAC-06 | Arithmetic inconsistency / **minor** | DOC-001, PDF p. 5, Table 2, Intraoperative injury, ODG | `4 (3.9)` of ODG n = 104 | 4 / 104 x 100 = 3.846...%, which rounds to **3.8%**, not 3.9%. | Visible count and percentage differ by 0.1 percentage point. Verify the displayed percentage. |
| TAC-07 | Arithmetic inconsistency / **minor** | DOC-001, PDF p. 6, Table 3, Differentiated status, Undifferentiated, ODG | `58 (55.6)` of ODG n = 104 | 58 / 104 x 100 = 55.769...%, which rounds to **55.8%**, not 55.6%. | Visible count and percentage differ by 0.2 percentage point. Verify the displayed percentage and, if necessary, the count. |
| TAC-08 | Arithmetic inconsistency / **minor** | DOC-001, PDF p. 7, Table 4, Paralytic ileus, ODG | `5 (4.9)` of ODG n = 104 | 5 / 104 x 100 = 4.807...%, which rounds to **4.8%**, not 4.9%. | Visible count and percentage differ by 0.1 percentage point. Verify the displayed percentage. |
| TAC-09 | Arithmetic inconsistency / **minor** | DOC-001, PDF p. 7, Table 4, Systemic infection, ODG | `4 (3.9)` of ODG n = 104 | 4 / 104 x 100 = 3.846...%, which rounds to **3.8%**, not 3.9%. | Visible count and percentage differ by 0.1 percentage point. Verify the displayed percentage. |
| TAC-10 | Arithmetic inconsistency / **minor** | DOC-001, PDF p. 7, Table 4, Surgical complications, ODG | `17 (16.4)` of ODG n = 104 | 17 / 104 x 100 = 16.346...%, which rounds to **16.3%**, not 16.4%. | Visible count and percentage differ by 0.1 percentage point. Verify the displayed percentage. |

## Checked items with no candidate issue

- **DOC-001, Table 1 (PDF p. 4):** Sex, ASA-PS, ECOG status, tumor location, and cN-stage subgroup counts each total 104 per treatment group; other displayed count/percentage pairs checked were consistent to one decimal place, apart from TAC-05.
- **DOC-001, Table 2 (PDF p. 5):** Intraoperative-injury component counts total the parent injury counts (LDG: 0 + 2 + 1 + 0 = 3; ODG: 2 + 1 + 1 + 0 = 4). Reconstruction counts total 104 in each group (71 + 33; 92 + 12). Other checked percentage cells were consistent, apart from TAC-06.
- **DOC-001, Table 3 (PDF p. 6):** Macroscopic type, pT stage, pN stage, TNM stage, and differentiated-status subgroup counts total 104 within each treatment group. The R1 parent count equals positive cytology plus positive resection-margin counts in both groups (7 = 6 + 1; 7 = 5 + 2). Other checked percentages were consistent, apart from TAC-07.
- **DOC-001, Table 4 (PDF p. 7):** Overall morbidity equals the sum of Clavien-Dindo grades (LDG: 14 + 6 + 1 + 1 + 0 + 1 = 23; ODG: 7 + 11 + 2 + 0 + 0 + 2 = 22). Major complications also equal grades IIIa-V (LDG: 3; ODG: 4). Component complication rows were not summed to overall morbidity because a patient can have multiple complications. Other checked percentage cells were consistent, apart from TAC-08 through TAC-10.
- **DOC-003, eTable 2 (PDF p. 3):** Each displayed categorical denominator totals 208, and each morbidity numerator totals 45, within its variable. The approach cells (23/104 and 22/104) agree with DOC-001 Table 4. Other displayed fractions/percentages were consistent, apart from TAC-01, TAC-02, and TAC-04.

## Limitations

No error is inferred from unavailable raw data. P values and regression estimates were not recalculated from summary cells when the reported test/model cannot be uniquely reconstructed from the article package; TAC-03 is limited to the visible point-estimate/CI containment failure.
