# Numeric Consistency Review

## Review status and method

- Status of every observation below: **Pending Human Adjudication**.
- Scope: all `N001`-`N076` relationships in `../relationships/numeric_relationship_inventory.md`, covering DOC-001 pp. 1-10, DOC-002 pp. 1-7, and DOC-003 pp. 1-29.
- Each proposed candidate was confirmed against the cited direct PDF page. Reused text, OCR, renders, and the quantitative maps were used only as locators/transcription aids.
- Candidate threshold: an exact printed source fact, a reproducible identity/label rule, a calculation or logical comparison, separation of observation from diagnosis, and a remaining human question.
- Rounding convention for diagnostics: nearest rounding at the displayed precision, with ordinary half-way uncertainty retained as an alternative. Diagnostic arithmetic does not replace an unreported source analysis.
- Outcome: **20 distinct provisional candidate proposals** (`NC-001`-`NC-020`). There was no candidate-count target or stopping rule.

## Provisional candidate proposals

### NC-001 — HbA1c is assigned an mg/dL unit in the abstract but a percent unit in Table 4

- **Relationship:** N008, cross-checked with N051.
- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-001 p. 1, abstract Results](../../../jama_flint_2019_oi_190079.pdf#page=1); [DOC-001 p. 8, Table 4](../../../jama_flint_2019_oi_190079.pdf#page=8).
- **Printed source facts:** The abstract gives the HbA1c daily-rate contrast as `-0.0002 mg/dL` (95% CI, `-0.0021 to 0.0016`). Table 4 labels `HbA1c, %`.
- **Rule and calculation:** A single reported HbA1c measure should retain its stated scale/unit across summary and tabular locations. `mg/dL` and `%` are not interchangeable labels, and no source conversion between them is supplied.
- **Tolerance:** Not a rounding issue.
- **Direct observation:** The two units are printed on the cited direct PDF pages.
- **Diagnostic inference:** The abstract unit may have been propagated from adjacent glucose/lipid outcomes.
- **Alternative source-grounded interpretations:** The phrase “daily rate” may carry the time denominator for all listed outcomes, but it does not reconcile the concentration unit with the percent unit. Table 4 may be the intended HbA1c scale.
- **Quality-control relevance:** A unit-bearing extraction of the abstract estimate can differ materially from a Table 4 extraction.
- **Exact human question:** What unit should accompany the HbA1c treatment-by-time estimate and interval?

### NC-002 — The UKU presence rule permits a score above the printed item maximum

- **Relationship:** N014.
- **Category:** Measure, label, or scale inconsistency.
- **Exact source location:** [DOC-001 p. 4, adverse-effect definition](../../../jama_flint_2019_oi_190079.pdf#page=4).
- **Printed source facts:** UKU items are stated to range from `0-3`; an adverse effect is then defined in part as “a score of 3 or 4” plus an increase from baseline.
- **Rule and calculation:** On the printed `0,1,2,3` item scale, `4 > 3` and is outside the stated range.
- **Tolerance:** Not a rounding issue.
- **Direct observation:** Both the maximum and the `3 or 4` rule occur in the same direct-source paragraph.
- **Diagnostic inference:** `4` may be a carryover from a differently coded version of the instrument or a transcription error.
- **Alternative source-grounded interpretations:** The paper might have used an unreported recoding or a special non-item code, but no such definition is supplied.
- **Quality-control relevance:** The printed operational threshold cannot be implemented literally for score 4 under the printed range.
- **Exact human question:** Should the presence rule say score 3 only, or should the printed UKU range/coding be expanded or otherwise defined?

### NC-003 — Placebo living-arrangement categories leave two randomized participants unaccounted for

- **Relationship:** N025.
- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [DOC-001 p. 5, Table 1](../../../jama_flint_2019_oi_190079.pdf#page=5).
- **Printed source facts:** Placebo header `n=62`; living with others `49 (79.0%)`, alone `10 (16.1%)`, senior residence `1 (1.6%)`.
- **Rule and calculation:** The three displayed living arrangements are mutually exclusive table categories. Counts sum `49+10+1=60`, two short of 62; percentages sum `79.0+16.1+1.6=96.7%`, 3.3 percentage points short of 100%.
- **Tolerance:** Count gap 2; percentage gap greatly exceeds the maximum 0.15 percentage point total drift from three values independently rounded to one decimal.
- **Direct observation:** Header and all three entries were confirmed on the direct PDF.
- **Diagnostic inference:** Two values may be missing without a displayed missingness denominator.
- **Alternative source-grounded interpretations:** The categories could intentionally cover only 60 respondents, but unlike several other Table 1 rows, no row-specific `n=60` is printed.
- **Quality-control relevance:** A reader treating the arm header as the denominator obtains an incomplete categorical distribution.
- **Exact human question:** Were two placebo participants missing living-arrangement data, and if so should the row denominator/missingness be printed?

### NC-004 — Hyperlipidemia percentages reproduce the opposite arm denominators

- **Relationship:** N029.
- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [DOC-001 p. 5, Table 1](../../../jama_flint_2019_oi_190079.pdf#page=5).
- **Printed source facts:** Arm headers are olanzapine `n=64` and placebo `n=62`; hyperlipidemia is `18 (29.0%)` and `19 (29.7%)`, respectively.
- **Rule and calculation:** `18/64=28.125%` (28.1%, not 29.0%); `19/62=30.645%` (30.6%, not 29.7%). Conversely, `18/62=29.032%` (29.0%) and `19/64=29.688%` (29.7%), exactly reproducing the printed percentages with the opposite headers.
- **Tolerance:** One-decimal rounding intervals do not include the header-denominator results.
- **Direct observation:** Counts, percentages, and arm headers were confirmed on the direct PDF.
- **Diagnostic inference:** The percentage denominators may have been transposed between arms.
- **Alternative source-grounded interpretations:** Row-specific denominators could differ, but a placebo denominator of 64 would exceed that arm's randomized population, and no row-specific denominators are printed.
- **Quality-control relevance:** Arm-specific prevalence is liable to be extracted with a denominator/percentage mismatch.
- **Exact human question:** Are the two percentages transposed or should different row denominators be supplied?

### NC-005 — Barnes participant counts are formatted as decimal-valued counts

- **Relationship:** N034.
- **Category:** Rate-versus-count inconsistency.
- **Exact source location:** [DOC-001 p. 6, Table 2](../../../jama_flint_2019_oi_190079.pdf#page=6).
- **Printed source facts:** Under the `No. (%) of Participants` columns, Barnes global score >0 is `3.0 (4.7)` and `2.0 (3.2)`.
- **Rule and calculation:** Participant counts are discrete integers; the percentages reproduce `3/64=4.6875%` and `2/62=3.2258%`, indicating counts 3 and 2 rather than measurements 3.0 and 2.0.
- **Tolerance:** Not a percentage-rounding issue; the percentages reconcile after treating the decimal-leading values as counts.
- **Direct observation:** Decimal points and the `No. (%)` header were confirmed on the direct PDF.
- **Diagnostic inference:** The counts may have inherited continuous-score numeric formatting.
- **Alternative source-grounded interpretations:** A decimal count could be read harmlessly as an integer-valued number, but the table label specifically distinguishes number from percentage.
- **Quality-control relevance:** Structured extraction may classify `3.0` and `2.0` as means or scores rather than counts.
- **Exact human question:** Should these participant counts be printed as `3` and `2`?

### NC-006 — AIMS participant counts are formatted as decimal-valued counts

- **Relationship:** N034.
- **Category:** Rate-versus-count inconsistency.
- **Exact source location:** [DOC-001 p. 6, Table 2](../../../jama_flint_2019_oi_190079.pdf#page=6).
- **Printed source facts:** Under `No. (%) of Participants`, AIMS overall severity >0 is `2.0 (3.1)` and `2.0 (3.2)`.
- **Rule and calculation:** Counts must be integers; `2/64=3.125%` and `2/62=3.2258%`, which reproduce 3.1% and 3.2% and identify the leading values as counts.
- **Tolerance:** Percentages reconcile at one decimal after integer interpretation.
- **Direct observation:** Values and header were confirmed on the direct PDF.
- **Diagnostic inference:** This may be the same formatting mechanism as NC-005, but it concerns a different instrument and printed result row.
- **Alternative source-grounded interpretations:** Mathematically `2.0=2`, though the representation is inconsistent with a participant-count label.
- **Quality-control relevance:** The row can be miscoded as a continuous scale result.
- **Exact human question:** Should both AIMS participant counts be printed as `2`?

### NC-007 — The placebo relapse-hospitalization percentage does not round to the printed value

- **Relationship:** N045.
- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [DOC-001 p. 8, Results](../../../jama_flint_2019_oi_190079.pdf#page=8).
- **Printed source facts:** `11 (32.3%) of 34` placebo relapses required psychiatric hospitalization.
- **Rule and calculation:** `100*11/34=32.352941...%`, which rounds to 32.4% at one decimal under nearest rounding, not 32.3%.
- **Tolerance:** The exact value lies outside the `[32.25,32.35)` interval ordinarily displayed as 32.3%; it is 0.00294 percentage point above the upper boundary. This is a very small boundary discrepancy.
- **Direct observation:** Numerator, denominator, and percentage were confirmed on the direct PDF.
- **Diagnostic inference:** The percentage may have been truncated or computed from a different unprinted denominator.
- **Alternative source-grounded interpretations:** A truncation convention would produce 32.3%; the paper otherwise reports many nearest-rounded one-decimal percentages but does not state a convention here.
- **Quality-control relevance:** Small percentage differences can be copied verbatim into evidence tables and prevent exact numerator/denominator reconciliation.
- **Exact human question:** Was 32.3% intentionally truncated, or should the printed percentage be 32.4%?

### NC-008 — Total-cholesterol absolute difference is 4.4, not the printed 4.3, at one decimal

- **Relationship:** N055.
- **Category:** Numeric or arithmetic inconsistency.
- **Exact source location:** [DOC-001 p. 9, Table 5](../../../jama_flint_2019_oi_190079.pdf#page=9).
- **Printed source facts:** Total cholesterol: olanzapine `9/64 (14.1%)`, placebo `6/62 (9.7%)`, absolute unadjusted difference `4.3%`.
- **Rule and calculation:** `100*(9/64-6/62)=4.3850806` percentage points, which rounds to 4.4; the displayed percentages also give `14.1-9.7=4.4`.
- **Tolerance:** Exact difference is outside the ordinary `[4.25,4.35)` one-decimal interval for 4.3.
- **Direct observation:** Counts, arm denominators, percentages, and difference were confirmed on the direct PDF.
- **Diagnostic inference:** The table may contain a one-tenth transcription or rounding defect.
- **Alternative source-grounded interpretations:** An unprinted analysis denominator or adjustment could differ, but the column is explicitly `absolute unadjusted difference` and the arm headers provide denominators.
- **Quality-control relevance:** An extracted unadjusted risk difference will not reproduce from the printed counts.
- **Exact human question:** What computation or denominator produced 4.3 percentage points, or should it be 4.4?

### NC-009 — LDL absolute difference is 4.4, not the printed 4.3, at one decimal

- **Relationship:** N056.
- **Category:** Numeric or arithmetic inconsistency.
- **Exact source location:** [DOC-001 p. 9, Table 5](../../../jama_flint_2019_oi_190079.pdf#page=9).
- **Printed source facts:** LDL: olanzapine `9/64 (14.1%)`, placebo `6/62 (9.7%)`, absolute unadjusted difference `4.3%`.
- **Rule and calculation:** `100*(9/64-6/62)=4.3850806` percentage points, which rounds to 4.4; `14.1-9.7=4.4` from displayed percentages.
- **Tolerance:** Same one-decimal interval test as NC-008.
- **Direct observation:** The separate LDL row was confirmed on the direct PDF.
- **Diagnostic inference:** The LDL row may repeat the same rounding/transcription mechanism as the total-cholesterol row.
- **Alternative source-grounded interpretations:** No different denominator is printed for LDL.
- **Quality-control relevance:** This distinct outcome row cannot be reproduced from its printed counts.
- **Exact human question:** What computation produced the LDL value 4.3, or should it be 4.4?

### NC-010 — Total-cholesterol and LDL incident-high result vectors are exact duplicates

- **Relationships:** N055 and N056.
- **Category:** Numeric or arithmetic inconsistency.
- **Exact source location:** [DOC-001 p. 9, Table 5](../../../jama_flint_2019_oi_190079.pdf#page=9).
- **Printed source facts:** Despite different thresholds (`240 mg/dL` total cholesterol; `160 mg/dL` LDL), both rows print `9 (14.1%)` versus `6 (9.7%)`, difference `4.3`, and CI `-8 to 17.2`.
- **Rule and calculation:** The complete eight-number result vector and interval are duplicated across two separately defined outcomes. The probability of identity is not calculated; the reproducible check is exact field-by-field equality.
- **Tolerance:** Exact equality at every displayed field.
- **Direct observation:** Both rows and their different thresholds were confirmed on the direct PDF.
- **Diagnostic inference:** The equality could be a duplicated row or could reflect the same participants meeting both thresholds.
- **Alternative source-grounded interpretations:** A genuine coincidence is source-grounded and plausible; exact duplication alone does not determine its cause.
- **Quality-control relevance:** Repeated result vectors across outcomes are a recognized transcription check and merit source-data confirmation before reuse.
- **Exact human question:** Did the same 9 and 6 participants satisfy both outcome definitions with the same interval, or was one row duplicated?

### NC-011 — The protocol's written ARD operation has the opposite sign from its interpretation rule

- **Relationship:** N062.
- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-002 p. 6, statistical analysis](../../../joi180151supp1_prod.pdf#page=6); [DOC-003 p. 4, ARD method](../../../joi180151supp2_prod.pdf#page=4).
- **Printed source facts:** DOC-002 says the RR-multiplied placebo event rate “is then subtracted from the placebo risk,” followed by “Negative values” favor aspirin. DOC-003 says negative ARD indicates reduced risk with aspirin.
- **Rule and calculation:** If no-aspirin risk is `R0` and `RR<1`, the operation as worded is `R0-(RR*R0)=R0(1-RR)>0`, but the interpretation requires a negative value. The sign-compatible ARD is `(RR*R0)-R0=R0(RR-1)<0`.
- **Tolerance:** Algebraic sign, not rounding.
- **Direct observation:** Wording and sign convention were confirmed on both direct PDFs.
- **Diagnostic inference:** The subtraction order in DOC-002 may be reversed in prose.
- **Alternative source-grounded interpretations:** “Which is then subtracted” might have been intended to refer to placebo risk being subtracted from the estimated aspirin risk, despite its grammatical antecedent.
- **Quality-control relevance:** Literal implementation of the protocol prose reverses benefit/harm signs.
- **Exact human question:** Which subtraction order was intended for ARD calculation?

### NC-012 — Incident-cancer model selection uses random effects at printed I2=25% although the rule requires >25%

- **Relationship:** N063.
- **Category:** Measure, label, or scale inconsistency.
- **Exact source locations:** [DOC-003 p. 4, model-selection rule](../../../joi180151supp2_prod.pdf#page=4); [DOC-003 p. 5, eMethods 3 all-patients incident-cancer row](../../../joi180151supp2_prod.pdf#page=5).
- **Printed source facts:** When DICs are within 3, random effects are favored if fixed-effect `I2 >25%`; otherwise fixed. Incident cancer has fixed DIC `27.06`, random DIC `27.93` (difference `0.87`), I2 `25`, selected model `random`.
- **Rule and calculation:** `|27.06-27.93|=0.87<3`; printed `25` is not greater than `25`, so the stated rule selects fixed, while the table selects random.
- **Tolerance:** The displayed integer I2 may hide an unrounded value greater than 25%; that unprinted precision is the main alternative.
- **Direct observation:** Rule and row were confirmed on the direct PDF.
- **Diagnostic inference:** The model may have been selected from unrounded I2 or by a `>=25%` implementation.
- **Alternative source-grounded interpretations:** The intended threshold may have been “25% or greater,” or the displayed I2 may be rounded down from above 25%.
- **Quality-control relevance:** The printed decision rule does not reproduce the printed model label at displayed precision.
- **Exact human question:** Was the decision based on an unrounded I2 greater than 25%, or should the threshold/model label be revised?

### NC-013 — eTable 3 omits the scale needed to interpret ARD and reproduce NNT/NNH

- **Relationship:** N066.
- **Category:** Measure, label, or scale inconsistency.
- **Exact source location:** [DOC-003 p. 15, eTable 3](../../../joi180151supp2_prod.pdf#page=15).
- **Printed source facts:** Cells are labeled `ARD` without a unit. Composite all-patients is `-0.41` with NNT `242`; major bleeding is `0.47` with NNH `210`.
- **Rule and calculation:** If `0.41` were a proportion, reciprocal NNT would be about `1/0.41=2.44`; interpreting it as 0.41 percentage point gives `100/0.41=243.9`, near the printed 242 after unrounded-input allowance. Thus the accompanying NNT numerically implies percentage points, but that scale is not printed.
- **Tolerance:** Unrounded ARD can explain the small 243.9-versus-242 difference; it cannot make the omitted unit explicit.
- **Direct observation:** The direct PDF table and footnote contain no percent/percentage-point label for ARD.
- **Diagnostic inference:** ARDs are likely intended as percentage points.
- **Alternative source-grounded interpretations:** A reader familiar with the analysis may infer percentage points from NNT, but the table is not self-defining.
- **Quality-control relevance:** A data extractor could interpret `0.41` as 41% rather than 0.41 percentage point, changing scale by 100-fold.
- **Exact human question:** Should eTable 3 label ARD values explicitly as percentage points (or state another intended scale)?

### NC-014 — All-patient major-bleeding ARD and NNH do not share a compatible displayed precision

- **Relationship:** N066.
- **Category:** Numeric or arithmetic inconsistency.
- **Exact source location:** [DOC-003 p. 15, eTable 3](../../../joi180151supp2_prod.pdf#page=15).
- **Printed source facts:** All-patient major bleeding ARD `0.47` and NNH `210`.
- **Rule and calculation:** On the percentage-point scale implied by the table, `100/0.47=212.77`; NNH 210 implies `100/210=0.47619`, which would display as 0.48 under nearest two-decimal rounding, not 0.47.
- **Tolerance:** Values displaying as 0.47 ordinarily lie in `[0.465,0.475)`; 0.47619 is outside.
- **Direct observation:** Both values were confirmed on the direct PDF.
- **Diagnostic inference:** The NNH may use a different unprinted estimate or one of the two printed values may be rounded/transcribed inconsistently.
- **Alternative source-grounded interpretations:** A nonstandard reciprocal/rounding convention or a separately calculated NNH could exist but is not stated.
- **Quality-control relevance:** The two extraction fields do not mechanically reconcile under the displayed ARD rule.
- **Exact human question:** Which unrounded ARD and NNH convention produced the pair 0.47 and 210?

### NC-015 — High-risk major-bleeding ARD and NNH do not reconcile

- **Relationship:** N066.
- **Category:** Numeric or arithmetic inconsistency.
- **Exact source location:** [DOC-003 p. 15, eTable 3](../../../joi180151supp2_prod.pdf#page=15).
- **Printed source facts:** High-risk major bleeding ARD `0.64` and NNH `152`.
- **Rule and calculation:** `100/0.64=156.25`; NNH 152 implies `100/152=0.65789`, which displays as 0.66 rather than 0.64.
- **Tolerance:** The reciprocal-implied value is outside the `[0.635,0.645)` interval displaying as 0.64.
- **Direct observation:** Both values were confirmed on the direct PDF.
- **Diagnostic inference:** Different unprinted inputs or transcription could underlie the pair.
- **Alternative source-grounded interpretations:** The NNH may have been computed from a separately estimated absolute effect not represented by the ARD cell, but the table does not state that.
- **Quality-control relevance:** An extractor cannot reproduce the displayed NNH from the displayed ARD even allowing ordinary rounding.
- **Exact human question:** What unrounded value or alternative rule produced NNH 152?

### NC-016 — Diabetes major-bleeding ARD and NNH do not reconcile

- **Relationship:** N066.
- **Category:** Numeric or arithmetic inconsistency.
- **Exact source location:** [DOC-003 p. 15, eTable 3](../../../joi180151supp2_prod.pdf#page=15).
- **Printed source facts:** Diabetes major bleeding ARD `0.80` and NNH `121`.
- **Rule and calculation:** `100/0.80=125`; NNH 121 implies `100/121=0.82645`, which displays as 0.83 rather than 0.80.
- **Tolerance:** The implied value is outside the `[0.795,0.805)` interval displaying as 0.80.
- **Direct observation:** Both values were confirmed on the direct PDF.
- **Diagnostic inference:** One value may use a different unprinted effect estimate.
- **Alternative source-grounded interpretations:** A separately modeled NNH is possible but not identified in the table or methods.
- **Quality-control relevance:** The discrepancy can propagate into benefit-harm summaries that combine ARD and NNH.
- **Exact human question:** What exact ARD and reciprocal convention produced NNH 121?

### NC-017 — Low- and high-risk total-stroke event counts do not sum to the all-participant counts

- **Relationship:** N067.
- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [DOC-003 p. 16, eTable 4](../../../joi180151supp2_prod.pdf#page=16).
- **Printed source facts:** Aspirin all `1116/73883`, low `752/56212`, high `381/17671`; no aspirin all `1136/72317`, low `788/56354`, high `380/15963`.
- **Rule and calculation:** Participant denominators partition exactly: `56212+17671=73883` and `56354+15963=72317`. Event counts do not: aspirin `752+381=1133`, 17 above 1116; no aspirin `788+380=1168`, 32 above 1136.
- **Tolerance:** Integer identities; no rounding.
- **Direct observation:** All four rows were confirmed on the direct PDF.
- **Diagnostic inference:** Some events may be defined or assigned differently across population rows, or counts may be transcribed incorrectly.
- **Alternative source-grounded interpretations:** If low/high outcome definitions or study availability differ despite exact denominator partitioning, the sums need not match; no such exception is stated in eTable 4.
- **Quality-control relevance:** Population-stratified event extraction cannot be reconciled to the all-participant row.
- **Exact human question:** Why do the exact low/high participant partitions not carry an additive total-stroke event partition?

### NC-018 — eFigure 2 detection-bias proportions do not match the 13 eTable 2 trial classifications

- **Relationship:** N071, using N065 exact categories.
- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source locations:** [DOC-003 pp. 10-14, eTable 2](../../../joi180151supp2_prod.pdf#page=10); [DOC-003 p. 20, eFigure 2](../../../joi180151supp2_prod.pdf#page=20).
- **Printed source facts:** Detection is `Unclear` for BDS, PHS, HOT, WHS, and ASCEND (5 trials) and `Low` for the other 8. The graph boundary is drawn at approximately 69% low/31% unclear, matching a 9/4 split rather than 8/5.
- **Rule and calculation:** Exact table recomputation is low `8/13=61.54%` and unclear `5/13=38.46%`. A 69.23%/30.77% graphic corresponds to 9/13 and 4/13, one trial different.
- **Tolerance:** One trial equals 7.69 percentage points; the plotted boundary is visually near 69%, not near 62%, on the printed 0%-100% axis.
- **Direct observation:** All 13 table categories and the direct-source graphic were inspected.
- **Diagnostic inference:** The detection bar may duplicate the blinding/overall 9/4 proportions or one eTable classification may differ from the graphic input.
- **Alternative source-grounded interpretations:** Because the graph has no numeric data labels, its precise boundary is a visual reading; however, the labeled 20% grid makes the one-trial difference distinguishable.
- **Quality-control relevance:** Graph-based risk-of-bias extraction and table-based extraction yield different domain summaries.
- **Exact human question:** Which detection-bias classification set generated eFigure 2?

### NC-019 — The printed Egger coefficient and SE cannot produce the printed t statistic at their displayed precision

- **Relationship:** N072.
- **Category:** Statistical reporting inconsistency.
- **Exact source location:** [DOC-003 p. 21, eFigure 3](../../../joi180151supp2_prod.pdf#page=21).
- **Printed source facts:** Egger coefficient `-0.47`, standard error `0.77`, `t=-0.59`, `P=0.57`.
- **Rule and calculation:** A coefficient/SE t ratio gives `-0.47/0.77=-0.6104`, about -0.61. Allowing ordinary two-decimal rounding, coefficient magnitude `[0.465,0.475)` divided by SE `[0.765,0.775)` yields t magnitude approximately `[0.600,0.621]`; printed -0.59 lies outside. The printed t and P are mutually plausible for about 8 df, so the mismatch is localized to coefficient/SE versus t.
- **Tolerance:** Full interval-of-rounded-input diagnostic stated above; no unreported model convention is assumed.
- **Direct observation:** All four values were confirmed on the direct PDF.
- **Diagnostic inference:** One of coefficient, SE, or t may derive from a different precision/output field.
- **Alternative source-grounded interpretations:** Some Egger implementation might label a quantity that is not the numerator of the displayed t, but the figure does not define an alternative relationship.
- **Quality-control relevance:** The inferential vector does not mechanically reproduce and may be copied into publication-bias assessments.
- **Exact human question:** What unrounded coefficient and SE, or what alternative test definition, produced `t=-0.59`?

### NC-020 — eTable 4 all-participant total-stroke events differ from the forest-plot counts after applying the stated ASCEND exclusion

- **Relationships:** N067 and N074.
- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-003 p. 16, eTable 4](../../../joi180151supp2_prod.pdf#page=16); [DOC-003 p. 24, eFigure 4 total-stroke forest plot](../../../joi180151supp2_prod.pdf#page=24); [DOC-002 p. 7, ASCEND composite-stroke protocol change](../../../joi180151supp1_prod.pdf#page=7).
- **Printed source facts:** eTable 4 reports 12 studies, aspirin `1116/73883`, no aspirin `1136/72317`. The 13 forest rows total aspirin `1358/81623` and no aspirin `1397/80057`; ASCEND is `240/7740` and `263/7740`.
- **Rule and calculation:** Removing ASCEND reproduces both eTable denominators exactly: `81623-7740=73883`, `80057-7740=72317`. It does not reproduce events: aspirin `1358-240=1118` versus printed 1116; no aspirin `1397-263=1134` versus printed 1136. The total number of events is preserved but 2 events shift from aspirin to no aspirin.
- **Tolerance:** Integer count identity; no rounding.
- **Direct observation:** eTable 4 and every total-stroke forest row were checked on the direct-source pages; the exclusion rationale was confirmed in DOC-002.
- **Diagnostic inference:** Two total-stroke events may be arm-transposed between the table and forest data, or a trial-level definition/version may differ.
- **Alternative source-grounded interpretations:** eTable 4 could use a separately curated event dataset while the forest plot uses another, but identical post-ASCEND participant totals and no displayed event-definition exception make that difference unresolved.
- **Quality-control relevance:** Two supplement extractions for the same 12-study total-stroke population yield different arm event counts.
- **Exact human question:** Which 12-study arm event totals are intended, and what accounts for the two-event transfer?

## Complete relationship check record

`COMPLETE` means the relationship received every applicable check in this lane; it is not an adjudication of any candidate.

| Relationship | Status | Provisional candidate(s), if any | Check summary |
|---|---|---|---|
| N001 | COMPLETE | None | Dates, centers, and phase durations repeat without conflict. |
| N002 | COMPLETE | None | Phase count, age range, stabilization, MMSE, and randomized duration are label-compatible. |
| N003 | COMPLETE | None | Doses, strengths, medians, and IQRs are compatible. |
| N004 | COMPLETE | None | `64+62=126`; allocation/taper labels are compatible. |
| N005 | COMPLETE | None | `78/126=61.9048%`, displayed 61.9%. |
| N006 | COMPLETE | None | `43+13+24+34=114`; `114/126=90.476%`, displayed 90.5%. |
| N007 | COMPLETE | None | Both relapse percentages reproduce and repeat identically. |
| N008 | COMPLETE | NC-001 | All estimate/CI repetitions match; HbA1c unit does not. |
| N009 | COMPLETE | None | Thresholds retain stated scales and periods. |
| N010 | COMPLETE | None | Remission duration/score/percentage rules are internally distinct and compatible. |
| N011 | COMPLETE | None | Outcomes and measurement frequencies are consistently labeled. |
| N012 | COMPLETE | None | Schedule and relapse criteria are internally compatible. |
| N013 | COMPLETE | None | AIMS item versus global and Simpson-Angus included-item distinctions explain range differences. |
| N014 | COMPLETE | NC-002 | UKU score 4 exceeds printed 0-3 range. |
| N015 | COMPLETE | None | `1/0.20=5`; sample-size inputs otherwise lack enough detail for recalculation. |
| N016 | COMPLETE | None | `60+16+5=81`; `350-81=269`; `269-74=195`; `195-33=162`. |
| N017 | COMPLETE | None | `31+21+7+5+1+9=74`. |
| N018 | COMPLETE | None | Stabilization and randomization components reconcile: `162-15=147`; `147-21=126`. |
| N019 | COMPLETE | None | `59+5=64`; `43+13+8=64`; all 64 analyzed. |
| N020 | COMPLETE | None | `60+2=62`; `24+34+4=62`; all 62 analyzed. |
| N021 | COMPLETE | None | Age categories sum to each arm and percentages reconcile. |
| N022 | COMPLETE | None | Sex categories sum to arms; women sum `37+41=78`. |
| N023 | COMPLETE | None | Race counts sum to arms; ethnicity is separately labeled. |
| N024 | COMPLETE | None | Marital counts sum to arms; percentage drift is rounding-compatible. |
| N025 | COMPLETE | NC-003 | Olanzapine sums to 64; placebo living categories sum to 60 of 62. |
| N026 | COMPLETE | None | Four site counts sum to 64 and 62; percentages reconcile. |
| N027 | COMPLETE | None | Row-specific denominators are explicit where reduced. |
| N028 | COMPLETE | None | Counts and percentages reproduce from arm denominators. |
| N029 | COMPLETE | NC-004 | Hypertension/diabetes reproduce; hyperlipidemia reproduces opposite denominators. |
| N030 | COMPLETE | None | Denominators and conversion label are explicit; no displayed converted comparator. |
| N031 | COMPLETE | None | 100% count identities and scale labels reconcile. |
| N032 | COMPLETE | None | Ranges/IQRs and one row-specific denominator are compatible. |
| N033 | COMPLETE | None | DKEFS/MMSE ranges, denominators, and labels are compatible. |
| N034 | COMPLETE | NC-005, NC-006 | Percentages identify the decimal-leading fields as participant counts. |
| N035 | COMPLETE | None | Arm dose vectors repeat the abstract values. |
| N036 | COMPLETE | None | Conversion factors and scale component distinctions are compatible. |
| N037 | COMPLETE | None | Reference groups, estimates, and labels are complete; inferential checks are also assigned to the statistical lane. |
| N038 | COMPLETE | None | Event-type sums exceed relapse counts under the explicit multiple-event footnote. |
| N039 | COMPLETE | None | At-risk series are nonincreasing and week-36 counts equal remission completers. |
| N040 | COMPLETE | None | NNT lacks enough source inputs for an independent formula check; no inconsistency inferred from missing details alone. |
| N041 | COMPLETE | None | `6+6=12` and `2+1=3`. |
| N042 | COMPLETE | None | Percentages are compatible with integer events under arm denominators. |
| N043 | COMPLETE | None | Each listed effect exceeds 5% in at least one arm; percentages map to plausible integer counts. |
| N044 | COMPLETE | None | Falls and serious-adverse-event percentages reproduce; one death is included in the olanzapine serious-event total. |
| N045 | COMPLETE | NC-007 | Olanzapine `6/13` rounds to 46.2%; placebo `11/34` boundary differs. |
| N046 | COMPLETE | None | Raw mean change need not equal marginal means under the explicit missing-data caveat. |
| N047 | COMPLETE | None | Same caveat; units and counts are compatible. |
| N048 | COMPLETE | None | Same caveat; units and labels are compatible. |
| N049 | COMPLETE | None | Same caveat; units and labels are compatible. |
| N050 | COMPLETE | None | Same caveat; units and labels are compatible. |
| N051 | COMPLETE | NC-001 | Table's percent unit conflicts with abstract mg/dL. |
| N052 | COMPLETE | None | Median/IQR and modeled difference are not forced into marginal subtraction. |
| N053 | COMPLETE | None | Same distinction; no rate/count confusion. |
| N054 | COMPLETE | None | Blank count cells are consistent with full-arm header-denominator convention; explicit missing-data caveat retained. |
| N055 | COMPLETE | NC-008, NC-010 | Percentages reproduce; difference rounding and exact cross-outcome duplication remain. |
| N056 | COMPLETE | NC-009, NC-010 | Percentages reproduce; difference rounding and exact cross-outcome duplication remain. |
| N057 | COMPLETE | None | Percentages and exact difference reproduce: about 3.0 points. |
| N058 | COMPLETE | None | Percentages and exact difference reproduce: about -0.2 point. |
| N059 | COMPLETE | None | Threshold, incident definition, CI-type, and conversion labels are coherent. |
| N060 | COMPLETE | None | `34/62=54.8%` relapsed, leaving `28/62=45.2%`, compatible with 45% no relapse. |
| N061 | COMPLETE | None | All protocol/method numeric definitions and change-dated thresholds were checked without an additional lane candidate. |
| N062 | COMPLETE | NC-011 | Printed subtraction order conflicts with printed sign direction. |
| N063 | COMPLETE | NC-012 | 43 model rows reproduce the rule at displayed precision; all-patient incident cancer does not. |
| N064 | COMPLETE | None | All 13 definition rows checked; source-level blank/not-defined labels retained without inference. |
| N065 | COMPLETE | None | Follow-up percentages/counts are arithmetically compatible where denominators are supplied; 13x7 domain vector complete. |
| N066 | COMPLETE | NC-013, NC-014, NC-015, NC-016 | All 44 cells checked for sign/interval/NNT display; three major-bleeding reciprocal pairs exceed displayed rounding tolerance. |
| N067 | COMPLETE | NC-017, NC-020 | Four rows checked for count/denominator/subgroup/forest identities. |
| N068 | COMPLETE | None | All 88 rates checked for direction, population, per-person-time scale, and repeated values; person-years are not supplied for independent rate reconstruction. |
| N069 | COMPLETE | None | All 44 sensitivity cells have ordered intervals and matching effect/contrast labels; header N values are not decomposed in the source. |
| N070 | COMPLETE | None | `668+717=1385`; `1385-235=1150`; eight exclusions sum 1131; 19 screened publications plus 2 added equals 21. |
| N071 | COMPLETE | NC-018 | Six graph domains reproduce eTable categories; detection differs by one trial. |
| N072 | COMPLETE | NC-019 | Coefficient/SE ratio fails displayed-precision test; t/P remain mutually plausible. |
| N073 | COMPLETE | None | 39 study RRs reproduce at two decimals; participant totals reproduce; weights sum within independent rounding tolerance. |
| N074 | COMPLETE | NC-020 | 36 study RRs reproduce; participant totals and weights reconcile; post-ASCEND total-stroke events differ from eTable 4. |
| N075 | COMPLETE | None | 22 study RRs, totals, and weight sums reproduce within displayed precision. |
| N076 | COMPLETE | None | 33 study RRs, totals, and weight sums reproduce within displayed precision. |

## Limitations

1. No raw participant data, unrounded model output, or person-time denominator file is supplied. Diagnostic arithmetic uses only printed inputs and explicitly preserves unrounded-value alternatives.
2. Table 4 marginal baseline/termination summaries cannot reproduce paired or model-based change estimates; its printed missing-data caveat prevents treating those differences as candidates.
3. eFigure 2 has no numeric segment labels; NC-018 uses the printed axis and the exact 13-row categorical table as its comparator.
4. Forest-plot graphics were directly inspected and all displayed study rows were mechanically checked, but pooled estimates were not independently refitted because the source does not supply every analytic convention and this lane does not substitute a new analysis.

