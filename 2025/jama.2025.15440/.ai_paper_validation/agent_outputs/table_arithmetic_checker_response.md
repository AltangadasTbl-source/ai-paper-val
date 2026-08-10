# Table Arithmetic Check - doc_001_main_article and doc_004_results_supplement

## Scope

Checked only the result-relevant tables identified in the package manifest and supplementary evidence map:

- `jama_wijesurendra_2025_oi_250068_1760999665.28362.pdf`, PDF p. 5: **Table. Baseline Characteristics of the Randomized Population**.
- `joi250068supp3_prod_1760999665.30362.pdf`, PDF p. 4: **eTable 1. Patch usage metrics**.
- `joi250068supp3_prod_1760999665.30362.pdf`, PDF pp. 5-6: **eTable 2. Baseline characteristics by patch ECG data availability**.
- `joi250068supp3_prod_1760999665.30362.pdf`, PDF p. 7: **eTable 3. Patch-detected conditions**.

No protocol, SAP, administrative content, or figures were audited. Source values were checked against the retained native text and rendered table pages.

## Retained candidate findings

None. No document-verifiable arithmetic or internal-consistency candidate was identified.

## Completed checks

- Main Table: each displayed mutually exclusive baseline-category total equals its column denominator of 2520: age (683 + 1032 + 805; 683 + 1061 + 776), sex (1340 + 1180 in each group), race/ethnicity including missing (2520 in each group), BMI including missing (2520 in each group), and CHA2DS2-VASc (2520 in each group). Displayed percentages agree with the count/2520 ratios to one decimal place.
- eTable 1: patch flow is 2126 + 188 + 206 = 2520; worn-duration groups are 1960 + 166 = 2126; removal reasons are 43 + 18 + 8 + 97 = 166. The related percentages match their stated denominators after rounding.
- eTable 2: patch-data and no-data counts sum to the displayed row total for every checked categorical row. The age, sex, BMI, and CHA2DS2-VASc category counts also sum to 2126 and 394 in their respective columns. Displayed row percentages agree with the stated within-row denominators after rounding.
- eTable 3: every displayed percentage agrees with its count divided by 2520 or 2126 after rounding. The AF subtypes add to the AF total: 74 + 15 = 89.

## Rejected or uncertain candidates

None. Potential overlaps among separately listed clinical conditions are not labelled as mutually exclusive; treating them as additive would require an unsupported assumption.

