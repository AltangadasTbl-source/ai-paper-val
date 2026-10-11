## C011 — Historical SELECT intervals at the null and significant P values

**Status:** Pending Human Adjudication

**Candidate statement:** Two historical SELECT associations in the protocol pair 95% odds-ratio intervals with printed lower limits of 1.00 and P values below .05.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol p.13 historical rationale

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-501

**Qualifying route:** Route A, category 1

**Classification rationale:** Both paired interval/P comparisons occur solely in historical rationale within the prospective protocol, classified as PLAN by content. P_P therefore maps to plan_material; no current REPORT estimate is a conflicting side.

**Classification ambiguity:** These are historical rationale, whereas plan_material ordinarily describes prospective design. The independent screen and audit retain the reproduced interval/test conflicts under the explicit always-register category 1, which takes precedence over peripheral historical context. They are not observed SELECT2 treatment effects.

**Exact source locations:** PLAN [protocol — PDF p.13, historical SELECT functional-independence and ordinal-shift results](<../joi240006supp2_prod_1708623114.99233.pdf#page=13>).

**Source evidence:** The protocol prints adjusted OR 2.92 (95% CI 1.00–7.91), P = .041 for functional independence and adjusted OR 2.01 (95% CI 1.00–4.03), P = .049 for ordinal shift. The latter is described as a significant shift.

**Reported-versus-comparator:** Each printed 95% interval includes the ratio null 1.00, while its own paired P is below the conventional .05 level. These are two occurrences of one interval/test pattern, not a combination of distinct estimates.

**Reasoning procedure:** Match each historical estimate to its own interval and P, retain the stated 95% confidence level, and compare null inclusion with significance at .05. Do not infer a Wald construction or substitute a crude association.

**Calculation:** Both printed lower endpoints equal the null 1.00. Their half-unit intervals are [0.995, 1.005]; the P intervals are [.0405, .0415] and [.0485, .0495], each wholly below .05. An unrounded lower bound above 1 is possible. Under category 1, that possibility is preserved for adjudication rather than screened out as rounding.

**Affected result or extracted value:** The historical SELECT functional-independence and ordinal-shift adjusted OR/95% CI/P pairings printed in the supplied protocol.

**Why context does not resolve it:** Route A, category 1 always registers a reproduced interval-versus-own-P/test conflict. Hidden precision or different inferential constructions do not remove this category.

**Alternative source-grounded interpretations:** Unrounded lower limits could exceed 1, or the confidence intervals and P values could use different constructions. The package does not supply the unrounded limits, variance outputs, test/interval methods, or historical analysis mapping. These possibilities do not establish which pairing was intended.

**Mechanical evidence recheck:** The independent rechecker found and visually confirmed the exact protocol page, both source estimates, limits and paired P values; the auditor independently reread the page. The printed-null comparison was reproduced without transcription correction. No current SELECT2 effect, raw data, or operational trial decision was inferred.

**Potential downstream evidence impact:** A data extractor using the protocol's historical rationale could copy an interval including 1 alongside a statistically significant P. Any relevance is limited to those historical associations; no change to the current trial's treatment conclusion is established.

## C012 — Historical safety significance statement includes P = .072

**Status:** Pending Human Adjudication

**Candidate statement:** A historical safety paragraph includes symptomatic intracranial hemorrhage with P = .072 among outcomes described as significantly increased.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol p.16 historical safety rationale

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-506

**Qualifying route:** Route A, category 1

**Classification rationale:** The printed test and accompanying significance statement are both historical PLAN content in one protocol. P_P and plan_material preserve that document role; current-trial REPORT safety results are not compared.

**Classification ambiguity:** Historical rationale ordinarily falls in the peripheral comparison tier. The screen and audit apply the explicit always-register test-conflict category 1. This is a historical safety characterization, not an observed SELECT2 safety effect.

**Exact source locations:** PLAN [protocol — PDF p.16, historical safety paragraph](<../joi240006supp2_prod_1708623114.99233.pdf#page=16>).

**Source evidence:** The paragraph lists symptomatic intracranial hemorrhage 8/173 (5%) versus 3/18 (17%), P = .072; neurological worsening 14/173 versus 5/18, P = .023; and mortality 15/173 versus 7/18, P = .001. Its plural sentence describes these safety outcomes as significantly increased with larger core.

**Reported-versus-comparator:** The sICH comparison's own P = .072 is above .05, although the grammatical significance statement includes the listed sICH outcome. The other two P values remain context, not substitutes for the sICH test.

**Reasoning procedure:** Read the complete list and its collective sentence together, associate each P with its own outcome, and compare the sICH test with the stated significant-increase characterization at the conventional .05 threshold. Check the counts separately without creating another finding.

**Calculation:** The P rounding interval [.0715, .0725] lies wholly above .05. The counts reconcile with their integer percentages: 8/173 = 4.624% rounds to 5%, and 3/18 = 16.667% rounds to 17%. The registered comparison is the significance statement, not a count discrepancy.

**Affected result or extracted value:** The historical protocol's sICH significance characterization for 8/173 versus 3/18.

**Why context does not resolve it:** Route A, category 1 applies to the reproduced own-test versus statistical-significance statement; display precision and historical context do not remove that category.

**Alternative source-grounded interpretations:** The sentence might use clinical significance, or collectively refer only to the statistically supported outcomes. No collective safety test, special significance threshold, or explicit exclusion of sICH from the significance description is supplied. The intended collective meaning remains unresolved.

**Mechanical evidence recheck:** Exact-source native reading confirmed the counts, each P, and the plural sentence. The applicable test/significance comparison and P precision interval were reproduced without transcription correction; the auditor retained the historical role and category-1 precedence. No individual event assignment or current safety effect was inferred.

**Potential downstream evidence impact:** An extractor using historical protocol rationale could copy a statistically significant sICH characterization alongside P = .072. This does not establish any change in current SELECT2 safety results or overall conclusions.

## C013 — Planned efficacy probability has the opposite treatment-score orientation

**Status:** Pending Human Adjudication

**Candidate statement:** The planned positive alternative P(MM score ≤ EVT score) = .5 + .0791 points toward lower disability in MM, while the plan names the corresponding direction EVT efficacy.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol pp.37,80–81 vs PLAN trial SAP pp.39–40; REPORT main p.3 corroborates score direction

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-XS-006, F-ST1-504

**Qualifying route:** Route A, category 2

**Classification rationale:** The conflicting score definitions, alternative and efficacy orientation are all PLAN material. The main article only corroborates score direction, so P_P alone and plan_material apply; corroboration does not add P_R.

**Classification ambiguity:** Operational score coding, X/Y labels, rank orientation and tie conventions are unavailable. Descending ranks could explain the sign of a rank-sum statistic, but do not themselves reconcile the explicitly labeled raw-score probability.

**Exact source locations:** PLAN [protocol — PDF p.37, lower-score benefit](<../joi240006supp2_prod_1708623114.99233.pdf#page=37>), [p.80, statistic and efficacy rule](<../joi240006supp2_prod_1708623114.99233.pdf#page=80>), [p.81, alternative and variable labels](<../joi240006supp2_prod_1708623114.99233.pdf#page=81>); PLAN [trial SAP — PDF p.39, repeated statistic](<../joi240006supp3_prod_1708623114.99733.pdf#page=39>), [p.40, alternative and bounds](<../joi240006supp3_prod_1708623114.99733.pdf#page=40>). REPORT [main article — PDF p.3, mRS direction](<../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3>) corroborates only.

**Source evidence:** The protocol describes improvement as decreasing mRS. Both appendices define Y as the MM Rankin score and X as the EVT Rankin score and print H_A: P(Y ≤ X) = 1/2 + theta, theta = .0791. W is the sum of EVT-group Rankin ranks; positive standardized boundaries are named EVT efficacy, with b = 2.604 and c = 2.772. The main article defines mRS 0 as no residual symptoms and 6 as death.

**Reported-versus-comparator:** The literal positive alternative increases the probability that MM disability is no greater than EVT disability, while the named benefit is for EVT. The raw-score labels establish this contrast independently of an assumed ascending-rank convention.

**Reasoning procedure:** Substitute the printed treatment labels into the stated probability and use the supplied lower-score benefit definition. Keep the W-based direction as supporting context that needs a rank convention; do not infer an executed statistic.

**Calculation:** The printed alternative is .5 + .0791 = .5791 for MM score ≤ EVT score. Theta's half-unit interval [.07905, .07915] remains positive. An illustrative EVT score 0/MM score 6 pair has clear EVT benefit but makes MM ≤ EVT false; this checks direction only and is not an observed participant pair. No observed Z or alpha consequence is calculated.

**Affected result or extracted value:** The planned treatment orientation of the primary efficacy alternative and its associated boundary specification.

**Why context does not resolve it:** Route A, category 2 applies to the explicit treatment-score direction reversal. A possibly different rank convention does not remove the printed raw-score labeling conflict.

**Alternative source-grounded interpretations:** Descending ranks may explain a positive EVT rank-sum boundary; recoded scores or reversed X/Y labels could explain the probability. Actual operational coding, probability orientation, rank order, tie treatment and observed interim statistics are missing. None of these possible mechanisms is established by the package.

**Mechanical evidence recheck:** The independent rechecker visually confirmed both appendices, the protocol score-direction statement and the corroborating REPORT definition. All repeated labels and signs match the registration; the literal probability-direction comparison was reproduced without transcription correction. The auditor retained one consolidated PLAN pattern.

**Potential downstream evidence impact:** A reviewer extracting the statistical design could copy a treatment-benefit orientation that differs from the stated score direction. No executed decision reversal, treatment-effect replacement, or changed operating characteristic is established.

## C014 — Retained interim schedule does not identify the 300-outcome rejection rule

**Status:** Pending Human Adjudication

**Candidate statement:** The SAP retains efficacy looks at 200 and 380 completed outcomes and says no additional analysis or design alteration occurred, yet describes boundary-based null rejection after 300 outcomes without identifying the inferential mapping.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN trial SAP pp.9,11–12,40

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-505

**Qualifying route:** Route B

**Classification rationale:** All compared schedule, calibration and chronology statements are in the operational trial SAP, classified as PLAN by content. The conflict concerns a primary statistical decision rule, so P_P and plan_material apply even where the SAP recounts trial chronology.

**Classification ambiguity:** The disclosed 300-outcome review may have used a permitted operational or information-time mapping. Its exact boundary and information fraction are not supplied. The candidate does not establish an additional formal test or altered alpha.

**Exact source locations:** PLAN [trial SAP — PDF p.9, §7.2 planned looks](<../joi240006supp3_prod_1708623114.99733.pdf#page=9>), [p.11, planned sample counts](<../joi240006supp3_prod_1708623114.99733.pdf#page=11>), [p.12, §7.5 300-outcome review and unchanged-design statements](<../joi240006supp3_prod_1708623114.99733.pdf#page=12>), [p.40, calibrated settings](<../joi240006supp3_prod_1708623114.99733.pdf#page=40>).

**Source evidence:** The planned efficacy looks are after completed 90-day follow-up in 200 and 380 patients, with maximum 560. Appendix settings repeat these counts and bounds b = 2.604/c = 2.772. Section 7.5 discloses the first 200-outcome review, a requested review after 300 completed outcomes supplied without altering design or adding interim analyses, and null rejection/early stopping attributed to crossing the prespecified efficacy boundary after examining 300 outcomes.

**Reported-versus-comparator:** The printed 300-outcome boundary-based rejection is not identified with either planned 200/380 look while the design and analysis schedule are described as unchanged. Chronology is disclosed, but the inferential mapping is not.

**Reasoning procedure:** Match planned completed-outcome counts and calibrated settings with the disclosed efficacy decision. Separate a primary boundary-rule comparison from administrative review dates; name the absent mapping without assuming an unscheduled formal test.

**Calculation:** Conservative half-unit count intervals [299.5, 300.5] versus [379.5, 380.5] leave gap 79 and relative discrepancy 79/380 = .20789; versus [199.5, 200.5], gap 99 gives 99/200 = .495. Thus 300 is not a display-rounding version of either look. These count diagnostics support the discrete decision-rule question; no observed Z or recalculated alpha is available.

**Affected result or extracted value:** The primary early-stopping rule and information time attached to the disclosed 300-outcome null rejection.

**Why context does not resolve it:** Route B: a planned primary stopping rule is in focus; simultaneous unchanged-schedule and boundary-rejection statements lack an immediate information-time/boundary mapping; that mapping bears on extracting the primary efficacy decision specification.

**Alternative source-grounded interpretations:** The review might have been discretionary or operational with a permissible scheduled-boundary mapping; broader available follow-up could correspond to another information time. The actual information fraction, statistic, applied bound, permissible unscheduled-look rule and amendment are unavailable. None is adopted as an observed explanation.

**Mechanical evidence recheck:** Exact-source page reading confirmed every scheduled count, calibration value and §7.5 statement. The numerical separation and unresolved logical mapping were reproduced without transcription correction. The auditor retained Route B and distinguished this executed interim-review mapping from C019's unexecuted final branch.

**Potential downstream evidence impact:** A systematic reviewer could extract the retained 200/380 schedule or the disclosed 300-outcome efficacy rule without a common mapping. No alpha violation, changed treatment estimate, or actual downstream propagation is established.

## C015 — PLAN sICH window and death component differ

**Status:** Pending Human Adjudication

**Candidate statement:** The analysis-specific SAP defines sICH using a 4-hour NIHSS window, while the trial SAP specifies 24-hour ascertainment and includes death; the definition governing the reported safety counts is not identified.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN analysis-specific SAP p.5 vs PLAN trial SAP pp.13,18,31; REPORT main p.3 and results supplement p.38 establish relevance and corroborate only

**Evidence state:** reproduced

**Inclusion audit:** QUESTIONED
The printed PLAN-only four/24-hour and death-component discrepancy is reproduced, but the assigned Route B does not establish B1 under the restricted plan-internal comparison tier: sICH is a non-key secondary safety endpoint in the supplied main article/SAP, with no source-supported change to a primary/key secondary result, analysis-population size, or planned primary decision rule. No always-register status/composite change or interval/test conflict is reproduced. The stable ID remains, with its exact evidence, for human adjudication.

**Finding IDs:** F-XS-004

**Qualifying route:** Route B

**Classification rationale:** The directly conflicting endpoint definitions are PLAN versus PLAN. REPORT names SITS-MOST and gives counts without independently specifying a time window or death component; those pages establish relevance and corroborate only. P_P alone and plan_material are the final classification.

**Classification ambiguity:** A later analysis-specific definition could intentionally revise the parent plan, or the reported named criterion could follow the parent plan. The operative definition/amendment is not identified. The independent inclusion audit questions scope because this is a PLAN-only non-key secondary safety comparison.

**Exact source locations:** PLAN [analysis-specific SAP — PDF p.5, §5.2.5](<../joi240006supp4_prod_1708623115.00733.pdf#page=5>); PLAN [trial SAP — PDF p.13, secondary endpoints](<../joi240006supp3_prod_1708623114.99733.pdf#page=13>), [p.18, §10.2.3.4.1](<../joi240006supp3_prod_1708623114.99733.pdf#page=18>), [p.31, template footnote](<../joi240006supp3_prod_1708623114.99733.pdf#page=31>). REPORT [main article — PDF p.3, endpoint name](<../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3>) and [results supplement — PDF p.38, eTable2 counts](<../joi240006supp5_prod_1708623115.01733.pdf#page=38>) establish relevance and corroborate only.

**Source evidence:** The specific SAP prints parenchymal hemorrhage type II/remote parenchymal hemorrhage with ≥4 NIHSS increase at 4-hour follow-up, with number/proportion reporting because events are few. The trial SAP p.13 names SITS-MOST with ≥4 NIHSS increase or death within 24 hours; pp.18/31 repeat 24-hour context. REPORT names SITS-MOST and prints 0/168 versus 2/168, but does not independently print a 4/24-hour or death-component rule.

**Reported-versus-comparator:** The PLAN definitions differ in ascertainment window and death inclusion. The reported counts are relevant to that definition but do not establish which rule was used. Their count/percentage display separately reconciles; no patient-level event discrepancy is claimed.

**Reasoning procedure:** Compare the directly printed PLAN definitions, preserve REPORT relevance without importing an outside definition into its named criterion, and distinguish source reproduction from whether the restricted comparison tier supports inclusion.

**Calculation:** Conservative window intervals [3.5, 4.5] and [23.5, 24.5] hours leave gap 19 hours, relative to 4 hours 19/4 = 4.75. Exact specified windows are definitions rather than rounded measurements. Death inclusion is categorical. No event reclassification or replacement count can be calculated.

**Affected result or extracted value:** The endpoint definition attached to the non-key secondary sICH counts 0/168 and 2/168.

**Why context does not resolve it:** The initial Route B screen identified competing PLAN definitions without an operative mapping to counts. The independent audit questions B1 under the restricted PLAN-only comparison tier because no source-supported primary/key secondary result, population-size or primary decision-rule change is established; the scope question remains explicit.

**Alternative source-grounded interpretations:** The specific SAP may intentionally revise the definition, or the reported named criterion may follow the parent plan. The actual ascertainment window, death inclusion, event roster and governing amendment are absent. No external SITS-MOST definition is used, and neither alternative establishes individual misclassification.

**Mechanical evidence recheck:** The rechecker confirmed all six cited pages and reproduced the PLAN-only window/component discrepancy. It corrected the relationship/domain to P_P/plan_material because REPORT has no independently conflicting window. That classification change does not change transcription or the reproduced evidence state. The auditor questioned inclusion, while retaining the stable ID and evidence.

**Potential downstream evidence impact:** If the candidate is confirmed within scope, an extractor could attach differing ascertainment definitions to the reported sICH counts. No effect on individual event classification, a primary result, or current-trial conclusions is established.

## C016 — Planned mismatch-volume primary strata have no supplied counterpart

**Status:** Pending Human Adjudication

**Candidate statement:** The SAP specifies 50/100-mL mismatch-volume strata for primary 90-day mRS analyses, but complete supplied REPORT coverage contains distinct joint-profile or continuous analyses without an identifiable categorical counterpart.

**Review domain:** protocol_report

**Relationship type:** P_R

**All relationships:** P_R

**Compared document roles:** PLAN analysis-specific SAP pp.4,6 vs complete supplied REPORT counterpart scope

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST1-305

**Qualifying route:** Route A, category 5

**Classification rationale:** The comparison is an explicit PLAN analysis specification versus its bounded absence or distinct analyses in REPORT materials. P_R therefore maps to protocol_report. Mentioning the same numbers as core cutoffs or graph ticks does not create a matching analysis.

**Classification ambiguity:** The planned results could exist outside the supplied package or could have been intentionally replaced by continuous analyses. No governing amendment or omission explanation is supplied; the absence statement is limited to the package.

**Exact source locations:** PLAN [analysis-specific SAP — PDF p.6, §5.3.3](<../joi240006supp4_prod_1708623115.00733.pdf#page=6>), [p.4, §5.2.1 primary endpoint](<../joi240006supp4_prod_1708623115.00733.pdf#page=4>). Identified REPORT comparisons: [main article — PDF p.6, Figure1](<../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=6>), [p.8, mismatch results](<../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=8>), [results supplement — PDF p.23, eFigure17](<../joi240006supp5_prod_1708623115.01733.pdf#page=23>), [p.43, eTable7](<../joi240006supp5_prod_1708623115.01733.pdf#page=43>). Complete counterpart scope: [main article, PDF pp.1–14; entry p.1](<../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=1>), [results supplement, PDF pp.1–53; entry p.1](<../joi240006supp5_prod_1708623115.01733.pdf#page=1>), [contributors, PDF pp.1–30; entry p.1](<../joi240006supp1_prod_1708623114.97236.pdf#page=1>), and [data sharing, PDF p.1](<../joi240006supp6_prod_1708623115.02733.pdf#page=1>).

**Source evidence:** SAP §5.3.3 adds mismatch-volume 50/100-mL strata and invokes outcome/treatment analyses in §5.2, whose §5.2.1 includes the primary 90-day mRS distribution. Identified REPORT displays instead use joint ratio/volume profiles 1.2/10 and 1.8/15 or continuous mismatch volume.

**Reported-versus-comparator:** The specified categorical primary mismatch-volume analyses have no identifiable result within the complete supplied REPORT counterpart scope. Core-volume 50/100-mL thresholds and continuous plot ticks represent different quantities or analysis forms.

**Reasoning procedure:** Follow the explicit SAP cross-reference to the primary endpoint, then compare it with complete REPORT page/figure/table mapping and source searches. Require matching quantity, categorization and endpoint; do not count numerically similar thresholds as counterparts.

**Calculation:** This is an analysis-presence and specification comparison, not a numerical estimate discrepancy. Half-unit intervals and a relative rounding gap are not applicable. No missing categorical treatment effect is invented or recomputed.

**Affected result or extracted value:** Reporting/extraction status of the prespecified primary mRS analyses in mismatch-volume 50/100-mL strata.

**Why context does not resolve it:** Route A, category 5 always registers a planned primary analysis not reported in the complete supplied counterpart scope. Distinct joint-profile and continuous analyses do not provide that categorical primary counterpart.

**Alternative source-grounded interpretations:** The categorical results may be available outside this package, or an operative amendment may have replaced them. Neither is established here. The planned categorical estimates and a governing replacement/omission explanation are the missing inputs.

**Mechanical evidence recheck:** The rechecker confirmed both SAP pages and the identified REPORT displays, with complete bounded REPORT mapping/search covering 14 + 53 + 30 + 1 pages. No matching categorical primary counterpart was found. Source reproduction and P_R classification were retained without transcription correction; no external absence was asserted.

**Potential downstream evidence impact:** An evidence reviewer could record the specified categorical primary analysis as available or prespecified without finding its extractable results, or substitute a different analysis. No omitted effect estimate or direction is inferred.

## C017 — Adverse-outcome forest favors labels reverse its printed contrast

**Status:** Pending Human Adjudication

**Candidate statement:** eFigure13 defines adverse mRS 5–6 risk in EVT compared with MM, yet its below-one axis side is labeled favors MM despite all 16 printed ratios being below 1.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement p.19; REPORT results p.15 and main p.3 corroborate adverse-outcome direction

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-101, F-XS-103, F-ST1-201

**Qualifying route:** Route A, category 2

**Classification rationale:** The title, reference, ratios and shared favors labels conflict within one REPORT results supplement. S_W and statistical_results apply; other REPORT pages corroborate the outcome direction without adding a conflicting S_C relationship.

**Classification ambiguity:** None in document-role assignment. Reciprocal reference or favorable-outcome coding could explain the plot labels, but would conflict with its printed adverse-outcome title and EVT/MM contrast.

**Exact source locations:** REPORT [results supplement — PDF p.19, eFigure13 title, contrast, axis labels and all 16 rows](<../joi240006supp5_prod_1708623115.01733.pdf#page=19>); REPORT [results supplement — PDF p.15, eFigure9 direction convention](<../joi240006supp5_prod_1708623115.01733.pdf#page=15>) and [main article — PDF p.3, mRS 5–6 definition](<../jama_sarraj_2024_oi_240006_1708623114.96234.pdf#page=3>) corroborate only.

**Source evidence:** The title names complete dependence or death (mRS 5–6), and the axis caption defines risk ratio in thrombectomy compared with medical management. The below-one left side says favors MM and the above-one right side says favors EVT. Every affected printed estimate is preserved below.

| Printed stratum | RR |
|---|---:|
| NCCT <70 mL | .68 |
| NCCT ≥70 mL | .77 |
| Largest/composite <70 mL | .82 |
| Largest/composite ≥70 mL | .72 |
| NCCT <100 mL | .61 |
| NCCT ≥100 mL | .87 |
| Largest/composite <100 mL | .62 |
| Largest/composite ≥100 mL | .78 |
| NCCT <150 mL | .76 |
| NCCT ≥150 mL | .55 |
| Largest/composite <150 mL | .72 |
| Largest/composite ≥150 mL | .69 |
| Composite mismatch 1.2/10 absent | .67 |
| Composite mismatch 1.2/10 present | .74 |
| Composite mismatch 1.8/15 absent | .76 |
| Composite mismatch 1.8/15 present | .71 |

**Reported-versus-comparator:** A below-one risk ratio for an undesirable outcome in EVT/MM means lower adverse risk in EVT, opposite the shared below-one favors-MM label. eFigure9 uses the same adverse contrast with a reconciling left-side favors-EVT label.

**Reasoning procedure:** Use the explicitly named adverse endpoint and treatment reference to determine ratio direction, then compare that reading with the favors labels for every stratum. Retain the adjusted estimates; do not substitute crude ratios or infer statistical significance from direction.

**Calculation:** All 16 point estimates remain below 1 allowing their .005 half-unit precision intervals; the largest possible upper endpoint is .875. The direction comparison does not depend on whether a confidence interval crosses 1. This is a qualitative reference/direction reversal, not a numeric rounding gap.

**Affected result or extracted value:** The treatment-favors reading of all 16 adjusted adverse-outcome risk ratios in eFigure13.

**Why context does not resolve it:** Route A, category 2 applies to the explicit direction/reference statement reversing printed values. A reconstructable intended favors label does not remove this category.

**Alternative source-grounded interpretations:** A reciprocal MM/EVT contrast or desirable-outcome coding could explain the labels, but each differs from the printed caption/title. Original effect coding and plot-generation labels are missing. No production mechanism or replacement ratio is established.

**Mechanical evidence recheck:** The independent rechecker directly viewed eFigure13 and individually confirmed all 16 rows, title, contrast and labels, plus corroborating eFigure9 and main endpoint definition. The direction conflict reproduced without transcription correction; the auditor retained one shared-axis pattern.

**Potential downstream evidence impact:** A data extractor or forest-plot reader could copy a treatment-favors direction opposite the printed adverse-outcome contrast. No reversal of trial efficacy conclusions or actual downstream propagation is established.

## C018 — Discordant-profile counts exceed disjoint totals and change arm attribution

**Status:** Pending Human Adjudication

**Candidate statement:** For discordant profile 2, MM favorable and adverse mRS counts exceed their own population totals in eTables9/10; matched CTP/MRI favorable counts also appear under competing treatment arms across eTables8/9.

**Review domain:** statistical_results

**Relationship type:** S_W

**All relationships:** S_W

**Compared document roles:** REPORT results supplement pp.45–50; REPORT results pp.31–32 corroborate category allocation

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-NUM-201, F-XS-104

**Qualifying route:** Route A, category 3

**Classification rationale:** All conflicting counts, proportions and arm headings are within one REPORT results supplement. The consolidated pattern concerns numerical event counts and proportions, so S_W and statistical_results apply. Figure20x corroborates category allocation without adding another relationship.

**Classification ambiguity:** Actual participant-level membership, outcome attribution and exact as-treated/ITT matching are unavailable. Composite favorable-arm transfer is not inferred from the CTP/MRI comparison; its independent within-display disjoint totals suffice.

**Exact source locations:** REPORT [results supplement — PDF p.45, eTable8 independence](<../joi240006supp5_prod_1708623115.01733.pdf#page=45>), [p.46, eTable8 ambulation/adverse outcomes](<../joi240006supp5_prod_1708623115.01733.pdf#page=46>), [p.47, eTable9 favorable outcomes](<../joi240006supp5_prod_1708623115.01733.pdf#page=47>), [p.48, eTable9 adverse outcomes](<../joi240006supp5_prod_1708623115.01733.pdf#page=48>), [p.49, eTable10 favorable outcomes](<../joi240006supp5_prod_1708623115.01733.pdf#page=49>), [p.50, eTable10 adverse outcomes](<../joi240006supp5_prod_1708623115.01733.pdf#page=50>), [p.31, eFigure20x profile heading](<../joi240006supp5_prod_1708623115.01733.pdf#page=31>), and [p.32, eFigure20x distribution](<../joi240006supp5_prod_1708623115.01733.pdf#page=32>).

**Source evidence:** Profile 2 is ASPECTS 6–10/core ≥70 mL. eTable8 CTP/MRI prints independence EVT 1/12 (8%), MM 0/11; ambulation EVT 3/12 (25%), MM 0/11; adverse mRS 5–6 EVT 8/12 (67%), MM 10/11 (91%). eTable9 prints independence MM 1/11 (9.1%), EVT 0/12; ambulation MM 3/11 (27.3%), EVT 0/12; adverse MM 10/11 (90.9%), EVT 8/12 (66.7%). eTable10 composite profile prints MM independence 2/12 (16.7%), ambulation 4/12 (33.3%), adverse 11/12 (91.7%); EVT favorable outcomes are 0/14 and adverse 9/14 (64.3%). Figure20x shows EVT n = 12, 8% mRS 2 and 17% mRS 3; MM n = 11 has no favorable segment and 9/9/82% in mRS 4/5/6.

**Reported-versus-comparator:** Within eTable9 MM, ambulation and adverse outcomes sum to 13 events out of 11. Within eTable10 MM, ambulation/adverse sum to 15/12 and independence/adverse to 13/12. These outcomes are disjoint. Across eTables8/9, the CTP/MRI favorable events move from EVT to MM despite unchanged 12/11 arm denominators; Figure20x corroborates eTable8's direction.

**Reasoning procedure:** Apply the supplied disjoint mRS cutoffs within each display before considering cross-location attribution. Then match CTP/MRI profile definition, denominators, column labels and favorable counts across tables and the distribution. Preserve all three within-display comparisons and the additional attribution pattern without selecting replacements.

**Calculation:** Exact admissible integer counts give 3 + 10 = 13 >11, 4 + 11 = 15 >12, and 2 + 11 = 13 >12. Printed percentage sum intervals are [118.1, 118.3]%, [124.9, 125.1]% and [108.3, 108.5]%; against a conservatively allowed 100 ± .5%, minimum gaps 17.6, 24.4 and 7.8 percentage points give relative discrepancies .176, .244 and .078, all >.05. For EVT 8% versus 0%, intervals [7.5, 8.5]/[0, .5] give gap 7 and 7/8 = .875; 25% versus 0% gives gap 24 and 24/25 = .96. MM 0% versus 9.1/27.3% has strictly positive gaps against the printed zero. Figure20x's 8% + 17% = 25% supports the EVT favorable direction.

**Affected result or extracted value:** Discordant-profile-2 favorable/adverse event counts, proportions and arm attribution in the CTP/MRI and composite displays.

**Why context does not resolve it:** Route A, category 3 independently qualifies the reproduced within-display disjoint totals. The competing CTP/MRI favorable-arm attribution also meets category 2. General analysis-population context does not remove either reproduced numerical pattern.

**Alternative source-grounded interpretations:** The package discloses ITT/as-treated distinctions, but equal CTP/MRI 12/11 denominators and only MM-to-EVT crossovers do not explain the printed transfer or impossible within-display totals. A row/column attribution issue is possible, not established. MM median/IQR 6 (6, 6) is distribution context; no specific quantile algorithm is assumed. Participant-level rosters and source-production alignment are missing.

**Mechanical evidence recheck:** The independent rechecker confirmed all eight pages, each count/denominator/percentage, treatment heading, profile definition and distribution segment. All three disjoint comparisons and the CTP/MRI attribution pattern reproduced beyond display precision without transcription correction. The auditor retained one consolidated pattern and did not infer composite arm transfer or replacement values.

**Potential downstream evidence impact:** An evidence extractor could copy differing favorable-event counts or arm assignments, or numerators that cannot jointly belong to the printed population. No patient-level cause, completed downstream propagation, or whole-paper conclusion change is established.

## C019 — Final overall efficacy failure has competing rescue and terminal branches

**Status:** Pending Human Adjudication

**Candidate statement:** For final testing after continued overall enrollment, the protocol permits selecting/testing a subgroup after overall efficacy failure, while the later SAP states no superiority upon failed final testing without an explicit subsequent rescue branch.

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol p.48 versus PLAN trial SAP p.10; PLAN protocol pp.1,45,46,47,49,81 and PLAN trial SAP pp.2,9,12,40 provide design, lineage and applicability context.

**Evidence state:** reproduced

**Inclusion audit:** CONFIRMED

**Finding IDs:** F-ST2-601

**Qualifying route:** Route B

**Classification rationale:** The conflicting prospective primary decision trees are both PLAN content. All contextual design, lineage and chronology pages are also used as PLAN context. P_P and plan_material apply; relevance to a reported adaptive framework does not create a REPORT conflict.

**Classification ambiguity:** The later approved SAP may intentionally supersede the protocol or summarize selection/testing concisely. The supported connection is extraction of the primary adaptive framework; this final branch was not reached in the disclosed early-stop chronology. No observed final inferential consequence follows.

**Exact source locations:** Principal PLAN comparison: [protocol — PDF p.48, final scenario 1 items 2/2.1/2.2](<../joi240006supp2_prod_1708623114.99233.pdf#page=48>) versus [trial SAP — PDF p.10, final paragraph and conclusions](<../joi240006supp3_prod_1708623114.99733.pdf#page=10>). PLAN context: [protocol p.1, August 4, 2021 date](<../joi240006supp2_prod_1708623114.99233.pdf#page=1>), [p.45, primary analysis/selection](<../joi240006supp2_prod_1708623114.99233.pdf#page=45>), [p.46, schedule/bounds](<../joi240006supp2_prod_1708623114.99233.pdf#page=46>), [p.47, enrollment scenarios](<../joi240006supp2_prod_1708623114.99233.pdf#page=47>), [p.49, simulation context](<../joi240006supp2_prod_1708623114.99233.pdf#page=49>), [p.81, final appendix rule](<../joi240006supp2_prod_1708623114.99233.pdf#page=81>); [trial SAP p.2, November 20, 2022 v1.0.0 approval](<../joi240006supp3_prod_1708623114.99733.pdf#page=2>), [p.9, retained final-selection language](<../joi240006supp3_prod_1708623114.99733.pdf#page=9>), [p.12, early-stop chronology](<../joi240006supp3_prod_1708623114.99733.pdf#page=12>), [p.40, final appendix threshold](<../joi240006supp3_prod_1708623114.99733.pdf#page=40>).

**Source evidence:** Protocol p.48 directs selection/testing of an optimal subgroup after failure to cross the final overall efficacy bound; subgroup crossing allows subgroup efficacy and non-crossing gives no benefit. SAP p.10 tests the population corresponding to overall or subgroup enrollment, then states efficacy on crossing and no superiority on failure. SAP p.9 still describes selecting the most promising of five cumulative subgroups at interim or final analysis. Both plans specify primary 90-day mRS, interim looks 200/380, maximum 560 and appendix final threshold c = 2.772. The protocol is dated August 4, 2021; SAP v1.0.0 is dated November 20, 2022 and says approval preceded data lock. SAP p.12 discloses early stopping after the 300-outcome review, so the final branch was unexecuted.

**Reported-versus-comparator:** Hold final stage, continued overall-population enrollment and failure of the overall efficacy test fixed. The protocol explicitly proceeds to a newly selected subgroup test with possible subgroup efficacy; the SAP's numbered consequence is no superiority, without an explicit further rescue step. Its retained final-selection wording makes the operative branch unclear.

| Held condition/consequence | Protocol p.48 | Trial SAP p.10 |
|---|---|---|
| Final stage after overall enrollment | Test overall population | Test overall population |
| Overall bound not crossed | Select/test optimal subgroup | Declare no superiority |
| Newly selected subgroup crosses | Subgroup efficacy permitted | No further rescue branch stated |
| Newly selected subgroup does not cross | No benefit | Failed-final-test conclusion already terminal |

**Reasoning procedure:** Compare explicit branch consequences under the same enrollment scenario; use selection language, common appendices, version dates and chronology to evaluate alternatives. Distinguish an unexecuted final specification from C014's executed 300-outcome interim mapping. Do not construct an observed subgroup test or infer operating characteristics.

**Calculation:** A categorical branch/conclusion comparison has no half-unit relative discrepancy. The common numeric threshold 2.772 has the identical interval [2.7715, 2.7725] in both appendices, gap 0 and relative discrepancy 0; it reconciles and is not the finding. No final Z, P, attained 560-patient sample, subgroup effect or alpha consequence is available or fabricated.

**Affected result or extracted value:** The final primary adaptive rejection tree: whether overall final efficacy failure still permits a newly selected subgroup efficacy declaration.

**Why context does not resolve it:** Route B: a primary planned decision rule is expressly in focus; the explicit rescue versus terminal descriptions, together with retained final-selection language, lack an immediate operative reconciliation; the permitted final efficacy conclusion changes how the planned primary decision tree is extracted. Unexecuted status bounds observed-result relevance.

**Alternative source-grounded interpretations:** The later approved SAP may intentionally replace the rescue branch, or its concise testing paragraph may incorporate subgroup selection before its terminal conclusion. Both appendices may summarize only overall rejection and leave subgroup logic elsewhere. Dates and approval support possible supersession but do not identify this branch change. The unchanged-design statement on p.12 concerns the 300-outcome review and does not prove no amendment ever occurred. An operative amendment, mapping of p.9 selection to p.10 failure, and final rescue implementation/calibration are unavailable.

**Mechanical evidence recheck:** A fresh appended-ID rechecker confirmed all 12 distinct pages, visually checking principal rules and key appendices/selection/chronology pages and directly reading the surrounding protocol text. Every registered statement matched without transcription correction. The fixed-condition branch comparison reproduced, all PLAN roles were confirmed, and the auditor retained Route B with version and unexecuted-stage limitations.

**Potential downstream evidence impact:** A reviewer extracting the adaptive design could copy a final primary rejection tree that either permits subgroup rescue or terminates at overall failure. The branch was unexecuted in the disclosed chronology; no changed early-stop treatment estimate, final observed decision, alpha inflation, or actual downstream consequence is established.


