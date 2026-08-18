## C001 — HbA1c is assigned an mg/dL unit in narrative results but a percent scale in Table 4

*Pending Human Adjudication*

**Candidate statement:** HbA1c is assigned an mg/dL unit in narrative results but a percent scale in Table 4. The printed relationship requires human adjudication.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-001 p. 1, abstract Results](../jama_flint_2019_oi_190079.pdf#page=1); [DOC-001 p. 7, Results](../jama_flint_2019_oi_190079.pdf#page=7); [DOC-001 p. 8, Table 4](../jama_flint_2019_oi_190079.pdf#page=8).

**Source evidence:** The abstract prints the HbA1c daily-rate contrast as `-0.0002 mg/dL` (95% CI, `-0.0021 to 0.0016`); the Results repeats the estimate, interval, and `mg/dL`; Table 4 labels the measure `HbA1c, %` and gives levels near 5.7-5.9. Adjacent narrative outcomes appropriately use `mg/dL` for lipids and glucose.

**Reported-versus-comparator:** A single named analyte should retain its stated measurement scale unless a conversion or alternate scale is supplied. `mg/dL` and `%` are not interchangeable, and the package supplies no HbA1c conversion. The estimate magnitude is compatible with a daily change on the displayed percentage scale but does not establish the intended unit by itself.

**Reasoning procedure:** The competing units are directly printed. A unit copied from adjacent glucose/lipid results is a diagnostic explanation only. This is a unit-label comparison, not a rounding issue.

**Calculation:** A single named analyte should retain its stated measurement scale unless a conversion or alternate scale is supplied. `mg/dL` and `%` are not interchangeable, and the package supplies no HbA1c conversion. The estimate magnitude is compatible with a daily change on the displayed percentage scale but does not establish the intended unit by itself.

**Alternative source-grounded interpretations:** Table 4 may supply the intended percent scale; alternatively, the model coefficient may use an unstated HbA1c scale. A shared daily time denominator does not reconcile concentration with percent.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** Abstract and table extraction can assign materially different units to the same coefficient, potentially propagating a scale error into evidence tables; this observation does not establish that the numeric estimate or paper-level conclusion is wrong.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Inspect the analysis output/data dictionary for the treatment-by-time HbA1c coefficient; confirm its scale and time unit; compare the intended label with both narrative occurrences and Table 4. What unit should accompany the HbA1c treatment-by-time estimate and interval—percentage points per day, `mg/dL`, or another explicitly defined scale?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C002 — The UKU adverse-effect rule permits a score above the printed item maximum

*Pending Human Adjudication*

**Candidate statement:** The UKU adverse-effect rule permits a score above the printed item maximum. The printed relationship requires human adjudication.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-001 p. 4, adverse-effect definition](../jama_flint_2019_oi_190079.pdf#page=4).

**Source evidence:** UKU items are stated to range from `0-3`; an adverse effect is defined in part as a score of `3 or 4` plus an increase from baseline.

**Reported-versus-comparator:** On the printed item scale `{0,1,2,3}`, `4 > 3` and is outside the stated range.

**Reasoning procedure:** The maximum and threshold are printed in the same paragraph. A carryover from another coding version or a transcription error is only a diagnostic inference. Exact scale-bound comparison; no rounding applies.

**Calculation:** On the printed item scale `{0,1,2,3}`, `4 > 3` and is outside the stated range.

**Alternative source-grounded interpretations:** An unreported recoding or special non-item code could permit 4, but no such definition is supplied.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** The operational rule cannot be implemented literally for score 4 under the printed range and could be miscoded in secondary extraction; no claim is made about outcome validity or conclusions.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Check the administered UKU version, coding dictionary, and analysis rule; determine whether score 4 exists and whether it is an item value or special code. Should the presence rule say score 3 only, or should the printed UKU range/coding be expanded or otherwise defined?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C003 — Placebo living-arrangement categories leave two randomized participants unaccounted for

*Pending Human Adjudication*

**Candidate statement:** Placebo living-arrangement categories leave two randomized participants unaccounted for. The printed relationship requires human adjudication.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-001 p. 5, Table 1](../jama_flint_2019_oi_190079.pdf#page=5).

**Source evidence:** The placebo header is `n=62`; living with others is `49 (79.0%)`, alone `10 (16.1%)`, and senior residence `1 (1.6%)`.

**Reported-versus-comparator:** The three displayed categories appear mutually exclusive. Counts give `49+10+1=60`, two below 62; percentages give `79.0+16.1+1.6=96.7%`, 3.3 points below 100%.

**Reasoning procedure:** Header and entries are printed directly. Missing values without a displayed row denominator are an inference. Three one-decimal percentages can accumulate at most about 0.15 percentage point ordinary independent rounding drift, far below 3.3 points; the count gap is exactly 2.

**Calculation:** The three displayed categories appear mutually exclusive. Counts give `49+10+1=60`, two below 62; percentages give `79.0+16.1+1.6=96.7%`, 3.3 points below 100%.

**Alternative source-grounded interpretations:** The categories may intentionally cover only 60 respondents, but no row-specific `n=60` is printed here although other rows show reduced denominators.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** Treating the arm header as the row denominator yields an incomplete distribution and can propagate incorrect missingness or prevalence values; it does not imply a broader study-design defect.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Check participant-level Table 1 derivation and missingness; confirm whether the denominator is 60 or 62 and whether an additional category exists. Were two placebo participants missing living-arrangement data, and if so should the row denominator or missingness be printed?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C004 — Hyperlipidemia percentages reproduce the opposite arm denominators

*Pending Human Adjudication*

**Candidate statement:** Hyperlipidemia percentages reproduce the opposite arm denominators. The printed relationship requires human adjudication.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-001 p. 5, Table 1](../jama_flint_2019_oi_190079.pdf#page=5).

**Source evidence:** Arm headers are olanzapine `n=64` and placebo `n=62`; hyperlipidemia is `18 (29.0%)` and `19 (29.7%)`, respectively.

**Reported-versus-comparator:** With header denominators, `18/64=28.125%` (28.1%) and `19/62=30.645%` (30.6%). The opposite denominators reproduce the print exactly: `18/62=29.032%` (29.0%) and `19/64=29.688%` (29.7%).

**Reasoning procedure:** Counts, percentages, and headers are direct. Transposition of percentage denominators is a diagnostic inference. The header-denominator results lie outside the one-decimal rounding intervals for the printed values.

**Calculation:** With header denominators, `18/64=28.125%` (28.1%) and `19/62=30.645%` (30.6%). The opposite denominators reproduce the print exactly: `18/62=29.032%` (29.0%) and `19/64=29.688%` (29.7%).

**Alternative source-grounded interpretations:** Unprinted row denominators could differ, but a placebo denominator of 64 exceeds its randomized arm and no row-specific denominators appear.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** Arm-specific baseline prevalence can be extracted with a mismatched denominator, affecting reuse of this descriptive result; no treatment-effect conclusion is adjudicated.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Recompute the row from the Table 1 source data and confirm arm assignment, missingness, and displayed denominator. Are the two percentages transposed, or should different row denominators be supplied?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C005 — Barnes participant counts are formatted as decimal-valued counts

*Pending Human Adjudication*

**Candidate statement:** Barnes participant counts are formatted as decimal-valued counts. The printed relationship requires human adjudication.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-001 p. 6, Table 2](../jama_flint_2019_oi_190079.pdf#page=6).

**Source evidence:** Under `No. (%) of Participants`, Barnes global score >0 is `3.0 (4.7)` and `2.0 (3.2)`.

**Reported-versus-comparator:** The count header and percentages identify the fields as participant counts: `3/64=4.6875%` and `2/62=3.2258%`. Numerically, `3.0=3` and `2.0=2`; the check concerns decimal representation under a count label, not an arithmetic mismatch.

**Reasoning procedure:** Decimal-leading fields and header are direct. Inherited continuous-score formatting is inferred. Percentages reconcile at one decimal after integer interpretation; the concern is representation, not percentage rounding.

**Calculation:** The count header and percentages identify the fields as participant counts: `3/64=4.6875%` and `2/62=3.2258%`. Numerically, `3.0=3` and `2.0=2`; the check concerns decimal representation under a count label, not an arithmetic mismatch.

**Alternative source-grounded interpretations:** Numerically, `3.0=3` and `2.0=2`, so the values may be harmless formatting rather than incorrect counts.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** Structured extraction can misclassify these cells as means or scale scores; any downstream risk is limited to representation/classification and does not imply a substantive result error.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Check the Table 2 production format and source variable type; confirm that the cells are participant counts. Should these participant counts be printed as `3` and `2`?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C006 — AIMS participant counts are formatted as decimal-valued counts

*Pending Human Adjudication*

**Candidate statement:** AIMS participant counts are formatted as decimal-valued counts. The printed relationship requires human adjudication.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-001 p. 6, Table 2](../jama_flint_2019_oi_190079.pdf#page=6).

**Source evidence:** Under `No. (%) of Participants`, AIMS overall severity >0 is `2.0 (3.1)` and `2.0 (3.2)`.

**Reported-versus-comparator:** The count header and percentages identify the fields as participant counts: `2/64=3.125%` and `2/62=3.2258%`, reproducing 3.1% and 3.2%. Numerically, `2.0=2`; the check concerns decimal representation under a count label, not an arithmetic mismatch.

**Reasoning procedure:** Values and header are direct. A shared formatting mechanism with the Barnes row is inferred, but this remains a distinct outcome row. Percentages reconcile at one decimal after integer interpretation.

**Calculation:** The count header and percentages identify the fields as participant counts: `2/64=3.125%` and `2/62=3.2258%`, reproducing 3.1% and 3.2%. Numerically, `2.0=2`; the check concerns decimal representation under a count label, not an arithmetic mismatch.

**Alternative source-grounded interpretations:** `2.0` is mathematically equal to 2, so this may be harmless formatting despite the count label.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** The row may be miscoded as a continuous-scale result in automated extraction; no substantive analysis error is established.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Check the table source variable type and rendering format; confirm that both leading fields are counts. Should both AIMS participant counts be printed as `2`?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C007 — The placebo relapse-hospitalization percentage does not round to the printed value

*Pending Human Adjudication*

**Candidate statement:** The placebo relapse-hospitalization percentage does not round to the printed value. The printed relationship requires human adjudication.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-001 p. 8, Results](../jama_flint_2019_oi_190079.pdf#page=8).

**Source evidence:** The paper states that `11 (32.3%) of 34` placebo relapses required psychiatric hospitalization.

**Reported-versus-comparator:** `100*11/34=32.352941...%`, ordinarily 32.4% at one decimal, not 32.3%.

**Reasoning procedure:** Numerator, denominator, and percentage are direct. Truncation or another unprinted denominator is inferred. The exact value is 0.00294 percentage point above the upper boundary of the ordinary `[32.25,32.35)` display interval for 32.3%; this is a very small boundary discrepancy.

**Calculation:** `100*11/34=32.352941...%`, ordinarily 32.4% at one decimal, not 32.3%.

**Alternative source-grounded interpretations:** A truncation convention produces 32.3%; the source does not state that convention here.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** The small mismatch can prevent exact reconciliation in evidence tables, but is unlikely by itself to affect the paper's conclusion.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Recompute from the analysis dataset and determine the percentage-display convention and exact denominator. Was 32.3% intentionally truncated, or should the printed percentage be 32.4%?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C008 — Total-cholesterol absolute unadjusted difference is 4.4, not the printed 4.3, at one decimal

*Pending Human Adjudication*

**Candidate statement:** Total-cholesterol absolute unadjusted difference is 4.4, not the printed 4.3, at one decimal. The printed relationship requires human adjudication.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [DOC-001 p. 9, Table 5](../jama_flint_2019_oi_190079.pdf#page=9).

**Source evidence:** Total cholesterol is `9/64 (14.1%)` versus `6/62 (9.7%)`, with absolute unadjusted difference `4.3%`.

**Reported-versus-comparator:** `100*(9/64-6/62)=4.3850806` percentage points, ordinarily 4.4; the displayed percentages also give `14.1-9.7=4.4`.

**Reasoning procedure:** Counts, denominators, percentages, and difference are direct. A one-tenth transcription/rounding defect is inferred. The exact difference lies outside the ordinary `[4.25,4.35)` one-decimal interval for 4.3.

**Calculation:** `100*(9/64-6/62)=4.3850806` percentage points, ordinarily 4.4; the displayed percentages also give `14.1-9.7=4.4`.

**Alternative source-grounded interpretations:** An unprinted denominator or different computation could differ, but the column is explicitly `absolute unadjusted difference` and arm denominators are printed.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** The risk difference cannot be reproduced from the printed counts and may be copied inconsistently into an evidence product; the small discrepancy does not establish an altered inference.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Recompute the unadjusted risk difference from the final Table 5 dataset and check the display rounding code. What computation or denominator produced 4.3 percentage points, or should it be 4.4?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C009 — LDL absolute unadjusted difference is 4.4, not the printed 4.3, at one decimal

*Pending Human Adjudication*

**Candidate statement:** LDL absolute unadjusted difference is 4.4, not the printed 4.3, at one decimal. The printed relationship requires human adjudication.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [DOC-001 p. 9, Table 5](../jama_flint_2019_oi_190079.pdf#page=9).

**Source evidence:** LDL is `9/64 (14.1%)` versus `6/62 (9.7%)`, with absolute unadjusted difference `4.3%`.

**Reported-versus-comparator:** `100*(9/64-6/62)=4.3850806` percentage points, ordinarily 4.4; `14.1-9.7=4.4`.

**Reasoning procedure:** The separate LDL row is directly printed. A repeated rounding/transcription mechanism is inferred. The exact result is outside the ordinary one-decimal display interval for 4.3.

**Calculation:** `100*(9/64-6/62)=4.3850806` percentage points, ordinarily 4.4; `14.1-9.7=4.4`.

**Alternative source-grounded interpretations:** No different LDL denominator is printed; an unreported computation remains possible.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** This distinct outcome row cannot be reproduced from its printed counts and can propagate an inconsistent risk difference; no material conclusion change is claimed.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Recompute the LDL row from its final source data and inspect the displayed-difference calculation. What computation produced the LDL value 4.3, or should it be 4.4?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C010 — Total-cholesterol and LDL incident-high result vectors are exact duplicates

*Pending Human Adjudication*

**Candidate statement:** Total-cholesterol and LDL incident-high result vectors are exact duplicates. The printed relationship requires human adjudication.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [DOC-001 p. 9, Table 5](../jama_flint_2019_oi_190079.pdf#page=9).

**Source evidence:** Despite different thresholds (`240 mg/dL` total cholesterol and `160 mg/dL` LDL), both rows print `9 (14.1%)` versus `6 (9.7%)`, difference `4.3`, and CI `-8 to 17.2`.

**Reported-versus-comparator:** Field-by-field comparison shows exact equality across the complete displayed result vector for two separately defined outcomes. No probability-of-coincidence claim is made.

**Reasoning procedure:** Duplicate vectors and distinct thresholds are direct. A copied row is inferred and not established. Exact equality at every displayed field.

**Calculation:** Field-by-field comparison shows exact equality across the complete displayed result vector for two separately defined outcomes. No probability-of-coincidence claim is made.

**Alternative source-grounded interpretations:** The same participants may genuinely meet both thresholds and produce identical intervals.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** Exact duplicate rows are a transcription-control signal and may lead to duplicated outcome extraction if one row is wrong; genuine coincidence would make the risk nil, and no conclusion defect is asserted.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Compare outcome-level source counts, participant identities, interval calculations, and table-generation code for the two thresholds. Did the same 9 and 6 participants satisfy both outcome definitions with the same interval, or was one row duplicated?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C011 — The protocol's written ARD operation has the opposite sign from its interpretation rule

*Pending Human Adjudication*

**Candidate statement:** The protocol's written ARD operation has the opposite sign from its interpretation rule. The printed relationship requires human adjudication.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-002 p. 6, statistical analysis](../joi180151supp1_prod.pdf#page=6); [DOC-003 p. 4, ARD method](../joi180151supp2_prod.pdf#page=4).

**Source evidence:** DOC-002 says the RR-multiplied placebo event rate is subtracted from placebo risk, then says negative values favor aspirin. DOC-003 says negative ARD indicates reduced risk with aspirin.

**Reported-versus-comparator:** Let no-aspirin risk be `R0`. For `RR<1`, the prose operation `R0-(RR*R0)=R0(1-RR)>0`, whereas the sign interpretation requires `(RR*R0)-R0=R0(RR-1)<0`.

**Reasoning procedure:** Wording and sign rules are direct. Reversed subtraction order in prose is inferred. Algebraic sign; rounding does not apply.

**Calculation:** Let no-aspirin risk be `R0`. For `RR<1`, the prose operation `R0-(RR*R0)=R0(1-RR)>0`, whereas the sign interpretation requires `(RR*R0)-R0=R0(RR-1)<0`.

**Alternative source-grounded interpretations:** The grammatical referent of “which is then subtracted” may have intended placebo risk to be subtracted from estimated aspirin risk.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** Literal protocol implementation reverses benefit/harm signs and can misdirect secondary implementation; the displayed final ARD signs may nevertheless have been computed correctly.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Inspect the statistical-analysis code/formula and confirm operand order and the intended wording. Which subtraction order was intended for ARD calculation?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C012 — Incident-cancer model selection uses random effects at printed I2=25% although the rule requires greater than 25%

*Pending Human Adjudication*

**Candidate statement:** Incident-cancer model selection uses random effects at printed I2=25% although the rule requires greater than 25%. The printed relationship requires human adjudication.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-003 p. 4, model-selection rule](../joi180151supp2_prod.pdf#page=4); [DOC-003 p. 5, all-patient incident-cancer row](../joi180151supp2_prod.pdf#page=5).

**Source evidence:** When DICs are within 3, random effects are favored if fixed-effect `I2 >25%`; the row prints fixed DIC `27.06`, random DIC `27.93`, I2 `25%`, and selected model `random`.

**Reported-versus-comparator:** `|27.06-27.93|=0.87<3`, so the tie branch applies. Printed `25%` does not satisfy the strict `>25%` condition, which selects fixed at displayed precision. The other 43 model rows were checked and agree with the rule.

**Reasoning procedure:** Rule, values, and selected label are direct. Selection from unrounded I2, an intended inclusive threshold, or a wrong label are alternative inferences. Displayed integer I2 may conceal an unrounded value above 25%; that unprinted precision is the relevant tolerance/alternative.

**Calculation:** `|27.06-27.93|=0.87<3`, so the tie branch applies. Printed `25%` does not satisfy the strict `>25%` condition, which selects fixed at displayed precision. The other 43 model rows were checked and agree with the rule.

**Alternative source-grounded interpretations:** Unrounded I2 may exceed 25%, or the intended rule may be `>=25%`.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** The printed algorithm does not reproduce the model label, which can impede model-choice extraction and replication; no claim is made that the selected estimate or conclusion is invalid.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Inspect unrounded fixed-effect I2 and the model-selection code; confirm the actual inequality and selected model. Was the decision based on an unrounded I2 greater than 25%, was the intended threshold inclusive at 25%, or should the selected-model label be fixed?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C013 — eTable 3 omits the scale needed to interpret ARD and reproduce NNT/NNH

*Pending Human Adjudication*

**Candidate statement:** eTable 3 omits the scale needed to interpret ARD and reproduce NNT/NNH. The printed relationship requires human adjudication.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-002 p. 6, protocol ARD rule](../joi180151supp1_prod.pdf#page=6); [DOC-003 p. 4, ARD/NNT method](../joi180151supp2_prod.pdf#page=4); [DOC-003 p. 15, eTable 3](../joi180151supp2_prod.pdf#page=15).

**Source evidence:** Methods define ARD direction but not its display unit. eTable 3 labels cells only `ARD`; composite all-patients is `-0.41` with NNT `242`, and major bleeding is `0.47` with NNH `210`.

**Reported-versus-comparator:** If `0.41` is a risk proportion, `1/0.41=2.44`; if it is 0.41 percentage point, `100/0.41=243.9`, near 242 with unrounded-input allowance. Likewise 0.47 percentage point gives about 212.8, whereas a proportion gives 2.13. The NNT/NNH values imply percentage points, but the scale is not printed.

**Reasoning procedure:** The missing unit and printed values are direct. Percentage-point interpretation is inferred from reciprocals. Unrounded ARDs can explain small reciprocal differences but cannot supply the absent unit. The scale ambiguity is a factor of 100.

**Calculation:** If `0.41` is a risk proportion, `1/0.41=2.44`; if it is 0.41 percentage point, `100/0.41=243.9`, near 242 with unrounded-input allowance. Likewise 0.47 percentage point gives about 212.8, whereas a proportion gives 2.13. The NNT/NNH values imply percentage points, but the scale is not printed.

**Alternative source-grounded interpretations:** A journal convention or analysis may intend percentage points, or another scaling convention may have been used; none is stated.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** An extractor can interpret 0.41 as 41% instead of 0.41 percentage point, creating a 100-fold scale error in downstream evidence reuse; this does not show that the underlying calculations or conclusions are wrong.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Inspect stored unrounded ARDs and analysis/output scaling; confirm that all 44 ARD cells use one stated unit and that all 18 NNT/NNH values use the same estimand. What is the explicit unit/scale of every ARD in eTable 3, and should the table label the values as percentage points or another stated scale?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C014 — All-patient major-bleeding ARD and NNH do not share a compatible displayed precision

*Pending Human Adjudication*

**Candidate statement:** All-patient major-bleeding ARD and NNH do not share a compatible displayed precision. The printed relationship requires human adjudication.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [DOC-003 p. 4, NNT/NNH method](../joi180151supp2_prod.pdf#page=4); [DOC-003 p. 15, eTable 3](../joi180151supp2_prod.pdf#page=15).

**Source evidence:** All-patient major-bleeding ARD is `0.47` and NNH is `210`.

**Reported-versus-comparator:** If the ARD and NNH summarize the same unrounded percentage-point estimand under an ordinary reciprocal convention, `100/0.47=212.77`; treating the integer 210 as an exact reciprocal gives `100/210=0.47619`, ordinarily displayed as 0.48 rather than 0.47.

**Reasoning procedure:** The pair is direct. Different unprinted effects, nonstandard rounding, or transcription are inferences. Values displayed as 0.47 under nearest two-decimal rounding lie in `[0.465,0.475)`, while 0.47619 lies outside. The source does not state its NNH integer-rounding convention or confirm that the two fields use an identical unrounded estimand, so this is a conditional displayed-precision diagnostic.

**Calculation:** If the ARD and NNH summarize the same unrounded percentage-point estimand under an ordinary reciprocal convention, `100/0.47=212.77`; treating the integer 210 as an exact reciprocal gives `100/210=0.47619`, ordinarily displayed as 0.48 rather than 0.47.

**Alternative source-grounded interpretations:** NNH may use a separately calculated absolute contrast or unstated convention, or the ARD may use nonstandard display rounding.

**Mechanical evidence recheck:** All cited locations and printed values were found in the direct PDFs. The ordinary nearest-rounding, common-estimand reciprocal compatibility test was reproduced, but the source does not state the NNH integer-display convention or establish that ARD and NNH use the identical unrounded estimand. This conditional caveat prevents an unconditional conclusion.

**Quality-control relevance:** ARD and NNH fields cannot be mechanically reconciled and may propagate discordant harm estimates into benefit-harm summaries; no paper-level conclusion error is asserted.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Retrieve the unrounded ARD used for NNH, identify the reciprocal and integer-rounding method, and confirm both fields use the same estimand. Which unrounded ARD and NNH convention produced the pair 0.47 and 210?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C015 — High-risk major-bleeding ARD and NNH do not reconcile

*Pending Human Adjudication*

**Candidate statement:** High-risk major-bleeding ARD and NNH do not reconcile. The printed relationship requires human adjudication.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [DOC-003 p. 4, NNT/NNH method](../joi180151supp2_prod.pdf#page=4); [DOC-003 p. 15, eTable 3](../joi180151supp2_prod.pdf#page=15).

**Source evidence:** High-risk major-bleeding ARD is `0.64` and NNH is `152`.

**Reported-versus-comparator:** `100/0.64=156.25`; NNH 152 implies `100/152=0.65789`, ordinarily 0.66 rather than 0.64.

**Reasoning procedure:** The pair is direct. Different hidden inputs or transcription are inferred. The implied 0.65789 lies outside the ordinary `[0.635,0.645)` interval displaying as 0.64; `SP1-007` places the reciprocal range around 155.0-157.5, not 152.

**Calculation:** `100/0.64=156.25`; NNH 152 implies `100/152=0.65789`, ordinarily 0.66 rather than 0.64.

**Alternative source-grounded interpretations:** NNH could be based on a separately modeled absolute effect not represented by the ARD cell, but the source does not state this.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** The population-specific harm summary is not reproducible and can propagate inconsistent ARD/NNH extraction; this does not establish a changed meta-analytic conclusion.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Retrieve the high-risk unrounded ARD and NNH calculation; confirm estimand, scale, and integer-rounding rule. What unrounded value or alternative rule produced NNH 152?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C016 — Diabetes major-bleeding ARD and NNH do not reconcile

*Pending Human Adjudication*

**Candidate statement:** Diabetes major-bleeding ARD and NNH do not reconcile. The printed relationship requires human adjudication.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [DOC-003 p. 4, NNT/NNH method](../joi180151supp2_prod.pdf#page=4); [DOC-003 p. 15, eTable 3](../joi180151supp2_prod.pdf#page=15).

**Source evidence:** Diabetes major-bleeding ARD is `0.80` and NNH is `121`.

**Reported-versus-comparator:** `100/0.80=125`; NNH 121 implies `100/121=0.82645`, ordinarily 0.83 rather than 0.80.

**Reasoning procedure:** The pair is direct. A different hidden estimate is inferred. The implied 0.82645 lies outside the ordinary `[0.795,0.805)` interval displaying as 0.80; `SP1-007` places the compatible reciprocal range around 124.2-125.8, not 121.

**Calculation:** `100/0.80=125`; NNH 121 implies `100/121=0.82645`, ordinarily 0.83 rather than 0.80.

**Alternative source-grounded interpretations:** A separately modeled NNH could exist, but it is not identified in the table or methods.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** The diabetes harm pair can propagate inconsistent reciprocal summaries into evidence reuse; no conclusion-level impact is established.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Retrieve the diabetes unrounded ARD and reciprocal calculation; confirm scale, estimand, and NNH rounding. What exact ARD and reciprocal convention produced NNH 121?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C017 — Low- and high-risk total-stroke event counts do not sum to the all-participant counts

*Pending Human Adjudication*

**Candidate statement:** Low- and high-risk total-stroke event counts do not sum to the all-participant counts. The printed relationship requires human adjudication.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** [DOC-003 p. 16, eTable 4](../joi180151supp2_prod.pdf#page=16).

**Source evidence:** Aspirin rows are all `1116/73883`, low `752/56212`, high `381/17671`; no-aspirin rows are all `1136/72317`, low `788/56354`, high `380/15963`.

**Reported-versus-comparator:** Denominators partition exactly: `56212+17671=73883` and `56354+15963=72317`. Events do not: aspirin `752+381=1133`, 17 above 1116; no aspirin `788+380=1168`, 32 above 1136.

**Reasoning procedure:** The four rows are direct. Different definitions/availability or transcription are inferred. Integer identities; no rounding.

**Calculation:** Denominators partition exactly: `56212+17671=73883` and `56354+15963=72317`. Events do not: aspirin `752+381=1133`, 17 above 1116; no aspirin `788+380=1168`, 32 above 1136.

**Alternative source-grounded interpretations:** Low/high outcome definitions or study availability could differ even with exact denominator partitioning, but eTable 4 states no exception.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** Population-stratified event extraction cannot be reconciled to the overall row, potentially affecting subgroup evidence tables; no claim is made about the fitted HRs or conclusions.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Reconstruct the all/low/high event counts from the final population flags and outcome dataset; document any nonpartitioning definition. Why do the exact low/high participant partitions not carry an additive total-stroke event partition?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C018 — Detection-bias graph represents 9 low/4 unclear trials while eTable 2 contains 8 low/5 unclear

*Pending Human Adjudication*

**Candidate statement:** Detection-bias graph represents 9 low/4 unclear trials while eTable 2 contains 8 low/5 unclear. The printed relationship requires human adjudication.

**Category:** Denominator, proportion, or total inconsistency

**Exact source locations:** eTable 2 on [DOC-003 p. 10](../joi180151supp2_prod.pdf#page=10), [p. 11](../joi180151supp2_prod.pdf#page=11), [p. 12](../joi180151supp2_prod.pdf#page=12), [p. 13](../joi180151supp2_prod.pdf#page=13), and [p. 14](../joi180151supp2_prod.pdf#page=14); [DOC-003 p. 20, eFigure 2](../joi180151supp2_prod.pdf#page=20).

**Source evidence:** Detection is unclear for BDS, PHS, HOT, WHS, and ASCEND (5) and low for the other 8 trials. The graph boundary is near the approximately 69% low/31% unclear position used for 9/4 domains, not the approximately 62%/38% table split. The other six graphical domains reproduce the table.

**Reported-versus-comparator:** The table gives low `8/13=61.54%` and unclear `5/13=38.46%`; a 9/4 graphic gives `69.23%/30.77%`, one trial or 7.69 percentage points different.

**Reasoning procedure:** All 13 table categories and the graphic boundary are direct observations. Duplication of another domain's proportions or use of an earlier classification set is inferred. The graphic has no numeric labels, so boundary reading is visual; the 20% grid and alignment with exact 9/4 domains make the one-trial difference distinguishable.

**Calculation:** The table gives low `8/13=61.54%` and unclear `5/13=38.46%`; a 9/4 graphic gives `69.23%/30.77%`, one trial or 7.69 percentage points different.

**Alternative source-grounded interpretations:** One table cell may have been intended as low, or the graph may reflect a different finalized set.

**Mechanical evidence recheck:** All 13 table classifications and the direct-source graph were found. The exact 8/5 table split was reproduced; the graph's approximately 9/4 reading was reproduced from axis position and alignment with other bars, but the graph has no numeric segment labels or plotted coordinates.

**Quality-control relevance:** Graph-based and table-based risk-of-bias extraction yield different summaries and may propagate different domain counts; this is a reporting-consistency issue, not a misconduct or validity judgment.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Regenerate the graph from the 13 final categorical rows and compare the underlying graphic input with eTable 2. Which detection-bias classification set generated eFigure 2, and which table or graphic reflects the intended final assessment?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C019 — The printed Egger coefficient and SE cannot produce the printed t statistic at displayed precision

*Pending Human Adjudication*

**Candidate statement:** The printed Egger coefficient and SE cannot produce the printed t statistic at displayed precision. The printed relationship requires human adjudication.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-003 p. 21, eFigure 3](../joi180151supp2_prod.pdf#page=21).

**Source evidence:** Egger coefficient `-0.47`, SE `0.77`, `t=-0.59`, and `P=0.57`.

**Reported-versus-comparator:** For a coefficient/SE t ratio, `-0.47/0.77=-0.6104`, about -0.61. With two-decimal rounding, coefficient magnitude `[0.465,0.475)` divided by SE `[0.765,0.775)` yields about `[0.600,0.621]`, excluding 0.59. The printed t and P remain mutually plausible for about 8 df.

**Reasoning procedure:** The four fields are direct. A different precision/output field or alternative Egger implementation is inferred. Full ordinary rounded-input intervals are used; no unreported model convention is imposed.

**Calculation:** For a coefficient/SE t ratio, `-0.47/0.77=-0.6104`, about -0.61. With two-decimal rounding, coefficient magnitude `[0.465,0.475)` divided by SE `[0.765,0.775)` yields about `[0.600,0.621]`, excluding 0.59. The printed t and P remain mutually plausible for about 8 df.

**Alternative source-grounded interpretations:** The named coefficient may not be the numerator of the displayed t under an unstated implementation, although the figure defines no alternative relationship.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** The inferential vector cannot be reproduced and may be copied into publication-bias assessments; no claim is made that the funnel-plot conclusion changes.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Inspect the Egger model output, exact coefficient/SE, degrees of freedom, and test definition; recompute t and P from the intended fields. What unrounded coefficient and SE, or what alternative test definition, produced `t=-0.59`?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C020 — Twelve non-ASCEND total-stroke forest rows do not reproduce eTable 4's event totals

*Pending Human Adjudication*

**Candidate statement:** Twelve non-ASCEND total-stroke forest rows do not reproduce eTable 4's event totals. The printed relationship requires human adjudication.

**Category:** Numeric or arithmetic inconsistency

**Exact source locations:** [DOC-003 p. 16, eTable 4](../joi180151supp2_prod.pdf#page=16); [DOC-003 p. 24, total-stroke forest plot](../joi180151supp2_prod.pdf#page=24); [DOC-002 p. 7, ASCEND protocol change](../joi180151supp1_prod.pdf#page=7).

**Source evidence:** eTable 4 reports 12 studies, aspirin `1116/73883` and no aspirin `1136/72317`. All 13 forest rows total `1358/81623` and `1397/80057`; ASCEND contributes `240/7740` and `263/7740`. Equivalently, the 12 non-ASCEND forest rows total `1118/73883` and `1134/72317`.

**Reported-versus-comparator:** Removing ASCEND exactly reproduces denominators: `81623-7740=73883` and `80057-7740=72317`. Events do not: `1358-240=1118` versus 1116 and `1397-263=1134` versus 1136. Forest minus table is `+2` aspirin and `-2` no aspirin; total events are preserved but two events shift arms.

**Reasoning procedure:** Table totals and every forest row are direct. Arm transposition, separate curation, or data revision are inferred. Integer event identities; no rounding.

**Calculation:** Removing ASCEND exactly reproduces denominators: `81623-7740=73883` and `80057-7740=72317`. Events do not: `1358-240=1118` versus 1116 and `1397-263=1134` versus 1136. Forest minus table is `+2` aspirin and `-2` no aspirin; total events are preserved but two events shift arms.

**Alternative source-grounded interpretations:** Bayesian and frequentist displays may use different event adjudications despite identical studies and denominators, but no such distinction is supplied.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** Two supplied extractions of the same 12-study population yield different arm counts and could propagate inconsistent event data into a review; this does not by itself establish a different pooled conclusion.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Sum the final 12-study dataset by arm, compare table and forest input files, and document any legitimate analysis-set or event-version distinction. Which 12-study arm event totals are intended, and what accounts for the two-event transfer?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C021 — A low-risk all-MI NNT is printed although the displayed ARD confidence interval reaches 0.00

*Pending Human Adjudication*

**Candidate statement:** A low-risk all-MI NNT is printed although the displayed ARD confidence interval reaches 0.00. The printed relationship requires human adjudication.

**Category:** Statistical reporting inconsistency

**Exact source locations:** [DOC-003 p. 4, NNT/NNH rule](../joi180151supp2_prod.pdf#page=4); [DOC-003 p. 15, eTable 3](../joi180151supp2_prod.pdf#page=15).

**Source evidence:** The methods/table state that NNT/NNH is reported for statistically significant risk changes. Low-risk all-MI ARD is `-0.27 (-0.49 to 0.00)` and NNT is `366`; no unrounded endpoint footnote is supplied.

**Reported-versus-comparator:** At displayed precision, a two-sided 95% CI reaching the null at 0.00 does not exclude zero, while an NNT is shown under an exclude-null reporting rule.

**Reasoning procedure:** CI, NNT, and reporting rule are direct. A negative unrounded endpoint or retained NNT is inferred. The unrounded upper endpoint may be slightly below zero and round to 0.00; unlike other rounded-to-null cells, this row provides no exact endpoint note.

**Calculation:** At displayed precision, a two-sided 95% CI reaching the null at 0.00 does not exclude zero, while an NNT is shown under an exclude-null reporting rule.

**Alternative source-grounded interpretations:** The unrounded interval may exclude zero and support the NNT, or the NNT may have been retained despite a null-reaching interval.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** Significance classification and NNT extraction can diverge from the displayed interval, potentially affecting summary tables; no claim is made that the underlying result is nonsignificant without unrounded evidence.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Retrieve the unrounded ARD interval and the flag used to display NNT; confirm sidedness/confidence level and reporting logic. What is the unrounded upper ARD confidence limit for low-risk all MI, and does it exclude zero under the analysis used to decide whether NNT 366 should be displayed?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C022 — The diabetes total-stroke HR endpoint is labelled as both a credible and a confidence limit

*Pending Human Adjudication*

**Candidate statement:** The diabetes total-stroke HR endpoint is labelled as both a credible and a confidence limit. The printed relationship requires human adjudication.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-003 p. 16, eTable 4](../joi180151supp2_prod.pdf#page=16).

**Source evidence:** The HR column is `HR (95% CrI)`; diabetes is `0.78 (0.61 to 1.00)*`; the asterisk says `Upper confidence interval 1.004`. The adjacent ARR is separately labelled with a 95% CI.

**Reported-versus-comparator:** `CrI` and `CI` denote distinct inferential interval types in this package, and the footnote is attached to the starred HR/CrI endpoint.

**Reasoning procedure:** Header and footnote are direct. Informal use of “confidence” or a wrong header is inferred. Terminology/label comparison; rounding is relevant only to 1.00 versus 1.004, which the footnote explains.

**Calculation:** `CrI` and `CI` denote distinct inferential interval types in this package, and the footnote is attached to the starred HR/CrI endpoint.

**Alternative source-grounded interpretations:** The footnote may use “confidence interval” informally, or the HR interval could be frequentist despite the Bayesian methods/header; the latter is not otherwise supported.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** Extractors can classify the same interval as Bayesian or frequentist, affecting evidence-model metadata; the numeric endpoint itself is not challenged.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Check the analysis output that generated the HR interval and identify whether 1.004 is a posterior credible or frequentist confidence limit. Should the footnote read `upper credible interval limit 1.004`, or is the HR interval type in the header incorrect?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C023 — The <=100-mg all-MI sensitivity endpoint is labelled as both a credible and a confidence limit

*Pending Human Adjudication*

**Candidate statement:** The <=100-mg all-MI sensitivity endpoint is labelled as both a credible and a confidence limit. The printed relationship requires human adjudication.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-003 p. 18, eTable 6](../joi180151supp2_prod.pdf#page=18).

**Source evidence:** The table says `Hazard Ratio (95% CrI)`, prints all-MI HR `0.87 (0.76 to 1.00)*` for aspirin dose <=100 mg, and footnotes `Upper confidence interval 0.9989`.

**Reported-versus-comparator:** The footnote is attached to a starred endpoint in a table explicitly defining 95% credible intervals; CI and CrI are distinct labels.

**Reasoning procedure:** Header, cell, and footnote are direct. Informal terminology or a wrong header is inferred. Terminology/label comparison. The footnote supplies the unrounded 0.9989 value and resolves the numeric null-boundary question, not the interval-type label.

**Calculation:** The footnote is attached to a starred endpoint in a table explicitly defining 95% credible intervals; CI and CrI are distinct labels.

**Alternative source-grounded interpretations:** “Confidence interval” may be informal wording; alternatively the sensitivity table may use frequentist intervals despite its CrI label, but no exception is stated.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** Secondary extraction may misclassify the interval type and significance framework; the value and direction are not otherwise challenged.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Inspect the sensitivity-analysis output and confirm whether 0.9989 is a posterior credible limit or frequentist confidence limit. Is 0.9989 the upper credible limit, or should the table's interval-type label be CI rather than CrI?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

## C024 — ASCEND ischemic-stroke events are included in the total-stroke forest plot despite explicit exclusion from total stroke

*Pending Human Adjudication*

**Candidate statement:** ASCEND ischemic-stroke events are included in the total-stroke forest plot despite explicit exclusion from total stroke. The printed relationship requires human adjudication.

**Category:** Measure, label, or scale inconsistency

**Exact source locations:** [DOC-003 p. 9, eTable 1](../joi180151supp2_prod.pdf#page=9); [DOC-003 p. 16, eTable 4](../joi180151supp2_prod.pdf#page=16); [DOC-003 p. 24, total- and ischemic-stroke forest plots](../joi180151supp2_prod.pdf#page=24); [DOC-002 p. 7, protocol explanation](../joi180151supp1_prod.pdf#page=7).

**Source evidence:** eTable 1 says ASCEND total stroke is `Not included in analysis - only reports ischemic stroke`. eTable 4 consequently has 12 total-stroke studies. The total-stroke forest plot nevertheless includes ASCEND `240/7740` versus `263/7740`; the exact row also appears in the separate ischemic-stroke plot.

**Reported-versus-comparator:** A measure explicitly classified as ischemic stroke should not be labelled and pooled as total stroke without an exception. Adding ASCEND denominators to the 12-study table totals exactly produces the 13-study forest totals: `73883+7740=81623` and `72317+7740=80057`, identifying the added row. The separate non-ASCEND arm-count inconsistency is C020, not merged here.

**Reasoning procedure:** Outcome-definition statement, row values, and appearances are direct. A broader frequentist convention, copied row, or analysis-set error is inferred. Exact row identity and integer denominators; rounding does not apply.

**Calculation:** A measure explicitly classified as ischemic stroke should not be labelled and pooled as total stroke without an exception. Adding ASCEND denominators to the 12-study table totals exactly produces the 13-study forest totals: `73883+7740=81623` and `72317+7740=80057`, identifying the added row. The separate non-ASCEND arm-count inconsistency is C020, not merged here.

**Alternative source-grounded interpretations:** The frequentist forest analysis may intentionally use a broader available-event convention than the Bayesian table, but no caption or method states that exception.

**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question.

**Quality-control relevance:** Total-stroke extraction may include an explicitly ischemic-only trial record and alter outcome classification in downstream synthesis; this candidate does not establish that the paper's conclusion is wrong.

**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed.

**Human verification steps:** Inspect the frequentist analysis code and final outcome mapping for ASCEND; determine whether the row should be removed, relabelled, or accompanied by a stated definition exception. Should ASCEND be removed from the total-stroke forest plot, or should the outcome label/caption and definition table explicitly describe the broader convention used?

**Human adjudication fields:**

- Validity: —
- Importance: —
- Action: —
- Initials: —
- Notes: —

