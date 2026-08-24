# Stable Candidate Ledger

All entries are quantitative quality-control candidates and remain **Pending Human Adjudication**. Stable IDs were assigned only after merging genuine duplicates across the numeric, cross-source, and statistical checker lanes. No candidate-count limit was applied.

## C001 — Person-day totals do not reconcile with stated mean follow-up days

- **Category:** Denominator, proportion, or total inconsistency
- **Relationships and provenance:** N010; `NC-N010-01`
- **Exact source:** [jama_butler_2020_oi_200054.pdf — PDF p. 4](<../../jama_butler_2020_oi_200054.pdf#page=4>)
- **Printed evidence:** 39,798 probiotic person-days with mean 252.4 days; 37,974 placebo person-days with mean 242.9 days; 155 randomized per arm and primary-analysis counts 152/153 are also printed.
- **Consistency rule:** A total and a mean must reconcile under the stated population denominator. Neither 155/155 nor 152/153 reproduces the means: 39,798/155=256.8 and 37,974/155=245.0; 39,798/152=261.8 and 37,974/153=248.2.
- **Alternative source-grounded interpretation:** The means may use an unstated filtered participant/day population that differs from both printed denominator sets.
- **Human question:** Which participants and day records define each mean, and which printed total, mean, or population label is intended?
- **Status:** Pending Human Adjudication

## C002 — Administration-method percentage conflicts with its printed fraction

- **Category:** Denominator, proportion, or total inconsistency
- **Relationships and provenance:** N011; `NC-N011-01`
- **Exact source:** [jama_butler_2020_oi_200054.pdf — PDF p. 4](<../../jama_butler_2020_oi_200054.pdf#page=4>)
- **Printed evidence:** The intervention-fidelity paragraph reports 89.4% (68,356/73,302) swallowed as capsules or sprinkled on food.
- **Consistency rule:** 68,356/73,302 × 100 = 93.2526%, which rounds to 93.3%, not 89.4%. The three printed route counts sum to 73,302.
- **Alternative source-grounded interpretation:** A different denominator may have generated 89.4%, but the printed parenthetical fraction supplies 73,302.
- **Human question:** Is the percentage, numerator, or stated denominator the intended administration-method value?
- **Status:** Pending Human Adjudication

## C003 — Adherence median is below its IQR and conflicts across main and supplement

- **Category:** Cross-document numeric inconsistency
- **Relationships and provenance:** N011, N059, S080; merged `NC-N011-02` and `XSC-001`
- **Exact sources:** [jama_butler_2020_oi_200054.pdf — PDF p. 4](<../../jama_butler_2020_oi_200054.pdf#page=4>); [joi200054supp2_prod.pdf — PDF p. 5](<../../joi200054supp2_prod.pdf#page=5>)
- **Printed evidence:** Main text: median 93.3%, IQR 93.56%-99.45%. Supplement: median 97.8%, IQR 93.56%-99.45%.
- **Consistency rule:** A conventional median cannot be below the lower quartile. The main median remains below 93.56% under printed rounding, while the supplement median is within the identical IQR; the medians differ by 4.5 percentage points.
- **Alternative source-grounded interpretation:** The locations may use unreported distinct analysis subsets or adherence derivations despite near-identical wording and identical IQR endpoints.
- **Human question:** Which median and analysis population are intended for the pooled full-or-partial-dose adherence summary?
- **Status:** Pending Human Adjudication

## C004 — Nonprophylactic-antibiotic percentages conflict with printed counts and denominators

- **Category:** Denominator, proportion, or total inconsistency
- **Relationships and provenance:** N014; `NC-N014-01`
- **Exact sources:** [jama_butler_2020_oi_200054.pdf — PDF p. 5](<../../jama_butler_2020_oi_200054.pdf#page=5>); [jama_butler_2020_oi_200054.pdf — PDF p. 4](<../../jama_butler_2020_oi_200054.pdf#page=4>) for the alternate 152/153 and overall 305 denominator context
- **Printed evidence:** Overall 202 (66.2%); probiotic 63.4% (97/155); placebo 69.1% (105/155).
- **Consistency rule:** 97/155=62.6%, 105/155=67.7%, and 202/310=65.2% to one decimal, while 97+105=202.
- **Alternative source-grounded interpretation:** Arm percentages match alternate denominators 153 and 152 approximately, suggesting outcome-data denominators, but those are not the printed fraction denominators and do not alone define the overall 66.2%.
- **Human question:** Which denominators support the three percentages, and should the fractions or percentages be relabeled?
- **Status:** Pending Human Adjudication

## C005 — Three-month oral-candidiasis ARD conflicts with printed proportions and supplement

- **Category:** Cross-document numeric inconsistency
- **Relationships and provenance:** N041, N068, S042, S088; `NC-N041-01`
- **Exact sources:** [jama_butler_2020_oi_200054.pdf — PDF p. 7](<../../jama_butler_2020_oi_200054.pdf#page=7>); [joi200054supp2_prod.pdf — PDF p. 8](<../../joi200054supp2_prod.pdf#page=8>)
- **Printed evidence:** Main text gives 88/113 (77.9%) versus 80/105 (76.2%) and ARD -0.2% (-11.3% to 10.9%). The supplement repeats the fractions and prints difference 0.02 (-0.10 to 0.13).
- **Consistency rule:** The fractions differ by +1.6856 percentage points in probiotic-minus-placebo order (or -1.6856 in reverse), neither of which rounds to -0.2%; +0.02 as a proportion is compatible with the fractions.
- **Alternative source-grounded interpretation:** The main ARD might be an adjusted estimator, but neither cited location labels it adjusted or defines a different estimator.
- **Human question:** Does -0.2% represent an unstated adjusted estimator, or which difference is intended for this matched result?
- **Status:** Pending Human Adjudication

## C006 — Matched B animalis interval has two different lower endpoints

- **Category:** Cross-document numeric inconsistency
- **Relationships and provenance:** S004, S085; `STAT-P1-001`
- **Exact sources:** [jama_butler_2020_oi_200054.pdf — PDF p. 5](<../../jama_butler_2020_oi_200054.pdf#page=5>); [joi200054supp2_prod.pdf — PDF p. 8](<../../joi200054supp2_prod.pdf#page=8>)
- **Printed evidence:** For the same 29/56 versus 2/52 three-month result, the main article prints adjusted OR 26.90 (95% CI 5.94-121.66), while eTable 5 prints 26.9 (95% CI 5.95-121.66).
- **Consistency rule:** Two different two-decimal lower endpoints cannot both be the same rounded value; point-estimate trailing precision and the upper endpoint otherwise match.
- **Alternative source-grounded interpretation:** The two locations may derive from different output versions or unrounded calculations not supplied in the package.
- **Human question:** Which lower endpoint is intended, and does a documented version difference explain 5.94 versus 5.95?
- **Status:** Pending Human Adjudication

## C007 — eTable 4 percentage does not reproduce from 20/119

- **Category:** Denominator, proportion, or total inconsistency
- **Relationships and provenance:** N061, S082; `STAT-P1-002`
- **Exact source:** [joi200054supp2_prod.pdf — PDF p. 7](<../../joi200054supp2_prod.pdf#page=7>), eTable 4 placebo group at three months, (+) category
- **Printed evidence:** The cell prints 20/119 (16.0).
- **Consistency rule:** 20/119 × 100 = 16.8067%, which rounds to 16.8%, not 16.0%. Across the four placebo three-month categories, numerators sum to 20+20+38+42=120 against the common printed denominator 119, while displayed percentages sum to 16.8+16.0+31.9+35.3=100.0%; this corroborates a repeated-cell inconsistency without identifying which element is intended.
- **Alternative source-grounded interpretation:** The percentage may use an unreported denominator specific to the cell, or one of the three printed elements may be a transcription defect.
- **Human question:** Which numerator, denominator, or percentage is intended for that cell?
- **Status:** Pending Human Adjudication

## C008 — CACE coefficient, confidence interval, and P value need reconciliation

- **Category:** Statistical reporting inconsistency
- **Relationships and provenance:** S069, S074, S080; `STAT-P1-003`
- **Exact sources:** [joi200054supp2_prod.pdf — PDF p. 3](<../../joi200054supp2_prod.pdf#page=3>); [joi200054supp2_prod.pdf — PDF p. 5](<../../joi200054supp2_prod.pdf#page=5>); [joi200054supp1_prod.pdf — PDF p. 52](<../../joi200054supp1_prod.pdf#page=52>)
- **Printed evidence:** The stated 2SLS CACE model multiplies coefficient and CI by 100 for presentation; eTable 2 prints adjusted coefficient 0.01, 95% CI -0.20 to 0.41, P=.52; the SAP states two-sided 95% inference.
- **Consistency rule:** The interval midpoint is 0.105, not 0.01, and endpoint distances from the point estimate are 0.21 and 0.40. Conditional on a symmetric Wald interval on the displayed coefficient scale, the interval and P value do not reproduce from the point estimate.
- **Alternative source-grounded interpretation:** A non-Wald interval, finite-sample method, transformation, different unrounded coefficient, or separately constructed P value may explain asymmetry; the package does not state CI construction or test degrees of freedom.
- **Human question:** Which point estimate, endpoint, scale multiplier, CI construction, or P-value method accounts for the printed combination?
- **Status:** Pending Human Adjudication

## Merge and registration record

- Registered stable IDs: C001, C002, C003, C004, C005, C006, C007, C008.
- Genuine duplicate merged before stable IDs: `NC-N011-02` and `XSC-001` concerned the same adherence medians, identical IQR, comparator, and ordering/cross-source rule; their provenance is retained in C003.
- No other proposals shared the same printed values, comparator, and consistency rule.
- Stable IDs must not be deleted, renumbered, or merged after this point.
