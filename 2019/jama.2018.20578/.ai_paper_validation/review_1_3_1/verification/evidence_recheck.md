# Mechanical Evidence Recheck

## Scope and method

- Stable IDs rechecked: `C001`, `C002`, `C003`, `C004`, `C005`, `C006`, `C007`, `C008`, `C009`, `C010`, `C011`, `C012`, `C013`, `C014`, `C015`, `C016`, `C017`, `C018`, `C019`, `C020`, `C021`, `C022`, `C023`, and `C024` (24 IDs).
- Each cited location was reopened in the supplied PDF. Direct PDF text extraction was used for text and tables; the source PDF page was rendered for the unlabeled eFigure 2 boundary and the image-based forest plots. Reused evidence assets were not treated as authority.
- This artifact records mechanical facts and unresolved source definitions only. It does not delete or merge any stable ID and does not assign an AI disposition.
- Status of every ID: **Pending Human Adjudication**.

## C001 — HbA1c narrative and Table 4 use different units

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-001 p. 1, abstract Results](../../../jama_flint_2019_oi_190079.pdf#page=1); [DOC-001 p. 7, Results](../../../jama_flint_2019_oi_190079.pdf#page=7); [DOC-001 p. 8, Table 4](../../../jama_flint_2019_oi_190079.pdf#page=8).
- **Source fact matched:** The abstract and Results both print the HbA1c daily-rate estimate as `-0.0002 mg/dL` with 95% CI `-0.0021 to 0.0016`.
- **Comparator matched:** Table 4 labels the analyte `HbA1c, %` and displays HbA1c levels on that scale; neighboring narrative lipid and glucose outcomes use `mg/dL`.
- **Rule applicable:** A matched analyte and coefficient require a consistent unit unless a conversion or a separately defined model scale is supplied.
- **Reproduced calculation or logical comparison:** Direct unit comparison gives `mg/dL` versus `%`; these are not the same unit, and no HbA1c conversion is printed in the package.
- **Inputs available or missing definitions:** The estimate, interval, analyte, narrative unit, and table unit are available. The coefficient's analysis-data unit and any conversion are missing.
- **Source-grounded alternatives:** The Table 4 percent scale may be intended for the coefficient, or the model may use another unstated HbA1c scale.
- **Direct observation versus inference:** Both competing unit labels are direct observations. A copy-forward from adjacent `mg/dL` outcomes is an inferred production explanation.
- **Exact human question:** What unit should accompany the HbA1c treatment-by-time estimate and interval: percentage points per day, `mg/dL`, or another explicitly defined scale?

## C002 — The UKU rule permits a value above the printed maximum

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-001 p. 4, adverse-effect definition](../../../jama_flint_2019_oi_190079.pdf#page=4).
- **Source fact matched:** The UKU scale is printed as `0-3` on each of 48 items.
- **Comparator matched:** In the same paragraph, an adverse effect may be present with a score of `3 or 4` plus an increase from baseline.
- **Rule applicable:** A permitted item value cannot exceed the stated item maximum without a special-code or recoding definition.
- **Reproduced calculation or logical comparison:** The printed set is `{0,1,2,3}` and `4 > 3`; therefore 4 is outside the stated range.
- **Inputs available or missing definitions:** The item range and operational threshold are available. Any special value 4, alternative UKU version, or recoding rule is missing.
- **Source-grounded alternatives:** Score 4 may be a special or recoded value not described on the page; alternatively, either the range or threshold may contain a transcription issue.
- **Direct observation versus inference:** The range and threshold are direct observations. The possible coding explanation is inference.
- **Exact human question:** Should the presence rule say score 3 only, or should the printed UKU range or special coding be expanded and defined?

## C003 — Placebo living-arrangement categories omit two participants

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-001 p. 5, Table 1](../../../jama_flint_2019_oi_190079.pdf#page=5).
- **Source fact matched:** The placebo column header is `n = 62`; the living-arrangement rows are with others `49 (79.0)`, alone `10 (16.1)`, and senior residence `1 (1.6)`.
- **Comparator matched:** The three displayed living-arrangement categories are presented as the full category block, with no missing or other row and no row-specific denominator.
- **Rule applicable:** Mutually exclusive exhaustive categories should sum to the displayed row denominator and approximately 100% after rounding.
- **Reproduced calculation or logical comparison:** `49 + 10 + 1 = 60`, leaving 2 of 62 unaccounted for; `79.0 + 16.1 + 1.6 = 96.7%`, leaving 3.3 percentage points.
- **Inputs available or missing definitions:** Arm total and all three displayed cells are available. The row denominator, missingness count, and any additional category are missing.
- **Source-grounded alternatives:** The row may intentionally describe 60 respondents, but Table 1 does not print `n = 60` for this block even though reduced denominators are shown elsewhere.
- **Direct observation versus inference:** The header, categories, and arithmetic gap are direct observations. Interpreting the two participants as missing is inference.
- **Exact human question:** Were two placebo participants missing living-arrangement data, and if so should the row denominator or missingness be printed?

## C004 — Hyperlipidemia percentages reproduce opposite-arm denominators

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-001 p. 5, Table 1](../../../jama_flint_2019_oi_190079.pdf#page=5).
- **Source fact matched:** Arm headers are olanzapine `n = 64` and placebo `n = 62`; hyperlipidemia cells are `18 (29.0)` and `19 (29.7)`, respectively.
- **Comparator matched:** The printed percentages match division by the opposite arm totals rather than their own column headers.
- **Rule applicable:** A count-percent cell should use its own arm denominator unless a different row denominator is stated.
- **Reproduced calculation or logical comparison:** `100*18/64 = 28.125%` and `100*19/62 = 30.645%`, ordinarily 28.1% and 30.6%. In contrast, `100*18/62 = 29.032%` and `100*19/64 = 29.688%`, reproducing 29.0% and 29.7%.
- **Inputs available or missing definitions:** Both counts and arm totals are available. Any row-specific denominator or missingness convention is absent; a placebo denominator of 64 would exceed its arm total.
- **Source-grounded alternatives:** Different row denominators could theoretically apply, but none is printed and the exact opposite-arm match remains.
- **Direct observation versus inference:** Counts, percentages, and headers are direct observations. Denominator transposition is an inferred explanation.
- **Exact human question:** Are the percentages transposed, or should different row denominators be supplied?

## C005 — Barnes participant counts are decimal-formatted

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-001 p. 6, Table 2](../../../jama_flint_2019_oi_190079.pdf#page=6).
- **Source fact matched:** Under `No. (%) of Participants`, Barnes global score greater than 0 is printed as `3.0 (4.7)` and `2.0 (3.2)`.
- **Comparator matched:** The arm headers are `n = 64` and `n = 62`, and the leading fields function as participant counts.
- **Rule applicable:** Participant counts are discrete integers even when a table-generation format permits trailing decimals.
- **Reproduced calculation or logical comparison:** Interpreting the leading values as counts gives `100*3/64 = 4.6875%` and `100*2/62 = 3.2258%`, reproducing 4.7% and 3.2%.
- **Inputs available or missing definitions:** Header, values, and denominators are available. The source variable type and rendering format are not supplied.
- **Source-grounded alternatives:** `3.0` and `2.0` are numerically equal to integer counts, so this can be representation-only formatting.
- **Direct observation versus inference:** Decimal display under a count header is direct. Inherited continuous-value formatting is inferred.
- **Exact human question:** Should the Barnes participant counts be printed as `3` and `2`?

## C006 — AIMS participant counts are decimal-formatted

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-001 p. 6, Table 2](../../../jama_flint_2019_oi_190079.pdf#page=6).
- **Source fact matched:** Under `No. (%) of Participants`, AIMS overall severity score greater than 0 is printed as `2.0 (3.1)` and `2.0 (3.2)`.
- **Comparator matched:** The arm headers are `n = 64` and `n = 62`, and the leading fields function as participant counts.
- **Rule applicable:** Participant counts are discrete integers.
- **Reproduced calculation or logical comparison:** `100*2/64 = 3.125%` and `100*2/62 = 3.2258%`, reproducing 3.1% and 3.2% when the leading values are read as count 2.
- **Inputs available or missing definitions:** Header, values, and denominators are available. The table-source variable type and formatting rule are missing.
- **Source-grounded alternatives:** Decimal `2.0` is numerically equal to integer 2, so the issue can be limited to representation.
- **Direct observation versus inference:** Decimal-formatted cells under the count header are direct. A shared formatting mechanism with the Barnes row is inferred.
- **Exact human question:** Should both AIMS participant counts be printed as `2`?

## C007 — Relapse-hospitalization percentage is on a rounding boundary

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-001 p. 8, Results](../../../jama_flint_2019_oi_190079.pdf#page=8).
- **Source fact matched:** The narrative prints `11 (32.3%) of 34` placebo-group relapses requiring psychiatric hospitalization.
- **Comparator matched:** The exact numerator-denominator fraction is available in the same sentence.
- **Rule applicable:** Under ordinary nearest one-decimal rounding, the exact percentage should round from the stated fraction.
- **Reproduced calculation or logical comparison:** `100*11/34 = 32.352941...%`, ordinarily displayed as 32.4%, not 32.3%. The exact value is only 0.00294 percentage point above 32.35%, the upper edge for a nearest-rounding display of 32.3%.
- **Inputs available or missing definitions:** Numerator and denominator are available. The percentage display convention is not stated.
- **Source-grounded alternatives:** Truncation to one decimal produces 32.3%; an unprinted alternative denominator is also possible but is not suggested by the sentence.
- **Direct observation versus inference:** All three printed values and the arithmetic are direct. Truncation is inferred.
- **Exact human question:** Was 32.3% intentionally truncated, or should the printed percentage be 32.4%?

## C008 — Total-cholesterol absolute difference does not reproduce

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-001 p. 9, Table 5](../../../jama_flint_2019_oi_190079.pdf#page=9).
- **Source fact matched:** Total cholesterol is printed as `9 (14.1)` of 64 versus `6 (9.7)` of 62 with absolute unadjusted difference `4.3` percentage points.
- **Comparator matched:** Both exact arm counts and denominators, as well as rounded percentages, are printed in the row.
- **Rule applicable:** The absolute unadjusted difference should equal the difference in arm risks on the percentage-point scale.
- **Reproduced calculation or logical comparison:** `100*(9/64 - 6/62) = 4.3850806`, ordinarily 4.4 at one decimal; the displayed percentages also give `14.1 - 9.7 = 4.4`.
- **Inputs available or missing definitions:** Counts, arm totals, and the column definition are available. No alternate row denominator or computation is supplied.
- **Source-grounded alternatives:** A different unprinted denominator or nonstandard display rule could produce another value, but neither is defined.
- **Direct observation versus inference:** Printed counts, denominators, and difference are direct. A one-tenth rounding or transcription mechanism is inferred.
- **Exact human question:** What computation or denominator produced 4.3 percentage points, or should it be 4.4?

## C009 — LDL absolute difference does not reproduce

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-001 p. 9, Table 5](../../../jama_flint_2019_oi_190079.pdf#page=9).
- **Source fact matched:** LDL is printed as `9 (14.1)` of 64 versus `6 (9.7)` of 62 with absolute unadjusted difference `4.3` percentage points.
- **Comparator matched:** The LDL row independently supplies the same exact arm counts, denominators, and rounded percentages.
- **Rule applicable:** The absolute unadjusted difference should equal the difference in arm risks.
- **Reproduced calculation or logical comparison:** `100*(9/64 - 6/62) = 4.3850806`, ordinarily 4.4; `14.1 - 9.7 = 4.4` as well.
- **Inputs available or missing definitions:** Counts, totals, and column definition are available. A different LDL-specific denominator or rule is not printed.
- **Source-grounded alternatives:** An unreported computation remains possible, but the displayed row does not identify one.
- **Direct observation versus inference:** The separate LDL row and mismatch are direct observations. A repeated production mechanism shared with total cholesterol is inferred.
- **Exact human question:** What computation produced the LDL value 4.3, or should it be 4.4?

## C010 — Total-cholesterol and LDL result vectors are exact duplicates

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-001 p. 9, Table 5](../../../jama_flint_2019_oi_190079.pdf#page=9).
- **Source fact matched:** The total-cholesterol definition uses a 240 `mg/dL` threshold and the LDL definition uses 160 `mg/dL`.
- **Comparator matched:** Both distinct rows print the complete vector `9 (14.1)`, `6 (9.7)`, `4.3`, and 95% CI `-8 to 17.2`.
- **Rule applicable:** Exact duplication across separately defined outcomes is a reproducible cross-row identity check; it does not by itself establish that either row is wrong.
- **Reproduced calculation or logical comparison:** All four displayed result fields are equal field by field despite the different analyte thresholds.
- **Inputs available or missing definitions:** Thresholds and displayed results are available. Participant identities, raw outcome flags, unrounded interval inputs, and table-generation code are missing.
- **Source-grounded alternatives:** The same 9 and 6 participants may genuinely meet both threshold definitions and yield identical intervals.
- **Direct observation versus inference:** The duplicate vectors and distinct definitions are direct. A copied row is inferred and not established.
- **Exact human question:** Did the same participants satisfy both definitions with the same interval, or was one row duplicated during production?

## C011 — Protocol ARD subtraction order conflicts with its sign rule

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-002 p. 6, statistical analysis](../../../joi180151supp1_prod.pdf#page=6); [DOC-003 p. 4, ARD method](../../../joi180151supp2_prod.pdf#page=4).
- **Source fact matched:** DOC-002 states that RR and its interval are multiplied by the placebo event rate, “which is then subtracted from the placebo risk,” and then says negative values favor aspirin.
- **Comparator matched:** DOC-003 likewise states that negative ARD values indicate reduced risk with aspirin.
- **Rule applicable:** The sign produced by the written subtraction must agree with the stated direction interpretation.
- **Reproduced calculation or logical comparison:** With no-aspirin risk `R0` and beneficial `RR < 1`, literal `R0 - RR*R0 = R0(1-RR) > 0`; the negative-favors-aspirin rule instead requires `RR*R0 - R0 = R0(RR-1) < 0`.
- **Inputs available or missing definitions:** The prose operation and sign interpretation are available. Exact operand order in code and the intended grammatical referent are missing.
- **Source-grounded alternatives:** The phrase may have intended the placebo risk to be subtracted from the estimated aspirin risk even though its grammar reads oppositely.
- **Direct observation versus inference:** Wording and sign statements are direct. Reversed prose operand order is an inferred explanation.
- **Exact human question:** Which subtraction order was intended and implemented for ARD calculation?

## C012 — Incident-cancer model label conflicts with the displayed selection rule

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-003 p. 4, model-selection rule](../../../joi180151supp2_prod.pdf#page=4); [DOC-003 p. 5, incident-cancer row](../../../joi180151supp2_prod.pdf#page=5).
- **Source fact matched:** The rule uses the lower DIC if the DIC difference is greater than 3; within 3, random effects are favored if fixed-effect `I2 >25%`.
- **Comparator matched:** The all-patient incident-cancer row prints fixed DIC `27.06`, random DIC `27.93`, `I2 = 25%`, and model `random`.
- **Rule applicable:** The displayed row can be evaluated under the exact printed branch condition.
- **Reproduced calculation or logical comparison:** `|27.06 - 27.93| = 0.87 < 3`, so the heterogeneity branch applies. Displayed `25%` does not satisfy the strict inequality `>25%`; at displayed precision the rule leads to fixed, unlike the printed random label.
- **Inputs available or missing definitions:** Displayed DICs, I2, rule, and label are available. Unrounded I2, whether the implemented threshold was inclusive, and actual code are missing.
- **Source-grounded alternatives:** Unrounded I2 may exceed 25%, or the implemented rule may be `>=25%` despite the printed strict inequality.
- **Direct observation versus inference:** Rule, row values, and selected label are direct. Hidden precision or an intended inclusive threshold is inferred.
- **Exact human question:** Was selection based on an unrounded I2 above 25%, was the intended threshold inclusive, or should the selected-model label be changed?

## C013 — eTable 3 does not state the ARD display scale

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-002 p. 6, protocol ARD rule](../../../joi180151supp1_prod.pdf#page=6); [DOC-003 p. 4, ARD and NNT/NNH method](../../../joi180151supp2_prod.pdf#page=4); [DOC-003 p. 15, eTable 3](../../../joi180151supp2_prod.pdf#page=15).
- **Source fact matched:** The methods define ARD direction and say NNT/NNH are calculated for significant changes, but they do not print a display unit. eTable 3 labels values only as `ARD`.
- **Comparator matched:** Examples include composite all-patient ARD `-0.41` with NNT `242` and major-bleeding ARD `0.47` with NNH `210`.
- **Rule applicable:** A displayed risk difference needs an explicit proportion or percentage-point scale to support reciprocal NNT/NNH interpretation.
- **Reproduced calculation or logical comparison:** If 0.41 is a proportion, `1/0.41 = 2.44`; if it is 0.41 percentage point, `100/0.41 = 243.90`, near 242 with hidden precision. For 0.47, the corresponding reciprocals are 2.13 versus 212.77. The NNT/NNH magnitudes imply percentage points, but the table does not state that scale.
- **Inputs available or missing definitions:** Printed ARDs, NNT/NNH values, and sign direction are available. Explicit ARD unit, unrounded ARDs, reciprocal convention, and integer-rounding rule are missing.
- **Source-grounded alternatives:** Percentage points may be an intended convention; another scale is possible only if separately defined, which this package does not do.
- **Direct observation versus inference:** Omission of a unit and all printed values are direct. Inferring percentage points from reciprocals is diagnostic reasoning.
- **Exact human question:** What is the explicit unit or scale of every ARD in eTable 3, and should the table label the values as percentage points or another stated scale?

## C014 — All-patient major-bleeding ARD and NNH do not reconcile at displayed precision

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-003 p. 4, NNT/NNH method](../../../joi180151supp2_prod.pdf#page=4); [DOC-003 p. 15, eTable 3](../../../joi180151supp2_prod.pdf#page=15).
- **Source fact matched:** The all-patient major-bleeding row prints ARD `0.47 (0.34 to 0.62)` and NNH `210`.
- **Comparator matched:** The methods identify NNH as the reciprocal summary for significant increased risk; the table context implies a percentage-point ARD scale.
- **Rule applicable:** If both fields summarize the same unrounded absolute risk difference, their displayed-precision intervals should contain a common value under the stated reciprocal relationship.
- **Reproduced calculation or logical comparison:** `100/0.47 = 212.77`; NNH 210 implies `100/210 = 0.47619`, ordinarily displayed as 0.48. A nearest-rounded ARD of 0.47 lies in `[0.465,0.475)`, which excludes 0.47619.
- **Inputs available or missing definitions:** Displayed ARD and NNH are available. The unrounded effect, NNH integer-rounding convention, and confirmation that both use the same estimand are missing.
- **Source-grounded alternatives:** NNH may use a separately calculated absolute contrast, nonstandard rounding, or more precise input not represented by the ARD cell.
- **Direct observation versus inference:** The printed pair and nonoverlap under ordinary rounding are direct mechanical facts. A separate estimand or transcription mechanism is inferred.
- **Exact human question:** Which unrounded ARD, estimand, and reciprocal convention produced the pair 0.47 and 210?

## C015 — High-risk major-bleeding ARD and NNH do not reconcile

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-003 p. 4, NNT/NNH method](../../../joi180151supp2_prod.pdf#page=4); [DOC-003 p. 15, eTable 3](../../../joi180151supp2_prod.pdf#page=15).
- **Source fact matched:** The high-risk major-bleeding row prints ARD `0.64 (0.35 to 0.97)` and NNH `152`.
- **Comparator matched:** NNH is presented as the reciprocal summary for the same significant increased-risk row.
- **Rule applicable:** The displayed ARD precision and NNH should be compatible if based on the same unrounded percentage-point risk difference.
- **Reproduced calculation or logical comparison:** `100/0.64 = 156.25`; NNH 152 implies `100/152 = 0.65789`, ordinarily 0.66. The implied value is outside the nearest-rounding interval `[0.635,0.645)` for 0.64.
- **Inputs available or missing definitions:** Displayed ARD and NNH are available. Unrounded ARD, exact NNH convention, and estimand identity are missing.
- **Source-grounded alternatives:** NNH may be based on a separately modeled contrast not represented by the displayed ARD, but the source does not state that.
- **Direct observation versus inference:** The pair and reciprocal mismatch are direct mechanical facts. A hidden separate effect or transcription is inference.
- **Exact human question:** What unrounded value, estimand, or alternative rule produced NNH 152?

## C016 — Diabetes major-bleeding ARD and NNH do not reconcile

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-003 p. 4, NNT/NNH method](../../../joi180151supp2_prod.pdf#page=4); [DOC-003 p. 15, eTable 3](../../../joi180151supp2_prod.pdf#page=15).
- **Source fact matched:** The diabetes major-bleeding row prints ARD `0.80 (0.29 to 1.39)` and NNH `121`.
- **Comparator matched:** NNH is displayed alongside the significant increased-risk ARD.
- **Rule applicable:** The two fields should be compatible under a common unrounded percentage-point risk difference and reciprocal convention.
- **Reproduced calculation or logical comparison:** `100/0.80 = 125`; NNH 121 implies `100/121 = 0.82645`, ordinarily 0.83. The implied value lies outside `[0.795,0.805)`, the nearest-rounding interval for displayed 0.80.
- **Inputs available or missing definitions:** Displayed ARD and NNH are available. Unrounded ARD, integer-rounding rule, and proof of a shared estimand are missing.
- **Source-grounded alternatives:** A separately modeled NNH or nonstandard convention could exist, but neither is identified.
- **Direct observation versus inference:** The pair and reciprocal mismatch are direct mechanical facts. A different hidden effect is inferred.
- **Exact human question:** What exact ARD, estimand, and reciprocal convention produced NNH 121?

## C017 — Low- and high-risk stroke events do not sum to all-participant events

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-003 p. 16, eTable 4](../../../joi180151supp2_prod.pdf#page=16).
- **Source fact matched:** Aspirin rows print all `1116/73883`, low risk `752/56212`, and high risk `381/17671`; no-aspirin rows print all `1136/72317`, low risk `788/56354`, and high risk `380/15963`.
- **Comparator matched:** The low- and high-risk denominators exactly partition the all-participant denominators in both arms.
- **Rule applicable:** If low and high risk are exhaustive disjoint subgroups for the displayed all-participant row, both denominators and event counts should add exactly.
- **Reproduced calculation or logical comparison:** Denominators reconcile: `56212 + 17671 = 73883` and `56354 + 15963 = 72317`. Events do not: `752 + 381 = 1133`, 17 above 1116; `788 + 380 = 1168`, 32 above 1136.
- **Inputs available or missing definitions:** All six event counts and denominators are available. Study membership by subgroup, outcome availability, and any nonpartitioning analysis-set definition are missing.
- **Source-grounded alternatives:** Low- and high-risk rows may use different study or outcome availability even though their denominators partition exactly, but no exception is stated in eTable 4.
- **Direct observation versus inference:** All printed values and sums are direct. Different availability or transcription is inferred.
- **Exact human question:** Why do the exact low/high participant partitions not carry an additive total-stroke event partition?

## C018 — Detection-bias table and graph imply different trial counts

- **Status:** Pending Human Adjudication.
- **Location found:** eTable 2 on [DOC-003 p. 10](../../../joi180151supp2_prod.pdf#page=10), [p. 11](../../../joi180151supp2_prod.pdf#page=11), [p. 12](../../../joi180151supp2_prod.pdf#page=12), [p. 13](../../../joi180151supp2_prod.pdf#page=13), and [p. 14](../../../joi180151supp2_prod.pdf#page=14); rendered source [DOC-003 p. 20, eFigure 2](../../../joi180151supp2_prod.pdf#page=20).
- **Source fact matched:** Detection bias is `Unclear` for British Doctors' Study, Physicians' Health Study, Hypertension Optimal Treatment, Women's Health Study, and ASCEND, and `Low` for the other eight trials: 8 low and 5 unclear among 13.
- **Comparator matched:** In eFigure 2, the green detection-bias segment ends at the same approximately 69% position as graph domains representing 9 of 13 low, leaving approximately 31% unclear; it does not end at the approximately 62% position implied by 8 of 13.
- **Rule applicable:** A risk-of-bias summary graph should reproduce the category counts in its detailed table for the same 13 trials and domain.
- **Reproduced calculation or logical comparison:** Table proportions are `8/13 = 61.54%` low and `5/13 = 38.46%` unclear. The displayed boundary corresponds visually to `9/13 = 69.23%` and `4/13 = 30.77%`, a one-trial or 7.69-percentage-point shift.
- **Inputs available or missing definitions:** All 13 table classifications and the rendered graph are available. The graph has no numeric labels, and its underlying input data and exact plotted coordinates are missing.
- **Source-grounded alternatives:** One detailed cell may have been intended as low, or the graph may use another finalized classification set.
- **Direct observation versus inference:** The table classifications and visible graph boundary are direct observations. Translating the unlabeled boundary to exactly 9/4 and proposing a duplicated domain or older input are inferences, although alignment with the other 9/4 bars makes that reading reproducible.
- **Exact human question:** Which detection-bias classification set generated eFigure 2, and which table or graphic reflects the intended final assessment?

## C019 — Egger coefficient and SE do not reproduce the printed t statistic

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-003 p. 21, eFigure 3](../../../joi180151supp2_prod.pdf#page=21).
- **Source fact matched:** The figure prints `Egger Test: -0.47 (standard error: 0.77); t = -0.59, P = 0.57`.
- **Comparator matched:** The named coefficient and standard error are presented with the t statistic in one inferential vector.
- **Rule applicable:** Under the ordinary coefficient-to-standard-error t relationship, `t = coefficient/SE`; displayed-input intervals can test whether rounding alone permits the printed t.
- **Reproduced calculation or logical comparison:** `-0.47/0.77 = -0.61039`, about -0.61. With coefficient magnitude in `[0.465,0.475)` and SE in `[0.765,0.775)`, the possible magnitude ratio is approximately `[0.600,0.621]`, excluding a nearest-rounded 0.59.
- **Inputs available or missing definitions:** Printed coefficient, SE, t, and P are available. Unrounded outputs, degrees of freedom, and the exact Egger implementation or test parameter are missing.
- **Source-grounded alternatives:** The displayed coefficient may not be the numerator used for the displayed t under an unstated implementation; t and P are otherwise mutually plausible for a small residual degrees of freedom.
- **Direct observation versus inference:** All four printed fields and the diagnostic ratio are direct/reproduced. An alternative implementation or field mismatch is inferred.
- **Exact human question:** What unrounded coefficient and SE, or what alternative test definition, produced `t = -0.59`?

## C020 — Twelve non-ASCEND forest rows differ from eTable 4 event totals

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-003 p. 16, eTable 4](../../../joi180151supp2_prod.pdf#page=16); rendered source [DOC-003 p. 24, total-stroke forest plot](../../../joi180151supp2_prod.pdf#page=24); [DOC-002 p. 7, ASCEND protocol change](../../../joi180151supp1_prod.pdf#page=7).
- **Source fact matched:** eTable 4 prints 12 studies with aspirin `1116/73883` and no aspirin `1136/72317`.
- **Comparator matched:** Summing all 13 total-stroke forest rows gives aspirin `1358/81623` and control `1397/80057`; the ASCEND row is `240/7740` versus `263/7740`.
- **Rule applicable:** Removing the explicitly identifiable ASCEND row should reproduce the same 12-study arm totals if table and forest use identical event records.
- **Reproduced calculation or logical comparison:** Denominators reconcile exactly: `81623 - 7740 = 73883` and `80057 - 7740 = 72317`. Events give `1358 - 240 = 1118`, not 1116, and `1397 - 263 = 1134`, not 1136. Relative to eTable 4, the forest has +2 aspirin and -2 control events while preserving the combined event total.
- **Inputs available or missing definitions:** Every forest row, table totals, and ASCEND row are available. The table and plot input datasets, event adjudication versions, and any Bayesian/frequentist analysis-set distinction are missing.
- **Source-grounded alternatives:** Separate event curation or analysis versions could be intentional despite identical study denominators, but no such distinction is stated.
- **Direct observation versus inference:** Printed row values, sums, and two-event arm shift are direct mechanical observations. Arm transposition or data revision is inferred.
- **Exact human question:** Which 12-study arm event totals are intended, and what accounts for the two-event transfer?

## C021 — NNT is printed while the displayed ARD confidence interval reaches zero

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-003 p. 4, NNT/NNH method](../../../joi180151supp2_prod.pdf#page=4); [DOC-003 p. 15, eTable 3](../../../joi180151supp2_prod.pdf#page=15).
- **Source fact matched:** The methods say NNT/NNH are calculated for outcomes with a statistically significant reduction or increase, and the table footnote says they are reported only for statistically significant ARDs.
- **Comparator matched:** Low-risk all myocardial infarction prints ARD `-0.27 (-0.49 to 0.00)` with NNT `366` and no unrounded-endpoint note.
- **Rule applicable:** At displayed precision, a two-sided 95% confidence interval that reaches the null at 0.00 does not visibly exclude zero, whereas the printed reporting rule conditions NNT display on statistical significance.
- **Reproduced calculation or logical comparison:** The displayed interval is `[-0.49, 0.00]`, which includes the null endpoint as printed; nevertheless, NNT 366 is populated.
- **Inputs available or missing definitions:** Reporting rule, displayed ARD interval, and NNT are available. The unrounded upper limit, significance flag, sidedness implementation, and display logic are missing.
- **Source-grounded alternatives:** The unrounded upper endpoint may be slightly negative and round to 0.00, in which case the analysis can exclude zero despite the displayed endpoint; alternatively, NNT may have been retained under another rule.
- **Direct observation versus inference:** Rule, interval, and NNT are direct. A negative unrounded endpoint is inferred.
- **Exact human question:** What is the unrounded upper ARD confidence limit, and does it exclude zero under the rule used to display NNT 366?

## C022 — Diabetes total-stroke endpoint is called both CrI and CI

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-003 p. 16, eTable 4](../../../joi180151supp2_prod.pdf#page=16).
- **Source fact matched:** The column header is `HR (95% CrI)` and the diabetes HR is `0.78 (0.61 to 1.00)*`.
- **Comparator matched:** The attached footnote says `*Upper confidence interval 1.004`; the adjacent ARR column is separately labeled `ARR (95% CI)`.
- **Rule applicable:** `CrI` and `CI` identify different inferential interval types in this package; a footnote attached to the HR endpoint should use the HR column's interval type unless an exception is defined.
- **Reproduced calculation or logical comparison:** Header-to-footnote comparison yields `credible interval` versus `confidence interval` for the same starred HR endpoint. The footnote resolves the rounded numeric endpoint `1.00` to `1.004` but not the terminology conflict.
- **Inputs available or missing definitions:** Header, cell, footnote, and adjacent CI label are available. The generating model output and intended interval framework for the endpoint are missing.
- **Source-grounded alternatives:** “Confidence” may be informal wording for a credible interval, or the HR interval may be frequentist despite the Bayesian header and methods.
- **Direct observation versus inference:** Both labels are direct. Informal terminology or a wrong header is inferred.
- **Exact human question:** Should the footnote say `upper credible interval limit 1.004`, or is the HR interval type in the header incorrect?

## C023 — The 100-mg-or-less all-MI endpoint is called both CrI and CI

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-003 p. 18, eTable 6](../../../joi180151supp2_prod.pdf#page=18).
- **Source fact matched:** The table identifies data as `Hazard Ratio (95% CrI)` and prints the all-MI, total-daily-dose-at-most-100-mg result `0.87 (0.76 to 1.00)*`.
- **Comparator matched:** The attached footnote says `*Upper confidence interval 0.9989`.
- **Rule applicable:** A footnoted endpoint should retain the table's defined inferential interval type unless an explicit methodological exception is stated.
- **Reproduced calculation or logical comparison:** The same endpoint is labeled as a 95% `CrI` by the table description and a `confidence interval` by the footnote. The unrounded 0.9989 explains the displayed 1.00 boundary but not the label difference.
- **Inputs available or missing definitions:** Table label, cell, and exact footnote endpoint are available. The generating sensitivity-analysis output and intended interval framework are missing.
- **Source-grounded alternatives:** The footnote may use confidence informally, or this sensitivity analysis may be frequentist despite the table's CrI definition; no exception is printed.
- **Direct observation versus inference:** Both competing labels are direct. Informal usage or a header error is inferred.
- **Exact human question:** Is 0.9989 the upper credible limit, or should the table's interval-type label be CI rather than CrI?

## C024 — ASCEND ischemic-stroke events appear in the total-stroke forest plot

- **Status:** Pending Human Adjudication.
- **Location found:** [DOC-003 p. 9, eTable 1](../../../joi180151supp2_prod.pdf#page=9); [DOC-003 p. 16, eTable 4](../../../joi180151supp2_prod.pdf#page=16); rendered source [DOC-003 p. 24, forest plots](../../../joi180151supp2_prod.pdf#page=24); [DOC-002 p. 7, protocol explanation](../../../joi180151supp1_prod.pdf#page=7).
- **Source fact matched:** eTable 1 states for ASCEND total stroke, `Not included in analysis - only reports ischemic stroke`; the protocol explains ASCEND's exclusively ischemic definition, and eTable 4 reports 12 total-stroke studies.
- **Comparator matched:** The total-stroke forest plot includes ASCEND `240/7740` versus `263/7740`; the identical ASCEND row is also present in the separate ischemic-stroke plot.
- **Rule applicable:** An event record explicitly classified as ischemic-only should not also be labeled and pooled as total stroke without a stated broader-definition exception.
- **Reproduced calculation or logical comparison:** Adding ASCEND denominators to eTable 4's 12-study totals gives the total-stroke forest denominators exactly: `73883 + 7740 = 81623` and `72317 + 7740 = 80057`. Exact row identity across the total- and ischemic-stroke panels identifies the added record.
- **Inputs available or missing definitions:** Outcome-definition table, protocol explanation, table study count, and both plotted ASCEND rows are available. The frequentist analysis code, final outcome mapping, and any broader total-stroke convention are missing.
- **Source-grounded alternatives:** The frequentist forest analysis may intentionally use an available-event convention broader than the Bayesian table, but neither its caption nor methods state that exception.
- **Direct observation versus inference:** The definition, exclusion statement, identical plotted row, and denominator identity are direct mechanical observations. A copied row or unstated broader convention is inferred.
- **Exact human question:** Should ASCEND be removed from the total-stroke forest plot, or should the outcome label, caption, and definition table explicitly describe the broader convention used?

## Recheck completion statement

- All 24 stable IDs in the ledger have a separate source-authority recheck above.
- No cited PDF location was absent. C018 remains limited by an unlabeled graphical boundary, and C012-C016, C019, and C021-C024 require unrounded outputs, code, or definitions not supplied in the package to resolve their exact human questions.
- Every candidate remains **Pending Human Adjudication**.
