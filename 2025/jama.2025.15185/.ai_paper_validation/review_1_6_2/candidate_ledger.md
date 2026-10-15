# Candidate Ledger

All candidates are Pending Human Adjudication. The independent initial screen included 11 findings consolidated into six issues; four findings were screened out. Stable IDs follow the first conflicting report anchor, then reading order within a page. Corroborating and contextual locations do not change the ordering anchor. In particular, the bounded adherence comparison is context for the missing-primary-analysis pattern, whose central report anchor follows the secondary-method paragraph on main p5.

The mechanical recheck reproduced all six comparisons and retained the provisional classifications. The final quality auditor confirmed inclusion of all six issues. IDs will not be deleted or renumbered.

| ID | Review domain | Relationship type | All relationships | Compared document roles | Evidence state | Inclusion audit | Finding IDs |
|---|---|---|---|---|---|---|---|
| C001 | statistical_results | S_W | S_W | REPORT main article p3 vs REPORT main article p6 | reproduced | CONFIRMED | F-ST1-007 |
| C002 | protocol_report | P_R | P_R, P_P | PLAN protocol pp86-87 vs PLAN SAP pp4,6-7 vs REPORT main article pp4-5 and results supplement pp12-13 | reproduced | CONFIRMED | F-XS-102, F-ST1-002 |
| C003 | protocol_report | P_R | P_R, P_P | PLAN protocol pp56,86 vs PLAN SAP p10 vs REPORT main article pp4-5 and analysis code p1 | reproduced | CONFIRMED | F-XS-101, F-ST1-001 |
| C004 | protocol_report | P_R | P_R | PLAN SAP pp5,11 vs REPORT main article pp5-6 and results supplement pp7,15 | reproduced | CONFIRMED | F-XS-104, F-ST1-005 |
| C005 | protocol_report | P_R | P_R | PLAN protocol p86 and SAP pp11-12,15 vs REPORT main article pp5-7 and results supplement pp13-14,18,25,27 | reproduced | CONFIRMED | F-XS-103, F-ST1-003, F-ST1-004 |
| C006 | statistical_results | S_W | S_W | REPORT main article Table2 p6 parent counts vs REPORT main article Table2 p6 component counts | reproduced | CONFIRMED | F-NUM-001 |


## C001 — PROMIS-29 scalar scoring and direction are not specified

**Candidate statement:** The report defines seven differently oriented PROMIS-29 domains but reports one scalar outcome and adjusted effect without identifying its aggregation, transformation or direction.

**Qualifying route:** Route B

**Status:** Pending Human Adjudication


- Findings: F-ST1-007; route B; proposed domain `statistical_results`; primary/all relationships `S_W`; REPORT main article definition versus REPORT main article scalar result, with the REPORT supplement only corroborating the scalar and PLAN protocol only contextual.
- Suggested source-order anchor: DOC-001p3, PROMIS-29 outcome definition, followed by DOC-001p6 result.
- All locations: [main p3, Secondary Outcomes](../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=3); [main p6, PROMIS-29 result](../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6); [results p15, PROMIS29 row](../../joi250066supp3_prod_1761597796.4701.pdf#page=15); contextual [protocol p70, PROMIS definition](../../joi250066supp1_prod_1761597796.4601.pdf#page=70).
- Source facts: main describes seven domains, four items/domain, raw4–20/domain, with higher scores meaning better in some domains and worse in others; it reports one L66(SD14),P65(14) and one adjusted difference−0.37[−3.34,2.61]; eTable4 reports L64.74(14.33),P65.11(13.79),the same effect,n582.
- Reason: the undefined function of those domains affects the scale/direction of this exact extracted effect; the domain definition and scalar result are both printed, so this is more than an unreported model option without a quantitative anchor.
- Precision: comparing a supposed individual raw domain upper bound20±0.5 with66±0.5 gives gap45/66=68.18%, but the paper does not claim this is an individual raw domain and that diagnostic is not the inclusion calculation; no numeric out-of-range assertion or route A claim is made.
- Alternatives/limit: a summed raw aggregate, transformed domain or recoded composite could produce a scalar; protocolp70 discusses population mean50/SD10 but does not identify the reported scalar's domains, aggregation or direction; no external scoring convention was imported.


## C002 — Primary analysis population changes from all randomized participants to survivors

**Candidate statement:** The protocol specifies an all-randomized primary analysis, while the SAP and report restrict primary FMA inference to survivors; death-inclusive analyses are supplementary.

**Qualifying route:** Route A, category 5

**Status:** Pending Human Adjudication


- Findings: F-XS-102,F-ST1-002; route A, category5; proposed domain `protocol_report`; primary `P_R`, all `P_R, P_P` because protocol and SAP themselves also differ.
- Suggested source-order anchor: DOC-001p4, primary population sentence, before its primary-model sentence.
- All locations: [protocol p86, §§11.4.1–11.4.2](../../joi250066supp1_prod_1761597796.4601.pdf#page=86); [protocol p87, §11.5](../../joi250066supp1_prod_1761597796.4601.pdf#page=87); [SAP p4, §3.2 and footnote](../../joi250066supp2_prod_1761597796.4701.pdf#page=4); [SAP p6, primary-estimand status](../../joi250066supp2_prod_1761597796.4701.pdf#page=6); [SAP p7, primary versus policyIII](../../joi250066supp2_prod_1761597796.4701.pdf#page=7); [main p4, Statistical Analyses](../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4); [main p5, flow and SAP explanation](../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5); [results p12, FAS definition](../../joi250066supp3_prod_1761597796.4701.pdf#page=12); [results p13, estimands1,3,4](../../joi250066supp3_prod_1761597796.4701.pdf#page=13).
- Source facts: protocol FAS=all randomized, primary performed on FAS, missing values imputed; SAP explicitly restricts deceased contributions to policyIII/composite; report excludes pre-three-month deaths from primary.610−28=582=296+286; deaths11+17=28; death-inclusive supplementary n610 remains labeled supplementary.
- Reason: categorical replacement of the primary population qualifies A5 regardless of whether the later prospective SAP intentionally supersedes the protocol; no count discrepancy is alleged and display precision is inapplicable to membership rules.
- Alternatives/limit: the endpoint is undefined after death and the protocol supplies no original numerical death rule; the SAP may be a prospective clarification, retained as an alternative without assuming an amendment outside the package.


## C003 — Primary mixed-model terms are absent from the implemented linear model

**Candidate statement:** The final protocol specifies a center random intercept and stroke-type fixed term, while the SAP, report and supplied code implement baseline-and-treatment linear regression.

**Qualifying route:** Route A, category 5

**Status:** Pending Human Adjudication


- Findings: F-XS-101,F-ST1-001; route A, category5; proposed domain `protocol_report`; primary `P_R`, all `P_R, P_P`.
- Suggested source-order anchor: DOC-001p4, primary linear model specification.
- All locations: [protocol p86, §11.4.2](../../joi250066supp1_prod_1761597796.4601.pdf#page=86); [protocol p56, synopsis](../../joi250066supp1_prod_1761597796.4601.pdf#page=56); [SAP p10, §5.2](../../joi250066supp2_prod_1761597796.4701.pdf#page=10); [main p4, primary model](../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4); [main p5, alignment explanation](../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5); [code p1, lines19–26](../../joi250066supp5_prod_1761597796.4751.pdf#page=1); historical corroboration [protocol p10](../../joi250066supp1_prod_1761597796.4601.pdf#page=10) and [protocol p39](../../joi250066supp1_prod_1761597796.4601.pdf#page=39).
- Source facts: final protocol specifies baseline+treatment+stroke-type fixed effects and center random intercept; SAP/main specify baseline+treatment linear regression; code line23 explicitly fits `lm(fma_affected.Visit_3 ~ fma_affected.Visit_1.cent + medication)`; primary−0.90[−3.78,1.98],P=.54. Earlier protocol versions contain center random intercept without stroke type and do not remove the final-version comparison.
- Reason: planned primary model replaced and original model result not identified; categorical formula/variance-structure comparison requires no rounding calculation and is unrelated to crude versus adjusted estimates.
- Alternatives/limit: SAP finalized before database closure may intentionally supersede protocol; explanation discusses terminology/estimands, not the omitted model terms, and no original mixed-model result is identified.


## C004 — Secondary missing-data procedures differ from the SAP rule

**Candidate statement:** The report discloses mRS and PRAI exceptions to the SAP general secondary-outcome imputation rule, affecting the methods and populations attached to the reported secondary results.

**Qualifying route:** Route B

**Status:** Pending Human Adjudication


- Findings: F-XS-104,F-ST1-005; route B; proposed domain `protocol_report`; primary/all relationships `P_R`.
- Suggested source-order anchor: DOC-001p5, secondary methods before center plot paragraph.
- All locations: [SAP p5, secondary list](../../joi250066supp2_prod_1761597796.4701.pdf#page=5); [SAP p11, §6](../../joi250066supp2_prod_1761597796.4701.pdf#page=11); [main p5, secondary methods](../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5); [main p6, mRS/PRAI results](../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6); [results p7, deviations](../../joi250066supp3_prod_1761597796.4701.pdf#page=7); [results p15, mRS/PRAI rows](../../joi250066supp3_prod_1761597796.4701.pdf#page=15).
- Source facts: SAP missing secondary outcomes imputed as primary except harms; main missing mRS/PRAI not imputed; supplement explicitly discloses death→mRS6 and no PRAI imputation; mRS0.93[0.69,1.23],n596 and PRAI n546=270+276 with51events/arm. No denominator arithmetic discrepancy is alleged.
- Reason B1: statistical missing-data/analysis-population specification is in scope and comparison tiers permit analysis specifications; it also bears on analysis-population sizes, rather than merely peripheral copied descriptions.
- Reason B2: nonimputation/death assignment and the general planned MI rule are substantively different procedures; disclosure identifies what was done but does not make the two specifications equivalent, with main nonimputation statement broader than the death-only mRS explanation.
- Reason B3: which patients/missing responses contribute affects interpretation/extraction of the named mRS odds ratio and PRAI proportions; no preferred approach is proposed.
- Exact route distinction: these are ordinary secondary procedures, not an outcome-status/composite change, an analysis expressly asserted prespecified despite absence from plan, or an unreported planned primary/key secondary analysis; A5's title alone is insufficient and inclusion rests on B.
- Alternatives/limit: death=6 follows the reported scale; intentional observed PRAI responses are explicitly disclosed; operative amendment/timing and surviving missing-mRS details are not supplied, and none is inferred.


## C005 — Planned primary-endpoint supplementary analyses are not identified in the report

**Candidate statement:** The supplied results do not identify the planned seven-variable subgroup interaction package, center-interaction model or additional-covariate primary sensitivities; alternative post hoc and baseline models do not supply those outputs.

**Qualifying route:** Route A, category 5

**Status:** Pending Human Adjudication


- Findings: F-XS-103,F-ST1-003,F-ST1-004; route A, category5; proposed domain `protocol_report`; primary/all relationships `P_R`.
- Suggested source-order anchor: DOC-001p5, post hoc subgroup/center methods and prespecified-analysis statement, with primary result p6.
- All locations: [protocol p86, §§11.4.1 and11.4.3a–e](../../joi250066supp1_prod_1761597796.4601.pdf#page=86); [SAP p11, §7](../../joi250066supp2_prod_1761597796.4701.pdf#page=11); [SAP p12, §7.2](../../joi250066supp2_prod_1761597796.4701.pdf#page=12); [SAP p15, subgroup addendum](../../joi250066supp2_prod_1761597796.4701.pdf#page=15); [main p4, adherence analysis](../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=4); [main p5, severity/center/spline methods and prespecification](../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=5); [main p6, primary/sensitivity result](../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6); [main p7, post hoc result](../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=7); [results p13, estimands1–8](../../joi250066supp3_prod_1761597796.4701.pdf#page=13); [results p14, post hoc estimands](../../joi250066supp3_prod_1761597796.4701.pdf#page=14); [results p18, eTables7/8](../../joi250066supp3_prod_1761597796.4701.pdf#page=18); [results p25, center graph](../../joi250066supp3_prod_1761597796.4701.pdf#page=25); [results p27, post hoc forest](../../joi250066supp3_prod_1761597796.4701.pdf#page=27).
- Source facts: SAP specifies primary-model interaction analyses/forest for age,sex,distal motor,cortical dysfunction,SSRI,stroke type,baseline severity with median cutoffs, plus center and center×treatment; protocol additionally specifies stroke-type interaction and covariate sensitivities age,sex,dementia,selective hand/wrist,cortical dysfunction,fatigue,SSRI,extrapyramidal symptoms,impetus. Supplied result inventory contains no corresponding seven-variable forest or these model outputs. Baseline-only interaction/spline models, descriptive center boxplots, and post hoc≤35/>35 severity display do not supply them.
- Consolidation: this is one repeated nonreporting/replacement pattern across planned analyses of the same primary result; center model and seven-variable package are not registered as separate issues merely because different checker headings describe them.
- Precision: not a comparison of rounded numeric copies; the planned median split and reported≤35/>35 split are distinct categorical rules, regardless of proximity; exact adjusted subgroup coordinates are not invented from graphs.
- Bounded additional location: protocol PP repeat allows justified reduced dose OR≥80%drug plus rehabilitation; post hoc strict dual-adherence result may implement part of it, but actual participant overlap/dose reductions cannot be inferred and are not an independent included issue.
- Alternatives/limit: models may have been fitted but output is outside the supplied package or deferred; later amendments may replace specifications; post hoc may describe particular graph implementation/pooling; the included observation remains the planned model outputs not identified in supplied results, not a claim about work elsewhere.


## C006 — Serious-event hierarchy counts do not reconcile with their parent totals

**Candidate statement:** Table 2 levodopa top-level categories sum to143 versus126 serious events, and placebo infection subtypes sum to52 versus44 infections, exceeding the display-precision threshold in both comparisons.

**Qualifying route:** Route A, category 3

**Status:** Pending Human Adjudication


- Findings: F-NUM-001; route A, category3; proposed domain `statistical_results`; primary/all relationships `S_W`.
- Suggested source-order anchor: DOC-001p6, Table2.
- All locations: [main p6, complete serious-event hierarchy and adverse-event narrative](../../jama_engelter_2025_oi_250066_1761597796.45511.pdf#page=6).
- Source facts: header Events,No.,L126/P129; L top-level55+16+5+12+4+4+6+3+3+2+1+0+32=143; P infections44 versus subtypes17+15+7+2+2+9=52. Indented stroke/cardiac/trauma subtypes are not counted again in top-level sum; other top-level row explicitly says none of the above. Narrative repeats parent totals, not category-derived totals.
- Half-unit rule: L sum[136.5,149.5],parent[125.5,126.5],gap10/126=.079365; P infection sum[49,55],parent[43.5,44.5],gap4.5/44=.102273. Both exceed.05 even allowing symmetric±.5 at a displayed zero. L infection and P overall sums independently fall below threshold and are not additional locations/issues.
- Reason: one counts-within-one-display repeated hierarchy pattern qualifies A3; a missing multiple-classification rule is an alternative, not an established explanation that reconciles the printed hierarchy.
- Alternatives/limit: one event may carry multiple diagnoses/sites or parent/components may use distinct units, but no such rule is printed; explicit event-versus-person distinction does not itself explain parent/component event counts.

