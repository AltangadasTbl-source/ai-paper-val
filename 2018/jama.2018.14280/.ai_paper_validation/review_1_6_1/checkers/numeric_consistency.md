# Numeric consistency review

## Scope and completion

Reviewed all 112 canonical numeric relationships N001–N112 in relationships/numeric_relationship_inventory.md: five supplied PDFs, 94 mapped pages; main article REPORT; protocol/SAP PLAN; results and data-sharing supplements REPORT. Scope includes all main flow/baseline/outcome/risk-count values, all 238 paired supplementary table comparisons, 72 explicit supplementary fractions, all pooled/mode totals, 16 subgroup differences, planned population arithmetic, source-matched repeated values, and effect-measure identity. The canonical inventory retains complete printed table rows and links. Main mapper N001–N060 and support N101–N115 are locator inputs, not a coverage limit.

Read QUALITY_CONTROL_SCOPE.md and review_contract.md completely. Reused source-linked extraction, tooling and coverage inventories; the source coverage ledger's initial support MAPPING_PENDING entries are superseded by the support mapper's durable 85/85 completion. No old conclusions or external evidence were read. Direct candidate confirmation: pdftotext -layout main PDF pages 1 and 4; fresh Poppler 25.03.0 pdftoppm render main page 6 at 110 dpi, preprocessing/numeric-main-p6.png, visually inspected. Sources and reused assets were preserved. Unaffected table arithmetic was checked from complete newly mapped source-linked transcriptions; no candidate rests on derivative-only wording.

Self-screening produced one consolidated finding and 22 excluded observations. No finding count was prescribed. There are no scientific-coverage gaps. Source limits: no raw/event-time data, survivor-specific denominator, complete variable-specific descriptive denominators, full binary-model formula, or exact graphical coordinates. Statistical-method and plan/report checks remain separately assigned; numeric review does not prescribe an analysis.

## Findings

### F-NUM-001

**Focus area:** C, effect-measure identity, supported by A numerator/denominator relationships.

**Proposed review domain:** statistical_results.

**Compared source locations and roles:** REPORT [main article PDF p6, printed p1877, Table2](../../../jama_simonis_2018_oi_180108.pdf#page=6), rows ICU mortality, hospital mortality, development of ARDS, development of pneumonia, pneumothorax, atelectasis, extrapulmonary infection, extrapulmonary sepsis, delirium, and need for tracheostomy; Table2 footnote c defines each effect as risk ratio and names Wald likelihood ratio approximation confidence intervals and chi-square P values. REPORT [main article PDF p1, printed p1872, Abstract Results](../../../jama_simonis_2018_oi_180108.pdf#page=1) repeats ARDS, pneumonia, severe atelectasis and pneumothorax RRs and intervals. REPORT [main article PDF p4, printed p1875, Statistical Analysis](../../../jama_simonis_2018_oi_180108.pdf#page=4) says other secondary binary outcomes were assessed with risk ratios/Wald approximation and chi-square tests; the intervention groups and adverse-event percentages give the low-versus-intermediate event-risk contrast. All compared locations are within one REPORT document.

**Printed inputs, rule and calculation:** Write a=low-group events, n=low-group assessed total, c=intermediate events, m=intermediate assessed total. The treatment effect event-risk ratio is R=(a/n)/(c/m). The displayed point estimates instead closely reproduce Q=[a/(a+c)]/[(n−a)/(n+m−a−c)], the risk of assignment to the low group among event cases divided by that among noncases. This reverses the roles of group and outcome. It is a different risk ratio from the randomized intervention contrast. Under the same reversed contingency orientation, the diagnostic log-RR confidence interval is Q exp(±1.96s), where s²=1/a−1/(a+c)+1/(n−a)−1/(n+m−a−c). This diagnostic explains the repeated magnitude/interval pattern; it does not claim access to the computation code.

The following table retains every affected row. The last column gives the separately evaluated lower- and upper-endpoint ranges of that reversed-orientation diagnostic CI, allowing each displayed count±0.5. Each range intersects its printed two-decimal CI endpoint interval. A near-null pair does not independently establish a contradiction merely by sharing the pattern.

| Table2 row | Low event/total | Intermediate event/total | Printed RR (95% CI) | Event-risk R at printed counts | Event-risk R interval, all input counts±0.5 | Reversed-orientation Q at printed counts | Reversed CI endpoint ranges, all input counts±0.5 |
|---|---|---|---|---|---|---|---|
| ICU mortality | 132/450 | 115/458 | 1.11 (0.96–1.27) | 1.168232 | [1.156219, 1.180375] | 1.110840 | [0.958049, 0.971924]; [1.270256, 1.287330] |
| Hospital mortality | 151/477 | 140/484 | 1.06 (0.93–1.22) | 1.094400 | [1.084634, 1.104255] | 1.066452 | [0.925462, 0.937678]; [1.213340, 1.228482] |
| ARDS | 17/448 | 23/462 | 0.86 (0.59–1.24) | 0.762228 | [0.722479, 0.803849] | 0.857889 | [0.570468, 0.618945]; [1.209728, 1.265919] |
| Pneumonia | 19/450 | 17/462 | 1.07 (0.78–1.47) | 1.147451 | [1.082955, 1.215998] | 1.072699 | [0.753114, 0.810999]; [1.441844, 1.501466] |
| Pneumothorax | 8/448 | 6/462 | 1.16 (0.73–1.84) | 1.375000 | [1.187291, 1.597257] | 1.163636 | [0.665355, 0.808816]; [1.780540, 1.898537] |
| Atelectasis | 51/449 | 52/464 | 1.00 (0.81–1.23) | 1.013534 | [0.991864, 1.035674] | 1.007708 | [0.807646, 0.830647]; [1.226624, 1.252889] |
| Infection | 20/448 | 28/463 | 0.84 (0.60–1.18) | 0.738202 | [0.705568, 0.772108] | 0.840148 | [0.576741, 0.617751]; [1.158011, 1.206085] |
| Sepsis | 12/448 | 16/463 | 0.87 (0.56–1.33) | 0.775112 | [0.718726, 0.835286] | 0.867955 | [0.529871, 0.596689]; [1.299774, 1.376254] |
| Delirium | 149/343 | 132/361 | 1.15 (0.99–1.34) | 1.188025 | [1.176221, 1.199950] | 1.156162 | [0.985654, 1.002471]; [1.333298, 1.356326] |
| Tracheostomy | 54/477 | 52/484 | 1.03 (0.84–1.26) | 1.053701 | [1.031852, 1.076020] | 1.029707 | [0.833003, 0.855334]; [1.243511, 1.268683] |

For example, ARDS: a=17,n=448,c=23,m=462. R=(17/448)/(23/462)=0.762228. Q=(17/40)/(431/870)=0.857889, matching the printed 0.86, and Q's point-input log interval is [0.594560,1.237844], matching the printed 0.59–1.24. Pneumothorax: R=(8/448)/(6/462)=1.375000, whereas Q=(8/14)/(440/896)=1.163636, matching 1.16; Q's point-input log interval is [0.735670,1.840566]. The Table2 point-input Q/log-CI diagnostics for the other eight rows are ICU 1.110840[0.964966,1.278765], hospital 1.066452[0.931552,1.220887], pneumonia 1.072699[0.781876,1.471696], atelectasis 1.007708[0.819111,1.239730], infection 0.840148[0.597141,1.182047], sepsis 0.867955[0.562984,1.338133], delirium 1.156162[0.994022,1.344749], tracheostomy 1.029707[0.844136,1.256073]. Differences in final digits of these diagnostic values are covered by the retained input intervals, not additional findings.

**Display-precision test:** For event risk, the conservative monotone bounds are Rmin=[(a−0.5)/(n+0.5)]/[(c+0.5)/(m−0.5)] and Rmax=[(a+0.5)/(n−0.5)]/[(c−0.5)/(m+0.5)]. A displayed RR r to two decimals retains [r−0.005,r+0.005]. The event-risk intervals in the table are disjoint from those printed RR intervals in eight rows: ICU/hospital mortality, ARDS, pneumonia, pneumothorax, extrapulmonary infection, extrapulmonary sepsis, and delirium. Atelectasis and tracheostomy overlap under this conservative display test and are included as affected/corroborating occurrences of the shared table computation pattern, not standalone inconsistencies. The ARDS and pneumonia/pneumothorax repetitions in the abstract retain the discrepancy. Atelectasis in the abstract repeats the near-null corroborating row.

**Affected result or extracted value:** The intervention risk-ratio effect estimates and their confidence intervals for these binary clinical outcomes, especially the abstract's ARDS, pneumonia and pneumothorax results. A data extractor using the printed effect and interval could take a treatment-effect magnitude that differs from the event-risk ratio established by the printed trial-arm counts. The concern is effect-size extraction; the shared chi-square P value is symmetric under contingency-table transposition, so this observation alone does not contradict the stated nonsignificance conclusions.

**Why context does not resolve it:** The local RR label, group headers, event fractions and abstract narration present event occurrence under the low versus intermediate strategy; they do not disclose a ratio of treatment-group membership conditional on event status. No displayed definition or formula says the table intentionally reports that reversed conditional quantity. Immediate context supplies two different quantities but no basis for choosing the displayed effect as the treatment-event RR. This is a repeated numerical transformation affecting the effect and interval, not merely a substituted symbol. The report states Cox models for HR rows, inverse-Gaussian models for stay days, mixed models for longitudinal variables, and Gaussian subgroup models, but does not establish an adjusted/model-based binary RR that would resolve this identity pattern. The finding therefore does not rest solely on comparing an established modeled estimate with a crude ratio.

**Source-grounded alternatives and missing definition:** The displayed estimates may be risk ratios from the reversed group/outcome contingency orientation demonstrated above, or may arise from a separate binary analysis whose outcome/exposure coding, denominator definition, and model have not been supplied. An explicitly defined adjusted event-risk model could explain a crude/estimated difference, but the package does not state one for these rows; this remains an alternative rather than an inferred fact. The computation code and exact binary effect definition are missing. This review does not choose a replacement analysis or a final value.

**Exact human question:** For every Table2 RR row and its abstract repetitions, what binary effect definition and outcome/group orientation generated the reported risk ratio and 95% confidence interval, and which ratio should be extracted as the low-versus-intermediate strategy's effect on event occurrence?

## Excluded observations

Each observation is listed once with one scope reason code. Reconciled broad groups document the checks without assigning finding identifiers.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main pp1–7; N001–N005,N097,N098 | Flow totals, group totals, losses, abstract primary sample sizes and <1% missingness reconcile:3695−2734=961;477+484=961;475+480=955;6/961=0.62435%. | NOT_REPRODUCED |
| REPORT main p5 Table1; N007–N056,N109 | Tobacco/alcohol/admission totals 475/482 versus header 477/484 and row-specific percentages do not establish a common complete-case descriptive denominator; unprinted variable-specific missingness is not an analysis-population contradiction. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p5 Table1; N009,N109 | 621/961=64.62% versus abstract 65% male; categorical percentages and sums retain final-digit intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p6 Table2 primary/secondary headers and all event fractions; N076,N078–N091 | Primary 475/480, secondary 475/481, and explicitly stated mortality/complication fractions use distinct outcome-specific available cases; row fractions make the extraction denominator immediate. | CONTEXT_RESOLVES |
| REPORT main pp1,5,6; N076–N079 | Primary/survivor/stay mean differences reconcile when each one-decimal mean retains±0.05; abstract medians accompany mean differences and the local labels identify the distinct summaries. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p6 Table2; N080–N091 | All printed main event percentages agree with their explicit fractions within display precision. | NOT_REPRODUCED |
| REPORT main p7 Figure2 risk tables; N092–N095 | All risk counts decrease and remain within randomized population; denominator differences from other outcomes do not change the primary analysis population. | PERIPHERAL_COMPARISON |
| REPORT main pp1,6,7; N090,N091 | Cox HR1.12/1.07 differ from crude death-risk ratios; Cox modeling is explicitly established on p4 and Table2 footnote d. | MODEL_VERSUS_CRUDE |
| REPORT main p7 Figure2 and p6 Table2; N078,N079,N094,N095 | Stay HR versus mean-difference summaries belong to separately stated Cox and inverse-Gaussian analyses; they are not the same effect quantity. | MODEL_VERSUS_CRUDE |
| REPORT DOC004 pp5–7 eTables1–3; N069–N071,N100–N108 | All mode-specific patient totals, available-ABG denominators and pH/acidosis event sums reconcile between pooled and mode displays; all numerators are within explicit denominators. | NOT_REPRODUCED |
| REPORT DOC004 p7 eTable3; N071 | Post-titration low VCV pH<7.25:74/264 (27.9); day1 intermediate PSV:6/161 (3.8). Conservative half-unit intervals for all printed inputs intersect displayed percentage intervals even though point recomputations 28.0303% and 3.7267% differ in last digit. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC004 pp5,7 eTables1/3; N069,N071 | Post-titration low pooled pH upper quartile 7.54 exceeds mode upper quartiles 7.36,7.40,7.37; this per-time descriptive comparison does not change primary/key-secondary result or analysis-population size. | PERIPHERAL_COMPARISON |
| REPORT DOC004 p6 eTable2 other-mode PEEP post-titration; N070 | Intermediate 8 (5–1) has implausible displayed upper quartile; immediate typographic context identifies a missing final character, in a peripheral ventilator descriptive cell. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC004 p7 eTable3 other-mode acidosis; N071 | 7/20 (35.) has trailing punctuation; count/denominator immediately identifies 35%. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC004 p8 eTable4; N072,N110 | Sedative/analgesic/NMBA/vasopressor percentages imply available denominators 453/462; fluids/blood explicitly 454/464. Different variable availability is unreported in detail and does not establish a shared denominator. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC004 p8 eTable4; N072,N110 | All explicit fluid/blood fractions and randomized-population rescue percentages reconcile; all 30 paired rows preserve their printed units and central/dispersion quantities. | NOT_REPRODUCED |
| REPORT DOC004 p9 eTable5; N073,N096 | All 16 paired mean differences fit half-unit intervals of one-decimal means; subgroup counts are not printed, so their totals cannot be inferred from SDs/intervals. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p6 subgroup paragraph; DOC004 p9 eTable5; N073,N096 | Main subgroup intervals called IQR coincide with eTable5 CI and negative endpoints cannot be quartiles of nonnegative VFD; interval identity is immediate from local effect context. | TERMINOLOGY_OR_WORDING |
| REPORT DOC004 p9 eTable5; N073 | Ventilation-before-randomization labels wrap across adjacent lines and footer mean() omits dispersion label; these presentational differences do not change the numeric means or differences. | NOTATION_OR_TYPOGRAPHY |
| PLAN protocol pp17,19; SAP p11; REPORT main p4; N062,N111 | 397 increased 20%=476.4, rounded 476 per arm and 952 overall; treating 20% as a reciprocal retention denominator is a different assumed convention from the protocol's explicit increase. | CONTEXT_RESOLVES |
| PLAN protocol pp13,38; N061,N099 | Historical 1961-patient histogram,29%/71%, observational volumes and original site expectations are background/recruitment quantities, not current primary/key-secondary results. | PERIPHERAL_COMPARISON |
| REPORT DOC004 pp10–13; N074,N075 | Unprinted empirical-curve coordinates cannot support exact counts or denominators; curves are retained qualitatively rather than digitized into an assumed result. | CONDITIONAL_OR_UNREPORTED |

## Compact completion record

Scope 94/94 mapped source pages; 112/112 canonical numeric relationships checked; 238/238 paired supplement comparisons retained; findings 1; excluded observations 22; scientific gaps 0. No candidate identifiers, severity, validity, or disposition were assigned. Durable artifacts: relationships/numeric_relationship_inventory.md and checkers/numeric_consistency.md. Fresh candidate confirmation derivative: preprocessing/numeric-main-p6.png (direct Poppler 25.03.0, 110 dpi).

