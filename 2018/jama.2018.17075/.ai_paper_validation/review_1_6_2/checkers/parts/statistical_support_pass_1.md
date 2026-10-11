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

**Exact locations and document roles:** REPORT DOC-003 [physical p.18, eTable10, normothermia column, CT Marshall evacuated mass lesion V and non-evacuated mass lesion VI rows](../../../../joi180132supp2_prod.pdf#page=18), compared with REPORT the same display's `No. (%)` header, normothermia `(n = 196)` heading, and the other CT rows. The literal cells were visually confirmed against the source-matched page and confirmed in direct source extraction.

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

**Exact locations and document roles:** REPORT DOC-003 [physical p.22, post hoc adequate-cooling Results, final adjusted odds-ratio statement](../../../../joi180132supp2_prod.pdf#page=22), compared with REPORT the same page's definition of results as odds ratios with 95% CIs and its unadjusted odds-ratio statement. Direct source extraction and the source-matched rendered page both show the numeric token275 inside the interval text.

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
