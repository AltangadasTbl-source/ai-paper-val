# Workflow 1.6 Statistical Consistency — Pass 1

- Runtime agent: root/statistics_pass1 (canonical task /root/statistics_pass1).
- Model: gpt-6.1-sol; reasoning effort: high; start mode: FRESH_SPAWN; current inherited provider retained.
- Complete scope: DOC-001 11 pages, DOC-002 60 pages, DOC-003 5 pages, DOC-004 25 pages, DOC-005 1 page; every mapped inferential relationship, using only supplied evidence.
- Stable statistical set: S001–S140, 140 relationships; every row PASS_1_COMPLETE. Part 1 covers S001–S117 (117); part 2 covers S118–S140 (23). These include 39 moderation rows, 24 nonimputed results, 8 CACE results, 16 main secondary coefficients, 8 Cohen D descriptors, 6 main OR/HR results, and all supplied missingness, power, qualitative inference and model-definition relationships.
- Discovery output: six qualifying local records SC01, SC02, SC03, SC05, SC06, SC07. SC04 is retained as an explicitly noncandidate coverage observation. No stable C ID, severity, adjudication or disposition is assigned here.
- Artifacts: statistics/relationship_inventory.md; statistics/parts/stats1-relationships-001.md; statistics/parts/stats1-relationships-002.md; checkers/statistical_pass_1.md.

## Completed checks

Every relationship was checked for endpoint order, estimate containment, direction and scale, qualitative null/P agreement, measure and reference labels, population/time/model/imputation identity, and matched repetitions or supplied transformation rules. The inventory records all printed values, source roles, exact locations, named missing inputs, and row-level completion. All displayed point estimates lie within their ordered intervals. All supplied standard errors are positive. Symptom and utility directions are distinguished. Moderator narratives agree with the negative F-BA×baseline PHQ coefficient, positive supplements×baseline GAD coefficient, and positive F-BA×UK utility coefficient. CACE stars agree qualitatively with the displayed intervals. Exact variance, degrees of freedom, covariance, confidence-interval engines, and test inversions are not inferred.

The baseline-GAD row in supplement 3 p19 prints B=.464, CI [.409,.520], P=0. It is DISPLAY_ZERO_NOT_CANDIDATE. Its direction, interval and narrative are compatible; no independent supplied-source contradiction exists. No tiny-tail probability or replacement threshold was reconstructed.

The main Table 3 doubling rule was checked with independent display rounding. For example, PHQ overall coefficient .33 and narrative adjusted mean difference .65 are compatible if an underlying coefficient .325 is rounded separately before and after doubling. The endpoint pairs .12/.25, .15/.29, .05/.11 and .50/1.01 likewise admit compatible independently rounded values. These are not candidates. Utility upper endpoints printed .000/.00 with P=.052/.055/.06 do not establish exact null boundaries. Cohen D is derived from baseline/T12 means and pooled SD, whereas B is baseline-adjusted ANCOVA; their signs need not match. Imputed means/SDs required to reproduce D are not supplied. The asymmetry of moderation Table B site intervals is not a candidate without a supplied symmetric interval definition.

Diagnostic approximation only: nonimputed T12 IDS supplements B=.28 and SE=.28 have a central ratio 1, but independently rounded inputs admit .285/.275≈1.036, corresponding to a two-sided normal diagnostic P≈.30. This illustrates why central rounded ratios do not prove a P contradiction. The actual normal/t choice and degrees of freedom are unreported; the diagnostic does not replace the reported analysis and creates no candidate.

## SC01 — Main sample-size total and factorial-cell count do not reconcile

- Proposed category: Numeric or arithmetic inconsistency.
- Relationship: S001 (M010).
- Compared roles/locations: REPORT [jama_bot_2019_oi_190007.pdf p4, Sample Size](../../../jama_bot_2019_oi_190007.pdf#page=4), total and parenthesis within the same paragraph. No PLAN comparator is needed to establish this mismatch.
- Printed evidence: “392 participants (196 in each of the 4 possible intervention combinations)”; the paragraph then gives 250 participants per combination allowing 22% attrition.
- Rule and direct observation: 4×196=784, not 392. The literal total and four cell counts cannot simultaneously be the same participant total. No inferential convention is needed.
- Derived diagnostic: 196/(1−.22)=251.28, approximately 250. The total 392 could refer to a marginal two-group comparison, with 196 misdescribed as a factorial cell count. That production explanation is not established.
- Alternative/missing definition: 392 may count a binary comparison rather than the complete four-cell trial; the intended sample unit for each number is unstated. This possibility does not reconcile the literal printed wording.
- Human question: What sample or comparison does 392 count, and what group does 196 count? Check the original power worksheet and intended marginal/factorial wording.
- Direct-source confirmation: fresh Poppler 110-dpi rendering of physical p4 visually confirms 392, 196, 4 and 250; native/layout text agrees.
- Role relationship: provisional S_W, solely within one REPORT document. This is a reporting consistency question, not a claim about achieved power or paper conclusions.

## SC02 — Protocol difference25% is not defined consistently with printed30%/15% incidences

- Proposed category: Numeric or arithmetic inconsistency.
- Relationship: S002 (U009).
- Compared roles/locations: PLAN [joi190007supp1_prod.pdf p16, section4.4](../../../joi190007supp1_prod.pdf#page=16), within the same sample-size paragraph.
- Printed evidence: a target “difference of 25% in the cumulative incidence rates” between conditions; control (placebo, no FBC) incidence 30%, intervention incidence 15%; additive interaction 180 participants/group, two-sided alpha .05 and power .90.
- Rule and direct observation: 30%−15%=15 percentage points, and (30−15)/30=50% relative reduction. Neither ordinary interpretation of this between-condition difference is 25%.
- Alternative/missing definition: 25% might refer to each strategy's marginal effect under an additive configuration while 30%/15% refer to both-control versus combined intervention, or to another contrast in the power calculation. The paragraph does not identify that mapping. No power formula is inferred.
- Human question: Which contrast and percentage base does 25% describe, and does it match the 30%/15% assumptions used for 180/group?
- Direct-source confirmation: fresh 110-dpi rendering of physical p16 visually confirms every percentage and power input.
- Role relationship: P_P, solely within PLAN material. The candidate is conditional on the unnamed percentage/contrast definition; it does not assert that the power calculation was wrong.

## SC03 — Report and protocol give different sample-size assumptions

- Proposed category: Cross-document numeric inconsistency.
- Relationships: S001, S002, S003 (M010, U009, U010).
- Compared roles/locations: REPORT [jama_bot_2019_oi_190007.pdf p4, Sample Size](../../../jama_bot_2019_oi_190007.pdf#page=4) versus PLAN [joi190007supp1_prod.pdf p16, section4.4](../../../joi190007supp1_prod.pdf#page=16) and [p17 continuation](../../../joi190007supp1_prod.pdf#page=17).
- Printed evidence: report active20%/control30%, relative33%/absolute10%, 196 per printed factorial cell, attrition22%, power90%. Protocol active15%/control30%, difference25%, 180/group, dropout20%, power90% for additive interaction, power80% for pure groups if synergistic. Both give250 per factorial arm.
- Rule and direct observation: the matched one-year MDD trial's sample-size descriptions differ in active incidence (20 versus15), per-group analyzable N (196 versus180), and dropout assumptions (22 versus20). This comparison is independent of SC01's literal total and SC02's percentage definition.
- Alternative/missing definition: main-effect and additive-interaction calculations may intentionally differ; protocol version7 incorporates amendments. The supplied package does not map the two calculations or identify which superseded which. Equal recruitment targets do not establish equal planning assumptions.
- Human question: Which calculation governed recruitment? Were separate power contrasts or an amendment intended? Obtain the dated calculations and contrast mapping for both descriptions.
- Direct-source confirmation: report p4 and protocol p16 fresh visual renders confirm the values; current protocol p17 native/layout text supplies the80% continuation.
- Role relationship: P_R, REPORT versus PLAN. This is a reporting/planning alignment question, not a protocol-violation or power-failure judgment.

## SC04 — Noncandidate coverage observation: planned standardizedT12 output and reportedB/D

S130 compares PLAN [joi190007supp2_prod.pdf p3, fourth-analysis paragraph](../../../joi190007supp2_prod.pdf#page=3) with REPORT [jama_bot_2019_oi_190007.pdf p8, Table3](../../../jama_bot_2019_oi_190007.pdf#page=8). The SAP plans standardized mean differences with95%CI/P at T12; the report explicitly provides unstandardized B withCI/P plus separate Cohen D point estimates. Example: PHQ supplements T12 B=.28, CI[.05,.50], P=.02, D=.10.

Both measures are truthfully labeled in the report. D uncertainty and the mapping from planned standardized T12 effects to reported baseline/T12 D are absent, but these omissions alone do not establish a numeric or mislabeled-result contradiction. No identity between B and D is imposed. This is a missing-definition/output-precision limitation, not one of the six qualifying candidates. No C ID should be assigned from this observation alone.

## SC05 — IDS endpoint hierarchy differs between protocol, SAP and report

- Proposed category: Measure, label, or scale inconsistency.
- Relationship: S129; concrete reported estimates S018–S021.
- Compared roles/locations: PLAN [joi190007supp1_prod.pdf p28, section8.1.1 main study parameter/endpoint](../../../joi190007supp1_prod.pdf#page=28), [p43, section10.1 primary parameter](../../../joi190007supp1_prod.pdf#page=43), versus PLAN [protocolp9 study parameters](../../../joi190007supp1_prod.pdf#page=9), [protocolp14 secondary objective](../../../joi190007supp1_prod.pdf#page=14), and PLAN [joi190007supp2_prod.pdf p2 Outcomes](../../../joi190007supp2_prod.pdf#page=2). REPORT comparators: [mainp4 Secondary Outcomes](../../../jama_bot_2019_oi_190007.pdf#page=4), [mainp8 Table3](../../../jama_bot_2019_oi_190007.pdf#page=8).
- Printed evidence: protocol p28 lists both cumulative12-month MDD and IDS baseline/3/6/12 under main endpoints; p43 primary analyses include IDS severity. Protocol p9 continues the main-endpoint list begun on p8; it does not call IDS secondary. Protocol p14 lists depressive symptoms in broader secondary objectives, without resolving the specific IDS hierarchy. SAP p2 explicitly calls IDS secondary. The report calls IDS secondary and prints the estimates in secondary Table3: supplements overall B=.60, CI[.15,1.05], P=.01; T12 B=.36, CI[−.19,.90], P=.20.
- Rule and direct observation: the same IDS outcome and inferential outputs receive different primary/main-versus-secondary labels. The candidate concerns the interpretation label of an actual reported statistic, not a general design concern.
- Alternative/missing definition: “main study parameter” might indicate an operational main measurement rather than formal primary hierarchy; protocol amendments may have updated sections incompletely; SAP may refine the final hierarchy. The applicable final rank is not provided explicitly.
- Human question: What final prespecified rank applies to IDS, and were protocol sections28/43 superseded? Confirm the hierarchy relevant to extraction and interpretation of the reported P=.01.
- Source authority: current page-delimited native/layout transcriptions and freshly reconstructed maps. Mechanical recheck must inspect exact supplied pages above.
- Role relationships: P_P for the explicit protocol/SAP difference; P_R for the protocol/report difference. Primary P_R by precedence. The SAP agrees with the report but independently differs from the protocol's main/primary label. Protocol p9 is corroboration of the main label, not a conflicting secondary label. The broader p14 wording is context only.

## SC06 — Cox results labelledposthoc while suppliedSAP lists the analysis prospectively

- Proposed category: Statistical reporting inconsistency.
- Relationship: S128; concrete HR results S011–S013.
- Compared roles/locations: PLAN [joi190007supp2_prod.pdf p4, Secondary analysis](../../../joi190007supp2_prod.pdf#page=4) versus REPORT [mainp4 Statistical Methods](../../../jama_bot_2019_oi_190007.pdf#page=4), [mainp6 Table2](../../../jama_bot_2019_oi_190007.pdf#page=6), and [mainp7 Onset](../../../jama_bot_2019_oi_190007.pdf#page=7).
- Printed evidence: SAP says “as a secondary analysis” it will examine time-to-onset MDD with Cox regression, HR95%CI/P. Report methods call it post hoc; Table2 labels “Post Hoc Outcome: Time to MDD Onset” and gives supplements HR1.05, CI[.86,1.27], P=.65; F-BA HR.91, CI[.75,1.10], P=.32; interaction HR.91, CI[.75,1.11], P=.36.
- Rule and direct observation: matched outcome/time-to-event/Cox/HR outputs are prospectively listed in supplied PLAN material but explicitly labeled post hoc in the REPORT. This is an interpretation/prespecification label attached to displayed statistics; no numeric effect mismatch is claimed.
- Alternative/missing definition: the SAP is undated, and its status or finalization could postdate the analytic decision. The report might mean a specific Cox configuration was post hoc rather than the general analysis. Exact approval history and implementation mapping are absent.
- Human question: Does post hoc refer to endpoint, model or implementation, and was the supplied SAP prospective for these exact HR outputs? Verify dated approvals and contrast/time configuration.
- Source authority: current SAPp4 transcription, mainp4 fresh render and mainp6 reusable source image confirm the labels. Mechanical recheck should inspect supplied SAPp4.
- Role relationship: P_R. No correction or protocol-violation judgment is assigned.

## SC07 — Agreement kappas reverse omega and micronutrient labels

- Proposed category: Measure, label, or scale inconsistency.
- Relationships: S053, S054 (U051, U055 footnote).
- Compared roles/locations: REPORT [joi190007supp3_prod.pdf p4, eAppendix2 product definitions](../../../joi190007supp3_prod.pdf#page=4), [p12, eAppendix6 Other measures](../../../joi190007supp3_prod.pdf#page=12), [p16, eAppendix8 double-asterisk footnote](../../../joi190007supp3_prod.pdf#page=16).
- Printed evidence: p4 supplement1=omega EPA/DHA capsule, supplement2=selenium/folate/vitaminD/calcium pill. P12 gives kappa agreement .73 and .70 for supplements1 and2 “respectively.” P16 gives multinutrient=.73 and omega=.70.
- Rule and direct observation: explicit product identity and “respectively” assign omega=.73 and micronutrient=.70 in p12; the table footnote assigns micronutrient=.73 and omega=.70. This is a matched agreement-statistic label reversal, independent of any CI/P convention.
- Alternative/missing definition: “multinutrient” could mean the combined products in one context, although the p16 adherence rows distinguish multinutrient from omega. Different measurement aggregation or denominators could produce different kappas, coincidentally equal and reversed, but no such definition is supplied.
- Human question: Which kappa belongs to omega and which to the micronutrient pill? Do both locations refer to the same weight/self-report measurement, aggregation and denominator?
- Direct-source confirmation: the reusable p16 source image visually confirms the footnote; current native/layout p4/p12 transcriptions supply product identity and the respectively clause. Mechanical recheck should confirm all exact pages.
- Role relationship: S_W, within one REPORT results supplement. P4 supplies product identity, not a different document or PLAN relationship.

## Bounded noncandidate limitations

OR/HR contrast definition: Table2 labels active effects with controls as reference and models−1/+1 coded interventions, but does not establish whether printed OR/HR is exp(B), exp(2B), a marginal contrast or another output transformation. The full coded treatment change spans two units; assuming the printed ratio is exp(B) would invent the estimand mapping. This missing definition is not a candidate. No squared ratio is asserted as a correction.

CACE rescaling: original effect scale/model, nonlinear mapping and paired imputed compliance fractions are not supplied. ITT OR1.06 and CACE OR.84 have different directions, but the two estimands are distinct and the ratio formula's original input is undefined. No identity with Table2 raw OR/logOR is assumed; no candidate is created from that assumption. Continuous CACE coefficients are likewise not forced to equal visible ITT coefficients divided by available-case adherence.

The source supplies two-sided .05, confidence95%, model names, adjustments, effectcoding,100MI, MAR and Rubin pooling, but not exact pooled degrees of freedom, covariance, finite-sample variance adjustments or CI/test engines. Moderator tables additionally lack table-specific model/MI definitions. Missingness and concealment test names, grouping, statistics and degrees of freedom are absent. Kappa paired denominators are absent. Exact P/CI/SE compatibility cannot be reconstructed from invented defaults.

Available-data graphics show boxes/IQR whiskers and means without printed exact inferential points; these are not confidence intervals. Planned RERI, nutrient and dietary analyses lack displayed inferential results; omission alone is not a numeric candidate. Raw imputed means/SDs, original CACE inputs, power worksheets and amendment chronology are absent. All102 source pages and140 registered statistical relationships remain covered. The coordinator must spawn a different fresh gpt-6.1-sol/high runtime for pass2 and enumerate all140 S IDs in both statistical coverage stages.

## Canonical aggregation of complete pass-1 relationship records

The following complete original parts are merged here without losing any input or pass-1 observation. Their AWAITING_PASS_2 cells are historical pass-1 handoff fields, not current status: the distinct pass-2 completion is recorded for every ID in the canonical statistical inventory and pass-2 checker below its own full aggregation. Original part files are preserved unchanged. This aggregation exposes all140 relationships directly in the canonical checker for the bundled validator; no new scientific inference or candidate decision is introduced.
# Statistical relationship inventory part 1

Scope: S001–S117, 117 distinct inferential or definition relationships; runtime /root/statistics_pass1, gpt-6.1-sol/high, FRESH_SPAWN. Every row is PASS_1_COMPLETE. Source roles and physical PDF pages are explicit. NR means not reported, not zero. The model-definition profiles in the canonical inventory apply to every row naming that profile. Check K means ordered endpoints, estimate containment, direction, scale and labels checked; matched repetitions checked where present; no independent inconsistency found. Check Q means no numeric estimate/interval available; all supplied inferential statements, scope, label and repetitions checked. Exact CI/P/test compatibility is not asserted when the profile lacks a supplied compatible rule. Every row awaits the distinct pass-2 agent.

## Power, assumptions and missingness

| S ID | Mapping key | Exact source and role | Printed inferential relationship | Definition profile | Pass-1 checks and observations | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|---|
| S001 | M010 | REPORT jama_bot_2019_oi_190007.pdf p4 Sample Size | Active20%, control30%; relative33%, absolute10%; N392,196 in each4 combinations; two-sided alpha.05,power.90,attrition22%,250/combination; prior25–50% | POWER-R | Counts/scale checked; SC01 internal total wording; SC03 comparison with PLAN assumptions | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S002 | U009 | PLAN joi190007supp1_prod.pdf p16 section4.4,p17 continuation | Difference25%; control30%,active15%; additive-interaction180/group,two-sided alpha.05,power.90,dropout20%,250/arm | POWER-P | SC02 percentage meaning; SC03 planning-assumption match to S001; no invented power formula | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S003 | U010 | PLAN joi190007supp1_prod.pdf p17 section4.4 | Synergistic pure-treatment-group comparison power80%; IDS continuous power statement separately tracked S140 | POWER-P | Q; contrast differs from additive calculation; unreported effect/variance prevent reconstruction | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S004 | M012 | REPORT jama_bot_2019_oi_190007.pdf p4 Statistical Methods | Scaled Schoenfeld proportionality test P>.05; hazard assumption met | PH-TEST | Q; direction agrees with stated test; statistic/df/per-term/global identity NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S005 | M071 | REPORT jama_bot_2019_oi_190007.pdf p6 Follow-up Attrition | Primary missingness across4arms,T3 P=.47;194/1025 missing | MISSING | Q; no difference narrative compatible; test/df NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S006 | M071 | REPORT jama_bot_2019_oi_190007.pdf p6 Follow-up Attrition | Primary missingness across4arms,T6 P=.62;254/1025 missing | MISSING | Q; no difference narrative compatible; test/df NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S007 | M071 | REPORT jama_bot_2019_oi_190007.pdf p6 Follow-up Attrition | Primary missingness across4arms,T12 P=.91;246/1025 missing | MISSING | Q; no difference narrative compatible; test/df NR | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Main primary and post hoc outcomes

| S ID | Mapping key | Exact source and role | Estimate, 95% CI, P | Profile | Checks and repetitions | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|---|
| S008 | M075,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset,p1 abstract | Supplements OR1.06,[.87,1.29],P.57;N512/513,54/51 events | LOGIT-MI | K; p1,p6,p7 estimates/CI identical;p6/p7 P identical; unit-change/contrast definition limitation only | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S009 | M077,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset,p1 abstract | F-BA OR.93,[.76,1.13],P.47;N512/513,48/57 events | LOGIT-MI | K; all repeats agree; shared effectcode contrast definition limitation only | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S010 | M078,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset,p1 abstract | Supplements×F-BA OR.93,[.76,1.14],P.48 | LOGIT-MI | K; repeats identical; p1 says combination and explicitly P for interaction; interpretation limited to interaction | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S011 | M080,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset | Supplements HR1.05,[.86,1.27],P.65;4488/4656 person-months | COX-MI | K; repetitions match; effectcode contrast definition limitation only; SC06 planned-secondary/post-hoc label | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S012 | M082,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset | F-BA HR.91,[.75,1.10],P.32;4641/4503 person-months | COX-MI | K; repetitions match; shared effectcode definition limitation only; SC06 shared analysis label | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S013 | M083,M085 | REPORT jama_bot_2019_oi_190007.pdf p6 Table2,p7 Onset | Supplements×F-BA HR.91,[.75,1.11],P.36 | COX-MI | K; repetitions match; interaction kept distinct from joint intervention effect | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Main secondary effects: each outcome/time/contrast separately

Narrative comparisons below use the explicit Table3 footnote d factor2. Rounding compatibility is assessed by allowing each rounded coefficient/endpoint its printed last-digit half-unit. Thus .33 may represent .325 and .12 may represent .124; their doubled displays .65 and .25 are compatible. No hidden exact values are assumed.

| S ID | Mapping key | REPORT exact location: jama_bot_2019_oi_190007.pdf | Coefficient,95% CI,P and matched adjusted mean difference | Profile | Checks | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|---|
| S014 | M092.overall,M105 | p8 Table3 PHQ supplements overall;p8 text | B.33,[.12,.53],P.002; text MD.65,[.25,1.06],P.002 | GEE-MI | K; factor2 matches after independent display rounding | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S015 | M092.T12,M108 | p8 Table3 PHQ supplements T12;p8 text | B.28,[.05,.50],P.02; text MD.56,[.11,1.01],P.02 | ROBUST-MI | K; factor2 matches after independent display rounding | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S016 | M093.overall | p8 Table3 PHQ F-BA overall | B−.13,[−.33,.07],P.19 | GEE-MI | K; negative symptom coefficient compatible with nonsignificance | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S017 | M093.T12 | p8 Table3 PHQ F-BA T12 | B−.17,[−.39,.06],P.14 | ROBUST-MI | K; narrative no other significant therapy effect agrees | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S018 | M094.overall,M106 | p8 Table3 IDS supplements overall;p8 text | B.60,[.15,1.05],P.01; text MD1.20,[.29,2.10],P.01 | GEE-MI | K; factor2 compatible with rounding; symptom increase direction | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S019 | M094.T12 | p8 Table3 IDS supplements T12 | B.36,[−.19,.90],P.20 | ROBUST-MI | K; overall significance does not imply T12 significance | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S020 | M095.overall | p8 Table3 IDS F-BA overall | B−.23,[−.67,.22],P.32 | GEE-MI | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S021 | M095.T12 | p8 Table3 IDS F-BA T12 | B−.28,[−.83,.27],P.31 | ROBUST-MI | K; Cohen D S033 belongs separate unadjusted baseline/T12 definition | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S022 | M096.overall,M107 | p8 Table3 GAD supplements overall;p8 text | B.25,[.08,.42],P.004; text MD.50,[.16,.84],P.004 | GEE-MI | K; exact displayed factor2 agreement | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S023 | M096.T12 | p8 Table3 GAD supplements T12 | B.14,[−.04,.33],P.13 | ROBUST-MI | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S024 | M097.overall | p8 Table3 GAD F-BA overall | B−.16,[−.32,.01],P.06 | GEE-MI | K; near-null nonsignificance retained | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S025 | M097.T12,M104 | p8 Table3 GAD F-BA T12;p8 text;p9 discussion | B−.24,[−.42,−.06],P.01; text MD−.48,[−.84,−.12],P.01 | ROBUST-MI | K; exact factor2 agreement, lower anxiety narrative and figure direction coherent | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S026 | M098.overall | p8 Table3 utility supplements overall | B−.006,[−.012,.000],P.052 | GEE-MI | K; rounded upper.000 may be slightly positive; no forced exact-zero boundary contradiction | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S027 | M098.T12 | p8 Table3 utility supplements T12 | B−.002,[−.008,.005],P.61 | ROBUST-MI | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S028 | M099.overall | p8 Table3 utility F-BA overall | B.002,[−.003,.008],P.44 | GEE-MI | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S029 | M099.T12 | p8 Table3 utility F-BA T12 | B.004,[−.002,.009],P.23 | ROBUST-MI | K | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Standardized descriptors and qualitative inference

| S ID | Mapping key | Exact location and role | Printed value or inferential statement | Profile | Checks | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|---|
| S030 | M092.D,M103 | REPORT main p8 Table3 PHQ supplements | Cohen D.10, no CI/P for D | COHEN | Positive sign agrees with poorer supplement PHQ change; no exact imputed group summaries supplied | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S031 | M093.D,M103 | REPORT main p8 Table3 PHQ F-BA | Cohen D−.02, no CI/P for D | COHEN | Direction coherent; adjusted B and baseline/T12 descriptor are different estimands | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S032 | M094.D,M103 | REPORT main p8 Table3 IDS supplements | Cohen D.05, no CI/P for D | COHEN | Positive sign agrees; exact imputed inputs NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S033 | M095.D,M103 | REPORT main p8 Table3 IDS F-BA | Cohen D.006, no CI/P for D | COHEN | Small positive D versus negative adjusted B is not a contradiction: unadjusted change and adjusted ANCOVA differ; inputs NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S034 | M096.D,M103 | REPORT main p8 Table3 GAD supplements | Cohen D.10, no CI/P for D | COHEN | Direction coherent; inputs NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S035 | M097.D,M103 | REPORT main p8 Table3 GAD F-BA | Cohen D−.07, no CI/P for D | COHEN | Direction coherent; inputs NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S036 | M098.D,M103 | REPORT main p8 Table3 utility supplements | Cohen D−.07, no CI/P for D | COHEN | Direction coherent; higher utility is better, unlike symptom scales | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S037 | M099.D,M103 | REPORT main p8 Table3 utility F-BA | Cohen D.08, no CI/P for D | COHEN | Direction coherent; no equality with adjusted B asserted | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S038 | M091 | REPORT main p7 secondary interaction prose,p8 Table3 footnote a | PHQ supplements×F-BA no significant interaction; P belongs aggregate range.41–.98, row-specific P NR | INTERACTION-MI | Q; main interactions omitted; nonimputed interactions S098/S099 are distinct variant | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S039 | M091 | REPORT main p7,p8 Table3 footnote a | IDS supplements×F-BA no significant interaction; P aggregate.41–.98,row-specific NR | INTERACTION-MI | Q; no inferred row-specific P | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S040 | M091 | REPORT main p7,p8 Table3 footnote a | GAD supplements×F-BA no significant interaction; P aggregate.41–.98,row-specific NR | INTERACTION-MI | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S041 | M091 | REPORT main p7,p8 Table3 footnote a | Utility supplements×F-BA no significant interaction; P aggregate.41–.98,row-specific NR | INTERACTION-MI | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S042 | U057.narrative | REPORT joi190007supp3_prod.pdf p18 moderation opening | MDD history×supplements: primary outcome not moderated; coefficient/CI/P NR | HISTORY-MOD | Q; statement not confused with main history covariate coefficient | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S043 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: primary outcome not moderated; coefficient/CI/P NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S044 | U057.narrative | REPORT supplement3 p18 | MDD history×supplements: PHQ secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S045 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: PHQ secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S046 | U057.narrative | REPORT supplement3 p18 | MDD history×supplements: IDS secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S047 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: IDS secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S048 | U057.narrative | REPORT supplement3 p18 | MDD history×supplements: GAD secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S049 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: GAD secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S050 | U057.narrative | REPORT supplement3 p18 | MDD history×supplements: utility secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S051 | U057.narrative | REPORT supplement3 p18 | MDD history×F-BA: utility secondary not moderated; coefficient/CI/P/time-specific NR | HISTORY-MOD | Q; no result assumed for unprinted separate time-to-onset moderation | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S052 | M116,U064 | REPORT main p8 concealment;REPORT joi190007supp3_prod.pdf p23 eAppendix13 | P<.001; n759; believed supplements percentages8.2,10.4,25.5,43.7 across four arms,three answers | CONCEAL | Q; matched P/percentages agree; exact test and tested grouping NR; no assumed chi-square df | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S053 | U051,U055 footnote | REPORT joi190007supp3_prod.pdf p12 compliance,p16 footnote | Kappa.73: p12 supplement1,p16 multinutrient | KAPPA | Definition-label comparison SC07; estimate in admissible range; no CI/SE | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S054 | U051,U055 footnote | REPORT joi190007supp3_prod.pdf p12 compliance,p16 footnote | Kappa.70: p12 supplement2,p16 omega | KAPPA | Definition-label comparison SC07; estimate in admissible range; no CI/SE | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Moderation Table A: PHQ at 12 months

All following locations are REPORT joi190007supp3_prod.pdf p18 Table A, B unstandardized, 95% CI/P, MOD-A profile. Netherlands reference has no inferential estimate and is retained in the profile, not an invented S row.

| S ID | Map | Predictor | B | 95% CI | P | Checks | Pass 1 | Pass 2 |
|---|---|---|---:|---|---|---|---|---|
| S055 | U057.a | Supplements | .046 | [−.399,.490] | .841 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S056 | U057.b | F-BA | .288 | [−.155,.731] | .203 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S057 | U057.c | Spain | −.480 | [−1.161,.202] | .168 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S058 | U057.d | UK | .275 | [−.373,.923] | .405 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S059 | U057.e | Germany | .233 | [−.396,.862] | .468 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S060 | U057.f | MDD history | −.536 | [−1.036,−.036] | .036 | K; main history covariate is not intervention×history | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S061 | U057.g | Baseline PHQ | .322 | [.265,.379] | <.001 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S062 | U057.h,M111 | F-BA×baseline PHQ | −.064 | [−.118,−.01] | .020 | K; p18 and main p8/p9 larger reduction at higher PHQ direction match | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S063 | U057.i | Supplements×baseline PHQ | .032 | [−.023,.086] | .259 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Moderation Table B: overall follow-up anxiety

All locations REPORT joi190007supp3_prod.pdf p19 Table B; MOD-B profile, B unstandardized, 95% CI/P; Netherlands reference. Intervals for site terms need not be forced symmetric without an explicit interval engine.

| S ID | Map | Predictor | B | 95% CI | P | Checks | Pass 1 | Pass 2 |
|---|---|---|---:|---|---|---|---|---|
| S064 | U058.a | Supplements | −.107 | [−.384,.17] | .45 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S065 | U058.b | F-BA | −.054 | [−.329,.221] | .703 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S066 | U058.c | Spain | .107 | [−.424,.520] | .694 | K; asymmetric about B, method NR; no symmetry-only candidate | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S067 | U058.d | UK | .117 | [−.371,.638] | .637 | K; asymmetric about B, method NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S068 | U058.e | Germany | .058 | [−.401,.606] | .804 | K; asymmetric about B, method NR | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S069 | U058.f | MDD history | −.317 | [−.698,.063] | .102 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S070 | U058.g | Baseline GAD | .464 | [.409,.52] | 0 | K; DISPLAY_ZERO_NOT_CANDIDATE; independent contradiction absent | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S071 | U058.h | F-BA×baseline GAD | −.016 | [−.068,.036] | .554 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S072 | U058.i,M111 | Supplements×baseline GAD | .062 | [.009,.115] | .022 | K; p18 and main p8 higher anxiety at higher baseline direction agree | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Utility moderation: all-site C1 and separate UK/NL C2 tables

All locations REPORT joi190007supp3_prod.pdf p20, B unstandardized,95% CI/P. MOD-C profile; C1 Netherlands reference for site/interactions. Both subgroup headings printed C2; numbering does not alter quantitative identities. Rounded B.000 does not establish an exact zero coefficient.

| S ID | Map | Table/population and predictor | B | 95% CI | P | Checks | Pass 1 | Pass 2 |
|---|---|---|---:|---|---|---|---|---|
| S073 | U059.a | C1 supplements | .000 | [−.012,.012] | .952 | K; rounding compatible | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S074 | U059.b | C1 F-BA | −.006 | [−.018,.006] | .313 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S075 | U059.c | C1 Spain | .005 | [−.012,.022] | .548 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S076 | U059.d | C1 UK | −.014 | [−.031,.003] | .097 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S077 | U059.e | C1 Germany | .011 | [−.006,.027] | .198 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S078 | U059.f | C1 MDD history | .009 | [−.003,.022] | .148 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S079 | U059.g | C1 baseline utility | .498 | [.438,.558] | <.001 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S080 | U059.h | C1 F-BA×Spain | .016 | [−.001,.032] | .066 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S081 | U059.i,M111 | C1 F-BA×UK | .017 | [.001,.033] | .041 | K; UK>NL narrative p18/main p8 matches | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S082 | U059.j | C1 F-BA×Germany | .006 | [−.01,.022] | .452 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S083 | U059.k | C1 supplements×Spain | −.006 | [−.023,.011] | .499 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S084 | U059.l | C1 supplements×UK | −.001 | [−.018,.016] | .907 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S085 | U059.m | C1 supplements×Germany | .002 | [−.014,.017] | .850 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S086 | U060.a | C2 UK supplements | .000 | [−.012,.011] | .944 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S087 | U060.b | C2 UK F-BA | .013 | [.001,.024] | .033 | K; UK benefit direction agrees with C1 comparison | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S088 | U060.c | C2 UK MDD history | .007 | [−.016,.03] | .559 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S089 | U060.d | C2 UK baseline utility | .738 | [.62,.856] | <.001 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S090 | U061.a | C2 NL supplements | .000 | [−.012,.012] | .935 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S091 | U061.b | C2 NL F-BA | −.007 | [−.019,.005] | .267 | K; distinct subgroup model, not exact C1 conditional coefficient identity | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S092 | U061.c | C2 NL MDD history | −.005 | [−.031,.021] | .697 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S093 | U061.d | C2 NL baseline utility | .509 | [.400,.619] | <.001 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Nonimputed sensitivity: every overall and T12 result

All locations REPORT joi190007supp3_prod.pdf p21 eAppendix11. Profile GEE-OBS overall, ROBUST-OBS T12. Effectcoded−1,+1; intervention and interaction included together; site/history/baseline adjusted. Main Table3 excludes interaction and imputes; numeric equality is not expected. Overall shows B95%CI; T12 shows B(SE), not a CI. No guessed variance or degrees of freedom.

| S ID | Map | Outcome/contrast/time | B | CI or SE exactly as labeled | P | Checks | Pass 1 | Pass 2 |
|---|---|---|---:|---|---|---|---|---|
| S094 | U062.a.overall | PHQ supplements overall | .30 | CI[.11,.49] | .002 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S095 | U062.a.T12 | PHQ supplements T12 | .28 | SE.11 | .013 | SE positive; no CI supplied; rounded ratio compatible diagnostically, no exact rule supplied | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S096 | U062.b.overall | PHQ F-BA overall | −.14 | CI[−.34,.05] | .14 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S097 | U062.b.T12 | PHQ F-BA T12 | −.22 | SE.11 | .052 | SE positive; near-threshold result not forced to P<.05 from rounded2.0 ratio | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S098 | U062.c.overall | PHQ interaction overall | −.01 | CI[−.20,.18] | .94 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S099 | U062.c.T12 | PHQ interaction T12 | .02 | SE.11 | .84 | SE positive; low ratio coherent qualitatively | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S100 | U062.d.overall | IDS supplements overall | .55 | CI[.11,.99] | .01 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S101 | U062.d.T12 | IDS supplements T12 | .28 | SE.28 | .30 | SE positive; .275–.285 rounding of numerator/denominator admits ratio1.036 and diagnostic Pabout.30 | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S102 | U062.e.overall | IDS F-BA overall | −.26 | CI[−.70,.18] | .25 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S103 | U062.e.T12 | IDS F-BA T12 | −.36 | SE.28 | .20 | SE positive; no exact inferential rule | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S104 | U062.f.overall | IDS interaction overall | −.01 | CI[−.45,.43] | .96 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S105 | U062.f.T12 | IDS interaction T12 | .12 | SE.28 | .66 | SE positive; no exact inferential rule | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S106 | U062.g.overall | GAD supplements overall | .24 | CI[.08,.40] | .004 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S107 | U062.g.T12 | GAD supplements T12 | .17 | SE.09 | .07 | SE positive; no exact inferential rule | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S108 | U062.h.overall | GAD F-BA overall | −.16 | CI[−.32,.00] | .06 | K; rounded upper.00 can be positive; no boundary-only candidate | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S109 | U062.h.T12 | GAD F-BA T12 | −.26 | SE.09 | .005 | SE positive; lower anxiety direction matches main sensitivity interpretation | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S110 | U062.i.overall | GAD interaction overall | .04 | CI[−.13,.20] | .66 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S111 | U062.i.T12 | GAD interaction T12 | .03 | SE.09 | .74 | SE positive; no exact inferential rule | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S112 | U062.j.overall | Utility supplements overall | −.006 | CI[−.011,.000] | .055 | K; precision permits null within unrounded interval | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S113 | U062.j.T12 | Utility supplements T12 | −.001 | SE.003 | .66 | SE positive; coarse ratio precision retained | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S114 | U062.k.overall | Utility F-BA overall | .002 | CI[−.004,.007] | .51 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S115 | U062.k.T12 | Utility F-BA T12 | .004 | SE.003 | .23 | SE positive; coarse ratio precision retained | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S116 | U062.l.overall | Utility interaction overall | −.002 | CI[−.008,.003] | .42 | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S117 | U062.l.T12 | Utility interaction T12 | .001 | SE.003 | .65 | SE positive; coarse ratio precision retained | PASS_1_COMPLETE | AWAITING_PASS_2 |
# Statistical relationship inventory part 2

Scope: S118–S140,23 relationships; same fresh pass-1 owner /root/statistics_pass1. All rows PASS_1_COMPLETE; definition profiles and K/Q check meanings are in canonical inventory/part1.

## CACE: every effect row separately

Every location below is REPORT joi190007supp3_prod.pdf p22 eAppendix12. CACE-MDD profile for MDD, CACE-CONT for symptoms. CI95%; single*=P<.05; **=P<.01 definition printed but no double-star cell. No exact P or SE supplied. Effectcoding−1,+1; omega adherence≥70%,F-BA8/21. The observed ITT and CACE populations/estimands are different; equality of their coefficients is not imposed.

| S ID | Map | Outcome/intervention | Estimate | 95% CI | Printed inference | Checks/repetitions | Pass 1 | Pass 2 |
|---|---|---|---:|---|---|---|---|---|
| S118 | U063.a,M112 | MDD F-BA | OR.78 | [.64,.95] | * P<.05 | K; main p8 OR/CI and significant narrative identical;p9 lower MDD coherent | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S119 | U063.b,M112 | MDD supplements | OR.84 | [.67,1.07] | no star,exact P NR | K; main p8 no primary effect compatible; direction differs from ITT S008 but CACE original-scale mapping unknown; see S127 | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S120 | U063.c | PHQ F-BA | B−.22 | [−.59,.15] | no star | K; direction matches ITT, inference nonsignificant | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S121 | U063.d | PHQ supplements | B.43 | [.08,.77] | * P<.05 | K; poorer symptoms direction matches main narrative | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S122 | U063.e | IDS F-BA | B−.42 | [−1.24,.40] | no star | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S123 | U063.f | IDS supplements | B.47 | [−.33,1.27] | no star | K | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S124 | U063.g | GAD F-BA | B−.31 | [−.60,−.02] | * P<.05 | K; lower anxiety direction matches primary ITT symptom analysis | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S125 | U063.h | GAD supplements | B.18 | [−.11,.47] | no star | K | PASS_1_COMPLETE | AWAITING_PASS_2 |

## Definition-linked inferential comparisons and planned quantitative analyses

| S ID | Mapping key | Exact sources and document roles | Printed relationship and check | Definition/missing inputs | Pass 1 | Pass 2 |
|---|---|---|---|---|---|---|
| S126 | U053,U054,U063.a/c/e/g,M014,M112 | REPORT joi190007supp3_prod.pdf pp14–15 CACE explanation,p22 F-BA column;REPORT main pp4,6,8 | CACE difference described as original intervention effect/proportion compliers; randomization instrument in structural equation model. Full-sample CACE coefficient matches main only for stated OR. No forced direct division of an OR. | CACE profile; original coefficient scale, exact original-model inputs, paired compliance denominator, nonlinear-to-linear estimand mapping NR. Cannot reproduce numerical rescaling from displayed ITT OR or B. Definition deficit is a limitation, not a manufactured candidate. | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S127 | U053,U054,U063.b/d/f/h,M014,M112 | REPORT joi190007supp3_prod.pdf pp14–15,p22 supplements column;REPORT main pp4,6,8 | Same formula statement for supplements; OR.84 versus ITT1.06 is a direction difference across distinct analyses; CACE direction is not asserted equal to ITT absent original input/model mapping. | Original effect scale/model and compliance fraction NR; no unsupported OR-ratio or log-OR scaling identity assumed. All printed CACE intervals contain estimate; stars coherent. | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S128 | U032,U040,U041,U042,M007,M012,M075 | PLAN joi190007supp1_prod.pdf pp28,43;PLAN joi190007supp2_prod.pdf pp2–4;REPORT main pp4,6 | Protocol primary survival and mixed analysis; SAP primary cumulative-MDD logistic OR95%CI/P, secondary Cox HR95%CI/P; report primary logistic/post-hoc Cox. Logistic definition matches SAP; protocol/SAP differ by version scope; SC06 report post-hoc Cox label versus SAP secondary plan. | PLAN models retain their prospective roles; no numerical results in plans. Version chronology/amendment mapping NR. No clinical/design adjudication. | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S129 | U002,U006,U020,U032,U040,M008,M094,M095 | PLAN joi190007supp1_prod.pdf pp9,14,28,43;PLAN joi190007supp2_prod.pdf p2;REPORT main pp4,8 | IDS in protocol p28 main study endpoints/p43 primary parameter severity; protocol p9 continues its main-endpoint list, while SAP p2 calls IDS secondary; main Table3 secondary IDS estimates S018–S021. SC05 concrete endpoint/inferential label discrepancy. | Endpoint hierarchy differs inside PLAN and between PLAN/REPORT; exact amendment history not supplied. Comparisons keep outcome,12month and scale identity. | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S130 | U041,M092–M103 | PLAN joi190007supp2_prod.pdf p3 fourth-analysis paragraph;REPORT main p8 Table3 | SAP T12 standardized mean differences95%CI/P; report T12 unstandardized coefficient95%CI/P plus separate Cohen D without CI/P. effect-measure/precision-output definition limitation only. | Unstandardized B and standardized D are explicitly distinct. No denominator or SD borrowed from available-data plots; missing imputed SD and D uncertainty. | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S131 | U009,U042,M078 | PLAN joi190007supp1_prod.pdf p16 power;PLAN joi190007supp2_prod.pdf p4 interaction plan;REPORT main p6 Table2 interaction | SAP multiplicative interaction A×B in logistic; planned additive RERI from linear-OR model with likelihood95%CI, lowest-risk joint reference recoding, RERI>0 departure criterion. Report shows multiplicative interaction only. | RERI estimate/CI not supplied; no numerical identity with OR.93 imposed; omission of separately planned analysis alone not a numeric candidate. | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S132 | U033,U041,U055.o–r | PLAN joi190007supp1_prod.pdf pp43–44;PLAN joi190007supp2_prod.pdf p3 third-analysis paragraph;REPORT supplement3 p16 | Planned nutrient-status regression in blood subset adjusted intervention; planned longitudinal T6/T12 blood concentrations adjustedT0 as compliance check. Report descriptive changes N335/334,medianIQR only. | No observed inferential test/CI/coefficient supplied; no conversion of IQR toSE or CI. Data availability/nutrient change identities covered; method omissions not candidates alone. | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S133 | U032,U041,U055.l/m/n | PLAN joi190007supp1_prod.pdf p43 secondary;PLAN joi190007supp2_prod.pdf p3 third-analysis paragraph;REPORT supplement3 p16 | Planned longitudinal behavior T3/T6/T12 and dietary intake T6/T12 adjustedT0; protocol secondary mixed models. Report diet/weight descriptive T12−T0,not inferential. | No estimateCI/P for these contrasts; SD-like parentheses are not inferential SE; missing supplied result prevents compatibility reconstruction. | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S134 | U033,U042,U043,M013,M111,U057–U061 | PLAN joi190007supp1_prod.pdf p44;PLAN joi190007supp2_prod.pdf pp4–5;REPORT main pp4,8;REPORT supplement3 pp18–20 | Protocol modifiers country/sex/education/income/BMI/age in Cox/Mixed; SAP history/center,interactionP<.05; report site/history plus post-hoc baseline severity; all printed modifier estimates tracked S055–S093. | Planned/unreported subgroup coefficient identities not invented; baseline severity explicitly post-hoc; table exact interval/variance engines and MI status NR. Matched PHQ/GAD/utility directions agree. | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S135 | U043,M011,M015,U062,U063 | PLAN joi190007supp2_prod.pdf p5 missingness;REPORT main pp4,6,p8 tables;REPORT supplement3 pp21–22 | SAP100datasets,MAR,Rubin rules,FIML/MI where appropriate;report100datasets,MAR,Rubin,MI main/CACE and nonimputed sensitivity. Two-sided.05 reportp6/SAPp3. | Poolingdf,finite-sample adjustment,exact model covariance,variance estimator,CI engine and multiplicity correction NR. Exchangeable GEE correlation supplied. No external defaults used to derive exact P from CI/SE. | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S136 | M071,M086 | REPORT jama_bot_2019_oi_190007.pdf p6 Follow-up Attrition,p7 Figure2 PHQ N | PHQ questionnaire missing rates did not differ across intervention groups. Available N baseline996,T3 819,T6 750,T12 757; corresponding missing29,206,275,268 among1025 are arithmetic locators, not new inferential estimates. | Overall no-difference statement covers these assessment times; no individual-time P/test/CI/statistic is supplied, and no time-specific inference is invented. Two-sided threshold mainp6; test model/df/variance/multiplicity NR. Q. | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S137 | M071,M087 | REPORT mainp6 Follow-up Attrition,p7 Figure2 IDS N | IDS questionnaire missing rates did not differ across intervention groups. Available N baseline994,T3 817,T6 747,T12 757; missing31,208,278,268 derived among1025. | Same broad missingness inference; no separate printed time-specific test. Test/model/df/variance/multiplicity NR. Q. | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S138 | M071,M088 | REPORT mainp6 Follow-up Attrition,p7 Figure2 GAD N | GAD questionnaire missing rates did not differ across intervention groups. Available N baseline993,T3 815,T6 747,T12 757; missing32,210,278,268 derived among1025. | Same broad missingness inference; no separate printed time-specific test. Test/model/df/variance/multiplicity NR. Q. | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S139 | M071,M089 | REPORT mainp6 Follow-up Attrition,p7 Figure2 utility N | Utility questionnaire missing rates did not differ across intervention groups. Available N baseline993,T3 814,T6 747,T12 757; missing32,211,278,268 derived among1025. | Same broad missingness inference; no separate printed time-specific test. Test/model/df/variance/multiplicity NR. Q. | PASS_1_COMPLETE | AWAITING_PASS_2 |
| S140 | U010 | PLAN joi190007supp1_prod.pdf p17 section4.4 | IDS-30 continuous outcome power will be much larger; prior prevention trial smaller samples gave significant differences; no numeric power/effect/variance/P supplied. | Separate from synergistic MDD contrast S003. Alpha/two-sided/power assumptions on p16 describe primary calculation; no IDS variance or specific IDS power model supplied. Qualitative expectation only; Q. | PASS_1_COMPLETE | AWAITING_PASS_2 |
