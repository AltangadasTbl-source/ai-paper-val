# Mechanical evidence recheck — bounded report and numeric shard

Fresh evidence recheck specialist `/root/recheck_reports`, gpt-6.1-sol/high. Exact assigned stable IDs: C008, C009, C010, C011, C012, C013. This artifact covers these IDs only; it does not replace the separate protocol shard. The complete QUALITY_CONTROL_SCOPE.md and review contract were read. Current-run ledger, inclusion screen, bounded independent screening notes and checker findings provided locators. All 17 cited source pages were independently viewed from source-matched rendered images. Native text and OCR were not final authority. JavaScript arithmetic independently reproduced the numerical comparisons below; no new Python, external source, source modification or reused-artifact modification was used.

The evidence state records the reproduced printed discrepancy or bounded method-mapping question. It does not establish an unprinted production mechanism, imply an observed participant-level change, or assign a human disposition. Every ID remains Pending Human Adjudication.

## C008 — Recruitment-pool portal percentages and counts

**Location found:** Yes, all three affected combinations were located on PLAN [DOC-002 PDF p18, §5.5.1 and Table 1](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=18). The prospective recruitment section describes EMR queries and an eligible patient population, rather than randomized trial outcomes.

| Exact affected location | Source value/text matched | Comparator matched | Role |
|---|---|---|---|
| Table 1, Johns Hopkins Medicine column, eligible-patient and portal-access rows | Eligible 21,346; portal access 13,910 (56) | The same column names the eligible pool and labels portal access (%) | PLAN |
| Table 1, Reading Health System column, same two rows | Eligible 8,751; portal access 4,892 (60) | The same column names the eligible pool and labels portal access (%) | PLAN |
| §5.5.1 paragraph immediately above Table 1 | Eligible 21,410; 13,910 (56%) with portal access | The paragraph explicitly says the latter count is of these participants | PLAN |

**Consistency rule applicable:** Yes. Route A, category 3 compares each displayed numerator, eligible-pool denominator and percentage within the same display. The pattern contains two table combinations and one paragraph combination. It does not register the separate 21,346-versus-21,410 pool-count difference, infer trial efficacy denominators, or question recruitment feasibility.

**Calculation and display precision reproduced:** For a numerator n and denominator d, the conservative recomputed percentage interval is [100(n−0.5)/(d+0.5), 100(n+0.5)/(d−0.5)]. This allows the full half-unit rounding intervals even though these are integer person counts.

| Combination | Recomputed interval, % | Printed interval, % | Gap, percentage points | Gap / absolute printed percentage |
|---|---|---|---:|---:|
| 13,910 / 21,346 versus 56% | [65.160565, 65.168302] | [55.5, 56.5] | 8.660565 | 0.154653 |
| 4,892 / 8,751 versus 60% | [55.893275, 55.911091] | [59.5, 60.5] | 3.588909 | 0.059815 |
| 13,910 / 21,410 versus 56% | [64.965788, 64.973493] | [55.5, 56.5] | 8.465788 | 0.151175 |

Every relative gap exceeds 0.05. All three affected printed combinations match the registration and remain separated after conservative precision allowance.

**Necessary inputs available:** Yes for the within-display arithmetic: all numerators, denominators, percentages and their column/paragraph mapping are printed. **Exact missing inputs or definitions:** A separate percentage denominator, EMR query date or snapshot, and any distinction between the eligible-pool and portal-percentage populations are not identified.

**Source-grounded alternative interpretation:** Different query snapshots or an unprinted denominator could account for the percentages. The paragraph's reference to these participants and the table's eligible-patient rows do not themselves identify that alternative denominator. The protocol background context is explicitly retained.

**Direct observation versus inferred explanation:** Direct observation is the printed count/denominator/percentage mismatch under the named same-display mapping. A denominator substitution or query-snapshot explanation is an inference only. No trial achievement-rate or analysis-population implication is established.

**Exact remaining human question:** Which eligible-pool denominators, portal-access counts and percentages belong together in these two columns and the immediately preceding paragraph?

**Classification confirmed:** Every compared location is PLAN by prospective protocol content. Primary relationship type P_P; all relationships P_P; review domain plan_material. No higher-precedence relationship is present. No classification correction is required. **Classification ambiguity:** This is recruitment background rather than a primary statistical-design element on which efficacy analysis demonstrably relies. The arithmetic fits the expressly always-register within-display category 3, while the general plan-material definition and peripheral-background catalogue create a bounded scope/classification boundary for the auditor. This ambiguity must not be represented as an established effect on a trial result.

**Evidence state:** reproduced. **Determining recheck fact:** All three cited combinations are present on the exact source page and their conservative relative gaps exceed 0.05; the registered numerical readings require no transcription correction.

## C009 — Interpolated PA vector bypassed by printed summaries

**Location found:** Yes, every affected prose and code location was independently viewed in the results REPORT.

| Exact source location | Source value/text matched | Comparator matched | Role |
|---|---|---|---|
| [DOC-003 PDF p13, Data Preprocessing and MVPA Calculation](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=13) | Missing data within valid days were imputed by interpolation; the supplied R code was used for this calculation | This processing claim is compared with both subsequent code loops | REPORT |
| [PDF p15, activity-summary loop](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=15) | ac is assigned datai$vectormagnitude; ac_mid and ac_imp are calculated; all four activity_stats calls receive ac and timestamp | No printed reassignment of ac to ac_imp or ac_imp argument appears between imputation and these calls | REPORT |
| [PDF p16, bout-summary loop](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=16) | ac, ac_mid and ac_imp are assigned again; all three BoutsOfPA calls receive ac, valid.long and timestamp | No printed substitution of ac_imp for ac appears before these calls | REPORT |
| [PDF p34, joint primary-component row, corroboration](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=34) | Weight loss plus weekly PA component: 23/183 and 23/185 | Identifies the PA-dependent reported quantity, not a separate numerical conflict | REPORT |

**Consistency rule applicable:** Yes, as a bounded Route B statistical-method question. In the visible script, a vector calculated into ac_imp is not passed to the displayed activity or bout summaries that receive ac. The prose identifies interpolation as part of processing and labels this calculation code. Both loops constitute one repeated processing-stream pattern. The direct observation does not establish that helper functions lack their own interpolation.

**Logical comparison reproduced:** Both source loops calculate `ac_imp <- impute_missing_data(ac_mid, wnw, valid.long)` and then call the outcome-summary functions with ac. The stated processing step's output has no visible connection to those calls. Consequently the supplied account does not identify whether the claimed preprocessing is implemented inside the helpers, elsewhere in the production stream, or through the unconsumed vector. **Display precision:** Inapplicable to argument identity and data-flow mapping; no numeric gap or participant output is inferred from the script.

**Necessary inputs available:** Yes for the visible code/prose comparison: the assignments and every affected call are printed. **Exact missing inputs or definitions:** Bodies and relevant internal preprocessing of activity_stats, BoutsOfPA and impute_missing_data; the analyzed input vector; and the correspondence between the printed script and the production pipeline. Participant-level accelerometry and output values are not supplied for calculating an actual outcome change.

**Source-grounded alternative interpretation:** The helpers may impute internally, or the published script may omit production steps connecting the processed vector to analysis. Those possibilities could make the actual pipeline coherent. They are not established by the printed statements or visible calls.

**Direct observation versus inferred explanation:** Direct observation is the ac_imp/ac argument mismatch in the two printed loops against the interpolation claim. An actual omission of interpolation in the analyzed data, a changed MVPA value, or altered primary-component achievement is not directly observed and is not claimed.

**Exact remaining human question:** Which processed vector and interpolation/nonwear procedure generated the published PA quantities, and where does ac_imp enter that calculation or where is equivalent interpolation implemented?

**Classification confirmed:** All compared locations are REPORT content within DOC-003. Primary relationship S_W; all relationships S_W; review domain statistical_results. The p34 component result corroborates relevance without creating another relationship. There is no PLAN comparison or independent main-article conflict, so no P_R or S_C relationship is added. No classification correction is required; the unresolved production mapping is an evidence limitation rather than a document-role ambiguity.

**Evidence state:** reproduced. **Determining recheck fact:** The claimed interpolated calculation and both affected ac-consuming summary loops are present exactly as registered, while the supplied data flow does not visibly connect ac_imp to either summary. Reproduction is restricted to that printed method-mapping question.

## C010 — Denominator after PA zero assignment

**Location found:** Yes, every cited aggregation and zero-assignment location was independently viewed.

| Exact source location | Source value/text matched | Comparator matched | Role |
|---|---|---|---|
| [DOC-003 PDF p13, Aggregation of MVPA Across Visits](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=13) | Weekly MVPA from all valid wear periods is summed and divided by available wear periods, maximum 11 postbaseline visits | This denominator definition is compared with zero assignment to periods without valid data | REPORT |
| [PDF p13, Data Preprocessing and Actigraphy Compliance](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=13) | Days without valid accelerometry receive zero MVPA; insufficient assigned-day wear results in zero minutes for the week | The source does not state whether these zero-filled periods become available wear periods for the aggregate denominator | REPORT |
| [PDF p30, eTable18a method](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=30) | Primary analysis assumes zero weekly PA during assigned periods without monitor wear | Corroborates the primary-analysis application of zero assignment | REPORT |
| [PDF p49, eTable8b handling column and rationale](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=49) | Zero minutes/week assigned to nonwear periods; no valid wear data leads to zero imputation for that month | The monthly zero values are not explicitly mapped to the available-period denominator on p13 | REPORT |

**Consistency rule applicable:** Yes, as the bounded Route B method/denominator question registered in the ledger. Available or valid recorded periods and scheduled periods after zero filling need not denote the same denominator. The report supplies both descriptions but does not explicitly give their joining definition. This is separate from the original-versus-reported missing-data specification and from the preceding vector-processing candidate.

**Logical comparison reproduced:** Let v denote the number of valid recorded periods and z the number of other scheduled periods assigned zero. Summing observed MVPA and dividing by v differs from dividing by v+z whenever z>0 and the sum is positive. Pure illustration, not participant data: one 200-minute recorded period plus one unavailable period gives 200/1=200 or (200+0)/2=100 minutes/week. These alternatives lie on different sides of 150 minutes/week. The direct-source wording does not explicitly choose between them by defining available after zero assignment. **Display precision:** Inapplicable to distinct aggregation formulas; the example has no empirical rounding claim.

**Necessary inputs available:** Yes for comparing the printed numerator/denominator and zero-assignment descriptions. **Exact missing inputs or definitions:** Whether a zero-filled nonwear/noncompliant period counts in available wear periods; whether averaging first operates across valid days, complete scheduled weeks or zero-filled monthly visits; and the endpoint-specific production denominator. Individual monthly PA and compliance records are absent, so actual reclassification cannot be quantified.

**Source-grounded alternative interpretation:** Assigning zero may make the scheduled period available to the final average, coherently reconciling the implementation. That is a plausible interpretation of the supplied zero-imputation rationale. The record asks for the explicit definition and does not assert that implementation excluded such periods or that participant classifications changed.

**Direct observation versus inferred explanation:** Direct observation is the unresolved mapping between valid/available averaging and zero filling in the supplied method descriptions. The contrasting formulas illustrate why the definition matters. They are not observed participant calculations or proof of a numerically changed primary result.

**Exact remaining human question:** Does each missing or noncompliant period assigned zero enter the denominator of the PA average used for the primary component and continuous PA summaries, and how are day, week and monthly-period aggregation joined?

**Classification confirmed:** Every compared location is REPORT methods/results within DOC-003. Primary relationship S_W; all relationships S_W; review domain statistical_results. No P_R relationship is added: this candidate concerns the report's aggregation definition, whereas the planned-versus-reported zero-assignment change belongs to a separate ID. No classification correction is required.

**Evidence state:** reproduced. **Determining recheck fact:** Both valid/available-period averaging and primary zero assignment are printed at the registered exact locations, with no explicit denominator-after-imputation mapping. The reproduced issue is that bounded method question, not a demonstrated incoherent implementation.

## C011 — Two AI-version exposure percentages

**Location found:** Yes, both affected rows and all denominator corroborators were independently viewed.

| Exact source location | Source value/text matched | Comparator matched | Role |
|---|---|---|---|
| [DOC-003 PDF p37, eTable1b, version 11.100.131, September 2023](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=37) | 5 (5) participants exposed | Heading expressly defines percentage of primary-analysis population assigned to AI-DPP | REPORT |
| [Same page, version 122.100.407, December 2024](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=37) | 5 (5) participants exposed | Same column heading; no changed late-version denominator is printed | REPORT |
| [PDF p27, Definitions of study cohorts](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=27) | Primary analysis includes all randomized participants | Establishes the population named by eTable1b | REPORT |
| [PDF p41, eTable4 randomized-population heading](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=41) | AI randomized N=183 | Matches the primary-analysis denominator, not the separate PP denominator of 151 | REPORT |
| [PDF p34, primary outcome/component forest rows](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=34) | AI primary denominator 183 | Independently corroborates the named primary denominator | REPORT |

**Consistency rule applicable:** Yes, Route A, category 3. The table's own percentage-population heading supplies the denominator definition; exact cohort locations establish its size. Both 5 (5%) rows form one repeated count/denominator/percentage pattern. Version exposure is not assumed to be mutually exclusive or an exhaustive partition.

**Calculation and display precision reproduced:** Centrally 100×5/183=2.732240%. Conservative half-unit count and denominator intervals give [100×4.5/183.5, 100×5.5/182.5]=[2.452316, 3.013699]%. The printed 5% interval is [4.5, 5.5]%. Gap 4.5−3.013699=1.486301 percentage points; relative gap 1.486301/5=0.297260, above 0.05, for each affected row. The seven preceding same-column rows are 58 (32), 102 (56), 109 (60), 103 (56), 99 (54), 105 (57), 104 (57); their central percentages using 183 are approximately 31.69, 55.74, 59.56, 56.28, 54.10, 57.38, 56.83, respectively, consistent with their integer percentages. Their coherence corroborates the named denominator without imposing a sum constraint.

**Necessary inputs available:** Yes: both counts, both percentages, the column population definition and AI primary N=183. **Exact missing inputs or definitions:** Any alternative late-version exposure population and its denominator, and any explanation distinguishing late-version rows from the preceding same-column rows.

**Source-grounded alternative interpretation:** A denominator around 100 could yield a 5% percentage for five exposures, but no such late-version denominator is specified. Exposure overlap is compatible with the table and does not explain the individual percentage mapping.

**Direct observation versus inferred explanation:** Direct observation is the two printed count/percentage combinations under the expressly named population. A changed denominator or substituted displayed value is only a possible explanation. No version exposure partition, participant assignment change or efficacy consequence is inferred.

**Exact remaining human question:** Which exposure counts and denominators govern the percentages in the September 2023 and December 2024 version rows?

**Classification confirmed:** Affected display and denominator corroborators are REPORT content within DOC-003. Primary relationship S_W; all relationships S_W; review domain statistical_results. Corroborators do not create additional cross-document conflicts. No classification correction or document-role ambiguity is required.

**Evidence state:** reproduced. **Determining recheck fact:** Both source rows visibly print 5 (5) under the primary-analysis heading, and the source-matched AI denominator is 183; conservative arithmetic remains separated beyond 0.05. No transcription correction is required.

## C012 — Baseline HbA1c-subgroup categorical P values

**Location found:** Yes, the entire cited count/P-value comparison and supplied method pointers were independently viewed.

| Exact source location | Source value/text matched | Comparator matched | Role |
|---|---|---|---|
| [DOC-003 PDF p44, eTable6 group headings and site rows](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=44) | A1c<5.7%, N=108; A1c5.7–6.4%, N=260. Johns Hopkins 79/164; Reading 29/96 | These site rows total the displayed two groups | REPORT |
| [Same page, ethnicity rows](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=44) | Not Hispanic 96/247; Hispanic 10/10; declined 0/2; unknown 2/1 | Four displayed categories total 108/260 | REPORT |
| [PDF p45, eTable6 footnote 1](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=45) | Site differed between groups, P=0.024; ethnicity differed, P=0.018 | Footnote belongs to the p44 baseline-A1c groups and categorical rows | REPORT |
| [PDF p29, eTable6 method-index row](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=29) | Baseline A1c-status comparison using methods described for main Table 1 | No distinct adjusted model or categorical-population mapping is printed here | REPORT |
| [PDF p28, eTable3 method-index row](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=28) | Main Table 1 baseline-method pointer | Corroborates the pointer; explicit chi-square/Wilcoxon prose continuing on p29 belongs to eTable4, not eTable6 | REPORT |
| [DOC-002 PDF p37, §9.4.1 general approach](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=37) | Categorical baseline differences assessed with chi-square or Fisher exact as appropriate | Supplies general test choices only, not an independent disagreement with the REPORT | PLAN |

**Consistency rule applicable:** Yes, under the registered Route B comparison of printed categorical counts and their footnote test mapping. The calculations below cover both general categorical methods named in the supplied plan. They do not assume a mandatory test convention or add an interval/P-value Route A category 1: no estimate/confidence-interval pairing is printed in this display.

**Calculation independently reproduced:** For each table, Pearson chi-square is Σ(O−E)²/E using the printed integer margins. Two-sided exact tests sum fixed-margin table probabilities no greater than the observed-table probability. Site enumeration contains 109 feasible 2×2 tables; ethnicity enumeration contains 252 feasible 2×4 tables with category totals 343,20,2,3 and first-group total 108. Log-factorial arithmetic independently gives the following results; exact-test total probability sums are within 7×10⁻¹³ of one. Pearson tail values are numerical approximations, sufficient for the reported digits.

| Display comparison | Pearson statistic and df | Pearson P | Exact two-sided P | Printed P |
|---|---|---:|---:|---:|
| Site, all displayed participants | χ²=3.450589, df=1 | ≈0.063229 | 0.0702626313 | 0.024 |
| Ethnicity, all four displayed categories | χ²=7.265468, df=3 | ≈0.063901 | 0.0550865759 | 0.018 |
| Ethnicity, known Hispanic/not-Hispanic categories only, explicit alternative | χ²=4.428916, df=1 | ≈0.035335 | 0.0438699543 | 0.018 |

**Display precision reproduced:** Each participant count has an integer half-unit interval containing only that feasible integer, so no different contingency table arises from input rounding. Printed P intervals are [0.0235,0.0245] for site and [0.0175,0.0185] for ethnicity. Against the full-table exact values, the respective gaps are 0.0457626313 and 0.0365865759; dividing by 0.024 and 0.018 gives relative discrepancies 1.906776 and 2.032588, above 0.05. Pearson counterparts have relative discrepancies approximately 1.613713 and 2.522278. The known-ethnicity-only alternative also remains separated: exact relative gap 1.409442. Site alone remains nonsignificant at 0.05 under both named choices, unlike the printed site statement. Ethnicity coding can alter significance, and is expressly left as a missing mapping rather than silently fixed.

**Necessary inputs available:** Yes for the reproduced printed-table categorical calculations: group sizes, category counts, source footnote values and general named methods. **Exact missing inputs or definitions:** The actual test/model and sidedness used for this footnote; any covariate adjustment or changed population; treatment of unknown/declined ethnicity, category collapsing or contrast coding; and the final mapping from those choices to the displayed table.

**Source-grounded alternative interpretation:** A different coded contrast, adjusted model, population or test convention could generate the footnote values. The general method pointer does not establish such a mapping. The plan's named categorical choices corroborate available calculations without proving which test was executed. No preferred analysis is proposed.

**Direct observation versus inferred explanation:** Direct observations are the printed groups, counts, P values and footnote claims. The exact and Pearson computations are reproduced comparisons under explicitly described method choices. An unprinted alternative model, coding or population is a possible explanation only; incompatibility with every possible categorical analysis is not claimed.

**Exact remaining human question:** Which population, ethnicity coding and categorical test/model generated site P=0.024 and ethnicity P=0.018, and how do those values map to the displayed 108/260 participant groups?

**Classification confirmed:** The discrepancy is within REPORT DOC-003, so primary relationship S_W; all relationships S_W; review domain statistical_results. DOC-002 p37 is PLAN by prospective protocol content but only corroborates general methods; it introduces no independent P_R relationship. The independently screened Route B classification is retained rather than reverting to the checker's interval-specific category 1 proposal. No ledger classification correction is required. **Classification ambiguity:** The executed method/population/coding mapping remains unavailable and limits the claim to the named within-display test question.

**Evidence state:** reproduced. **Determining recheck fact:** The source groups/counts and both footnote values match, and independent exact calculations under supplied general methods remain separated beyond display precision, with an unresolved method/population mapping. Reproduction is not a claim that every possible unprinted model gives these same computed P values.

## C013 — MI-pooled risks versus displayed risk difference

**Location found:** Yes, the same-row risk/RD values and all cited pooling descriptions were independently viewed.

| Exact source location | Source value/text matched | Comparator matched | Role |
|---|---|---|---|
| [DOC-003 PDF p59, eTable16 sole primary-outcome row](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=59) | MI-pooled achievement risks: AI 32.2%, human 31.9%; RD −1.1 pp with one-sided 95% lower limit −11.5 pp | Same row and risk-difference heading identify the between-arm contrast; no separate adjusted final contrast is labeled | REPORT |
| [PDF p30, eTable16 methods](../../../../joi250084supp2_prod_1765403089.61751.pdf#page=30) | Twenty imputed datasets combined using Rubin's rules; imputation predictors include arm, baseline variables, demographics and engagement | Describes imputation/pooling, not a distinct final adjusted outcome contrast for the p59 RD | REPORT |
| [DOC-002 PDF p88, MICE method row](../../../../joi250084supp1_prod_1765403089.61351.pdf#page=88) | Final outcome proportions and between-group risk differences combined across imputations using Rubin's rules | Corroborates pooling; supplies no independent plan/report conflict | PLAN |

**Consistency rule applicable:** Yes, as the registered Route B same-display risk/contrast mapping question. For common imputation-specific arm-risk estimands, linear pooling satisfies mean(pAI−pH)=mean(pAI)−mean(pH). Imputation predictors alone do not establish adjustment of the final contrast. The comparison does not treat an explicitly labeled adjusted estimate as a crude count difference. It does not assume that all possible final modeled contrasts must equal pooled marginal risk differences.

**Calculation and display precision reproduced:** Printed one-decimal risks imply AI [32.15,32.25]% and human [31.85,31.95]%, hence common-risk contrast [0.20,0.40] pp. The printed RD interval is [−1.15,−1.05] pp. Gap 0.20−(−1.05)=1.25 pp; relative discrepancy 1.25/1.1=1.136364, above 0.05. Thus the displayed positive risk contrast and negative RD do not reconcile under the common-estimand pooling identity. The −11.5 pp one-sided lower endpoint exceeds the −15 pp NI margin; no independent NI-conclusion conflict is alleged.

**Necessary inputs available:** Yes for the printed-value and common-risk precision comparison: both risks, RD, sidedness/lower limit and pooling description. **Exact missing inputs or definitions:** Whether all three cells share the same imputation-specific risk estimands; the final estimation model/link and adjustment variables for RD; any standardization target or differently weighted pooling; and imputation-specific final risk and contrast estimates. Those inputs are needed to distinguish the arithmetic mapping from a distinct modeled contrast and to reproduce the printed final estimator exactly.

**Source-grounded alternative interpretation:** An independently adjusted or standardized final RD can coexist with the two pooled marginal arm risks, including a different direction. The supplied material does not explicitly label that final contrast or map it to the arm risks. The recheck retains this possibility and asks for that mapping; it does not impose a preferred model or claim the observed data necessarily have a positive adjusted effect.

**Direct observation versus inferred explanation:** Direct observations are the three same-row point values and the pooling statements. The reproduced arithmetic applies to common imputation-specific risk estimands. Distinct adjusted estimands, production mechanisms or substituted display values are inferred alternatives only. No raw-data inconsistency, exact variance reproduction or changed NI conclusion is established.

**Exact remaining human question:** Which final estimation model and estimand produced RD −1.1 pp, and how does it relate to the AI 32.2% and human 31.9% MI-pooled risks in the same row?

**Classification confirmed:** Compared quantities and report method description are REPORT content within DOC-003. Primary relationship S_W; all relationships S_W; review domain statistical_results. PLAN p88 only corroborates the pooling description and does not introduce P_R. No ledger classification correction is required. **Classification ambiguity:** Distinct final modeled estimands could reconcile the values; the absent mapping remains explicit rather than being converted to a claim of universal estimator incompatibility.

**Evidence state:** reproduced. **Determining recheck fact:** Exact source cells and pooling descriptions match the registration, and their common-estimand arithmetic exceeds display precision while the supplied account does not identify a distinct final contrast. This state records the bounded printed mapping question and preserves the separately modeled alternative.

## Classification fact table

| ID | Review domain | Relationship type | All relationships | Compared roles by content | Evidence state | Recheck classification action |
|---|---|---|---|---|---|---|
| C008 | plan_material | P_P | P_P | PLAN DOC-002 p18 table and paragraph | reproduced | Confirmed; recruitment-background scope/domain boundary explicitly retained |
| C009 | statistical_results | S_W | S_W | REPORT DOC-003 p13 prose versus pp15–16 code | reproduced | Confirmed; p34 REPORT result only corroborates relevance |
| C010 | statistical_results | S_W | S_W | REPORT DOC-003 p13 aggregation versus pp13,30,49 zero assignment | reproduced | Confirmed; separate planned-versus-reported candidate not merged here |
| C011 | statistical_results | S_W | S_W | REPORT DOC-003 p37 two rows versus its population definition, corroborated by pp27,34,41 | reproduced | Confirmed; all compared content lies in one results REPORT |
| C012 | statistical_results | S_W | S_W | REPORT DOC-003 pp44–45 counts/footnote; REPORT pp28–29 pointers and PLAN DOC-002 p37 only corroborate methods | reproduced | Confirmed; Route B and no independent P_R preserved |
| C013 | statistical_results | S_W | S_W | REPORT DOC-003 p59 same-row risks/RD; REPORT p30 and PLAN DOC-002 p88 only corroborate pooling | reproduced | Confirmed; no independent P_R introduced |

No source transcription or location correction was needed. All relationships listed are the only supported conflict relationships, so precedence P_R > P_P > S_C > S_W makes no further change. This table supplies evidence/classification facts only; inclusion audit remains for the separate fresh quality-control auditor.

## Inspected page and engine record

All 17 unique pages below were actually viewed in this fresh specialist. Existing current-run preprocessing images are direct-source CPU renders, engine PyMuPDF 1.28.0 at 200 dpi via the user-authorized stt interpreter and supplied pdf_tools.py. The preserved p41 image is a source-matched historical render whose historical rendering engine is not recorded. No new rendering or OCR was required. The tooling record's GPU_USER_REQUESTED setting concerns approved GPU OCR; no OCR was used here.

| Direct source and PDF page | Viewed image, package-relative path | Engine |
|---|---|---|
| DOC-002 p18 | .ai_paper_validation/review_1_6_2/preprocessing/numeric-plan-page018.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-002 p37 | .ai_paper_validation/review_1_6_2/preprocessing/st1-plan-p37.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-002 p88 | .ai_paper_validation/review_1_6_2/preprocessing/st1-plan-p88.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-003 p13 | .ai_paper_validation/review_1_6_2/preprocessing/st1-report-p13.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-003 p15 | .ai_paper_validation/review_1_6_2/preprocessing/st1-report-p15.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-003 p16 | .ai_paper_validation/review_1_6_2/preprocessing/st1-report-p16.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-003 p27 | .ai_paper_validation/review_1_6_2/preprocessing/cross-results-27.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-003 p28 | .ai_paper_validation/review_1_6_2/preprocessing/st1-report-p28.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-003 p29 | .ai_paper_validation/review_1_6_2/preprocessing/st1-report-p29.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-003 p30 | .ai_paper_validation/review_1_6_2/preprocessing/screen-results-30.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-003 p34 | .ai_paper_validation/review_1_6_2/preprocessing/cross-results-34.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-003 p37 | .ai_paper_validation/review_1_6_2/preprocessing/numeric-support-p037.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-003 p41 | .ai_paper_validation/document_outputs/DOC-003-results-supplement/page_images/page-041.png | Preserved source-matched render; historical engine unrecorded |
| DOC-003 p44 | .ai_paper_validation/review_1_6_2/preprocessing/st1-report-p44.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-003 p45 | .ai_paper_validation/review_1_6_2/preprocessing/st1-report-p45.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-003 p49 | .ai_paper_validation/review_1_6_2/preprocessing/cross-results-49.png | PyMuPDF 1.28.0 / 200 dpi / CPU |
| DOC-003 p59 | .ai_paper_validation/review_1_6_2/preprocessing/st1-report-p59.png | PyMuPDF 1.28.0 / 200 dpi / CPU |

Completion: six assigned IDs covered separately; every affected repeated-pattern location inspected; 17 unique source pages viewed; six evidence states reproduced; zero transcription corrections; zero not_reproduced states; no location or scientific coverage gap. Remaining items are explicitly named per ID: portal denominator mapping and background classification boundary, PA helper/production-stream mapping, denominator after PA zero assignment, late-version denominator, subgroup categorical-test/model/population/coding mapping, and final MI-estimand/model mapping. No candidate was deleted or assigned a disposition.
