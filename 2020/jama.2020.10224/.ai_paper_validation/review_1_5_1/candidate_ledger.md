# Candidate Ledger

All three distinct propositions referred by the completed numeric-consistency, statistical-pass-1, and cross-source-consistency checkers are registered below. Genuine duplicates were merged before stable numbering: the unit and protocol-table propositions were independently referred by the numeric and cross-source checkers but concern the same printed values and the same rule. There is no candidate cap. No display-zero P-value candidate exists.

Every record has status **Pending Human Adjudication**. This ledger makes no validity, severity, correction, or publication decision.

## C001 — Vitamin-D concentration unit differs at the 20-unit baseline threshold

- **Category:** Measure, label, or scale inconsistency.
- **Exact PDF locations:** [DOC-001 main article — PDF p. 6](<../../jama_okereke_2020_oi_200066.pdf#page=6>), Results, “Baseline Characteristics”; [DOC-001 main article — PDF p. 4](<../../jama_okereke_2020_oi_200066.pdf#page=4>), Table 1 and footnote; [DOC-001 main article — PDF p. 8](<../../jama_okereke_2020_oi_200066.pdf#page=8>), Figure 4; DOC-003 Supplement 2 [PDF p. 38](<../../joi200066supp2_prod.pdf#page=38>), [PDF p. 39](<../../joi200066supp2_prod.pdf#page=39>), and [PDF p. 40](<../../joi200066supp2_prod.pdf#page=40>), eTable 14 and narrative.
- **Source evidence:** DOC-001 p. 6 prints: “The mean 25-hydroxyvitamin D level was 31.1 ng/mL and 11.6% of participants had levels lower than 20 mg/mL.”
- **Comparator evidence:** DOC-001 Table 1 labels the same analyte and its categories as `<20` and `≥20 ng/mL`, with `ng/mL × 2.5` for nmol/L. DOC-001 Figure 4 labels the matched baseline subgroup `<20` and `≥20 ng/mL`. DOC-003 eTable 14 defines low vitamin D as `<20 ng/mL`.
- **Reproducible rule and calculation:** The same analyte and threshold in the same randomized baseline cohort should retain its concentration unit across matched descriptions. The printed unit differs: `mg/mL` versus `ng/mL`. As a dimensional diagnostic, `1 mg = 1,000,000 ng`, so literal `20 mg/mL = 20,000,000 ng/mL`; it is not the same threshold as `20 ng/mL`. No rounding rule can reconcile a unit difference.
- **Direct observation:** The p. 6 narrative prints `20 mg/mL`; the matched table, figure, and supplement definitions print `20 ng/mL`.
- **Inference:** The isolated unit may be a label or transcription error, but the supplied package does not state the intended replacement or its production mechanism.
- **Source-grounded alternatives:** The narrative could refer to a different unstated analytic unit, but the same sentence gives a 31.1 `ng/mL` mean and no alternative conversion or threshold definition is supplied. A typesetting error is possible but not established.
- **Checker provenance:** `checkers/numeric_consistency.md`, Proposition 1; `checkers/statistical_pass_1.md`, directly confirmed cross-lane referral; `checkers/cross_source_consistency.md`, Vitamin-D concentration unit proposition.
- **Exact human question:** Does the printed `20 mg/mL` on DOC-001 PDF p. 6 require correction or clarification, and what unit was intended for that threshold?
- **Status:** Pending Human Adjudication.

## C002 — Protocol ICD-9-code prose cites Table 3 while the code list is Table 1

- **Category:** Measure, label, or scale inconsistency.
- **Exact PDF locations:** [DOC-002 protocol — PDF p. 18](<../../joi200066supp1_prod.pdf#page=18>), ICD-9-code paragraph and immediately following table; [DOC-002 protocol — PDF p. 23](<../../joi200066supp1_prod.pdf#page=23>), Table 3.
- **Source evidence:** DOC-002 p. 18 states: “ICD-9 codes will be used to identify depression (Table 3).” The table directly following that sentence is captioned “Table 1. ICD-9 Codes Identifying Relevant Depressive Disorders.”
- **Comparator evidence:** DOC-002 p. 23 contains the separately numbered “Table 3,” a recurrent-depression power table rather than an ICD-9 code list.
- **Reproducible rule and calculation:** A textual locator for the ICD-9 code list should identify the displayed table containing that list. The direct comparison is `Table 3 ≠ Table 1`; no numerical rounding or tolerance applies. The p. 23 Table 3 cannot be the code-list target because its contents are power percentages by assumed risk ratio.
- **Direct observation:** The code-list prose uses `Table 3`; the adjacent code-list caption uses `Table 1`; the actual Table 3 has a different topic.
- **Inference:** The prose locator may be stale after renumbering, or another version may have used a different number. The supplied package does not establish which printed field was intended to change.
- **Source-grounded alternatives:** The locator could be inherited from a prior protocol version; the adjacent caption could have been renumbered without updating prose. No supplied intervening or appended ICD-9 table numbered Table 3 was identified.
- **Checker provenance:** `checkers/numeric_consistency.md`, Proposition 2; `checkers/statistical_pass_1.md`, directly confirmed cross-lane referral; `checkers/cross_source_consistency.md`, Incorrect protocol table locator proposition.
- **Exact human question:** Which table number was intended for the ICD-9 code-list reference on DOC-002 PDF p. 18, and does the authoritative protocol version contain an omitted code-list table numbered Table 3?
- **Status:** Pending Human Adjudication.

## C003 — Supplementary depression-risk subgroup narrative refers to main Figure 3, but its printed values match main Figure 4

- **Category:** Cross-document numeric inconsistency.
- **Exact PDF locations:** [DOC-003 Supplement 2 — PDF p. 13](<../../joi200066supp2_prod.pdf#page=13>), “Description of Results from Sub-Group Analyses in Figure 3 and eTable 2”; [DOC-001 main article — PDF p. 8](<../../jama_okereke_2020_oi_200066.pdf#page=8>), Figure 4; [DOC-001 main article — PDF p. 7](<../../jama_okereke_2020_oi_200066.pdf#page=7>), Figure 3.
- **Source evidence:** DOC-003 p. 13 says there were no treatment-by-subgroup interactions “(main Figure 3)” and prints depression-risk subgroup results: women `p-interaction=0.10`; normal versus higher BMI `p-interaction=0.06`; baseline vitamin-D use `HR=0.87 (95% CI: 0.73-1.04)`; and baseline 25(OH)D `≥20 ng/ml HR=0.89 (95% CI: 0.77-1.04)`.
- **Comparator evidence:** DOC-001 Figure 4 prints those same depression-risk subgroup P values and hazard ratios at the displayed precision. DOC-001 Figure 3 is a crude PHQ-8 score-distribution figure and does not print the cited hazard ratios or interaction P values.
- **Reproducible rule and calculation:** For a figure locator to be a matched comparator, population, outcome, contrast, subgroup, measure, and displayed precision must agree. The DOC-003 values match DOC-001 Figure 4 exactly: `.10`, `.06`, `0.87 (0.73-1.04)`, and `0.89 (0.77-1.04)`. They do not appear in Figure 3. Thus the p. 13 numerical narrative identifies a figure inconsistent with its matched values.
- **Direct observation:** DOC-003 prints “main Figure 3” and the listed subgroup values; DOC-001 Figure 4 prints the values, whereas Figure 3 does not.
- **Inference:** “Figure 3” may be a cross-reference or retained-heading error. The supplied files do not establish whether the narrative parenthetical, heading, or figure numbering was intended to differ.
- **Source-grounded alternatives:** A prior main-article layout could have numbered the depression-risk graphic as Figure 3, but no such version is supplied. The current supplied main article has the matching values only in Figure 4.
- **Checker provenance:** `checkers/cross_source_consistency.md`, Supplementary narrative figure-locator proposition. The numeric and statistical checkers found no distinct duplicate of this cross-document locator issue.
- **Exact human question:** Should the DOC-003 p. 13 reference and/or heading identify Figure 4 in the supplied main article, or was another authoritative figure-numbering version intended?
- **Status:** Pending Human Adjudication.

## Registration summary

- **Registered distinct candidates:** 3.
- **Stable IDs:** C001, C002, C003.
- **Candidate cap:** None.
- **Display-zero P candidate:** None.
