# Mechanical evidence recheck and classification confirmation

Pending Human Adjudication. Combined stable scope: C001, C002, C003, C004, C005, C006, C007. The initial fresh rechecker covered six IDs; a different fresh rechecker covered appended C007 in the lossless section below. Every registered source location was reread against its supplied-source page image. No stable ID is removed, and evidence states are mechanical evidence-record facts only.

The complete scope, review contract, report specification, settings, performance profile, tooling record, current source inventory, current candidate ledger, initial inclusion screen and cited checker findings were read. This recheck uses only supplied-package evidence. Current native/layout extractions locate text; source-matched page images establish the printed statements, values, row alignment and sign. No earlier review conclusions, external sources, raw data or unreported model internals were used.

## Confirmed classification table

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Classification confirmation |
|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | PLAN SAP p.5 versus REPORT main pp.3,7 and results supplement pp.21,22 | reproduced | Confirmed; prospective composite differs from reported composite. |
| C002 | protocol_report | P_R | P_R | PLAN protocol p.9 and SAP pp.2,3 versus REPORT main pp.3,8,9 and results supplement pp.1,23 | reproduced | Confirmed; named planned secondary objective contrasts with reported post hoc expansion. |
| C003 | protocol_report | P_R | P_R | PLAN SAP pp.5,7 versus REPORT main pp.3,9,10 | reproduced | Confirmed; primary-outcome subgroup specification differs. |
| C004 | statistical_results | S_W | S_W | REPORT main p.6 adjusted time-effect columns and p.3 method context | reproduced | Confirmed; distinct adjusted estimands lack a source-defined mapping within one report. |
| C005 | statistical_results | S_W | S_W | REPORT results supplement p.1 index versus p.24 residual caption and graph | reproduced | Confirmed; main p.9 corroborates one reading and adds no relationship. |
| C006 | statistical_results | S_W | S_W | REPORT results supplement p.17 LDL interval versus same-display mean/SD comparator rows | reproduced | Confirmed; reproducing-method comparison within one result table. |

Roles were determined by content: the protocol and SAP state prospective objectives and analyses; the main pages report trial analyses and results; supplement p.1 indexes the named reported displays, and pp.17,21–24 contain trial-result tables or figures. The supplement's operational PLAN pages 2–16 are not conflicting locations for these IDs. Each ID has only one relationship code, so precedence P_R > P_P > S_C > S_W requires no mixed-code selection. Agreement or corroboration between locations does not create an additional relationship. No role, relationship or domain adjustment is required.

## C001 — Statin component absent from the reported in-hospital composite

**Finding IDs:** F-XS-001, F-ST1-502. **Evidence state:** reproduced. **Determining recheck fact:** the prospective in-hospital definition visibly includes statin, and every registered REPORT definition visibly omits it; the main report explicitly states that its predefined in-hospital statin data were not collected. No value or location adjustment was required.

| Exact location found and role | Source value/text matched | Comparator match and affected result |
|---|---|---|
| PLAN [SAP p.5, §6.1.2, printed lines 1149–1151](../../../joi170166supp2_prod.pdf#page=5) | Optimal in-hospital medication includes aspirin, ADP receptor antagonist [clopidogrel, prasugrel, or ticagrelor], heparin, statin and beta blocker. | Five-component prospective definition located; it is the comparator for all four REPORT occurrences below. |
| REPORT [main p.3, Outcomes, lower left column](../../../jama_huffman_2018_oi_170166.pdf#page=3) | Aspirin, ADP receptor antagonist, anticoagulant and β-blocker; the same sentence says in-hospital statin was additionally predefined but data were not collected. | Four reported components match the registered comparison and explicit noncollection statement. Discharge medication continuation at the top of the right column includes statin and is a separate endpoint. |
| REPORT [main p.7, Table 3, optimal in-hospital medication row and footnote c](../../../jama_huffman_2018_oi_170166.pdf#page=7) | Footnote c lists aspirin, ADP antagonist, anticoagulant and β-blocker among patients eligible for all medications; no statin. | Control 3122 (31.7%), intervention 3878 (35.8%); cluster-adjusted difference 8.61 (6.98–10.23), OR 1.70 (1.57–1.85); primary difference 6.00 (3.90–8.11), OR 1.45 (1.28–1.64). All printed values and row alignment match. |
| REPORT [results supplement p.21, eTable 5, corresponding row and footnote c](../../../joi170166supp3_prod.pdf#page=21) | Same four-component definition using anticoagulant; no statin. | GRACE OR 2.19 (1.83–2.62), transfer OR 1.47 (1.29–1.66), insurance OR 1.45 (1.28–1.64), prehospital aspirin OR 1.47 (1.30–1.66). All four affected sensitivity results match. |
| REPORT [results supplement p.22, eTable 6, corresponding row and footnote b](../../../joi170166supp3_prod.pdf#page=22) | Aspirin, ADP antagonist, heparin and beta-blocker among patients eligible for all medications; no statin. | Exposure-time interaction analysis OR 0.87 (0.70–1.07) matches. |

**Applicable consistency rule and logical reproduction:** focus area D and Route A, category 5 protect a planned-versus-reported composite-definition comparison. Set comparison finds statin in the PLAN conjunction and absent from every REPORT conjunction. The anticoagulant/heparin wording is not a separate registered difference. Reported definitions agree with each other. The in-hospital and discharge endpoints were distinguished before comparison.

**Display-precision check:** this is a categorical component-set comparison. Half-unit numeric intervals and a relative discrepancy do not apply; rounding cannot make a four-component definition contain statin. The associated printed results are located rather than recomputed as a five-component result.

**Necessary inputs and exact missing inputs:** the planned component list, reported component lists, disclosure and associated modeled results are available. Statin observations, a five-component outcome count, the eligibility set for that outcome, and a dated amendment documenting the component change are not supplied. The supplied aggregate results cannot reconstruct them.

**Alternative source-grounded interpretation:** omission is a disclosed adaptation to noncollection. A later prospective amendment could establish the adapted four-component endpoint, but none is supplied here. Removing a component may also change eligibility; that possible consequence is not established from patient data.

**Direct observation versus inferred explanation:** the five-versus-four list and disclosure are direct observations. Amendment timing, approval and participant-level effects are explanations or consequences that this recheck does not establish.

**Classification:** PLAN SAP versus REPORT main/results tables gives primary P_R, all relationships P_R and review domain protocol_report. No P_P, S_C or S_W inconsistency is demonstrated by the corroborating definitions. Role ambiguity: none. Possible undisclosed amendment is an endpoint-history uncertainty, not a role uncertainty.

**Exact remaining human question:** Was the optimal in-hospital medication endpoint prospectively redefined to omit statin, and which dated definition and eligibility rule accompanies the reported four-component counts and modeled results relative to the five-component endpoint in the supplied SAP?

## C002 — Planned secondary expanded MACE versus reported post hoc expansion

**Finding IDs:** F-XS-003, F-ST1-503. **Evidence state:** reproduced. **Determining recheck fact:** both prospective documents name in-hospital and 30-day expanded MACE as secondary objectives, while the main report repeatedly calls its specified expansion post hoc. The planned expansion's unprovided component definition remains an explicit identity uncertainty. No value or location adjustment was required.

| Exact location found and role | Source value/text matched | Comparator match and affected result |
|---|---|---|
| PLAN [protocol p.9, §2.2.3, printed lines 259–263](../../../joi170166supp1_prod.pdf#page=9) | Under Secondary Objectives, evaluation includes in-hospital and 30-day expanded MACE. | The named objective and its prospective secondary placement match. The adjacent §2.3 defines ordinary four-component MACE, not the expanded composite. |
| PLAN [SAP p.2, §2.1.2, printed lines 1071–1072](../../../joi170166supp2_prod.pdf#page=2) | Secondary-objective bullet begins the intervention comparison and ends this page with in-hospital and… | Exact beginning of the comparator found, rather than attributing the whole sentence solely to p.3. |
| PLAN [SAP p.3, printed lines 1073–1074](../../../joi170166supp2_prod.pdf#page=3) | Continuation includes discharge advice, and in-hospital and 30-day expanded MACE. | The page-spanning secondary objective matches the protocol. No expanded component list is supplied in this statement. |
| REPORT [main p.3, Outcomes continuation and Statistical Analysis](../../../jama_huffman_2018_oi_170166.pdf#page=3) | Both passages describe post hoc analyses adding incident in-hospital heart failure, cardiogenic shock and cardiac arrest. | Repeated post hoc status and specified expansion match, separately from the caution that other secondary analyses are exploratory after no multiplicity adjustment. |
| REPORT [main p.8, Secondary and Post Hoc Analyses, lower right column](../../../jama_huffman_2018_oi_170166.pdf#page=8) | A post hoc analysis evaluates 30-day MACE plus the three incident in-hospital outcomes; unadjusted intervention 7.0% versus control 9.1%, cluster OR 0.89 (0.80–1.00). | Status, component description, rates and cluster result match. |
| REPORT [main p.9, result continuation below Figure 3 and Discussion](../../../jama_huffman_2018_oi_170166.pdf#page=9) | Continuation gives adjusted difference −1.34% (−2.72% to 0.04%) and OR 0.84 (0.70–1.00); Discussion again calls the expansion post hoc. | Primary-model numerical results and repeated status match. |
| REPORT [results supplement p.1, eTable 7 contents entry](../../../joi170166supp3_prod.pdf#page=1) | Exploratory analysis title names MACE plus in-hospital incident heart failure, cardiogenic shock and cardiac arrest. | Named display, components and title status match p.23. |
| REPORT [results supplement p.23, eTable 7 title, expanded-composite row and footnote a](../../../joi170166supp3_prod.pdf#page=23) | Same exploratory title; control 919 (9.1%), intervention 795 (7.0%); cluster difference −0.86 (−1.72 to −0.01), OR 0.89 (0.80–1.00); primary difference −1.34 (−2.72 to 0.04), OR 0.84 (0.70–1.00). | All registered values match. Footnote distinguishes cluster-only from temporal adjustment; ordinary MACE components are death, reinfarction, stroke and major GUSTO bleeding. |

**Applicable consistency rule and logical reproduction:** focus area D; Route A, category 5. Compare the named prospective secondary expanded-MACE objective with the specifically expanded result described as post hoc. The report explicitly gives the added components; the prospective passages do not. The observation is the status/definition contrast and unresolved identity mapping, not a claim that every exploratory label changes outcome hierarchy. The two plans agree, and the REPORT repetitions agree.

**Display-precision check:** prespecification, outcome status and component identity are categorical. Numeric half-unit intervals and relative discrepancies are inapplicable to that contrast. Numerical report copies match their respective models; no additional interval/test conflict is claimed from the printed OR upper limit 1.00.

**Necessary inputs and exact missing inputs:** dates and content of the supplied protocol/SAP, objective placement, reported expanded components, status statements and results are available. The prospective expanded-MACE component set, analysis specification and any later dated amendment are absent. Thus exact equivalence of the broad planned objective and the reported seven-component outcome cannot be determined.

**Alternative source-grounded interpretation:** the planned broad expansion could denote a different endpoint, with the particular heart-failure/shock/arrest expansion selected later. Alternatively, the specific reported endpoint could implement the already named secondary objective. Both readings remain possible because the plan does not identify its added components.

**Direct observation versus inferred explanation:** secondary placement and repeated post hoc characterization are direct observations. Their reason and exact endpoint identity are not observed. This recheck does not infer analysis timing or a specific amendment.

**Classification:** the conflicting status descriptions lie across PLAN and REPORT, giving primary P_R, all relationships P_R and protocol_report. Agreement between plans adds no P_P; agreeing report titles/narrative add no S_C or S_W. Roles have no ambiguity. Composite identity is a bounded substantive ambiguity retained for human review.

**Exact remaining human question:** Does eTable 7's MACE-plus-heart-failure/shock/arrest outcome implement the prospective secondary expanded-MACE objective, or is it a distinct post hoc expansion, and which dated component definition and outcome status applies to extracting its reported results?

## C003 — Reported prespecified primary-MACE subgroup set differs from the supplied plan

**Finding IDs:** F-XS-002, F-ST1-504. **Evidence state:** reproduced. **Determining recheck fact:** the SAP's a priori primary-endpoint subgroup list contains age <65/>65 and toolkit use, while the report's prespecified Figure 3 uses <50/50–69/≥70 and hospital type and supplies no toolkit-use primary-MACE result. No value or location adjustment was required.

| Exact location found and role | Source value/text matched | Comparator match |
|---|---|---|
| PLAN [SAP p.7, §7.5.2, printed lines 1243–1254](../../../joi170166supp2_prod.pdf#page=7) | A priori subgroups under primary endpoint analyses: hospital size; use of quality-improvement toolkit components; age <65 and >65 years; sex; STEMI versus NSTEMI. | All five planned characteristics and the exact printed age partition match. The equality boundary at 65 is not added as an issue. |
| PLAN [SAP p.5, §6.1.3, printed lines 1156–1165](../../../joi170166supp2_prod.pdf#page=5) | Toolkit downloads and meeting frequency can be used in subgroup analyses to evaluate whether intervention effect is modified by toolkit use. | Supporting specification for toolkit-use effect modification found; it does not specify government/nonprofit/private or the reported age bands. |
| REPORT [main p.3, Statistical Analysis and separate process-evaluation statement](../../../jama_huffman_2018_oi_170166.pdf#page=3) | Results reported by prespecified age, sex, STEMI/NSTEMI, hospital size and hospital type, with interaction testing; mixed-methods process evaluation will be reported separately. | Both the reported subgroup list and bounded deferral statement match. The latter does not identify a deferred primary-MACE toolkit-use subgroup result. |
| REPORT [main p.9, Figure 3 title, age/hospital-type rows and narrative](../../../jama_huffman_2018_oi_170166.pdf#page=9) | Title and narrative call the displayed primary 30-day MACE subgroups prespecified. Three age groups and three hospital-type groups are printed. | Exact counts, adjusted differences and ORs are separately matched below. No toolkit-use row appears in the complete 14-row figure. |
| REPORT [main p.10, opening Discussion paragraph](../../../jama_huffman_2018_oi_170166.pdf#page=10) | Primary outcome results described as consistent across prespecified individual- and hospital-level subgroups. | Repeated prespecified characterization found. |

The affected Figure 3 rows are source-matched as follows. Event counts/total (%) are intervention then control, and differences are the displayed intervention-minus-control adjusted differences.

| Figure 3 row | Intervention | Control | Adjusted difference (95% CI) | Adjusted OR (95% CI) |
|---|---|---|---|---|
| Age <50 | 58/2079 (2.8) | 68/2045 (3.3) | 1.42 (−0.71 to 3.54) | 1.53 (0.83–2.79) |
| Age 50–69 | 297/6606 (4.5) | 326/5863 (5.6) | −0.57 (−2.02 to 0.88) | 0.89 (0.67–1.19) |
| Age ≥70 | 247/2623 (9.4) | 251/2158 (11.6) | −0.23 (−3.32 to 2.85) | 0.98 (0.71–1.35) |
| Government (n=9 hospitals) | 158/3036 (5.2) | 275/4097 (6.7) | −0.55 (−2.56 to 1.47) | 0.90 (0.61–1.33) |
| Nonprofit (n=12 hospitals) | 186/2964 (6.3) | 193/2785 (6.9) | −0.62 (−3.43 to 2.20) | 0.91 (0.59–1.40) |
| Private (n=42 hospitals) | 258/5308 (4.9) | 177/3184 (5.6) | 0.89 (−1.19 to 2.97) | 1.16 (0.82–1.64) |

**Applicable consistency rule and logical reproduction:** focus area D; Route A, category 5. Hospital size, sex and STEMI/NSTEMI match. Reported age bands differ from the prospective partition; reported hospital type has no located prospective subgroup specification; planned toolkit-component use has no located reported primary-MACE subgroup result. These are one subgroup-specification pattern, with all repeated prespecified claims retained.

The complete current-source native/layout text for the protocol and SAP was searched for subgroup, hospital type, age cutpoints and toolkit components. The relevant prospective subgroup hits locate the SAP sections reread visually above, with no additional specification for the reported age bands or hospital type. The complete current-source main/results text was searched for toolkit-use primary-MACE analysis, and the report's subgroup display and narrative were inspected; none is supplied. These absence statements are confined to this package, not to publications or documents outside it.

**Display-precision check:** categorical subgroup sets and partitions are not half-unit estimates. Rounding cannot transform two age groups into the reported three groups or hospital type into toolkit use. The printed adjusted effects are attached results, not values recomputed from crude event ratios.

**Necessary inputs and exact missing inputs:** prospective subgroup list, implementation-measure context, reported rows, labels and repeated status claims are available. A dated specification establishing the reported age partition and hospital-type analyses, and a primary-MACE toolkit-use result or explicit replacement/deferral document, are absent. No participant-level reassignment or interaction statistic is reconstructed.

**Alternative source-grounded interpretation:** a later prospective analysis specification may have changed the age bands, added hospital type and replaced/deferred toolkit use. The promised separate process evaluation may address implementation, but its statement does not show whether it contains this primary-outcome subgroup analysis.

**Direct observation versus inferred explanation:** planned and reported subgroup lists, figure rows and reported prespecified claims are direct observations. The reason for changes, amendment timing and any content of an unsupplied separate paper are not observed.

**Classification:** PLAN SAP versus REPORT main gives primary P_R, all relationships P_R and protocol_report. The report's repeated claims agree, adding no S_W, and no second REPORT is a conflicting comparator. Role ambiguity: none. A possible later specification is retained as a substantive uncertainty.

**Exact remaining human question:** Which dated prospective specification establishes Figure 3's three age bands and hospital-type analyses as prespecified, and where is the SAP's primary-MACE toolkit-use subgroup analysis reported or documented as replaced or deferred?

## C004 — Distinct adjusted time contrasts lack an estimand mapping

**Finding ID:** F-ST1-001. **Evidence state:** reproduced. **Determining recheck fact:** both time rows contain the registered distinct adjusted effects under headings sharing the same method footnote, without a source-defined mapping of their respective estimands/models. This is a reproduction of the mapping gap, not a rule requiring distinct valid estimands to equal each other. No value or location adjustment was required.

**Locations found and values matched:** REPORT [main p.6, Table 2 title, both time rows, both effect headings, footnotes b/c](../../../jama_huffman_2018_oi_170166.pdf#page=6). The title says process/time outcomes are adjusted for within-hospital clustering and temporal trends. Both adjusted-effect headings cite b; c identifies the final time-row effects as β-coefficients. Footnote b describes intervention-versus-control effects and intervention-minus-control marginal effects in mixed-effects logistic or quantile models with a hospital random-effects term and temporal adjustment. REPORT [main p.3, Statistical Analysis](../../../jama_huffman_2018_oi_170166.pdf#page=3) supplies hospital/time analysis context but no row-specific mapping of the two time columns.

| Source row | Control median (IQR), n | Intervention median (IQR), n | Difference (95% CI) | β (95% CI) |
|---|---|---|---|---|
| Door-to-balloon, STEMI, minutes | 65 (53–105), 4022 | 77 (55–118), 3639 | 6.18 (−4.78 to 17.14) | 13.00 (3.64–22.36) |
| Door-to-needle, STEMI, minutes | 44 (30–67), 1455 | 45 (27–75), 1433 | 0.40 (−5.23 to 6.03) | 5.00 (−5.20–15.20) |

Both values and comparators match the source image. The shared Difference heading includes a percent sign; the candidate concerns the analysis mapping rather than the readily recognized time-unit label. No adjusted estimate is equated with a crude difference of these arm medians.

**Applicable rule and logical reproduction:** focus areas B/C; Route B. In-focus method/estimate logic requires enough mapping to identify the analysis generating an extracted adjusted result. The β label distinguishes a parameter name but the shared source footnote does not distinguish a marginal effect, conditional quantile coefficient, separate model or transformed estimand for these rows. The magnitude and, for door-to-balloon, null-inclusion interpretation depend on which quantity is extracted. No P value or test is supplied for these rows, so this is not an interval-versus-test observation.

**Display-precision calculation:** printed point-value intervals are [6.175,6.185] and [12.995,13.005], gap 6.810, relative to 6.18 equal to 1.10194175; and [0.395,0.405] and [4.995,5.005], gap 4.590, relative to 0.40 equal to 11.475. These establish distinct numbers beyond display precision, not interchangeability or an arithmetic obligation that the numbers agree.

All endpoint half-unit intervals are reproduced:

| Row/column | Lower endpoint interval | Upper endpoint interval | Null inclusion at all allowed rounding values |
|---|---|---|---|
| Door-to-balloon Difference | [−4.785,−4.775] | [17.135,17.145] | Includes 0 |
| Door-to-balloon β | [3.635,3.645] | [22.355,22.365] | Excludes 0 |
| Door-to-needle Difference | [−5.235,−5.225] | [6.025,6.035] | Includes 0 |
| Door-to-needle β | [−5.205,−5.195] | [15.195,15.205] | Includes 0 |

Every point remains inside its own ordered interval. No interval or point value is reconstructed from unreported covariance or degrees of freedom.

**Necessary inputs and exact missing inputs:** printed estimates/intervals, row units, displayed arm contributor counts, model-family statement and adjustment context are available. For each column and row, the estimand, quantile level, exact scale/transformation, distinct model specification, marginalization procedure and any distinct analysis population are not supplied. These are the inputs needed to identify and independently generate each contrast; the recheck does not infer them from the crude medians.

**Alternative source-grounded interpretation:** the Difference column may give a marginal time effect and the β column a conditional quantile coefficient; different quantiles, transformations, contributing populations or adjustment models could produce distinct legitimate summaries. The source names quantile models and β but does not state that mapping.

**Direct observation versus inferred explanation:** distinct printed effects, their interval null inclusion and the shared incomplete mapping are directly observed. Specific marginal/conditional or model explanations are alternatives, not established generating procedures.

**Classification:** both compared columns and their explanatory context are REPORT content in one main article, giving primary S_W, all relationships S_W and statistical_results. This concerns estimates and statistical-method logic, not misattribution to another outcome or time point. Role/classification ambiguity: none; estimand identity remains unresolved.

**Exact remaining human question:** Which estimand, model, units/scale, quantile level, adjustment terms, marginalization procedure and analysis population generated each adjusted effect column for door-to-balloon and door-to-needle time, and how should the respective 6.18/13.00 and 0.40/5.00 results and intervals be distinguished in extraction?

## C005 — Opposing directional readings of the named hospital residual display

**Finding ID:** F-ST1-505. **Evidence state:** reproduced. **Determining recheck fact:** the same eFigure 1A is indexed as Expected minus Observed while its caption assigns negative/left departures to lower hospital MACE and positive/right departures to higher hospital MACE. The quantitative reference/scale alternative is retained; exact hospital numbers are not inferred. No value or location adjustment was required.

| Exact location found and role | Source text/value matched | Comparator match |
|---|---|---|
| REPORT [results supplement p.1, eFigure 1A index](../../../joi170166supp3_prod.pdf#page=1) | Residual of 30-day MACE rate, with the parenthetical subtraction order Expected – Observed, by individual hospitals. | Exact plot name and subtraction order match the registered index reading. |
| REPORT [results supplement p.24, eFigure 1A graph and complete caption](../../../joi170166supp3_prod.pdf#page=24) | Residual axis ticks −3,−2,−1,0,1,2; hospital rank order increases left to right, with clearly negative points on the left and positive points on the right. Caption describes predicted MACE rates from a hospital/time-adjusted mixed logistic model, hospital-level departures from mean MACE with residual 0, and left lower/right higher than the mean. | Both directional caption statements, model context, nonzero signs and zero reference match. Caption also says a hospital CI excluding zero differs from the mean at 5%. |
| REPORT [main p.9, narrative below Figure 3](../../../jama_huffman_2018_oi_170166.pdf#page=9) | eFigure 1A evaluates site event rate compared with mean event rate throughout the entire trial. | This corroborates the caption's primary-outcome mean-reference description; it is not a conflicting comparator. |

**Applicable rule and logical reproduction:** focus area B; Route A, category 2. For the literal index reading r=E−O, O>E implies r<0 and O<E implies r>0. The caption gives a positive departure to hospitals higher than the reference mean, and negative departure to hospitals lower than that mean. Under a common expected/reference quantity and scale, these are opposing directions. The index is first assessed against the peripheral-heading rule: it supplies subtraction order for a signed primary-outcome hospital result, which changes interpretation of nonzero departures, rather than merely locating a panel.

**Display-precision check:** the observed conflict is between directional definitions. Exact hospital residual values, expected/observed pairs and interval endpoints are not printed, so no truthful half-unit numeric interval or relative magnitude discrepancy can be calculated for a hospital. No decimal ordinates, hospital IDs or event counts were digitized. Clear negative and positive graph signs establish the direction comparison; arbitrary rounding intervals around unseen numerical values are not used to reconcile the definitions.

**Necessary inputs and exact missing inputs:** exact index wording, plot name, visible signed axis/points, caption direction and model context are available. The precise residual formula, subtraction order used in computation, whether the scale is event probability or log odds or a hospital random effect, how expected is related to the trial mean, and individual hospital values/contributors are not supplied. Thus the literal index calculation is a logical comparison, not numerical reconstruction of the plotted model.

**Alternative source-grounded interpretation:** the plotted quantity may be a predicted hospital departure or random effect on the model scale, while the index uses expected-minus-observed wording for a different residual quantity. Expected may also differ from the caption's mean reference. The caption explicitly mentions modeled predicted rates, supporting those alternatives. They could distinguish two residual definitions but the source does not state which formula/scale applies to the same named display.

**Direct observation versus inferred explanation:** opposing printed reference descriptions, axis signs and caption direction are direct observations. Equating expected to the caption mean is the explicit condition of the direction logic, not an independently supplied formula. A random-effect interpretation or different scale is a source-grounded possible explanation, not a confirmed computation. No change to the trial-wide intervention effect is inferred.

**Classification:** p.1's entry describes a trial-result figure and p.24 presents that result; both are REPORT in the same supplement. Primary S_W, all relationships S_W, statistical_results. The main article only corroborates one reading and creates no S_C relationship. Role ambiguity: none. The exact residual reference and scale remain a bounded interpretive ambiguity.

**Exact remaining human question:** What formula, subtraction order, reference quantity and scale generated eFigure 1A, and does a positive plotted residual denote higher or lower hospital MACE relative to that reference, given the index's Expected−Observed description and caption's positive/higher interpretation?

## C006 — LDL interval differs from the same-display reproducing calculation

**Finding ID:** F-ST1-501. **Evidence state:** reproduced. **Determining recheck fact:** exact eTable 1 LDL inputs and limits match the registration, and the calculation reproducing the other same-display mean/SD rows yields endpoint ranges separated from the printed LDL limits by more than 5% after full half-unit input intervals. LDL-specific contributors and generating procedure remain absent. No value or location adjustment was required.

**Location found:** REPORT [results supplement p.17, eTable 1 title, complete/missing group headers, LDL row and all five comparator mean/SD rows](../../../joi170166supp3_prod.pdf#page=17). Headers are complete follow-up n=21079 and missing follow-up n=295. The table prints Difference (95% CI). These are complete/missing groups, not randomized arms. The footnote's intervention/control terminology is not used to infer an adjusted randomized treatment contrast.

Every input and printed comparator is visually source-matched:

| Row | Complete mean (SD) | Missing mean (SD) | Printed difference (95% CI) |
|---|---|---|---|
| Age, years | 60.6 (12.1) | 60.0 (11.6) | −0.6 (−2.0 to 0.8) |
| Weight, kg | 63.5 (9.7) | 62.6 (9.3) | −0.9 (−2.0 to 0.2) |
| Systolic pressure, mmHg | 138.5 (28.9) | 138.9 (32.5) | 0.4 (−2.9 to 3.7) |
| Heart rate, bpm | 79.9 (18.9) | 82.9 (19.1) | 3.0 (0.8 to 5.2) |
| Hemoglobin, printed mg/dl | 13.2 (2.0) | 13.2 (2.1) | 0.0 (−0.3 to 0.2) |
| LDL cholesterol, mg/dl | 122.4 (40.8) | 131.4 (46.0) | 9.0 (3.2 to 14.8) |

**Applicable rule and reproduced calculation:** focus areas B/C; Route A, category 4. This is a method that reproduces other rows of the same display, not a claim that the authors used it or a recommendation to adopt it. Define d=meanMissing−meanComplete, pooled variance v=((nC−1)sC²+(nM−1)sM²)/(nC+nM−2), SE=sqrt(v(1/nC+1/nM)), and endpoints d±1.96SE. The multiplier is a reproducing normal approximation. No LDL-generating degrees of freedom are asserted.

With the printed inputs, LDL gives d=9.0, SE=2.3964893360, and endpoints 4.3028809014 and 13.6971190986. The point difference reconciles: recomputed mean-difference range [8.90,9.10] overlaps printed 9.0's interval [8.95,9.05]. The discrepancy concerns the interval endpoints, not the point estimate, containment or endpoint order.

**Full display-precision calculation:** each one-decimal mean and SD takes ±0.05; conservatively the displayed group totals take ±0.5, nC in [21078.5,21079.5] and nM in [294.5,295.5]. Thus LDL mean/SD input intervals are [122.35,122.45], [40.75,40.85], [131.35,131.45], [45.95,46.05]. All 64 corners of the six-input rectangle were independently evaluated with JavaScript. Means affect d monotonically; both positive SDs increase SE. For these input ranges, SE decreases monotonically with nC and nM, as checked from the pooled variance expression; the corner extrema therefore bound the full interval rectangle, rather than sampling internal values. Although participant totals are counts, allowing fractional half-units is conservative for this check.

The resulting same-method ranges and printed-limit intervals are:

| Row | Recomputed endpoints at printed inputs | Full lower endpoint range | Full upper endpoint range | Printed lower interval | Printed upper interval |
|---|---|---|---|---|---|
| Age | −1.98965319, 0.78965319 | [−2.09656791,−1.88275104] | [0.68275104,0.89656791] | [−2.05,−1.95] | [0.75,0.85] |
| Weight | −2.01402075, 0.21402075 | [−2.12070452,−1.90734897] | [0.10734897,0.32070452] | [−2.05,−1.95] | [0.15,0.25] |
| Systolic pressure | −2.92697797, 3.72697797 | [−3.03550242,−2.81847022] | [3.61847022,3.83550242] | [−2.95,−2.85] | [3.65,3.75] |
| Heart rate | 0.82785750, 5.17214250 | [0.72028958,0.93541117] | [5.06458883,5.27971042] | [0.75,0.85] | [5.15,5.25] |
| Hemoglobin | −0.22998469, 0.22998469 | [−0.33592720,−0.12405228] | [0.12405228,0.33592720] | [−0.35,−0.25] | [0.15,0.25] |
| LDL | 4.30288090, 13.69711910 | [4.19321414,4.41252805] | [13.58747195,13.80678586] | [3.15,3.25] | [14.75,14.85] |

Age, weight, systolic pressure and heart-rate endpoints already reproduce at printed inputs. For hemoglobin, a mean difference of −0.05 achievable inside the displayed mean intervals with the displayed SDs gives endpoints approximately −0.27998469 and 0.17998469; both match the printed endpoint intervals and the displayed point-difference interval. Thus the comparator method jointly reproduces the hemoglobin row too. All five comparator rows have zero interval gap and relative discrepancy zero after display precision.

For LDL the closest lower-limit gap is 4.1932141427−3.25=0.9432141427, divided by |3.2| gives 0.2947544196. The upper-limit gap is 14.75−13.8067858573=0.9432141427, divided by |14.8| gives 0.0637306853. Both exceed 0.05. Using exact integer group counts would not bridge these conservative gaps. These are interval-limit comparisons, not a model-versus-crude treatment contrast or a peripheral comparison with a copied baseline table.

**Necessary inputs and exact missing inputs:** same-display means, SDs, group totals, printed differences/limits and 95% level are available. Actual complete/missing LDL assay contributor counts, row-specific missingness, generating interval procedure and any LDL-specific variance estimator or degrees of freedom are absent. The full analysis cannot be independently regenerated from the package alone. The table does not state that every patient contributed LDL.

**Alternative source-grounded interpretation:** fewer LDL assay contributors than the header group totals could widen its CI. LDL may also use a distinct interval procedure. Clinical measurement rows have no individual contributor counts, so these are explicit unresolved alternatives. Category 4 records the unstated producing method as the human question even though another same-display method reproduces five rows.

**Direct observation versus inferred explanation:** printed inputs/limits and their numerical separation under the stated reproducing method are direct reproducible facts. The authors' actual method, assay availability, or source of interval width is not established. No proposed replacement result is supplied.

**Classification:** all conflicting numeric content is REPORT in the same eTable 1, giving primary S_W, all relationships S_W and statistical_results. Roles and classification have no ambiguity; producing counts and method are unresolved.

**Exact remaining human question:** What complete- and missing-follow-up LDL contributor counts and confidence-interval procedure generated 9.0 mg/dL (95% CI 3.2–14.8), given the same-display reproducing calculation and its surviving endpoint gaps when the printed group totals are used?

## Direct-source confirmation, derivative provenance and limits

Seventeen unique physical source pages were visually reread: main pp.3,6,7,8,9,10; protocol p.9; SAP pp.2,3,5,7; results supplement pp.1,17,21,22,23,24. All cited affected locations were available. Source statements, values, units, columns and captions above were confirmed on current-source renderings, rather than accepted from text extraction alone.

Current-run page images inspected unchanged were `preprocessing/curator/main3.png`, `main-6.png`, `main-7.png`, `main-8.png`, `main-9.png`, `main-10.png`, `sap7.png`, `supp3-17.png`, `supp3-21.png`, `supp3-22.png`, `supp3-23.png`, `supp3-24.png`; and `preprocessing/cross/protocol9.png`, `sap3.png`, `sap5.png`. These are direct current-source Poppler CPU renderings whose source correspondence is recorded by the run's curator/checker provenance. The source integrity baseline is `source_hashes_before.sha256`; no source or reused asset was modified.

Two fresh derivatives were needed for pages without an existing current-run image in the cited scope:

| Fresh derivative, run-relative path | Direct source and truthful page | Engine, device and exact command |
|---|---|---|
| preprocessing/recheck/sap2.png | joi170166supp2_prod.pdf, physical p.2 | Poppler pdftoppm 25.03.0, CPU; `pdftoppm -f 2 -l 2 -singlefile -scale-to 1800 -png joi170166supp2_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck/sap2` |
| preprocessing/recheck/supp3-1.png | joi170166supp3_prod.pdf, physical p.1 | Poppler pdftoppm 25.03.0, CPU; `pdftoppm -f 1 -l 1 -singlefile -scale-to 1800 -png joi170166supp3_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck/supp3-1` |

Current-run `preprocessing/screen-initial/` native/layout text was used for bounded complete-document term searches and page location, not as final authority for candidate statements. Arithmetic was independently performed in JavaScript, with no Python review/extraction or OCR. No fallback environment was required. The recorded device is CPU throughout.

Remaining limitations are candidate-specific missing definitions, not missing cited pages: C001 amendment and five-component eligibility/result; C002 prospective expanded component identity; C003 later subgroup specification and toolkit-use result; C004 separate time estimand/model mapping; C005 residual formula/reference/scale and exact hospital values; C006 assay contributor counts and CI construction. All six IDs remain Pending Human Adjudication.
# Appended candidate evidence recheck

Assigned scope: C007 only, registered from F-ST2-501. The complete `QUALITY_CONTROL_SCOPE.md`, complete `workflow_1_6_2/review_contract.md`, recorded CPU tooling, C007 ledger card, pass-2 inclusion screen, and pass-2 support finding were read. Scientific conclusions below were independently checked against the supplied current PDFs. Existing extraction and current-source images were preserved; locators alone were not treated as final authority. This part does not modify the ledger or any other candidate.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state |
|---|---|---|---|---|---|
| C007 | protocol_report | P_R | P_R | PLAN SAP pp.6,7 vs REPORT main pp.3,6,7 and results supplement pp.17,21,22,23 | reproduced |

## C007 — Planned complete-case primary-MACE sensitivity result is not identified

**Finding provenance:** F-ST2-501, statistical pass 2 support. **Status:** Pending Human Adjudication.

### Locations found, source transcription, comparator and document roles

All nine registered physical PDF pages were located and visually reread from current-source renderings. Their text and table alignment match the registered source comparison. The following table separately identifies every registered location; all source links use physical PDF pages.

| Exact source location | Content-based role and location found | Source value/text matched and function in comparison |
|---|---|---|
| [SAP p.6, §7.1 lines 1190–1198 and §7.2 lines 1205–1210](../../../joi170166supp2_prod.pdf#page=6) | PLAN; found. Prospective statistical analysis specification, dated 17 June 2015. | §7.1 specifies intention to treat unless otherwise specified and says the methods below handle missing data for primary and secondary endpoints. §7.2 identifies data not obtained at 30-day assessment following outpatient follow-up or three telephone attempts as missing. It expressly states that sensitivity analyses will use complete case analysis and multiple imputation to evaluate missing outcomes. This is the planned-method source statement. |
| [SAP p.7, §7.5 lines 1229–1238](../../../joi170166supp2_prod.pdf#page=7) | PLAN; found. Prospective primary-endpoint analysis. | Primary outcome is 30-day MACE; the primary analysis uses mixed-effects logistic regression with random hospital effects and fixed time effects in four-month periods. This links the p.6 missing-data provision to the primary outcome. The conditional hospital-imbalance sensitivity is separate contextual content. |
| [Main p.3, Outcomes and Statistical Analysis](../../../jama_huffman_2018_oi_170166.pdf#page=3) | REPORT; found. Description of the conducted trial and reported analyses. | Outcomes says an unreachable participant after three attempts was considered lost to follow-up. Statistical Analysis specifies the primary mixed-effects logistic model with random hospital and fixed four-month time terms, says all results are reported using intention-to-treat analysis, and names other adjustment, exposure-time and subgroup analyses. It supplies no complete-case designation or missing-outcome model coding. |
| [Main p.6, follow-up paragraph beneath Table 2](../../../jama_huffman_2018_oi_170166.pdf#page=6) | REPORT; found. Trial follow-up and analysis-cohort description. | 295 participants had incomplete outcome data: 215 not followed by the enrolling site and 80 unreachable after three contact attempts. Intervention and control totals are 11,308 and 10,066, respectively. The paragraph points to eTable 1 for baseline characteristics of participants with and without follow-up, rather than a missing-outcome effect estimate. |
| [Main p.7, Table 3 primary-MACE row, footnote a, and Primary Analysis paragraph](../../../jama_huffman_2018_oi_170166.pdf#page=7) | REPORT; found. Observed primary results and reported sensitivity summaries. | Table 3 headers give control n=10,066 and intervention n=11,308. Primary 30-day MACE is 645 (6.4%) versus 602 (5.3%); the primary analysis difference is −0.09 percentage points (95% CI −1.32 to 1.14), OR 0.98 (0.80–1.21). Footnote a describes hospital clustering and additional temporal adjustment. The paragraph says results were similar after multiple imputation of missing follow-up data; hypothetical missing-follow-up-event scenarios and multiple imputation yielded a broader range of plausible results consistent with the primary analysis. It does not identify any of these results as the planned complete-case sensitivity. This is the principal REPORT comparator. |
| [Results supplement p.17, eTable 1 title, headers, table and footnote](../../../joi170166supp3_prod.pdf#page=17) | REPORT; found. Baseline summaries of actual trial participants. | The title identifies baseline characteristics by complete and missing follow-up, with complete follow-up n=21,079 and missing follow-up n=295. Rows contain baseline characteristics and their between-group differences, not a primary-MACE treatment effect. The term complete refers to follow-up availability; no complete-case primary-MACE analysis is identified. |
| [Results supplement p.21, eTable 5 title, primary row, column labels and footnotes](../../../joi170166supp3_prod.pdf#page=21) | REPORT; found. Observed covariate-adjusted outcome analyses. | Title and columns specify GRACE covariates, transfer status, insurance status and prehospital aspirin adjustment. The four primary-MACE ORs are 1.06 (0.77–1.44), 0.98 (0.80–1.21), 0.97 (0.79–1.20), and 0.99 (0.80–1.22). Neither labels nor footnotes designate a complete-case missing-outcome analysis. Matching the second OR to the main primary OR does not identify the contributing population or missing-data procedure. |
| [Results supplement p.22, eTable 6 title, primary row and footnotes](../../../joi170166supp3_prod.pdf#page=22) | REPORT; found. Observed analysis of intervention exposure time. | Title specifies adjustment for clustering, temporal trends and interaction with time exposed to intervention. Primary-MACE OR is 1.14 (0.76–1.70). This identifies an exposure-time analysis, without designating a complete-case missing-outcome sensitivity. |
| [Results supplement p.23, eTable 7 title, rows, headers and footnotes](../../../joi170166supp3_prod.pdf#page=23) | REPORT; found. Expanded-composite and component results. | Title explicitly names MACE plus in-hospital incident heart failure, cardiogenic shock and cardiac arrest. The expanded primary-analysis OR is 0.84 (0.70–1.00), and risk difference −1.34 (−2.72 to 0.04). The full-cohort headers and hospital/time model footnote do not designate a complete-case analysis of the original primary-MACE outcome. |

**Additional source-confirmed context:** [Main p.4, Figure 1 caption](../../../jama_huffman_2018_oi_170166.pdf#page=4), REPORT, expressly says that patients lost to follow-up were included in the analysis, after defining those participants as unreachable after three contacts or not followed by the site. This statement provides analysis-population context. It does not identify a complete-case sensitivity, specify missing-outcome coding, or distinguish the contributing population of each model. It adds no conflicting relationship and does not alter the exact compared-roles string in the classification table.

### Full REPORT missing-analysis search

Fresh native-text derivatives were generated directly from the complete main PDF (physical pp.1–12) and complete results-supplement PDF (physical pp.1–27), using recorded direct Poppler tooling on CPU. They were searched independently for complete-case, complete case, available-case, observed-case, case deletion, listwise, missing, imputation, sensitivity, hypothetical, lost to follow-up, and included-in-analysis language. Native and existing current layout locators agreed on the relevant occurrences. No complete-case designation or existing-result mapping was located anywhere in supplied REPORT text. The relevant main missing-data analysis text is on p.7; the follow-up descriptions are on pp.3,4,6. Supplement missing-follow-up occurrences refer to the index and descriptive eTable 1, not an outcome sensitivity result.

The complete results-supplement REPORT scope is its [index p.1](../../../joi170166supp3_prod.pdf#page=1) and trial results on pp.17–27. Its toolkit pp.2–16 is prospective operational PLAN content by content and cannot establish a completed trial sensitivity result. Current-source images were visually inspected for the index and every results page: eTables 1–7 on pp.17–23; hospital residual [p.24](../../../joi170166supp3_prod.pdf#page=24); unadjusted hospital differences [p.25](../../../joi170166supp3_prod.pdf#page=25); unadjusted MACE [p.26](../../../joi170166supp3_prod.pdf#page=26) and death [p.27](../../../joi170166supp3_prod.pdf#page=27) temporal plots. The additional [p.18](../../../joi170166supp3_prod.pdf#page=18), [p.19](../../../joi170166supp3_prod.pdf#page=19), and [p.20](../../../joi170166supp3_prod.pdf#page=20) tables are baseline summaries. Their titles, labels and captions do not identify a complete-case primary-MACE sensitivity. These are search-context locations, not additional independent inconsistencies. Absence is bounded to supplied REPORT materials; no external code, publication or unsupplied record was searched.

### Applicable rule and reproduced logical comparison

The comparison is a prospectively named primary-outcome sensitivity analysis versus its identifiable reported counterpart. SAP §7.1 covers missing primary outcomes; §7.2 supplies the method set `{complete-case analysis, multiple imputation}`. The report identifies multiple imputation and hypothetical missing-event scenarios, but supplies no complete-case designation or definition mapping the primary model or a hypothetical scenario to that planned method. The baseline complete/missing-follow-up comparison has neither the endpoint nor the treatment-effect identity required to be that counterpart. The covariate, exposure and expanded-composite tables identify different analyses. Therefore the complete-case primary-MACE sensitivity has no identifiable reported counterpart in the supplied package.

This logical comparison is reproduced. It does not establish whether the analysis was performed. It does not require, or assert, a numerical difference from the primary OR or risk difference. The applicable scope is focus area D and Route A, category 5: a planned primary analysis, including a prespecified sensitivity analysis of the primary endpoint, without an identified reported result. Intention-to-treat terminology, cohort totals and the descriptive baseline comparison do not supply the missing result-to-method mapping.

**Display-precision interval check:** Not applicable to the categorical analysis availability/identity comparison: there is no complete-case estimate or interval to compare against a printed number, so no recomputed numerical interval or relative discrepancy can be formed. Contextual exact integer identities reproduce: 215+80=295; 21,079+295=21,374; and 10,066+11,308=21,374. These are participant counts rather than rounded measurements, and their gap is zero. They do not determine outcome availability within each arm, the primary-model inclusion rule, or a complete-case effect. No arm-specific complete-case denominator, event count, OR, risk difference or confidence interval was reconstructed from these totals.

### Inputs, remaining definitions and alternatives

**Necessary inputs available:** Yes, for the registered logical comparison: the explicit prospective method statement, its primary-endpoint scope, the reported primary endpoint/model/effect, the observed missing-follow-up counts, the report sensitivity statements, and the complete supplied REPORT analysis labels and captions are available and readable. No targeted OCR is needed.

**Exact missing inputs or definitions:** A reported result or narrative result designated as the complete-case primary-MACE sensitivity; the rule that determines outcome completeness for that sensitivity; its contributing population, including arm-specific totals or an equivalent model-population definition; missing-outcome coding/inclusion in the primary model; the definitions of the hypothetical scenarios; a definition mapping any existing primary, adjusted or hypothetical-scenario result to complete-case analysis; and any supplied documentation of replacement or deferral. These missing elements prevent reconstruction of the complete-case numerical effect and confident attribution of an existing effect to it. They do not prevent checking that the named prospective analysis has no identified counterpart.

**Source-grounded alternative interpretation:** The primary model could already implement the planned complete-case analysis while the descriptive and intention-to-treat population statements retain the full cohort; an unspecified hypothetical scenario could implement it; or the analysis could have been replaced or deferred. The Figure 1 statement that lost participants were included gives context but does not state the outcome coding or inclusion for each individual model. Neither that statement nor the printed table denominators resolves these alternatives. The SAP and report do not establish which alternative applies; none is adopted as an explanation.

**Direct observation versus inferred explanation:** Directly observed are the explicit SAP complete-case provision, primary-endpoint scope, REPORT imputation/scenario language, cohort counts, and identified supplemental analysis labels. The bounded search and source-page reread directly find no explicit complete-case result or mapping. Whether the analysis was actually performed, why it is not identified, whether the primary result is already complete-case, and whether it would change the trial conclusion are inferred possibilities without sufficient supplied evidence; no conclusion about them is assigned.

**Affected result:** Availability, identity and analysis population of the planned complete-case sensitivity estimate for the primary 30-day MACE intervention effect, alongside the primary OR 0.98 (0.80–1.21) and risk difference −0.09 percentage points (−1.32 to 1.14).

### Classification and evidence state

**Document roles confirmed:** Both SAP locations are PLAN because they prospectively prescribe analyses. Main pp.3,6,7 and results supplement pp.17,21,22,23 are REPORT because they describe completed trial methods, participants and results. Additional main p.4 and the supplemental index/results search locations are REPORT context. No document-role amendment is required.

**Primary relationship type confirmed:** `P_R`. **All relationships confirmed:** `P_R`. **Review domain confirmed:** `protocol_report`. The contrast is between the planned complete-case analysis and what is identifiable in REPORT material. The report documents jointly establish that side of the comparison and do not conflict with one another, so they add no `S_C` or `S_W`. SAP p.7 supports the primary-outcome identity without a plan-internal discrepancy, so it adds no `P_P`. Precedence `P_R > P_P > S_C > S_W` yields `P_R`; the domain follows the required `P_R` to `protocol_report` mapping. No classification ambiguity is present. No transcribed source value or registered location required amendment.

**Evidence state:** `reproduced`.

**Determining recheck fact:** The source-confirmed SAP explicitly prescribes complete-case sensitivity analysis for missing primary-outcome data, while source-confirmed REPORT sensitivity text, all supplied REPORT searches, and the supplemental analysis identities supply no complete-case primary-MACE result or mapping. The registered categorical observation remains under its stated logical rule.

**Exact remaining human question:** Where is the SAP-prespecified complete-case sensitivity analysis for primary 30-day MACE reported, with its contributing population and result, or which reported primary/scenario analysis implements it and what supplied definition establishes that mapping?

### Tooling provenance and bounded limitations

New derivatives were written only beneath `review_1_6_2/preprocessing/recheck7/` with direct Poppler 25.03.0 `pdftotext` on CPU:

```bash
pdftotext jama_huffman_2018_oi_170166.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck7/main-native.txt
pdftotext joi170166supp3_prod.pdf .ai_paper_validation/review_1_6_2/preprocessing/recheck7/supp3-native.txt
```

Source-page authority used current-source images: `preprocessing/st2-support/sap6.png`; `preprocessing/curator/sap7.png`, `main3.png`, `main-4.png`, `main-6.png`, `main-7.png`, and every `supp3-17.png` through `supp3-27.png`; plus `preprocessing/recheck/supp3-1.png`. Existing current layout text in `preprocessing/screen2/` supported searches only. No image was altered; no rendering, OCR, fallback environment, unapproved Python extraction, external source or web access was used in this recheck. All assigned source locations were readable. Remaining limitations are exactly the missing complete-case result/population and primary-model/scenario mapping listed above.

Handoff: C007 covered; one assigned ID; one evidence state `reproduced`; classification retained; zero unreadable assigned locations. All missing result and definition questions remain for human adjudication.
