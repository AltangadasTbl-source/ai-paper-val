# Independent initial inclusion screen

Fresh runtime: root/inclusion_initial; gpt-6.1-sol/high; initial independent screening. Complete QUALITY_CONTROL_SCOPE.md and Workflow 1.6.2 review contract read. Scope: all 31 findings in the current canonical numeric (4), cross-source (11), and statistical-pass-1 (16) checker artifacts. No earlier scientific conclusions, external sources, or candidate-count expectation used. Sources and reused derivatives preserved. Decisions rest on independently reread exact source pages, direct native PDF extraction, and direct source-page renderings, rather than checker transcriptions alone.

All 31 findings have exactly one initial decision: 29 INCLUDE findings consolidated into 18 distinct issue groups, and 2 SCREENED_OUT findings (PERIPHERAL_COMPARISON: 1; CONDITIONAL_OR_UNREPORTED: 1). Repeated qualifying findings remain INCLUDE and will share their group's stable ID, preserving their provenance and union of locations. The coordinator assigned C001–C018 to these consolidated groups in source order. Every eventual candidate remains Pending Human Adjudication.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-NUM-001 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-NUM-002 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-NUM-101 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C017 |
| F-NUM-201 | numeric_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C018 |
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C010 |
| F-XS-002 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-XS-003 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-XS-004 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C015 |
| F-XS-005 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-XS-006 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C013 |
| F-XS-101 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C006 |
| F-XS-102 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-XS-103 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C017 |
| F-XS-104 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C018 |
| F-XS-105 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C005 |
| F-ST1-101 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C004 |
| F-ST1-201 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C017 |
| F-ST1-301 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C007 |
| F-ST1-302 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C008 |
| F-ST1-303 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C002 |
| F-ST1-304 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C003 |
| F-ST1-305 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C016 |
| F-ST1-306 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C009 |
| F-ST1-401 | statistics_pass_1 | initial | SCREENED_OUT | CONDITIONAL_OR_UNREPORTED | — |
| F-ST1-501 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C011 |
| F-ST1-502 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C010 |
| F-ST1-503 | statistics_pass_1 | initial | SCREENED_OUT | PERIPHERAL_COMPARISON | — |
| F-ST1-504 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C013 |
| F-ST1-505 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C014 |
| F-ST1-506 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C012 |
| F-ST2-601 | statistics_pass_2 | pass_2 | INCLUDE | MEETS_THRESHOLD | C019 |

## One-sentence decision justifications

- F-NUM-001: Route B qualifies because the same REPORT labels 8/336 and 204/336 as follow-up MRI populations, leaving the analysis-population size for the infarct-growth result unresolved well beyond display precision.
- F-NUM-002: Route B qualifies because Figure 2B's ≥100-mL EVT primary mRS distribution gives approximately 38% ambulation and 62% mRS≥4, whereas the matched discussion describes approximately 20% and 80%.
- F-NUM-101: Route A, category 2 qualifies because eFigure 13 labels the below-one side of an explicitly adverse-outcome EVT/MM risk contrast as favoring MM, reversing the printed estimates' treatment direction.
- F-NUM-201: Route A, category 3 qualifies because the same MM discordant-profile-2 populations in eTables 9 and 10 have mutually exclusive mRS0–3 and mRS5–6 event proportions exceeding 100% beyond precision.
- F-XS-001: Route A, category 5 qualifies because the same planned 90-day functional-independence endpoint has primary and secondary status, and imaging/stay endpoints change secondary-to-tertiary status within supplied PLAN material.
- F-XS-002: Route A, category 5 qualifies because the specific SAP calls composite core primary and prespecified while the REPORT calls its matched analyses post hoc sensitivities.
- F-XS-003: Route A, category 5 qualifies because the specific all-as-treated plan is replaced for primary imaging-stratified treatment comparisons by randomized-group reporting.
- F-XS-004: Route B qualifies because supplied plans define the reported sICH endpoint using 4-hour versus 24-hour ascertainment and differing death inclusion, leaving the definition attached to its reported event counts unclear.
- F-XS-005: Route B qualifies because the explicitly planned age/time prognostic analysis and supplied fitted surfaces use different time endpoints without an identified replacement specification; independent ambulation is not established as key secondary, so absent-key-secondary Route A status is not assumed.
- F-XS-006: Route A, category 2 qualifies because the literal positive alternative P(MM score≤EVT score)=.5+.0791 points toward lower MM disability while the printed decision is labeled EVT efficacy.
- F-XS-101: Route B qualifies because the matched ≥100-mL primary mRS distribution does not yield the supplementary independence/ambulation event percentages in either treatment arm after segment-wise rounding allowances.
- F-XS-102: Route A, category 2 qualifies because the narrative says EVT independence/ambulation probability increases with mismatch volume while both explicitly cited EVT curves decrease.
- F-XS-103: Route A, category 2 qualifies for the same eFigure 13 treatment-direction pattern as F-NUM-101.
- F-XS-104: Route A, category 2 qualifies because matched discordant-profile-2 favorable events move between explicitly labeled treatment arms, with unchanged arm denominators and a supporting distribution showing the opposing attribution.
- F-XS-105: Route B qualifies because CTP/MRI and composite core are distinct numerical covariates but competing captions and narrative do not identify which produced the 70/100/150-mL independent-ambulation surfaces.
- F-ST1-001: Route A, category 1 qualifies because two printed 95% intervals ending at ratio null 1.00 accompany significant-association statements, and hidden endpoint precision does not remove this category.
- F-ST1-101: Route B qualifies because finite RR1.00 and CI0.37–2.72 accompany all-zero within-subgroup outcomes despite a stated ordinary within-subgroup modified-Poisson analysis that needs an additional estimation step to produce a finite fit.
- F-ST1-201: Route A, category 2 qualifies for the same eFigure 13 direction pattern as F-NUM-101 and F-XS-103.
- F-ST1-301: Route A, category 2 qualifies for the same continuous mismatch-volume EVT narrative-versus-curve reversal as F-XS-102.
- F-ST1-302: Route B qualifies for the same competing core-covariate labels as F-XS-105.
- F-ST1-303: Route A, category 5 qualifies for the same replaced primary treatment-group specification as F-XS-003.
- F-ST1-304: Route A, category 5 qualifies for the same composite-core primary/prespecified-versus-post-hoc-sensitivity pattern as F-XS-002.
- F-ST1-305: Route A, category 5 qualifies because the SAP explicitly plans mismatch-volume 50/100-mL analyses of the primary 90-day mRS distribution, whereas the complete supplied REPORT counterpart scope contains only different joint profiles and continuous mismatch analyses.
- F-ST1-306: Route B qualifies for the same planned-versus-reported time-predictor definition as F-XS-005 without claiming that ambulation is key secondary.
- F-ST1-401: The source reproduces RR1.29(0.93–1.79) and RD0.168(0.011–0.325), but different adjusted scales and confidence constructions can yield different null-inclusion readings, and no supplied common estimand/interval identity or same-effect P/test establishes a contradiction rather than a missing mapping.
- F-ST1-501: Route A, category 1 qualifies because both historical SELECT 95% OR intervals print a lower endpoint of 1.00 while their P values .041/.049 are significant, and this always-register category is retained despite historical PLAN context.
- F-ST1-502: Route A, category 5 qualifies for the same protocol outcome-hierarchy pattern as F-XS-001.
- F-ST1-503: The source reproduces 21.2% versus 51.2% scenario-4 fixed-design simulation power, but this plan-internal operating-characteristic output is peripheral and does not change any printed sample-size/power input, primary decision boundary, reported primary/key result, or analysis-population size.
- F-ST1-504: Route A, category 2 qualifies for the same explicit planned probability-direction reversal as F-XS-006.
- F-ST1-505: Route B qualifies because the PLAN simultaneously retains a 200/380 inferential schedule with no additional analysis and reports a boundary-based rejection after 300 outcomes, leaving the operative stopping decision rule unidentified.
- F-ST1-506: Route A, category 1 qualifies because the historical safety statement includes sICH with P=.072 while describing the listed outcomes as significantly increased at the default .05 threshold.

## Consolidated issue groups

Group labels below preserve the screening handoff. The coordinator registered G001–G018 as C001–C018 in their stated source order. Locations listed as corroboration are retained but do not independently create a relationship type. Numeric findings use the half-unit display rule; discrete specifications and qualitative directions have no fabricated numerical discrepancy. No final correction or disposition is suggested.

### G001 — Follow-up MRI analysis-population count

Members: F-NUM-001. Source-order key: DOC-001:p004:Results-imaging.

Locations: REPORT [main p.4 Results imaging](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4), [p.9 infarct-growth paragraph](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9), [p.11 discussion](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=11); REPORT [results p.51 eTable11](../../../joi240006supp5_prod_1708623115.01733.pdf#page=51) corroborates 204=101+24+79.

Recommend statistical_results; primary/all relationship S_W. Route B. Source p.4 prints follow-up MRI8/336 and CT328/336; p.9 prints MR diffusion follow-up204(61%). Count intervals [7.5,8.5] and [203.5,204.5] leave gap195, relative195/8=24.375; percentage-copy gap58/2=29. This changes the population underpinning reported infarct-growth medians68/95/125mL. The baseline MRI total8 suggests a temporal-label alternative but does not identify a reconciled follow-up population. Ask which time point/population 8 represents. Supplemental p.51 and p.11 corroborate the larger population rather than create S_C.

### G002 — Primary treatment-group specification

Members: F-XS-003, F-ST1-303. Source-order key: DOC-001:p004:Statistical-Analysis-population.

Locations: PLAN [analysis SAP p.3 principles](../../../joi240006supp4_prod_1708623115.00733.pdf#page=3), [p.4 primary outcome analysis](../../../joi240006supp4_prod_1708623115.00733.pdf#page=4); REPORT [main p.4 population rule](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4), [p.6 Figure1](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6), [results p.8 flow](../../../joi240006supp5_prod_1708623115.01733.pdf#page=8), [p.38 eTable2](../../../joi240006supp5_prod_1708623115.01733.pdf#page=38).

Recommend protocol_report; primary/all P_R. Route A, category5. SAP specifies all analyses as-treated; REPORT expressly uses randomized allocation for across-treatment imaging comparisons and received treatment within arms. Printed168/168 versus170/166 and two MM→EVT crossovers establish different attribution, although counts individually reconcile. The parent trial ITT convention and supplied within-arm as-treated results do not report the planned across-arm as-treated primary comparison. Ask for the governing amendment/specification; no preferable approach is proposed.

### G003 — Composite-core analysis hierarchy and prespecification

Members: F-XS-002, F-ST1-304. Source-order key: DOC-001:p004:post-hoc-sensitivity.

Locations: PLAN [analysis SAP p.3 primary/sensitivity bullets](../../../joi240006supp4_prod_1708623115.00733.pdf#page=3), [p.7 appendix item1](../../../joi240006supp4_prod_1708623115.00733.pdf#page=7); REPORT [main p.1 abstract](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=1), [p.4 methods](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4), [p.6 Figure1/narrative](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6), [p.8 Figure3](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=8), [results p.16 eFigure10](../../../joi240006supp5_prod_1708623115.01733.pdf#page=16).

Recommend protocol_report; primary/all P_R. Route A, category5. SAP primary=max(hypodensity,CTP/MRI), sensitivity=CTP/MRI alone; appendix calls composite prespecified. REPORT calls composite/hypodensity analyses post hoc sensitivities and foregrounds CTP/MRI. These are distinct measurements (reported medians101 versus73mL), so this is an analysis-status comparison. Report p.11's broad preplanned-concept disclosure is an alternative distinction but does not supply an operative hierarchy amendment. Ask which primary/prespecified specification governed each analysis. Abstract is corroborating emphasis, not itself an explicit primary/sensitivity conflict.

### G004 — Finite all-zero subgroup risk estimates

Members: F-ST1-101. Source-order key: DOC-001:p004:within-subgroup-modified-Poisson.

Locations: REPORT [main p.4 method](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4); REPORT [results p.13 eFigure7 ASPECTS0–2](../../../joi240006supp5_prod_1708623115.01733.pdf#page=13), [p.14 eFigure8 ASPECTS0–2](../../../joi240006supp5_prod_1708623115.01733.pdf#page=14). PLAN [analysis SAP p.4](../../../joi240006supp4_prod_1708623115.00733.pdf#page=4) and [p.5](../../../joi240006supp4_prod_1708623115.00733.pdf#page=5) corroborate methods.

Recommend statistical_results; primary S_C; all S_C,S_W. Route B. Both source rows print zero outcomes in both arms, n19, and finiteRR1.00(0.37–2.72). Under the stated within-subgroup unrestricted Poisson fit an all-zero outcome has log likelihood−sum(exp(eta)); decreasing its intercept improves likelihood without a finite maximizer, so finite treatment RR/robust uncertainty needs an additional rule. Count0's half-unit interval has no other admissible nonnegative integer; all displayed ratio/limit intervals remain finite. This directly concerns printed extracted inferential results rather than a generic missing method detail. Pooled/regularized/pseudo-observation fitting or plotting placeholders are alternatives requiring identification, not adopted explanations. PLAN only corroborates, so no P_R.

### G005 — Printed null-boundary intervals and significant associations

Members: F-ST1-001. Source-order key: DOC-001:p006:ASPECTS-prognosis.

Locations: REPORT [main p.6 ASPECTS paragraph](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6), [p.7 Table2](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7), [p.10 age/time paragraph](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10), [p.4 two-sided .05 rule](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=4); [p.1 abstract](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=1) corroborates ASPECTS interval.

Recommend statistical_results; primary/all S_W. Route A, category1. Significant ASPECTS worsening accompanies0.91(0.82–1.00); significant imaging-to-reperfusion ambulation decrease accompanies0.97(0.93–1.00). Both printed95% intervals contain null1. Upper-limit half-unit interval[.995,1.005] permits a hidden limit below1, and a different test/marginal analysis is possible; these alternatives do not remove category1. Table2 interaction .83 is not the ASPECTS effect P. Ask for unrounded limits, corresponding effect Ps and inferential mappings for both associations. One repeated endpoint/significance pattern.

### G006 — Large-core primary mRS distribution and functional thresholds

Members: F-NUM-002, F-XS-101. Source-order key: DOC-001:p007:Figure2B.

Locations: REPORT [main p.7 Figure2B](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=7), [p.10 discussion](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10); REPORT [results p.13 eFigure7 ≥100mL](../../../joi240006supp5_prod_1708623115.01733.pdf#page=13), [p.14 eFigure8 ≥100mL](../../../joi240006supp5_prod_1708623115.01733.pdf#page=14). Main [p.3](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3) defines ambulation=mRS0–3.

Recommend statistical_results; primary S_C; all S_C,S_W. Route B. Visual legend confirmation yields Figure2B EVT2/6/10/20 for mRS0/1/2/3 and MM2/4/16 for mRS0/2/3, with absent-width mRS1 not fabricated as a printed cell. Cumulated EVT independence/ambulation intervals[16.5,19.5]/[36,40]% contrast supplementary[7.835,7.845]/[17.645,17.655]%; MM[5,7]/[20.5,23.5]% contrast[2.035,2.045]/[6.115,6.125]%. Relative minimum gaps1.104,1.039,1.449,2.349 all exceed.05. Count/denominator half-unit ranges also remain separated. Discussion20%ambulation/80%mRS≥4 versus Figure38%/62% leaves gaps15.5/20=.775 and15.5/80=.19375. All displays match primary90-day outcome, CTP/MRI≥100mL and ITT51/49. Two crossovers do not identify a matching partition. Ask which category distribution/threshold counts apply; no numeric replacement selected.

### G007 — EVT continuous mismatch prediction direction

Members: F-XS-102, F-ST1-301. Source-order key: DOC-001:p008:mismatch-volume-probability.

Locations: REPORT [main pp.8–9 spanning narrative](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=8), [continuation p.9](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=9); REPORT [results p.23 eFigure17A/B](../../../joi240006supp5_prod_1708623115.01733.pdf#page=23).

Recommend statistical_results; primary/all S_C. Route A, category2. Narrative says increasing mismatch volume increases EVT functional-independence/ambulation probability and decreases MM probability. The cited figure's cyan EVT curves decrease with increasing labeled mismatch volume in both A/B; MM also decreases. Curve direction visually reproduced without extracted coordinates. Binary mismatch presence is a different contrast and does not reconcile this continuous direction statement. Ask for the intended model/predictor/direction; combine both affected outcomes as one pattern.

### G008 — Core covariate identity in age/time surfaces

Members: F-XS-105, F-ST1-302. Source-order key: DOC-001:p010:age-time-core-definition.

Locations: REPORT [main p.10 age/time narrative](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10), [p.3 composite definition](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3); REPORT [results p.24 eFigure18 title/explanation](../../../joi240006supp5_prod_1708623115.01733.pdf#page=24), [p.25 eFigure19 title/explanation](../../../joi240006supp5_prod_1708623115.01733.pdf#page=25).

Recommend statistical_results; primary S_C; all S_C,S_W. Route B. eFigure18 title specifies CTP/MRI70/100/150mL but explanatory text specifies composite twice; eFigure19 title/text specify composite; main describes both as CTP/MRI. Supplied composite=max(CT hypodensity,CTP/MRI) distinguishes these covariates numerically. This quantity-changing label controls which analysis/patient measurement the fitted prognosis applies to; field terminology does not identify one variable. No plotted prediction is numerically invented. Ask for each fitted core covariate; possibilities of separate variables or shared composite remain alternatives.

### G009 — Planned versus reported prognostic time predictor

Members: F-XS-005, F-ST1-306. Source-order key: DOC-001:p010:age-time-predictor.

Locations: PLAN [analysis SAP p.5 §5.2.3](../../../joi240006supp4_prod_1708623115.00733.pdf#page=5); REPORT [main p.10 age/time results](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=10), [results p.24 eFigure18](../../../joi240006supp5_prod_1708623115.01733.pdf#page=24), [p.25 eFigure19](../../../joi240006supp5_prod_1708623115.01733.pdf#page=25); counterpart search scope all supplied REPORTs DOC-001pp1–14,DOC-006pp1–53,DOC-002pp1–30,DOC-007p1.

Recommend protocol_report; primary/all P_R. Route B, independently narrowed from F-XS-005's category5 claim. Ambulation is secondary, not established as key secondary or in the abstract; do not frame mere absent non-key analysis as category5. The qualifying comparison is the explicitly planned age×LKW-to-randomization model specification against reported age×imaging-to-reperfusion/end-procedure and age×LKW-to-reperfusion/end-procedure fitted surfaces, changing a meaningful numerical time predictor. Both variables cannot identify one planned model; timing in minutes and core settings are not the cause. Planned surfaces could be separate unreported analyses and reported surfaces additional exploratory analyses, which is the status ambiguity for human review. No supplied counterpart identifies the planned joint surface; adjustment for randomization time elsewhere does not provide it.

### G010 — Planned outcome hierarchy

Members: F-XS-001, F-ST1-502. Source-order key: DOC-003:p008:primary-outcome.

Locations: PLAN [protocol p.8 synopsis](../../../joi240006supp2_prod_1708623114.99233.pdf#page=8), [p.37 primary outcomes](../../../joi240006supp2_prod_1708623114.99233.pdf#page=37), [p.50 secondary analysis](../../../joi240006supp2_prod_1708623114.99233.pdf#page=50); PLAN [trial SAP p.13](../../../joi240006supp3_prod_1708623114.99733.pdf#page=13), [p.14](../../../joi240006supp3_prod_1708623114.99733.pdf#page=14), [p.17](../../../joi240006supp3_prod_1708623114.99733.pdf#page=17) secondary analysis is retained as checker-cited corroboration.

Recommend plan_material; primary/all P_P. Route A, category5. Protocol p.8/p.37 explicitly names mRS0–2 at90days second primary; p.50 explicitly calls it secondary. Protocol p.50 also gives secondary status to infarct volume/growth and length of stay, while SAPp.13/14 gives tertiary status. Same endpoints/status changes form one planned hierarchy pattern; later-version revision is an alternative but does not reconcile the dated protocol's internal statuses. Ask for operative hierarchy/amendment. No omitted parent-trial primary result is inferred.

### G011 — Historical SELECT null-boundary intervals and P values

Members: F-ST1-501. Source-order key: DOC-003:p013:historical-SELECT.

Locations: PLAN [protocol p.13 historical functional/ordinal results](../../../joi240006supp2_prod_1708623114.99233.pdf#page=13).

Recommend plan_material; primary/all P_P. Route A, category1. Direct page rendering confirms OR2.92(1.00–7.91),P=.041 andOR2.01(1.00–4.03),P=.049. Printed95% intervals include1 while P<.05. A rounded underlying lower bound above1 or a different CI/test method is possible; category1 expressly preserves both cases for adjudication and historical context does not remove an always-register observation. This is historical PLAN rationale, not an observed SELECT2 effect. Ask for underlying limits/methods; retain classification ambiguity that plan_material normally addresses prospective design but content is unequivocally PLAN.

### G012 — Historical safety significance statement

Members: F-ST1-506. Source-order key: DOC-003:p016:early-window-safety.

Locations: PLAN [protocol p.16 historical safety paragraph](../../../joi240006supp2_prod_1708623114.99233.pdf#page=16).

Recommend plan_material; primary/all P_P. Route A, category1. Sentence lists sICH8/173(5%)vs3/18(17%),P=.072, neurologic worseningP=.023 and mortalityP=.001, and says these safety outcomes significantly increased. P interval[.0715,.0725] is wholly>.05; counts/direction themselves reconcile. Collective or clinical-significance wording is an alternative, but no collective test or threshold is printed and the literal listed-test/significance conflict remains category1. Historical PLAN classification ambiguity retained. Ask whether the significance statement includes sICH and what threshold/test supports it.

### G013 — Planned efficacy probability direction

Members: F-XS-006, F-ST1-504. Source-order key: DOC-003:p037:lower-mRS-benefit (comparison appendicesp80–81).

Locations: PLAN [protocol p.37 score direction](../../../joi240006supp2_prod_1708623114.99233.pdf#page=37), [p.80 statistic/bounds](../../../joi240006supp2_prod_1708623114.99233.pdf#page=80), [p.81 alternative/variables](../../../joi240006supp2_prod_1708623114.99233.pdf#page=81); PLAN [trial SAP p.39](../../../joi240006supp3_prod_1708623114.99733.pdf#page=39), [p.40](../../../joi240006supp3_prod_1708623114.99733.pdf#page=40). REPORT [main p.3](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3) corroborates only score direction.

Recommend plan_material; primary/all P_P. Route A, category2, strengthened from F-XS-006's general-route proposal by the explicit treatment-score reversal. Source formulaP(Y≤X)=.5+theta,theta=.0791,Y=MMscore,X=EVTscore increases the probability MM disability is no greater than EVT, contrary to named EVT efficacy and lower-score benefit. Illustrative EVT0/MM6 yieldsY≤X=false. Rank-sum WEVT centered with positive efficacy boundaries2.604/2.772 additionally needs rank direction; descending ranks could explain that sign but not the printed raw-score probability labels. Positive theta remains positive at half-unit precision. Ask for actual X/Y coding, probability orientation, ranks and ties; no operational interim statistic is assumed.

### G014 — Unchanged schedule and 300-patient boundary rejection

Members: F-ST1-505. Source-order key: DOC-004:p009:interim-schedule.

Locations: PLAN [trial SAP p.9 schedule](../../../joi240006supp3_prod_1708623114.99733.pdf#page=9), [p.11 planned counts](../../../joi240006supp3_prod_1708623114.99733.pdf#page=11), [p.12 actual review/no-additional-analysis statements](../../../joi240006supp3_prod_1708623114.99733.pdf#page=12), [p.40 calibrated settings](../../../joi240006supp3_prod_1708623114.99733.pdf#page=40).

Recommend plan_material; primary/all P_P. Route B. Direct sourcep12 says data were provided without altering design or incorporating additional interim analyses, then attributes stopping and null rejection to the prespecified boundary after300 completed outcomes. Planned efficacy looks200/380 and final560 are explicit;300 differs. Disclosure of chronology does not identify the applied inferential rule or its mapping. No alpha violation or unsupported observedZ is asserted. Operational/discretionary review or a permitted boundary mapping is an alternative requiring definition. This changes a planned decision rule, so it is not an administrative chronology comparison.

### G015 — Symptomatic hemorrhage definition/window

Members: F-XS-004. Source-order key: DOC-005:p005:sICH-definition.

Locations: PLAN [analysis SAP p.5](../../../joi240006supp4_prod_1708623115.00733.pdf#page=5), PLAN [trial SAP p.13](../../../joi240006supp3_prod_1708623114.99733.pdf#page=13), [p.18](../../../joi240006supp3_prod_1708623114.99733.pdf#page=18), [p.31](../../../joi240006supp3_prod_1708623114.99733.pdf#page=31); REPORT [main p.3 endpoint](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3), [results p.38 event counts](../../../joi240006supp5_prod_1708623115.01733.pdf#page=38).

Recommend protocol_report; primary P_R; all P_R,P_P. Route B. Specific SAP explicitly prints4-hour window with≥4 NIHSS increase; parent SAPp13 prints24hours and NIHSS increase or death; p18/p31 repeat24hours. Report identifies SITS-MOST and0/168vs2/168 but not an independent window/component rule. Compared PLAN definitions directly conflict; report's named criterion matches the parent definition within supplied evidence and leaves current-plan4hours unaccounted for. Classification ambiguity: P_R rests on the REPORT's named criterion and package-defined meaning, not a separately printed24-hour REPORT qualifier; direct rechecker must retain that distinction. Ask which adjudication definition produced counts. No outside definition is used.

### G016 — Planned mismatch-volume primary outcome strata

Members: F-ST1-305. Source-order key: DOC-005:p006:section5.3.3.

Locations: PLAN [analysis SAP p.6 §5.3.3](../../../joi240006supp4_prod_1708623115.00733.pdf#page=6), [p.4 §5.2.1](../../../joi240006supp4_prod_1708623115.00733.pdf#page=4); REPORT [main p.6 Figure1](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6), [p.8 mismatch results](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=8), [results p.23 eFigure17](../../../joi240006supp5_prod_1708623115.01733.pdf#page=23), [p.43 eTable7](../../../joi240006supp5_prod_1708623115.01733.pdf#page=43); complete counterpart scope DOC-001pp1–14,DOC-006pp1–53,DOC-002pp1–30,DOC-007p1.

Recommend protocol_report; primary/all P_R. Route A, category5. Specific SAP explicitly adds50/100mL mismatch-volume strata and invokes outcome/treatment analyses in§5.2, including primary90-day mRS distribution. Supplied REPORT uses joint1.2/10 and1.8/15 profiles and continuous mismatch volume; core50/100mL cutoffs and plot ticks are different quantities. Current source extraction and complete counterpart-search handoff do not identify the specified categorical primary analyses. Ask where they are supplied or which amendment accounts for replacement/omission; no reporting absence outside this package is asserted.

### G017 — Adverse-outcome forest favors direction

Members: F-NUM-101, F-XS-103, F-ST1-201. Source-order key: DOC-006:p019:eFigure13.

Locations: REPORT [results p.19 eFigure13 all16rows,title,reference,axis labels](../../../joi240006supp5_prod_1708623115.01733.pdf#page=19); [p.15 eFigure9](../../../joi240006supp5_prod_1708623115.01733.pdf#page=15) corroborates direction convention. REPORT [main p.3](../../../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3) corroborates mRS5–6 definition.

Recommend statistical_results; primary/all S_W. Route A, category2. eFigure13 explicitly uses risk of achieving adverse mRS5–6 in EVT compared with MM, yet labels left/below1 as favoringMM and right/above1 as favoringEVT. All16RRs are below1 (.68,.77,.82,.72,.61,.87,.62,.78,.76,.55,.72,.69,.67,.74,.76,.71); maximal upper half-unit .875 remains below1. The affected strata are NCCT and largest/composite core< or≥70/100/150mL and both composite mismatch-profile presence/absence pairs. Direction reversal follows the stated adjusted RR contrast, not replacement with crude risks. Reciprocal reference or desirable-outcome coding is an alternative contradicted by the printed caption, requiring human clarification. One axis pattern, preserving all16rows.

### G018 — Discordant-profile favorable counts and disjoint outcomes

Members: F-NUM-201, F-XS-104. Source-order key: DOC-006:p045:eTable8-matched-counts.

Locations: REPORT [results p.45 eTable8 independence](../../../joi240006supp5_prod_1708623115.01733.pdf#page=45), [p.46 ambulation/adverse](../../../joi240006supp5_prod_1708623115.01733.pdf#page=46), [p.47 eTable9](../../../joi240006supp5_prod_1708623115.01733.pdf#page=47), [p.48 continuation](../../../joi240006supp5_prod_1708623115.01733.pdf#page=48), [p.49 eTable10](../../../joi240006supp5_prod_1708623115.01733.pdf#page=49), [p.50 continuation](../../../joi240006supp5_prod_1708623115.01733.pdf#page=50), [p.31 eFigure20x heading](../../../joi240006supp5_prod_1708623115.01733.pdf#page=31), [p.32 distribution](../../../joi240006supp5_prod_1708623115.01733.pdf#page=32).

Recommend statistical_results; primary/all S_W, superseding F-XS-104's report_internal_inconsistency proposal because the consolidated pattern concerns event counts and proportions. Routes A, category3 (internal disjoint counts), and category2 (CTP/MRI favorable-event arm attribution). Profile2 is ASPECTS6–10/core≥70mL. eTable9MM ambulation3/11 plusadverse10/11 exceeds its population; eTable10MM4/12+11/12 and2/12+11/12 likewise exceed12. Printed percentage sum intervals[118.1,118.3],[124.9,125.1],[108.3,108.5]% versus conservatively allowed100±.5 leave relative gaps.176,.244,.078. eTable8 gives CTP/MRI favorable events EVT1/12 and3/12,MM0/11, whileeTable9 assigns1/11 and3/11 toMM and0/12 toEVT; eFigure20x EVT8%mRS2+17%mRS3 andMMno favorable segments supports the eTable8 direction. EVT8%vs0% gap7/8=.875 and25%vs0% gap24/25=.96; MM0%vs9.1/27.3% remain separated. ITT/as-treated definitions differ generally but identical profile12/11 denominators and only MM→EVT crossovers do not explain this attribution pattern. eTables9/10 MMmedian/IQR6(6,6) add distribution context; no unsupported specific quantile algorithm is needed. Composite arm attribution is not independently inferred from the CTP/MRI copy; its within-display disjoint totals suffice. Ask which arm/population/outcome counts apply; one repeated profile pattern with all locations.

## Screened-out source confirmations

F-ST1-401: independently reread REPORT results pp.43–44 and main p.4. The MM ratio interval[.93,1.79] contains1 and difference interval[.011,.325] excludes0 for all endpoint half-unit allowances; this numerical observation is reproduced. However, the cell labels two distinct adjusted measures, supplies no common risk-pair identity or confidence construction, and prints no same-effect P/statistic (the .83 is heterogeneity). Different confidence intervals on nonlinear scales or conditional/marginal estimands need not give the same null inclusion. Treating that difference alone as a contradictory same-analysis result assumes an unstated mapping; asking only for that mapping is missing-method detail, rather than a reproduced logical contradiction. No routeA1 interval-versus-own-test or routeA4 same-display reproducing method is established. The issue is therefore CONDITIONAL_OR_UNREPORTED, not rounding, despite robust endpoint separation.

F-ST1-503: independently reread PLAN protocolp49 and directly rendered trialSAPp11. Fixed power21.2%vs51.2% has intervals[21.15,21.25]vs[51.15,51.25], gap29.90percentage points and relative29.90/21.2=1.410377. Matching scenario4 effects(.4,.4,.4,.4,−.1,−.1),weighted.1,adaptiveN502/power78.5%,fixedN560 are confirmed. This is simulated operating-characteristic output under an alternative scenario, not an input used to select the primary sample size or an implemented boundary. The maximum560,planned alpha/power inputs,all displayed decision boundaries and observed result remain unchanged. Apply scope comparison tiers first: peripheral plan-internal output comparison. No printed production mechanism establishes a routeA2 digit slip, no interval/test conflict, no counts, and no source-defined reproducing simulation method that reconstructs other rows establishes routeA4. PERIPHERAL_COMPARISON is the sole reason code.

## Independent source-reading and derivative provenance

Engine: direct Poppler26.01.0; computeCPU. No OCR, GPU, Python extraction, or fallback environment used by this agent. Commands were run inside the supplied package; all outputs remain under preprocessing/inclusion_initial.

- `pdftotext -layout jama_sarraj_2024_oi_240006_1708623114.96234.pdf .ai_paper_validation/review_1_6_2/preprocessing/inclusion_initial/main-layout.txt`
- `pdftotext -layout joi240006supp4_prod_1708623115.00733.pdf .ai_paper_validation/review_1_6_2/preprocessing/inclusion_initial/analysis-sap-layout.txt`
- `pdftotext -layout joi240006supp2_prod_1708623114.99233.pdf .ai_paper_validation/review_1_6_2/preprocessing/inclusion_initial/protocol-layout.txt`
- `pdftotext -layout joi240006supp5_prod_1708623115.01733.pdf .ai_paper_validation/review_1_6_2/preprocessing/inclusion_initial/results-layout.txt`
- For each N in9,11,12,13,14,17,18,31,39,40: `pdftoppm -f N -l N -singlefile -scale-to 1800 -png joi240006supp3_prod_1708623114.99733.pdf .ai_paper_validation/review_1_6_2/preprocessing/inclusion_initial/sap-pN`; each sap-pN.png visually read against its exact PDF page.
- For each N in15,32: `pdftoppm -f N -l N -singlefile -scale-to 1800 -png joi240006supp5_prod_1708623115.01733.pdf .ai_paper_validation/review_1_6_2/preprocessing/inclusion_initial/results-pN`; each results-pN.png visually read against its exact PDF page.
- For each N in8,16: `pdftoppm -f N -l N -singlefile -scale-to 1600 -png joi240006supp5_prod_1708623115.01733.pdf .ai_paper_validation/review_1_6_2/preprocessing/inclusion_initial/results-pN`; each results-pN.png visually read against its exact PDF page.

This agent produced 18 direct derivatives: four full-source layout text files and fourteen exact-page PNGs. Additional direct native readings confirmed main pp.1/5 and results p.16; direct rendered flowp.8 confirmed168/168 allocation and170/166 received-treatment counts; rendered p.32 confirmed the eFigure20x category colors, and rendered p.15 confirmed the corroborating adverse-outcome favorable-side convention. TrialSAPp17 directly confirms the secondary functional-independence hierarchy. No decision changed during these final source confirmations.

Additional visually read current-run exact-source derivatives: preprocessing/cross_reports/main-p7.png; supp-13.png; supp-14.png; supp-p19.png; supp-p23.png; supp-p47.png; preprocessing/support_protocol/page-13.png; page-80.png; page-81.png. These images were directly rendered from their named supplied PDFs by current mappers/checkers, with their Poppler/CPU provenance retained in those current artifacts; no historical checker/report was used. Independent page-native readings additionally cover all exact quoted narrative/caption/table cells: mainpp3,4,6,8,9,10,11; analysisSAPpp3–7; protocolpp8,13,16,37,49,50,80,81; resultspp24,25,31,32,38,43–51. Direct scanned trialSAP images provide the quoted definitions/formulas/schedule, not OCR substitution. No numeric transcription discrepancy changed any finding; a minor location extension retains the p.9 continuation of the main mismatch direction sentence.

Limits: missing unrounded limits/effect Ps; raw fit outputs and zero-event estimation rule; core/time model covariate mapping; operative plan amendments; sICH adjudication window/components; rank convention/treatment coding; 300-look boundary mapping; exact fitted graph coordinates. The complete REPORT counterpart absence checks are bounded to the supplied package and retain the complete fresh mapper/checker page coverage as factual absence evidence. These are named definition limits, not uncovered finding locations. Stable classification/evidence states remain for the distinct fresh mechanical rechecker and auditor.

## Independent pass-2 decision and consolidated registration

F-ST2-601: INCLUDE, MEETS_THRESHOLD, C019. Reproduced Route B primary final-rule branch comparison; version/lineage ambiguity and unexecuted-final-stage limits remain explicit. It is distinct from C014's executed 300-outcome interim review. The complete independent source confirmations and alternatives are in inclusion_screen_pass_2.md, and all affected locations are retained in C019.

Cumulative totals: 32 findings screened, 30 INCLUDE findings consolidated into 19 stable candidates, 2 SCREENED_OUT findings (1 CONDITIONAL_OR_UNREPORTED; 1 PERIPHERAL_COMPARISON). Every finding has exactly one decision and every included finding maps to a stable ID. All candidates remain Pending Human Adjudication.
