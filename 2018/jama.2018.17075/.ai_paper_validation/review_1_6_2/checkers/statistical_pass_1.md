# Statistical consistency pass 1 — complete canonical review

Four fresh high-effort shards are merged without omitted findings, exclusions or relationship records.

# Statistical checker pass 1 — main and early supplementary results

Fresh runtime agent ID: 01a129ba-d0ae-7972-ad30-ec98db09c65f. Model: gpt-6.1-sol. Effort: high. Exact scope: DOC-001 physical pp.1–10 and DOC-003 physical pp.1–11, REPORT by content. Relationship inventory: statistics/parts/report_main.md, S001–S095 (95 explicit PASS_1_COMPLETE records). Scientific inputs were supplied sources, source-matched reusable text/images and fresh maps only. No old candidates, report conclusions or external literature were read. Five finding patterns and four excluded observations are recorded below. Every finding remains subject to independent inclusion screening; no candidate ID or adjudication assigned.

Read complete normative scope and review contract. Check coverage includes every assigned printed estimate, effect CI, descriptive IQR, P value, model label, test decision, interaction, graphical interval and report method. Plan/sample-size/interim checks and later supplementary statistical results have separate disjoint high-effort shards. Method-based arithmetic is grounded in the report's unadjusted chi-square equal-proportions description and reproducing neighboring rows; fitted-model and rank-test approximations are diagnostics only. Integer participant/event counts are indivisible observed counts: the only integer in each half-unit display interval is its printed integer. Do not use fractional people as hypothetical alternative observed counts. Printed effect/P limits use their half-unit intervals; route A category 1 is not excused by display precision.

## Findings

### F-ST1-001

**Title:** Primary risk-difference direction differs between abstract and detailed results.

**Relationships:** S001. **Locations and document roles:** REPORT [main abstract physical p.1](../../../jama_cooper_2018_oi_180132.pdf#page=1); REPORT [primary narrative physical p.5](../../../jama_cooper_2018_oi_180132.pdf#page=5); REPORT [Table 2 physical p.7](../../../jama_cooper_2018_oi_180132.pdf#page=7).

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

**Relationships:** S008, S009, S087, S088. **Locations and document roles:** REPORT [main binary-analysis method physical p.3](../../../jama_cooper_2018_oi_180132.pdf#page=3); REPORT [Table 2 bleeding rows physical p.7](../../../jama_cooper_2018_oi_180132.pdf#page=7); REPORT [eTable 6 bleeding rows physical p.10](../../../joi180132supp2_prod.pdf#page=10).

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

**Relationships:** S017, S033. **Locations and document roles:** REPORT [main survival-analysis method physical p.4](../../../jama_cooper_2018_oi_180132.pdf#page=4); REPORT [main six-month follow-up description physical p.2](../../../jama_cooper_2018_oi_180132.pdf#page=2); REPORT [eFigure 2 physical p.5](../../../joi180132supp2_prod.pdf#page=5).

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

**Relationships:** S090, S091, S092, S093, S094. **Locations and document roles:** REPORT [main statistical method physical p.4](../../../jama_cooper_2018_oi_180132.pdf#page=4); REPORT [main nonsignificance summary physical p.5](../../../jama_cooper_2018_oi_180132.pdf#page=5); REPORT [eTable 7 physical p.11](../../../joi180132supp2_prod.pdf#page=11).

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

**Relationships:** S080. **Locations and document roles:** REPORT [main binary-analysis method physical p.3](../../../jama_cooper_2018_oi_180132.pdf#page=3); REPORT [eTable 6 cardiovascular rows physical p.10](../../../joi180132supp2_prod.pdf#page=10).

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

# Statistical pass 1: report-support shard

Runtime agent ID: 01a129ba-f6dd-7cd3-ac0d-591be72882c8. Model gpt-6.1-sol; reasoning effort high; start mode FRESH_SPAWN. Exact assigned scope: DOC-003 joi180132supp2_prod.pdf physical pp.12–24, R018–R068. All 107 statistical relationships S201–S307 have PASS_1_COMPLETE in statistics/parts/report_support.md. Two findings and four excluded observations. No candidate IDs assigned. No prior candidate, screening, verifier or report conclusions were used.

The complete scope and 1.6.2 review contract were read. Direct-source native/layout text was read for every assigned page; reusable source-matched rendered pages 12,15,16,17,18,20,21,22 were inspected visually, including both finding locations. Processing used CPU and available pdftotext; no OCR, new render, custom Python or external evidence was used. Sources and reusable assets remain unchanged.

## Completed check coverage

Every independent printed baseline test in eTables8,10,13, every outcome/subgroup row and interaction P in eTables9,11, both sensitivity primary results, kappa, all missingness effects/proportion intervals/tests, and both adequate-cooling OR results were reviewed. Shared omnibus tests are retained once with all component categories. All median/IQR endpoints and point containment were checked. All valid RR/OR/RD intervals contain their point estimates and agree with their printed P at the stated two-sided .05 level. The two significant pneumonia intervals are consistent with P=.02 and P=.003 and with increased risk in the hypothermia group. Unadjusted RR/log-interval calculations reproduce other rows of eTables9/11; adjusted values are evaluated against their stated model rather than a crude ratio. Stated chi-square tests and log-Wald CIs need not have exactly the same numerical P.

Flow totals, analysis population definitions, treatment transfer rules, early death handling, missing outcome assignment, MAR/predictive mean matching with 11 datasets, and stated hierarchical adjustment were reviewed without proposing another analysis. The report explicitly discloses exploratory secondary comparisons without multiplicity adjustment. There is no noninferiority, equivalence, interim or stopping conclusion in this shard. Missing model inputs, raw ranks and imputation strata are recorded as limitations rather than invented. Main article pp.3–4 was consulted for source-grounded method definitions only, without undertaking main-paper discovery.

## Findings

### F-ST1-101

**Title:** Two normothermia CT cells do not reconcile with the count-and-percentage header.

**Statistical relationships:** S248; all affected cells constitute one repeated count/percentage ordering pattern.

**Exact locations and document roles:** REPORT DOC-003 [physical p.18, eTable10, normothermia column, CT Marshall evacuated mass lesion V and non-evacuated mass lesion VI rows](../../../joi180132supp2_prod.pdf#page=18), compared with REPORT the same display's `No. (%)` header, normothermia `(n = 196)` heading, and the other CT rows. The literal cells were visually confirmed against the source-matched page and confirmed in direct source extraction.

**Printed values:** V `34.7 (68)`; VI `1 (2)`. Other normothermia CT rows are I `3 (1.5)`, II `108 (55.1)`, III/IV `15 (7.7)`. The shared CT test is P=.71. Hypothermia entries follow `No. (%)`, including V `44 (33.1)` and VI `0 (0)`.

**Rule and calculation:** Under the stated `No. (%)` order, V means count34.7 and percentage68; 100×34.7/196=17.7041%, while VI means count1 and percentage2; 100×1/196=.5102%. The literal normothermia category counts sum to 3+108+15+34.7+1=161.7 rather than196. Apply a deliberately lenient half-unit interval to every printed input, including the denominator: V count[34.65,34.75], denominator[195.5,196.5], implied percentage[17.63359,17.77494]; printed68 allows[67.5,68.5]. Gap49.72506 percentage points; relative discrepancy49.72506/68=.73125. VI count[.5,1.5], denominator[195.5,196.5], implied percentage[.25445,.76726]; printed2 allows[1.5,2.5]. Gap.73274; relative discrepancy.73274/2=.36637. Both exceed.05. Exact integer-count treatment would make the gaps larger.

**Focus area:** A, counts and denominators, with consequences for the category test's input reading.

**Proposed review domain:** statistical_results.

**Proposed relationship type:** S_W; all relationships S_W.

**Qualifying route:** Route A, category 3.

**Affected result or extracted value:** The normothermia counts and proportions for Marshall V and VI in the as-treated baseline population, and any extraction of that CT distribution used to understand the as-treated comparison.

**Why context does not resolve it:** Route A category3 applies to count/denominator/percentage conflicts within one display. Reconstructing a likely count/percentage transposition does not remove the literal numerical readings under the displayed header.

**Alternatives and missing definition:** Interpreting the V cell as 68(34.7) and VI as 2(1) would sum to196, and 68/196=34.6939% and 2/196=1.0204% reconcile with those reordered percentages. This is an alternative reading, not a source correction. If the printed order is intentional, the category-specific count and denominator definitions would be needed.

**Exact human question:** What counts and percentages should be extracted for the normothermia Marshall V and VI rows in eTable10, and which category values were used for the printed shared P=.71?

### F-ST1-102

**Title:** An additional printed number leaves the adjusted odds-ratio interval limits unclear.

**Statistical relationships:** S292.

**Exact locations and document roles:** REPORT DOC-003 [physical p.22, post hoc adequate-cooling Results, final adjusted odds-ratio statement](../../../joi180132supp2_prod.pdf#page=22), compared with REPORT the same page's definition of results as odds ratios with 95% CIs and its unadjusted odds-ratio statement. Direct source extraction and the source-matched rendered page both show the numeric token275 inside the interval text.

**Printed values:** The final statement is `0.95 (0.55-275 1.64) P = .84` for an adjusted odds ratio hypothermia versus normothermia after adjustment for time to randomization. The preceding unadjusted result is OR.91(.59–1.41), P=.68; the method states hierarchical multivariable logistic regression adjusting for baseline imbalance and treating location/site as random effects, with ORs and 95%CIs.

**Rule and calculation:** A two-limit 95% interval requires a lower and an upper limit. The printed expression has three numerical components after the point estimate: .55,275,1.64; its upper-limit field therefore cannot be taken uniquely from the source without dropping or reinterpreting a number. If275 is taken as the upper limit following the hyphen, it produces [.55,275]; if1.64 is taken as the upper limit, it produces [.55,1.64]. For the two competing upper-limit readings, half-unit intervals are[274.5,275.5] and[1.635,1.645]. Their gap is272.855; relative discrepancy against1.64 is166.375, well above.05. Both include null1 and point.95; no significance conflict is asserted. This calculation quantifies the changed interval magnitude rather than attempting to recompute an adjusted CI from absent model inputs.

**Focus area:** B, estimate and test logic, specifically the printed confidence-limit values available for extraction.

**Proposed review domain:** statistical_results.

**Proposed relationship type:** S_W; all relationships S_W.

**Qualifying route:** Route A, category 2.

**Affected result or extracted value:** The upper confidence limit for the adjusted odds ratio.95 comparing adequately cooled evaluable hypothermia patients with controls after adjustment for time to randomization.

**Why context does not resolve it:** Route A category2 covers a printed numerical slip that changes extracted magnitude even when a probable intended reading can be reconstructed. The immediate text contains275 as well as1.64; these upper-limit readings differ beyond display precision.

**Alternatives and missing definition:** The numeric token275 might be an unintended insertion and the intended interval might be(.55–1.64); this alternative is compatible with the reported no-significant-difference statement and P=.84. Alternatively275 may belong to a displaced count or other annotation. The supplied page does not define a role for it. No preferred corrected interval is assigned, and no numeric reconstruction of the hierarchical model is claimed.

**Exact human question:** What are the two 95% confidence limits for the adjusted odds ratio.95 on supplementary physical p.22, and does the printed token275 belong to that interval or to another quantity?

## Excluded observations

Only apparent issues considered and not emitted appear below. Reconciled checks are in the relationship inventory. Each row has one scope reason code.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-003 pp.16,20, PP/as-treated sensitivity methods, S234/S270 | Majority of first72h is described using degree×hours AUC below35°C, but a numeric AUC cutoff is not supplied locally. The source points to the SAP; an omitted local cutoff alone is not a contradiction, and the plan shard owns exact specification alignment. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-003 pp.14,19, adjusted rows, S219/S256 | PP row labels favorable outcome whereas as-treated row labels unfavorable outcome. They concern different populations; individual adjusted model outputs/outcome coding are unavailable. Inferring that1.11 necessarily used the favorable event from its similarity to a crude OR/RR would invent a mapping; no same-analysis numerical conflict is reproduced. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-003 p.21 eTable12 most-likely RR, S286/S288 | The stratified RR CI.95–1.06 is narrower than a diagnostic unstratified log-RR interval from rounded counts (approximately.85–1.21). The source explicitly specifies CMH for this scenario, unlike the unadjusted worst/best rows. Strata, dataset-specific values and pooling definition are absent; neither the null/P decision nor a source-established same-analysis value conflicts. The diagnostic is not treated as the reported model. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-003 p.21 eTable12 most-likely H count/percentage, S284 | 133/260=51.153846%, compared with51.1%. With exact counts the gap to the printed percentage interval[51.05,51.15] is.003846 percentage points, relative.0000753. Allowing half-unit intervals for displayed inputs gives overlap and gap0. Both satisfy the display-precision screen. | ROUNDING_OR_DISPLAY_PRECISION |

## Limitations

Adjusted model reproduction, interaction P reproduction, exact rank tests, kappa's sampling calculation and imputation-stratified pooling require inputs not supplied in this report shard. Valid interval endpoint order, point containment and null/P decision checks were nevertheless completed. Figure4 bars have no stated confidence-level definition, so no unprinted level was inferred. No scientific coverage gap remains within physical pp.12–24. Independent inclusion screening and source-level mechanical recheck remain coordinator stages.
# Statistical pass 1 — PLAN method/design shard

- Runtime agent: 01a129bb-2346-7d93-89e3-266a9f7a3f14.
- Model / effort / start mode: gpt-6.1-sol / high / FRESH_SPAWN.
- Pass record: PASS_1_COMPLETE.
- Exact scope: DOC-002 physical PDF pp.1–194, PLAN statistical design and method relationships, with supplied DOC-001 methods pp.2–4 as REPORT comparators. Monitoring printed inferential/count rows pp.189–194 belong to a separate high shard; this shard covers their method, population and decision-rule definitions.
- Stable relationships: 82, S401–S482; each explicitly PASS_1_COMPLETE in statistics/parts/plan.md.
- Findings: 5, F-ST1-201–F-ST1-205. Excluded observations: 17.
- Complete QUALITY_CONTROL_SCOPE.md and review contract read. Source-linked current-run mapper assets only; no old conclusions, candidate IDs, external SAP text, web, or raw-data assumptions.

Source authority: exact supplied PDF text via direct Poppler pdftotext25.03.0; source-matched reusable text/images serve as locators. All four current-run plan maps were read, original shardA before its full raw-source appendix; administrative/background/pointer units retain complete page accounting. Images pp.152,183,187 inspected. A fresh CPU direct pdftoppm25.03.0 stdout-only rendering of p187 at220dpi confirmed an apparent mapper inequality discrepancy as '<48', so it is not emitted. No durable derivative produced. Direct source p69,p77,p83–86,p97–101,p108–110,p118–119,p132,p139,p174–175,p178–180,p188 and REPORT pp3–4 opened for source-grounded checks.

Evidence links resolve from this part directory. Coordinator canonical merge should preserve truthful supplied-PDF links and physical page anchors. Proposed classifications are for independent screening and recheck; no adjudication or correction is assigned.

## Findings

### F-ST1-201

**Title:** Final protocol gives different anchors for the required hypothermia duration.

**Relationship:** S416. **Focus area:** D. **Proposed review domain:** plan_material. **Proposed primary/all relationships:** P_P / P_P.

**Compared locations and document roles:** PLAN [DOC-002 p69, final protocol V9 §6.5 synopsis](../../../joi180132supp1_prod.pdf#page=69); PLAN [p77 §12.11](../../../joi180132supp1_prod.pdf#page=77); PLAN [p97 §26.3.1](../../../joi180132supp1_prod.pdf#page=97); PLAN [p99 §26.4 flowchart and late-cooling footnote](../../../joi180132supp1_prod.pdf#page=99).

**Printed statements:** p69 reaches33°C and then maintains that temperature 'for a further72hours'. p77 assesses rewarming72hours after randomization. p97 describes72hours after severe head injury. p99 starts with '72hours post randomisation?' and says late cooling requires a minimum48hours of cooling before considering rewarming. All occur in the same final V9 dated11July2017.

**Rule and calculation:** A duration following attainment of33°C differs from elapsed time following randomization or injury. Let r be randomization and c>r attainment of33°C. The synopsis implies earliest ordinary rewarming c+72h; the detailed rule gives a randomization threshold r+72h, with late-cooling minimum c+48h and the clinical stability conditions. These are different interventions even when all stability conditions are satisfied. For a source-permitted delayed attainment more than24h after randomization, the late-cooling footnote can permit rewarming after48h actual cooling while the synopsis requires72h. This is a logical schedule comparison, not an inferred patient-level duration or subtraction of group medians. Both displayed integer durations have intervals [47.5,48.5] and [71.5,72.5]; their gap23h/72h=.3194, above.05. Injury versus randomization alone would differ by at most the enrollment window and is not the basis of the finding.

**Qualifying route:** Route B.

**Affected result or extracted value:** The randomized intervention's required hypothermia duration used to characterize the six-month favorable-GOSE comparison and adherence to sustained cooling.

**Why context does not resolve it:** The same final protocol contains the competing anchors and a48h minimum; no amendment in the supplied bundle says that its synopsis was superseded within V9. The schedules cannot be represented by one duration after target attainment.

**Alternatives and missing definition:** The detailed randomization-based bedside rule could govern practice while the synopsis describes an ideal target. Clinical instability can extend either schedule but does not reconcile different eligible starts. Missing definition: which time anchor and minimum actual duration define the final planned randomized intervention for interpretation and extraction.

**Exact human question:** Which V9 duration rule governed the planned intervention:72h after achieving33°C,72h after randomization with a48h late-cooling minimum, or72h after injury?

### F-ST1-202

**Title:** The final protocol and report give different durations of normothermic management after rewarming.

**Relationship:** S417. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary relationship:** P_R. **All relationships:** P_R, P_P.

**Compared locations and document roles:** PLAN [DOC-002 p77 §12.11](../../../joi180132supp1_prod.pdf#page=77), PLAN [p101 §26.5.1](../../../joi180132supp1_prod.pdf#page=101); REPORT [DOC-001 p3 Rewarming](../../../jama_cooper_2018_oi_180132.pdf#page=3), REPORT [p1 abstract intervention](../../../jama_cooper_2018_oi_180132.pdf#page=1).

**Printed statements:** PLAN p77 says after reaching37°C, hypothermia-arm patients remain normothermic below38°C using pads up to a maximum7days or earlier ICU discharge. PLAN p101 says after reaching37°C, they remain normothermic using pads 'for96hours post randomisation', after which ward protocol governs, and repeats a96h pyrexia-avoidance window for all patients. REPORT p3 says once37°C is reached, automated surface cooling maintains normothermia if required 'for up to7days postrandomization'; REPORT abstract says temperature was managed7days in both groups.

**Rule and calculation:** A postrandomization device-management window of96h equals4d, whereas7d equals168h. The integer rounded windows [95.5,96.5]h and [156,180]h (allowing7d its full half-day interval) remain separated by59.5h; relative gap against96h=.6198>.05. This concerns the planned period, not actual required device use in an individual patient. No inference about body temperature after pads were discontinued is made.

**Qualifying route:** Route B.

**Affected result or extracted value:** The planned duration of randomized temperature management and the comparator/intervention definition extracted alongside six-month favorable-GOSE and mortality results.

**Why context does not resolve it:** Both PLAN statements occur in finalV9, and its appendix explicitly assigns ward protocol after96h. REPORT describes a7d window. Neither early ICU discharge nor the words 'if required' make the maximum planned management windows equal.

**Alternatives and missing definition:** p101 could retain an older bedside guidance window, or seven-day management could continue under ward protocol beyond the mandated96h device period. Missing definition: whether96h or7d is the protocolized temperature-management duration after randomization and whether the7d report includes management outside the randomized protocol.

**Exact human question:** Which temperature-management window applies to the reported trial: mandated surface-pad normothermia through96h, management through7d, or a defined combination of these?

### F-ST1-203

**Title:** The reported planned rewarming rate exceeds the final protocol's stated recommended maximum.

**Relationship:** S418. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary/all relationships:** P_R / P_R.

**Compared locations and document roles:** PLAN [DOC-002 p77 §12.11](../../../joi180132supp1_prod.pdf#page=77); PLAN [p99 §26.4](../../../joi180132supp1_prod.pdf#page=99); PLAN [p100 §26.5](../../../joi180132supp1_prod.pdf#page=100); REPORT [DOC-001 p3 Rewarming](../../../jama_cooper_2018_oi_180132.pdf#page=3). Original PLAN [p21 §12.11](../../../joi180132supp1_prod.pdf#page=21) supplies an alternative version context only.

**Printed values:** Final PLAN p77 active gradual rewarming0.17°C/h and 'recommended maximum'0.5°C every3h; p99 rate aim0.17°C/h; p100 same schedule and approximately24h from33to37°C, with slowing0.2°C per2h and emergency faster rates at intensivist discretion. REPORT p3 gradual controlled rewarming 'at a target rate up to0.25°C/h'. Original protocol uses0.25°C/h.

**Rule and calculation:**0.5°C/3h=.1667°C/h agrees with printed0.17. A reported routine target up to0.25°C/h is greater than the final recommended maximum. Allowing0.17 and0.25 their half-hundredth intervals gives [.165,.175] and [.245,.255]; gap.070/.17=.4118>.05. This is a printed planned-rate comparison, not an assertion that patients actually rewarmed at the maximum.

**Qualifying route:** Route B.

**Affected result or extracted value:** The planned randomized intervention's rewarming rate used to characterize early sustained cooling and its six-month neurologic comparison.

**Why context does not resolve it:** The reported rate matches the original rather than final protocol. The final plan distinguishes emergency faster rewarming from its routine maximum; the REPORT paragraph presents0.25 as the ordinary target without that qualification. No supplied later amendment explicitly restores the original routine rate.

**Alternatives and missing definition:** 'Up to0.25' could be an outer safety ceiling encompassing the actual0.17 target, or it could reflect the original procedure. Emergency faster rewarming is expressly allowed in the final plan and is not itself questioned. Missing definition: whether0.25 was an amended routine ceiling, an umbrella bound, or only an emergency allowance.

**Exact human question:** What routine rewarming target and maximum governed the trial, and how does the reported up-to0.25°C/h rate relate to finalV9's0.17°C/h recommended maximum?

### F-ST1-204

**Title:** The report's primary analysis-population description omits a final-protocol exclusion class.

**Relationship:** S425. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed primary/all relationships:** P_R / P_R.

**Compared locations and document roles:** PLAN [DOC-002 p84 §15.2](../../../joi180132supp1_prod.pdf#page=84); PLAN [pp174–175 V8 amendment, Section15](../../../joi180132supp1_prod.pdf#page=174); REPORT [DOC-001 p3 Statistical Analysis](../../../jama_cooper_2018_oi_180132.pdf#page=3); REPORT [p4 Patient Characteristics](../../../jama_cooper_2018_oi_180132.pdf#page=4).

**Printed statements:** Final PLAN p84 includes all randomly assigned patients except those withdrawing all-data consent AND those not fulfilling inclusion criteria and never receiving intervention. V8 amendment explicitly calls this modifiedITT and describes alcohol/drug-associated altered consciousness instead of TBI as a possible member of the latter class. REPORT p3 says all a-priori analyses by randomized group, excluding consent withdrawals unless otherwise indicated. REPORT p4 says11 consent withdrawals leave500 evaluable; eligibility exclusions are described for PP/as-treated analyses separately.

**Rule and calculation:** The specified full-analysis sets differ: PLAN randomized minus consent withdrawals minus not-eligible-and-never-intervention patients; REPORT randomized minus consent withdrawals. REPORT511−11=500 reproduces its stated set. The supplied report does not quantify whether the second exclusion class is empty in the primary set. The finding is the printed membership-rule contrast, not a claim that a known number of participants must be removed or that the500 count fails arithmetic. Display precision does not apply to a set-definition change.

**Qualifying route:** Route B.

**Affected result or extracted value:** The intended primary favorable-GOSE analysis population and interpretation of the reported randomized comparison as fullITT or modifiedITT.

**Why context does not resolve it:** The final protocol and disclosed amendment explicitly retain the extra exclusion, while the report distinguishes eligibility restrictions only in sensitivity populations. The numerical511−11 description does not explain whether the planned excluded class was empty, removed elsewhere, or retained.

**Alternatives and missing definition:** There may have been no participant meeting BOTH noneligibility and never-intervention criteria, so realized sets coincide. A later published SAP could amend the rule, but only its pointer is supplied and its contents cannot be assumed. Missing definitions: occurrence/count of this class in the primary population and any final supplied amendment to its exclusion rule.

**Exact human question:** Did the primary analysis apply the final protocol's not-eligible-and-never-intervention exclusion, and if so, was that class empty or excluded separately from the11 consent withdrawals?

### F-ST1-205

**Title:** The DSMC charter's printed approximate P threshold does not match its stated normal three-SD monitoring boundary.

**Relationship:** S437. **Focus area:** D, B. **Proposed review domain:** plan_material. **Proposed primary/all relationships:** P_P / P_P.

**Compared locations and document roles:** PLAN [DOC-002 p188 Statistical Monitoring Guidelines](../../../joi180132supp1_prod.pdf#page=188), normal-binomial boundary paragraph; PLAN [p84 §15.1.3 two-sided-tests definition](../../../joi180132supp1_prod.pdf#page=84) supplies the overall plan's sidedness context. The source's2015 charter transcript is supplied as part of the plan bundle.

**Printed values:** Conventional Haybittle–Peto three-standard-deviation boundary '|Zk|≥3', calculated from a normal approximation to the discrete binomial difference, followed by '(approximate P<0.001 in both cases)'. The source says the two interim analyses assess dichotomized GOSE or mortality at DSMC discretion.

**Rule and calculation:** Under the explicitly stated standard-normal approximation, at|Z|=3 the two-sided tail probability2[1−Φ(3)]=.002699796, and even the one-sided tail is.001349898; neither is below.001. P<.001 corresponds to|Z|>3.290527 for a two-sided rule, rather than3. These calculations use the source's normal approximation, not an inferred exact binomial test. Display-precision cannot exclude a routeA interval/P/test conflict; even allowing a printed.001 threshold interval [.0005,.0015], the two-sided.002699796 probability remains separated by.001199796, relative1.199796>.05.

**Qualifying route:** Route A, category 1.

**Affected result or extracted value:** The efficacy/safety stopping threshold a reviewer extracts for the planned interim primary neurological or mortality monitoring.

**Why context does not resolve it:** This is the routeA test/P category. The statement's word 'approximate' and the overall conservative nature of the boundary do not make these numerical normal-tail thresholds the same.

**Alternatives and missing definition:** The three-SD Z rule may have governed practice, with '<.001' meant as a qualitative shorthand; alternatively an intended P<.001 boundary would require a larger criticalZ. Discrete tests can have different tail probabilities, but the supplied rule expressly specifies the normal approximation. Missing definition: whether Z≥3 or the printed P<.001 is the operative threshold.

**Exact human question:** Which stopping threshold governed the two stated interim analyses, |Z|≥3 or P<.001, and what sidedness/test definition gives the charter's printed P approximation?

## Excluded observations

Only apparent issues not emitted appear here. Reconciled checks without an apparent issue remain in the S inventory. Every row has exactly one reason code.

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC-002 pp27,83; REPORT p3 |80% versus82% primary power, with different software/test approximations possible; discrepancy below5% and no reproducible precise-method conflict. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 pp83–84; REPORT p4 |Final significance .0459 versus displayed .05: copy intervals [.04585,.04595] and [.045,.055] overlap. Exact borderline stopping/decision applicability remains a named limitation, without asserting a reported significance reversal. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN DOC-002 p84 vspp85–86 |Eleven endpoint tests versus six monitoring occasions: five dual-endpoint occasions plus one mortality-only occasion gives11; prose mixes counts of endpoints and occasions. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002 pp15,19,144 |Original ICU-discharge secondary mortality absent final plan: V2→3 explicitly deletes it, so versions are not conflicting simultaneous specifications. | NOT_REPRODUCED |
| PLAN DOC-002 pp15,19,140,72–73 |Original AQOL8 versus final SF12: supplied amendment explicitly replaces instrument. | NOT_REPRODUCED |
| PLAN DOC-002 pp22,78,139,144,148; REPORT p4 |Original planned run-in count versus eight realized nonrandomized run-in participants: different versions and planned versus realized administrative count. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 pp72–73; REPORT pp3–4 |Prespecified secondary outcomes called exploratory for interpretation because no multiplicity adjustment; they remain labeled secondary in the REPORT outcome definition. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002 pp72–73,84; REPORT p3 |Sliding-dichotomy/QOL/cost-effectiveness/CACE expressly not reported here, but supplied sources do not designate these as key secondary or put their results in abstract; omitted ordinary secondary output alone is outside required key-secondary omission category. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 pp25,81 vspp19,72; REPORT pp2–3 |Six-month injury versus randomization anchor differs by≤3h enrollment window and is immediately understandable for this follow-up. | CONTEXT_RESOLVES |
| PLAN DOC-002 p73; REPORT p4 |'Interaction' between time-to33°C and GOSE in cooling arm versus χ² association: intended within-arm outcome association is clear, no second interaction factor specified. | TERMINOLOGY_OR_WORDING |
| PLAN DOC-002 pp84–85; REPORT pp3–4 |Absent full externally published SAP leaves exact prespecified covariate list unavailable; no printed statement conflicts merely because REPORT names IMPACT-TBI. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 p183,p187Figure2 |MapperPD053 transcribed hypothermia-to-standard early-death cooling '>48h'; exact source direct render prints '<48h' and agrees with update prose. | NOT_REPRODUCED |
| PLAN DOC-002 pp183,187 |Exactly48h compliance boundary not separately described; no actual reported classification/value at the boundary supplied. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp85–86; REPORT p3 |SAE ascertainment through7d after treatment cessation compared with adverse-event outcomes within10d: different defined quantities, no matched-window conflict. | NOT_REPRODUCED |
| PLAN DOC-002 p132 |PK appendix AUC adds concentration multiplied terminalslope, dimensional gap if slope is1/h; separate unreported substudy does not govern a parent reported result or decision rule. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 pp99–100 vsp131 |Propofol appendix 'passively rewarm' versus parent active rewarming: separate observational substudy description; no supplied parent result relies on that appendix wording. | PERIPHERAL_COMPARISON |
| PLAN DOC-002 p177 vspp174–175 |Version8 adoption filename/header date difference without changed inference, population or decision rule. | PERIPHERAL_COMPARISON |

## Limitations and full-check closure

Published SAP full text and published protocol full text are external pointers only; their contents were not retrieved or inferred. Exact East design inputs/output, baseline multinomial category probabilities for ordinal power, within-subject covariances for substudies, and raw participant data are absent. These limit exact reproduction but do not create findings without source conflict. Standard-normal power calculations in S427,S462–463,S466,S469,S471 are labeled diagnostics and do not replace the source's analysis. No primary/key-secondary estimate, CI, P value or SE in the final report was independently checked by this method shard; those relationships belong to its companion high shards, including a separately commissioned monitoring-value shard. All82 assigned method/design relationships are PASS_1_COMPLETE. No coverage gap remains in this assigned scope.
# Statistical pass 1 — DSMC monitoring displays

Runtime: 01a129be-d2f9-73e3-94d5-a2df0a75cd43; gpt-6.1-sol/high; fresh spawn. Scope DOC-002 physical pp.189–194, PLAN by content. Stable relationships S601–S685 (85), fully recorded in `statistics/parts/monitoring.md`, each PASS_1_COMPLETE. Complete normative scope and review contract read. Sources/old audit artifacts preserved. No web, external literature, custom Python, old candidates or old conclusions used.

Direct source: `pdftotext -layout -f 189 -l 194 joi180132supp1_prod.pdf -`. All six source-matched reusable page images inspected. Finding independently confirmed on a fresh direct-source p192 render with Poppler pdftoppm25.03.0, CPU, command/derivative recorded in the relationship part.

## Findings

### F-ST1-301

**Title:** The July2016 cumulative favourable-GOSE chart's Y series follows unfavourable counts.

**Relationships:** S636, S641, S642, S654. One repeated cumulative-series pattern; all affected points retained below.

**Exact compared locations and document roles:** PLAN DOC-002 [`joi180132supp1_prod.pdf`, physical p192](../../../joi180132supp1_prod.pdf#page=192), upper chart, “180 day favourable outcome (GOSE5–8) in blocks of25”, Y numerator/denominator row; same PLAN p192 lower chart, “Cummulative 180 day favourable outcome (GOSE5–8)”, blue Y series. PLAN [physical p191](../../../joi180132supp1_prod.pdf#page=191), GOSE favourable and unfavourable score rows, corroborates totals but is not needed to reproduce the same-page cumulative discrepancy.

**Printed values:** The p192 Y favourable block pairs are7/13,2/8,11/16,5/10,8/10,6/12,3/8,5/12,6/14,5/12,2/9,4/9,3/11,6/9. The lower blue Y series lies near6,12,17,22,24,30,35,42,50,57,64,69,77,80 at the corresponding successive blocks. These are graphical coordinates read against labelled count-axis ticks, not printed point-label transcriptions. The lower orange X series follows its favourable block sums. The table prints favourable Y73 and unfavourable Y80.

**Rule and calculation:** A cumulative favourable-count series should sum the favourable numerators in its corresponding block series. That method reproduces orange X throughout:10,18,20,27,36,41,50,57,62,66,69,78,81,86. Applied to Y it yields7,9,20,25,33,39,42,47,53,58,60,64,67,73, whereas the displayed blue line follows the complements (denominator minus favourable count):6,12,17,22,24,30,35,42,50,57,64,69,77,80. The complement identity is an observed reproduction pattern, not a claim about production mechanism.

**Display-precision calculation:** For the second cumulative point (through block26–50), displayed favourable inputs7 and2 each receive ±.5, giving cumulative interval[8,10]. The plotted blue Y point is near12; a conservative graphical reading interval[11,13] is used, wider than the usual ±.5 count-display interval. The interval gap is at least1, relative to the graphical count12 it is at least1/12=.0833>.05. With usual half-unit graphical precision[11.5,12.5], the gap is1.5/12=.125. The third point should sum7+2+11=20, interval[18.5,21.5], while the graphical reading is near17; using ±.5 gives[16.5,17.5], gap1/17=.0588>.05. The second point is the conservative reproduction anchor. End totals73 versus graph near80 corroborate the pattern; that endpoint alone is not the inclusion anchor because permitting14 independent half-unit input intervals gives an interval broad enough to overlap80.

**Focus area:** A/B, cumulative count and outcome identity used in primary dichotomized-GOSE interim monitoring.

**Proposed review domain:** `plan_material`.

**Proposed primary relationship type:** `P_P`; **All relationships:** `P_P`.

**Qualifying route:** Route A, category4. The printed graphical cumulative result does not reproduce under a cumulative-sum method that reproduces the other series of the same display, with a reproduced relative discrepancy>.05. The monitored outcome is the primary GOSE dichotomy used in the supplied interim decision process; these are operational monitoring inputs rather than background historical baseline values.

**Affected result or extracted value:** Y cumulative favourable-GOSE count at the350-patient July2016 monitoring review, particularly cumulative count through block26–50 (near12 in the cumulative display versus9 from the favourable block numerators), and the identity of the Y curve presented to support primary-outcome monitoring.

**Why context does not resolve it:** Route A category4 applies. A reader sees a favourable-outcome title, favourable block pairs and an X cumulative series that agree, alongside a Y cumulative series representing different outcome counts. The immediate display does not state that Y is intended to show unfavourable outcomes. The table and upper chart reproduce one reading while the lower chart supplies another; reconstruction of the intended series does not eliminate the displayed count a reader may use.

**Alternatives and missing definition:** The blue series may intentionally have been an unfavourable outcome series, with an undeclared difference from the X series/title; alternatively it may be intended as a favourable series. No point-level data labels or explanatory note specify a different Y estimand. The exact plotted-series data are not supplied as structured numbers; the conservative early-point graph-reading bound is therefore explicit. No claim is made about whether the DSMC used this line rather than the coherent table or about any resulting stopping decision. Arm identity is not supplied and is not inferred.

**Classification ambiguity:** The observation is entirely inside prospective PLAN monitoring material; no REPORT location is a side of the discrepancy. The independent screen should assess the proposed routeA category4 application to a graphical cumulative primary-outcome result. No separate protocol-versus-report claim is made.

**Exact human question:** Should the July2016 p192 blue Y cumulative series represent favourable GOSE5–8 counts, as the title and block table state, or unfavourable GOSE1–4 counts, which reproduce the plotted sequence; which cumulative series should a reader use for this monitoring display?

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| PLAN DOC-002 pp189,191,193, monitoring-table P columns and GOSE-score rows | Specific tests, sidedness, variance estimation and the name of the parenthesized GOSE dispersion are not supplied. Exact P reproduction or a claimed method/data conflict would depend on additional assumptions; all means and diagnostic sample SDs reconcile and no confidence interval or printed test conclusion contradicts these P values. | CONDITIONAL_OR_UNREPORTED |

## Completed checks and limitations

All GOSE-category count sums, category-derived mean scores, diagnostic sample SDs, favourable/unfavourable/death/survival aggregates, table percentages under display precision, missingness/refusal/enrollment decompositions, block numerator bounds, block denominator sums, bar-height/numerator matches, and cumulative-chart/table outcome matches were reviewed. Two dates' Y cumulative favourable plots differ in the expected way: May2017 p194 follows its favourable counts, while the July2016 p192 pattern above remains reproduced against its own block data. No issue is inferred merely from increasing contributor counts over time.

No estimate interval, printed confidence level, standard error, test statistic, equivalence/noninferiority margin, or stopping conclusion occurs in this six-page shard. Exact table-test mechanics cannot be established; those definitions are missing, not substituted by conventional assumptions. The supplied primary-outcome monitoring P values .26/.53/.68 do not satisfy the charter's .001 threshold, so these displayed tests do not themselves create a stopping-rule conflict. No treatment identity or individual-level data is inferred. Graphical reading precision is explicitly bounded. Findings1; excluded observations1; relationships85; uncovered units0.

## Complete first-pass relationship records

The four detailed first-pass statistical inventories contain the scientific source checks for all369 S IDs. Their records are copied here without loss so the canonical checker directly exposes every relationship, in addition to its findings/exclusions. Distinct second-pass completion is recorded in checkers/statistical_pass_2.md. Historical PLAN labels on observed DSMB numerical locations S601–S685 are superseded by REPORT content assignments confirmed in recheck/pass2/audit; prospective charter rules remain PLAN.

### report_main first-pass records

| S ID | Exact source location (REPORT) | Printed relationship and complete components | Pass 1 check and outcome | Pass 1 status | Pass 2 status |
|---|---|---|---|---|---|
| S001 | DOC-001 pp 1,2,5,7 | Primary 6-month favorable GOS-E H 117/240(48.8), N 111/226(49.1); RR 0.99(0.82–1.19), P .94; RD abstract+0.4(−9.4,8.7), body−0.4(−9.4,8.7) | RR/RD intervals ordered and contain estimates; χ² P .937204 agrees .94; primary direction discrepancy F-ST1-001. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S002 | DOC-001 pp 3–5,7 | Severity-adjusted favorable RR 0.98(0.87–1.11), P .75; hierarchical log-binomial, extended IMPACT covariate, location/site random effects | Containment/null/test decision agree; log-scale Wald diagnostic P ≈.75; no independent reproduction without model inputs. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S003 | DOC-001 p 7 | Hospital death 52/260 vs 43/239; RD 2.0(−4.9,8.9), RR 1.11(0.77–1.60), P .57 | Unadjusted ratios, Wald log-RR/RD and χ² P .568097 reproduce display; all decisions agree. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S004 | DOC-001 pp 5,7 | 6-month death 54/256 vs 44/239; RD 2.7(−4.3,9.7), RR 1.15(0.80–1.64), P .45 | χ² P .453996 and log-RR/RD intervals reproduce; direction and nonsignificance agree. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S005 | DOC-001 pp 1,5,7; DOC-003 p 10 | Pneumonia 143/260 vs 123/240; RD 3.8(−5.0,12.5), RR 1.07(0.91–1.27), P .40 | χ² P .401146 and intervals reproduce; all copies agree. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S006 | DOC-001 p 7; DOC-003 p 10 | Bacteremia 19/260 vs 12/240; RD 2.3(−1.9,6.5), RR 1.46(0.72–2.95), P .29 | χ² P .285058 and intervals reproduce; lower endpoint 0.72499 allows 0.72 at supplied rounded parameters. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S007 | DOC-001 p 7; DOC-003 p 10 | Other infection 36/260 vs 38/240; RD−2.0(−8.2,4.3), RR 0.87(0.57–1.33), P .53 | χ² P .531864 and intervals reproduce; direction agree. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S008 | DOC-001 pp 1,5,7; DOC-003 p 10 | Intracranial bleeding 47/260 vs 37/240; RD 2.7(−3.9,9.2), RR 1.23(0.43–3.5), P .70; supplementP .43 | Count-based RR 1.172557(0.791181–1.737769), χ² P .426669; F-ST1-002. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S009 | DOC-001 p 7; DOC-003 p 10 | Extracranial bleeding 8/260 vs 6/240; RD 0.6(−2.3,3.5), RR 1.17(0.79–1.74), P .43; supplementP .70 | Count-based RR 1.230769(0.433345–3.495582), χ² P .696039; F-ST1-002. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S010 | DOC-001 p 7 | Surgically removed hematoma yes:22/66 vs 27/68; RD−6.4(−22.6,9.9), RR 0.84(0.54–1.32), P .44 | Containment, endpoint order, unadjusted direction and nonsignificance agree. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S011 | DOC-001 p 7 | Surgically removed hematoma no:95/174 vs 84/158; RD 1.4(−9.3,12.2), RR 1.03(0.84–1.25), P .79 | Containment, unadjusted direction and nonsignificance agree. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S012 | DOC-001 pp 4,6,7 | Treatment×surgically removed hematoma logistic interaction P .43 | No significant interaction claim agrees; no coefficient/SE supplied for exact recomputation. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S013 | DOC-001 p 7 | Any intracranial mass yes:22/69 vs 28/71; RD−7.6(−23.4,8.3), RR 0.81(0.52–1.27), P .35 | Containment, unadjusted direction and nonsignificance agree. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S014 | DOC-001 p 7 | Any intracranial mass no:95/171 vs 83/155; RD 2.0(−8.8,12.8), RR 1.04(0.85–1.27), P .72 | Containment, unadjusted direction and nonsignificance agree. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S015 | DOC-001 pp 4,6,7 | Treatment×any intracranial mass logistic interaction P .33 | No significant interaction claim agrees; no coefficient/SE supplied. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S016 | DOC-001 pp 4,5,7 | Ordinal GOS-E odds ratioH/N 0.97(0.71–1.34), P .88; ordinal logistic, score-test proportional-odds justification; Figure 3 all 8ordered categories | Interval containment/order/null/test conclusion agree; no score statistic or category-level exact data supplied; graph direction agrees. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S017 | DOC-001 pp 4,5; DOC-003 p 5 | Unadjusted death HR 1.13(0.76–1.69), P .54; Cox model and corresponding KM/logrank | Containment/order/null/P agree; ratio distinguishes hazards from crude risk; administrative censoring discrepancy trackedS033. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S018 | DOC-001 pp 1,2,7,8 | Superiority conclusion: no improvement 6-month neurological outcome; all secondary exploratory, two-sided P <.05, no multiplicity adjustment | Primary CI includes null and P .94; no noninferiority/equivalence/margin claim; conclusion follows stated primary rule. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S019 | DOC-001 pp 3,4 | Randomized-group analysis excluding consent withdrawals; no missing-data imputation; unadjusted χ² binary; hierarchy/log-binomial adjustment; logistic interactions; alternative PP/as-treated subsets | Distinct analyses identified; missing definitions do not alone form observations. Design/plan comparators are separate assigned shard. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S020 | DOC-001 pp 1,4,5 | Baseline age means(SD)H 35.0(13.5), N 34.1(13.4), overall 34.5(13.4) | Weighted mean 34.568 close within precision; positive SD; no between-group P printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S021 | DOC-001 pp 4,5 | Baseline GCS overall H 6(4–7), N 6(4–7), overall 6(4–7) median (IQR) | Both medians inside ordered IQR and scale 3–15. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S022 | DOC-001 p 5 | Baseline motor GCS H 3(1–4), N 3(2–5) median (IQR) | Both medians inside ordered IQR. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S023 | DOC-001 p 5 | Scene temperature mean (SD)H 36.0(1.2), N 35.9(1.0)°C; observed n 162/143 | Positive dispersion, correct descriptive rather than CI interpretation; no printed test. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S024 | DOC-001 p 5 | IMPACT core+CT probability unfavorable 6-month mean (SD)0.46(0.24)/0.46(0.23), scale 0–1 | Means within probability scale; SD feasible; differs from extended score adjustment definition as separately named quantity. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S025 | DOC-001 p 5 | ISS median (IQR)H 26.0(18.0–34.0), N 20.0(20.5–35.0) | N median below Q1 logically; half-unit gap.40/20=.02; excluded ROUNDING_OR_DISPLAY_PRECISION because descriptive IQR, not inferential CI. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S026 | DOC-001 p 5 | Injury→randomization median (IQR)H 1.8(1.0–2.7), N 2.0(1.1–2.8)h | Containment and ordered endpoints agree. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S027 | DOC-001 pp 1,4,8 | Overall injury→randomization 1.9(1.0–2.7), initiation 1.8(1.0–2.7), H cooling duration 72.2(69.8–77.3), rewarming 22.5(16–27)h | All medians inside ordered IQR; target time and initiation are distinguished source-defined quantities. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S028 | DOC-001 p 6 | Figure 2 A temperature/B ICP; all 17/16six-hour blocks per arm; medians,25–75%boxes,1.5IQR whiskers; contributors M068, M069, M071; observed unimputed | All plots visually checked for median/box order and H temperature direction; unique per interval counts need not monotonically decrease; hourly observations are repeated same patient, no independence inference imposed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S029 | DOC-001 pp 4,6 | Claim core temperature significantly lower H first 96 h; Figure 2 gives descriptive boxes without test statistic/P/method | Direction visually agrees; precise significance-test reproduction unavailable; apparent missing test definition excluded CONDITIONAL_OR_UNREPORTED. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S030 | DOC-001 p 6 | PP pneumonia 70.5%vs 57.1%; RD 13.3(2.4–24.2), RR 1.23(1.04–1.47), P .02 | Containment/order/direction/superiority decisions agree; rounded percentages RD 13.4 versus 13.3 within precision; detailed PP table separate shard. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S031 | DOC-001 p 6 | As-treated pneumonia 70.7%vs 54.6%; RD 16.1(5.7–26.5), RR 1.29(1.09–1.53), P .003 | Containment/order/direction/significance agree; detailed as-treated table separate shard. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S032 | DOC-003 p 4 | eFigure 1 nine 4-hour rewarming bins; temperature°C/ICPmmHg least square means 95%CI, longitudinal mixed linear patient random effect | Every graphical mean inside CI, endpoints ordered; explicit repeated patient model; no P/numeric endpoints supplied; no invented exact values. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S033 | DOC-003 p 5; DOC-001 pp 2,4,5 | KM survival plot at days 0,50,100,150,200,250; risk H 260,206,202,200,91,23; N 240,196,195,195,88,17; logrankP .5349; HR 1.13(.76–1.69), P .54; stated censor 6 months/last contact | Risk sets monotone and curves nonincreasing; survival rather than death; caption resolved by axis; logrank versus Cox P variation coherent; censoring beyond 6 months F-ST1-003. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S034 | DOC-003 p 6 | Randomization location:out of hospital 123/260(47.3)vs 101/240(42.1); ED137/260(52.7)vs 139/240(57.9); shared P .24 | Complement categories sum to total; χ² testP ≈.239 corroborates nonsignificance; counts scoped numeric checker. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S035 | DOC-003 p 6 | Out-of-hospital injury→randomization 1.0(.8–1.3)vs 1.0(.7–1.4)h, P .98 | Median containment/order agree; rank test cannot reproduce from quartiles alone; no CI versus P conflict. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S036 | DOC-003 p 6 | Hospital injury→randomization 2.6(2.0–3.0)vs 2.6(2.2–3.0)h, P .58 | Median containment/order agree; no distributional reconstruction from quartiles. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S037 | DOC-003 p 6; DOC-001 p 4 | Reached 35°C 233/260(89.6%); time 2.5(.8–5.5)h median (IQR) | Proportion/containment/order/copy agree; N NA not a treatment effect. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S038 | DOC-003 p 6; DOC-001 p 4 | Reached 33°C 186/260(71.5%); time 10.1(6.8–15.9)h median (IQR) | Proportion/containment/order/copy agree; target 33 subset of 35 logic feasible. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S039 | DOC-003 p 7 | Withdrawal 99/260(38.1%), reasons 9,51,35,1,3; N nontrial cooling 23/240(9.6%), first 96 h | Reasons sum 99; all proportions reproduce; no inferential test reported. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S040 | DOC-003 p 8 eTable 4 | ICP monitor inserted; H 205(78.8), N 192(80.0), P .75; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S041 | DOC-003 p 8 eTable 4 | Monitoring duration, d; H 7.2(5.0–9.6), N 6.3(3.6–9.4), P .04; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S042 | DOC-003 p 8 eTable 4 | End hours ICP>20, h; H 6(1–17), N 6(1–24), P .46; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S043 | DOC-003 p 8 eTable 4 | ICP index,%; H 4.2(1.0–11.5), N 4.5(1.3–13.7), P .60; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S044 | DOC-003 p 8 eTable 4 | End hours CPP≤60, h; H 10(3–18), N 10(3–22), P .69; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S045 | DOC-003 p 8 eTable 4 | CPP index,%; H 6.5(2.7–13.5), N 7.4(2.3–15.5), P .52; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S046 | DOC-003 p 8 eTable 4 | Hypertonic saline received; H 133(51.2), N 131(54.6), P .44; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S047 | DOC-003 p 8 eTable 4 | Hypertonic saline standardized 3%, mL; H 1092(359–2347), N 1248(546–2830), P .18; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S048 | DOC-003 p 8 eTable 4 | Mannitol 20%received; H 68(26.2), N 70(29.2), P .45; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S049 | DOC-003 p 8 eTable 4 | Mannitol 20%, mL; H 375(250–500), N 250(200–500), P .20; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S050 | DOC-003 p 8 eTable 4 | Thiopentone received; H 53(20.4), N 59(24.6), P .26; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S051 | DOC-003 p 8 eTable 4 | Thiopentone total, g; H 7(1.3–13.3), N 3.3(.5–12.4), P .26; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S052 | DOC-003 p 8 eTable 4 | CSF venting; H 72(27.7), N 67(27.9), P .96; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S053 | DOC-003 p 8 eTable 4 | PaCO2<33 mmHg; H 202(77.7), N 184(76.7), P .79; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S054 | DOC-003 p 8 eTable 4 | PaCO2<33 mmHg, d; H 4(2–5), N 3(2–5), P .64; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S055 | DOC-003 p 8 eTable 4 | Noradrenaline>15mcg/min; H 145(55.8), N 143(59.6), P .39; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S056 | DOC-003 p 8 eTable 4 | Noradrenaline>15mcg/min, d; H 4(2–6), N 2(2–4), P <.000; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. Very small printed P excluded ROUNDING_OR_DISPLAY_PRECISION. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S057 | DOC-003 p 8 eTable 4 | Adrenaline>5mcg/min; H 17(6.5), N 9(3.8), P .16; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S058 | DOC-003 p 8 eTable 4 | Adrenaline>5mcg/min, d; H 1(1–2), N 1(1–2), P .90; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S059 | DOC-003 p 8 eTable 4 | Subdural evacuation; H 56(21.5), N 51(21.3), P .94; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S060 | DOC-003 p 8 eTable 4 | Extradural evacuation; H 27(10.4), N 31(12.9), P .38; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S061 | DOC-003 p 8 eTable 4 | Intracerebral evacuation; H 4(1.5), N 6(2.5), P .44; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S062 | DOC-003 p 8 eTable 4 | Craniectomy; H 56(21.5), N 60(25.0), P .36; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S063 | DOC-003 p 8 eTable 4 | Bifrontal decompressive craniectomy; H 8(3.1), N 7(2.9), P .92; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S064 | DOC-003 p 8 eTable 4 | Albumin 4–5%received; H 21(8.1), N 22(9.2), P .66; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S065 | DOC-003 p 8 eTable 4 | Albumin 4–5%, mL; H 1000(500–1500), N 500(500–1000), P .54; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S066 | DOC-003 p 8 eTable 4 | Red blood cells received; H 82(31.5), N 82(34.2), P .53; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S067 | DOC-003 p 8 eTable 4 | Red blood cells, mL; H 753(512–1342), N 900(565–1500), P .21; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S068 | DOC-003 p 8 eTable 4 | FFP received; H 58(22.3), N 62(25.8), P .36; Hn 260, Nn 240 | Count percentages and χ² diagnostic agree within display precision; no interval printed. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S069 | DOC-003 p 8 eTable 4 | FFP, mL; H 1058(600–1791), N 973(600–1673), P .75; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S070 | DOC-003 p 8 eTable 4 | Fluid balance day 1, mL; H 2139(1000–3501), N 1897(635–3669), P .29; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S071 | DOC-003 p 8 eTable 4 | Fluid balance days 1–5, mL; H 2100(994–3441), N 1900(640–3687), P .44; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S072 | DOC-003 p 8 eTable 4 | Fluid balance days 6–10, mL; H −505(−1319–301), N −240(−1116–616), P .04; Hn 260, Nn 240 | Median within ordered IQR in both arms; IQR is a distributional spread, not effect CI; printed P cannot be rebuilt from summaries alone. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S073 | DOC-003 p 9 | Mechanical ventilation 8.3(3.6–12.5)/6.9(2.8–11.8)d, P .06 | Medians inside IQR; nonsignificance agrees with main; full rank data unavailable. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S074 | DOC-003 p 9 | ICU stay 11.9(5.7–18.3)/11.4(4.7–17.5)d, P .33 | Medians inside IQR; no CI versus P conflict; full rank data unavailable. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S075 | DOC-003 p 9 | Hospital stay 19.8(10.2–31.8)/18.8(8.1–32.8)d, P .74 | Medians inside IQR; no CI versus P conflict; full rank data unavailable. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S076 | DOC-003 p 9 | GOS-E 6-month mean (SD)4.2(2.2)/4.2(2.2), n 240/226, P .86 | Means within 1–8 and SD positive; rounded means equal do not imply P=1; no exact mean/stated test supplied. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S077 | DOC-003 p 9 | Unfavorable GOS-E 2–4 among survivors 69(37.1%)/71(39.0%), P .71 | Denominators reconstruct 186/182 from 240−54/226−44; χ² P ≈.71; favorable+unfavorable+deaths partition primary GOS-E population. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S078 | DOC-003 p 10 | Bradycardia<40 bpm 49/260(18.8)/10/240(4.2), P <.0001 | χ² P ≈3.716e−7 supports printed bound and direction. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S079 | DOC-003 p 10 | VT 7/260(2.7)/5/240(2.1), P .66 | χ² P .656678 reproduces. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S080 | DOC-003 p 10 | VF 1/260(.4)/0/240(0), P 1.00 | χ² P .336185; Fisher P 1.00 alternative; F-ST1-005. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S081 | DOC-003 p 10 | Asystole/PEA 7/260(2.7)/7/240(2.9), P .88 | χ² P .879243 reproduces. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S082 | DOC-003 p 10 | H induction hypotension 18/260(6.9), N NA; MAP <60 definition | Percentage reproduces; no between-group inferential claim. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S083 | DOC-003 p 10 | H maintenance hypotension 23/260(8.8), N NA; MAP <60 definition | Percentage reproduces; no between-group inferential claim. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S084 | DOC-003 p 10 | Pneumonia 143/260(55.0)/123/240(51.3), P .40 | Supplement-only test cross-references S005; χ² P .401146. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S085 | DOC-003 p 10 | Bacteremia 19/260(7.3)/12/240(5.0), P .29 | Supplement-only test cross-references S006; χ² P .285058. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S086 | DOC-003 p 10 | Other infection 36/260(13.8)/38/240(15.8), P .53 | Supplement-only test cross-references S007; χ² P .531864. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S087 | DOC-003 p 10 | Intracranial bleeding 47/260(18.1)/37/240(15.4), P .43 | χ² P .426669 reproduces; matched main S008; F-ST1-002. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S088 | DOC-003 p 10 | Extracranial bleeding 8/260(3.1)/6/240(2.5), P .70 | χ² P .696039 reproduces; matched main S009; F-ST1-002. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S089 | DOC-003 p 10 | Intractable ICP43/260(16.5)/43/239(18.0), P .67; >20 mmHg>20 minutes, maximal therapy | χ² P .667657 reproduces; exact denominators honored. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S090 | DOC-003 p 11 | Time to 33°C1–7 h:18/49[36.7%(22.8–50.7)] | Proportion reproduces; 95%CI ordered and contains 36.7; Wald CI 23.2366–50.2327 diagnostic difference≤5% after precision. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S091 | DOC-003 p 11 | Time to 33°C8–13 h:28/67[41.8%(29.6–53.9)] | Proportion reproduces; 95%CI ordered and contains 41.8; Wald CI 29.9811–53.6010 diagnostic difference≤5% after precision. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S092 | DOC-003 p 11 | Time to 33°C>13 h:32/59[54.2%(41.2–67.3)] | Proportion reproduces; 95%CI ordered and contains 54.2; Wald CI 41.5249–66.9497 diagnostic difference≤5% after precision. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S093 | DOC-003 p 11 | Never 33°C:39/65[60.0%(47.8–72.2)] | Proportion reproduces; 95%CI ordered and contains 60; Wald CI 48.0904–71.9096 diagnostic difference≤5% after precision. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S094 | DOC-003 p 11; DOC-001 pp 4,5 | eTable 7 shared P .09, unadjusted χ² equal proportions effect of time 33°C stated in main; four display groups | χ²(3)=8.133762, P .0433268 vs.09; F-ST1-004; no assumed trend coding. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |
| S095 | DOC-001 p 3 | Historical power basis RR 1.46(1.12–1.92), P .006; prior <45subgroup 50% increase, P .02 | Historical cited numbers: containment/order/null/significance agree; original external studies not fetched; no primary trial result mapped to historical contrast. | PASS_1_COMPLETE | PASS_2_COMPLETE in distinct second-pass checker |

### report_support first-pass records

| S ID | Source location and population | Printed relationship, including all components | Pass-1 check and remaining definition | Status |
|---|---|---|---|---|
| S201 | [p.12 PP methods](../../../joi180132supp2_prod.pdf#page=12), REPORT | Retrospective severe TBI; exclude eligibility deviations; cooling >48h at ≤35°C within96h; exclude noncompliant survivors/known-noncompliant early deaths; include compliant or undetermined early deaths. | Explicit population rule, coherent with flow; no source conflict established locally. | PASS_1_COMPLETE |
| S202 | [p.12 eFigure3](../../../joi180132supp2_prod.pdf#page=12), REPORT | Randomized511=266H+245N; consent6H/5N; prehospital exclusions14H=2+5+7,10N=2+8; hospital exclusions29H=26+3,29N=26+3; ICU217H/201N; early withdrawals50H=5+10+35,4N; nonsevere35N; ICU35H=30survivors+5deaths,1N; missing8H,1lost+9unavailableN; outcomes124H/151N. | 266−6−14−29=217;245−5−10−29=201;217−50−35−8=124;201−4−35−1−10=151. Baseline132/161 reconciles before outcome missingness. | PASS_1_COMPLETE |
| S203 | [p.13 eTable8 sex](../../../joi180132supp2_prod.pdf#page=13), REPORT,132H/161N | Men107(81.1)/132(82.0);women25(18.9)/29(18.0);P=.84. | Counts sum to arm totals; pooled two-arm proportion diagnostic agrees; one shared test. | PASS_1_COMPLETE |
| S204 | [p.13 eTable8 age](../../../joi180132supp2_prod.pdf#page=13), REPORT | Means(SD)35.2(12.9)/34.4(13.0)y;P=.57. | Rounded mean/SD diagnostic compatible; exact test implementation not supplied. | PASS_1_COMPLETE |
| S205 | [p.13 eTable8 GCS overall](../../../joi180132supp2_prod.pdf#page=13), REPORT | Median(IQR)5(4–7)/6(4–7);P=.35. | Quartiles ordered, medians contained; individual ranks unavailable. | PASS_1_COMPLETE |
| S206 | [p.13 eTable8 GCS motor](../../../joi180132supp2_prod.pdf#page=13), REPORT | 3(1–4)/3(2–5);P=.25. | Quartiles ordered, medians contained; ranks unavailable. | PASS_1_COMPLETE |
| S207 | [p.13 eTable8 pupils](../../../joi180132supp2_prod.pdf#page=13), REPORT | One/both reacting113/132(85.6)/137/161(85.1);P=.90. | Count-percent and two-arm decision compatible. | PASS_1_COMPLETE |
| S208 | [p.13 eTable8 hypotension](../../../joi180132supp2_prod.pdf#page=13), REPORT | 10/130(7.7)/12/160(7.5);P=.95;SBP<90mmHg. | Explicit row denominators; count-percent/test compatible. | PASS_1_COMPLETE |
| S209 | [p.13 eTable8 hypoxia](../../../joi180132supp2_prod.pdf#page=13), REPORT | 18/129(14.0)/25/159(15.7);P=.68;SpO2<90%. | Explicit row denominators; count-percent/test compatible. | PASS_1_COMPLETE |
| S210 | [p.13 eTable8 temperature](../../../joi180132supp2_prod.pdf#page=13), REPORT | Mean(SD)35.9(1.1)/35.9(1.0)°C;scene n78H/83N;P=.98. | Rounded equal displayed means do not require exact equal underlying means; diagnostic compatible. | PASS_1_COMPLETE |
| S211 | [p.13 eTable8 CT](../../../joi180132supp2_prod.pdf#page=13), REPORT | I2(1.5)/2(1.2),II72(54.5)/84(52.2),III/IV14(10.6)/15(9.3),V44(33.3)/58(36.0),VI0(0)/2(1.2);sharedP=.73. | Category totals132/161; one omnibus test; cells reconcile. | PASS_1_COMPLETE |
| S212 | [p.13 eTable8 IMPACT](../../../joi180132supp2_prod.pdf#page=13), REPORT | Unfavorable-probability mean(SD).48(.23)/.47(.21);P=.74;range0–1. | Rounded summary diagnostic compatible; not an observed favorable proportion. | PASS_1_COMPLETE |
| S213 | [p.13 eTable8 ISS](../../../joi180132supp2_prod.pdf#page=13), REPORT | Median(IQR)29(21–34.5)/29(22–35);P=.44;scale0–75. | Ordered/contained; ranks unavailable. | PASS_1_COMPLETE |
| S214 | [p.13 eTable8 injury cause](../../../joi180132supp2_prod.pdf#page=13), REPORT | Motor43(32.6)/59(36.6),motorcycle14(10.6)/12(7.5),bicycle12(9.1)/14(8.7),pedestrian15(11.4)/28(17.4),object13(9.8)/10(6.2),fall28(21.2)/34(21.1),other7(5.3)/4(2.5);sharedP=.45. | All categories total132/161; one omnibus test. | PASS_1_COMPLETE |
| S215 | [p.13 eTable8 ethanol positive](../../../joi180132supp2_prod.pdf#page=13), REPORT | 51/111(45.9)/58/130(44.6);P=.84. | Explicit denominators and count-percent/test compatible. | PASS_1_COMPLETE |
| S216 | [p.13 eTable8 ethanol>51](../../../joi180132supp2_prod.pdf#page=13), REPORT | 38/111(34.2)/43/130(33.1);mg/dL;P=.85. | Explicit denominators and count-percent/test compatible. | PASS_1_COMPLETE |
| S217 | [p.13 eTable8 injury-to-randomization](../../../joi180132supp2_prod.pdf#page=13), REPORT | Median(IQR)1.7(1.0–2.5)/2.0(1.1–2.6)h;P=.18. | Ordered/contained; ranks unavailable. | PASS_1_COMPLETE |
| S218 | [p.14 eTable9 primary](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | Favorable GOS-E5–8 at6months58/124(46.8)/69/151(45.7);RR1.02(.79–1.32);P=.86. | CrudeRR1.02361;logCI.79249–1.32213;null/P agree. | PASS_1_COMPLETE |
| S219 | [p.14 eTable9 adjusted](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | Severity-adjusted RR for favorable outcome using IMPACT1.04(.65–1.69);P=.86. | Ordered/contained/null-P compatible; log-binomial adjustment specified mainpp.3–4; individual model inputs unavailable. | PASS_1_COMPLETE |
| S220 | [p.14 eTable9 hospital death](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | 30/132(22.7)/33/160(20.6);RR1.10(.71–1.71);P=.66. | Crude/log-RR reproduction and null/P agree; denominator160 explicitly row-specific. | PASS_1_COMPLETE |
| S221 | [p.14 eTable9 6month death](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | 31/132(23.5)/34/160(21.3);RR1.11(.72–1.70);P=.65. | Crude/log-RR reproduction and null/P agree. | PASS_1_COMPLETE |
| S222 | [p.14 eTable9 pneumonia](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | 93/132(70.5)/92/161(57.1);RR1.23(1.04–1.47);P=.02. | RR1.23295;logCI1.03657–1.46654;excludes1/P<.05 agree; increased H risk. | PASS_1_COMPLETE |
| S223 | [p.14 eTable9 bacteremia](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | 14/132(10.6)/8/161(5.0);RR2.13(.92–4.93);P=.07. | RR2.13447;logCI.92365–4.93255;null/P agree. | PASS_1_COMPLETE |
| S224 | [p.14 eTable9 other infection](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | 25/132(18.9)/30/161(18.6);RR1.02(.63–1.64);P=.95. | RR1.01641;logCI.63002–1.63978;null/P agree. | PASS_1_COMPLETE |
| S225 | [p.14 eTable9 intracranial bleeding](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | 26/132(19.7)/29/161(18.0);RR1.09(.68–1.76);P=.71. | RR1.09352;logCI.67888–1.76142;null/P agree. | PASS_1_COMPLETE |
| S226 | [p.14 eTable9 extracranial bleeding](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | 2/132(1.5)/6/161(3.7);RR.41(.08–1.98);P=.25. | RR.40657;logCI.08343–1.98117;null/P agree; exact chi-square choice not inferred. | PASS_1_COMPLETE |
| S227 | [p.14 eTable9 surgery yes](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | Favorable12/41(29.3)/20/54(37.0);RR.79(.44–1.42);P=.43. | Counts/percent/RR/interval/null-P agree. | PASS_1_COMPLETE |
| S228 | [p.14 eTable9 surgery no](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | Favorable46/83(55.4)/49/97(50.5);RR1.10(.83–1.45);P=.51. | Subgroup totals match primary; RR/CI/null-P agree. | PASS_1_COMPLETE |
| S229 | [p.14 eTable9 surgery interaction](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | Footnote b interactionP=.31. | Stated logistic interaction; coefficient/SE/covariance absent; no incompatible conclusion. | PASS_1_COMPLETE |
| S230 | [p.14 eTable9 mass yes](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | MarshallV+VI favorable12/41(29.3)/21/56(37.5);RR.78(.44–1.40);P=.40. | Counts/RR/CI/null-P agree. | PASS_1_COMPLETE |
| S231 | [p.14 eTable9 mass no](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | Favorable46/83(55.4)/48/95(50.5);RR1.10(.83–1.45);P=.51. | Subgroup totals match primary; RR/CI/null-P agree. | PASS_1_COMPLETE |
| S232 | [p.14 eTable9 mass interaction](../../../joi180132supp2_prod.pdf#page=14), REPORT,PP | Footnote c interactionP=.29. | Logistic interaction coefficient/SE absent; no incompatible conclusion. | PASS_1_COMPLETE |
| S233 | [p.15 eFigure4](../../../joi180132supp2_prod.pdf#page=15), REPORT,PP | Temperature°C first96h;17coordinates0,1–6,7–12,13–18,19–24,25–30,31–36,37–41,43–48,49–54,55–60,61–66,67–72,73–78,79–84,85–90,91–96;H/Ncurves/bars. | H declines~35.9→33.3 thenrewarm~35.6,N~35.9→37.2;directions consistent. Bar meaning not stated; no exact unprinted CI invented. | PASS_1_COMPLETE |
| S234 | [p.16 PP sensitivity methods](../../../joi180132supp2_prod.pdf#page=16), REPORT | Majorityfirst72h instead96;degree×hours AUCbelow35°C;lineartrapezoid ignoringmissing;SAPreference. | Local AUC cutoff/time mapping not numeric; no contradictory threshold printed; plan definition assigned separately. | PASS_1_COMPLETE |
| S235 | [p.16 agreement](../../../joi180132supp2_prod.pdf#page=16), REPORT | Kappa.93(.90–.97),agreement describedhigh. | Ordered/contained;category cross-tab absent so exact kappa/SE not reconstructed. | PASS_1_COMPLETE |
| S236 | [p.16 eFigure5](../../../joi180132supp2_prod.pdf#page=16), REPORT | Same initialflowS202;HICU39withdrawals=35survivors+4deaths;N1withdrawal;missing8H/10N;primary120H/151N. | 217−50−39−8=120;N unchanged151;footnote explicitly defines majority72h, clarifying figure shorthand. | PASS_1_COMPLETE |
| S237 | [p.16 sensitivity primary](../../../joi180132supp2_prod.pdf#page=16), REPORT | Favorable55/120(45.8)/69/151(45.7);unadjustedRR1.00(.77–1.30);P=.98. | CrudeRR1.00302;loginterval reproduces;null/P agree. | PASS_1_COMPLETE |
| S238 | [p.17 as-treated methods](../../../joi180132supp2_prod.pdf#page=17), REPORT | Retrospective severeTBI/eligibility exclusions;>48h≤35°Cwithin96h;complianttoH/noncomplianttoN;knownnoncompliant earlydeathoppositearm;compliant/undetermined earlydeathassignedarm. | Explicit reassignment and earlydeath rules consistent with flow; no preference for another analysis. | PASS_1_COMPLETE |
| S239 | [p.17 eFigure6](../../../joi180132supp2_prod.pdf#page=17), REPORT | InitialflowasS202;ICU217H/201N;early50H/4N;nonsevere35N;1N→H,35H→N=30survivors+5deaths;missing8H/1lost+11unavailableN;primary125H/184N. | H217−50−35+1−8=125;N201−4−35−1+35−12=184;pre-missing133/196 matchesbaseline. | PASS_1_COMPLETE |
| S240 | [p.18 eTable10 sex](../../../joi180132supp2_prod.pdf#page=18), REPORT,133H/196N | Men108(81.2)/158(80.6);women25(18.8)/38(19.4);sharedP=.89. | Totals/percentages/test compatible. | PASS_1_COMPLETE |
| S241 | [p.18 eTable10 age](../../../joi180132supp2_prod.pdf#page=18), REPORT | Means(SD)35.2(12.8)/34.3(13.2)y;P=.55. | Rounded-summary t diagnostic compatible;exactimplementation absent. | PASS_1_COMPLETE |
| S242 | [p.18 eTable10 GCS overall](../../../joi180132supp2_prod.pdf#page=18), REPORT | Median(IQR)5(4–7)/6(4–7);P=.29. | Ordered/contained;ranks unavailable. | PASS_1_COMPLETE |
| S243 | [p.18 eTable10 GCS motor](../../../joi180132supp2_prod.pdf#page=18), REPORT | 3(1–4)/4(2–5);P=.23. | Ordered/contained;ranks unavailable. | PASS_1_COMPLETE |
| S244 | [p.18 eTable10 pupils](../../../joi180132supp2_prod.pdf#page=18), REPORT | 114/133(85.7)/167/196(85.2);P=.90. | Count-percent/two-arm decision compatible. | PASS_1_COMPLETE |
| S245 | [p.18 eTable10 hypotension](../../../joi180132supp2_prod.pdf#page=18), REPORT | 10/131(7.6)/15/194(7.7);P=.97. | Explicit denominators;percent/test compatible. | PASS_1_COMPLETE |
| S246 | [p.18 eTable10 hypoxia](../../../joi180132supp2_prod.pdf#page=18), REPORT | 18/130(13.8)/30/194(15.5);P=.69. | Explicit denominators;percent/test compatible. | PASS_1_COMPLETE |
| S247 | [p.18 eTable10 temperature](../../../joi180132supp2_prod.pdf#page=18), REPORT | Mean(SD)35.9(1.1)/35.9(1.0)°C;scene78H/99N;P=.87. | Displayed equal means allow unequal underlying roundedmeans;no conflict. | PASS_1_COMPLETE |
| S248 | [p.18 eTable10 CT](../../../joi180132supp2_prod.pdf#page=18), REPORT | I2(1.5)/3(1.5),II73(54.9)/108(55.1),III/IV14(10.5)/15(7.7),V44(33.1)/34.7(68),VI0(0)/1(2);sharedP=.71. | Literal Ncells fail count-percent header;F-ST1-101. Shared test cannot be reconstructed from literal fractionalcount;alternative transposed readings yield196N. | PASS_1_COMPLETE |
| S249 | [p.18 eTable10 IMPACT](../../../joi180132supp2_prod.pdf#page=18), REPORT | Mean(SD).48(.23)/.46(.22);P=.50. | Roundedsummary diagnostic compatible;not observedrisk. | PASS_1_COMPLETE |
| S250 | [p.18 eTable10 ISS](../../../joi180132supp2_prod.pdf#page=18), REPORT | Median(IQR)29(22–35)/29(21–34);P=.59. | Ordered/contained;ranks unavailable. | PASS_1_COMPLETE |
| S251 | [p.18 eTable10 injurycause](../../../joi180132supp2_prod.pdf#page=18), REPORT | Motor43(32.3)/70(35.7),motorcycle14(10.5)/18(9.2),bicycle12(9)/16(8.2),pedestrian15(11.3)/31(15.8),object13(9.8)/13(6.6),fall29(21.8)/43(21.9),other7(5.3)/5(2.6);P=.64. | Categories total133/196;oneomnibus test. | PASS_1_COMPLETE |
| S252 | [p.18 eTable10 ethanolpositive](../../../joi180132supp2_prod.pdf#page=18), REPORT | 52/112(46.4)/69/152(45.4);P=.87. | Explicitdenominators;percent/test compatible. | PASS_1_COMPLETE |
| S253 | [p.18 eTable10 ethanol>51](../../../joi180132supp2_prod.pdf#page=18), REPORT | 39/112(34.8)/52/152(34.2);mg/dL;P=.92. | Explicitdenominators;percent/test compatible. | PASS_1_COMPLETE |
| S254 | [p.18 eTable10 injurytorandomization](../../../joi180132supp2_prod.pdf#page=18), REPORT | Median(IQR)1.7(1.0–2.5)/1.9(1.0–2.6)h;P=.37. | Ordered/contained;ranks unavailable. | PASS_1_COMPLETE |
| S255 | [p.19 eTable11 primary](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | Favorable59/125(47.2)/82/184(44.6);RR1.06(.83–1.35);P=.65. | RR1.05912;logCI.82843–1.35405;null/P agree. | PASS_1_COMPLETE |
| S256 | [p.19 eTable11 adjusted](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | Labelseverity-adjustedRRforunfavorableoutcomeusingIMPACT1.11(.70–1.76);P=.65. | Ordered/contained/null-P compatible;sourceprints unfavorable unlike PProw. No supplied modeloutput establishes recoding;excludedobservation records missing mapping. | PASS_1_COMPLETE |
| S257 | [p.19 eTable11 hospitaldeath](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | 30/133(22.6)/38/195(19.5);RR1.16(.76–1.77);P=.50. | Crude/logRR/CI/null-P compatible;explicit195denominator. | PASS_1_COMPLETE |
| S258 | [p.19 eTable11 6monthdeath](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | 31/133(23.3)/40/195(20.5);RR1.14(.75–1.72);P=.55. | Crude/logRR/CI/null-P compatible. | PASS_1_COMPLETE |
| S259 | [p.19 eTable11 pneumonia](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | 94/133(70.7)/107/196(54.6);RR1.29(1.09–1.53);P=.003. | RR1.29464;logCI1.09422–1.53176;excludes1/P<.05;increasedHrisk. | PASS_1_COMPLETE |
| S260 | [p.19 eTable11 bacteremia](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | 14/133(10.5)/11/196(5.6);RR1.88(.88–4.00);P=.10. | Crude/logRR/CI/null-P compatible. | PASS_1_COMPLETE |
| S261 | [p.19 eTable11 otherinfection](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | 26/133(19.5)/33/196(16.8);RR1.16(.73–1.85);P=.53. | Crude/logRR/CI/null-P compatible. | PASS_1_COMPLETE |
| S262 | [p.19 eTable11 intracranialbleeding](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | 26/133(19.5)/39/196(19.9);RR.98(.63–1.53);P=.94. | Crude/logRR/CI/null-P compatible. | PASS_1_COMPLETE |
| S263 | [p.19 eTable11 extracranialbleeding](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | 2/133(1.5)/10/196(5.1);RR.29(.07–1.32);P=.09. | RR.29474;logCI.06562–1.32377;null/P agree;chi-square and logWald numericalP need not match. | PASS_1_COMPLETE |
| S264 | [p.19 eTable11 surgeryyes](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | Favorable12/41(29.3)/23/64(35.9);RR.81(.46–1.45);P=.48. | Crude/logRR/CI/null-P compatible. | PASS_1_COMPLETE |
| S265 | [p.19 eTable11 surgeryno](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | Favorable47/84(56.0)/59/120(49.2);RR1.14(.87–1.48);P=.34. | Subgroups sumprimary;RR/CI/null-P agree. | PASS_1_COMPLETE |
| S266 | [p.19 eTable11 surgeryinteraction](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | InteractionP=.27. | Logisticinteractioncoefficient/SEabsent;no conflictstated. | PASS_1_COMPLETE |
| S267 | [p.19 eTable11 massyes](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | Favorable12/41(29.3)/24/66(36.4);RR.80(.45–1.43);P=.45. | Crude/logRR/CI/null-P compatible. | PASS_1_COMPLETE |
| S268 | [p.19 eTable11 massno](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | Favorable47/84(56.0)/58/118(49.2);RR1.14(.87–1.48);P=.34. | Subgroups sumprimary;RR/CI/null-P agree. | PASS_1_COMPLETE |
| S269 | [p.19 eTable11 massinteraction](../../../joi180132supp2_prod.pdf#page=19), REPORT,AT | InteractionP=.25. | Logisticinteractioncoefficient/SEabsent;no conflictstated. | PASS_1_COMPLETE |
| S270 | [p.20 ATsensitivitymethods](../../../joi180132supp2_prod.pdf#page=20), REPORT | Majorityfirst72h;AUCdegree×hoursbelow35°C,trapezoidignoringmissing;HnoncomplianttoN,NrescuecomplianttoH. | SameexplicitAUCdefinitionasS234;localcutoffunprinted;no independentcontradiction. | PASS_1_COMPLETE |
| S271 | [p.20 eFigure7](../../../joi180132supp2_prod.pdf#page=20), REPORT | SameinitialflowasS239;1N→H,39H→N;missing8H/12N;primary121H/188N. | H217−50−39+1−8=121;N201−4−35−1+39−12=188. | PASS_1_COMPLETE |
| S272 | [p.20 sensitivityprimary](../../../joi180132supp2_prod.pdf#page=20), REPORT | Favorable56/121(46.3)/85/188(45.2);unadjustedRR1.02(.80–1.31);P=.85. | CrudeRR1.02363;logCI/chi-square/nullP compatible. | PASS_1_COMPLETE |
| S273 | [p.21 missingnessmethods](../../../joi180132supp2_prod.pdf#page=21), REPORT | Missing34/500(6.8)=20/260(7.7)H+14/240(5.8)N;worstHbad/Ngood,bestHgood/Nbad;MARpredictivemeanmatchingallbaseline/discharge,11datasets. | Missingcounts/percentagesreconcile;worst117H/125N,best137H/111Nfollowobserved117H/111N. | PASS_1_COMPLETE |
| S274 | [p.21 eTable12 worstH](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | 117/260;45.0%(38.8–51.2). | Ordered/contained;binomialnormaldiagnostic45±6.047percentagepointscompatible. | PASS_1_COMPLETE |
| S275 | [p.21 eTable12 worstN](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | 125/240;52.1%(45.6–58.5). | Ordered/contained;normalproportionCIreproducesdisplay. | PASS_1_COMPLETE |
| S276 | [p.21 eTable12 worstRR](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | RR.86(.72–1.04),sharedP=.11. | CrudeRR.864;logCI/null-Pagree. | PASS_1_COMPLETE |
| S277 | [p.21 eTable12 worstRD](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | RD−7.1(−15.8–1.7)percentagepoints,sharedP=.11. | Difference−7.0833;unpoolednormalCIreproduces;null/Pagree. | PASS_1_COMPLETE |
| S278 | [p.21 eTable12 worsttest](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | Unadjustedchi-squareequalproportionsP=.11. | Pooledtwo-armchi-squareapproximately2.51,P~.113;agreement. | PASS_1_COMPLETE |
| S279 | [p.21 eTable12 bestH](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | 137/260;52.7%(46.5–58.9). | Ordered/contained;proportionnormalCIreproduces. | PASS_1_COMPLETE |
| S280 | [p.21 eTable12 bestN](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | 111/240;46.3%(39.8–52.7). | Ordered/contained;proportionnormalCIreproduces. | PASS_1_COMPLETE |
| S281 | [p.21 eTable12 bestRR](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | RR1.14(.95–1.36),sharedP=.15. | CrudeRR1.1393;logCI/null-Pagree. | PASS_1_COMPLETE |
| S282 | [p.21 eTable12 bestRD](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | RD6.4(−2.3–15.2)percentagepoints,sharedP=.15. | Difference6.4423;unpoolednormalCIreproduces;null/Pagree. | PASS_1_COMPLETE |
| S283 | [p.21 eTable12 besttest](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | Unadjustedchi-squareequalproportionsP=.15. | Pooledchi-squareapproximately2.07,P~.150;agreement. | PASS_1_COMPLETE |
| S284 | [p.21 eTable12 MIH](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | 133/260;51.1%(45.1–57.2). | Count-derived51.1538;precisiongapbelow5%;CIcontainsestimate;imputationaveraging/roundingnotdefined. | PASS_1_COMPLETE |
| S285 | [p.21 eTable12 MIN](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | 121/240;50.4%(44.1–56.7). | Countpercent/orderedCIcontained;pooledimputationintervalinputsnotavailable. | PASS_1_COMPLETE |
| S286 | [p.21 eTable12 MIRR](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | StratifiedRR1.00(.95–1.06),sharedP=.88. | Ordered/contained/null-Pcompatible;distinctCMHmethodexplicit,so crudeRR/CIisdiagnostic-only;strata/poolinginputsabsent. | PASS_1_COMPLETE |
| S287 | [p.21 eTable12 MIRD](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | RD.7(−8.0–9.5)percentagepoints,sharedP=.88;Miettinen–Nurminenstratumscorelimits. | Ordered/contained/null-Pcompatible;inputsforstratifiedCI/MIpoolingabsent;notreplacedwithcrudeanalysis. | PASS_1_COMPLETE |
| S288 | [p.21 eTable12 MItest](../../../joi180132supp2_prod.pdf#page=21), REPORT,ITT | CMHstratifiedproportionsP=.88. | Specificstrata/MIpoolingnotprinted;no incompatibletestdecision;unreporteddefinitionnotafindingalone. | PASS_1_COMPLETE |
| S289 | [p.22 adequatecoolingmethod](../../../joi180132supp2_prod.pdf#page=22), REPORT | EvaluableHadequate>48hvscontrols;categoricalchi-square,normalt-test,otherwiseWilcoxon;hierarchicmultivariablelogisticadjustmentforimbalance,location/site randomeffects;OR95%CI. | Internallycoherentstatedmethod;baseline-and-outcomepopulation124H/226Nmatchesp.23. | PASS_1_COMPLETE |
| S290 | [p.22 injurytorandomizationmeanstest](../../../joi180132supp2_prod.pdf#page=22), REPORT | H1.73(.78)h,N2.00(1.04)h;P=.01;Naverage16minlater. | Difference.27h=16.2min;poolednormaldiagnosticcompatible;mean/t-testdiffersfromp.23median/ranktest(.02). | PASS_1_COMPLETE |
| S291 | [p.22 adequatecoolingunadjustedOR](../../../joi180132supp2_prod.pdf#page=22), REPORT | Favorable58/124(46.8)/111/226(49.1);OR.91(.59–1.41);P=.68;no significantdifference. | CrudeOR=(58×115)/(66×111)=.91046;logORCIreproduces;null/P/conclusionagree. | PASS_1_COMPLETE |
| S292 | [p.22 adequatecoolingadjustedOR](../../../joi180132supp2_prod.pdf#page=22), REPORT | AdjustedfortimetorandomizationOR.95;literalCItext(.55–275 1.64);P=.84;underlyingresultdidnotchange. | Sourcevisuallyconfirmsinsertednumeric275;F-ST1-102. Ifendpoints.55/1.64areintended,ordered/contained/null-Pagree,butnotnormalized. | PASS_1_COMPLETE |
| S293 | [p.23 eTable13 sex](../../../joi180132supp2_prod.pdf#page=23), REPORT,124H/226N | Men100(80.6)/180(79.6);women24(19.4)/46(20.4);sharedP=.82. | Armcounts/percentages/chi-squarecompatible. | PASS_1_COMPLETE |
| S294 | [p.23 eTable13 age](../../../joi180132supp2_prod.pdf#page=23), REPORT | Mean(SD)34.7(12.7)/34.3(13.6)y;P=.78. | Roundednormal/t-testdiagnosticcompatible. | PASS_1_COMPLETE |
| S295 | [p.23 eTable13 GCSoverall](../../../joi180132supp2_prod.pdf#page=23), REPORT | Median(IQR)5(4–7)/6(4–7);P=.39. | Ordered/contained;ranksunavailable. | PASS_1_COMPLETE |
| S296 | [p.23 eTable13 GCSmotor](../../../joi180132supp2_prod.pdf#page=23), REPORT | 3(1–4)/3(2–5);P=.43. | Ordered/contained;ranksunavailable. | PASS_1_COMPLETE |
| S297 | [p.23 eTable13 pupils](../../../joi180132supp2_prod.pdf#page=23), REPORT | 106/124(85.5)/188/226(83.2);P=.58. | Countpercent/chi-squaredecisioncompatible. | PASS_1_COMPLETE |
| S298 | [p.23 eTable13 hypotension](../../../joi180132supp2_prod.pdf#page=23), REPORT | 10/123(8.1)/27/225(12);P=.26. | Explicitrowdenominators;percent/testcompatible. | PASS_1_COMPLETE |
| S299 | [p.23 eTable13 hypoxia](../../../joi180132supp2_prod.pdf#page=23), REPORT | 17/121(14)/34/223(15.2);P=.77. | Explicitrowdenominators;percent/testcompatible. | PASS_1_COMPLETE |
| S300 | [p.23 eTable13 temperature](../../../joi180132supp2_prod.pdf#page=23), REPORT | Mean(SD)35.9(1.1)/35.9(1.0)°C;scene75H/136N;P=.86. | RoundedmeaninputspermitP;exactunroundedvaluesabsent. | PASS_1_COMPLETE |
| S301 | [p.23 eTable13 CT](../../../joi180132supp2_prod.pdf#page=23), REPORT | I2(1.6)/14(6.2),II67(54)/121(53.5),III/IV14(11.3)/20(8.8),V41(33.1)/68(30.1),VI0(0)/3(1.3);sharedP=.28. | Totals124/226;oneomnibuschi-square;no decisionconflict. | PASS_1_COMPLETE |
| S302 | [p.23 eTable13 IMPACT](../../../joi180132supp2_prod.pdf#page=23), REPORT | Unfavorable-probabilitymean(SD).48(.23)/.47(.22);P=.54. | RoundingintervalinputspermitreportedP;notanobservedoutcomerisk. | PASS_1_COMPLETE |
| S303 | [p.23 eTable13 ISS](../../../joi180132supp2_prod.pdf#page=23), REPORT | Median(IQR)29(21–34.5)/29(21–35);P=.95. | Ordered/contained;ranksunavailable. | PASS_1_COMPLETE |
| S304 | [p.23 eTable13 injurycause](../../../joi180132supp2_prod.pdf#page=23), REPORT | Motor41(33.1)/82(36.3),motorcycle14(11.3)/17(7.5),bicycle11(8.9)/20(8.8),pedestrian14(11.3)/35(15.5),object12(9.7)/16(7.1),fall25(20.2)/50(22.1),other7(5.6)/6(2.7);sharedP=.51. | Categorytotals124/226;oneomnibuschi-square. | PASS_1_COMPLETE |
| S305 | [p.23 eTable13 ethanolpositive](../../../joi180132supp2_prod.pdf#page=23), REPORT | 48/105(45.7)/80/180(44.4);P=.84. | Countpercent/explicitdenominators/testcompatible. | PASS_1_COMPLETE |
| S306 | [p.23 eTable13 ethanol>51](../../../joi180132supp2_prod.pdf#page=23), REPORT | 35/105(33.3)/60/180(33.3);mg/dL;P=1.00. | Proportionsboth1/3exactly;testcompatible. | PASS_1_COMPLETE |
| S307 | [p.23 eTable13 injurytorandomization](../../../joi180132supp2_prod.pdf#page=23), REPORT | Median(IQR)1.6(1.0–2.5)/2.1(1.1–2.8)h;P=.02. | Ordered/contained;explicitWilcoxonfornonnormaldata;ranksunavailable;differentstatistic/testfromS290. | PASS_1_COMPLETE |

### plan first-pass records

| S ID | Exact roles/locations and mapper keys | Inferential/design relationship and printed specification | Pass 1 check/result | Pass 1 state |
|---|---|---|---|---|
| S401 | PLAN DOC-002 pp14,18,19,69,72; PA003,PA007,PA020,PB005,PB006,PB009 | Superiority hypothesis, favorable GOSE5–8 at6months; null equal favorable proportions | Direction/primary threshold/time/status coherent across versions and REPORT pp1,3; no NI/equivalence margin. | PASS_1_COMPLETE |
| S402 | PLAN pp15,19,40–45,72,103–105; PA007,PA036,PA062–066,PB009,PC042–044 | GOSE1 death through8 upper good recovery; favorable5–8, unfavorable1–4 | Ordered scale and dichotomy coherent; questionnaire severity boundaries agree. | PASS_1_COMPLETE |
| S403 | PLAN pp15,19,28,72,84; PA008,PA046,PA050,PB011,PC006,PC010 | Ordinal GOSE proportional-odds secondary analysis; partial model allowed finalversion | REPORT p4 ordinal-logistic analysis and score-test assumption assessment compatible; no PO assumption inferred beyond printed text. | PASS_1_COMPLETE |
| S404 | PLAN pp15,19,28,72; PA009,PA051,PB012 | Sliding dichotomy secondary outcome, tertiles of baseline prognostic risk | REPORT p3 expressly not reported here. No supplied key-secondary designation; omitted cutpoints cannot generate a stand-alone method finding. | PASS_1_COMPLETE |
| S405 | PLAN pp15,19,46–49,72–73,106–107,140; PA010,PA067–069,PB013,PC045–046,PD004 | QOL original EQ5D/AQOL8, final EQ5D/SF12 | AQOL→SF12 disclosed amendment; REPORT p3 QOL not reported here. No current-version conflict. Utility scoring absent, no reported conflicting value. | PASS_1_COMPLETE |
| S406 | PLAN pp15,19,28,73,84; PA011,PA048,PB014,PC013 | Survivor favorable GOSE secondary; final SACE among would-survive-either-arm population | Distinguish SACE from observed survivor proportion. No SACE estimate supplied in this shard; ordinary secondary omission alone does not meet key-secondary threshold. | PASS_1_COMPLETE |
| S407 | PLAN pp15,19,73,84; PA012,PB015,PC011 | Six-month all-cause mortality secondary, unadjusted RR/RD in final binomial models | Outcome/time/role agree REPORT p3. Final numeric compatibility assigned other shards. | PASS_1_COMPLETE |
| S408 | PLAN pp15,19,73,84; PA013,PB015,PC011 | Hospital-discharge all-cause mortality secondary | REPORT p3 agrees; distinguish hospital denominator from6mo. | PASS_1_COMPLETE |
| S409 | PLAN pp15,19,144; PA014,PD007 | Original ICU-discharge mortality secondary removed V2→3 | Explicit deletion reconciles its absence from final secondary list and REPORT. | PASS_1_COMPLETE |
| S410 | PLAN pp15,19,73,85–86; PA015,PA053–054,PB016,PC018,PC021 | Adverse events bleeding/infection secondary; SAE window commencement→7d after cessation | Distinguish AE endpoint from SAE reporting window; REPORT10d adverse-event window is not automatically contradicted by different SAE window. | PASS_1_COMPLETE |
| S411 | PLAN pp73,85,140,144,149,153; PB016,PC014,PD004,PD010,PD018 | Health economic evaluation, payer cost/favorable GOSE and QALY, EQ5D-3L six months | Added outcome disclosed; not reported here per REPORT p3; separate economic publication scope. | PASS_1_COMPLETE |
| S412 | PLAN pp73,144; PB017,PD008; REPORT p4 | Time-to33°C relation with dichotomized GOSE in cooled arm described as interaction; REPORT unadjustedchi-square association | Within-arm wording lacks a second factor; intended outcome association evident, so wording alone does not establish replaced analysis. | PASS_1_COMPLETE |
| S413 | PLAN pp73,85,144; PB018,PC015,PD008; REPORT p4 | Treatment×evacuated mass-lesion interaction; MarshallV andV/VI subgroups | REPORT logistic treatment×subgroup interaction matches planned comparison; no named logistic covariance/test detail inferred. | PASS_1_COMPLETE |
| S414 | PLAN pp14,19,34,73–74,91–93,144–147,157; PA004–005,PB019–022,PC026–029,PD009,PD011,PD024 | Original≥15,<60; final≥18,<60; severe bluntTBI/GCS<9/intubation; window2→2.5→3h, BP100→90 | Version chronology and final repeated eligibility thresholds mapped; nonmatching older eligibility is not current conflict. Estimated age REPORT18–60 wording is operational shorthand, not numerical population contradiction. | PASS_1_COMPLETE |
| S415 | PLAN pp14–15,20–22,69,75–77,91–93,139,146–147; PA006,PA023,PB007–008,PB025,PB029,PD012 | Induction4°C saline up to2L; final1L afterintubation/2L before,100mL/min; initial35°C then33°C | REPORT p3 up-to2L is compatible with status-specific maximum; no dose discrepancy. | PASS_1_COMPLETE |
| S416 | PLAN pp15,21–22,69,77,97,99; PA026,PA029,PB007,PB034,PC034,PC037 | Final synopsis72h at33°C versus rewarming72h afterrandomization with latecooling48h minimum | Same-version time anchors/dose differ. F-ST1-201. | PASS_1_COMPLETE |
| S417 | PLAN pp21–22,77,100–101; PA025,PA029,PB035,PC038–039 | Postwarming normothermia hypothermiaarm up to7d versus96h postrandomization in final appendix | Same-version management duration differs; corroborating REPORT pp1,3 gives7d. F-ST1-202, relationships P_R,P_P. | PASS_1_COMPLETE |
| S418 | PLAN pp21–22,77,99–100,158–162; PA029,PB034,PC037–038,PD025–031; REPORT p3 | Original0.25°C/h, final0.17°C/h; console0.5°C/3h, slowing0.2°C/2h; emergency clinician allowance | 0.5/3=.1667 coherent. REPORT 'target rate up to0.25' vsfinal recommended maximum.17 differs ~45%; F-ST1-203. | PASS_1_COMPLETE |
| S419 | PLAN pp21,76–77,92,139,147; PA027–028,PB026–027,PB032–033,PC028,PD001–002,PD014 | Temporarybleeding hold35–37°C, restart≤48h; interventionwithdrawal retains follow-up | Original60h/revised48h and ceased-treatment/withdrawn-data distinctions disclosed; REPORT p3 bleeding exceptions coherent. | PASS_1_COMPLETE |
| S420 | PLAN pp22,78,96,139,142,160; PA030–031,PB036,PB038,PC033,PD006,PD028 | Control rescue35°C permitted finalversion; ordinary control37±.5 | Original norescue rule superseded; final control rescue compatible REPORT p3. No interpretation of rescue as randomized intervention. | PASS_1_COMPLETE |
| S421 | PLAN pp22,78,139,144,148; PA032,PB038,PD003,PD007,PD016 | Run-in2/site→6leadsite→4leadsite, nonrandomized; initial512includesrun-in, final500randomized | Amendments separate run-in from randomized total; REPORT p4 eightobservedrun-in is realized ratherthan planned-count conflict. | PASS_1_COMPLETE |
| S422 | PLAN pp22,78,148; PA033,PB039,PD017; REPORT pp2–3 | Blockenvelopes1:1; originalambulance/centre; finalregion×prehospital/EDstrata | Current randomization factors match REPORT; blocksize2/4 appears in REPORT and absent plan is no contradiction. | PASS_1_COMPLETE |
| S423 | PLAN pp22,25,78,81,90; PA031,PA036,PB037,PB042,PC025; REPORT pp2–3 | Blinded central trained GOSE telephoneassessment; cliniciansunblinded | Inferential ascertainment coherent; biomarker substudy clinicianprovidedGOSE cannot by itself alter parent ascertainment. | PASS_1_COMPLETE |
| S424 | PLAN pp25,81; PA034–037,PB041–042 | Death or6months postrandomization follow-up, endpoint6months postinjury; consent permission,interventionwithdrawal retainsITT | Randomization≤3h afterinjury makes six-month anchor wording immediately resolvable for this endpoint. Consent withdrawal distinct from missingoutcome and treatmentwithdrawal. | PASS_1_COMPLETE |
| S425 | PLAN pp84,174–175; PC007–008,PD038; REPORT pp3–4 | ModifiedITT excludes withdrawn-all-data consent AND noteligible/neverintervention; REPORT allrandomized exceptconsent | Disclosed plan amendment does not explain report primary population retaining the second class. F-ST1-204. | PASS_1_COMPLETE |
| S426 | PLAN pp25–28,81,84; PA037,PA047,PB042,PC007–008; REPORT p3 | Missingness no imputation reported; plan no parent imputation formula specified | No printed conflicting imputation specification; missing detail alone not finding. | PASS_1_COMPLETE |
| S427 | PLAN pp27,83; PA039–040,PB044; REPORT p3 | Baseline50%, target65%,30%RRI/15%ARI;364total/182arm80%two-sided power;REPORT82% | .65−.50=.15, .15/.50=.30; n depends exacttest/continuity. Normal diagnostics uncorrected≈339total,continuitycorrected≈364.80vs82 within5% display rule. | PASS_1_COMPLETE |
| S428 | PLAN pp27,83; PA039,PB044 | NNT7 forabsolute15% favorableincrease | 1/.15=6.667; integerNNT7 coherent. | PASS_1_COMPLETE |
| S429 | PLAN pp27,83; PA042,PB044 |5%longterm follow-up allowance364→384 |364/.95=383.158; round tobalanced384coherent; intervalprecision overlap. | PASS_1_COMPLETE |
| S430 | PLAN pp27,83–84; PA043,PB044,PC001 |12% interventionwithdrawal allowance8%+2%+2%;384→496 |8+2+2=12; diagnostic one-arm dilution factor1/.88² gives495.868, compatible496. Do not infer as authors' exactformula. | PASS_1_COMPLETE |
| S431 | PLAN pp27,83,150; PA044–045,PB044,PD019 |Single interim.3% adds2,target498;two interim.7% target500;original14run-in total512 |496+2=498;498+14=512; amendments500target coherent. Fractional inflation language smallrounding <5%; no count/denominator result conflict. | PASS_1_COMPLETE |
| S432 | PLAN pp28,84,150–151; PA046,PC006,PD020 |EightcategoryPO model lnOR=.62;182/arm96%one-sided poweralpha.05 |Full referencecategoryprobabilities notsupplied, cannot reproducePOpower; inferentialtwo-sided reporting can differfrompowerplanning. No source contradiction. | PASS_1_COMPLETE |
| S433 | PLAN pp28,84,151; PA052,PC002,PD021 |Single50%interim replacedby25%(125),50%(250) |Explicit amendment reconciles single/two-occasion schedules. Version3printed256 supersededbycurrent250. | PASS_1_COMPLETE |
| S434 | PLAN pp84–86,175,178–179; PC002–004,PC019–020,PD039,PD042;REPORTp2 |Extra safety occasions300,350,400,450;450uses28dmortality,otherstwo6moendpoints |Sixoccasions, five×two+one=11endpoint tests; 'ten of11...both' wording no independent count contradiction. | PASS_1_COMPLETE |
| S435 | PLAN pp84–86,152,188; PC019,PD022,PD054 |Noearly futilitystopping; DS MC safety discretion; fixed3SD boundary |No claim futilitystopping in REPORT; no clinicalpreference critique. | PASS_1_COMPLETE |
| S436 | PLAN pp84,188; PC004–005,PD054;REPORTp4 |Revisedfinalcritical±1.996/P=.0459,earliercharter1.975/.048;REPORTsignificanceP<.05 |Different schedule versions explaincriticalvalues; rounded alpha copyintervals [.04585,.04595] and [.045,.055] overlap. Borderline decision-rule applicability remains named limitation; no primary verdict changed. | PASS_1_COMPLETE |
| S437 | PLAN pp28,152,188; PA052,PD022,PD054 |Normal-binomial Haybittle–Peto|Z|≥3;charter'approximateP<.001' |Two-sidednormalP=.0026998 andone-sided=.0013499; printedPthreshold/testrule conflict. F-ST1-205. | PASS_1_COMPLETE |
| S438 | PLAN pp84,188; PC005,PD054;REPORTp4 |Two-sided95%CI;nomultiplicity adjustment beyondinterim spending;secondaryexploratoryinterpretation |REPORT retains secondaryoutcome labels; exploratoryinterpretation warning does notitself changeprespecifiedoutcome status. | PASS_1_COMPLETE |
| S439 | PLAN p84; PC004 |Eastapproximatechi-square82.3%(down83),366fullyevaluable,11interimtests,4%−.7%=3.3%extra |4−.7=3.3; engine/designfile notsupplied; noexactreproduction asserted. 82.3vs83smallcompatible reportingprecision. | PASS_1_COMPLETE |
| S440 | PLAN p180; PD044;REPORTp3 |August2017target500→510;withdrawconsent2.5vexpected2%,loss7v5% |Explicitblindedextension reconciles final510 versus500plan; not a numerical guarantee toattainexactpower. | PASS_1_COMPLETE |
| S441 | PLAN pp28,84; PA048,PC009;REPORTp3 |OriginalMH/logisticcovariate analyses;finalunadjustedbinomialRR/RD/OR |Finalversion replaces originalmethods; REPORTχ²equalproportionscompatible unadjustedbinomialtests. Primary ORreporting omitted ordinaryadditionalmeasure,not key outcome omission. | PASS_1_COMPLETE |
| S442 | PLAN p84; PC011;REPORTp3 |Log-binomialRR/identity-binomialRDsecondarybinarymodels;REPORTχ²tests |Effect-model estimation and hypothesisχ²testingcan coexist; no independently conflicting value assumed here. | PASS_1_COMPLETE |
| S443 | PLAN pp28,84–85; PA049,PC013,PC016;REPORTp4 |KM/logrank,unadjusted/adjustedCoxHR;covariate sensitivity |Unadjustedreported survival matches permittedmethod; adjustedsecondaryresult omission lackskeysecondarydesignation. | PASS_1_COMPLETE |
| S444 | PLAN p85; PC016;REPORTpp3–4 |Primary/secondaryadjustments prespecifiedbaselinecovariates+substantialimbalances;extendedIMPACTTBI,strata random effects |SuppliedfullpublishedSAP absent; no assumption itscovariatelist excludesIMPACT. Broadfinalcovariateplancompatible statedseverityadjustment. | PASS_1_COMPLETE |
| S445 | PLAN pp84–85,178–179; PC007,PC017,PD043;REPORTp3 |ITT assignment-effect versusCACEcooling-effect,exploratorysecondarywithbinary/continuouscompliance |Distinctestimands coherent;CACEexpresslynotreportedhere. No missingkeysecondaryclaim. | PASS_1_COMPLETE |
| S446 | PLAN p85; PC017;PLANp183 |OriginalPPcooledcompliantversusallcontrols;Juneupdate excludesineligibleandcrossingcontrols |LaterSAPupdateexplicitlyaddsclinicallyrelevantdoseanalyses; scoped versionchangecoherent. | PASS_1_COMPLETE |
| S447 | PLAN pp181–182,186; PD045 |Publishedprotocol/SAPexternalpointer;actualupdatesonlylocallysupplied |No externalSAPmethod assumed; pointerunitscoveredwith no directstatisticalcontent. | PASS_1_COMPLETE |
| S448 | PLAN pp183,184,187; PD046–053;REPORTp4 |June12/13updatesbeforelock/unblinding;time-injury-to35/33;doseversusdepthsensitivities |Prespecificationchronologystated; no contradictory unblindingdate supplied. | PASS_1_COMPLETE |
| S449 | PLAN p183; PD047;REPORTp4 |Retrospective severeTBI,excludeallunmetinclusion/presentexclusions inPP/as-treated |Populationdefinition matches REPORT; differentialexplicit earlywithdrawalbranches preserved,publishedSAPcontextnot supplied. | PASS_1_COMPLETE |
| S450 | PLAN pp183,184,187; PD048,PD051,PD053;REPORTp4 |Compliance>48h≤35°C within96h;PPsurvivorsnoncompliantremoved;earlydeathknowncompliant/undeterminedincluded |Text/June13diagram agree with earlydeath exception; REPORTcondenseddefinition omitsdetailbutdoesnotprintconflictingdeathhandling. | PASS_1_COMPLETE |
| S451 | PLAN pp183,184,187; PD049,PD052,PD053;REPORTp4 |As-treatedcompliershypothermia,noncompliersstandard;earlydeathnoncompliantassignmentcrosses |Directp187hypothermia→standarddeathline'<48h',notmapper'>48'; allcurrentrowsreconcile. | PASS_1_COMPLETE |
| S452 | PLAN pp183,187; PD048–049,PD053 |Exactly48h boundary:prose>48compliance,diagram<48removal,>48controlcrossing |Equalityhandling unreportedand likelycontinuousdurationrounding; missingboundarydetailalone no printed resultconflict. | PASS_1_COMPLETE |
| S453 | PLAN pp184,187; PD052–053;REPORTpp3–4 |SensitivityoutcomeadjustmentonlyextendedIMPACT-TBI;generalhierarchicstrata random effects |REPORTgeneraladjustmentdescription may concernITT; exactPP/as-treatedfittedmodelnotprinted; no inferentialmodelconflict assertedbyconvention. | PASS_1_COMPLETE |
| S454 | PLAN pp184,187; PD051–053 |Plannedflow511randomized,armXXX/XX/Xplaceholders |Explicitplannedplaceholdersare notobservedcounts/testresults. | PASS_1_COMPLETE |
| S455 | PLAN pp139–153,157–162,174–179; PD001–043 |AmendmentchainV1→2→3→4→5→6→7→8→9;version8dated2016vsadoptionfile2015 |Administrativeheaderdatevariationdoesnotchangeanalysisdecisionrule;no finding. | PASS_1_COMPLETE |
| S456 | PLAN pp189–190; PD055 |DSMBDec2015codedX/Y,GOSE273(7refused,20lost),140/133;noidentifiedindividualrowtest |Endpointmonitoringfits300recruitassessment; sourcecontainsnoCI,SE, testname orarmlabel. Numericalrowchecks assignedotherstatisticalshards. | PASS_1_COMPLETE |
| S457 | PLAN pp191–192; PD056 |July2016GOSE321,7refused,22missing;20knownsurvivors,mortality341 |GOSEversusmortalitypopulations explicitlydifferent;noequaldenominatorassumption. Numericalrowchecks otherstatisticalshards. | PASS_1_COMPLETE |
| S458 | PLAN pp193–194; PD057–058 |May2017GOSE364,8refused,28missing;26survivors,mortality390 |Outcomecomplete-caseversusknownsurvival cohorts explicitlydifferent;Ptestdetailsabsent. Countandindividualtestchecks separate shard. | PASS_1_COMPLETE |
| S459 | PLAN pp189–194; PD055–058 |Cumulativechartsblockeventcounts;monitoringuses6moendpointsexcept450 |Chartsnotratesorfinaleffectestimates;nofinalbetween-armtreatmentidentityimputed. No suppliedmonitoringPpasses3SDthreshold. | PASS_1_COMPLETE |
| S460 | PLAN pp16–17,23,27,70–71,79,112–113,119,121,128,163–164; PA016–019,PA041,PB045–047,PC054 |Historicalmeta-analysis/citedcohortRRs,Pvalues andnare priorrationale |SeparatefromcurrentPOLARresults; historicaldisplaysmappedand screenedscopewise. PriorRR.76CI.05–1.05P.18 lacksnamedCI/Pmethod; noassumedlogWaldfinding. | PASS_1_COMPLETE |
| S461 | PLAN pp108–109; PC047–050 |RenalAKIallPOLAR,RIFLERisk/Injury/Failure;urine7d,creatinine10d;severitybaseline→worst10d |7ddescriptionalongside10dcontinuedcollectionmakespurposeclear;substudydoesnotproduceparentreportedprimaryresult. | PASS_1_COMPLETE |
| S462 | PLAN p108; PC048 |Renalcontinuous250/arm,.25SD,80%,two-sided.05;SD24%,difference6% |Normaldiagnosticn≈251.164/arm;balanced250gives≈79.9%;.25×24%=6%coherentwithinprecision. | PASS_1_COMPLETE |
| S463 | PLAN p108; PC048 |RenalbinaryAKI9%vs3%,absolute6%,250/arm,approx80%power |Normaldiagnostic≈245armuncorrected;continuitycorrectionalters;claimedapprox80%coherent.Noexactsoftwareassumption. | PASS_1_COMPLETE |
| S464 | PLAN pp108–109; PC049–050 |RenalprimaryeGFR/creatinineseverity;secondarycumulativeRIFLEandAKIfreedays;logistic/multiplelinear/Cox |Methodsallowedbyoutcometype;no reportednumberrequiresalternativeanalysis. | PASS_1_COMPLETE |
| S465 | PLAN pp109–110; PC051–053 |Renalbiomarkerfirst50,baseline/24/48/72hsamples,treatment×time repeated-measuresANOVA |Repeatstructureexplicit;within-personcovariance unspecifiedbutno conflict/reportednumber. | PASS_1_COMPLETE |
| S466 | PLAN p109; PC052 |Renalbiomarkerr=.4,n50,80%two-sided.05;25/arm,.8SD |Fisherzdiagnosticn≈46.8;two-meandiagnosticn≈24.53/arm;integer50/25compatible. Spearman/Pearsonnotassumed. | PASS_1_COMPLETE |
| S467 | PLAN p110; PC053 |Logisticrelations/AUCamongbiomarkers,creatinine/eGFR/RIFLE/survival |Continuousoutcomeconversiondefinitionsunreported;separateunreportedsubstudywithoutparentreportedstatistic.Specificgapnotmainreportfinding. | PASS_1_COMPLETE |
| S468 | PLAN pp114–117; PC055–060 |Energysubstudyprimarymeanenergyfirst72h;secondaryfirst7d/rewarming/fever>39°C;40consecutivetwosites |Separateoutcomehierarchy,notparentGOSE. Repeatedmeasurements twice/daythrough7thenalternateuntildeath/extubation/discharge mapped. | PASS_1_COMPLETE |
| S469 | PLAN p118; PC061 |Energy2000caloriesSD400,difference400;16/arm80%two-sided.05,20%noncompletion20/arm |Normaldiagnosticn15.6978/arm;16/(1−.20)=20coherent. Exactsmall-sampletestnot supplied,so no assumedt-powerconflict. | PASS_1_COMPLETE |
| S470 | PLAN p118; PC061 |Energyappropriate normal/nonparametriccomparisons;50%monitoring |No exact fittedmodel/repeatcovariance suppliedandno parentresultusingit. Methoddetailabsencealone nofinding. | PASS_1_COMPLETE |
| S471 | PLAN pp119–120; PC062–065 |Neurologicalbiomarker80=40/arm;dailyblood5d;GOSE6mo;Spearman.4542planningr.45power>80% |Fisherzdiagnosticn≈36.4forr.45;40compatible,not an exactSpearmanpowerassertion. | PASS_1_COMPLETE |
| S472 | PLAN p119; PC064 |Neurologicalbiomarkermultiplelinearregressionandtwo-wayANOVA;clinicianprovidedGOSE |Within-subjectcovarianceandoutsidescoretransferunreported;no reportedparentstatisticproducedbythismodel. | PASS_1_COMPLETE |
| S473 | PLAN pp122–126,164–170; PC067–072,PD032–037 |TEGobservational20POLAR+20nonPOLAR;primarybetweencohorts,secondarypaired33/37°C |Notindependentsamplestestappliedtopaireddata:patientrandomeffectexplicitinmixedmodel. | PASS_1_COMPLETE |
| S474 | PLAN pp124,167–168; PC069–070,PD035 |TEGsample148–72h,sample2120±12h;table'48and72hrs' |Tablecaptionversuswindowwordingimmediatelyresolvedbymeasurementprose;nochangedcurrentresulttimepoint. | PASS_1_COMPLETE |
| S475 | PLAN pp123–126,166–170; PC068–072,PD034–037 |TEG R/alpha/MA/A30,humanpairedtemperatureassays;normality/logtransform,mixedpatienteffects,.05two-sided |Design/repeatmethodlogical;instrumentunitsaredefinitions,nopatientestimatecontradiction. | PASS_1_COMPLETE |
| S476 | PLAN pp128–132; PC073–082 |Propofolobservationalpaired10,34–35vs36.5–38;continuousinfusionpriorstableconcentration |SeparatePKsubstudy,not mainGOSE;clinicalinterruptioncriteria mapped,steady-state assumption statedratherthanimputed. | PASS_1_COMPLETE |
| S477 | PLAN pp130–131; PC077–079 |Propofolcease<35°C;sampleprestopthen5/10/15/30/60min;occasionB'passivelyrewarm' |Separateappendixpassivewordingcontrastsparentno-passiveguideline;no evidenceparentreportedprotocolusedthissubstudydescription. Peripheral. | PASS_1_COMPLETE |
| S478 | PLAN p132; PC081 |CLtotL/h=dosemg/h dividedCSSmg/L |Dimensionalandformulaidentitycoherent. Statedsteady-stateassumptionnotcritique. | PASS_1_COMPLETE |
| S479 | PLAN p132; PC081 |AUCtrapezoids+lastconcentration multipliedterminalslope |Ifslopeis1/h,productunitsmg/(Lh)vsAUCmgh/L;reciprocal-slopeormeanlifedefinitionnotgiven. SeparateunreportedPKsubstudydoesnotaffectparentreportedanalysis; excludedPERIPHERAL_COMPARISON. | PASS_1_COMPLETE |
| S480 | PLAN p132; PC080–082 |NONMEMbetween/withinvariation;pairedt/Wilcoxonsignedrank/McNemarwhenassumptionsmet |Pairedcoherentchoices;modeldetailnotassumed. | PASS_1_COMPLETE |
| S481 | PLAN pp32–39,89–102,141–142,158–162; PA056–061,PC024–041,PD005–006,PD025–031 |SharedphysiologicalmonitoringandICPtreatmentthreshold20/CPP60;temporalseveritytriggers |Co-interventionquantitiesmapped;notinferentialparentanalysisunlessspecificdisplayconflict. No preferredclinicalalgorithm proposed. | PASS_1_COMPLETE |
| S482 | PLAN pp1–12,29–31,50–52,53–68,79–80,82–83,87–88,111,127,133–138,143,154–156,171–173,177,181–182,185–186 |Covers/admin/contents/bibliographies/blankpages/externalpointers withnocurrentinferentialrelationship |Completepageaccountingviafourmaps. Page127blankandscannedadminpagesexplicitlyinspectedbymappers; no gap or inventedstatistic. | PASS_1_COMPLETE |

### monitoring first-pass records

| S ID | PLAN location | Printed relationship | Pass-1 check and outcome | Pass 1 |
|---|---|---|---|---|
| S601 | p189, GOSE=1 | X27/140 (19%); Y27/133 (20%); P=.83 | Percentages reconcile; death direction retained; no interval/test conflict printed. | PASS_1_COMPLETE |
| S602 | p189, GOSE=2 | X1/140 (1%); Y2/133 (2%); P=.61 | Percentages reconcile with display intervals; sparse counts do not establish the exact test. | PASS_1_COMPLETE |
| S603 | p189, GOSE=3 | X25/140 (18%); Y28/133 (21%); P=.5 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S604 | p189, GOSE=4 | X10/140 (7%); Y12/133 (9%); P=.57 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S605 | p189, GOSE=5 | X32/140 (23%); Y30/133 (23%); P=.95 | Percentages reconcile; near-equal displayed proportions do not require an identical P value to other rows. | PASS_1_COMPLETE |
| S606 | p189, GOSE=6 | X15/140 (11%); Y17/133 (13%); P=.6 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S607 | p189, GOSE=7 | X19/140 (14%); Y9/133 (7%); P=.06 | Percentages reconcile; P is nonsignificant and no interval implies otherwise. | PASS_1_COMPLETE |
| S608 | p189, GOSE=8 | X11/140 (8%); Y8/133 (6%); P=.55 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S609 | p189, GOSE score | X4.39 (2.23); Y4.08 (2.11); P=.23 | Frequency-weighted means 4.392857/4.075188 reproduce. Diagnostic sample SDs 2.227030/2.105635 reproduce parenthesized values; dispersion definition absent. | PASS_1_COMPLETE |
| S610 | p189, unfavourable GOSE1–4 | X63/140 (45%); Y69/133 (52%); P=.26 | Category sums 63/69 and percentages reconcile; chart sums match. | PASS_1_COMPLETE |
| S611 | p189, unfavourable survival GOSE2–4 | X36/140 (26%); Y42/133 (32%); P=.28 | Counts equal unfavourable totals less deaths; percentages use all GOSE participants, consistent with displayed values. | PASS_1_COMPLETE |
| S612 | p189, header and group headings | Outcome273; consent refusals7; lost20; X140/Y133; 12 blocks ending300 | 140+133=273 and 273+7+20=300. Mortality/unfavourable block denominators each sum140/133. | PASS_1_COMPLETE |
| S ID | PLAN location/block | M pairs X; Y | U pairs X; Y | Pass 1 |
|---|---|---|---|---|
| S613 | pp189–190, 0–25 | 1/11; 3/13 | 1/11; 6/13 | PASS_1_COMPLETE |
| S614 | pp189–190, 26–50 | 4/14; 0/8 | 6/14; 6/8 | PASS_1_COMPLETE |
| S615 | pp189–190, 51–75 | 3/6; 0/16 | 4/6; 5/16 | PASS_1_COMPLETE |
| S616 | pp189–190, 76–100 | 3/14; 2/10 | 7/14; 5/10 | PASS_1_COMPLETE |
| S617 | pp189–190, 101–125 | 1/13; 1/10 | 4/13; 2/10 | PASS_1_COMPLETE |
| S618 | pp189–190, 126–150 | 1/11; 2/12 | 6/11; 6/12 | PASS_1_COMPLETE |
| S619 | pp189–190, 151–175 | 2/14; 2/8 | 5/14; 5/8 | PASS_1_COMPLETE |
| S620 | pp189–190, 176–200 | 2/11; 3/12 | 4/11; 7/12 | PASS_1_COMPLETE |
| S621 | pp189–190, 201–225 | 2/9; 4/14 | 5/9; 8/14 | PASS_1_COMPLETE |
| S622 | pp189–190, 226–250 | 1/10; 4/12 | 6/10; 7/12 | PASS_1_COMPLETE |
| S623 | pp189–190, 251–275 | 5/14; 4/9 | 11/14; 7/9 | PASS_1_COMPLETE |
| S624 | pp189–190, 276–300 | 2/13; 2/9 | 4/13; 5/9 | PASS_1_COMPLETE |
| S625 | pp189–190, cumulative plots and table | M cumulative X1,5,8,11,12,13,15,17,19,20,25,27; Y3,3,3,5,6,8,10,13,17,21,25,27 | U cumulative X1,7,11,18,22,28,33,37,42,48,59,63; Y6,12,17,22,24,30,35,42,50,57,64,69. Both figures agree with these sums, table outcomes, axes and coding. | PASS_1_COMPLETE |
| S ID | PLAN location | Printed relationship | Pass-1 check and outcome | Pass 1 |
|---|---|---|---|---|
| S626 | p191, GOSE=1 | X34 (20%); Y32 (21%); P=.88 | GOSE denominators168/153 from complete category sums; percentages reconcile. | PASS_1_COMPLETE |
| S627 | p191, GOSE=2 | X1 (1%); Y2 (1%); P=.61 | Percentages reconcile; exact test undefined. | PASS_1_COMPLETE |
| S628 | p191, GOSE=3 | X33 (20%); Y30 (20%); P=.99 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S629 | p191, GOSE=4 | X14 (8%); Y16 (10%); P=.51 | Percentages reconcile including Y10.4575% within 10±.5 display interval. | PASS_1_COMPLETE |
| S630 | p191, GOSE=5 | X36 (21%); Y32 (21%); P=.91 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S631 | p191, GOSE=6 | X16 (10%); Y20 (13%); P=.31 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S632 | p191, GOSE=7 | X22 (13%); Y11 (7%); P=.08 | Percentages reconcile; no interval implying significance supplied. | PASS_1_COMPLETE |
| S633 | p191, GOSE=8 | X12 (7%); Y10 (7%); P=.83 | Percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S634 | p191, GOSE score | X4.27 (2.22); Y4.10 (2.14); P=.49 | Weighted means4.267857/4.098039 reproduce; diagnostic sample SDs2.217171/2.139124 reproduce. | PASS_1_COMPLETE |
| S635 | p191, unfavourable GOSE1–4 | X82 (49%); Y80 (52%); P=.53 | Category sums and percentages reconcile; no reported interval/test conflict. | PASS_1_COMPLETE |
| S636 | p191, favourable GOSE5–8 | X86 (51%); Y73 (48%); P=.53 | Category sums/percentages reconcile; same P for complementary binary outcomes coherent; p192 block counts sum86/73. | PASS_1_COMPLETE |
| S637 | p191, unfavourable survival | X48 (29%); Y48 (31%); P=.58 | 82−34=48 and80−32=48; all-GOSE percentages reconcile; no inferential contradiction supplied. | PASS_1_COMPLETE |
| S638 | p191, 180 mortality | X34 (19%); Y32 (20%); P=.78 | Mortality denominators181/160 from block sums;34/181=18.7845%,32/160=20%; distinct GOSE versus survival denominators explicitly disclosed. | PASS_1_COMPLETE |
| S639 | p191, header/footnote |350 enrolled;321 GOSE;7 refusals;22 missing;20/22 missing GOSE known survivors; survival341 |321+7+22=350;321+20=341; GOSE168+153=321; survival181+160=341. Additional13 X and7 Y survivors yield no added deaths. | PASS_1_COMPLETE |
| S ID | PLAN location/block | M pairs X; Y | F pairs X; Y | Pass 1 |
|---|---|---|---|---|
| S640 | pp191–192, 0–25 |1/12;3/13|10/11;7/13| PASS_1_COMPLETE |
| S641 | pp191–192, 26–50 |4/14;0/10|8/14;2/8| PASS_1_COMPLETE |
| S642 | pp191–192, 51–75 |3/8;0/16|2/6;11/16| PASS_1_COMPLETE |
| S643 | pp191–192, 76–100 |3/15;2/10|7/14;5/10| PASS_1_COMPLETE |
| S644 | pp191–192, 101–125 |1/14;1/11|9/13;8/10| PASS_1_COMPLETE |
| S645 | pp191–192, 126–150 |1/12;2/12|5/11;6/12| PASS_1_COMPLETE |
| S646 | pp191–192, 151–175 |2/16;2/8|9/14;3/8| PASS_1_COMPLETE |
| S647 | pp191–192, 176–200 |2/12;3/13|7/11;5/12| PASS_1_COMPLETE |
| S648 | pp191–192, 201–225 |2/11;4/14|5/10;6/14| PASS_1_COMPLETE |
| S649 | pp191–192, 226–250 |1/11;4/13|4/10;5/12| PASS_1_COMPLETE |
| S650 | pp191–192, 251–275 |5/14;4/9|3/14;2/9| PASS_1_COMPLETE |
| S651 | pp191–192, 276–300 |2/14;2/10|9/14;4/9| PASS_1_COMPLETE |
| S652 | pp191–192, 301–325 |2/12;4/12|3/10;3/11| PASS_1_COMPLETE |
| S653 | pp191–192, 326–350 |5/16;1/9|5/16;6/9| PASS_1_COMPLETE |
| S654 | pp191–192, cumulative plots/table |Mortality X1,5,8,11,12,13,15,17,19,20,25,27,29,34; Y3,3,3,5,6,8,10,13,17,21,25,27,31,32|Mortality agrees. Favourable X10,18,20,27,36,41,50,57,62,66,69,78,81,86 agrees; favourable Y should7,9,20,25,33,39,42,47,53,58,60,64,67,73. Blue Y curve instead follows approximately6,12,17,22,24,30,35,42,50,57,64,69,77,80, the cumulative unfavourable complements. F-ST1-301. | PASS_1_COMPLETE |
| S ID | PLAN location | Printed relationship | Pass-1 check and outcome | Pass 1 |
|---|---|---|---|---|
| S655 | p193, GOSE=1 |n364; X36 (19.6%);Y35 (19.4%);P=.98|GOSE denominators184/180 from category sums; percentages reconcile.| PASS_1_COMPLETE |
| S656 | p193, GOSE=2 |n364; X1 (.5%);Y2 (1.1%);P=.62|Percentages reconcile; exact test undefined.| PASS_1_COMPLETE |
| S657 | p193, GOSE=3 |n364; X36 (19.6%);Y36 (20.0%);P=.92|Percentages reconcile; different denominators explain proportions despite equal counts.| PASS_1_COMPLETE |
| S658 | p193, GOSE=4 |n364; X16 (8.7%);Y18 (10.0%);P=.67|Percentages reconcile; no inferential contradiction supplied.| PASS_1_COMPLETE |
| S659 | p193, GOSE=5 |n364; X41 (22.3%);Y39 (21.7%);P=.89|Percentages reconcile; no inferential contradiction supplied.| PASS_1_COMPLETE |
| S660 | p193, GOSE=6 |n364; X17 (9.2%);Y24 (13.3%);P=.22|Percentages reconcile; no inferential contradiction supplied.| PASS_1_COMPLETE |
| S661 | p193, GOSE=7 |n364; X24 (13.0%);Y13 (7.2%);P=.07|Percentages reconcile; no interval implying significance supplied.| PASS_1_COMPLETE |
| S662 | p193, GOSE=8 |n364; X13 (7.1%);Y13 (7.2%);P=.95|Percentages reconcile; no inferential contradiction supplied.| PASS_1_COMPLETE |
| S663 | p193, GOSE score |n364;X4.3 (2.2);Y4.2 (2.1);P=.65|Weighted means4.288043/4.183333 reproduce; diagnostic sample SDs2.195044/2.131108 reproduce.| PASS_1_COMPLETE |
| S664 | p193, unfavourable GOSE |n364;X89 (48.4%);Y91 (50.6%);P=.68|Category sums/percentages reconcile; no interval/test conflict.| PASS_1_COMPLETE |
| S665 | p193, unfavourable survival |n364;X53 (28.8%);Y56 (31.1%);P=.63|89−36=53;91−35=56; percentages reconcile using GOSE denominators.| PASS_1_COMPLETE |
| S666 | p193, favourable GOSE |n364;X95 (51.6%);Y89 (49.4%);P=.68|Category sums/percentages reconcile; complementary binary P matches; p194 block counts sum95/89.| PASS_1_COMPLETE |
| S667 | p193, 180-day mortality |n390;X36 (18.0%);Y35 (18.4%);P=.91|Block denominators200/190; percentages reconcile; GOSE/survival distinction explicit.| PASS_1_COMPLETE |
| S668 | p193, header/footnote |400;GOSE364;refusals8;missing28;26/28 known survivors;survival390|364+8+28=400;364+26=390; GOSE184+180=364;survival200+190=390. Additional16 X and10 Y survivors add no deaths.| PASS_1_COMPLETE |
| S ID | PLAN location/block | M pairs X; Y | F pairs X; Y | Pass 1 |
|---|---|---|---|---|
| S669 | pp193–194, 0–25 |1/12;3/13|10/11;7/13| PASS_1_COMPLETE |
| S670 | pp193–194, 26–50 |4/14;0/10|8/14;2/8| PASS_1_COMPLETE |
| S671 | pp193–194, 51–75 |3/8;0/16|2/6;11/16| PASS_1_COMPLETE |
| S672 | pp193–194, 76–100 |3/15;2/10|7/14;5/10| PASS_1_COMPLETE |
| S673 | pp193–194, 101–125 |1/14;1/11|9/13;8/10| PASS_1_COMPLETE |
| S674 | pp193–194, 126–150 |1/12;2/12|5/11;6/12| PASS_1_COMPLETE |
| S675 | pp193–194, 151–175 |2/16;2/8|9/14;3/8| PASS_1_COMPLETE |
| S676 | pp193–194, 176–200 |2/12;3/13|7/11;5/12| PASS_1_COMPLETE |
| S677 | pp193–194, 201–225 |2/11;4/14|5/10;6/14| PASS_1_COMPLETE |
| S678 | pp193–194, 226–250 |1/11;4/13|4/10;5/12| PASS_1_COMPLETE |
| S679 | pp193–194, 251–275 |5/14;4/9|3/14;2/9| PASS_1_COMPLETE |
| S680 | pp193–194, 276–300 |2/14;2/10|9/14;4/9| PASS_1_COMPLETE |
| S681 | pp193–194, 301–325 |2/12;4/12|3/10;3/11| PASS_1_COMPLETE |
| S682 | pp193–194, 326–350 |5/16;1/9|5/16;6/9| PASS_1_COMPLETE |
| S683 | pp193–194, 351–375 |1/10;0/15|7/10;10/13| PASS_1_COMPLETE |
| S684 | pp193–194, 376–400 |1/9;3/15|2/6;6/14| PASS_1_COMPLETE |
| S685 | pp193–194, cumulative plots/table |Mortality X1,5,8,11,12,13,15,17,19,20,25,27,29,34,35,36;Y3,3,3,5,6,8,10,13,17,21,25,27,31,32,32,35|Favourable X10,18,20,27,36,41,50,57,62,66,69,78,81,86,93,95;Y7,9,20,25,33,39,42,47,53,58,60,64,67,73,83,89. Both figures agree with these sums and table values. p194 Y series agrees with the outcome label.| PASS_1_COMPLETE |

