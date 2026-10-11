# Numeric consistency review

Completed scope: all numeric relationships mapped across six supplied PDFs, 100 physical pages; 110 stable N relationships with complete grouped vectors. Read QUALITY_CONTROL_SCOPE.md and the complete Workflow1.6.1 review contract. No prior candidate/report conclusions or external sources used. Findings:2. Excluded observation groups:14. No scientific coverage gap.

Evidence: current-run main/support maps, current-source-matched reusable extraction, fresh direct Poppler layout reads of main pp.1–4,8–10 and results supplement pp.29–30. Main p.8 and results supplement p.42 source-matched rasters were visually inspected. Report units and denominator labels are preserved as printed. Main pp.9–10 were independently read from current direct PDF extraction, including table notes and Figure2. Graph coordinates without exact labels remain approximate.

Every mapped full count/percentage vector was checked against its stated population and denominator, with partitions/sums only when categories are mutually exclusive. All33 longitudinal main group/time contrasts were checked for feasible mean differences at display precision. Effect quantities were checked only with the displayed count comparison or a stated identity; no adjusted/model-based quantity was forced to a crude value. Participant flow reconciles:1011+1002=2013;993+991=1984;989+987=1976;917+912=1829. Exclusion branches18+11=29,4+4=8,72+75=147 all reconcile.

## Findings

### F-NUM-001

The treatment risk-ratio label does not reconcile with the displayed treatment-specific event risks; a repeated alternative ratio pattern also appears in matched displays.

**Exact locations and document roles:** REPORT main [abstract,p.1](../../../jama_bluth_2019_oi_190055_16092.pdf#page=1), [primary/component narrative,p.8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), [Table3,p.9](../../../jama_bluth_2019_oi_190055_16092.pdf#page=9), [Table3 continuation and Figure2,p.10](../../../jama_bluth_2019_oi_190055_16092.pdf#page=10), with computation description REPORT [Statistical Analysis,p.4](../../../jama_bluth_2019_oi_190055_16092.pdf#page=4). All affected binary Table3 rows and Figure2 rows are enumerated below. REPORT results supplement [eTable8,p.29](../../../joi190055supp4_prod_16092.pdf#page=29) is a corroborating per-protocol occurrence under its generic Effect Estimate header, not an independent definite RR label. REPORT results supplement [eFigure12,p.42](../../../joi190055supp4_prod_16092.pdf#page=42) repeats the primary collapsed-composite0.93(0.83–1.04) under Odds Ratio(95%CI). Its other modeled component/global results are not diagnosed by crude recomputation.

**Printed inputs and rule:** Primary211/989(21.3%) versus233/987(23.6%), labeledRR0.93(0.83–1.04), P=.23. The main method states primary and other binary intervention effects as risk ratios, with Wald likelihood-ratio approximation and χ² testing; the site-adjusted mixed model is a separately described sensitivity analysis. For the displayed treatment comparison, RR=(H events/H total)/(L events/L total)=0.903748. The displayed0.93 interval[0.925,0.935] cannot represent that value. Even allowing counts and totals their conservative±0.5 intervals yields approximately[0.8987,0.9088], disjoint from the printedRR interval. The crude treatment OR=211×754/(778×233)=0.877644, also distinct from the collapsed-composite value labeledOR0.93 in eFigure12. No corresponding adjusted definition is provided for the collapsed-composite repeat.

A diagnostic alternative, not a claimed author implementation, is T=[H events/(H events+L events)]/[H non-events/(H non-events+L non-events)]. For the primary result T=(211/444)/(778/1532)=0.935791, much closer to0.93 than the treatmentRR. Hypoxemia T=(49/183)/(940/1793)=0.510737, matching printed0.51; its treatmentRR=(49/989)/(134/987)=0.364932. Pleural effusion T=(43/64)/(946/1912)=1.357955, near printed1.35; its treatmentRR=2.043478. Hypotension T=(313/483)/(676/1493)=1.431233, near printed1.43; its treatmentRR=1.837453. Table vectors below show the same orientation pattern across outcomes. Small differences between T and printed values, including apparent truncation, are not separate findings. Identity of the displayed quantity is the unresolved relationship.

**Focus area:**C (effect-measure identity), with A event-risk denominators. **Proposed review domain:**statistical_results. Proposed relationships:S_W and S_C; no PLAN source is needed to establish this reporting relationship.

**Affected result or extracted value:** The primary treatmentRR and CI0.93(0.83–1.04); the displayed binary treatment-effect quantities in Table3 and Figure2; hypoxemia, hypotension and bradycardia effect magnitudes; the primary collapsed-composite quantity that eFigure12 labelsOR. Counts and absolute risk differences are separately displayed and do not identify which ratio/interval an extractor should take as the intended treatment effect.

**Why context does not resolve it:** The primary result is repeatedly called an intervention risk ratio, while the numerical value differs beyond display precision from that treatment-risk ratio. A distinct transposed quantity reproduces the general numeric pattern but is not defined as the target estimand in the supplied report. The primary collapsed-composite repeat is additionally labeledOR in the supplement. A reader cannot choose the intended ratio and matching interval merely by correcting a typographic label; that choice changes the extracted treatment-effect magnitude.

**Source-grounded alternatives:** The labeled treatmentRR might have been intended, the displayed quantity might use the transposed conditional risks in the diagnostic, or an unstated adjusted/alternative estimand might apply. The generic PP Effect Estimate heading does not decide among them. Site-adjusted and GEE results are separately specified and cannot silently define the unadjusted collapsed-composite display. No preferred analysis is proposed.

**Exact human question:** What event definition, denominator orientation, estimand and computation produced the ratios and intervals labeled risk ratio in the main article, and which treatment-effect quantity and interval should be extracted for the primary collapsed composite and the other listed binary results, including its odds-ratio-labeled supplement repeat?

#### Complete affected binary vector

H/L totals989/987 throughout this table. Equal-event rows are retained as occurrences of the same reported computation block; they are not independent contradictions. Hospital-free days and5-day mortality are excluded from this vector because their notes identify mean difference and CoxHR. Acute myocardial infarction has no ratio.

| Main Table3 row / exact page | H events | L events | Printed RR | Treatment-risk ratio | Diagnostic T |
|---|---:|---:|---:|---:|---:|
| Primary PPC,p.9 | 211 | 233 | 0.93 | 0.9037 | 0.9358 |
| Mild respiratory failure,p.9 | 135 | 154 | 0.92 | 0.8749 | 0.9228 |
| Moderate respiratory failure,p.9 | 42 | 58 | 0.83 | 0.7227 | 0.8320 |
| Severe respiratory failure,p.9 | 30 | 36 | 0.90 | 0.8316 | 0.9053 |
| Atelectasis,p.9 | 44 | 55 | 0.88 | 0.7984 | 0.8828 |
| Pleural effusion,p.9 | 43 | 21 | 1.35 | 2.0435 | 1.3580 |
| New pulmonary infiltrates,p.9 | 14 | 18 | 0.87 | 0.7762 | 0.8723 |
| Cardiopulmonary edema,p.9 | 17 | 9 | 1.31 | 1.8851 | 1.3117 |
| Bronchospasm,p.9 | 12 | 10 | 1.09 | 1.1976 | 1.0909 |
| Pulmonary infection,p.9 | 10 | 10 | 0.99 | 0.9980 | 0.9990 |
| Aspiration,p.9 | 2 | 1 | 1.33 | 1.9960 | 1.3327 |
| ARDS,p.9 | 3 | 1 | 1.50 | 2.9939 | 1.5000 |
| Pneumothorax,p.9 | 1 | 3 | 0.50 | 0.3327 | 0.4990 |
| Severe PPC,p.9 | 116 | 134 | 0.91 | 0.8639 | 0.9174 |
| Extrapulmonary composite,p.9 | 167 | 150 | 1.06 | 1.1111 | 1.0632 |
| SIRS,p.9 | 93 | 83 | 1.06 | 1.1182 | 1.0615 |
| Sepsis,p.9 | 18 | 15 | 1.09 | 1.1976 | 1.0915 |
| Severe sepsis,p.9 | 7 | 10 | 0.82 | 0.6986 | 0.8214 |
| Septic shock,p.9 | 7 | 8 | 0.93 | 0.8732 | 0.9319 |
| GI failure,p.9 | 65 | 56 | 1.07 | 1.1584 | 1.0784 |
| Kidney failure,p.9 | 31 | 32 | 0.98 | 0.9668 | 0.9826 |
| Extrapulmonary infection,p.9 | 29 | 23 | 1.11 | 1.2583 | 1.1177 |
| Hepatic failure,p.9 | 9 | 9 | 0.99 | 0.9980 | 0.9990 |
| Coma,p.9 | 2 | 2 | 0.99 | 0.9980 | 0.9990 |
| DIC,p.9 | 1 | 0 | 2.00 | undefined (L risk0) | 1.9990 |
| Impaired wound healing,p.9 | 22 | 26 | 0.91 | 0.8444 | 0.9138 |
| Unexpected ICU,p.9 | 41 | 32 | 1.12 | 1.2787 | 1.1274 |
| Hypoxemia,p.9 | 49 | 134 | 0.51 | 0.3649 | 0.5107 |
| Hypotension,p.9 | 313 | 170 | 1.43 | 1.8375 | 1.4312 |
| Bradycardia,p.9 | 98 | 59 | 1.27 | 1.6577 | 1.2743 |
| In-hospital mortality,p.9 | 12 | 5 | 1.41 | 2.3951 | 1.4154 |
| Rescue,p.10 | 59 | 166 | 0.49 | 0.3547 | 0.4937 |
| Vasoactive drugs,p.10 | 491 | 439 | 1.10 | 1.1162 | 1.1089 |

All full printed CI/P/percentage/difference vectors are preserved verbatim in MAIN070–104 of the new [main map](../extraction/main_quantitative_evidence.md). They are affected locations of the one ratio-identity pattern, not additional findings. The DIC row has a finite printedRR2.00 although L risk is0; its very narrow interval belongs to the same transposed pattern, not an independently registered count finding.

| Figure2 row,p.10 | H events/total | L events/total | Printed RR | Treatment-risk ratio | Diagnostic T |
|---|---|---|---:|---:|---:|
| Nonlaparoscopic | 79/240 | 74/253 | 1.09 | 1.1254 | 1.0904 |
| Laparoscopic | 130/740 | 156/727 | 0.88 | 0.8187 | 0.8800 |
| BMI<40 | 76/336 | 94/376 | 0.93 | 0.9048 | 0.9319 |
| BMI≥40 | 135/653 | 139/611 | 0.94 | 0.9088 | 0.9416 |
| SpO2<96% | 88/317 | 112/342 | 0.88 | 0.8477 | 0.8819 |
| SpO2≥96% | 123/672 | 121/645 | 0.99 | 0.9757 | 0.9852 |
| Peripheral incision | 32/126 | 25/126 | 1.16 | 1.2800 | 1.1646 |
| Upper abdominal incision | 179/863 | 208/861 | 0.90 | 0.8586 | 0.9041 |
| Waist:hip<1 | 97/467 | 100/457 | 0.97 | 0.9492 | 0.9675 |
| Waist:hip≥1 | 98/447 | 112/449 | 0.92 | 0.8789 | 0.9173 |
| All patients | 211/989 | 233/987 | 0.93 | 0.9037 | 0.9358 |

The treatment×subgroup binomial model is stated for interaction testing; no adjustment defining the displayed subgroup point estimates is stated. These rows extend the recurring quantity ambiguity rather than challenge a specified adjusted estimate. Complete Figure2 intervals/interactions are retained in MAIN106–111.

| PP eTable8,p.29 corroborating row | H events/917 | L events/912 | Printed generic effect | Treatment-risk ratio | Diagnostic T |
|---|---:|---:|---:|---:|---:|
| Primary PPC | 186 | 209 | 0.92 | 0.8851 | 0.9237 |
| Mild respiratory | 119 | 140 | 0.90 | 0.8454 | 0.9039 |
| Moderate respiratory | 38 | 51 | 0.84 | 0.7410 | 0.8452 |
| Severe respiratory | 25 | 35 | 0.83 | 0.7104 | 0.8263 |
| ARDS | 3 | 1 | 1.50 | 2.9836 | 1.4975 |
| Bronchospasm | 11 | 10 | 1.04 | 1.0940 | 1.0453 |
| New infiltrates | 14 | 14 | 0.99 | 0.9945 | 0.9972 |
| Infection | 10 | 9 | 1.05 | 1.1051 | 1.0503 |
| Aspiration | 2 | 1 | 1.33 | 1.9891 | 1.3304 |
| Pleural effusion | 38 | 18 | 1.37 | 2.0996 | 1.3687 |
| Atelectasis | 38 | 50 | 0.85 | 0.7559 | 0.8553 |
| Cardiopulmonary edema | 15 | 7 | 1.36 | 2.1312 | 1.3659 |
| Pneumothorax | 1 | 2 | 0.66 | 0.4973 | 0.6645 |

### F-NUM-002

The count/denominator pairs and percentages in two adjacent neuromuscular rows do not reconcile, while their absolute differences use the printed denominators.

**Exact locations and document roles:** REPORT main [Table2,p.8](../../../jama_bluth_2019_oi_190055_16092.pdf#page=8), Monitoring of neuromuscular function and Reversal rows, both arms; immediate Neuromuscular blockade parent row and monitoring footnote d inspected. No PLAN source is involved.

**Printed inputs:** Monitoring632/982(64.9%) versus651/984(67.7%), absolute difference−1.8(−6.0 to2.4),P=.40. Reversal724/982(74.3%) versus723/984(75.2%), absolute difference0.2(−3.6 to4.1),P=.90. The parent blockade row is974(98.5%) versus961(97.4%).

**Rule and calculation:** An explicitly labeled No./total No.(%) pair should satisfy percentage=100×numerator/denominator. The four recomputed percentages are64.358%,66.159%,73.727%,73.476%. Conservative±0.5 intervals for each integer input yield64.275–64.442%,66.074–66.243%,73.639–73.816%,73.388–73.564%. None overlaps the corresponding displayed percentage intervals64.85–64.95%,67.65–67.75%,74.25–74.35%,75.15–75.25%. The printed-denominator differences are−1.800 and+0.251percentage points, consistent with the displayed differences under display intervals. Using the parent blockade counts as denominators instead yields64.887%,67.742%,74.333%,75.234%, matching all four printed percentages, but monitoring difference then becomes−2.855points and reversal−0.901points.

**Focus area:**A. **Proposed review domain:**statistical_results. Proposed relationship:S_W.

**Affected result or extracted value:** High/low proportions with neuromuscular monitoring and reversal, the applicable complete-case denominators, and the corresponding between-arm risk differences. For reversal, denominator choice changes the direction of the extracted point difference.

**Why context does not resolve it:** Both denominator sets occur in the same table. The parent-count denominator reproduces percentages; the explicitly printed row denominators reproduce absolute differences. Footnote d defines any monitoring but does not define a restriction to recipients of blockade, nor distinguish percentages from the denominators used for the displayed comparisons. Immediate context therefore supplies two competing calculations rather than one unmistakable intended population.

**Source-grounded alternatives:** Percentages may refer to recipients of blockade whereas fractions/differences refer to participants with row data, or one displayed denominator/percentage set may require reconciliation. The report does not state which population the percentages intend. No preferred denominator is proposed.

**Exact human question:** For the monitoring and reversal rows, do the percentages and absolute differences refer to complete cases with denominators982/984 or to recipients of neuromuscular blockade with denominators974/961, and what count, denominator and comparison should be extracted for each row?

## Excluded observations

Each observation group occurs once here; each has exactly one reason code. Straight reconciliations are documented in the N inventory rather than treated as screened findings.

| Location | Observation | Reason code |
|---|---|---|
| Main Tables1–3, especially tobacco, infection, radiography/prophylaxis and kidney-grade percentages | Several last decimal digits do not follow conventional nearest rounding with exact integers, consistent with truncated display. Conservative half-unit input intervals resolve many; for the remainder the explicit count/denominator immediately determines the proportion and no population/result choice is unclear. | CONTEXT_RESOLVES |
| Main Table2 p.7–8 all33 mean contrasts, temperature/blood loss and hospital-free means | Differences occasionally differ from subtraction of rounded summaries, but their half-unit input intervals admit the printed difference. | ROUNDING_OR_DISPLAY_PRECISION |
| Main abstract p.1 hypoxemia CI versus Table3 p.9 | Abstract prints upper6.1 rather than−6.1; negative difference, direction, P<.001 and exact table interval identify the intended missing minus immediately. | NOTATION_OR_TYPOGRAPHY |
| Main Table1 p.6 WBC unit, Table2 p.7 Heat rate, Figure2 p.10 waist:hip cm; protocol p.14/results supplement p.20 hemoglobin unit | Numeric scale and immediate clinical label make the intended units/word obvious; no alternative trial result applies. | NOTATION_OR_TYPOGRAPHY |
| Main abstract p.1 intervention989/987 described as randomized; Figure1 p.3 randomized1011/1002 | Abstract explicitly identifies completed1976 and the detailed flow supplies original allocation and exclusions; intended analysis population resolves immediately. | CONTEXT_RESOLVES |
| Main Table1 p.6 abdominal/nonabdominal denominators and abstract pooled1778(90.1%) | Arm fractions are swapped/incomplete descriptively; abdominal894+884=1778 and986+987=1973 recover pooled90.1%. These do not change primary-analysis989/987 or any key secondary event denominator. | PERIPHERAL_COMPARISON |
| Main Table1 BMI35–40/>40 versus Figure2 BMI<40/≥40, surgical approach and waist:hip missing observations | Cutoffs/populations are not identical; per-variable complete cases explain smaller subgroup totals. No contradictory primary denominator established. | PERIPHERAL_COMPARISON |
| Main Table3 p.9 GI65/56 versus graded49/46 and renal-grade denominator subsets; results eTable6 p.27 totals984/982,985/986,986/986 | Explicit subset denominators/complete-case methods permit missing descriptive/classification entries; assuming every case must have grade/data is unsupported. | CONDITIONAL_OR_UNREPORTED |
| Results eTables3–5 pp.24–26 fluid/agent subtype sums versus any-use counts | Multiple drugs/fluids can be used in one participant; mutually exclusive sums are not stated. | CONDITIONAL_OR_UNREPORTED |
| Results eFigure9 p.39 repeated at-risk vector from primary curve and approximate endpoint versus caption13.6% | Risk-set convention/censoring and exact graphical coordinates are not supplied; assuming an endpoint-specific event-removal vector is unsupported. | CONDITIONAL_OR_UNREPORTED |
| Results eFigures8–11 pp.38–41 HR/rates versus crude risks; eTable9 p.30 and eFigure12 p.42 modeled components/GEE/random-effects results | Kaplan–Meier/Cox, generalized linear/mixed, proportional-odds and GEE estimands are separately specified; crude treatment risk ratios do not test their identities. Only explicit primary collapsed-composite repeat is included in F-NUM-001. | MODEL_VERSUS_CRUDE |
| Results eFigure11 p.41 caption names extrapulmonary complications | Probability-of-death title, mortality axis, percentages and mortalityHR make intended result attribution unmistakable. | CONTEXT_RESOLVES |
| Protocol p.12 retained748 target versus p.11 revised2013 and amendment pp.2–3; original712→748 versus revised1912→2013 dropout arithmetic | Explicit revised target and dated amendment resolve retained original text;5% uplift versus allowance conventions explain historical enrollment rounding. Power-method assumptions are separately assigned to the statistical lane. | CONTEXT_RESOLVES |
| Protocol/SAP administrative sites, dates, source-check percentages, historical ARISCAT1627/1624 and ordinary visit/contributor counts | These are peripheral/historical details and do not change a result, primary/key secondary analysis population or planned decision rule in the numeric lane. | PERIPHERAL_COMPARISON |

## Limits and handoff

Numeric scope completed:110/110 relationships; six sources,100/100 mapped pages. No raw participant data, unprinted graph coordinates, individual continuous-variable contributor counts or exact risk-set conventions are available. Such absent definitions are not filled by assumptions. Two findings require independent inclusion screening and direct-source recheck. No candidate IDs, severity or adjudication assigned. Durable paths:relationships/numeric_relationship_inventory.md and checkers/numeric_consistency.md.
