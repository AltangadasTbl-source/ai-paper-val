# Statistical consistency pass 1 — main A and PLAN

Runtime agent: /root/statistics_1_main_a; newly spawned qc161_statistical_consistency_reviewer, gpt-6.1-sol/high. Scope: S001–S094 plus S400–S417 (112 relationships). Each has an explicit PASS_1_COMPLETE row in statistics/parts/statistical_main_a.md. This is pass 1 only; a different fresh runtime agent must perform pass 2.

Read completely: QUALITY_CONTROL_SCOPE.md, workflow_1_6_1/review_contract.md, PERFORMANCE_PROFILE.md, workflow_1_6_1/report_spec.md, settings.toml, tooling/source inventories and current main/support maps. Supplied source text and exact pages govern; prior candidate/review/report conclusions and external evidence were not used. Tooling: direct Poppler pdftotext25.03.0 selected-page source reads; reused native/layout and rendered source pages. Source render DOC-001 p.6 and p.9 confirmed table/figure quantities and captions; mapper's new protocolp14 render confirmed the contact timeline. No derivative files were created, no Python scientific orchestration, no GPU.

## Completed inferential checks

112 assigned relationships: 94 main model/design/result keys plus18 PLAN families SUP-P01–P18 (S400–S417). All main Table1 differences (27), Table2 process/time tuples (21), Table3 cluster-only and hospital/time tuples (20), Figure3 subgroup tuples (14), primary/secondary/post hoc narrative matches and eight model/design keys received source-grounded checks. Methods were checked against hospital-cluster randomization, stepped-wedge time structure, population eligibility, missingness language, explicit primary/secondary definitions, planned models/covariates, sample-size inputs, interim thresholds and exploratory multiplicity statements. Every estimate is contained in its ordered interval. Matched RD/OR directions agree. The primary null-spanning intervals agree with no demonstrated primary decrease. No NI/equivalence margin or conclusion is reported. No interim statistic or numerical stopping decision is supplied.

Absent test statistic, standard error, degrees of freedom, interval construction, variance estimator, or interaction parameter definitions were not filled by convention. Only diagnostic approximations are used where named below. The point/CI/P compatibility for the troponin statement cannot be determined as the same test from the package. The exact primary regression contributor count and outcome coding for295 incomplete outcomes are also not established; ITT accounting was not equated to complete binary outcomes. Precise missing definitions are retained in the inventory.

## Self-screened findings

### F-ST1-001

**Candidate statement:** Table2 reports two adjusted time contrasts for each of door-to-balloon and door-to-needle time, but does not identify the separate analyses or estimands that produced the difference and beta-coefficient columns.

**Relationships:** S046 and S048; N078 and N080. One repeated time-outcome mapping pattern.

**Exact source locations and document roles:** REPORT [main article physical p.6, printedp572, Table2, door-to-balloon and door-to-needle rows, both effect columns, title and footnotesb/c](../../../jama_huffman_2018_oi_170166.pdf#page=6). REPORT [main article physicalp3, printedp569, Statistical Analysis](../../../jama_huffman_2018_oi_170166.pdf#page=3) supplies the general cluster/time model description but no separate time-outcome contrast specification.

**Printed values and statements:** Table2's title states adjustment for within-hospital clustering and temporal trends. Door-to-balloon median times: control65(53–105)min, n4022; intervention77(55–118)min, n3639. The difference column prints6.18(95%CI−4.78 to17.14); the beta column prints13.00(3.64–22.36). Door-to-needle: control44(30–67)min,n1455; intervention45(27–75)min,n1433; difference0.40(−5.23 to6.03); beta5.00(−5.20–15.20). Footnotec identifies beta-coefficients. Footnoteb attaches the same intervention/control and marginal-effects description to both columns and names mixed-effects logistic or quantile regression including within-hospital clustering and temporal trends. The displayed difference header is percent, while the row descriptors are minutes.

**Rule and calculation:** A method description must identify what analysis and quantity a reported effect represents when distinct outputs have different inferential readings. This is a mapping observation; no equality between a conditional coefficient and a marginal contrast is assumed. The balloon point contrasts differ by13.00−6.18=6.82. Two-decimal display intervals[6.175,6.185] and[12.995,13.005] are disjoint. The needle contrasts differ by5.00−0.40=4.60, with disjoint point display intervals[.395,.405] and[4.995,5.005]. The balloon difference95%CI spans0; the beta95%CI has lower3.64>0. Display precision cannot supply their estimand mapping. Each estimate is inside its own CI, and no P value/test statistic is inferred. The percent header alone is screened out as notation, because minute outcome rows establish their measurement unit; the independent concern is the unidentified distinct contrasts and their different null-inclusion reading.

**Focus area:** C (statistical method logic; analysis description does not identify which analysis produced each time-effect number).
**Proposed review domain:** statistical_results.
**Proposed relationship type:** S_W.
**Compared document roles:** REPORT main Table2 values and method labels versus REPORT main Statistical Analysis.

**Affected result or extracted value:** The adjusted intervention effect on door-to-balloon and door-to-needle time, especially extraction of balloon6.18(−4.78,17.14) versus13.00(3.64,22.36), which give different conclusions about exclusion of zero at the printed95% confidence level.

**Why context does not resolve it:** The distinct column labels show that two outputs are presented, but the common adjustment title/footnote does not define whether they differ by model, quantile, conditional/marginal target, outcome transformation, standardization or contrast population. Immediate context supplies no formula or separate model mapping for the two quantities. A reader can identify time in minutes, yet cannot identify which adjusted time effect applies to a specified analysis.

**Source-grounded alternatives and missing definitions:** A marginal time contrast and a conditional quantile-regression coefficient could be intentionally distinct; different time models or transformations could also yield different outputs. These are possible interpretations, not asserted methods. Needed definitions are each column's model/estimand, quantile or outcome scale, standardization/reference population, units, and interval construction. No preferred analysis is proposed.

**Exact human question:** Which models, estimands, units and reference populations produced the difference and beta-coefficient columns for the two time outcomes in Table2, and which adjusted door-to-balloon result should a reader extract for each specified analysis?

Self-screen: directly source-confirmed; in focusC; immediate context does not map the distinct analyses; the specific time-effect estimate and interval extracted can change. Both rows are consolidated.

### F-ST1-002

**Candidate statement:** The age subgroup boundaries used for the primary30-day MACE result differ from those in the supplied SAP, while the report calls the Figure3 groups prespecified.

**Relationships:** S006,S077,S078,S079,S410 (SUP-P11). One age-subgroup specification pattern.

**Exact source locations and document roles:** PLAN [SAP physicalp7, section7.5.2, lines1243–1254, especiallyline1251](../../../joi170166supp2_prod.pdf#page=7). REPORT [main physicalp3, Statistical Analysis subgroup description](../../../jama_huffman_2018_oi_170166.pdf#page=3). REPORT [main physicalp9, Figure3 title/age rows and first Results paragraph](../../../jama_huffman_2018_oi_170166.pdf#page=9). REPORT [main physicalp2, Methods Study Design](../../../jama_huffman_2018_oi_170166.pdf#page=2) states analysis according to the supplied SAP and is contextual, not a separate conflicting relationship.

**Printed values and statements:** SAP7.5.2 calls its analyses a priori and specifies age(<65years and>65years). Main methods call age subgroups prespecified; Figure3 title also calls its groups prespecified. Figure3 instead uses<50,50–69,≥70years. Their adjusted MACE ORs are respectively1.53(.83–2.79),.89(.67–1.19),.98(.71–1.35), and RDs1.42%(−.71,3.54),−.57%(−2.02,.88),−.23%(−3.32,2.85). The intervention/control event-denominator pairs are58/2079 versus68/2045;297/6606 versus326/5863;247/2623 versus251/2158.

**Rule and calculation:** A planned-versus-reported primary endpoint subgroup specification must be matched by boundaries, not merely by variable name. The SAP two-way age partition at65 differs from the reported three-way partition at50 and70. Ages50–64 and65–69 lie in the same reported middle group but on different sides of the planned65 boundary; ages below50 and50–64 are separated in the report but together in the plan. This remains irrespective of how age65 itself is assigned in the SAP's abbreviated bounds. Report denominators2079+6606+2623=11308 and2045+5863+2158=10066 account for both arms; events58+297+247=602 and68+326+251=645 account for primary MACE totals. Thus this is a different age analysis of the same primary endpoint/population, not a count discrepancy or display rounding. Adjusted age65 effects cannot be reconstructed by averaging the three displayed adjusted ORs/RDs.

**Focus area:** D (planned-versus-reported statistical analysis, primary endpoint subgroup).
**Proposed review domain:** protocol_report.
**Proposed relationship type:** P_R.
**All relationships:** P_R.
**Compared document roles:** PLAN SAP subgroup boundaries versus REPORT main Figure3/Methods subgroup specification.

**Affected result or extracted value:** The primary30-day MACE age-specific effect estimates and their interpretation as prespecified analyses; the package does not report the planned<65/>65 effect estimates in Figure3.

**Why context does not resolve it:** Neither the reported figure nor adjacent methods/results identifies a revised age specification or explains replacement of the planned65 boundary. This is not a synonym or omitted comparison symbol: the participant partitions differ materially and cannot be mapped one-to-one. A reader cannot establish whether the displayed estimates correspond to a disclosed amendment, a different prespecified plan, or a subsequently chosen grouping.

**Source-grounded alternatives and missing definitions:** The supplied SAP may have been superseded by an amendment not supplied; the65-year analysis may have been performed separately; or Figure3 may use additional age groups while “prespecified” refers more generally to the age variable. The package does not establish which explanation applies. The absent item is a source-defined link between the planned and displayed age subgroup specifications, not a recommendation for alternate cutoffs.

**Exact human question:** What supplied prespecification or disclosed amendment defines the<50,50–69 and≥70year MACE groups in Figure3, and how do those results relate to the SAP's planned<65/>65year subgroup analysis?

Self-screen: source-confirmed beyond display precision; in focusD because the primary endpoint analysis is compared; immediate context does not explain the changed analysis; primary subgroup extraction and prespecified-status interpretation can change. No judgment on the choice of age groups is assigned.

## Excluded observations

Each pattern is listed once with exactly one scope reason code. Concordant relationships without an apparent discrepancy are completion records, not exclusion observations.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 Table2p6, Table3p7, Figure3p9 | Several adjusted RDs/ORs differ from crude percentages/ratios, including direction reversals. Hospital/time models are expressly reported, so crude recomputation does not test the adjusted estimand. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 Tables1–3/Figure3 and p6 troponin; REPORT DOC-004p17 eTable1; DOC-004p22 eTable6 | Exact CI/test/P compatibility and interaction interpretation require absent definitions. For troponin, median difference3.3(.1,6.5) versus mainP<.001: a diagnostic normal-Wald approximation gives SE(6.5−.1)/3.92≈1.633,z≈2.02,P≈.043, but no source identifies that as the printed test or CI construction. Interaction coefficient/time reference likewise absent; no contradictory test is asserted. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 Table1p5 creatinine, all displayed means/medians/proportions, Table3p7/null-adjacent ORs, p3interim rules; PLAN SAPp8 | Rounded baseline differences,0.0(0.0,0.0),OR upper1.00 and numerical z/P boundary displays do not establish inconsistencies. Standard-normal-tail diagnostics forz2.797 and1.977 give approximately.00516 and.0480 and agree at displayed precision; no stopping result is supplied. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001p6 Table2footnoteb andp7 Table3footnotea | Footnote wording attributes “difference in marginal effects” to ORs, but neighboring separate difference and OR columns, scales and narrative identify the intended binary quantities immediately; no evidence that an OR was computed as a difference. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-001p6 Table2time rows/header | Percentage header on minute time rows alone is immediately resolved by minute row descriptors and beta labels. The independent model/estimand mapping concern is F-ST1-001. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-001p6in-hospitalbeta narrative/Table2 | Narrative upperCI8.10 versus Table2upper8.40 forRD6.25,lower4.10 is a single-character slip whose intended table value is evident; both intervals have the same direction and null-exclusion interpretation. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-001p7dischargebeta narrative versusp6Table2 | Narrative RD6.63/OR1.47 versus table6.69/1.48 with identical printed CIs concerns an individual secondary process measure, not the primary result, analysis-population size or decision rule; no key-secondary status for that individual measure is established. | PERIPHERAL_COMPARISON |
| REPORT DOC-001p3sample size; PLAN DOC-002p18, DOC-003p4 | Exact80% stepped-wedge power cannot be reproduced from onlyN/ICC/risk/effect/alpha without cluster-period sizes/allocation and calculation implementation. No default balance/covariance or alternative power formula is inferred. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002p18,DOC-003p4; REPORT DOC-001p3 | Sample increase15000→15750 equals addition5%; division by.95 instead gives15789.47, while15750×.95=14962.5. Immediate context resolves conventional approximate5% inflation, with no distinct retained-count claim or decision discrepancy. | CONTEXT_RESOLVES |
| PLAN DOC-003p4section5 versusp3design/diagram | “Each of the four time periods” conflicts lexically with five cohorts, but its immediate design/diagram specifies the five crossovers at months4,8,12,16,20; intended schedule is clear. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-001p4flowcaption,p6missingness,p7primaryimputation; PLAN DOC-003p6 | Lost participants remain in analysis accounting;295 have incomplete follow-up; primary imputation/coding and model contributor count are not stated. These facts do not establish that all295 were missing all binary outcome information or that ITT total equals regression n. No missing=no-event or complete-case assumption is used. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002pp11,13,14timeline; REPORT DOC-001p3outcomes | Plan's discharge+30day contact date versus report's30day outcome wording lacks a source-defined competing admission-origin cutoff. Contact timing is not automatically an outcome window; no planned-versus-reported endpoint change is established. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-003p5; REPORT DOC-001p3,Table3p7 | Inpatient statin is planned but explicitly disclosed as not collected in main methods. Heparin versus anticoagulant label alone is immediately understood here without a source-established changed composite population. | CONTEXT_RESOLVES |
| PLAN DOC-003pp5,7–8; REPORT DOC-001p3process/subgroups | Toolkit-use subgroup/substudies are not displayed as main numeric results and process evaluation is expressly to be reported separately; report hospital-type subgroup does not establish absence of another prespecification. No missing-result or unreported-amendment hypothesis is registered. | CONDITIONAL_OR_UNREPORTED |

## Handoff

Pass1 complete. Exact scope112 relationships: S001–S094,S400–S417. Findings2: F-ST1-001,F-ST1-002. Excluded observations14. Assigned scientific gaps0. Missing exact test/CI construction, time-effect model/estimand mapping, contributor counts/missing-outcome coding, cluster-period power inputs and interaction reference definitions are recorded with source-grounded limitations. Candidate assignment, independent inclusion screen, evidence-state assignment and human adjudication belong to later stages. No severity, disposition or correction is assigned.

Artifacts: statistics/parts/statistical_main_a.md; checkers/parts/statistical_main_a.md. All evidence links in these part artifacts use four-level parent traversal; the coordinator must rewrite to three levels when merging into canonical statistics/relationship_inventory.md or checkers/statistical_pass_1.md.

# Statistical pass 1 — main graphical shard

## Execution and exact scope

Fresh runtime ID: root/statistics_1_main_b; gpt-6.1-sol/high; FRESH_SPAWN. Pass 1 only. Assigned scope is the disjoint union of all 60 Figure 2 descriptive rate/95% CI relationships: S095, S096, S097, S098, S099, S100, S101, S102, S103, S104, S105, S106, S107, S108, S109, S110, S111, S112, S113, S114, S115, S116, S117, S118, S119, S120, S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132, S133, S134, S135, S136, S137, S138, S139, S140, S141, S142, S143, S144, S145, S146, S147, S148, S149, S150, S151, S152, S153, S154. Numeric cross-references N113–N172 preserve outcome/cohort/step identity.

The normative scope and review contract, current tooling record, and complete current main map were read. The source-matched reused image of [REPORT DOC-001 physical p. 8, Figure 2](../../../jama_huffman_2018_oi_170166.pdf#page=8) was inspected visually. Direct source native/layout text was read with available Poppler pdftotext 25.03.0. The exact row-by-row visual, interval and labeling checks, approximate coordinate values, printed n values, explicit source constraints, and all 60 PASS_1_COMPLETE records are in [the assigned statistical inventory part](../../statistics/parts/statistical_main_b.md). Its image provenance is the current asset inventory's USABLE historic pdftoppm 180-dpi DOC-001-08.png. No source or prior artifact was edited, and prior checker/candidate/report conclusions were not read.

## Statistical checks and findings

All 60 points lie visually between their lower and upper interval endpoints. Every interval is ordered, rate and endpoint positions are feasible percentages, panel labels distinguish MACE from mortality, and cohort colors/control-open/intervention-solid markers agree with the stated phase and step. No estimate-containment, endpoint-order, or source-label direction contradiction was reproduced.

The caption explicitly establishes 95% CIs and the title explicitly establishes unadjusted rates. It provides no rate-specific P value, test statistic, standard error, comparison test, sidedness, CI algorithm, variance estimator, covariance, clustering treatment of these bars, or event count. Exact rate/CI numerals are also absent. These named absences restrict possible mechanical checks; the graph supplies no rate-specific superiority, noninferiority, equivalence, multiplicity, interim, or stopping conclusion. The corresponding trial-level methods and decision rules are separately assigned relationships, not assumed to govern each descriptive bar.

Every observation was self-screened against all four inclusion criteria. Finding count: 0. No F-ST1-201 or subsequent finding ID is assigned.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| [REPORT DOC-001 p. 8, Figure 2A/B and caption](../../../jama_huffman_2018_oi_170166.pdf#page=8), S095–S154 | Exact CI reconstruction or estimate/P/test/standard-error compatibility would require exact rate and endpoint numerals, a specified CI algorithm and its variance/cluster treatment, and a supplied comparison test and sidedness. Those inputs are not reported for the descriptive graph. CI-overlap significance and reconstructed event counts would likewise depend on unreported assumptions. No independent contradiction was reproduced. | CONDITIONAL_OR_UNREPORTED |
| [REPORT DOC-001 p. 8, Figure 2A/B](../../../jama_huffman_2018_oi_170166.pdf#page=8) versus [REPORT DOC-001 p. 7, Table 3 adjusted results](../../../jama_huffman_2018_oi_170166.pdf#page=7) | Individual unadjusted cohort-step rates can move in a different direction from overall cluster/time-adjusted treatment estimates. The title, population/time labels, and model descriptions identify different quantities; the adjusted effects are not crude ratios or differences of these graph points. | MODEL_VERSUS_CRUDE |
| [REPORT DOC-001 p. 9, Discussion, first intervention step](../../../jama_huffman_2018_oi_170166.pdf#page=9) versus [REPORT DOC-001 p. 8, Figure 2A/B](../../../jama_huffman_2018_oi_170166.pdf#page=8) | Reading “lower ... rates in the first step compared with other steps” as requiring every cohort's own first-step rate to be below every subsequent within-cohort rate would add an unstated comparison. The immediate trial/figure context identifies intervention periods by step: only cohort 1 contributes to intervention at step 1, whereas later intervention steps combine additional cohorts. The statement is interpretable at intervention-step level; it is not a universal claim about each plotted cohort trajectory. No exact pooled rate or inferential test was reconstructed from graphical coordinates. | CONTEXT_RESOLVES |

## Scope completion and handoff

Pass 1 complete for all 60 assigned relationships; 0 findings; 3 consolidated excluded observations; 0 scientific-coverage gaps. Graphical readings are approximate (about 0.1–0.2 percentage point as stated in the current main map), never exact source numerals. Exact numeric CI/test reconciliation cannot be performed because the named graph inputs are absent, not because a unit was omitted. No cross-source plan review or additional relationship was added in this bounded shard. No web, external literature, GPU, Python orchestration, fresh OCR, or fallback tooling was used.

Assigned durable paths:
- statistics/parts/statistical_main_b.md
- checkers/parts/statistical_main_b.md

Coordinator performs the canonical merge and future fresh-agent pass 2.

# Statistical Pass 1 — Support Baseline and Graph Shard

Runtime agent: `/root/statistics_1_support`; fresh `gpt-6.1-sol`/`high` statistical specialist. Scope: REPORT DOC-004 eTables 1–4 at physical pp. 17–20, eFigures 1A/1B/2A/2B at pp. 24–27, p. 1 contents context. Stable relationship IDs S155–S237, 83 relationships: 68 printed estimate/95% CI tuples, 12 exhaustive graphical families and 3 method/context families. Every tuple and assigned graph cell was checked; no sampling. eTables 5–7, PLAN statistical families and main-paper relationships are assigned to other fresh statistical shards. Unique paired inventory: `statistics/parts/statistical_support.md`.

Read completely: QUALITY_CONTROL_SCOPE.md, Workflow 1.6.1 review_contract.md, PERFORMANCE_PROFILE.md, report_spec.md and settings.toml. Read current source/tooling/asset inventories and current source-linked evidence maps; source-matched reusable native/layout text and all assigned renders were used. No old candidate, checker, disposition, screening or report was a scientific input; no web, GPU, additional Python or source mutation was used. Only owned part files were written. Direct tool record follows `tooling_record.md`.

## Checks and outcome

All 68 displayed estimate/95% CI tuples have ordered endpoints and contain their point estimate. All eTable 1 directions are consistent with missing-minus-complete adjacent columns within display precision; eTable 2 differences are consistent with the explicitly stated marginal intervention-minus-control contrast. Every marginal point and both CI endpoints are retained in the paired inventory. No P value/test statistic/standard error is supplied for these table tuples. Test sidedness, row-specific distribution/model, covariance, interval construction and degrees of freedom cannot be inferred from convention. A normal approximation is not substituted for a source-specified analysis.

All available eTable 3–4 medians lie within ordered IQRs; descriptive SDs are nonnegative and are distinguished from intervals. The step/arm structure and creatinine collection timing are coherent. All assigned graph symbols, visible interval stems and both endpoints were inspected, with complete sixty-cell temporal-graph records and sequential full-rank records for the residual/waterfall plots in the paired inventory. Visible intervals contain their markers; direction and phase labels reconcile. Overlap and point-only symbols preclude exact individual CI digitization; those values are not invented. The residual figure's own caption defines the zero comparison and direction sufficiently for its graphical use. No preferred method is proposed.

Findings meeting the inclusion threshold: **0**. No finding ID is assigned. No independent discrepancy beyond the source-grounded exclusions below remains in this scope. The following table records each excluded observation once, consolidating repeated patterns rather than listing every occurrence separately.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 p. 17 eTable 1 title, headers and footnote a; S155–S171/S235 | Footnote says intervention minus control although headers are complete and missing follow-up. Adjacent columns and signs identify missing minus complete immediately; for example 60.0−60.6=−0.6 and 42.4−30.8=11.6. | CONTEXT_RESOLVES |
| REPORT DOC-004 p. 17 eTable 1 symptom-to-door time and creatinine; p. 18 eTable 2 triglycerides and creatinine; S162/S169/S213/S215 | Differences appear to exceed subtraction of rounded centers or CI appears zero-width. Half-unit intervals permit the displayed results: 266.49−245.51=20.98 rounds to 21; 1.049−0.951=0.098 rounds to 0.1; 121.49−120.51=0.98 rounds to 1; eTable 2 creatinine endpoints 0.96/1.04 both display as 1.0. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-004 p. 18 eTable 2 modeled baseline marginal effects/differences versus raw main Table 1 and eTables 3–4; S172–S222/S236 | Adjusted marginal means/proportions and differences can differ materially from crude group summaries, including transfer and insurance direction. Footnote explicitly supplies hospital random effect and temporal trend with mixed logistic, linear or quantile regression. | MODEL_VERSUS_CRUDE |
| REPORT DOC-004 p. 17 eTable 1 initial troponin difference3.3(95% CI0.1–6.5); REPORT main physical p. 6 missing-follow-up comparison P<.001; S166 | A same-test reconstruction would require unreported test, sidedness, interval construction and estimand mapping. Both printed results indicate a difference; a median-difference CI and a distribution comparison need not be the same analysis. Main S093 owns that P-value relationship. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-004 p. 17 eTable 1 and p. 18 eTable 2, all CI-bearing rows; S155–S222/S235/S236 | Exact baseline CI reproduction would require row-specific available-case n, interval construction, test/sidedness, covariance or row-specific model details not printed here. Unreported details alone do not establish an inconsistency or an analysis whose reported quantity is unidentified. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-004 p. 1 contents expected−observed description versus p. 24 eFigure 1A caption, ascending residuals and zero line; S223 | Contents wording differs from the figure's explicit lower-rate left/higher-rate right caption. The actual display and its caption resolve direction; this contents label does not create an ambiguous extracted primary treatment estimate. | CONTEXT_RESOLVES |
| REPORT DOC-004 pp. 24, 26–27 all hospital residual/rate graphical intervals; S223/S225–S234 | Exact hospital point estimates, numerators/denominators, individual interval endpoints/methods, clipping details and numeric residual transformation are not supplied. Overlapping or point-only marks cannot support invented interval reconstruction or significance assignments. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-004 p. 25 eFigure 1B axis and caption; S224 | Control−intervention sign is the opposite algebraic convention to treatment-minus-control adjusted differences elsewhere; the axis explicitly defines a decrease and makes positive/negative interpretation clear. | CONTEXT_RESOLVES |
| REPORT DOC-004 p. 24 eFigure 1A caption; S223 | Per-hospital zero-nonoverlap at the 5% level does not supply a family-level multiplicity claim. Treating that caption as an adjusted simultaneous test would require an unreported assumption. | CONDITIONAL_OR_UNREPORTED |

## Completion and limitations

Pass 1 complete for S155–S237: 83 relationships; 0 emitted findings; 9 consolidated excluded observations. All eight assigned result pages and the p. 1 context were covered. No scientific scope gap. Limitations: exact per-hospital graph coordinates and interval endpoints absent; overplotted or point-only marks not fully numerically separable; baseline and graphical interval/test construction incompletely specified for exact reconstruction. There is no new sample-size, superiority/noninferiority/equivalence, interim, stopping or multiplicity decision statement in this assigned display scope. Parent coordinator merges this part without loss; a distinct fresh pass-2 agent must revisit every registered S ID after the full ledger, screening and recheck are available.
# Statistical pass 1 — support outcomes shard

Stage `statistics_pass_1`; fresh runtime identity `/root/statistics_1_outcomes`; model `gpt-6.1-sol`; reasoning effort `high`; start mode `FRESH_SPAWN`. This agent is not a mapper or a pass-2 agent. Coordinator retains the actual spawn-return ID for `agent_execution_manifest.md`.

Exact assigned scope: REPORT DOC-004 physical pp.21–23, eTables5–7, all66 printed estimate/95% CI tuples and exact associated footnotes/model text, with matched main REPORT context on physical pp.3,7–9. The tuple IDs are S320–S385; method IDs are S386–S388. Each of69 records is explicitly PASS_1_COMPLETE in `statistics/parts/statistical_support_outcomes.md`. Baseline eTables1–4, eFigures, and PLAN families are assigned elsewhere.

Read completely: `QUALITY_CONTROL_SCOPE.md`, `workflow_1_6_1/review_contract.md`, `PERFORMANCE_PROFILE.md`, `workflow_1_6_1/report_spec.md`, and `workflow_1_6_1/settings.toml`. Routing preflight reports PASS. Tooling record authorizes direct Poppler text/rendering and records no OCR or Office converter. Current source/evidence inventories and complete assigned support map entries were read. Source-matched existing renders DOC-004-21/22/23 were inspected visually. Direct `pdftotext -layout -f 21 -l 23 joi170166supp3_prod.pdf -` confirmed table numerals and footnotes without writing any scratch derivative. No supplied source, reused asset, or another agent's artifact was changed; no old scientific conclusions, web, GPU, or Python scientific review were used.

## Completed checks

- All40 eTable5 OR/CI tuples, all10 eTable6 OR/CI tuples, and all16 eTable7 RD/OR/CI tuples have ordered endpoints and contain their point estimates. Every OR and its endpoints is positive. Exact printed tuples and their individual checks are preserved in the inventory.
- Intervention/control direction agrees in all eight paired RD/OR comparisons in eTable7: expanded composite C and P, heart failure C and P, shock C and P all have RD<0 and OR<1; cardiac arrest C has RD0.16 and OR1.08, while P has RD−0.20 and OR0.91. The changed adjusted direction is not a raw-count arithmetic comparison.
- Model and effect-measure identity are explicit for eTable5 sensitivities and eTable7's cluster-only versus cluster/time analyses. eTable7 specifies OR intervention/control and RD marginal intervention minus control, keeping these distinct. eTable6 identifies an interaction-adjusted sensitivity model; no coefficient-specific exposure reference is supplied. No missing parameter is supplied from convention.
- Confidence level95% is printed. No tuple includes a P value, test statistic, standard error, interval-construction method, covariance or variance estimator. Exact estimate/interval/test compatibility cannot be mechanically reconstructed without those inputs. No Wald approximation, interval-derived P value or assumed degrees of freedom is used as a finding rule.
- No superiority, noninferiority, equivalence, multiplicity, interim or stopping decision is newly asserted in the assigned tables. The main article treats secondary results as exploratory and reports the time-exposure exercise as post hoc. The source does not prescribe a noninferiority/equivalence margin for these results. The main primary no-decrease interpretation is not contradicted by eTable5 primary intervals or the eTable6 primary interval, which all include1.
- Source-described models account for hospital clustering and, where stated, the fixed temporal structure. No preference for an alternate method is introduced. Medication and counseling eligibility/discharge definitions are preserved. There is no assigned new sample-size calculation. Missing analytic Ns or missingness implementations in sensitivity tables alone cannot supply a reproducible sample-size inconsistency.
- All eTable7 arm count/percentage pairs reconcile at one decimal using denominators10066/11308: expanded9.1297/7.0304%; HF2.2551/1.6891%; shock2.1558/1.5034%; arrest2.0465/2.0959%. These are direct arithmetic percentages, not model diagnostics. The expanded endpoint's main p.8–9 OR0.89(0.80–1.00), primary OR0.84(0.70–1.00), RD−1.34(−2.72 to0.04), and rates7.0/9.1% match the supplement. Composite counts are not treated as sums of independent events. All four ICCs are within[0,1], with no variance equation supplied for further reproduction.

## Findings

Zero findings meet all four inclusion conditions after self-screening. No F-ST1-301 or other finding ID is assigned. This does not adjudicate any result; it records completed scope and the threshold decision.

## Excluded observations

Each observation is recorded once with exactly one scope reason code. Ordinary reconciled tuples are documented in the relationship inventory rather than repeated here.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 pp.21–23 eTables5–7 headers and all tuples | No row P value, test statistic, standard error, exact interval-construction method or variance estimator is printed. An interval-to-test inconsistency would require assuming those absent inputs. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-004 p.23 eTable7 counts, model columns and footnote a; REPORT DOC-004 p.21 eTable5 sensitivity columns | Crude ratios/differences differ from model effects. Expanded crude risk difference is approximately−2.10 percentage points while cluster RD is−0.86; crude arrest direction is positive while the cluster/time RD is−0.20. Printed footnotes expressly identify mixed-model marginal differences and adjusted ORs. No crude-versus-model discrepancy qualifies. | MODEL_VERSUS_CRUDE |
| REPORT DOC-004 p.22 eTable6 title and OR column; REPORT DOC-001 pp.3,8 exposure-time analysis | Exposure-time unit/coding, centering/reference, coefficient-specific mapping, interaction coefficient and its test are not printed. Immediate context identifies an interaction-adjusted sensitivity analysis; treating the OR as a specific interaction multiplier or a conditional effect at an assumed time would go beyond supplied text. The missing items alone do not reproduce a contradictory analysis. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-004 p.22 eTable6 optimal in-hospital medication0.87(0.70–1.07), p.21 eTable5 values1.45–2.19; REPORT DOC-001 p.8 “overall effects were similar” paragraph | These exploratory process estimates use different models. The main statement does not assert an unchanged estimate for every process row, and comparing secondary sensitivity values across model specifications does not change a primary/key secondary result, analysis population size or decision rule. | PERIPHERAL_COMPARISON |
| REPORT DOC-004 p.21 eTable5 footnote c; p.22 eTable6 footnote b; REPORT DOC-001 p.3 secondary-outcome definition | In-hospital medication list uses anticoagulant in the main/eTable5 and heparin in eTable6. The clinical class/member wording is readily resolvable; supplied text does not establish a different eligible composite population or alternate drug contribution that changes a reported value. | TERMINOLOGY_OR_WORDING |
| REPORT DOC-004 p.21 eTable5 GRACE-column footnote and results; REPORT DOC-001 p.3 model covariates | Analytic sample Ns and missing-creatinine/covariate handling are not printed for the GRACE sensitivity column. No specific sample attrition, imputation, omission or contradiction with intention-to-treat is inferred from that absence. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-004 p.23 eTable7 expanded-composite cluster RD−0.86(−1.72 to−0.01) and OR0.89(0.80–1.00); primary RD−1.34(−2.72 to0.04) and OR0.84(0.70–1.00) | An upper OR limit displayed1.00 has half-unit rounding interval[0.995,1.005]. It can be below1 for the cluster model or above1 for the primary model. The printed endpoint cannot support an apparent conflicting null-inclusion claim; the RD/OR interval methods also are not stated to be identical. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-004 p.21 eTable5 30-day mortality versus cardiovascular mortality, transfer/insurance/aspirin columns | Three pairs of identical two-decimal estimates and intervals do not establish duplication of distinct results: closely overlapping mortality events and rounding can produce identical displayed values. No source asserts that these models must yield distinct printed values. | CONTEXT_RESOLVES |

## Limitations and handoff

There are no scientific coverage gaps in this three-page shard. Exact mechanical test reproduction is limited by the missing inputs listed above; exposure coding and sensitivity analytic sample Ns cannot be reconstructed. No assumption or diagnostic approximation substitutes for these definitions. Full69-record inventory provides a durable source-grounded pass-2 scope. Pass 2 must be performed by a newly spawned different runtime under gpt-6.1-sol/high after the complete ledger, screening log and mechanical recheck exist.

Counts: pass1; source pages3; printed tuples66; associated methods3; relationships69; IDs S320–S388; findings0; excluded observations8; unresolved scientific units0.

## Per-relationship pass-1 completion register

The following register is merged mechanically from the fresh specialists' individual source-grounded inventory rows. Full printed evidence, checks, limitations and source locations remain in statistics/relationship_inventory.md; no relationship is represented only by a range.

| Relationship ID | Completion |
|---|---|
| S001 | PASS_1_COMPLETE |
| S002 | PASS_1_COMPLETE |
| S003 | PASS_1_COMPLETE |
| S004 | PASS_1_COMPLETE |
| S005 | PASS_1_COMPLETE |
| S006 | PASS_1_COMPLETE |
| S007 | PASS_1_COMPLETE |
| S008 | PASS_1_COMPLETE |
| S009 | PASS_1_COMPLETE |
| S010 | PASS_1_COMPLETE |
| S011 | PASS_1_COMPLETE |
| S012 | PASS_1_COMPLETE |
| S013 | PASS_1_COMPLETE |
| S014 | PASS_1_COMPLETE |
| S015 | PASS_1_COMPLETE |
| S016 | PASS_1_COMPLETE |
| S017 | PASS_1_COMPLETE |
| S018 | PASS_1_COMPLETE |
| S019 | PASS_1_COMPLETE |
| S020 | PASS_1_COMPLETE |
| S021 | PASS_1_COMPLETE |
| S022 | PASS_1_COMPLETE |
| S023 | PASS_1_COMPLETE |
| S024 | PASS_1_COMPLETE |
| S025 | PASS_1_COMPLETE |
| S026 | PASS_1_COMPLETE |
| S027 | PASS_1_COMPLETE |
| S028 | PASS_1_COMPLETE |
| S029 | PASS_1_COMPLETE |
| S030 | PASS_1_COMPLETE |
| S031 | PASS_1_COMPLETE |
| S032 | PASS_1_COMPLETE |
| S033 | PASS_1_COMPLETE |
| S034 | PASS_1_COMPLETE |
| S035 | PASS_1_COMPLETE |
| S036 | PASS_1_COMPLETE |
| S037 | PASS_1_COMPLETE |
| S038 | PASS_1_COMPLETE |
| S039 | PASS_1_COMPLETE |
| S040 | PASS_1_COMPLETE |
| S041 | PASS_1_COMPLETE |
| S042 | PASS_1_COMPLETE |
| S043 | PASS_1_COMPLETE |
| S044 | PASS_1_COMPLETE |
| S045 | PASS_1_COMPLETE |
| S046 | PASS_1_COMPLETE |
| S047 | PASS_1_COMPLETE |
| S048 | PASS_1_COMPLETE |
| S049 | PASS_1_COMPLETE |
| S050 | PASS_1_COMPLETE |
| S051 | PASS_1_COMPLETE |
| S052 | PASS_1_COMPLETE |
| S053 | PASS_1_COMPLETE |
| S054 | PASS_1_COMPLETE |
| S055 | PASS_1_COMPLETE |
| S056 | PASS_1_COMPLETE |
| S057 | PASS_1_COMPLETE |
| S058 | PASS_1_COMPLETE |
| S059 | PASS_1_COMPLETE |
| S060 | PASS_1_COMPLETE |
| S061 | PASS_1_COMPLETE |
| S062 | PASS_1_COMPLETE |
| S063 | PASS_1_COMPLETE |
| S064 | PASS_1_COMPLETE |
| S065 | PASS_1_COMPLETE |
| S066 | PASS_1_COMPLETE |
| S067 | PASS_1_COMPLETE |
| S068 | PASS_1_COMPLETE |
| S069 | PASS_1_COMPLETE |
| S070 | PASS_1_COMPLETE |
| S071 | PASS_1_COMPLETE |
| S072 | PASS_1_COMPLETE |
| S073 | PASS_1_COMPLETE |
| S074 | PASS_1_COMPLETE |
| S075 | PASS_1_COMPLETE |
| S076 | PASS_1_COMPLETE |
| S077 | PASS_1_COMPLETE |
| S078 | PASS_1_COMPLETE |
| S079 | PASS_1_COMPLETE |
| S080 | PASS_1_COMPLETE |
| S081 | PASS_1_COMPLETE |
| S082 | PASS_1_COMPLETE |
| S083 | PASS_1_COMPLETE |
| S084 | PASS_1_COMPLETE |
| S085 | PASS_1_COMPLETE |
| S086 | PASS_1_COMPLETE |
| S087 | PASS_1_COMPLETE |
| S088 | PASS_1_COMPLETE |
| S089 | PASS_1_COMPLETE |
| S090 | PASS_1_COMPLETE |
| S091 | PASS_1_COMPLETE |
| S092 | PASS_1_COMPLETE |
| S093 | PASS_1_COMPLETE |
| S094 | PASS_1_COMPLETE |
| S400 | PASS_1_COMPLETE |
| S401 | PASS_1_COMPLETE |
| S402 | PASS_1_COMPLETE |
| S403 | PASS_1_COMPLETE |
| S404 | PASS_1_COMPLETE |
| S405 | PASS_1_COMPLETE |
| S406 | PASS_1_COMPLETE |
| S407 | PASS_1_COMPLETE |
| S408 | PASS_1_COMPLETE |
| S409 | PASS_1_COMPLETE |
| S410 | PASS_1_COMPLETE |
| S411 | PASS_1_COMPLETE |
| S412 | PASS_1_COMPLETE |
| S413 | PASS_1_COMPLETE |
| S414 | PASS_1_COMPLETE |
| S415 | PASS_1_COMPLETE |
| S416 | PASS_1_COMPLETE |
| S417 | PASS_1_COMPLETE |
| S095 | PASS_1_COMPLETE |
| S096 | PASS_1_COMPLETE |
| S097 | PASS_1_COMPLETE |
| S098 | PASS_1_COMPLETE |
| S099 | PASS_1_COMPLETE |
| S100 | PASS_1_COMPLETE |
| S101 | PASS_1_COMPLETE |
| S102 | PASS_1_COMPLETE |
| S103 | PASS_1_COMPLETE |
| S104 | PASS_1_COMPLETE |
| S105 | PASS_1_COMPLETE |
| S106 | PASS_1_COMPLETE |
| S107 | PASS_1_COMPLETE |
| S108 | PASS_1_COMPLETE |
| S109 | PASS_1_COMPLETE |
| S110 | PASS_1_COMPLETE |
| S111 | PASS_1_COMPLETE |
| S112 | PASS_1_COMPLETE |
| S113 | PASS_1_COMPLETE |
| S114 | PASS_1_COMPLETE |
| S115 | PASS_1_COMPLETE |
| S116 | PASS_1_COMPLETE |
| S117 | PASS_1_COMPLETE |
| S118 | PASS_1_COMPLETE |
| S119 | PASS_1_COMPLETE |
| S120 | PASS_1_COMPLETE |
| S121 | PASS_1_COMPLETE |
| S122 | PASS_1_COMPLETE |
| S123 | PASS_1_COMPLETE |
| S124 | PASS_1_COMPLETE |
| S125 | PASS_1_COMPLETE |
| S126 | PASS_1_COMPLETE |
| S127 | PASS_1_COMPLETE |
| S128 | PASS_1_COMPLETE |
| S129 | PASS_1_COMPLETE |
| S130 | PASS_1_COMPLETE |
| S131 | PASS_1_COMPLETE |
| S132 | PASS_1_COMPLETE |
| S133 | PASS_1_COMPLETE |
| S134 | PASS_1_COMPLETE |
| S135 | PASS_1_COMPLETE |
| S136 | PASS_1_COMPLETE |
| S137 | PASS_1_COMPLETE |
| S138 | PASS_1_COMPLETE |
| S139 | PASS_1_COMPLETE |
| S140 | PASS_1_COMPLETE |
| S141 | PASS_1_COMPLETE |
| S142 | PASS_1_COMPLETE |
| S143 | PASS_1_COMPLETE |
| S144 | PASS_1_COMPLETE |
| S145 | PASS_1_COMPLETE |
| S146 | PASS_1_COMPLETE |
| S147 | PASS_1_COMPLETE |
| S148 | PASS_1_COMPLETE |
| S149 | PASS_1_COMPLETE |
| S150 | PASS_1_COMPLETE |
| S151 | PASS_1_COMPLETE |
| S152 | PASS_1_COMPLETE |
| S153 | PASS_1_COMPLETE |
| S154 | PASS_1_COMPLETE |
| S155 | PASS_1_COMPLETE |
| S156 | PASS_1_COMPLETE |
| S157 | PASS_1_COMPLETE |
| S158 | PASS_1_COMPLETE |
| S159 | PASS_1_COMPLETE |
| S160 | PASS_1_COMPLETE |
| S161 | PASS_1_COMPLETE |
| S162 | PASS_1_COMPLETE |
| S163 | PASS_1_COMPLETE |
| S164 | PASS_1_COMPLETE |
| S165 | PASS_1_COMPLETE |
| S166 | PASS_1_COMPLETE |
| S167 | PASS_1_COMPLETE |
| S168 | PASS_1_COMPLETE |
| S169 | PASS_1_COMPLETE |
| S170 | PASS_1_COMPLETE |
| S171 | PASS_1_COMPLETE |
| S172 | PASS_1_COMPLETE |
| S173 | PASS_1_COMPLETE |
| S174 | PASS_1_COMPLETE |
| S175 | PASS_1_COMPLETE |
| S176 | PASS_1_COMPLETE |
| S177 | PASS_1_COMPLETE |
| S178 | PASS_1_COMPLETE |
| S179 | PASS_1_COMPLETE |
| S180 | PASS_1_COMPLETE |
| S181 | PASS_1_COMPLETE |
| S182 | PASS_1_COMPLETE |
| S183 | PASS_1_COMPLETE |
| S184 | PASS_1_COMPLETE |
| S185 | PASS_1_COMPLETE |
| S186 | PASS_1_COMPLETE |
| S187 | PASS_1_COMPLETE |
| S188 | PASS_1_COMPLETE |
| S189 | PASS_1_COMPLETE |
| S190 | PASS_1_COMPLETE |
| S191 | PASS_1_COMPLETE |
| S192 | PASS_1_COMPLETE |
| S193 | PASS_1_COMPLETE |
| S194 | PASS_1_COMPLETE |
| S195 | PASS_1_COMPLETE |
| S196 | PASS_1_COMPLETE |
| S197 | PASS_1_COMPLETE |
| S198 | PASS_1_COMPLETE |
| S199 | PASS_1_COMPLETE |
| S200 | PASS_1_COMPLETE |
| S201 | PASS_1_COMPLETE |
| S202 | PASS_1_COMPLETE |
| S203 | PASS_1_COMPLETE |
| S204 | PASS_1_COMPLETE |
| S205 | PASS_1_COMPLETE |
| S206 | PASS_1_COMPLETE |
| S207 | PASS_1_COMPLETE |
| S208 | PASS_1_COMPLETE |
| S209 | PASS_1_COMPLETE |
| S210 | PASS_1_COMPLETE |
| S211 | PASS_1_COMPLETE |
| S212 | PASS_1_COMPLETE |
| S213 | PASS_1_COMPLETE |
| S214 | PASS_1_COMPLETE |
| S215 | PASS_1_COMPLETE |
| S216 | PASS_1_COMPLETE |
| S217 | PASS_1_COMPLETE |
| S218 | PASS_1_COMPLETE |
| S219 | PASS_1_COMPLETE |
| S220 | PASS_1_COMPLETE |
| S221 | PASS_1_COMPLETE |
| S222 | PASS_1_COMPLETE |
| S223 | PASS_1_COMPLETE |
| S224 | PASS_1_COMPLETE |
| S225 | PASS_1_COMPLETE |
| S226 | PASS_1_COMPLETE |
| S227 | PASS_1_COMPLETE |
| S228 | PASS_1_COMPLETE |
| S229 | PASS_1_COMPLETE |
| S230 | PASS_1_COMPLETE |
| S231 | PASS_1_COMPLETE |
| S232 | PASS_1_COMPLETE |
| S233 | PASS_1_COMPLETE |
| S234 | PASS_1_COMPLETE |
| S235 | PASS_1_COMPLETE |
| S236 | PASS_1_COMPLETE |
| S237 | PASS_1_COMPLETE |
| S320 | PASS_1_COMPLETE |
| S321 | PASS_1_COMPLETE |
| S322 | PASS_1_COMPLETE |
| S323 | PASS_1_COMPLETE |
| S324 | PASS_1_COMPLETE |
| S325 | PASS_1_COMPLETE |
| S326 | PASS_1_COMPLETE |
| S327 | PASS_1_COMPLETE |
| S328 | PASS_1_COMPLETE |
| S329 | PASS_1_COMPLETE |
| S330 | PASS_1_COMPLETE |
| S331 | PASS_1_COMPLETE |
| S332 | PASS_1_COMPLETE |
| S333 | PASS_1_COMPLETE |
| S334 | PASS_1_COMPLETE |
| S335 | PASS_1_COMPLETE |
| S336 | PASS_1_COMPLETE |
| S337 | PASS_1_COMPLETE |
| S338 | PASS_1_COMPLETE |
| S339 | PASS_1_COMPLETE |
| S340 | PASS_1_COMPLETE |
| S341 | PASS_1_COMPLETE |
| S342 | PASS_1_COMPLETE |
| S343 | PASS_1_COMPLETE |
| S344 | PASS_1_COMPLETE |
| S345 | PASS_1_COMPLETE |
| S346 | PASS_1_COMPLETE |
| S347 | PASS_1_COMPLETE |
| S348 | PASS_1_COMPLETE |
| S349 | PASS_1_COMPLETE |
| S350 | PASS_1_COMPLETE |
| S351 | PASS_1_COMPLETE |
| S352 | PASS_1_COMPLETE |
| S353 | PASS_1_COMPLETE |
| S354 | PASS_1_COMPLETE |
| S355 | PASS_1_COMPLETE |
| S356 | PASS_1_COMPLETE |
| S357 | PASS_1_COMPLETE |
| S358 | PASS_1_COMPLETE |
| S359 | PASS_1_COMPLETE |
| S360 | PASS_1_COMPLETE |
| S361 | PASS_1_COMPLETE |
| S362 | PASS_1_COMPLETE |
| S363 | PASS_1_COMPLETE |
| S364 | PASS_1_COMPLETE |
| S365 | PASS_1_COMPLETE |
| S366 | PASS_1_COMPLETE |
| S367 | PASS_1_COMPLETE |
| S368 | PASS_1_COMPLETE |
| S369 | PASS_1_COMPLETE |
| S370 | PASS_1_COMPLETE |
| S371 | PASS_1_COMPLETE |
| S372 | PASS_1_COMPLETE |
| S373 | PASS_1_COMPLETE |
| S374 | PASS_1_COMPLETE |
| S375 | PASS_1_COMPLETE |
| S376 | PASS_1_COMPLETE |
| S377 | PASS_1_COMPLETE |
| S378 | PASS_1_COMPLETE |
| S379 | PASS_1_COMPLETE |
| S380 | PASS_1_COMPLETE |
| S381 | PASS_1_COMPLETE |
| S382 | PASS_1_COMPLETE |
| S383 | PASS_1_COMPLETE |
| S384 | PASS_1_COMPLETE |
| S385 | PASS_1_COMPLETE |
| S386 | PASS_1_COMPLETE |
| S387 | PASS_1_COMPLETE |
| S388 | PASS_1_COMPLETE |
