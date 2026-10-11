# Statistical consistency pass 1 — Workflow 1.6

Fresh mandatory agent runtime identifier: /root/statistical_pass_1. Model gpt-6.1-sol; reasoning effort high; start mode FRESH_SPAWN. Exact scope S001–S137, processed as disjoint sequential scopes S001–S043 (43 groups) and S044–S137 (94 groups). Every historical outcome within grouped rows, every baseline comparison in each of two PaCO2 strata, and every plotted inference is included. Canonical durable coverage: [relationship inventory](../statistics/relationship_inventory.md). All137 records explicitly PASS_1_COMPLETE; pass2 reserved for a distinct fresh high-effort agent. No scientific-coverage gap remains.

## Source authority and checks

Read the supplied scope, review contract, settings, report specification, tooling, routing, coverage and fresh main/support/results maps. Source-linked reusable native text was a locator; selected direct Poppler pdftotext layout reads confirmed main pp1,4,6,7,8, protocol pp15,17,33,34 and results pp2,4,7,9. Source-matched reusable rendered results pp4,7,9 were inspected visually for percentage cells, outcome tuples and eFigure axis/P. No source, reused asset, provider setting or other agent artifact was modified. No fallback package or OCR was required. No web, old candidate queue or old report conclusion was read.

All applicable confidence intervals contain their printed point estimates and have ordered endpoints. Protective directions, adverse-event directions, confidence levels and OR versus absolute percentage-point/days scales were checked. No CI endpoint-order or point-containment candidate was found. All group/contrast repetitions were aligned by outcome, population, time and inferential definition.

The main REPORT p4 explicitly names two-tailed inference, chi-square for primary and specified secondary proportions, multiple/multilevel logistic ORs, and separate day7/time-to-death-day90 log-rank tests. It does not specify the chi-square variant, row-specific secondary/exploratory selection, CI construction, variance estimator or continuous difference estimand. PLAN pp33–34 gives chi-square/Fisher for categorical predictors and Student t/Mann–Whitney for continuous variables/stays, but not realized row-by-row selection or confidence-interval rules. This plan is corroborating method context; it is not proof that a different method was forbidden. Historical studies in PLAN p17 lack their original inferential methods in the supplied package, so their P values were not reconstructed by assuming a common method.

Conditional numerical calculations used JavaScript arithmetic only. For a two-by-two table with HF event count a among n and NIV b among m, Pearson chi-square uses N(ad−bc)^2 divided by row-total and column-total products, with N=n+m and cells a,n−a,b,m−b; tail probability uses the chi-square distribution with1 degree of freedom. This degree follows the explicitly stated two-group binary comparison in the diagnostic; it is not a claim about an unreported adjusted model. Yates subtracts N/2 from the absolute cross-product difference, bounded atzero. Fisher diagnostics condition on the printed margins and sum hypergeometric probabilities no larger than the observed table probability, two-sided as source context specifies. Likelihood-ratio chi-square diagnoses use2 times the sum of observed log observed/expected cells. These exact-count calculations are diagnostic whenever the supplied source does not fix the corresponding variant. They are not reconstructions of unreported adjusted estimators.

## Candidate observations for coordinator registration

These14 observations carry checker-local labels ST01, ST02, ST03A, ST03B, and ST04–ST13, without C IDs. Distinct numerical/cell rules remain distinct; genuine duplicates may be merged across checker lanes before registration. All await human adjudication. No severity, acceptance or correction is assigned.

### ST01 — Respiratory-failure absolute difference differs within main REPORT

- Relationship IDs: S003, S044 as corroboration.
- Compared locations/roles: REPORT [main p1 abstract Results](../../../jama_thille_2019_oi_190108.pdf#page=1), REPORT [main p6 Secondary Outcomes](../../../jama_thille_2019_oi_190108.pdf#page=6), and REPORT [main p8 Table2 respiratory-failure row](../../../jama_thille_2019_oi_190108.pdf#page=8).
- Source evidence: abstract and narrative difference−8.7%, CI−15.2 to−1.8 and P=.01; Table2 same outcome/counts88/302 and70/339, difference−8.5%, same CI/P.
- Rule/calculation: matched printed estimate should agree at common precision;100(70/339−88/302)=−8.490105pp, which displays−8.5. The .2pp printed difference is independent of interval or P conventions.
- Proposed category: Numeric or arithmetic inconsistency; role basis REPORT versus REPORT within main, S_W. Supplement corroborates counts only.
- Missing definition/alternative: an unlabelled different estimate/population could explain the difference, although identical row/outcome/CI and complete denominators indicate matching.
- Exact human question: Does−8.7 describe a separately defined estimator/population, or should the main repeated effect match the Table2 exact-count risk difference?

### ST02 — Respiratory-failure P differs between REPORT documents

- Relationship IDs: S003 and S044.
- Compared locations/roles: REPORT [main p1](../../../jama_thille_2019_oi_190108.pdf#page=1), REPORT [main p6](../../../jama_thille_2019_oi_190108.pdf#page=6), REPORT [main p8 Table2](../../../jama_thille_2019_oi_190108.pdf#page=8), and REPORT [results p2 eTable1 first row](../../../joi190108supp2_prod.pdf#page=2). Main REPORT [p4 statistical rule](../../../jama_thille_2019_oi_190108.pdf#page=4) establishes chi-square comparison.
- Source evidence: same day7 respiratory failure88/302 versus70/339; main P=.01, supplement P=.02.
- Rule: a matched inference reported at identical two-decimal precision should agree if its chi-square definition is the same.
- Conditional diagnostics: Pearson chi-square6.198500 gives P=.012785863, rounding .01; continuity-corrected P=.016490410 rounds .02; Fisher P=.013361178 rounds .01. The printed values are genuinely different; these variants demonstrate a supplied-source question rather than establishing an identical realized test.
- Proposed category: Cross-document numeric inconsistency; REPORT main versus REPORT results supplement, S_C.
- Missing definition/alternative: the supplement may use continuity correction while main uses uncorrected chi-square, not disclosed by row.
- Exact human question: Were distinct chi-square conventions intentionally used for this otherwise identical result, and which P belongs to each specified inference?

### ST03A — Percent heading covers the ICU length-of-stay difference

- Relationship ID: S007.
- Compared locations/roles: REPORT [main p8 Table2 absolute-difference heading and length-of-stay row block](../../../jama_thille_2019_oi_190108.pdf#page=8).
- Source evidence: shared heading Absolute Difference, % (95% CI); the length-of-stay block explicitly says median(IQR),days; ICU .5(−1.6 to2.6).
- Rule: percentage points and days are distinct units; the shared difference heading labels the ICU stay row as percent without identifying any percentage transformation.
- Proposed category: Measure, label, or scale inconsistency; REPORT within main, S_W. Distinct from ST03B because the compared numeric row differs.
- Alternative/missing definition: undisclosed percentage transformation or a table-heading exception; the exact mean/median difference estimator is also unspecified and is not inferred from displayed medians.
- Exact human question: Is the ICU stay difference in days or a transformed percent scale, and what unit/estimand should the table heading convey for this row?

### ST03B — Percent heading covers the hospital length-of-stay difference

- Relationship ID: S008.
- Compared locations/roles: REPORT [main p8 Table2 absolute-difference heading and hospital stay row](../../../jama_thille_2019_oi_190108.pdf#page=8).
- Source evidence: heading Absolute Difference, % (95% CI), length-of-stay block median(IQR),days; hospital difference2.3(−1.4 to6.1).
- Rule: percentage points and days are distinct units; the shared heading labels the hospital stay difference as percent without a stated transformation.
- Proposed category: Measure, label, or scale inconsistency; REPORT within main, S_W. The hospital tuple differs from the ICU tuple and remains a separate observation.
- Alternative/missing definition: an undisclosed percentage transformation or heading exception; exact difference estimator is unspecified and is not inferred from displayed medians.
- Exact human question: Is the hospital stay difference in days or a transformed percent scale, and which unit/estimand belongs to this row?

### ST04 — Main ICU-mortality P requires a chi-square convention/denominator reconciliation

- Relationship ID: S009.
- Compared locations/roles: REPORT [main p8 Table2 ICU mortality](../../../jama_thille_2019_oi_190108.pdf#page=8), REPORT [main p1 repeated ICU mortality](../../../jama_thille_2019_oi_190108.pdf#page=1), and REPORT [main p4 statistical rule](../../../jama_thille_2019_oi_190108.pdf#page=4).
- Source evidence:26/302 versus21/339; P=.25, repeated in abstract; methods specify chi-square for ICU mortality.
- Conditional diagnostic rule/calculation: uncorrected Pearson chi-square1.370452597 gives P=.241734136, likelihood-ratio P=.242123765, Yates P=.308257873; two-sided Fisher P=.288309354. None lies in the two-decimal nearest-rounding bin [.245,.255) for .25; truncation of the uncorrected values yields .24 as well. The compatible unadjusted definitions inspected do not account for .25.
- Proposed category: Statistical reporting inconsistency; REPORT within main, S_W. PLAN methods merely corroborate possible variants and do not add a discrepancy relationship.
- Missing definition/alternative: source says chi-square without specifying variant, whether stratification entered this row, the exact analysis denominator, or missingness at mortality assessment; another explicitly defined adjusted chi-square may reconcile.
- Exact human question: Which chi-square statistic and denominators generated .25, and do they match the26/302 and21/339 comparison actually printed? This is a conditional numeric reconciliation question, not an assertion that a missing convention alone is a defect.

### ST05 — Su historical-trial sample size differs inside PLAN

- Relationship IDs: S032 and S037.
- Compared locations/roles: PLAN [protocol p15 historical Su narrative](../../../joi190108supp1_prod.pdf#page=15), PLAN [protocol p17 Table1 Su row](../../../joi190108supp1_prod.pdf#page=17).
- Source evidence: narrative says trial included400 patients; table NIV n202 versus oxygen n204.
- Rule/calculation:202+204=406, distinct from400. Historical/background content remains PLAN.
- Proposed category: Numeric or arithmetic inconsistency; PLAN versus PLAN within one protocol bundle, P_P.
- Alternative/missing definition: narrative may intentionally round to400 or describe an unlabelled population different from the table.
- Exact human question: Does400 intentionally summarize an approximate enrollment count, or do these two locations intend the same exact historical sample size?

### ST06 — Hypercapnic HF ineffective-cough percentage

- Relationship ID: S109.
- Compared locations/roles: REPORT [results p4 eTable2 ineffective cough HF hypercapnic cell](../../../joi190108supp2_prod.pdf#page=4).
- Source evidence:14/45(69), under No./totalNo.(%).
- Rule/calculation:100×14/45=31.111111%; printed69% differs beyond rounding/truncation. The complement31/45=68.888889% is close to69, a diagnostic clue only.
- Proposed category: Denominator, proportion, or total inconsistency; REPORT within results supplement, S_W.
- Alternative/missing definition: percentage could refer to effective rather than ineffective cough or an unlabelled complement denominator; source does not state such reversal.
- Exact human question: Should69% describe the complement, or should numerator/denominator/label describe a different quantity? P=.6561 is coherent with printed count denominators and is not itself a contradiction.

### ST07 — Hypercapnic NIV ineffective-cough percentage

- Relationship ID: S109.
- Compared locations/roles: REPORT [results p4 eTable2 ineffective cough NIV hypercapnic cell](../../../joi190108supp2_prod.pdf#page=4).
- Source evidence:16/59(73).
- Rule/calculation:100×16/59=27.118644%; printed73%; complement43/59=72.881356%, diagnostic only.
- Proposed category: Denominator, proportion, or total inconsistency; REPORT within results supplement, S_W.
- Alternative/missing definition: undisclosed complement coding or inaccurate numerator/denominator/percentage.
- Exact human question: Which displayed quantity is intended for the NIV hypercapnic ineffective-cough cell? Treat separately from HF cell because printed values and comparator differ.

### ST08 — Hypercapnic HF abundant-secretions percentage

- Relationship ID: S110.
- Compared locations/roles: REPORT [results p4 eTable2 abundant secretions HF hypercapnic cell](../../../joi190108supp2_prod.pdf#page=4).
- Source evidence:20/46(57).
- Rule/calculation:100×20/46=43.478261%; displayed57%; complement26/46=56.521739%, diagnostic only.
- Proposed category: Denominator, proportion, or total inconsistency; REPORT within results supplement, S_W.
- Alternative/missing definition: an unlabelled absent-secretions complement may have supplied the percentage.
- Exact human question: Does57% describe absence while20/46 describes presence, or does a different numerator/denominator apply? P=.5465 matches printed count comparison.

### ST09 — Hypercapnic NIV abundant-secretions percentage

- Relationship ID: S110.
- Compared locations/roles: REPORT [results p4 eTable2 abundant secretions NIV hypercapnic cell](../../../joi190108supp2_prod.pdf#page=4).
- Source evidence:23/61(62).
- Rule/calculation:100×23/61=37.704918%; displayed62%; complement38/61=62.295082%, diagnostic only.
- Proposed category: Denominator, proportion, or total inconsistency; REPORT within results supplement, S_W.
- Alternative/missing definition: undisclosed complement coding or a mismatched value.
- Exact human question: Which quantity is intended by the percent in this cell, given the printed numerator/denominator and common row label?

### ST10 — Nonhypercapnic ICU-mortality P requires chi-square reconciliation

- Relationship ID: S132.
- Compared locations/roles: REPORT [results p7 eTable4 ICU mortality](../../../joi190108supp2_prod.pdf#page=7); corroborating rule REPORT [main p4 chi-square/subgroup methods](../../../jama_thille_2019_oi_190108.pdf#page=4).
- Source evidence:HF21/254 versus NIV19/276; P=.5548; contrast−1.4pp, CI−6.1 to3.2.
- Conditional diagnostics: Pearson chi-square .362927994 gives P=.546884582; likelihood-ratio P=.547092106; continuity-corrected P=.661493369; Fisher P=.622413761. These do not fit the four-decimal bin [.55475,.55485); finite precision of integer counts is not an explanation. CI remains contained/ordered/crosses0 and is not criticized using an unknown construction.
- Proposed category: Statistical reporting inconsistency; discrepancy is within REPORT eTable4, S_W. Main rule corroborates the expected test family and does not by itself create S_C.
- Missing definition/alternative: selected chi-square convention or adjusted/stratified model, row-specific nonmissing denominator and test statistic are not supplied.
- Exact human question: Which test and denominators generated .5548, and are they the printed21/254 versus19/276 ICU-mortality contrast?

### ST11 — Nonhypercapnic day90 mortality absolute difference

- Relationship ID: S136.
- Compared locations/roles: REPORT [results p7 eTable4 day90 mortality row and header](../../../joi190108supp2_prod.pdf#page=7).
- Source evidence:HF54/254(21), NIV50/276(18); difference−3.8(−9.9 to3.6), P=.3626.
- Rule/calculation: NIV-minus-HF absolute risk difference100(50/276−54/254)=−3.143900pp. The printed−3.8 exceeds ordinary one-decimal rounding/truncation differences. P diagnostic .362584624 is coherent with these counts and is not itself criticized.
- Proposed category: Numeric or arithmetic inconsistency; REPORT within results supplement, S_W.
- Missing definition/alternative: a separately estimated adjusted or survival-based difference is possible but not labelled in the table; CI method is absent and is not reconstructed.
- Exact human question: Does−3.8 refer to an unlabelled estimand/population, or should the displayed absolute risk difference correspond to the printed event counts?

### ST12 — Survival eFigure time-origin labels conflict

- Relationship ID: S137.
- Compared locations/roles: REPORT [results p9 survival eFigure title and x-axis](../../../joi190108supp2_prod.pdf#page=9).
- Source evidence: title From Extubation to Day90; x-axis Days Since Intubation; initial risk counts302/339 equal analyzed extubated cohort.
- Rule: extubation and intubation are different time origins, so the same plotted axis cannot transparently represent both without a stated mapping. Direct visual observation; no exact curve coordinate or survival estimate derived.
- Proposed category: Measure, label, or scale inconsistency; REPORT within results supplement, S_W.
- Missing definition/alternative: axis label may be stale; title may name clinical follow-up while model uses another origin. No actual time variable supplied to select one.
- Exact human question: Which origin was used for the survival curves and log-rank test, and which label describes that variable?

### ST13 — Day90 mortality Table2/eFigure P matching needs test attribution

- Relationship IDs: S012 and S137.
- Compared locations/roles: REPORT [main p8 Table2 day90 mortality](../../../jama_thille_2019_oi_190108.pdf#page=8), REPORT [main p4 day90 log-rank methods](../../../jama_thille_2019_oi_190108.pdf#page=4), REPORT [results p9 eFigure explicitly log-rank P](../../../joi190108supp2_prod.pdf#page=9).
- Source evidence:main Table2 P=.30 for65/302 versus62/339 day90 deaths; eFigure overall same starting302/339 log-rank P=.37; main p4 states time extubation to death is compared by log-rank atday90.
- Rule: if the two report locations intend the same stated log-rank day90 comparison, their two-decimal P values conflict beyond rounding. This is a conditional cross-location match, not a claim that proportion and survival tests must agree.
- Diagnostic alternative: Pearson death proportions P=.305165421, plausibly displayed .30 by truncation, whereas log-rank .37 cannot be reconstructed without event/censor times. The table P column does not identify its row test; its analysis may be a distinct proportion test while eFigure reports the specified survival test.
- Proposed category: Cross-document numeric inconsistency; REPORT main versus REPORT results supplement, S_C. The survival-axis origin ambiguity ST12 is a separate label rule.
- Exact human question: Does Table2 .30 use an unlabelled proportion comparison distinct from the eFigure log-rank .37, or do both intend the day90 log-rank analysis described in methods? Source event/censor data, row test labels and actual origin are required to settle it.

## Non-candidate diagnostics and missing definitions

- Main S006 P=.009 versus Pearson .009544/LR .009523, main S010 .80 versus .808084, main S012 .30 versus .305165, and main S022 .10 versus supplemental .1057 can reflect truncation. A nearest-rounding assumption alone is not enough to emit separate candidates.
- Main S015 P=.35 versus Pearson .355468 is coherent with likelihood-ratio chi-square .352735; variants are not collapsed.
- eTable1 S057 respiratory/cardiac arrest and S061 pneumonia both7/302 versus3/339 display .20 and .14. Conditional Fisher .203196 and Pearson .143932 account for these values; row test choice is missing, so numerical duplication alone is not an independently contradictory identical inference.
- eTable2 complementary ventilation/SBT categories S086/S087 and S097/S098 correctly share P. Continuous rows were checked in both strata; rounded means/SDs, unknown nonmissing n and t-versus-Mann–Whitney selection prevent exact P reconstruction. No raw-data distribution or test selection was inferred.
- eTable3 S121 P=.9999 and main S020/eTable1 S060/S064 .99 with Fisher diagnostic1 can reflect display cap/export. No candidate is manufactured from near-unit output.
- eTable4 S127 CI upper0.0 and P=.0505 allow a small positive unrounded endpoint and remain coherent.
- S134 printed difference−8.9 versus exact−8.979592 may be truncated. S115 six/63 printed9% may be truncated. Precision policy is unreported; no additional candidate is emitted solely for these rounding-convention differences.
- Logistic S024 OR .60(.38–.93), P=.02 is protective, contained and ordered. A log-normal Wald diagnostic from rounded endpoints is conditional because covariance, variance estimator and inferential statistic are missing; no Wald reconstruction is asserted.
- Continuous contrasts S007/S008/S017/S019/S117/S118/S130/S131 have ordered containing CIs. Point estimate is not assumed to be subtraction of displayed medians. Selected test, CI method and variance/estimand are missing; interval-based normal approximations do not establish a supplied-source contradiction.
- S026–S028/S137 log-rank tests cannot be reconstructed from periodic risk counts alone; exact event/censor times are absent. Risk-table losses are not assumed all events.
- All historical PLAN S030–S039 subcomparisons were checked for internal direction, significance language, printed count/percent/n and repeated narrative/table values; original test/sidedness/model definitions unavailable, so no retrospective inference from convention.
- PLAN S040–S043 and REPORT S029 are analysis-rule relationships. Sample target590 inflated10% gives649, rounded operational target650; no sample-size candidate without exact formula, allocation rounding and continuity conventions.
- No mapped P is printed0 or0.000. DISPLAY_ZERO_NOT_CANDIDATE policy applies if an otherwise coherent display zero appears during final recheck; no tiny-tail calculation or replacement threshold is used.

Completion:137/137 statistical groups, both strata and all grouped subcomparisons processed;14 checker-local candidate observations; no candidate count cap; no source-coverage gap. Limitations are the precisely named inferential definitions above. Coordinator should merge only exact duplicate comparison/rule records across lanes and preserve every stable C ID once assigned.

