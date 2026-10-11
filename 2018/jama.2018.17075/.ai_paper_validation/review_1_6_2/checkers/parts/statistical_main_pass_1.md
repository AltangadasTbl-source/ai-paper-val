# Statistical checker pass 1 — main and early supplementary results

Fresh runtime agent ID: 01a129ba-d0ae-7972-ad30-ec98db09c65f. Model: gpt-6.1-sol. Effort: high. Exact scope: DOC-001 physical pp.1–10 and DOC-003 physical pp.1–11, REPORT by content. Relationship inventory: statistics/parts/report_main.md, S001–S095 (95 explicit PASS_1_COMPLETE records). Scientific inputs were supplied sources, source-matched reusable text/images and fresh maps only. No old candidates, report conclusions or external literature were read. Five finding patterns and four excluded observations are recorded below. Every finding remains subject to independent inclusion screening; no candidate ID or adjudication assigned.

Read complete normative scope and review contract. Check coverage includes every assigned printed estimate, effect CI, descriptive IQR, P value, model label, test decision, interaction, graphical interval and report method. Plan/sample-size/interim checks and later supplementary statistical results have separate disjoint high-effort shards. Method-based arithmetic is grounded in the report's unadjusted chi-square equal-proportions description and reproducing neighboring rows; fitted-model and rank-test approximations are diagnostics only. Integer participant/event counts are indivisible observed counts: the only integer in each half-unit display interval is its printed integer. Do not use fractional people as hypothetical alternative observed counts. Printed effect/P limits use their half-unit intervals; route A category 1 is not excused by display precision.

## Findings

### F-ST1-001

**Title:** Primary risk-difference direction differs between abstract and detailed results.

**Relationships:** S001. **Locations and document roles:** REPORT [main abstract physical p.1](../../../../jama_cooper_2018_oi_180132.pdf#page=1); REPORT [primary narrative physical p.5](../../../../jama_cooper_2018_oi_180132.pdf#page=5); REPORT [Table 2 physical p.7](../../../../jama_cooper_2018_oi_180132.pdf#page=7).

**Printed values:** Abstract risk difference 0.4% (95% CI −9.4% to 8.7%) alongside H 117(48.8%) versus N 111(49.1%). Narrative and Table 2 print −0.4 percentage points, identical interval; Table 2 gives denominators 240 and 226 and RR 0.99.

**Rule and calculation:** Under the H −N contrast of the detailed table, 100(117/240−111/226)=−0.365044 percentage points. The abstract plus sign differs from the detailed minus sign. Half-unit abstract interval [0.35,0.45] versus body interval [−0.45,−0.35] has gap 0.70 percentage points, relative discrepancy 0.70/0.4=1.75. The count-derived value is also below the abstract interval by 0.715044, relative 1.78761. CI endpoints are ordered, include both estimates and null; P .94 correctly indicates no superiority, so the observation concerns printed direction rather than the significance conclusion.

**Focus area:** B. **Proposed review domain:** statistical_results. **Provisional relationship:** S_W; all relationships S_W.
**Qualifying route:** Route A, category 2.
**Affected result or extracted value:** Sign of the primary absolute risk difference copied from the abstract.
**Why context does not resolve it:** Route A category 2 requires retaining a printed sign that reverses the H −N effect; reconstructibility from the table does not remove the issue.
**Alternatives and missing definition:** The abstract could intend N −H, but it uses the same CI as the H −N table and does not disclose reversing the contrast. This possible interpretation is preserved.
**Exact human question:** Which signed contrast and risk-difference value should be extracted from the abstract's primary result?
**Pass record:** PASS_1_COMPLETE.

### F-ST1-002

**Title:** Bleeding effect intervals and P values align with the opposite outcome's counts.

**Relationships:** S008, S009, S087, S088. **Locations and document roles:** REPORT [main binary-analysis method physical p.3](../../../../jama_cooper_2018_oi_180132.pdf#page=3); REPORT [Table 2 bleeding rows physical p.7](../../../../jama_cooper_2018_oi_180132.pdf#page=7); REPORT [eTable 6 bleeding rows physical p.10](../../../../joi180132supp2_prod.pdf#page=10).

**Printed values:** Table 2 intracranial bleeding 47/260(18.1%) versus 37/240(15.4%), RD 2.7(−3.9,9.2), RR 1.23(0.43–3.5), P .70. Extracranial bleeding 8/260(3.1%) versus 6/240(2.5%), RD 0.6(−2.3,3.5), RR 1.17(0.79–1.74), P .43. eTable 6 reports identical counts but intracranial P .43 and extracranial P .70. Main method states unadjusted chi-square equal-proportions analysis.

**Rule and calculation:** The unadjusted ratio/log-Wald CI/Pearson test reproduces the primary, hospital-death, six-month-death, pneumonia, bacteremia and other-infection rows (P .937204,.568097,.453996,.401146,.285058,.531864). Applied to intracranial counts it gives RR 1.172557, CI[0.791181,1.737769], P .426669 and RD 2.660256 CI[−3.878255,9.198768]. Applied to extracranial counts it gives RR 1.230769, CI[0.433345,3.495582], P .696039 and RD 0.576923 CI[−2.305386,3.459232]. The two printed RD columns reproduce their own rows. Their RR/CI/P triplets instead reproduce the opposite bleeding row. Consolidated as one repeated displacement pattern without assigning a production mechanism.

**Display precision:** Intracranial printed lower-limit 0.43 interval [0.425,0.435] versus reproducing lower-limit 0.791181 gives gap 0.356181, relative 0.828328; upper 3.5 interval [3.45,3.55] versus 1.737769 gives gap 1.712231, relative 0.489209. Its printed P .70 interval [.695,.705] versus .426669 gives gap.268331/.70=.383329. Extracranial lower 0.79 interval [.785,.795] versus .433345 gives gap.351655/.79=.445133; upper 1.74 interval [1.735,1.745] versus 3.495582 gives gap 1.750582/1.74=1.00608. Its printed P .43 interval [.425,.435] versus .696039 gives gap.261039/.43=.607068. Printed RR point estimates alone differ by less than the .05 relative threshold, but intervals and P values do not. Printed-copy eTable 6 P values also differ beyond precision: .70 versus .43 has gap.26/.70=.371429; .43 versus .70 gap.26/.43=.604651.

**Focus areas:** B, C. **Proposed review domain:** statistical_results. **Provisional relationship:** S_C; all relationships S_C, S_W.
**Qualifying route:** Route A, category 4.
**Affected result or extracted value:** Outcome-specific bleeding RR precision, CI limits and P values.
**Why context does not resolve it:** A method reproduces the neighboring rows and the opposite bleeding row, while these printed row assignments change extracted intervals and tests. Immediate reconstruction does not identify which reported row a reader should reuse without a review.
**Alternatives and missing definition:** A separate undisclosed analysis could yield the two triplets, but would have to explain their exact opposite-row alignment and disagreement with eTable 6. No adjusted model is stated for these rows.
**Exact human question:** Which unadjusted RR, 95% CI and P value belong to each bleeding outcome, and were any separate analyses used?
**Pass record:** PASS_1_COMPLETE.

### F-ST1-003

**Title:** Survival risk sets extend beyond the stated six-month censoring rule.

**Relationships:** S017, S033. **Locations and document roles:** REPORT [main survival-analysis method physical p.4](../../../../jama_cooper_2018_oi_180132.pdf#page=4); REPORT [main six-month follow-up description physical p.2](../../../../jama_cooper_2018_oi_180132.pdf#page=2); REPORT [eFigure 2 physical p.5](../../../../joi180132supp2_prod.pdf#page=5).

**Printed values:** Main method: patient survival assessed with Cox proportional hazards regression “censored at 6 months or last known point of contact,” presented as Kaplan–Meier curves with log-rank test. eFigure 2 caption describes six-month death comparison HR 1.13(0.76–1.69), P .54. Figure axis is patient survival in days, with risk sets H 91/N 88 at 200 days and H 23/N 17 at 250 days; censored ticks continue beyond 200 days.

**Rule and calculation:** Under censoring at six months or an earlier last contact, participants cannot remain at risk after the six-month cut. Six consecutive calendar months never span 200 days (even a conservative upper bound of 186 days is below 200); the plot retains 179 at risk at 200 days and 40 at 250 days. This is not inferred from an empty extended axis: the positive risk counts and censor ticks are printed. Count-rounding intervals contain no alternative integer 0 for 91,88,23 or 17. The conservative time discrepancy at 200 days is at least 14 days, exceeding .05 relative to 200; at 250 days it is at least 64 days. HR/CI/P containment and null decisions themselves reconcile.

**Focus area:** C. **Proposed review domain:** statistical_results. **Provisional relationship:** S_C; all relationships S_C.
**Qualifying route:** Route B.
**Affected result or extracted value:** The observation window and administrative censoring used for the reported six-month Cox/KM/log-rank mortality comparison.
**Why context does not resolve it:** Neither the method nor caption defines a later cutoff or says that the graph uses a different survival dataset from the HR/test. The reader cannot identify whether the six-month rule, risk table or analysis window applies.
**Alternatives and missing definition:** The figure may use actual later follow-up contacts while the HR is restricted to six months, or “six months” may denote a visit with a broader window. Neither mapping is supplied. A delayed contact does not alone explain retaining risk after an explicitly stated censoring cut.
**Exact human question:** What administrative censoring time and dataset were used for eFigure 2, and are they the same as those used for HR 1.13 and the reported Cox/log-rank tests?
**Pass record:** PASS_1_COMPLETE.

### F-ST1-004

**Title:** The cooling-time favorable-outcome P value does not reproduce under the stated equal-proportions test.

**Relationships:** S090, S091, S092, S093, S094. **Locations and document roles:** REPORT [main statistical method physical p.4](../../../../jama_cooper_2018_oi_180132.pdf#page=4); REPORT [main nonsignificance summary physical p.5](../../../../jama_cooper_2018_oi_180132.pdf#page=5); REPORT [eTable 7 physical p.11](../../../../joi180132supp2_prod.pdf#page=11).

**Printed values:** Main states the effect on favorable outcome of time taken for cooled patients to achieve 33°C was compared with unadjusted chi-square test for equal proportions. eTable 7 four displayed groups:1–7 h n 49, favorable 18; 8–13 h n 67, favorable 28; >13 h n 59, favorable 32; never n 65, favorable 39. SharedP .09. Row-specific proportions and 95%CIs contain their estimates. Main summary states no significant difference.

**Rule and calculation:** For the four displayed categories, totals 240 and 117 yield common favorable rate 117/240=.4875. Pearson statistic sum_i (a_i−n_i*.4875)^2/[n_i*.4875*(1−.4875)]=8.133762156. For the displayed four-category binary contingency table the independence test has (4−1)(2−1)=3 degrees of freedom, determined by the stated test and table structure, not guessed model conventions. P=.0433268, below the stated .05 level, versus printed .09. The same Pearson method reproduces the report's ordinary unadjusted categorical rows. Excluding the never group as a source-grounded alternative to “cooled patients” gives 78/175, statistic 3.658952245,2 df, P=.1604976, also different from.09.

**Display precision:** For exact integer counts the recomputed four-group P is.0433268; printed.09 interval [.085,.095] has gap.0416732, relative.463036. The three-reached-group alternative gap from printed upperlimit.095 is.0654976/.09=.727751. Four-group test classification versus printed P is a routeA1 test conflict, so it is not excused by the display-precision rule.

**Focus areas:** B, C. **Proposed review domain:** statistical_results. **Provisional relationship:** S_C; all relationships S_C, S_W.
**Qualifying route:** Route A, category 1.
**Affected result or extracted value:** P value and significance interpretation of the association of cooling-time category with six-month favorable GOS-E.
**Why context does not resolve it:** Route A category 1 retains a nonsignificant printed P versus a significant stated-test result; the table does not identify a different subset, adjusted model or statistic that generated.09.
**Alternatives and missing definition:** The P may use a distinct cooling-time subset, exact test or other statistic. The source-grounded three-reached-strata alternative does not reproduce.09. No time-trend coding or other model was assumed.
**Exact human question:** Which groups, sample and unadjusted test generated P=.09, and how does that test map to the four rows in eTable 7?
**Pass record:** PASS_1_COMPLETE.

### F-ST1-005

**Title:** Ventricular-fibrillation P value uses an unresolved exception to the reported unadjusted chi-square method.

**Relationships:** S080. **Locations and document roles:** REPORT [main binary-analysis method physical p.3](../../../../jama_cooper_2018_oi_180132.pdf#page=3); REPORT [eTable 6 cardiovascular rows physical p.10](../../../../joi180132supp2_prod.pdf#page=10).

**Printed values:** Adverse events described as compared with unadjusted chi-square equal-proportions test. eTable 6 ventricular fibrillation 1/260(0.4%) versus 0/240(0%), P 1.00. Neighboring ventricular tachycardia 7/260 versus 5/240 P .66 and asystole 7/260 versus 7/240 P .88.

**Rule and calculation:** For VF pooled rate 1/500=.002; z=[1/260−0/240]/sqrt(.002*.998*(1/260+1/240))=.961731135; Pearson χ²=z²=.92492678,1 df gives P=.3361847. The same formula gives VT P .656678 and asystole P .879243, reproducing their printed P .66 and .88, and reproduces every other eTable 6 comparison. Printed 1.00 interval [.995,1] versus .3361847 has gap.6588153, relative.6588153> .05. Integer event counts 1 and 0 are exact; half-unit intervals contain only their respective admissible integer counts.

**Focus area:** C. **Proposed review domain:** statistical_results. **Provisional relationship:** S_C; all relationships S_C.
**Qualifying route:** Route A, category 4.
**Affected result or extracted value:** Statistical test and extracted P value for ventricular fibrillation.
**Why context does not resolve it:** The stated method and a method reproducing every other comparison do not reproduce this row; an exception affects which analysis a reader attributes to its P value.
**Alternatives and missing definition:** A two-sided Fisher exact test gives P 1.00 for the single observed event, and a continuity-corrected test could also give a high P. These are coherent possible exceptions but neither is identified for this row. No preference between methods is asserted.
**Exact human question:** Was an exact or continuity-corrected test used for ventricular fibrillation, and what exception to the stated unadjusted chi-square method applies?
**Pass record:** PASS_1_COMPLETE.

## Excluded observations

Only apparent observations that were not emitted are listed; successful checks remain in the S inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p 5 Table 1 ISS, S025 | N median 20.0 is below descriptive IQR lower limit 20.5. Half-unit intervals[19.95,20.05] and[20.45,20.55] leave gap.40/20.0=.02≤.05. This is an IQR, not an effect confidence interval; descriptive quantile ordering was explicitly checked, and the scope display threshold screens the size. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 p 8 eTable 4 noradrenaline-duration P, S056 | Source visually prints P <.000. This very small P display is not a finding by itself; the two medians lie within their IQRs and no CI/test contradiction is supplied. Native text's wrapped “1” is not treated as authority over the page. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-003 p 11 eTable 7 row-specific intervals, S090, S091, S092, S093 | Diagnostic binomial normal intervals 23.2366–50.2327,29.9811–53.6010,41.5249–66.9497,48.0904–71.9096 differ modestly from printed 22.8–50.7,29.6–53.9,41.2–67.3,47.8–72.2. Endpoint gaps after.05 half-units are all≤.05relative; CI engine unspecified; no independent containment or decision conflict in these marginal intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 pp 4,6 Figure 2 temperature claim, S029 | The precise test behind “significantly lower” is not supplied; visual direction agrees and no contradictory numeric estimate, interval or P is printed. Missing test alone cannot register a candidate. | CONDITIONAL_OR_UNREPORTED |

## Limits and handoff

No scientific scope gap: all assigned pages and 95 relationship records complete. Individual ranks, model coefficients, variance inputs and time-to-event data are not supplied, so exact rank/model recomputation is unavailable and not fabricated. Most plot limits are graphical rather than printed values; every visible component is checked with that distinction. Stable findingsF-ST1-001, F-ST1-002, F-ST1-003, F-ST1-004, F-ST1-005 require fresh inclusion screening. PASS_1_COMPLETE.

