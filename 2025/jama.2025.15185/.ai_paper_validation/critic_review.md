# Critic Review of Evidence-Verifier Output

## Scope and disposition

- Input reviewed: the 10 findings classified `Verified` by the evidence verifier.
- Review boundary: no new issues were sought and no external information was used.
- Final disposition: **9 retained as Minor**, **0 retained as Major**, **0 retained as Uncertain**, and **1 rejected**.
- Taxonomy normalization: each retained finding is assigned one of the five allowed issue categories. Claims about which source is correct, participant-level misclassification, clinical importance, or effects on unreported analyses have been removed.

## Retained findings

### 1. eTable 6 overall adverse-event total is one event short

- **Original verifier finding:** 1
- **Category:** Arithmetic inconsistency
- **Severity:** Minor
- **Issue statement:** The supplement reports 145 prespecified adverse events overall, but its arm totals and every displayed classification block sum to 146.
- **Evidence:** `DOC-004` / `supplement_3_results`, `joi250066supp3_prod_1761597796.4701.pdf`, PDF p. 17, eTable 6: overall `n=145`, placebo `67`, levodopa `79`; intensity counts `58, 86, 2`; outcome counts `1, 29, 116`; drug-relation counts `2, 66, 23, 2, 39, 14`. `DOC-001` / `main_article`, `jama_engelter_2025_oi_250066_1761597796.45511.pdf`, PDF p. 6, Table 2 and Adverse Events text: arm totals `79` and `67` and overall total `146`.
- **Comparison/calculation:** `67+79=146`; `58+86+2=146`; `1+29+116=146`; `2+66+23+2+39+14=146`. Each is one greater than the displayed overall `145`.
- **Bounded impact:** One-event error in the supplement header; the arm counts and displayed breakdowns are not shown to be wrong.
- **Critic rationale:** Retained because multiple independent sums directly establish the arithmetic error. Cross-document evidence corroborates it, but the most specific category is Arithmetic inconsistency.

### 2. Supplementary stroke-type arm counts do not reconcile with its overall counts or the main article

- **Original verifier finding:** 2
- **Category:** Cross-document inconsistency
- **Severity:** Minor
- **Issue statement:** The supplement reports levodopa stroke-type counts of 263 ischemic and 44 hemorrhagic, whereas the main article reports 260 and 47, and only the main-article values reproduce the supplement's overall counts.
- **Evidence:** `DOC-004` / `supplement_3_results`, PDF p. 10, eTable 1: overall/placebo/levodopa ischemic `519/259/263` and hemorrhagic `91/44/44`. `DOC-001` / `main_article`, PDF p. 4, Table 1, Type of stroke: levodopa ischemic `260 (84.7%)`, hemorrhagic `47 (15.3%)`; placebo ischemic `259 (85.5%)`, hemorrhagic `44 (14.5%)`.
- **Comparison/calculation:** Supplement arm sums are `259+263=522`, not 519, and `44+44=88`, not 91. Main-article arm sums are `259+260=519` and `44+47=91`.
- **Bounded impact:** The documents differ by three levodopa participants in each stroke-type category; arm totals remain 307. The supplied evidence does not establish which underlying classification is correct.
- **Critic rationale:** Retained after removing the verifier's stronger claim that participants were actually “misclassified,” which cannot be established without raw data.

### 3. Onset-to-randomization timing differs by 4 to 5 median days

- **Original verifier finding:** 3
- **Category:** Cross-document inconsistency
- **Severity:** Minor
- **Issue statement:** The main article reports a median of 3 days from stroke onset to randomization in each arm, while the identically described supplement row reports 7 days for levodopa and 8 days for placebo.
- **Evidence:** `DOC-001` / `main_article`, PDF p. 4, Table 1, “Time from stroke onset to randomization, median (IQR), d”: levodopa `3.0 (2.0-5.0)`, placebo `3.0 (2.0-5.0)`. `DOC-004` / `supplement_3_results`, PDF p. 11, eTable 1, “Median time from stroke onset to randomization [IQR]”: overall `7 [5,10]`, placebo `8 [5,10]`, levodopa `7 [5-11]`.
- **Comparison/calculation:** Levodopa median difference: `7-3=4` days. Placebo median difference: `8-3=5` days.
- **Bounded impact:** The package gives incompatible descriptive timing values. It does not establish which is correct or demonstrate a change to the reported treatment-effect estimate.
- **Critic rationale:** Retained because the labels, units, and comparison populations match. Kept Minor to avoid an unsupported clinical-importance judgment.

### 4. PRAI placebo numerator differs by one participant

- **Original verifier finding:** 4
- **Category:** Cross-document inconsistency
- **Severity:** Minor
- **Issue statement:** The main article reports 52 of 270 placebo participants with no or no relevant improvement, whereas eTable 4 reports 51 of 270.
- **Evidence:** `DOC-001` / `main_article`, PDF p. 6, Secondary Outcomes: levodopa `51/276 (18%)`, placebo `52/270 (19%)`. `DOC-004` / `supplement_3_results`, PDF p. 15, eTable 4, PRAI row: levodopa `51/276 (18.48%)`, placebo `51/270 (18.89%)`.
- **Comparison/calculation:** `52/270=19.26%`, consistent with the main article's rounded 19%; `51/270=18.89%`, exactly matching eTable 4. The placebo numerators differ by one.
- **Bounded impact:** One participant and 0.37 percentage points in the unrounded placebo rate; denominators and levodopa values agree.
- **Critic rationale:** Retained because each document's percentage is internally consistent with its own incompatible numerator.

### 5. Estimands 3 and 4 use an analysis-population label inconsistent with the stated definition

- **Original verifier finding:** 5
- **Category:** Statistical reporting inconsistency
- **Severity:** Minor
- **Issue statement:** eTable 2 labels Estimands 3 and 4 as “Full analysis set” even though that set is defined as excluding deaths and both estimands report `N=610`, incorporating the 28 deaths.
- **Evidence:** `DOC-004` / `supplement_3_results`, PDF p. 12, eTable 2 population definition: participants who died before the 3-month assessment were excluded from the full analysis set. PDF p. 13: Estimand 1, Full analysis set, `N=582`; Estimand 3, Full analysis set, deceased participants' FMA values imputed, `N=610`; Estimand 4, Full analysis set, death-and-FMA endpoint, `N=610`. PDF p. 16, eTable 5: 28 participant deaths.
- **Comparison/calculation:** `610-28=582`, matching Estimand 1's stated full-analysis-set count; Estimands 3 and 4 use `582+28=610`.
- **Bounded impact:** The population labels conflict with the supplied definition. The displayed N values and death-handling descriptions still identify the apparent analyzed populations; the numerical estimates are not shown to be wrong.
- **Critic rationale:** Retained as a definitional reporting inconsistency, but reduced from the verifier's Moderate assessment to Minor because the N and intercurrent-event descriptions make the likely populations visible.

### 6. Estimand 11's written conjunction cannot produce its reported N

- **Original verifier finding:** 6
- **Category:** Statistical reporting inconsistency
- **Severity:** Minor
- **Issue statement:** eTable 3 says Estimand 11 excludes participants meeting both the low-rehabilitation and low-medication conditions, but excluding only that intersection cannot yield the reported `N=395`.
- **Evidence:** `DOC-004` / `supplement_3_results`, PDF p. 14, eTable 3, Estimand 11: exclusion of participants with low rehabilitation “and” less than 80% medication, `N=395`. PDF p. 13, eTable 2: excluding low medication alone gives `N=496`; excluding low rehabilitation alone gives `N=450`. `DOC-001` / `main_article`, PDF p. 4, Statistical Analyses: the post hoc analysis includes only participants meeting both adherence requirements.
- **Comparison/calculation:** From base `N=582`, the low-medication set has `582-496=86` participants and the low-rehabilitation set has `582-450=132`. Their intersection is at most 86; excluding only the intersection must retain at least `582-86=496`, not 395. The reported N excludes 187 participants, which is feasible for the union (`86+132-187=31` in both low-adherence sets).
- **Bounded impact:** The supplement's literal population rule is not reproducible. The main article wording and displayed N support the apparent intended rule, so the estimate itself is not shown to be numerically wrong.
- **Critic rationale:** Retained because the set bound is valid and document-grounded. Reduced from Moderate to Minor because the main article and N substantially resolve the intended analysis population.

### 7. eFigure 7 assigns incompatible labels to the PH3 subgroups

- **Original verifier finding:** 7
- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Issue statement:** eFigure 7's color key calls the PH3 series “moderate-severe impairment” and “very severe impairment,” while the figure legend defines the two subgroups as severe (`FMA <=35`) and mild to moderate (`FMA >35`).
- **Evidence:** `DOC-004` / `supplement_3_results`, PDF p. 27, eFigure 7: green key “moderate-severe impairment”; purple key “very severe impairment”; PH3 legend “severe impairment (<=35 points) vs. mild to moderate impairment (>35 points).”
- **Comparison/logical basis:** Neither color-key descriptor matches the corresponding two threshold-defined labels, and no alternate mapping is given.
- **Bounded impact:** The two plotted subgroup estimates cannot be mapped confidently to the stated threshold groups from the figure alone; points and intervals are unchanged.
- **Critic rationale:** Retained because the conflicting labels are visible on the same figure and directly impair interpretation of the subgroup series.

### 8. eTable 4 mislabels the mRS odds ratio as an FMA mean difference

- **Original verifier finding:** 8
- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Issue statement:** eTable 4 places the mRS estimate under a column headed as a mean difference on FMA, while the main article identifies the same value as an adjusted odds ratio.
- **Evidence:** `DOC-004` / `supplement_3_results`, PDF p. 15, eTable 4: effect-column header “Estimated Effect of Levodopa: Mean Difference on FMA, [CI]”; mRS row `0.93 [0.69-1.23]`. `DOC-001` / `main_article`, PDF p. 6, Secondary Outcomes: adjusted odds ratio `0.93 (95% CI, 0.69-1.23)`.
- **Comparison/logical basis:** An odds ratio is neither a mean difference nor measured in FMA points.
- **Bounded impact:** The supplement can cause the mRS effect measure to be misread; the main text supplies the correct metric and the numeric estimate agrees.
- **Critic rationale:** Retained because this is a direct metric-label mismatch, not a methodological critique.

### 9. eFigure 6 contains a conflicting embedded figure number

- **Original verifier finding:** 10
- **Category:** Presentation inconsistency
- **Severity:** Minor
- **Issue statement:** The supplement identifies the spline plot as eFigure 6 but its embedded caption calls it Figure 4, while eFigure 4 is a different forest plot.
- **Evidence:** `DOC-004` / `supplement_3_results`, PDF p. 26: page heading “eFigure 6. Nonlinear association between baseline and three-month FMA (spline model)” and embedded caption “Figure 4: Main estimate including FMAA at baseline as spline: estimated marginal effects.” PDF pp. 23-24: eFigure 4 is the forest plot of FMA estimands at 3 months.
- **Comparison/logical basis:** The p. 26 plot carries two incompatible figure identifiers, and Figure 4 already identifies a separate plot.
- **Bounded impact:** Figure-numbering and cross-reference ambiguity only; the spline plot remains identifiable.
- **Critic rationale:** Retained as a narrowly stated presentation error.

## Rejected finding

### Original verifier finding 9: eFigure 5 title versus change-score axis

- **Decision:** Rejected
- **Reason:** The title “FMA at Three Months by Treatment Arm and Center” identifies the outcome and assessment time but does not explicitly state that raw 3-month scores, rather than baseline-to-3-month change scores, are plotted. The y-axis explicitly identifies “change Visit 1 to Visit 3,” so the figure itself discloses the plotted quantity. Inferring that the title necessarily promises a raw score is semantic and not a document-demonstrated contradiction. Retaining it would overstate a shorthand title as a verified reporting inconsistency.

## Consolidation notes for report generation

- Retain original verifier finding numbers `1-8` and `10`; omit `9`.
- Use the revised issue statements and bounded-impact language above.
- Do not state that the supplement stroke counts prove participant misclassification or that either document contains the correct source-data values.
- Do not elevate the timing discrepancy on clinical or methodological grounds.
- Do not claim that the Estimand 3, 4, or 11 estimates are numerically wrong; the verified problems concern population labels/rules.
