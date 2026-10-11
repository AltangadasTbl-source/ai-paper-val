# Mechanical Evidence Recheck and Classification Confirmation

Status: COMPLETE. Runtime identity: /root/evidence_recheck. Fresh evidence_rechecker stage, gpt-6.1-sol/high. Canonical record includes the fresh pass-2 C005 developmental recheck, appended below; original stage provenance remains recorded. Assigned and covered stable IDs: C001, C002, C003, C004, C005, C006. Every registered affected location was found. Evidence-state counts: reproduced 6; reproduced_after_transcription_correction 0; not_reproduced 0. No registered value, source page, document role, relationship type, all-relationships field, or review domain required a transcription or classification change. These are mechanical evidence facts; every candidate remains Pending Human Adjudication.

QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely, together with PERFORMANCE_PROFILE.md, report_spec.md, settings.toml, the current ledger, screening record, checker evidence and tooling record. Supplied evidence only was used. Existing text and maps served as locators; readable source-page images confirmed the numbers, symbols and compared analysis statements. No legacy scientific conclusion or external source was used.

## Classification Facts for Coordinator Writeback

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Classification change |
|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main article abstract versus REPORT main article flow and surgery narrative | reproduced | None |
| C002 | protocol_report | P_R | P_R, P_P | PLAN protocol versus PLAN SAP versus REPORT main article and results supplement | reproduced | None |
| C003 | protocol_report | P_R | P_R, P_P | PLAN protocol and PLAN SAP versus REPORT main article prior specifications | reproduced | None |
| C004 | protocol_report | P_R | P_R | PLAN protocol and PLAN SAP versus REPORT main article formal interim | reproduced | None |
| C005 | protocol_report | P_R | P_R | PLAN protocol and PLAN SAP analyses versus REPORT main article and results supplement | reproduced | None |
| C006 | plan_material | P_P | P_P | PLAN protocol hypothesis versus PLAN protocol power assumptions; PLAN SAP clarification | reproduced | None |

The primary relationship in each mixed candidate follows P_R > P_P > S_C > S_W. Corroborating documents do not add relationships. The main article reports completed trial methods/results; the non-plan results supplement contains completed enrollment and outcome analyses, so both are REPORT. The protocol and SAP contain prospective hypotheses and analysis specifications, so both are PLAN, including retrospective explanatory passages embedded in those documents. No role was inferred from a filename or supplement number.

## C001 — Abstract Operative-Repair Population Count

**Location found; source and comparator matched:** Yes, separately at every registered location.

| Exact supplied-source location | Role by content | Directly confirmed content and comparison function |
|---|---|---|
| [Main PDF p. 1, Abstract Results opening sentence](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1) | REPORT | Among 338 randomized infants, the sentence states that 320 underwent operative repair. This is the registered source count and operative-population attribution. |
| [Main PDF p. 3, Figure 1, both treatment branches](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3) | REPORT | Early: 163 retained, 147 repairs before discharge, 5 after discharge, 11 without repair; late: 157 retained, 90 repairs after reaching 55 weeks, 39 before reaching it, 28 without repair. Nine infants per arm did not undergo treatment as randomized. These are independent comparator counts. |
| [Main PDF p. 4, Patient Characteristics and Surgery Characteristics](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4) | REPORT | Nine withdrawals per arm leave 163/157; the early-arm surgery paragraph gives 152 repairs among 163 infants. This matches the registered population and early count. |
| [Main PDF p. 5, Surgery Characteristics continuation, both columns](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5) | REPORT | Early 11 without repair and 5 repairs after discharge; late 129 repairs among 157 infants and 28 without repair. This matches the registered late count and no-repair comparators. |

**Consistency rule applicable:** Yes. Focus A and Route B: the same infant operative total, across disjoint randomized arms, must match its arm-specific repair counts when the population and observation window are matched. The explicit abstract result-count comparison is within scope. This concerns a count, so statistical_results applies rather than report_internal_inconsistency.

**Calculation and display-precision interval check:** Reproduced. The body gives 152 + 129 = 281. The flow independently gives (147 + 5) + (90 + 39) = 281, and 163 + 157 − 11 − 28 = 281. The retained population is 163 + 157 = 320. Exact integer gap: 320 − 281 = 39; relative gap 39/320 = 0.121875. Conservatively allowing half-unit intervals for the two body counts gives [151.5,152.5] + [128.5,129.5] = [280,282], compared with abstract [319.5,320.5]; gap 37.5, relative gap 37.5/320 = 0.1171875. The four repair branches give [279,283], gap 36.5/320 = 0.1140625. The retained-minus-no-repair calculation gives [279,283], with the same gap. All exceed 0.05. Assigning repairs to all 18 withdrawals would give at most 299 among the randomized infants; using 338 ± 0.5 minus the two no-repair counts ± 0.5 gives upper bound 300.5, below abstract lower bound 319.5 by 19, or 19/320 = 0.059375. Withdrawals alone cannot bridge the printed total.

**Necessary inputs available:** Yes for the registered count comparison: arm-specific repair, retained, randomized, withdrawal and no-repair counts are supplied. **Exact missing inputs or definitions:** A distinct population or observation window that could support the abstract's 320 operative repairs is not defined; participant-level operation histories after the displayed observation period are not supplied. Neither is necessary to reproduce the printed comparison.

**Source-grounded alternative interpretation:** The abstract may refer to the 320 nonwithdrawn infants; that total is explicitly reconstructable from the body. A separate repair window/population remains possible but is not identified in the supplied materials. No substitute count is prescribed.

**Direct observation versus inferred explanation:** The printed 320 operative count and printed total of 281 repairs are direct observations. Attributing 320 to a retained-population label or a production mechanism is an inference, not an established explanation.

**Classification confirmation:** S_W; All relationships S_W; statistical_results. Every conflicting count is within one REPORT article. Neither plan nor the results supplement is a conflicting comparator. No classification ambiguity or change.

**Evidence state:** reproduced. Determining fact: source-image readings confirm 320 as operative repairs and 152/129 as arm-specific repairs; their intervals remain separated beyond 0.05.

**Exact remaining human question:** Which population and observation window does the abstract's statement that 320 infants underwent operative repair describe, given the 152 early and 129 late repairs and the 39 infants without repair in the body and flow?

## C002 — Planned and Reported Primary and Hospital-Day Analysis Specifications

**Location found; source and comparator matched:** Yes at every registered location.

| Exact supplied-source location | Role by content | Directly confirmed content and comparison function |
|---|---|---|
| [Protocol PDF p. 13, lines 471–488](../../../joi240020supp1_prod_1710443209.74911.pdf#page=13) | PLAN | Primary any-SAE: binomial GLMM with log link, treatment/GA covariates and random center. Hospital days: lognormal model with treatment/GA and random center. Continuous outcomes have absolute differences and 95% CIs. Final Bayesian analyses are also specified. |
| [SAP PDF p. 7, lines 263–266](../../../joi240020supp2_prod_1710443209.75411.pdf#page=7) | PLAN | Multilevel models; same model for frequentist and Bayesian analyses for each outcome; binary logistic and count negative-binomial models. |
| [SAP PDF p. 8, lines 267–271](../../../joi240020supp2_prod_1710443209.75411.pdf#page=8) | PLAN | Site random intercept and GA-group covariate; binary RR/RD calculated from logistic model, count RR, and uncertainty intervals. |
| [Main PDF p. 4, Statistical Analysis model paragraph](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4) | REPORT | Logistic mixed primary and negative-binomial mixed hospital model; GA and site included. Frequentist primary instead uses GEE logistic with exchangeable site correlation because the mixed-effects model did not converge. |
| [Main PDF p. 6, Table 2 and outcome narrative](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6) | REPORT | Bayesian primary RR 0.68/RD −7.9%; hospital RR 0.91. These identify the affected outcomes and modeled effects. |
| [Results-supplement PDF p. 5, eTable 2 and model footnote](../../../joi240020supp3_prod_1710443209.75411.pdf#page=5) | REPORT | Frequentist primary RR 0.65/RD −9.0%; hospital RR 0.91. The footnote repeats the logistic/negative-binomial specifications and explicitly repeats the convergence-driven GEE exception. |

**Consistency rule applicable:** Yes. Focus D, Route A category 5, concerning replacement of a planned primary/key-secondary analysis. The SAP shared multilevel primary model and reported frequentist GEE implementation are distinct. The hospital-day model and measure, and primary link, also differ between protocol and later SAP/report. No preferred model is inferred.

**Calculation or logical comparison reproduced, including display precision:** Reproduced by matching outcome, 10-month window, population, model family/link and center structure. Protocol log-link binomial differs from SAP/report logistic; protocol lognormal hospital modeling with absolute differences differs from negative-binomial/count RR; SAP site-random-intercept/shared frequentist-Bayesian primary model differs from the explicitly reported frequentist GEE replacement. Model names, links and covariance structures are qualitative specifications; no half-unit interval or relative numerical gap applies. The differing Bayesian and frequentist effect values are affected outputs, not a claim that two inferential analyses must yield identical numbers.

**Necessary inputs available:** Yes for the specification comparison and identification of affected effects. **Exact missing inputs or definitions:** The governing dated amendment/analysis-specification precedence, implementation code, original frequentist mixed-model output and convergence diagnostics are not supplied. These are needed to establish implementation history or reproduce fitted effects, not the printed model replacement.

**Source-grounded alternative interpretation:** The SAP is the later detailed plan and may intentionally supersede the protocol's log-link/lognormal specifications. The report itself explains the GEE fallback through nonconvergence. Both alternatives are retained explicitly; the disclosed reason does not make GEE the same analysis as the planned mixed model or supply the absent mixed-model result.

**Direct observation versus inferred explanation:** The three sets of specifications and disclosed nonconvergence are printed facts. Which dated specification formally superseded another, and whether a separate planned output was retained elsewhere, remain unestablished.

**Classification confirmation:** P_R; All relationships P_R, P_P; protocol_report. P_R arises from report versus protocol/SAP analyses; P_P arises from explicit protocol/SAP family/link/measure differences. P_R takes precedence. The two REPORT documents agree and add no S_C relationship. No classification change; possible intentional supersession is the bounded classification ambiguity.

**Evidence state:** reproduced. Determining fact: the source confirms both the SAP shared multilevel model specification and the expressly disclosed report GEE replacement, together with protocol/SAP family differences.

**Exact remaining human question:** Which dated specifications governed the final primary and hospital-day models, how did the logistic/negative-binomial specifications supersede the protocol's log-link/lognormal specifications, and which planned analyses were replaced or retained under the disclosed GEE fallback?

## C003 — Bayesian Intervention and Subgroup Main-Effect Prior Specifications

**Location found; source and comparator matched:** Yes at every registered location.

| Exact supplied-source location | Role by content | Directly confirmed content and comparison function |
|---|---|---|
| [Protocol PDF p. 13, lines 486–498](../../../joi240020supp1_prod_1710443209.74911.pdf#page=13) | PLAN | General final neutral intervention prior centered RR 1 with 95% interval 0.33–3.0; subgroup main effects N(0,1000), with Uniform(0,1000) for SD parameters. |
| [SAP PDF p. 8, lines 283–290](../../../joi240020supp2_prod_1710443209.75411.pdf#page=8) | PLAN | Categorical intervention OR prior centered 1, 95% CrI 0.2–4, log-OR Normal mean 0/SD 0.7; count RR prior 0.33–3.3. Intercept Normal SD 10, GA Normal SD 1, random-intercept SD half-Normal SD 1. |
| [SAP PDF p. 9, lines 327–332](../../../joi240020supp2_prod_1710443209.75411.pdf#page=9) | PLAN | Subgroup main effects reuse primary-analysis priors. Interaction Normal SD 0.6 is separately printed but is not an additional registered numerical discrepancy. |
| [Main PDF p. 4, priors and modifier paragraphs](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4) | REPORT | Categorical/count intervention OR/RR priors centered 1 with 95% CrI 0.33–3.0; other terms called vague. Modifier paragraph gives interaction range 0.33–3.0. |
| [Main PDF p. 6, Table 2/Figure 2 and narrative](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6) | REPORT | Affected primary RR 0.68/RD −7.9%/97% benefit and hospital RR 0.91/82% benefit. |
| [Main PDF p. 8, Figure 3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8) | REPORT | Affected primary subgroup posterior effects, intervals and benefit probabilities for GA, BPD and surgical approach. |

**Consistency rule applicable:** Yes. Focus D and Route B: compare printed parameter-specific intervention-prior ranges for primary categorical SAE and abstract-reported hospital-day count outcomes, and compare explicit subgroup main-effect/SD specifications between plans. A neutral center does not identify a common spread or SD distribution. The candidate concerns actual competing printed specifications rather than merely a missing method detail.

**Calculation and display-precision interval check:** Reproduced. Using SAP as reference copy: categorical lower 0.2 has interval [0.15,0.25], versus report 0.33 interval [0.325,0.335]; gap 0.075, relative 0.075/0.2 = 0.375. Categorical upper 4 has [3.5,4.5], versus report 3.0 [2.95,3.05]; gap 0.45, relative 0.45/4 = 0.1125. Count upper 3.3 has [3.25,3.35], versus report 3.0 [2.95,3.05]; gap 0.20, relative 0.20/3.3 = 0.060606. Each exceeds 0.05. Count lower endpoints are both 0.33 and have overlapping intervals, gap zero; this endpoint is not discrepant. Protocol/SAP subgroup main-effect/SD distribution statements are a qualitative comparison; Uniform versus half-Normal SD specifications are distinct without interpreting N(0,1000)'s second parameter. No numeric precision interval applies to those family statements. Within-SAP Normal SD 0.7 versus its range and interaction SD 0.6 versus report range are outside the registered pattern; no conflict is inferred from those screened precision comparisons.

**Necessary inputs available:** Yes for the printed endpoint and distribution comparisons and affected-result identification. **Exact missing inputs or definitions:** Actual parameter-specific prior implementation, the protocol N(0,1000) second-parameter convention, count-prior functional form/log scale, final prior-precedence statement, analysis code and posterior draws are not supplied. They are required to establish the implemented prior or quantify any posterior change; no such change is claimed.

**Source-grounded alternative interpretation:** The report's general range agrees with the protocol and may abbreviate that specification; the detailed SAP may describe computational priors or supersede the protocol subgroup priors. Different parameter scales may have been used. None of these possibilities identifies which competing printed intervention ranges describe the final implementation. The adjective vague is not independently treated as a numerical distribution conflict.

**Direct observation versus inferred explanation:** Differing intervention endpoints and subgroup main-effect/SD specifications are directly printed. A particular implemented prior, source of the differences, and numerical posterior consequence are not observed.

**Classification confirmation:** P_R; All relationships P_R, P_P; protocol_report. SAP PLAN versus main REPORT intervention ranges supplies P_R; protocol/SAP subgroup specifications supply P_P; P_R takes precedence. The protocol general intervention range merely corroborates the report and adds no relationship. Affected REPORT results are identification locations, not conflicting comparators. No classification change. Ambiguity is limited to implementation and plan precedence.

**Evidence state:** reproduced. Determining fact: three source-confirmed intervention endpoint comparisons retain relative interval gaps above 0.05, and plan subgroup SD specifications differ explicitly.

**Exact remaining human question:** Which parameter-specific intervention and subgroup main-effect priors were actually used for the reported primary, hospital-day and subgroup Bayesian results, and how do the supplied ranges, distributions and N(0,1000) convention describe that implementation?

## C004 — Formal Interim Analysis Information Milestone

**Location found; source and comparator matched:** Yes at every registered location.

| Exact supplied-source location | Role by content | Directly confirmed content and comparison function |
|---|---|---|
| [Protocol PDF p. 14, lines 519–530](../../../joi240020supp1_prod_1710443209.74911.pdf#page=14) | PLAN | Amended safety/efficacy analysis expecting 10-month outcomes for approximately 200 infants; efficacy stopping guideline probability of decreased SAEs >95%. |
| [Protocol PDF p. 25, version 7 history, lines 979–982](../../../joi240020supp1_prod_1710443209.74911.pdf#page=25) | PLAN | Approximately-200-infant safety/efficacy review replaces two interim safety analyses at 33%/66% enrollment; final Bayesian analyses added. This confirms the applicable amended plan rather than an earlier two-look design. |
| [SAP PDF p. 4, lines 119–127](../../../joi240020supp2_prod_1710443209.75411.pdf#page=4) | PLAN | One formal primary interim when 10-month data available for 200 randomized infants; stopping note gives 97% benefit crossing 95%. It does not state a revised 309 milestone. |
| [Main PDF p. 4, formal interim paragraph](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4) | REPORT | Formal interim completed with data available for 309 infants in February 2021; 97% benefit exceeded 95%, and enrollment stopped. |
| [Main PDF p. 8, Limitations first paragraph](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8) | REPORT | Trial stopped early after meeting a prespecified Bayesian effectiveness rule. This corroborates stopping and does not define a different interim population. |

**Consistency rule applicable:** Yes. Focus D and Route B: compare the planned information milestone for the single formal primary efficacy review with its reported information population. This is a statistical decision-point comparison, not a recruitment-calendar difference. The approximate protocol qualifier is preserved; the SAP prints 200 without that qualifier.

**Calculation and display-precision interval check:** Reproduced for 200 versus 309. Planned [199.5,200.5] and reported [308.5,309.5] have gap 108; relative gap 108/200 = 0.54, exceeding 0.05. Exact count difference is 109/200 = 0.545. The rounded 97% benefit probability interval [96.5%,97.5%] exceeds the rounded 95% interval [94.5%,95.5%]; if the threshold is exact, 97% also exceeds 95%. The stopping-probability comparison reconciles and is not an additional candidate. Final 159 + 149 = 308 outcomes is a different analysis-time population and is not substituted for 309.

**Necessary inputs available:** Yes for the planned/reported information-count comparison and stated efficacy threshold. **Exact missing inputs or definitions:** Exact participant-level interim dataset, definition of data available at that look, operational scheduling explanation, and any further information-milestone amendment are not supplied. They are needed to explain the change or reconstruct the interim result, not to observe it.

**Source-grounded alternative interpretation:** A delayed formal review could increase the available records; available data could have a different operational definition; a further unsupplied amendment could apply. The supplied amended history and later SAP do not establish these explanations. No failure of the >95% stopping guideline is claimed.

**Direct observation versus inferred explanation:** Printed planned 200/approximately 200 and reported 309 are directly observed. Operational delay, changed definition or amendment is a possible explanation, not a supplied fact.

**Classification confirmation:** P_R; All relationships P_R; protocol_report. The plans agree on the 200 milestone and the report locations agree on stopping; they supply no P_P or S_W conflict. No classification change. The approximate qualifier and possible unsupplied amendment are retained as bounded ambiguity.

**Evidence state:** reproduced. Determining fact: the SAP's formal 200-outcome milestone and article's formal 309-infant look remain separated by a relative interval gap of 0.54.

**Exact remaining human question:** How was the planned 200-infant formal interim milestone implemented or amended to the reported look with data available for 309 infants, and what exact population generated its 97% primary-benefit probability?

## C005 — Planned Primary and Key-Secondary Analyses Without Supplied Reported Counterparts

**Location found; source text and report comparator matched:** Yes. Every listed prospective statement was reread in its source-page image. Absence is bounded to both complete supplied REPORT documents, independently searched and read across all 18 physical pages; it is not inferred from a missing keyword alone.

| Exact planned location | Role by content | Confirmed specification |
|---|---|---|
| [SAP PDF p. 4, lines 133–149](../../../joi240020supp2_prod_1710443209.75411.pdf#page=4) | PLAN | Complementary frequentist/Bayesian analyses for primary SAE and important secondary death, hospital days and BSIDIII; effect estimates and uncertainty intervals, Bayesian probabilities. |
| [SAP PDF p. 5, lines 163–166](../../../joi240020supp2_prod_1710443209.75411.pdf#page=5) | PLAN | mITT and PP populations; PP includes infants receiving their randomized intervention with determined primary outcome. |
| [SAP PDF p. 8, lines 269–276](../../../joi240020supp2_prod_1710443209.75411.pdf#page=8) | PLAN | Outcome-specific effects and intervals; probabilities of any effect and at least 3% and 5% SAE risk reduction. |
| [SAP PDF p. 9, lines 315–347](../../../joi240020supp2_prod_1710443209.75411.pdf#page=9) | PLAN | Primary PP analysis will be done; primary/hospital-day modifiers include maternal education ≤12 years, prenatal care, difficult-to-reduce hernia, sex and race/ethnicity; additional approach/distance analyses; continuous-GA association followed by treatment interaction. |
| [Protocol PDF p. 13, lines 490–500](../../../joi240020supp1_prod_1710443209.74911.pdf#page=13) | PLAN | Primary/secondary modifiers GA, BPD, education, prenatal care and reducibility, with sex and race/ethnicity analyses; point estimates, 95% CrIs and benefit/harm probabilities. |
| [SAP PDF p. 2, lines 28–37](../../../joi240020supp2_prod_1710443209.75411.pdf#page=2) | PLAN | Planned analyses may be included in future manuscripts as the subcommittee deems necessary. This is an explicit alternative publication scope, not a reported result. |

**Completed report-side location search:** All locations below are REPORT by completed trial content. Result-supplement native glyph corruption was resolved by viewing every readable page image. The article's compared result pages were visually read; its remaining non-result text was read in source-matched layout extraction.

| Exact REPORT location | Content inspected and absence result |
|---|---|
| [Main PDF p. 1](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1) | Abstract: primary complete-outcome analysis, any-benefit probability, overall hospital days and GA/BPD subgroup benefits. No named missing counterpart. |
| [Main PDF p. 2](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=2) | Key Points, rationale, eligibility, intervention and randomization. No named missing counterpart. |
| [Main PDF p. 3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3) | Flow, randomization and outcomes. Flow gives available-outcome primary 159/149, not an additional PP analysis. |
| [Main PDF p. 4](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4) | Methods identify completed GA/BPD/approach modifiers; developmental assessment explicitly ongoing; statistical models/any-benefit and interim described. No named missing counterpart. |
| [Main PDF p. 5](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5) | Baseline Table 1 and surgery characteristics. Baseline sex/race and operation descriptions are not modifier results or PP effects. |
| [Main PDF p. 6](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6) | Table 2/Figure 2 and primary/secondary results: primary 159/149 with 97% any-benefit; overall hospital RR 0.91/82%. No PP, ≥3%/≥5%, continuous-GA, remaining modifiers or modeled death counterpart. |
| [Main PDF p. 7](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7) | Table 3 death 2 (1.3%) versus 3 (2.0%), descriptive event narratives and primary GA/BPD/approach heterogeneity. No modeled death or remaining planned counterpart. |
| [Main PDF p. 8](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8) | Figure 3 gives only primary GA/BPD/approach subgroups and overall effect; discussion, limitations, conclusion and author list. No named missing counterpart. |
| [Main PDF p. 9](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=9) | Affiliations, contributions, disclosures, funding, acknowledgments and references. No named missing counterpart. |
| [Main PDF p. 10](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=10) | References. No named missing counterpart. |
| [Results supplement PDF p. 1](../../../joi240020supp3_prod_1710443209.75411.pdf#page=1) | Contents lists enrollment, frequentist primary/major-secondary table, centers and acknowledgments. |
| [Results supplement PDF p. 2](../../../joi240020supp3_prod_1710443209.75411.pdf#page=2) | eTable 1 enrollment reasons. No named missing counterpart. |
| [Results supplement PDF p. 3](../../../joi240020supp3_prod_1710443209.75411.pdf#page=3) | eTable 1 enrollment/refusal continuation. No named missing counterpart. |
| [Results supplement PDF p. 4](../../../joi240020supp3_prod_1710443209.75411.pdf#page=4) | eTable 1 continuation. No named missing counterpart. |
| [Results supplement PDF p. 5](../../../joi240020supp3_prod_1710443209.75411.pdf#page=5) | eTable 2: primary 159/149 and overall hospital-day frequentist effects, plus model footnote. No named missing counterpart. |
| [Results supplement PDF p. 6](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6) | eTable 3 center enrollment. No named missing counterpart. |
| [Results supplement PDF p. 7](../../../joi240020supp3_prod_1710443209.75411.pdf#page=7) | Acknowledgments/personnel. No named missing counterpart. |
| [Results supplement PDF p. 8](../../../joi240020supp3_prod_1710443209.75411.pdf#page=8) | Acknowledgments continuation. No named missing counterpart. |

**Consistency rule applicable:** Yes. Focus D and Route A category 5, planned primary/key-secondary analyses not reported. Primary PP, clinically important SAE reduction probabilities, primary modifiers and continuous-GA analyses explicitly analyze the primary endpoint. Hospital days appear in the abstract, and death is explicitly designated important secondary in the SAP. Their planned inference is within the comparison tier. One repeated nonreporting pattern retains every specification.

**Logical comparison and display-precision check:** Reproduced separately for (1) primary PP population/effect; (2) probabilities of at least 3% and 5% SAE reduction; (3) primary education/prenatal-care/reducibility/sex/race-ethnicity/distance modifiers; (4) hospital-day modifier effects; (5) continuous-GA SAE association and treatment interaction; (6) modeled important-secondary death effects/uncertainty/probabilities. None has a printed counterpart in the supplied REPORT pages. The 97% any-benefit probability is a different event from ≥3%/≥5% reduction; GA categories are distinct from continuous GA; raw death counts do not supply model effects and uncertainty. No half-unit interval or relative numerical discrepancy applies to qualitative absence. The printed threshold numbers identify the specified probability events; the issue is not their rounding.

**Necessary inputs available:** Yes: unconditional planned statements, outcome hierarchy, complete article and complete results supplement. **Exact missing inputs or definitions:** Result/status/location for each named output, PP population/effect, threshold probabilities, omitted modifiers, continuous-GA specification/result and modeled death uncertainty/probabilities are not supplied. Additional publications, final amendments and code/data are absent; the review does not establish whether any analysis was conducted.

**Conditional and deferred analyses distinguished:** SAP p. 9 lines 311–314 makes imbalance-adjusted sensitivity conditional on important baseline imbalance; article p. 4 says no other clinically important baseline differences. That conditional analysis is outside the retained pattern. At the initial recheck stage, article p. 4 ongoing developmental assessment was retained as an exclusion. The independently screened pass-2 extension below supersedes that scope decision under Route A category 5 while preserving the explicit ongoing status. SAP p. 2 permits later manuscripts; no supplied statement specifically assigns the six retained groups of analyses to a deferred publication. No prediction-tool output or peripheral secondary analysis is added.

**Source-grounded alternative interpretation:** Outputs may appear in unsupplied later manuscripts, may have been replaced, may have remained unperformed or may have been omitted from publication under the SAP's discretion. No choice among these explanations is asserted.

**Direct observation versus inferred explanation:** Explicit prospective specifications and lack of corresponding outputs in the complete supplied REPORT set are direct bounded observations. Nonconduct, replacement, omission or later publication is an unestablished explanation.

**Classification confirmation:** P_R; All relationships P_R; protocol_report. This compares PLAN specifications with REPORT output coverage. Two REPORT documents consistently lacking an output do not create S_C; corroborating plan statements do not add P_P. No classification change. Ambiguity concerns later publication/status, not document role.

**Evidence state:** reproduced. Determining fact: every named retained planned analysis has no result counterpart after independent complete 10-page article and 8-page results-supplement inspection, while conditional/deferred analyses are explicitly distinguished.

**Exact remaining human question:** Where are the planned primary PP result, ≥3%/≥5% SAE benefit probabilities, remaining primary modifiers and continuous-GA analyses, hospital-day modifier results and complementary modeled death analyses reported, or which were deferred, replaced or not conducted under the final plan?

### Pass-2 developmental extension — independently rechecked

**Prominent source context:** [Main PDF p. 4, Outcomes, left column](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4) explicitly states that the 2-year neurocognitive assessment is ongoing and identifies the Bayley third-edition cognitive composite at 2 years' corrected age. This is a directly observed explanation for the absence of developmental outputs in this report. Assessment completion, an observed developmental effect, a missed deadline and a requirement that these results already exist are not inferred. [SAP PDF p. 2, lines 28–37](../../../joi240020supp2_prod_1710443209.75411.pdf#page=2) also permits planned analyses in future manuscripts as deemed necessary by the HIP subcommittee.

**Evidence state:** reproduced. The determining recheck fact is that the supplied plan explicitly specifies important-secondary BSIDIII overall and modifier inference, while neither complete supplied REPORT document contains its effect estimates, uncertainty intervals or posterior probabilities. The directly confirmed ongoing-status statement remains part of that evidence. No registered source value or location required transcription correction.

**Classification:** Review domain protocol_report; primary relationship P_R; All relationships P_R. Compared roles are PLAN protocol and PLAN SAP developmental specifications versus REPORT main article and REPORT results supplement coverage. Each role is confirmed from its content: the protocol/SAP make prospective assessment and analysis commitments; the article and eTables present observed trial results. There is no classification change. P_R is the applicable highest-precedence type. Agreeing PLAN statements merely corroborate the specifications, and agreeing REPORT coverage merely corroborates absent outputs; these do not supply P_P, S_C or S_W. The disclosed ongoing assessment and prospective publication discretion create a bounded reporting-status question, not a role ambiguity or a demonstrated amendment.

#### Exact PLAN locations found and source statements matched

Every row was found at the stated physical PDF page and printed line locations. All rows have document role PLAN by content. The comparator for each required developmental output is the complete REPORT search recorded below.

| Exact supplied-source location | Source value/text matched and comparison function |
|---|---|
| [SAP p. 2, lines 28–37 and 44–58](../../../joi240020supp2_prod_1710443209.75411.pdf#page=2) | Future-manuscript discretion is explicit. The objective compares early versus late repair neurodevelopment using cognitive composite BSIDIII scores at 22–26 months corrected age; this establishes the treatment comparison and supports later separate reporting as an alternative. |
| [SAP p. 4, lines 116–117 and 129–149](../../../joi240020supp2_prod_1710443209.75411.pdf#page=4) | Neurodevelopmental outcomes are collected at 22–26 months corrected age. BSIDIII is explicitly among important secondary outcomes receiving complementary frequentist and Bayesian analyses. Planned frequentist outputs include group-mean differences and 95% CIs; Bayesian outputs include posterior medians, 95% CrIs and intervention benefit/harm probabilities. The 0.4 SD/6-point planned difference assuming 200 assessed infants is a sample-size assumption, not an observed result. |
| [SAP p. 8, lines 267–276](../../../joi240020supp2_prod_1710443209.75411.pdf#page=8) | Continuous outcomes use normal regression with site random intercept and GA group, <28 versus ≥28 weeks, as a covariate. Mean-group differences, 95% CIs/CrIs and any-effect benefit/harm probabilities are specified. The 3% and 5% clinically important reduction thresholds in this paragraph specifically concern SAE risk; they are not assigned to the developmental score. |
| [SAP p. 9, lines 318–332](../../../joi240020supp2_prod_1710443209.75411.pdf#page=9) | BSIDIII scores are expressly included in Bayesian hierarchical treatment-modifier analyses. Named moderators are GA <28 versus ≥28 weeks, BPD, maternal education ≤12 years, prenatal care and difficult-to-reduce hernia. Subgroup treatment estimates, 95% CrIs and benefit/harm probabilities are specified, with similar analyses for sex and race/ethnicity. These are the seven modifier dimensions retained in the independently included extension. |
| [Protocol p. 12, lines 413–448 and 462](../../../joi240020supp1_prod_1710443209.74911.pdf#page=12) | Developmental follow-up at 22–26 months, cognitive composite comparison, assessment access and funding qualifications are explicit. Initial limited funding for 200 participants and voluntary/eligibility qualifications do not establish an observed developmental denominator. The composite scale has SD 15; 0.4 SD is stated as six points for the planned comparison. |
| [Protocol p. 13, lines 463–465 and 481–484](../../../joi240020supp1_prod_1710443209.74911.pdf#page=13) | The developmental sample-size statement continues with 200 assessed infants at 22–26 months. A linear mixed model for BSIDIII uses treatment and GA covariates and random center; continuous-outcome absolute differences and 95% CIs are specified. |
| [Protocol p. 13, lines 490–500](../../../joi240020supp1_prod_1710443209.74911.pdf#page=13) | BSIDIII is expressly included in treatment-modifier models. The five core moderators and similar sex/race-ethnicity analyses match the named SAP dimensions, with point estimates, 95% CrIs and benefit/harm probabilities. This corroborates the planned developmental modifier outputs; it does not introduce a plan-internal conflict. |

**Extraction/source distinction:** Direct native text on SAP p. 9 and protocol p. 13 drops the underline in some inequality glyphs, rendering maternal education as <12 and the upper GA stratum as >28. The source page images visibly print maternal education ≤12 and GA ≥28. The ledger already uses the image-confirmed education threshold, so this is an extraction limitation handled by visual confirmation, not a correction to registration or a separate reporting issue.

#### Complete REPORT comparator search and locations found

The full absence search covered main physical pp. 1–10 and results-supplement physical pp. 1–8, totaling 18 of 18 REPORT pages. Each page was independently reread. Main article text was read directly from the supplied PDF in bounded exact-page layout extractions; p. 4 was also visually confirmed. Every results-supplement page was freshly rendered from its supplied PDF and visually read because its native text glyphs are unsuitable for this comparator. Search/read targets were the overall early-versus-late cognitive-composite strategy effect, frequentist estimate/95% CI, Bayesian posterior median/95% CrI/benefit-harm probability and the seven named developmental modifier dimensions. Neither source provides any of those developmental inferential outputs.

| Exact supplied-source page | Role by content | Content found and comparator matched |
|---|---|---|
| [Main p. 1](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=1) | REPORT | Abstract reports SAE, hospital-day and primary subgroup results; no developmental effect, interval, probability or modifier output. |
| [Main p. 2](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=2) | REPORT | Key Points, rationale, design, eligibility and interventions. Neurodevelopment occurs in eligibility context, without a treatment-comparison result. |
| [Main p. 3](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=3) | REPORT | Flow diagram, randomization and primary SAE ascertainment; no developmental inferential output. |
| [Main p. 4, Outcomes and Statistical Analysis](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=4) | REPORT | Explicit ongoing 2-year Bayley cognitive assessment. Methods and beginning of primary results provide no developmental estimate/interval/probability. The ongoing statement is preserved as the direct status comparator. |
| [Main p. 5, Table 1 and surgery characteristics](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=5) | REPORT | Baseline and operative descriptive values; no developmental inferential output. |
| [Main p. 6, Table 2, Figure 2 and primary/secondary results](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=6) | REPORT | SAE and hospital-day effects only. A primary RR or hospital-day effect is a different outcome and cannot stand in for BSIDIII inference. |
| [Main p. 7, Table 3 and heterogeneity](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=7) | REPORT | Serious adverse events and primary SAE subgroup inference, followed by discussion; no overall or modifier developmental inference. |
| [Main p. 8, Figure 3, discussion and end matter](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=8) | REPORT | Figure 3 expressly analyzes SAEs by GA, BPD and operative approach. These are primary-outcome effects, not cognitive-composite effects. Discussion, limitations, conclusions and author list contain no developmental inference. |
| [Main p. 9](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=9) | REPORT | Affiliations, contributions, disclosures, funding, acknowledgment and references; no developmental inferential output. |
| [Main p. 10](../../../jama_blakely_2024_oi_240020_1710443209.74411.pdf#page=10) | REPORT | References only; no developmental inferential output. |
| [Results supplement p. 1, contents](../../../joi240020supp3_prod_1710443209.75411.pdf#page=1) | REPORT | Contents lists enrollment information, frequentist primary/major-secondary analyses, center information and acknowledgments. No developmental display is listed or present. |
| [Results supplement p. 2, eTable 1](../../../joi240020supp3_prod_1710443209.75411.pdf#page=2) | REPORT | Enrollment/exclusion reasons; no developmental inference. |
| [Results supplement p. 3, eTable 1 continuation](../../../joi240020supp3_prod_1710443209.75411.pdf#page=3) | REPORT | Enrollment and refusal reasons; no developmental inference. |
| [Results supplement p. 4, eTable 1 continuation](../../../joi240020supp3_prod_1710443209.75411.pdf#page=4) | REPORT | Enrollment-reason continuation; no developmental inference. |
| [Results supplement p. 5, eTable 2 and model notes](../../../joi240020supp3_prod_1710443209.75411.pdf#page=5) | REPORT | Frequentist SAE and hospital-day estimates, intervals and P values only; no developmental overall/modifier inference. |
| [Results supplement p. 6, eTable 3](../../../joi240020supp3_prod_1710443209.75411.pdf#page=6) | REPORT | Enrollment by center; no developmental inference. |
| [Results supplement p. 7](../../../joi240020supp3_prod_1710443209.75411.pdf#page=7) | REPORT | Committee and personnel acknowledgments; no developmental inference. |
| [Results supplement p. 8](../../../joi240020supp3_prod_1710443209.75411.pdf#page=8) | REPORT | Personnel acknowledgments continuation; no developmental inference. |

#### Rule, logical reproduction and display precision

**Consistency rule applicable:** Yes. Focus D and Route A, category 5 apply to a planned primary or key secondary analysis without a reported counterpart. The SAP's explicit important-secondary designation for BSIDIII establishes the eligible comparison tier. The planned objects are analyses and their specified quantitative outputs, rather than a general preference for another analysis or an isolated undocumented model detail.

**Logical comparison reproduced:** Yes. The plan contains the BSIDIII overall treatment comparison and specified modifier inference; the complete supplied report package contains no matching quantitative output. Matching was required on outcome, treatment comparison and inferential object. Ongoing-assessment disclosure is found, but it is a status statement rather than an effect estimate, uncertainty interval or posterior probability. The absence observation is bounded to this package. Under the specified category-5 rule, disclosed ongoing assessment remains context and does not supply a numerical counterpart. The completed REPORT search does not imply completed developmental follow-up.

**Display-precision interval check:** Inapplicable to the registered qualitative absence comparison: there are no two printed developmental effects or recomputable developmental results to place in rounding intervals, and no numeric relative discrepancy is assigned. The linked sample-size inputs themselves reconcile: 0.4 × 15 = 6 points. As a separate nonconflicting contextual check, [0.35, 0.45] × [14.5, 15.5] gives [5.075, 6.975], overlapping the displayed six-point interval [5.5, 6.5]; gap and relative discrepancy are zero. This check concerns intended sample-size assumptions only and supplies no observed cognitive effect.

#### Inputs, alternatives, observations and remaining question

**Necessary inputs available:** Yes for the bounded mechanical comparison: explicit named developmental outcome and important-secondary status, prospective overall and subgroup analysis/output specifications, exact assessment-window/status statements and both complete supplied REPORT documents. The comparison needs no raw data or model re-fit.

**Exact missing inputs or definitions:** The supplied package does not provide developmental assessment completion/status after this report, actual assessed or analyzed developmental denominators, implemented overall/modifier analysis output, treatment effects or intervals/probabilities, a later developmental manuscript location, or an amendment/reporting decision identifying any deferred or replaced developmental analysis. Those inputs are needed to answer eventual availability or implementation questions, not to observe the absence in these 18 supplied report pages. No developmental-specific clinically important threshold is inferred from the SAE-specific 3%/5% thresholds.

**Source-grounded alternative interpretation:** Deferred developmental reporting while assessment continues is directly supported by main p. 4. The SAP's future-manuscript discretion supports separate later publication. Protocol p. 12 also describes funding, access, consent and eligibility qualifications for assessment, preventing an assumption that every randomized infant underwent the developmental assessment. No later publication is supplied. These sources support a reporting-status explanation without establishing completion, nonconduct, an overdue result, an observed treatment direction or a need to change the analysis.

**Direct observation versus inferred explanation:** Direct observations are the prospective important-secondary and modifier specifications, the explicit ongoing status and the absence of matching quantitative outputs from both complete supplied REPORT documents. Deferred reporting is source-supported; eventual result availability and actual analysis conduct remain unknown. The only inference used in classification is matching prospective specified outputs to supplied report coverage. No causal explanation for absence beyond disclosed context is established.

**Exact remaining human question:** Given the report's explicit statement that the 2-year neurocognitive assessment is ongoing, what is the reporting status or later result location of the planned important-secondary BSIDIII early-versus-late strategy-effect and developmental modifier estimates, intervals and posterior probabilities?

#### Source handling and limitations

Recorded tools/device: direct Poppler pdfinfo, pdftotext and pdftoppm 26.01.0; CPU; fallback NOT_NEEDED. Main source page count was directly confirmed as 10 and results-supplement count as 8. Native source-page text was read to stdout, with no extraction derivative written. Current exact-page images used for visual source confirmation were preprocessing/initial_screen/sap-p4.png, preprocessing/support_mapping/DOC-003-p8.png and DOC-003-p9.png, and preprocessing/cross_source_checks/main-p4.png. Source image glyphs took precedence over native transcription wherever they differed.

Ten unique fresh derivatives were created only below preprocessing/extension_recheck/: results-1.png, results-2.png, results-3.png, results-4.png, results-5.png, results-6.png, results-7.png, results-8.png, protocol-12.png and protocol-13.png. All were visually inspected. Engine: direct Poppler pdftoppm 26.01.0; compute device CPU. Commands: `pdftoppm -f 1 -l 8 -scale-to 1700 -png joi240020supp3_prod_1710443209.75411.pdf .ai_paper_validation/review_1_6_2/preprocessing/extension_recheck/results` and `pdftoppm -f 12 -l 13 -scale-to 1900 -png joi240020supp1_prod_1710443209.74911.pdf .ai_paper_validation/review_1_6_2/preprocessing/extension_recheck/protocol`. No OCR or Python helper was needed.

There is no assigned-source location or REPORT-page coverage gap. Later developmental results, raw data, implementation code and reporting updates remain unavailable and limit claims about eventual reporting or conduct. The canonical recheck, ledger, screening and manifest were not modified by this agent. Classification is unchanged and the extension evidence state is reproduced; these are evidence-record facts, with no adjudication assigned.

## C006 — Protocol Hospital-Day Median Assumptions

**Location found; source and comparator matched:** Yes at every registered and related location.

| Exact supplied-source location | Role by content | Directly confirmed content and comparison function |
|---|---|---|
| [Protocol PDF p. 3, lines 105–109](../../../joi240020supp1_prod_1710443209.74911.pdf#page=3) | PLAN | Hospital-day hypothesis prints a three-day median reduction, with 18 early versus 15 late hospital days. |
| [Protocol PDF p. 12, lines 460–462](../../../joi240020supp1_prod_1710443209.74911.pdf#page=12) | PLAN | Hospital power assumptions explicitly distinguish median 8/5 from mean 18/13, with lognormal distribution and 98% power for a three-day median difference. |
| [SAP PDF p. 3, lines 73–80](../../../joi240020supp2_prod_1710443209.75411.pdf#page=3) | PLAN | Hospital hypothesis gives medians 8/5 and expressly clarifies the protocol p. 3 pair by pointing to the protocol p. 12 inputs. The intended median pair is supplied, not inferred. |
| [Protocol PDF p. 13, Table 4](../../../joi240020supp1_prod_1710443209.74911.pdf#page=13) | PLAN | Three-day median-difference column gives hospital power 98%, 97%, 92%, 81% at 293, 250, 200, 150 infants/group. Related power output only. |
| [SAP PDF p. 4, lines 114–115](../../../joi240020supp2_prod_1710443209.75411.pdf#page=4) | PLAN | Repeats hospital 98% power, medians 8/5, means 18/13 and lognormal assumption. Corroborates the intended inputs. |

**Consistency rule applicable:** Yes. Focus D, permitted plan-internal sample-size/power assumptions, and Route A category 2. The source-confirmed arm-specific median magnitudes differ beyond display precision. The supplied clarification identifies intended inputs but does not remove a reproduced magnitude-changing printed-value comparison under the always-register category. CONTEXT_RESOLVES is not applicable to that category. This is not a new claim about the power algorithm.

**Calculation and display-precision interval check:** Reproduced. Early median 18 interval [17.5,18.5] versus 8 interval [7.5,8.5]: gap 9 days, relative 9/18 = 0.5. Late median 15 interval [14.5,15.5] versus 5 interval [4.5,5.5]: gap 9 days, relative 9/15 = 0.6. Both exceed 0.05. Exact median gaps are 10 days per arm. Both pairs have an exact three-day early-minus-late contrast; conservative contrast intervals are [2,4] for both pairs, gap zero. Agreement in the contrast does not reconcile the two arm-specific input magnitudes. Printed means 18/13 are separately labeled and do not equal the 18/15 median pair.

**Necessary inputs available:** Yes for both median comparisons, labels and explicit clarification. **Exact missing inputs or definitions:** None needed to identify the intended 8/5 medians; the SAP supplies them expressly. The power test/algorithm is not named, and no code is supplied; those inputs would be needed to regenerate 98% and the entire power table, which is outside this registered comparison.

**Source-grounded alternative interpretation:** The SAP establishes intended 8/5 medians for the hypothesis/power assumptions. Human extraction may rely on that clarification while documenting the protocol's printed 18/15 pair. Both pairs preserve the three-day contrast. No final replacement or human disposition is assigned here.

**Direct observation versus inferred explanation:** Both protocol median pairs, the labeled mean pair and the SAP clarification are direct observations. A specific production mechanism for the original pair is not observed; no numerical conflict in the power algorithm is inferred.

**Classification confirmation:** P_P; All relationships P_P; plan_material. The inconsistency is solely within PLAN protocol content; the PLAN SAP corroborates one side and supplies explicit clarification, without creating a REPORT relationship. No classification change or document-role ambiguity.

**Evidence state:** reproduced. Determining fact: source images confirm median 18/15 in one protocol section and median 8/5 in another, with relative interval gaps 0.5/0.6; the SAP's explicit clarification is retained as evidence of intended inputs, without treating it as deletion of the printed-value observation.

**Exact remaining human question:** How should the protocol's printed 18/15 median assumptions and the SAP's explicit identification of intended 8/5 medians be represented when extracting the planned hospital-day hypothesis and power inputs?

## Evidence Handling, Tools and Remaining Limits

No new extraction, rendering or OCR derivative was necessary. Compute device followed tooling_record.md: CPU; fallback NOT_NEEDED. Current source-matched images and existing source-linked renders were inspected without modification. Current image producers recorded direct Poppler pdftoppm 26.01.0/CPU. Historical reused image-engine versions are not recorded; those images were source-linked locators/readings, not independent scientific comparators. The current source-matched full article layout and plan layout were used only for text location/context. No source, reused asset or another agent's output was modified.

Visually inspected main pages: 1, 3, 4, 5, 6, 7, 8. Main pages 2, 9, 10 were read in source-matched layout text for the bounded absence check. Visually inspected protocol pages: 3, 12, 13, 14, 25. Visually inspected SAP pages: 2, 3, 4, 5, 7, 8, 9. Visually inspected results-supplement pages: 1, 2, 3, 4, 5, 6, 7, 8. All physical source-page links above use truthful #page=N locations. Repeated patterns retain every registered occurrence.

There is no unresolved source-location or transcription coverage gap for the six assigned IDs. Remaining human questions are bounded to the population/window, plan precedence and replaced models, implemented priors, interim population/amendment, absent-output status/location, and representation of explicitly clarified median assumptions. Participant-level records, model code/posterior draws, convergence diagnostics, additional amendments and later manuscripts are not supplied. Their absence limits causal/implementation explanation and raw-data reconstruction, without changing the recorded mechanical evidence states.
