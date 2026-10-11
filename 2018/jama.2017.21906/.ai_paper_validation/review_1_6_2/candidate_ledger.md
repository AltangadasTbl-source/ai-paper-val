# Stable candidate ledger — Workflow 1.6.2

Pending Human Adjudication. Seven issues were registered after fresh independent initial and pass-2 inclusion screens. Stable IDs follow first conflicting REPORT locations in source order, with supporting method context and corroborating locations excluded from the ordering key. The three repeated checker pairs share one ID per issue. Evidence states reflect completed fresh rechecks; inclusion-audit fields reflect the completed independent audit; no assigned ID will be deleted.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | protocol_report | P_R | P_R | PLAN SAP p.5 vs REPORT main pp.3,7 and results supplement pp.21,22 | reproduced | CONFIRMED | F-XS-001, F-ST1-502 |
| C002 | protocol_report | P_R | P_R | PLAN protocol p.9 and SAP pp.2,3 vs REPORT main pp.3,8,9 and results supplement pp.1,23 | reproduced | CONFIRMED | F-XS-003, F-ST1-503 |
| C003 | protocol_report | P_R | P_R | PLAN SAP pp.5,7 vs REPORT main pp.3,9,10 | reproduced | CONFIRMED | F-XS-002, F-ST1-504 |
| C004 | statistical_results | S_W | S_W | REPORT main Table 2 p.6 effect columns and method context p.3 | reproduced | CONFIRMED | F-ST1-001 |
| C005 | statistical_results | S_W | S_W | REPORT results supplement p.1 index vs same REPORT p.24 eFigure 1A caption | reproduced | CONFIRMED | F-ST1-505 |
| C006 | statistical_results | S_W | S_W | REPORT results supplement p.17 eTable 1 LDL row vs same-display mean/SD rows | reproduced | CONFIRMED | F-ST1-501 |
| C007 | protocol_report | P_R | P_R | PLAN SAP pp.6,7 vs REPORT main pp.3,6,7 and results supplement pp.17,21,22,23 | reproduced | CONFIRMED | F-ST2-501 |

## C001 — MEDICATION


- **Supporting findings and provenance:** F-XS-001, cross_source_consistency_reviewer; F-ST1-502, statistics_pass_1 support shard.
- **All compared source locations:** PLAN [SAP p. 5, §6.1.2, lines 1149–1151](../../joi170166supp2_prod.pdf#page=5); REPORT [main p. 3, Outcomes](../../jama_huffman_2018_oi_170166.pdf#page=3); REPORT [main p. 7, Table 3 optimal in-hospital medication row and footnote c](../../jama_huffman_2018_oi_170166.pdf#page=7); REPORT [results supplement p. 21, eTable 5 corresponding row and footnote c](../../joi170166supp3_prod.pdf#page=21); REPORT [results supplement p. 22, eTable 6 corresponding row and footnote b](../../joi170166supp3_prod.pdf#page=22).
- **Independent source comparison:** SAP lists aspirin, ADP receptor antagonist, heparin, statin, and beta blocker; the main Outcomes paragraph lists four components and states that in-hospital statin use was predefined but not collected; Table 3 and both sensitivity displays likewise omit statin. The categorical five-versus-four component difference is reproduced; display precision is inapplicable. Anticoagulant/heparin wording alone is not added as another issue.
- **Qualifying route and tier:** Route A, category 5; planned versus reported composite definition is expressly within the protected comparison tier. Disclosure of noncollection does not remove an always-register changed definition.
- **Affected results:** Control 3122 (31.7%) versus intervention 3878 (35.8%); primary adjusted difference 6.00 percentage points (3.90–8.11) and OR 1.45 (1.28–1.64); cluster-adjusted difference 8.61 (6.98–10.23) and OR 1.70 (1.57–1.85); all four eTable 5 medication ORs and eTable 6 OR 0.87 (0.70–1.07).
- **Proposed classification:** Review domain `protocol_report`; relationship type `P_R`; all relationships `P_R`; compared roles PLAN SAP versus REPORT main/results tables. The REPORT occurrences agree with each other and do not add `S_C` or `S_W` relationships.
- **Classification ambiguity and alternatives:** None in roles or relationship; an intentional disclosed adaptation or later approved amendment could explain the component change, but the supplied package does not establish the amendment or a five-component result.
- **Source-order locator:** DOC-001 p. 3, Outcomes, optimal in-hospital medication definition; associated result DOC-001 p. 7, Table 3.


**Status:** Pending Human Adjudication

## C002 — EXPANDED


- **Supporting findings and provenance:** F-XS-003, cross_source_consistency_reviewer; F-ST1-503, statistics_pass_1 support shard.
- **All compared source locations:** PLAN [protocol p. 9, §2.2.3, lines 259–263](../../joi170166supp1_prod.pdf#page=9); PLAN [SAP p. 2, §2.1.2, lines 1071–1072](../../joi170166supp2_prod.pdf#page=2) and [continuation p. 3, lines 1073–1074](../../joi170166supp2_prod.pdf#page=3); REPORT [main p. 3, Outcomes and Statistical Analysis](../../jama_huffman_2018_oi_170166.pdf#page=3); REPORT [main p. 8, Secondary and Post Hoc Analyses](../../jama_huffman_2018_oi_170166.pdf#page=8); REPORT [main p. 9, result continuation and Discussion](../../jama_huffman_2018_oi_170166.pdf#page=9); REPORT [results supplement p. 1, eTable 7 contents entry](../../joi170166supp3_prod.pdf#page=1); REPORT [results supplement p. 23, eTable 7 title, expanded-composite row, and footnotes](../../joi170166supp3_prod.pdf#page=23).
- **Independent source comparison:** Both prospective documents place in-hospital and 30-day expanded MACE under secondary objectives; the report twice calls the added heart-failure/shock/arrest analysis post hoc on p. 3 and repeats that status in Results and Discussion; eTable 7 calls it exploratory. The named outcome-status contrast is reproduced, without assuming that all uses of exploratory imply an outcome-hierarchy change. Display precision is inapplicable to prospective status.
- **Qualifying route and tier:** Route A, category 5; a planned outcome's status and composite identity are within the protected plan/report comparison tier even though the plans do not specify the expansion's components.
- **Affected results:** Expanded composite control 919 (9.1%) versus intervention 795 (7.0%); cluster-adjusted difference −0.86 (−1.72 to −0.01), OR 0.89 (0.80–1.00); primary adjusted difference −1.34 (−2.72 to 0.04), OR 0.84 (0.70–1.00), and the prespecified/post-hoc characterization attached to them.
- **Proposed classification:** Review domain `protocol_report`; relationship type `P_R`; all relationships `P_R`; compared roles PLAN protocol/SAP versus REPORT main/results supplement. The two plans agree, so no `P_P` relationship is introduced; report locations also agree.
- **Classification ambiguity and alternatives:** Roles are clear; prospective-versus-reported composite identity is unresolved because the plan supplies the broad expanded-MACE name without its components, so the reported seven-component outcome may be a distinct expansion selected later or the intended planned expansion.
- **Source-order locator:** DOC-001 p. 3, Outcomes continuation and Statistical Analysis post-hoc expansion statements; associated result DOC-001 pp. 8–9 and DOC-004 p. 23.


**Status:** Pending Human Adjudication

## C003 — SUBGROUPS


- **Supporting findings and provenance:** F-XS-002, cross_source_consistency_reviewer; F-ST1-504, statistics_pass_1 support shard.
- **All compared source locations:** PLAN [SAP p. 7, §7.5.2, lines 1243–1254](../../joi170166supp2_prod.pdf#page=7); PLAN [SAP p. 5, §6.1.3, lines 1156–1165](../../joi170166supp2_prod.pdf#page=5); REPORT [main p. 3, Statistical Analysis subgroup statement and separate process-evaluation statement](../../jama_huffman_2018_oi_170166.pdf#page=3); REPORT [main p. 9, Figure 3 title, age/hospital-type rows, and accompanying subgroup paragraph](../../jama_huffman_2018_oi_170166.pdf#page=9); REPORT [main p. 10, opening Discussion paragraph](../../jama_huffman_2018_oi_170166.pdf#page=10).
- **Independent source comparison:** SAP explicitly lists age <65/>65, hospital size, toolkit-component use, sex, and STEMI/NSTEMI under primary-endpoint a priori subgroup analyses; Figure 3 instead uses <50/50–69/≥70 and government/nonprofit/private hospital type, calls the display prespecified, and has no toolkit-use subgroup. Searches of the complete direct protocol/SAP text locate no prospective specification for hospital type or the revised age partition; complete direct report text locates no toolkit-use primary-MACE subgroup result. The equality boundary at age 65 is not a separate issue. Display precision does not equate different categorical partitions.
- **Qualifying route and tier:** Route A, category 5; reported prespecified analyses absent from the supplied plan and replaced/unreported planned analyses of the primary endpoint are protected comparisons.
- **Affected results:** Primary-MACE age ORs 1.53 (0.83–2.79), 0.89 (0.67–1.19), 0.98 (0.71–1.35); hospital-type ORs 0.90 (0.61–1.33), 0.91 (0.59–1.40), 1.16 (0.82–1.64), with the corresponding Figure 3 differences and event counts; availability and status of the planned age-at-65 and toolkit-use heterogeneity analyses.
- **Proposed classification:** Review domain `protocol_report`; relationship type `P_R`; all relationships `P_R`; compared roles PLAN SAP versus REPORT main Figure 3/methods/narrative. The report's prespecified claims agree across locations and do not add a report-internal relationship.
- **Classification ambiguity and alternatives:** None in roles or relationship; a later dated specification could change age bands, add hospital type, or defer toolkit-use analysis, but no supplied amendment documents this, and the separately promised process-evaluation report is not itself the primary-MACE subgroup result.
- **Source-order locator:** DOC-001 p. 3, Statistical Analysis prespecified subgroup sentence; associated result DOC-001 p. 9, Figure 3.


**Status:** Pending Human Adjudication

## C004 — TIME


- **Supporting finding and provenance:** F-ST1-001, statistics_pass_1 main shard.
- **All compared source locations:** REPORT [main p. 6, Table 2 title, door-to-balloon and door-to-needle rows, both adjusted-effect headings, and footnotes b/c](../../jama_huffman_2018_oi_170166.pdf#page=6); REPORT [main p. 3, Statistical Analysis](../../jama_huffman_2018_oi_170166.pdf#page=3).
- **Independent source comparison:** The door-to-balloon row prints difference 6.18 (−4.78 to 17.14) and β 13.00 (3.64–22.36), while door-to-needle prints difference 0.40 (−5.23 to 6.03) and β 5.00 (−5.20 to 15.20). Both headings share footnote b, which describes intervention-minus-control marginal effects from mixed logistic/quantile models including hospital/time adjustment; footnote c identifies β but does not map a different estimand or model to the Difference column. The adjusted quantities are not compared with crude median differences.
- **Display precision:** Door-to-balloon estimate intervals [6.175,6.185] and [12.995,13.005] have gap 6.810/6.18 = 1.10194; door-to-needle intervals [0.395,0.405] and [4.995,5.005] have gap 4.590/0.40 = 11.475. Both exceed 0.05. The door-to-balloon Difference CI includes zero throughout endpoint rounding intervals, whereas its β CI excludes zero; there is no printed P value or test, so this is not registered as a Route A category 1 interval/test conflict.
- **Qualifying route and tier:** Route B: B1, in-focus estimate/method logic within one result display; B2, the shared description plus β label does not identify the analyses producing the distinct time contrasts; B3, the extracted door-to-balloon effect and its null-inclusion interpretation, and the extracted door-to-needle magnitude, depend on which adjusted quantity applies. This is not the separately obvious percent-sign unit notation.
- **Proposed classification:** Review domain `statistical_results`; relationship type `S_W`; all relationships `S_W`; compared roles REPORT main Table 2/methods.
- **Classification ambiguity and alternatives:** None in roles or relationship; a marginal versus conditional contrast, a different quantile, transformation, model, or contributing population could distinguish the columns, but the source does not name that distinction. The observation requests the mapping rather than assuming that distinct effect summaries must generally be equal.
- **Source-order locator:** DOC-001 p. 6, Table 2 door-to-balloon row, followed by door-to-needle row; DOC-001 p. 3 is supporting method context.


**Status:** Pending Human Adjudication

## C005 — RESIDUAL


- **Supporting finding and provenance:** F-ST1-505, statistics_pass_1 support shard.
- **All compared source locations:** REPORT [results supplement p. 1, eFigure 1A index entry](../../joi170166supp3_prod.pdf#page=1); REPORT [results supplement p. 24, eFigure 1A signed axis/points and caption](../../joi170166supp3_prod.pdf#page=24). REPORT [main p. 9, accompanying eFigure 1A description](../../jama_huffman_2018_oi_170166.pdf#page=9) corroborates the caption's primary-outcome heterogeneity interpretation and is supporting context rather than an additional conflicting location.
- **Independent source comparison:** The index assigns the exact named plot the formula Expected minus Observed; its negative values then denote observed above expected, whereas the plot's caption associates negative/left hospital departures with lower MACE than the reference mean and positive/right departures with higher MACE. Main p. 9 describes this as heterogeneity of the primary outcome, comparing each site's event rate with the trial mean. The source image confirms nonzero negative and positive points and axis ticks −3 through 2; no pixel-derived decimal estimate, hospital identifier, or event count was manufactured.
- **Qualifying route and tier:** Route A, category 2, direction/reference reading reversal. The comparison is first checked against the peripheral index/heading tier: this entry supplies the subtraction order of a signed primary-outcome hospital result, so changing it reverses the interpretation of the nonzero departures rather than merely changing a pointer or heading. The explicit caption lets a reader choose its reading, but does not reconcile the competing printed index definition; contextual reconstructability does not remove category 2.
- **Display precision:** The comparison concerns the sign/reference interpretation of clearly nonzero displayed points, not a magnitude reconstructed from rounded inputs; half-unit intervals and a relative discrepancy for exact hospital values cannot be reported because those values are not printed. Rounding of an unreported exact ordinate is not used to reconcile opposing directional definitions.
- **Affected result:** Whether positive and negative eFigure 1A residuals denote hospitals above or below the expected/reference primary 30-day MACE rate, including the interpretation of intervals excluding zero; this does not claim that the trial-wide intervention OR changes.
- **Proposed classification:** Review domain `statistical_results`; relationship type `S_W`; all relationships `S_W`; compared roles REPORT results-supplement index versus REPORT same-supplement figure. Corroborating main text does not introduce `S_C`.
- **Classification ambiguity and alternatives:** None in roles; the index may describe an expected-minus-observed quantity distinct from a predicted hospital departure or random effect displayed in the figure, and the exact definition/scale of expected versus mean is unprovided. That alternative leaves the same named display with competing quantitative reference descriptions and is the remaining human question, rather than evidence that a specific unprinted hospital pair has been reconstructed.
- **Source-order locator:** DOC-004 p. 1, eFigure 1A entry; affected result DOC-004 p. 24, with DOC-001 p. 9 corroborating description.


**Status:** Pending Human Adjudication

## C006 — LDL


- **Supporting finding and provenance:** F-ST1-501, statistics_pass_1 support shard.
- **All compared source locations:** REPORT [results supplement p. 17, eTable 1 complete/missing follow-up headers; LDL, age, weight, systolic blood pressure, heart-rate, and hemoglobin rows](../../joi170166supp3_prod.pdf#page=17).
- **Independent source values:** Complete follow-up n=21,079, LDL 122.4 (SD 40.8); missing follow-up n=295, LDL 131.4 (SD 46.0); printed difference 9.0 with 95% CI 3.2–14.8 mg/dL. The exact source table supplies no LDL-specific contributor counts and no CI procedure. This is a within-display method/interval comparison, not a cross-location baseline-copy comparison.
- **Independent calculation:** With pooled variance `[(nC−1)sC²+(nM−1)sM²]/(nC+nM−2)` and `SE = sqrt(pooled variance × [1/nC+1/nM])`, the displayed LDL values give SE 2.39648934 and a 1.96-multiplier interval 4.30288090–13.69711910. The same method reproduces printed age endpoints from −1.98965319/0.78965319, weight from −2.01402075/0.21402075, systolic pressure from −2.92697797/3.72697797, and heart rate from 0.82785750/5.17214250. Hemoglobin's endpoints overlap after displayed mean/SD rounding; neither a new preferred method nor a claim about the producing procedure is made.
- **Display precision:** Independent corner calculations allow ±0.05 for both means/SDs and conservatively ±0.5 for the displayed group counts. The LDL lower endpoint interval is [4.19321414,4.41252805] and upper endpoint interval [13.58747195,13.80678586]. Printed-limit intervals are [3.15,3.25] and [14.75,14.85]. The closest gap is 0.94321414 for each, giving lower relative discrepancy 0.29475442 and upper relative discrepancy 0.06373069, both above 0.05.
- **Qualifying route and tier:** Route A, category 4; the numerical mismatch survives display precision under a method that reproduces other same-display mean/SD rows. No peripheral cross-document baseline comparison or model-versus-crude comparison is substituted.
- **Affected extracted value:** The baseline LDL missing-minus-complete 95% confidence interval 3.2–14.8 mg/dL.
- **Proposed classification:** Review domain `statistical_results`; relationship type `S_W`; all relationships `S_W`; compared roles REPORT same results-supplement eTable 1.
- **Classification ambiguity and alternatives:** None in roles or relationship; fewer LDL contributors or a distinct interval construction could explain the wider interval, and both remain explicit source-grounded alternatives because assay-specific counts and procedure are absent. Under category 4 the unprovided generating method is the human question, rather than a reason to remove the reproduced finding.
- **Source-order locator:** DOC-004 p. 17, eTable 1 LDL row; other rows in that display support the reproducing-method comparison.


**Status:** Pending Human Adjudication

## C007 — Planned complete-case primary-MACE sensitivity result is not identified


**Supporting finding and provenance:** F-ST2-501, `statistics_pass_2`, support part `checkers/parts/statistical_pass_2_support.md`; underlying relationships S516, with S515/S518 and main S005 providing analysis-population/model context. This issue is distinct from C001's medication components, C002's expanded-outcome status/identity, C003's subgroup specifications, C004's time contrasts, C005's residual direction, and C006's LDL interval construction.

**Compared source locations and roles:**

- PLAN [SAP physical p.6, §7.1, lines 1190–1198, and §7.2, lines 1205–1210](../../joi170166supp2_prod.pdf#page=6): prospective intention-to-treat and missing-outcome provisions, including complete-case analysis and multiple imputation.
- PLAN [SAP physical p.7, §7.5, lines 1229–1238](../../joi170166supp2_prod.pdf#page=7): primary 30-day MACE and primary hospital/time mixed logistic model.
- REPORT [main physical p.3, Statistical Analysis and outcome follow-up description](../../jama_huffman_2018_oi_170166.pdf#page=3): reported model, intention-to-treat statement, and three-contact loss-to-follow-up rule.
- REPORT [main physical p.6, follow-up paragraph beneath Table 2](../../jama_huffman_2018_oi_170166.pdf#page=6): 295 incomplete outcomes, comprising 215 not followed by the site and 80 unreachable after three attempts; randomized-arm totals 10,066 and 11,308.
- REPORT [main physical p.7, Table 3 primary-MACE row, footnote a, and Primary Analysis paragraph](../../jama_huffman_2018_oi_170166.pdf#page=7): reported primary effect and missing-data sensitivity summaries.
- REPORT [results supplement physical p.17, eTable 1 title, complete/missing headers and table](../../joi170166supp3_prod.pdf#page=17): descriptive baseline comparison for complete follow-up n=21,079 and missing follow-up n=295; this is not a primary-MACE sensitivity result.
- REPORT [results supplement physical p.21, eTable 5 title, primary row, headers and footnotes](../../joi170166supp3_prod.pdf#page=21): GRACE, transfer, insurance and prehospital-aspirin adjustment analyses.
- REPORT [results supplement physical p.22, eTable 6 title, primary row and footnotes](../../joi170166supp3_prod.pdf#page=22): time-exposed interaction analysis.
- REPORT [results supplement physical p.23, eTable 7 title, outcome rows, headers and footnotes](../../joi170166supp3_prod.pdf#page=23): expanded-composite and component analyses.

**Independent source comparison:** SAP §7.1 expressly assigns the subsequent missing-data methods to primary and secondary endpoints; §7.2 says sensitivity analyses will use complete-case analysis and multiple imputation to evaluate missing outcomes. SAP §7.5 identifies primary 30-day MACE. The main report says all results use intention-to-treat analysis. Its primary result is OR 0.98 (95% CI 0.80–1.21) and risk difference −0.09 percentage points (95% CI −1.32 to 1.14). The same paragraph states that results were similar after multiple imputation and describes broader but consistent results from hypothetical missing-event scenarios and multiple imputation. Neither that paragraph nor the inspected model descriptions/tables identify a complete-case primary-MACE result. Complete supplied main/results-supplement text searches found no complete-case analysis designation or mapping. Supplemental eTable 1 compares baseline characteristics by follow-up availability; eTables 5–7 identify other analyses rather than a complete-case missing-outcome sensitivity.

**Logical rule and reproduction:** The planned primary-outcome missing-data sensitivity set explicitly contains complete-case analysis and multiple imputation; the reported missing-data sensitivity set explicitly identifies multiple imputation and hypothetical scenarios without defining any reported result as the complete-case analysis. Thus a planned primary-outcome sensitivity analysis has no identified reported counterpart. This reproduces the planned-versus-reported observation within the supplied package; it does not establish that complete-case analysis was never performed. An existing result could implement the planned analysis, but the mapping is absent.

**Display precision:** The finding concerns categorical analysis availability/identity rather than a numerical comparison; recomputed rounding intervals and relative discrepancy are inapplicable. The coherent identities 21,079 + 295 = 21,374 and 10,066 + 11,308 = 21,374 do not identify the primary model's contributing population or missing-outcome coding. No complete-case event count, OR, risk difference, interval, or arm-specific complete-case total is inferred from these cohort numbers.

**Qualifying route and comparison tier:** Route A, category 5; a prespecified primary-outcome sensitivity analysis without an identified reported result is an always-register planned-versus-reported analysis observation. It is within focus area D and the protected report-versus-plan analysis-specification tier. The peripheral-comparison rule does not apply: the relevant difference is the primary-MACE missing-outcome sensitivity analysis, rather than a copied baseline value, isolated contributor count, pointer, calendar or administrative detail.

**Affected result or extracted value:** Availability, identity and analysis population of the SAP-prespecified complete-case sensitivity estimate for the primary 30-day MACE intervention effect, alongside the reported primary OR 0.98 (0.80–1.21) and risk difference −0.09 percentage points (−1.32 to 1.14). The supplied evidence does not show that reporting the complete-case result would change the overall trial conclusion.

**Proposed classification:** Review domain `protocol_report`; primary relationship type `P_R`; all relationships `P_R`; compared roles PLAN SAP versus REPORT main and trial-results supplement. The report locations jointly establish what is reported and do not conflict with one another, so they add no `S_C` or `S_W` relationship. SAP p.7 is supporting primary-endpoint/model context, not a plan-internal conflict. No role ambiguity is present.

**Why context does not remove the issue:** Route A category 5 directly applies. Intention-to-treat describes assignment/analysis principles but does not specify how missing outcomes entered the primary model. Full cohort table headers and the complete/missing descriptive table do not supply that model definition. A named imputation result or an unspecified hypothetical scenario also does not, by itself, identify the planned complete-case analysis.

**Source-grounded alternatives and exact missing definitions:** The reported primary model may itself have used complete cases while retaining full cohort descriptive headings; a hypothetical scenario could implement complete-case analysis; or the planned sensitivity may have been replaced or deferred. These alternatives remain possible because the report does not define the primary model's inclusion/coding of the 295 missing outcomes or the hypothetical scenarios. The missing elements are the complete-case outcome-availability rule and contributing population, the result or narrative result identified as that sensitivity analysis, the mapping from any existing primary/scenario result to complete-case analysis, and any supplied documentation of replacement or deferral. No alternative is assumed.

**Exclusion rationale and consolidation:** This is not solely an unreported imputation-model detail: the supplied plan explicitly names the primary-outcome analysis to be reported, bringing it under Route A category 5. It is not duplicated by the current six candidates, whose rules and results differ. No independent issue is added for imputation-model internals, hypothetical-scenario internals alone, or the conditionally planned hospital-imbalance sensitivity. Those elements supply no separate reproduced conflict in this assigned finding.

**Exact human question:** Where is the SAP-prespecified complete-case sensitivity analysis for primary 30-day MACE reported, with its contributing population and result, or which reported primary/scenario analysis implements it and what supplied definition establishes that mapping?

**Status:** Pending Human Adjudication.

