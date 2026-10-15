# Mechanical Evidence Recheck

Scope: C001, C002, C003, C004, C005, C006. Each stable ID remains Pending Human Adjudication. This artifact records source-confirmation and classification facts, not a disposition.

The recheck read the current candidate ledger, current independent screen/source notes and current factual maps as locators, then independently opened the cited supplied-source PDF pages as images. Neither OCR nor an earlier assessment was treated as final authority. No pre-existing workflow 1.6.2 scientific artifact was used. No source or reused artifact was modified.

## Source authority and tooling

Document roles follow the content actually compared. The main article, non-plan results supplement, and main-analysis implementation code are REPORT. The trial-protocol versions and SAP/addendum are PLAN: their compared passages prescribe future analyses even though the SAP carries a Final Report header. A prospective SAP is not reclassified as REPORT merely because of that header.

The following current-run source renderings were independently opened with the local image viewer. Source authority is the PDF page represented, not its OCR transcription:

- Main article PDF pages 3, 4, 5, 6 in preprocessing/statistical_current/main-03.png through main-06.png, and page 7 in preprocessing/initial_screen/main-07.png.
- Protocol PDF pages 10, 39, 56, 70 in preprocessing/initial_screen/protocol-10.png, protocol-39.png, protocol-56.png, protocol-70.png; pages 86, 87 in preprocessing/statistical_current/protocol-86.png, protocol-87.png.
- SAP PDF pages 4, 5, 10, 11, 12, 15 in preprocessing/statistical_current/sap-04.png, sap-05.png, sap-10.png, sap-11.png, sap-12.png, sap-15.png; pages 6, 7 in preprocessing/initial_screen/sap-06.png, sap-07.png.
- Results PDF pages 7, 13, 15, 25 in preprocessing/statistical_current/results-07.png, results-13.png, results-15.png, results-25.png; pages 12, 14, 18 in preprocessing/current_support/cross-results-12.png, cross-results-14.png, results-18.png; page 27 in preprocessing/initial_screen/results-27.png.
- Main-analysis code PDF page 1 in preprocessing/statistical_current/code-01.png.
- Results contents PDF page 1 freshly rendered to preprocessing/recheck-results-01.png by the recorded pinned fallback: `.ai_paper_validation/review_1_6_2/tooling/venv/bin/python workflow_1_6_2/scripts/pdf_tools.py render joi250066supp3_prod_1761597796.4701.pdf --page 1 .ai_paper_validation/review_1_6_2/preprocessing/recheck-results-01.png`. Engine: PyMuPDF 1.26.4, 200 dpi, CPU. No additional extraction or OCR was necessary.

The union is 29 distinct source pages. Repeated use of one page in different candidate records below denotes separate comparisons, not additional source pages. The existing current rendering provenance is recorded in screening/initial_source_notes.md and tooling_record.md. All processing used CPU.

## Classification and evidence-state register

| ID | Evidence state | Review domain | Relationship type | All relationships | Classification result |
|---|---|---|---|---|---|
| C001 | reproduced | statistical_results | S_W | S_W | Retained: domain/scalar mapping within the main REPORT; supplement and protocol are corroboration/context only. |
| C002 | reproduced | protocol_report | P_R | P_R, P_P | Retained: protocol versus report primary population, and protocol versus SAP population specification; P_R has precedence. |
| C003 | reproduced | protocol_report | P_R | P_R, P_P | Retained: protocol versus report implementation and protocol versus SAP model specification; P_R has precedence. |
| C004 | reproduced | protocol_report | P_R | P_R | Retained: SAP versus disclosed report secondary missing-data procedures. |
| C005 | reproduced | protocol_report | P_R | P_R | Retained: planned primary-endpoint supplementary outputs are not identified in the supplied report materials. |
| C006 | reproduced | statistical_results | S_W | S_W | Retained: parent/component event counts within the main REPORT table. |

No registered transcription or source-page assignment required replacement. No document-role, relationship or domain change is required by the recheck. The distinctions below bound what each evidence state establishes.

## C001 — PROMIS-29 scalar scoring and direction

**Evidence state:** reproduced

**Determining recheck fact:** The main article defines seven differently oriented domain scores, each with raw range 4–20, but its quantitative result is a single PROMIS-29 mean and a single adjusted difference without a mapping from the domains to that scalar or its direction. The recheck reproduces that incomplete quantitative definition; it does not establish an out-of-range score.

**Locations found and source/comparator matched:**

| Exact supplied-source location | Role by content | Directly matched content and comparison function |
|---|---|---|
| [Main PDF page 3, Secondary Outcomes](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3) | REPORT | PROMIS-29 comprises 7 domains with 4 items each; raw range 4–20 points per domain; higher scores reflect better functioning in some domains and worse functioning in others. This is the report's score definition. |
| [Main PDF page 6, Secondary Outcomes](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) | REPORT | One mean (SD): levodopa 66 (14), placebo 65 (14); one adjusted mean difference −0.37 points, 95% CI −3.34 to 2.61. This is the scalar result to which the domain definition must be connected. |
| [Results PDF page 15, eTable 4 PROMIS 29 row](../../../joi250066supp3_prod_1761597796.4701.pdf#page=15) | REPORT, corroborating | Placebo 65.11 (13.79), levodopa 64.74 (14.33), SMD 0.026, difference −0.37 [−3.34, 2.61], n=582. This independently confirms a single scalar row and matching adjusted effect, but does not supply its construction. |
| [Protocol PDF page 70, PROMIS assessment](../../../joi250066supp1_prod_1761597796.4601.pdf#page=70) | PLAN, contextual | Population mean 50 and SD 10 are discussed for each scale. Seven 4-question domains plus a pain-intensity item on 0–10 are described. No explicit mapping identifies which transformation or aggregate produced the reported scalar. |

**Consistency rule applicable:** Focus area C, Route B: a printed multidomain, mixed-direction definition cannot be connected uniquely to the printed scalar outcome. The specific extraction at issue is the scale and favorable direction of the −0.37 [−3.34, 2.61] adjusted result. This is a result-linked scoring-definition gap, not an assertion that an unspecified model option should have been supplied.

**Logical comparison and display precision:** A function mapping the described domains to one scalar is necessary to determine what an increment means. No such function is printed at these locations. Rounding cannot supply an aggregation, recoding rule, domain identity or direction, so the registered logical comparison has no numeric discrepancy interval or relative-gap statistic. A comparison of 66 against an individual domain's upper limit 20 is inapplicable: the report does not call 66 a raw individual-domain score. It must not become an out-of-range assertion. For the corroborating scalar copies, main levodopa 66 has interval [65.5, 66.5], whereas supplementary 64.74 has [64.735, 64.745]; their gap is 0.755, relative gap 0.755/66=0.0114394, within the scope's display-precision tolerance. Placebo [64.5, 65.5] overlaps [65.105, 65.115], gap 0. The adjusted differences have the identical half-unit interval [−0.375, −0.365], and both CI limits also match to their displayed precision. These copy checks do not add an S_C relationship.

**Necessary inputs available:** Domain count, raw domain ranges, mixed direction statement, scalar summaries, adjusted effect and interval. **Exact missing inputs or definitions:** The actual scalar variable, included domains/items, transformation/weighting/aggregation, any reversals, and whether higher scalar scores indicate better or worse status. Individual-level domain scores and scoring code are unavailable, so the scalar cannot be reconstructed from raw data here.

**Alternative source-grounded interpretation:** The scalar might be a raw sum, a transformed domain, or a recoded composite. The protocol's discussion of population mean 50/SD 10 makes transformed scores a possible interpretation but does not identify this result. None is selected by assumption or external scoring conventions.

**Direct observation versus inferred explanation:** The domain definition and scalar row are direct observations. A particular aggregate, transformation, omitted label, or software operation would be an inferred production explanation and is not established.

**Classification:** Compared REPORT main page 3 versus REPORT main page 6; primary relationship S_W, all relationships S_W; statistical_results because this concerns the quantitative outcome and its method of scoring. The supplementary result confirms one scalar, and the protocol offers context rather than conflicting with a specified report scoring rule; neither adds a relationship. **Classification ambiguity:** The exact scalar is unspecified, but the roles of the compared passages are unambiguous.

**Exact remaining human question:** What exact PROMIS-29 variable, domain/item combination, scoring transformation and direction produced the single reported mean and adjusted difference −0.37 [−3.34, 2.61]?

## C002 — Primary analysis population

**Evidence state:** reproduced

**Determining recheck fact:** The protocol assigns the primary analysis to the all-randomized FAS and prescribes multiple imputation for missing data; the SAP explicitly limits deceased participants' contribution to designated supportive strategies, and the report explicitly excludes pre-three-month deaths from its primary n=582 analysis. Death-inclusive n=610 results remain supportive rather than primary.

**Locations found and source/comparator matched:**

| Exact supplied-source location | Role by content | Directly matched content and comparison function |
|---|---|---|
| [Protocol PDF page 86, §§11.4.1–11.4.3](../../../joi250066supp1_prod_1761597796.4601.pdf#page=86) | PLAN | FAS consists of all randomized patients. The final sentence assigns all analyses except sensitivity analyses c/d to FAS; primary §11.4.2 is among them. |
| [Protocol PDF page 87, §11.5](../../../joi250066supp1_prod_1761597796.4601.pdf#page=87) | PLAN | Missing data addressed using multiple imputation by chained equations; complete-case sensitivity. No explicit original numerical death-handling rule is provided here. |
| [SAP PDF page 4, §3.2 and footnote](../../../joi250066supp2_prod_1761597796.4701.pdf#page=4) | PLAN | FAS still all randomized; imputation for survivors; deceased participants not imputed except treatment-policy strategy III. Footnote says deceased remain in FAS but contribute only to policy III and composite strategy. |
| [SAP PDF page 6, §4.3](../../../joi250066supp2_prod_1761597796.4701.pdf#page=6) | PLAN | Treatment-policy strategy is primary; other estimands supportive only. Death before Visit 3 is a listed intercurrent event. |
| [SAP PDF page 7, §§4.3.1–4.3.3](../../../joi250066supp2_prod_1761597796.4701.pdf#page=7) | PLAN | Primary references FAS §3.2; policy III separately includes and imputes participants who died. Read with page 4, not as an isolated all-randomized assertion. |
| [Main PDF page 4, Statistical Analyses](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4) | REPORT | Participants who died before three-month assessment excluded from primary; missing/incomplete FMA imputed for survivors. |
| [Main PDF page 5, Results, Figure 1 and SAP explanation](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) | REPORT | 610 randomized, 307/303; deaths 11/17; 582 eligible primary, 296/286. SAP finalized before database closure, with terminology/estimands explanation. |
| [Results PDF page 12, population definitions](../../../joi250066supp3_prod_1761597796.4701.pdf#page=12) | REPORT | FAS definition explicitly states deaths before three-month assessment excluded from analysis. Death-inclusive estimands described separately. |
| [Results PDF page 13, eTable 2 estimands 1, 3 and 4](../../../joi250066supp3_prod_1761597796.4701.pdf#page=13) | REPORT | Primary estimand 1: n=582, −0.90 [−3.78, 1.98]. Estimand 3 deaths imputed: n=610, −0.98 [−3.77, 1.81]. Composite estimand 4: n=610, 1.06 [0.86, 1.26]. |

**Consistency rule applicable:** Focus area D, Route A category 5: the primary population specified in the protocol is replaced by the survivor primary analysis, with death-inclusive analyses supportive. The comparison concerns primary status and contribution rules, not arithmetic disagreement in participant flow.

**Logical comparison and display precision:** All randomized participants versus survivors before a specified assessment are different membership rules. Half-unit rounding cannot reconcile those categorical rules. The counts corroborate the distinction and reconcile internally: 610−(11+17)=582; 307−11=296; 303−17=286; 296+286=582. Under conservative half-unit intervals, randomized [609.5,610.5] minus deaths [27,29] yields [580.5,583.5], overlapping primary [581.5,582.5]; analyzed arms sum to [581,583], also overlapping that total. Thus numeric discrepancy gap=0 and relative discrepancy=0 for these count checks. The primary-population comparison remains categorical, not a rounded-number finding.

**Necessary inputs available:** The all-randomized FAS definition, assignment of primary analysis to FAS, death exclusions, supportive-strategy designations, and participant totals. **Exact missing inputs or definitions:** The protocol's original post-death numerical FMA rule, a package-supplied amendment explicitly replacing the primary population, and the decision history establishing whether the later SAP was a clarification or change. Raw data are unnecessary to reproduce the printed specification difference.

**Alternative source-grounded interpretation:** FMA is not observed after death, and the SAP/report provide an explicit estimand framework rather than silently dropping the deaths. The prospective SAP may intentionally supersede or clarify the earlier protocol. The report's before-database-closure statement supports that possibility but does not turn the two specifications into the same contribution rule.

**Direct observation versus inferred explanation:** All cited definitions, primary/supportive designations and n values are direct observations. Whether the change was authorized, prospectively amended, or motivated by a particular estimand interpretation is not established by this recheck. No effect of the population change on conclusions is inferred.

**Classification:** PLAN protocol versus REPORT main/results gives P_R; PLAN protocol versus PLAN SAP gives P_P. Both are actual compared specifications, not merely corroborating documents. Primary relationship P_R by precedence; all relationships P_R, P_P; domain protocol_report. Report locations agree with one another, and the SAP's page-4 footnote resolves its own primary FAS reference; no S_C or S_W is added. **Classification ambiguity:** A prospective superseding SAP/amendment could explain the difference, but does not change these document roles.

**Exact remaining human question:** Was the survivor primary population a documented prospective clarification or replacement of the protocol's all-randomized primary analysis, and what was the intended original treatment of deaths for that primary endpoint?

## C003 — Primary mixed-model specification and supplied implementation

**Evidence state:** reproduced

**Determining recheck fact:** The final protocol specifies baseline FMA, treatment and stroke type as fixed terms plus a center random intercept. The SAP, main report and supplied implementation explicitly use baseline-and-treatment linear regression without the stroke-type term or center random intercept.

**Locations found and source/comparator matched:**

| Exact supplied-source location | Role by content | Directly matched content and comparison function |
|---|---|---|
| [Protocol PDF page 56, Statistical Considerations synopsis](../../../joi250066supp1_prod_1761597796.4601.pdf#page=56) | PLAN | Mixed-effects model; baseline, treatment and type of event fixed effects; center random factor. |
| [Protocol PDF page 86, §11.4.2](../../../joi250066supp1_prod_1761597796.4601.pdf#page=86) | PLAN | Baseline covariate, treatment and acute ischemic versus hemorrhagic stroke fixed effects; one random intercept per center. |
| [SAP PDF page 10, §5.2](../../../joi250066supp2_prod_1761597796.4701.pdf#page=10) | PLAN | Linear model with baseline FMA and treatment as two-level variable of interest; no stroke-type or center random-effect term specified. |
| [Main PDF page 4, Statistical Analyses](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4) | REPORT | Linear regression adjusted for baseline FMA, with treatment group as primary variable. |
| [Main PDF page 5, analysis explanation](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) | REPORT | SAP finalized before database closure; describes general alignment and terminology/estimand differences. Does not identify a center random intercept or stroke-type term in the fitted primary model. |
| [Main PDF page 6, Primary Outcome](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) | REPORT, affected result | Baseline-adjusted primary difference −0.90, 95% CI −3.78 to 1.98, P=.54. This is the result attached to the implemented primary analysis. |
| [Code PDF page 1, lines 19–26 and 31–32](../../../joi250066supp5_prod_1761597796.4751.pdf#page=1) | REPORT | Line 23: `lm(fma_affected.Visit_3 ~ fma_affected.Visit_1.cent + medication)`. Model pooling at line 26; diagnostic refit uses the same formula. Implementation confirms the named covariates rather than leaving their absence dependent on narrative brevity. |
| [Protocol PDF page 10, earlier synopsis](../../../joi250066supp1_prod_1761597796.4601.pdf#page=10) | PLAN, historical context | Earlier mixed model includes baseline/treatment and center random factor; no stroke-type fixed effect here. |
| [Protocol PDF page 39, earlier §11.4.2](../../../joi250066supp1_prod_1761597796.4601.pdf#page=39) | PLAN, historical context | Earlier baseline/treatment fixed model with center random intercept. Later protocol pages 56/86 explicitly add stroke type and retain center. |

**Consistency rule applicable:** Focus area D, Route A category 5: a planned primary model is replaced in the supplied primary implementation, and the original mixed-model result is not identified. The explicit code means this does not consist only of a possibly abbreviated model description. Historical protocol versions are context; the comparison uses the final protocol specification.

**Logical comparison and display precision:** Protocol structure is `baseline + treatment + stroke type + center random intercept`; SAP/report/code structure is `baseline + treatment`. These term/variance-structure sets differ. Half-unit intervals and relative numeric discrepancy are inapplicable to model-term membership. The source's primary effect −0.90 [−3.78,1.98], P=.54 is the affected result, not an arithmetic contradiction asserted here. Its displayed effect interval [−0.905,−0.895] lies inside the reported CI, and CI endpoints [−3.785,−3.775]/[1.975,1.985] straddle zero consistently with P∈[.535,.545]. No unprinted coefficient or original-model estimate is reconstructed.

**Necessary inputs available:** Both explicit model specifications and the executable primary formula in the supplied code PDF. **Exact missing inputs or definitions:** A documented decision/amendment replacing the original model, output from that original model if fitted, and raw/imputed datasets needed to quantify any numerical effect of model changes. These missing data do not prevent the specification-set comparison.

**Alternative source-grounded interpretation:** The before-database-closure SAP may be the intended operative specification, superseding the protocol. The report's statement of general alignment may encompass such a change. Neither explanation is treated as proof of an unprinted original mixed-model fit or an unchanged numerical estimate.

**Direct observation versus inferred explanation:** The terms appearing in the protocol/SAP/code are direct observations. Reasons for term removal, center variance magnitude, and effects on standard errors or conclusions would be inferred and are not supplied here.

**Classification:** PLAN final protocol versus REPORT main/code gives P_R; PLAN final protocol versus PLAN SAP gives P_P. Primary P_R by precedence; all relationships P_R, P_P; domain protocol_report. Main and code corroborate one implemented formula and do not conflict, so their being separate REPORT files does not create S_C. **Classification ambiguity:** Possible prospective supersession; no role ambiguity. Historical evolution of the protocol is not counted as a separate model candidate or relationship.

**Exact remaining human question:** Which prospective document replaced the protocol's center random intercept and stroke-type fixed term, and is a result from the originally specified primary mixed model available in the supplied reporting record?

## C004 — Secondary missing-data procedures

**Evidence state:** reproduced

**Determining recheck fact:** SAP §6 says missing secondary outcomes are imputed as for the primary analysis, except harms. The main report expressly says missing mRS and PRAI data were not imputed; the results supplement expressly identifies death-to-mRS-6 assignment and PRAI nonimputation as deviations. These printed rules differ even though the report discloses what it did.

**Locations found and source/comparator matched:**

| Exact supplied-source location | Role by content | Directly matched content and comparison function |
|---|---|---|
| [SAP PDF page 5, §4.2](../../../joi250066supp2_prod_1761597796.4701.pdf#page=5) | PLAN | Lists mRS and patient-reported relevance of motor improvement among secondary outcomes. They are not the outcomes-for-potential-harm exception. |
| [SAP PDF page 11, §6](../../../joi250066supp2_prod_1761597796.4701.pdf#page=11) | PLAN | 100 chained-equation imputations, pooled using Rubin's rules; missing secondary outcomes imputed as for primary; harms not imputed. |
| [Main PDF page 5, secondary methods](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) | REPORT | Secondary summary-score imputation generally; mRS ordinal logistic model; missing mRS and relevance-of-improvement data not imputed. |
| [Results PDF page 7, deviations from SAP](../../../joi250066supp3_prod_1761597796.4701.pdf#page=7) | REPORT | Deceased participants' mRS set to 6 rather than imputed; missing subjective PRAI responses not imputed. |
| [Main PDF page 6, mRS and PRAI results](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) | REPORT | mRS adjusted OR 0.93, 95% CI 0.69–1.23; main PRAI narrative has levodopa 51/276 (18%) and placebo 52/270 (19%). |
| [Results PDF page 15, eTable 4 mRS/PRAI rows](../../../joi250066supp3_prod_1761597796.4701.pdf#page=15) | REPORT | mRS 0.93 [0.69,1.23], n=596. PRAI placebo 51 (18.89%), n=270; levodopa 51 (18.48%), n=276; total n=546. The ledger's 51-per-arm statement matches this table specifically, not the main placebo narrative. |

**Consistency rule applicable:** Focus area D, Route B. Missing-data and analysis-population specifications are in scope; these non-harm secondary procedures have an explicit printed SAP comparator. The applicable result is the mRS OR and the PRAI observed-response proportions/population. Disclosure identifies the reported procedure but does not make imputation, death assignment, and nonimputation equivalent. These ordinary secondary procedures do not independently satisfy category 5's unreported-primary/key-secondary-analysis limb; no outcome-status or composite change is claimed.

**Logical comparison and display precision:** Planned missing-secondary imputation versus reported mRS/PRAI exceptions is categorical; rounding intervals cannot reconcile these rules. No count discrepancy is necessary to reproduce this candidate. The displayed PRAI population reconciles: 270+276=546; half-unit summed interval [545,547] overlaps total [545.5,546.5], gap 0, relative gap 0. Table proportions also reconcile: 100×51/270=18.8889% and 100×51/276=18.4783%. Allowing ±0.5 on those count/denominator inputs gives approximately [18.6691%,19.1095%] and [18.2640%,18.6933%], each overlapping its own printed percentage interval [18.885%,18.895%] and [18.475%,18.485%]. These are checks of the table, not an inference that the main placebo numerator is 51. No S_C relationship is added to this missing-data candidate for that separate numeral.

**Necessary inputs available:** Secondary-outcome status, prospective missing-data rule, reported exceptions and affected result/population counts. **Exact missing inputs or definitions:** Whether surviving participants with missing mRS were omitted or imputed, by-arm missingness/death contributions to mRS n=596, exact PRAI missingness eligibility and any operative amendment/timing for the exceptions. No assumptions are made about individual patient responses or the result under the planned imputation.

**Alternative source-grounded interpretation:** Death-to-mRS-6 follows the main report's definition of 6 as death, and PRAI may intentionally use only observed subjective responses. The supplement explicitly discloses both. The death-only mRS explanation is narrower than the main blanket nonimputation wording, so surviving mRS missingness cannot be inferred from it.

**Direct observation versus inferred explanation:** The general SAP rule and disclosed report deviations are direct. Whether the operative analysis is available case, how non-death missing mRS was treated, and how the estimate would change under another procedure are not established.

**Classification:** PLAN SAP versus REPORT main and results supplement, primary/all P_R, domain protocol_report. Both report documents disclose exceptions, so neither is a conflicting REPORT comparator for this registered pattern. No P_P is added solely because other plan passages corroborate the general SAP approach. **Classification ambiguity:** The scope of surviving-mRS nonimputation and possible prospective amendment remain undefined; document roles are clear.

**Exact remaining human question:** What mRS and PRAI missing-data rules were operative, including surviving participants with missing mRS, and how do those rules account for mRS n=596 and PRAI n=546 relative to the supplied SAP imputation specification?

## C005 — Planned primary-endpoint supplementary outputs

**Evidence state:** reproduced

**Determining recheck fact:** The supplied plan contains an explicit seven-variable primary-endpoint subgroup interaction/forest package, an explicit center-plus-center-by-treatment model, and primary-endpoint additional-covariate sensitivities. The supplied report index and result displays identify estimand sensitivities, a center graph, continuous baseline interaction/spline models and a post hoc fixed-35 severity graph, but not the specified seven-variable forest or the center/covariate model outputs. The reproduced observation is restricted to nonidentification of these planned outputs in this supplied package.

**Locations found and source/comparator matched:**

| Exact supplied-source location | Role by content | Directly matched content and comparison function |
|---|---|---|
| [Protocol PDF page 86, §§11.4.1 and 11.4.3](../../../joi250066supp1_prod_1761597796.4601.pdf#page=86) | PLAN | Primary endpoint sensitivities: graphical center heterogeneity; treatment-by-stroke-type term; added age, sex, dementia, selective hand/wrist movement, cortical dysfunction, fatigue, SSRI treatment, mild extrapyramidal symptoms, reduced impetus; complete-case and PP repeats. PP includes ≥80% prescribed dose or justified reduced dosage, plus rehabilitation attendance. |
| [SAP PDF page 11, §7](../../../joi250066supp2_prod_1761597796.4701.pdf#page=11) | PLAN | Main model to include center and treatment-by-center interaction, in addition to graphical display by center/groups. |
| [SAP PDF page 12, §7.2](../../../joi250066supp2_prod_1761597796.4701.pdf#page=12) | PLAN | Seven subgroup variables: age, sex, distal motor function, cortical dysfunction, SSRI use, stroke type, baseline FMA severity. Use primary estimand and main model plus subgroup and treatment interaction; forest plot. |
| [SAP PDF page 15, subgroup addendum](../../../joi250066supp2_prod_1761597796.4701.pdf#page=15) | PLAN | Hypothesized subgroup directions; age and baseline FMA use <median versus ≥median; other variables have the named categorical cutoffs. |
| [Main PDF page 4, supplementary/post hoc estimands](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4) | REPORT | Seven additional predefined estimands; post hoc death=0 and strict drug-plus-rehabilitation adherence analyses. These identify reported supplementary analyses, not all planned model outputs. |
| [Main PDF page 5, subgroup/center/spline methods](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5) | REPORT | Post hoc ≤35 versus >35 severity groups; post hoc center plot with small centers pooled; post hoc spline/baseline-by-treatment tests. Also says prespecified analyses performed as outlined in SAP. |
| [Main PDF page 6, primary/sensitivity result](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6) | REPORT | Refers to seven additional estimands and post hoc analyses, including the fixed-35 severity subgroup; primary −0.90 [−3.78,1.98]. |
| [Main PDF page 7, Additional Post Hoc Analyses](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=7) | REPORT | Describes nonlinear baseline association and no baseline-treatment interaction; points to supplementary eTables 7/8 and eFigures 6/7. |
| [Results PDF page 1, complete display contents](../../../joi250066supp3_prod_1761597796.4701.pdf#page=1) | REPORT | Lists nine eTables and seven eFigures. Named primary supplementary outputs are estimands, baseline interaction/spline tables, center graph, baseline spline graph and post hoc forest. No separate seven-variable or center-interaction/covariate model result is identified by this complete index. |
| [Results PDF page 13, eTable 2](../../../joi250066supp3_prod_1761597796.4701.pdf#page=13) | REPORT | Eight estimands with n=582,551,610,610,545,496,450,524 and corresponding effects. No subgroup/covariate/center-interaction output columns. |
| [Results PDF page 14, eTable 3](../../../joi250066supp3_prod_1761597796.4701.pdf#page=14) | REPORT | Post hoc change-score, death=0 and combined adherence estimands; no seven-variable subgroup or center-interaction coefficients. |
| [Results PDF page 18, eTables 7 and 8](../../../joi250066supp3_prod_1761597796.4701.pdf#page=18) | REPORT | Continuous centered baseline FMA×treatment model and baseline spline model. No age, sex, distal motor, cortical, SSRI, stroke-type or center interaction terms appear in these displayed tables. |
| [Results PDF page 25, eFigure 5](../../../joi250066supp3_prod_1761597796.4701.pdf#page=25) | REPORT | Patient dots/boxplots stratified by HFR, INS, USB, USZ and other; smaller centers pooled. Supplies the graphical component of the planned center exploration, not the additional center-by-treatment model output. |
| [Results PDF page 27, eFigure 7](../../../joi250066supp3_prod_1761597796.4701.pdf#page=27) | REPORT | Post hoc PH1 death=0, PH2 adherence exclusions, PH3 baseline FMA ≤35/>35. Does not show all seven planned subgroup factors or their specified interaction package. |

**Consistency rule applicable:** Focus area D, Route A category 5: prespecified primary-endpoint supplementary/sensitivity analyses are not identified in supplied results. These are analyses of the primary FMA endpoint, not a broad critique of exploratory research. The same primary-endpoint nonreporting/replacement pattern is consolidated across the listed plans and outputs. This record does not assert that no model was ever fitted outside the package.

**Logical comparison and display precision:** Compare the named planned analysis sets with the named and displayed outputs. A single continuous baseline interaction plus a spline table is not the seven-variable interaction package. A center graph fulfills a graphical component but cannot identify a model estimate/test for center×treatment. A post hoc fixed cutoff 35 does not identify a prespecified sample-median split: the main overall median is reported as 34, but individual subgroup membership and its precision are not reconstructed. These are analysis identities and categorical rules; no half-unit numeric interval or relative gap can establish their equivalence. No exact adjusted subgroup effect is inferred from the forest graph.

**Bounded adherence context:** The protocol PP allowance for justified reduced dosage is printed; the main positive strict-adherence definition and post hoc n=395 display are printed. The actual overlap of those sets, participants with justified reductions, and a distinct protocol-PP result are not available. Thus this context does not establish a second independent population discrepancy, and the recheck does not use unknown membership as evidence for the core planned-output pattern.

**Necessary inputs available:** Prospective named analyses, complete supplied display index, explicit report analysis inventory and candidate-matched displayed outputs. **Exact missing inputs or definitions:** Locations/results for the seven-variable interaction/forest package, center×treatment model and additional-covariate sensitivities; a supplied amendment replacing them; actual median cutoffs/membership if the fixed-35 graph is intended to satisfy the median-split plan; any results held outside the supplied package. Individual data are unavailable and not needed to establish what outputs are identified in this package.

**Alternative source-grounded interpretation:** Some planned work may have been performed but reported elsewhere or deferred. The center graph supplies part of the center plan; continuous baseline interactions provide related, differently defined evidence. A later prospective amendment may explain replacement. None identifies the unlocated outputs in the supplied materials or proves they were never computed.

**Direct observation versus inferred explanation:** Plan promises and the displayed output identities are direct. Nonidentification is a bounded comparison of the supplied report inventory against those promises. Failure to fit a model, reasons for omission, and effects on conclusions are not inferred.

**Classification:** PLAN protocol/SAP versus REPORT main/results gives P_R, all relationships P_R, domain protocol_report. Plans collectively prescribe analyses whose outputs are not identified; their different levels of detail are not independently registered as plan-plan conflicts in this candidate. Main and supplement identify consistent related output types, so they add no S_C or S_W. **Classification ambiguity:** Whether an unprovided amendment superseded these analyses or outputs exist elsewhere remains open; source roles are clear.

**Exact remaining human question:** Where are the specified seven-variable subgroup interaction/forest results, center-plus-center-by-treatment model results and additional-covariate primary-endpoint sensitivities, or which supplied prospective amendment replaced or deferred them?

## C006 — Serious-event parent and component counts

**Evidence state:** reproduced

**Determining recheck fact:** The directly inspected table prints levodopa serious-event parent total 126 with 13 top-level counts summing to 143, and placebo infection parent 44 with six subtype counts summing to 52. Both remain above the scope's 0.05 relative-gap threshold after conservative half-unit allowances.

**Locations found and source/comparator matched:** Both comparisons are within [main PDF page 6, Table 2 and Adverse Events narrative](../../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6), role REPORT. The column header is Events, No.; levodopa n=126, placebo n=129. The adjacent narrative prints 255 serious events in 177 of 610 participants, 126 levodopa and 129 placebo; it repeats the event parent totals rather than the component sums. Table footnote a describes the later prespecified events of interest and supplies no multiple-classification rule for the serious-event hierarchy.

| Affected within-display comparison | Source parent matched | Comparator components matched directly from the PDF |
|---|---:|---|
| Levodopa all serious events versus top-level categories | 126 | Infection 55; stroke 16; extracranial bleeding 5; cardiac event 12; cancer 4; trauma 4; kidney failure 6; epileptic seizure 3; DVT/pulmonary embolism 3; electrolyte disorder 2; fracture 1; traumatic intracerebral hemorrhage 0; other (none of the above) 32. Sum 143. |
| Placebo infections versus infection subtypes | 44 | Pulmonary 17; urinary tract 15; abdominal 7; meningoencephalitis/encephalitis 2; unspecified infection 2; other infection 9. Sum 52. |

**Hierarchy confirmation:** The infection subtypes, stroke subtypes and cardiac subtypes have a further indentation. They are not counted again in the top-level sum. Fall is indented beneath Trauma, and its 4/5 counts are not added again. Trauma's 4/5 parent is counted once. This yields exactly the 13 top-level categories listed above, not a sum that double-counts fall. The label other (none of the above) is present.

**Consistency rule applicable:** Focus area A, Route A category 3: counts within one display do not reconcile under the printed parent/component hierarchy when interpreted as an additive event classification. The missing multiplicity/classification definition is retained as a human question rather than supplied by assumption. Both affected comparisons belong to one repeated hierarchy-count pattern.

**Calculation and display-precision intervals:**

| Comparison | Exact displayed arithmetic | Recomputed half-unit interval | Printed parent half-unit interval | Gap | Relative gap |
|---|---|---|---|---:|---:|
| Levodopa top level | 55+16+5+12+4+4+6+3+3+2+1+0+32=143 | 13 inputs at ±0.5: [136.5,149.5] | 126±0.5: [125.5,126.5] | 136.5−126.5=10 | 10/126=0.0793651 |
| Placebo infection | 17+15+7+2+2+9=52 | 6 inputs at ±0.5: [49,55] | 44±0.5: [43.5,44.5] | 49−44.5=4.5 | 4.5/44=0.1022727 |

The symmetric allowance at the displayed levodopa zero is deliberately conservative. A nonnegative count constraint would not reconcile the comparison. Both relative gaps exceed 0.05. Counts are integers, but the displayed-precision calculation nevertheless applies the required half-unit rule.

**Other locations of the same hierarchy checked:** Levodopa infection subtypes sum 27+15+5+0+1+11=59; [56,62] versus parent 55±0.5 gives gap 0.5, relative 0.5/55=0.0090909. Placebo top-level categories sum 44+19+10+3+7+5+2+6+4+2+3+0+34=139; [132.5,145.5] versus parent 129±0.5 gives gap 3, relative 3/129=0.0232558. Those two do not meet the displayed-precision threshold and are not additional affected comparisons. Stroke and cardiac subtype totals reconcile directly in both arms. The prespecified-event-of-interest rows form a different explicitly headed display block and are not added to the serious-event parent.

**Necessary inputs available:** Full table hierarchy, every affected component, printed parent counts, event units and adjacent participant/event distinction. **Exact missing inputs or definitions:** Whether a single event may occupy multiple top-level or infection-subtype rows, whether parents count unique events while components count diagnoses/sites, and the event-to-category mapping. No raw event listing is supplied. These missing definitions limit the explanation, not reproduction of the displayed sums and gaps.

**Alternative source-grounded interpretation:** The distinction between 255 events and 177 participants shows that repeated events per participant exist; it does not state that one event has multiple classifications. Multiple diagnoses/sites per event or distinct parent/component units could explain nonadditivity, but no such rule is printed. This is a source-compatible alternative, not a demonstrated reconciliation.

**Direct observation versus inferred explanation:** Counts, indentation, arithmetic and gaps are direct. Overlapping coding, multiple sites, or different units are inferred possible explanations. No specific event is alleged to have been duplicated, omitted or assigned to any category.

**Classification:** REPORT main Table 2 parent versus REPORT main Table 2 component rows; primary/all S_W; domain statistical_results because the comparison is counts and aggregation. The adjacent report narrative corroborates the parent values; no plan or second report is a conflicting comparator. **Classification ambiguity:** Additivity depends on the unprinted event-classification convention; document roles and within-report relationship are clear.

**Exact remaining human question:** Are serious-event and infection categories mutually exclusive and exhaustive at the printed event unit; if not, what multiple-classification or distinct-unit rule explains levodopa 143 components versus 126 events and placebo 52 infection subtypes versus 44 infections?

## Handoff and limitations

All six assigned IDs have individual source/comparator confirmations, applicable rules, precision treatment, input availability, missing definitions, alternatives, observation/explanation distinctions, remaining human questions and content-based classifications. All six evidence states are reproduced. No transcription or classification change is required. This does not establish an adjudicated outcome.

No source-page access limitation remains within the assigned scope. Remaining substantive limits are the undefined PROMIS scalar, original death rule/amendment history, replacement-model decision/output, secondary missingness details, planned output locations, and serious-event classification convention. Model effects and raw participant/event membership cannot be reconstructed without unprovided individual data. Absence comparisons are restricted to the supplied reporting package and do not assert absence of work elsewhere.
