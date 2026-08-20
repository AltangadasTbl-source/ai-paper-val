# Stable Candidate Ledger

All five source-grounded quality-control candidates below are **Pending Human Adjudication**. Stable IDs were assigned only after merging the numeric, statistical-pass-1, and cross-source propositions. The duplicate ECOG proposition from the numeric and cross-source lanes was merged because it concerns the same printed cell, denominator, and percentage rule. The two sample-size candidates remain separate because one applies an internal whole-person addition rule and the other compares different planning inputs across documents.

## C001 — Talc-arm ECOG unknown percentage does not match the count and denominator

- **Status:** Pending Human Adjudication
- **Category:** Denominator, proportion, or total inconsistency
- **Relationships/provenance:** N009; numeric review and cross-source review (duplicate-only merge).
- **Exact locations:** DOC-001 `jama_thomas_2017_oi_170130.pdf#page=4`, Table 1, ECOG score, talc pleurodesis column.
- **Direct source evidence:** Talc arm `n=72`; ECOG rows `53 (74)`, `14 (19)`, and unknown `5 (17)`; counts total 72.
- **Rule/calculation:** A `No. (%)` cell uses `100 × count / denominator`; `100 × 5/72 = 6.944...%`, which rounds to 7%, not 17%. Companion cells confirm the denominator and whole-percent convention.
- **Alternative source-grounded interpretations:** The percentage may contain an extra digit, or the count/denominator may be wrong; no alternate denominator is supplied.
- **Exact human question:** Is the intended cell `5 (7)`, or is a different count or denominator supported by the table-production record?

## C002 — Final-protocol sample-size addition does not equal the printed total

- **Status:** Pending Human Adjudication
- **Category:** Numeric or arithmetic inconsistency
- **Relationships/provenance:** N052 and S042; numeric review addendum and statistical pass-1 proposition P1-03.
- **Exact location:** DOC-002 `joi170130supp1_prod.pdf#page=37`, final-protocol sample-size section.
- **Direct source evidence:** The page prints 62 patients per group, an additional 24 patients for loss to follow-up, and a total recruitment target of 146.
- **Rule/calculation:** Whole-person base plus additions must equal the total: `62 + 62 + 24 = 148`, not 146. Also, 20% of 124 is 24.8, which does not produce 146 under ordinary rounding.
- **Alternative source-grounded interpretations:** One of the base-per-group value, added-person count, loss percentage, or target may be misstated; the later SAP/main calculation uses a different coherent basis but does not repair this page.
- **Exact human question:** Which printed component is intended, and what was the internally consistent final-protocol sample-size calculation?

## C003 — Final protocol and SAP/main article give different sample-size inputs for the same target

- **Status:** Pending Human Adjudication
- **Category:** Cross-document numeric inconsistency
- **Relationships/provenance:** N052 and S042; cross-source review Proposition A.
- **Exact locations:** DOC-002 `joi170130supp1_prod.pdf#page=37` (final protocol); DOC-002 `joi170130supp1_prod.pdf#page=62` (SAP); DOC-001 `jama_thomas_2017_oi_170130.pdf#page=3` (Methods).
- **Direct source evidence:** The final protocol gives 62 per group plus a 20%/24-participant allowance for target 146. The SAP and main article give 65 per group, 12% loss, and target 73 per group/146.
- **Rule/comparison:** These are two incompatible base-size and attrition parameter sets presented for the same AMPLE recruitment target. The supplied package does not explicitly connect them with a superseding calculation.
- **Alternative source-grounded interpretations:** The SAP/main basis may have deliberately superseded the final-protocol calculation; version history mentions sample-size-section changes but does not identify the operative numeric replacement on these pages.
- **Exact human question:** Which parameter set governed recruitment, and should the relation between the final-protocol and SAP/main calculations be clarified?

## C004 — SAP ITT definition conflicts with the reported 144-patient ITT denominator

- **Status:** Pending Human Adjudication
- **Category:** Analysis-unit or population inconsistency
- **Relationships/provenance:** S044 with affected reported relationships S002, S005-S025, and S027-S032; statistical pass-1 proposition P1-01.
- **Exact locations:** DOC-002 `joi170130supp1_prod.pdf#page=62` and `#page=63` (SAP ITT definition); DOC-001 `jama_thomas_2017_oi_170130.pdf#page=3` (flow), `#page=4` (analysis population), and `#page=6` (Table 2).
- **Direct source evidence:** The SAP defines ITT as every randomized subject, including those not receiving assigned treatment. The main article reports 74+72=146 randomized, excludes one pre-intervention withdrawal per arm from all analyses, and labels 73+71=144 as ITT.
- **Rule/calculation:** Under the supplied SAP definition, all 146 randomized participants belong to ITT; the reported ITT denominator is `73+71=144`, two fewer.
- **Alternative source-grounded interpretations:** A modified ITT convention or later amendment may authorize the exclusions, but no supplied source names or documents it.
- **Exact human question:** Was an operative amendment or prespecified exception used, and if not, should the ITT label or affected denominators be clarified?

## C005 — Estimated-difference contrast direction is unlabeled and reverses between the main and MI tables

- **Status:** Pending Human Adjudication
- **Category:** Measure, label, or scale inconsistency
- **Relationships/provenance:** S010-S024, S033, S051; statistical pass-1 proposition P1-02.
- **Exact locations:** DOC-001 `jama_thomas_2017_oi_170130.pdf#page=6`, Table 2; DOC-003 `joi170130supp2_prod.pdf#page=2`, multiple-imputation eTable.
- **Direct source evidence:** Both tables list IPC before talc and label a column `Estimated Difference (95% CI)` without a subtraction order. Main baseline dyspnea is 50.0 versus 52.2 with +2.27 and day 1 is 64.5 versus 69.7 with +5.25, implying talc minus IPC. MI baseline is 49.8 versus 51.9 with -2.06 and day 1 is 65.5 versus 71.7 with -6.19, implying IPC minus talc.
- **Rule/comparison:** A signed difference needs a reference group/contrast direction. Arithmetic shows opposite implied subtraction orders across the two tables; MI versus non-MI explains magnitude changes, not an unlabeled sign convention.
- **Alternative source-grounded interpretations:** Both signs can be reconstructed from the displayed group estimates and may be intentional parameterizations; the candidate concerns labeling, not numerical equality of the two analyses.
- **Exact human question:** Were opposite reference groups intended, and should each table explicitly label its subtraction order?

No display-zero P-value-only proposition was registered. No candidate has been assigned severity, validity, disposition, or correction.
