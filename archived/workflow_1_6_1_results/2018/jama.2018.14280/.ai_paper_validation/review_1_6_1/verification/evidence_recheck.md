# Mechanical evidence recheck

Assigned stable ID: C001. Runtime task: `/root/evidence_rechecker`, fresh evidence recheck specialist, gpt-6.1-sol/high. Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md completely, and read the current ledger, independent inclusion screen and the two supporting checker findings. Only supplied package evidence was used. Source files, reused assets and other agents' artifacts were preserved. This file records evidence facts and classification, without selecting a human disposition.

## C001 — Binary risk-ratio definition and displayed intervention event fractions

**Evidence state:** reproduced

**Determining recheck fact:** Every registered fraction, RR, interval and cited location was found in the supplied sources. Eight Table 2 event-risk-ratio ranges remain disjoint from their printed RR intervals even when every count and denominator is conservatively allowed its half-unit interval. The two near-null rows overlap under that same conservative criterion and are retained as corroborating occurrences only. No registered source value or location required a transcription change.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT main article Table 2, footnote c, Statistical Analysis and abstract. The SAP secondary-outcome paragraph is PLAN corroboration only.

**Classification ambiguity:** None for document roles, relationship type or domain. The exact binary estimand remains unspecified.

### Exact source-location and text confirmation

| Location | Location found | Source value/text matched | Comparator matched | Role confirmed by content |
|---|---|---|---|---|
| [Main PDF page 6, printed page 1877, Table 2](../../../jama_simonis_2018_oi_180108.pdf#page=6), all ten rows listed below | Yes; table heading, low and intermediate strategy headers, row labels and row-specific fractions visually confirmed | Yes; all ten event fractions, percentages, RRs, 95% CIs and P values match the registration | Yes; the fractions are within the stated low and intermediate intervention columns, paired with each row's RR and footnote c | REPORT: presents completed trial outcomes, estimates and tests |
| [Main PDF page 6, Table 2 footnote c](../../../jama_simonis_2018_oi_180108.pdf#page=6) | Yes; right-hand footnote block | Yes; defines the effect estimate as risk ratio, gives 95% confidence intervals using Wald likelihood ratio approximation, and chi-square P values | Yes; superscript c attaches to every one of the ten RR rows | REPORT: explanatory analysis note for reported results |
| [Main PDF page 4, printed page 1875, Statistical Analysis](../../../jama_simonis_2018_oi_180108.pdf#page=4) | Yes; right column, secondary binary outcome paragraph | Yes; specifies risk ratio, 95% CIs using Wald likelihood ratio approximation, and chi-square hypothesis testing | Yes; this is the reported secondary binary method, distinct from the nearby Cox survival, inverse-Gaussian stay, mixed longitudinal and Gaussian subgroup analyses | REPORT: retrospective description of analyses performed for this trial |
| [Main PDF page 1, printed page 1872, abstract Results](../../../jama_simonis_2018_oi_180108.pdf#page=1) | Yes; final secondary-results sentence | Yes; all four pulmonary-complication repetitions match Table 2 as detailed below | Yes; the interventions and results establish low then intermediate strategy order, and the same adverse events and values are repeated | REPORT: completed trial abstract, with numerical results |
| [SAP PDF page 13, Secondary outcomes](../../../joi180108supp2_prod.pdf#page=13) | Yes; secondary-outcome section | Yes; prospectively specifies intervention effects on ICU/hospital mortality and other secondary outcomes as risk ratios, 95% Wald approximation intervals and chi-square tests | Yes as corroboration of the report's RR label; no conflicting planned binary quantity is established | PLAN: uses prospective analysis specifications for secondary outcomes and per-protocol analysis |

**Classification reason:** The compared numerical values, intervention-column fractions and RR definitions are in one REPORT document. S_W is therefore the only applicable relationship and the primary type under P_R > P_P > S_C > S_W precedence. The SAP confirms the same label rather than disagreeing with the report; it adds no P_R relationship. There is no compared conflict between PLAN locations or between different REPORT documents. Because the issue concerns effect identity, estimates and intervals, statistical_results is the matching domain rather than report_internal_inconsistency. All provisional classification fields are confirmed.

### Every Table 2 occurrence: source and comparator match

All rows below are at the exact Table 2 location linked above. The low and intermediate fractions, percentages, RR and interval were read directly from fresh source extraction and checked against the current run's directly rendered page. Footnote c defines their estimate as RR and their intervals as 95% CIs. For each row, location found = yes, source value matched = yes, comparator matched = yes, and the event-risk identity rule is applicable to the stated intervention contrast. The explicit fraction supplies each outcome's denominator; neither the randomized header n nor the secondary-section header n is substituted.

| Outcome | Low event/total (%) | Intermediate event/total (%) | Printed RR (95% CI) | Printed P |
|---|---|---|---|---|
| ICU mortality | 132/450 (29.3) | 115/458 (25.1) | 1.11 (0.96–1.27) | .15 |
| Hospital mortality | 151/477 (31.7) | 140/484 (28.9) | 1.06 (0.93–1.22) | .35 |
| Development of ARDS | 17/448 (3.8) | 23/462 (5.0) | 0.86 (0.59–1.24) | .38 |
| Development of pneumonia | 19/450 (4.2) | 17/462 (3.7) | 1.07 (0.78–1.47) | .67 |
| Pneumothorax | 8/448 (1.8) | 6/462 (1.3) | 1.16 (0.73–1.84) | .55 |
| Atelectasis | 51/449 (11.4) | 52/464 (11.2) | 1.00 (0.81–1.23) | .94 |
| Extrapulmonary infection | 20/448 (4.5) | 28/463 (6.0) | 0.84 (0.60–1.18) | .28 |
| Extrapulmonary sepsis | 12/448 (2.7) | 16/463 (3.5) | 0.87 (0.56–1.33) | .50 |
| Delirium | 149/343 (43.4) | 132/361 (36.6) | 1.15 (0.99–1.34) | .06 |
| Need for tracheostomy | 54/477 (11.3) | 52/484 (10.7) | 1.03 (0.84–1.26) | .78 |

### Consistency rule, reproduced arithmetic and display precision

Let a/n be the low-strategy event fraction and c/m the intermediate-strategy event fraction. The event-risk contrast supplied by those columns is R = (a/n)/(c/m). An RR labeled as the low-versus-intermediate effect on event occurrence refers to that conditioning unless a different model-based estimand is specified. The displayed binary-analysis descriptions do not establish such a different estimand. The rule addresses effect identity; it does not require a model-based estimate to equal a crude fraction when the source establishes the model.

Integer counts give the point calculations below. Additionally, to reproduce the registered conservative precision check, allow each displayed count or denominator ±0.5 independently. The monotone bounds are R_min = (a−0.5)(m−0.5)/[(n+0.5)(c+0.5)] and R_max = (a+0.5)(m+0.5)/[(n−0.5)(c−0.5)]. Every two-decimal printed RR r is allowed [r−0.005, r+0.005]. Closed endpoints are used conservatively; none of the disjoint decisions depends on an endpoint tie. All calculations were independently reproduced with JavaScript arithmetic, not with Python scientific orchestration.

| Outcome | R at printed counts | Conservative R interval | Printed RR interval | Reproduced comparison |
|---|---:|---|---|---|
| ICU mortality | 1.168232 | [1.156219, 1.180375] | [1.105, 1.115] | Disjoint |
| Hospital mortality | 1.094400 | [1.084634, 1.104255] | [1.055, 1.065] | Disjoint |
| ARDS | 0.762228 | [0.722479, 0.803849] | [0.855, 0.865] | Disjoint |
| Pneumonia | 1.147451 | [1.082955, 1.215998] | [1.065, 1.075] | Disjoint |
| Pneumothorax | 1.375000 | [1.187291, 1.597257] | [1.155, 1.165] | Disjoint |
| Atelectasis | 1.013534 | [0.991864, 1.035674] | [0.995, 1.005] | Overlap; corroborating occurrence only |
| Extrapulmonary infection | 0.738202 | [0.705568, 0.772108] | [0.835, 0.845] | Disjoint |
| Extrapulmonary sepsis | 0.775112 | [0.718726, 0.835286] | [0.865, 0.875] | Disjoint |
| Delirium | 1.188025 | [1.176221, 1.199950] | [1.145, 1.155] | Disjoint |
| Need for tracheostomy | 1.053701 | [1.031852, 1.076020] | [1.025, 1.035] | Overlap; corroborating occurrence only |

For example, ARDS R = (17/448)/(23/462) = 0.762228; its generous range still ends below 0.855. Pneumothorax R = (8/448)/(6/462) = 1.375000; even its generous lower bound exceeds 1.165. These and the other six disjoint rows establish the registered pattern independently of the two near-null rows.

### Abstract repetitions and their precision checks

All four repetitions were found and matched at [main PDF page 1, abstract Results](../../../jama_simonis_2018_oi_180108.pdf#page=1). Each matches the outcome, arm order, displayed percentages, RR, 95% CI and P in Table 2. For each row, source and comparator match = yes, document role = REPORT, and relationship = S_W. Percentage-only bounds use p±0.05 percentage points for each one-decimal displayed percentage and [r−0.005, r+0.005] for the RR.

| Abstract occurrence | Printed low vs intermediate percentages | Printed RR (95% CI); P | Percentage-only R interval | Comparison and matched Table 2 evidence |
|---|---|---|---|---|
| ARDS | 3.8% vs 5.0% | 0.86 (0.59–1.24); .38 | [0.742574, 0.777778] | Disjoint from [0.855, 0.865]; matched counts also disjoint |
| Pneumonia | 4.2% vs 3.7% | 1.07 (0.78–1.47); .67 | [1.106667, 1.164384] | Disjoint from [1.065, 1.075]; matched counts also disjoint |
| Severe atelectasis | 11.4% vs 11.2% | 1.00 (0.81–1.23); .94 | [1.008889, 1.026906] | Percentage-only interval is disjoint from [0.995, 1.005], but the deliberately broader matched-count range [0.991864, 1.035674] overlaps; retained as corroboration under the registered conservative count criterion |
| Pneumothorax | 1.8% vs 1.3% | 1.16 (0.73–1.84); .55 | [1.296296, 1.480000] | Disjoint from [1.155, 1.165]; matched counts also disjoint |

The abstract's severe atelectasis label matches the named pulmonary complication in the outcomes paragraph and the atelectasis row; it does not identify a different numerical result. No separate issue is inferred from the expanded label. The percentage-only atelectasis observation is reported transparently without promoting this occurrence beyond its registered corroborating role under the more generous count check.

### Diagnostic alternative and interval reproduction limits

The alternative conditional ratio Q = [a/(a+c)]/[(n−a)/(n+m−a−c)] compares low-group membership among event cases with low-group membership among noncases. This is a different conditional quantity from R. The diagnostic log-Wald interval Q exp(±1.96s), with s² = 1/a − 1/(a+c) + 1/(n−a) − 1/(n+m−a−c), was independently calculated for all ten rows. It tracks the displayed family but does not establish the actual computation code or exact reported CI implementation.

| Outcome | Diagnostic Q | Diagnostic point-input interval | Diagnostic lower endpoint range at input-interval corners | Diagnostic upper endpoint range at input-interval corners |
|---|---:|---|---|---|
| ICU mortality | 1.110840 | [0.964966, 1.278765] | [0.958049, 0.971924] | [1.270256, 1.287330] |
| Hospital mortality | 1.066452 | [0.931552, 1.220887] | [0.925462, 0.937678] | [1.213340, 1.228482] |
| ARDS | 0.857889 | [0.594560, 1.237844] | [0.570468, 0.618945] | [1.209728, 1.265919] |
| Pneumonia | 1.072699 | [0.781876, 1.471696] | [0.753114, 0.810999] | [1.441844, 1.501466] |
| Pneumothorax | 1.163636 | [0.735670, 1.840566] | [0.665355, 0.808816] | [1.780540, 1.898537] |
| Atelectasis | 1.007708 | [0.819111, 1.239730] | [0.807646, 0.830647] | [1.226624, 1.252889] |
| Extrapulmonary infection | 0.840148 | [0.597141, 1.182047] | [0.576741, 0.617751] | [1.158011, 1.206085] |
| Extrapulmonary sepsis | 0.867955 | [0.562984, 1.338133] | [0.529871, 0.596689] | [1.299774, 1.376254] |
| Delirium | 1.156162 | [0.994022, 1.344749] | [0.985654, 1.002471] | [1.333298, 1.356326] |
| Need for tracheostomy | 1.029707 | [0.844136, 1.256073] | [0.833003, 0.855334] | [1.243511, 1.268683] |

The endpoint ranges reproduce the checker diagnostics by evaluating all 16 corners of the four input intervals; they are separately evaluated endpoint ranges, not a reconstruction of a jointly fitted reported interval. Each printed endpoint's ±0.005 interval intersects its respective diagnostic range. Some point-input values do not round exactly to the reported value: for example, hospital Q = 1.066452 versus printed 1.06 and ICU diagnostic upper endpoint = 1.278765 versus printed 1.27. These facts limit the diagnostic explanation; they do not reconcile the eight R-versus-printed-RR discrepancies. They also prevent an assertion that the diagnostic formula reproduces the exact reported pipeline. The small diagnostic numerical differences between the two checker artifacts do not concern a registered source transcription and do not change the evidence state.

Chi-square association testing is invariant under transposing the two-by-two table. Consequently, matching or nonsignificant P values cannot select between R and Q conditioning. No separate CI/P incompatibility or change to the secondary nonsignificance statements is established here. No change to the primary result is inferred.

### Necessary inputs, missing definitions and alternative interpretations

**Necessary inputs available:** For all ten rows, the source provides both event counts, both outcome-specific totals, strategy labels, the RR label, reported point and interval, interval confidence level, hypothesis-test family and printed P. The report provides two-sided P values and a .05 significance level. These inputs suffice for the displayed event-risk identity and its conservative precision test. They also suffice for the expressly labeled reverse-conditioning diagnostic. No raw data are needed for those two arithmetic comparisons.

**Exact missing inputs or definitions:** The supplied materials do not define the binary outcome/exposure orientation used to calculate these estimates; the denominator conditioning and reference category of the reported RR; any additional binary-model link, covariates, stratification, adjustment or marginalization; or the exact function, implementation and numerical formatting used for the named Wald likelihood ratio approximation. R version 3.4.1 is stated, but no binary computation code or complete binary estimator specification is supplied. Thus exact reproduction of the authors' RR/CI pipeline is unavailable. The row-specific event denominators themselves are available and are not missing.

**Source-grounded alternative interpretation:** The printed family may represent the diagnostic reverse-conditioned quantity, or a binary model-based event-risk contrast whose definition is not stated. Nearby explicit Cox, inverse-Gaussian, mixed and Gaussian descriptions demonstrate that different analyses are used elsewhere, but do not establish an adjusted binary model for these ten RR rows. A specified adjusted model could explain a crude-versus-estimated difference; that remains an alternative for human clarification, not an inferred fact. Neither alternative selects a replacement analysis or a final extracted estimate.

**Direct observation versus inferred explanation:** Direct observations are the source-matched fractions, labels, RR/CI/P values and method text. Reproduced arithmetic facts are the eight disjoint R intervals, two overlapping conservative intervals, abstract repetition matches, and the diagnostic Q/interval values. A particular coding orientation or undocumented model is an inferred possible explanation only. The recheck does not assert access to, or reconstruction of, the computation code.

**Exact remaining human question:** For each of the ten Table 2 RR rows and its abstract repetition where present, what outcome/group orientation, denominator conditioning, reference group and any binary-model adjustment generated the reported risk ratio and 95% confidence interval, and which defined quantity should be extracted as the low-versus-intermediate strategy's effect on event occurrence?

### Source authority, derivative provenance and limits

Direct tools in tooling_record.md are available; no OCR, fallback environment or GPU was needed. Fresh derivatives were written only below review_1_6_1/preprocessing/: recheck-main-p1.txt, recheck-main-p4.txt, recheck-main-p6.txt and recheck-sap-p13.txt, each directly extracted with Poppler 25.03.0 pdftotext -layout from its named supplied PDF page; and recheck-main-p1.png, recheck-main-p4.png and recheck-sap-p13.png, directly rendered with Poppler 25.03.0 pdftoppm at 110 dpi. All three fresh images were visually inspected. The current run's numeric-main-p6.png was also visually inspected; its source match was established by the fresh page-6 extraction, table heading, printed page, strategy-column alignment, all fractions and effect entries, and footnote c. Reusable text and checker transcriptions served as locators, with the supplied PDFs remaining authoritative.

Current sha256sum values match source_hashes_before.sha256: main PDF aa0fdc5835724bd9c4fdcecf14eb7cef28a955428db34ad5cba8f644076148d9; SAP PDF 9aa3d6bf69706a5e25e5727cb0cfec6a32bda8299fa8bb3fde14e4755e782ec2. No supplied source or reused artifact was modified.

Scope complete: C001; ten Table 2 rows, four abstract repetitions, Table 2 footnote c, main Statistical Analysis and corroborating SAP paragraph. No assigned location remains unconfirmed. The unresolved item is the exact binary effect/interval definition and implementation identified above; it limits explanatory reconstruction, not the displayed arithmetic recheck. Durable artifact: verification/evidence_recheck.md.
