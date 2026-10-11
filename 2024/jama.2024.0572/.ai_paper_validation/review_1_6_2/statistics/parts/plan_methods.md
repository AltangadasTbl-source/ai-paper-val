# Statistical relationship inventory — plan methods, second-pass bounded shard

Mechanical source-linked split of first-pass statistics/parts/tables_b_plan.md. Scope: S5067–S5120, 54 inferential and statistical-design records. All first-pass evidence and complete Bayesian calculation facts below are preserved unchanged. Fresh pass-2 agent adds its independent completion facts.

# Statistical pass 1 inventory: tables B and plan methods

Fresh statistical shard: /root/stat1_tables_b_plan; model gpt-6.1-sol; reasoning high; FRESH_SPAWN. Scope: DOC-006 eTables8–13 physical pp45–53; DOC-003 entire protocol statistical-method and numerical decision-rule content; DOC-004 entire parent SAP statistical-method and numerical decision-rule content. Historical inferential statements are tracked as supplied PLAN facts, separately from SELECT2 outcomes. Main-report methods, DOC-005 and other result displays are separate assigned shards.

Read QUALITY_CONTROL_SCOPE.md and review_contract.md completely. Mapping aids: support_parts/results_b_admin.md, protocol.md and trial_sap_a.md/trial_sap_b.md. Final authority: direct Poppler layout extraction for DOC-003/006 and source-matched images for scanned DOC-004. Direct transient command pdftotext -layout -f N -l N source.pdf -. Visually read DOC-006 pp45–53; protocol pp13,80,81 and parent SAP pp10,11,12,16,40; existing mapper visual records cover other plan pages. No new derivative, Python, web or prior conclusions used. Reused sources/assets preserved. CPU inspection; engine/version for reused renders recorded in evidence_asset_inventory.md, unrecorded legacy engine versions remain limitations.

120 records: S5001–S5120. Every displayed estimate/CI pair and interaction test in eTables8–10 is independent:24+6+10+6+10+6; eTable12 adds4. Plan methods/rules37; historical inferential pairs/tests17. A Bayesian threshold vector is one complete decision rule, with every row calculated independently within that record.

Shared table definitions:95%CI; ordinal ratio null1, binary RR null1, RD null0. eTable8 is within each received-treatment arm, profile versus concordant reference: concordant ASPECTS<6/core≥70mL, D1 ASPECTS<6/core<70, D2 ASPECTS6–10/core≥70. N163EVT/N156MM. eTable9 is randomized EVT-versus-MM treatment effect within CTP/MRI profile, eTable10 within composite-core profile. Interaction always compares treatment-effect modification across profiles. No individual effect-test P is supplied in those tables. N/A cells have no numerical estimate/test to enumerate.

Numeric context for matching: eTable8 FI:EVT32/163,MM10/156; concordant10/75 vs3/82; D1 21/76 vs7/63; D2 1/12 vs0/11. Ambulation62/163vs27/156;concordant18/75vs8/82;D1 41/76vs19/63;D2 3/12vs0/11. mRS5–6 75/163vs97/156;concordant42/75vs59/82;D1 25/76vs28/63;D2 8/12vs10/11. eTable9 FI MM/EVT concordant3/83vs10/74;D1 7/63vs21/76;D2 1/11vs0/12(N/A). Ambulation8/83vs18/74;19/63vs41/76;3/11vs0/12(N/A). mRS5–6 60/83vs41/74;28/63vs25/76;10/11vs8/12. eTable10 FI8/118vs18/112;2/28vs13/38;2/12vs0/14(N/A);ambulation19/118vs35/112;8/28vs24/38;4/12vs0/14(N/A);mRS5–6 74/118vs53/112;14/28vs13/38;11/12vs9/14. Cross-table FI/ambulation cell attribution is preserved for numeric/cross-source review, without assuming same analysis set.

Descriptive-only inspection: eTable11 MRI-follow-up groupsN101MM/24mTICI0–2a/79mTICI2b–3, medians(IQR)CTP/MRI95(56,135)/125(76,179)/68(37,142); composite63(22,102)/91(71,142)/45(16,90);CT69(31,122)/107(87,152)/60(24,110). Each median lies within ordered IQR, no inferential CI/test. eTable13 core minus follow-up:162−143=19,140−90=50,93−11=82mL; each exceeds≥10mL threshold. 'Significant' there explicitly means volume threshold, not an unstated P test. These displays have no omitted inferential estimate/test.

### S5067 — Discordance superiority rule

- Location/role: [DOC-003 physical p22](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=22); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Prior EVT good-outcome rates 48% vs32%; planned15 percentage-point margin; logistic OR95%CI for discordant imaging comparison (p51); diagram p71.
- Checks/calculation: 48−32=16 percentage points. No executed margin decision supplied. p51 repeats same profile in two word orders, while p22, second p51 paragraph and diagram clearly identify two opposite profiles. Excluded wording observation.
- Definitions/limits: Margin-to-OR decision mapping lacks executed result; no generic preference asserted.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Direct protocol pp.22,51 confirm 16-point historical separation and prospective15-point margin; comparison profiles are immediately identifiable despite repeated wording. No executed OR-to-margin conclusion is supplied; exclusions remain wording/missing implementation, not a numerical superiority conclusion.

### S5068 — Functional-independence hierarchy

- Location/role: [DOC-003 physical p37](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=37); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: p8/p37: second primary=mRS0–2 at90days. p50: secondary endpoint=mRS0–2 at90days. DOC004p13/p17: secondary.
- Checks/calculation: Same outcome/time receives primary and secondary status inside one dated protocol. F-ST1-502; PLAN/PLAN, P_P.
- Definitions/limits: Status discrepancy directly affects planned hierarchy.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Exact protocol pp.37,50 and SAP pp.13,17 reproduce primary-versus-secondary status for the same90-day mRS0–2 endpoint. C010 and its Route A category5 provenance cover this pattern; PLAN-only P_P classification retained.

### S5069 — Protocol primary analysis

- Location/role: [DOC-003 physical p45](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=45); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: ITT90-day mRS; normal-approximation WMW/GLR; additional generalizedCMH stratified by randomization factors; age,NIHSS,time,core called continuous.
- Checks/calculation: Overall and adjusted rank-based comparisons are separately defined. Continuous stratification language lacks implementation but no numerical contradiction supplied.
- Definitions/limits: Stratum construction and tie/rank implementation missing; generic omission excluded.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Protocol p.45 names normal-WMW overall and additional generalized-CMH adjustment separately. Continuous-covariate language omits implementation but supplies no conflicting adjusted statistic. No test, strata or variance structure inferred.

### S5070 — Adaptive population partition

- Location/role: [DOC-003 physical p45](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=45); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: G1A/B: ASPECTS3–5/core<50; G2A/B: ASPECTS6–10/core≥50; G3A/B: ASPECTS3–5/core≥50. A0–12h/B12–24h. Five cumulative subgroups; DOC004p9 matches.
- Checks/calculation: Imaging definitions partition eligible population; five cumulative alternatives plus overall match J6. No observed boundary-time duplicate enrollment supplied.
- Definitions/limits: Unstated handling of exactly12hours does not establish numerical conflict.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Direct protocol p.45 and SAP p.9 confirm six disjoint imaging/time groups and five cumulative alternatives plus overall J=6. Exactly12h assignment is unreported without an observed duplicate count; no numeric population inconsistency.

### S5071 — Projected distributions and standardized effect

- Location/role: [DOC-003 physical p46](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=46); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT mRS0–6:4,8,12,16,19,13,28%; MM:1,4,9,14,19,10,43%; effect.34; DOC004pp10–11 repeats.
- Checks/calculation: Both sums100%. Diagnostic half-tie WMW=.59375; sqrt(12)*(.59375−.5)=.324760. Difference from.34 less than5% before rounding; no finding.
- Definitions/limits: Standardized effect and tie-variance definition absent; diagnostic is not ASSISTant reproduction.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Both seven-cell projected distributions independently sum100%. Half-tie superiority=.59375 and untied normal standardization=.32475953 are diagnostic only; .34 versus that diagnostic differs4.48% and does not clear precision threshold.

### S5072 — Sample size and power

- Location/role: [DOC-003 physical p46](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=46); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: FixedN376=188/arm; power90%, alpha5% in protocol; DOC004p11 one-sided.025. Additional184 gives adaptive560; interim200/380; adaptive91%power/effect.34/one-sided.025.
- Checks/calculation: Arithmetic reproduces. Diagnostic N=4*(1.959964+1.281552)^2/.34^2=363.579. Effect[.335,.345],power[.895,.905],alpha[.0245,.0255] yields approximateN349–379, overlapping376±.5; exactWMW/simulation not reconstructed.
- Definitions/limits: Protocol fixed alpha sidedness absent; two-sided.05/one-sided.025 share critical z.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; 376=188+188 and376+184=560 reproduce;560−380=180. Diagnostic normal fixed N363.57865 is not ASSISTant/WMW reproduction; first-pass half-unit input bounds349–379 overlap printed376. One-sided.025 and unspecified protocol.05 do not establish calibration conflict.

### S5073 — First interim tree

- Location/role: [DOC-003 physical p47](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=47); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N200 completed90-day. Overall neither→continue; efficacy→stop; futility→select/test subgroup. Selected neither→restrict; efficacy→stop; futility→stop. DOC004pp9–10 repeats.
- Checks/calculation: All branches defined; maximum560, with smaller available analyzedN after enrichment.
- Definitions/limits: No realized interim statistic or relaxed-bound formula supplied.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Direct protocol p.47/SAP p.9 specify every first-look overall/selected efficacy/futility/continue branch. Actual first200-patient continuation is disclosed atSAP p.12 without an observed statistic to reverse the decision.

### S5074 — Second interim tree

- Location/role: [DOC-003 physical p47](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=47); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N380 completed90-day. Overall repeats first tree; selected neither→180 additional; efficacy→stop; futility→stop. DOC004p10 matches.
- Checks/calculation: 560−380=180; both accrual scenarios specified.
- Definitions/limits: No executed N380 decision supplied.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Second-look two-scenario tree matches protocol pp.47–48 and SAP p.10; additional180=560−380. No executed380-patient rule supplied; do not substitute300 review for this scheduled branch (C014).

### S5075 — Final tree

- Location/role: [DOC-003 physical p48](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=48); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Protocolp48 overall560: failure→select/test subgroup; previously selected→test selected. DOC004p10 tests overall or selected and otherwise declares not superior.
- Checks/calculation: Later SAP does not restate overall-failure rescue branch. Actual trial stopped at300 (p12). Apparent final-branch observation excluded because no executed result supplied.
- Definitions/limits: CONDITIONAL_OR_UNREPORTED; preserve both dated descriptions.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Direct protocol p.48 explicitly allows final subgroup selection/test after overall failure; SAP p.10 explicitly declares not superior on failed final efficacy test and p.40 states the overall final boundary. This is a printed planned primary decision-rule difference, not merely absent executed data: F-ST2-601; version/relevance ambiguity retained.

### S5076 — Adaptive simulation scenario 0

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 0,0,0,0,0,0; mean0; adaptiveN426,power2.0%; fixed560,power2.5%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean0; null rates within2.5%; futility59.1%/N426 context coherent. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Six zero effects yield weighted mean0; weights sum1; null2.0% adaptive/2.5% fixed and expected426≤560 reconcile. Simulation code/seed unavailable; observed trial statistics not substituted.

### S5077 — Adaptive simulation scenario 1

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .32,.32,.32,.32,.32,.32; mean.32; adaptive376,86.0%; fixed560,95.8%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Mean.32; diagnostic normal fixed power≈.958; printed copies match. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Six.32 effects yield weighted.32; expected376≤560. Fixed95.8% versus adaptive86.0% with smaller expectedN is coherent; normal-power diagnostic about.958 only, not simulation-code reproduction.

### S5078 — Adaptive simulation scenario 2

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .3,.3,.3,.3,.3,.3; mean.3; adaptive393,81.1%; fixed560,93.3%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Mean.3; diagnostic normal power≈.944 differs<5% from.933, not an exact simulation calculation. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Six.30 effects yield weighted.30; expected393≤560. Fixed93.3% versus adaptive81.1% is internally allowed; a normal diagnostic about.944 is within relative5%, without claiming exact simulation reproduction.

### S5079 — Adaptive simulation scenario 3

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .4,.4,.4,.4,0,0; mean.16; adaptive500,74.1%; fixed560,45.7%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.4*.4=.16. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Weighted mean .4*(.14+.06+.14+.06)=.16; adaptiveN500≤560. Printed45.7% fixed/74.1% adaptive preserve distinct designs; no cross-design equivalence assumed.

### S5080 — Adaptive simulation scenario 4

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .4,.4,.4,.4,−.1,−.1; mean.1; adaptive502,78.5%; fixed560:21.2%protocol/51.2%SAP; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.4*.4−.1*.6=.10. Same supplied input row; fixed powers differ beyond precision. F-ST1-503. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Exact protocol p.49/SAP p.11 confirm scenario4fixed21.2%/51.2%, equal other displayed inputs. Complete screen records F-ST1-503 PERIPHERAL_COMPARISON; no duplicate finding. This alternative operating-characteristic output does not supply observed rejection or changed sample-size input.

### S5081 — Adaptive simulation scenario 5

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .4,.4,.3,.3,0,−.1; mean.122; adaptive513,67.1%; fixed560,29.2%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.4*.2+.3*.2−.1*.18=.122. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Weighted mean .4*.20+.3*.20−.1*.18=.122; expected513≤560, fixed29.2%/adaptive67.1% distinct design outputs. No interval/test or count conflict.

### S5082 — Adaptive simulation scenario 6

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .5,.5,0,0,0,0; mean.1; adaptive503,70.6%; fixed560,21.2%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.5*.2=.10. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Weighted mean .5*(.14+.06)=.10; expected503≤560. Fixed21.2% and adaptive70.6% are distinct algorithms, not paired estimates/tests.

### S5083 — Adaptive simulation scenario 7

- Location/role: [DOC-003 physical p49](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=49); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: .5,0,0,0,0,0; mean.07; adaptive503,60.5%; fixed560,12.8%; DOC004p11; weights.14,.06,.14,.06,.42,.18; 5000trials.
- Checks/calculation: Weighted mean.5*.14=.07. Weights sum1; all expectedN≤560.
- Definitions/limits: Simulation code/seed not supplied. Normal calculations explicitly diagnostic.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Weighted mean .5*.14=.07; expected503≤560. Fixed12.8% versus adaptive60.5% concerns concentrated alternative; coherent with separate designs, no reproducible conflict.

### S5084 — Minimization algorithm

- Location/role: [DOC-003 physical p78](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=78); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Gk=ΣwfIk; variance reduction2ΣwfNk/(K−1)+constant; choose minimum. Protocol weights4,4,3,3,2,blank,1,1 for age,NIHSS,clot,time,core,mismatch,hemisphere,center. SAPp37:3,4,3,3,4,2,2,1 plusASPECTS3; p79/SAPp38 T2probabilities.9/.5/.1.
- Checks/calculation: Probability.9 favors lower imbalance, tie.5 and opposite.1. Later SAP refines factors and weights. No realized allocation discrepancy. Blank weight alone excluded.
- Definitions/limits: No allocation/raw-data audit; later values retained by version.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Direct protocol pp.78–79/SAP pp.37–38 confirm minimum-imbalance assignment with probabilities.9/.5/.1; updates to factor weights are explicit in later plan. Blank protocol mismatch weight lacks executed allocation contradiction; no raw randomization audit.

### S5085 — Primary missing-outcome rules

- Location/role: [DOC-003 physical p52](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=52); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Protocol90±15day nominalvisit; retrieveclinic/phone60–120days then ordinal-logisticMI. SAPp16 MAR,30imputations,Rubin pooling/tipping point; ITT352p14.
- Checks/calculation: Broader retrieval window is explicit; later SAP adds MI detail. No executed conflicting imputation calculation.
- Definitions/limits: Exact predictor list absent, generic omission excluded.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Protocol p.52 defines broader60–120-day recovery before ordinal MI; SAP p.16 adds MAR,30imputations and Rubin pooling/tipping analysis. Parent352 ITT versus imaging336 is eligibility subset context, not same-population count conflict; no imputed patient output supplied.

### S5086 — Early-window safety

- Location/role: [DOC-003 physical p55](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=55); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Protocolpp55–56 MM mortality increase>20%vsEVT→hold enrollment pendingDSMB.
- Checks/calculation: Absolute/relative scale unspecified but no executed safety decision supplied.
- Definitions/limits: CONDITIONAL_OR_UNREPORTED for missing20%scale alone.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Direct pp.55–56 place hold on MMmortality increase>20% pending DSMB; absolute/relative scale absent. No observed triggering value/test conflicts; isolated missing scale remains conditional rather than an implemented stopping conclusion.

### S5087 — Bayesian sICH ≤100cc

- Location/role: [DOC-003 physical p58](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=58); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N50,100,150,200,250; inclusive triggers24,44,63,82,101 throughN. PriorBeta(.35,.65); posterior Pr(p>.35)>.95; then Pr(EVT>MM+.10)>.95.
- Checks/calculation: PosteriorBeta(.35+s,.65+N−s). Exact incomplete-beta minima24,44,63,82,101; all reproduce.
- Definitions/limits: Step2 has no observed paired data; not assumed executed.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Every ≤100cc sICH trigger independently recomputed using source Beta(.35,.65) posterior; minima24/44/63/82/101 atN50/100/150/200/250 all reproduce. Step2requires paired event data not supplied.

### S5088 — Bayesian sICH >100cc

- Location/role: [DOC-003 physical p59](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=59); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N20,30,40,50,60,70,80,90,100; lower limits11,16,20,24,28,32,36,40,44. Beta(.35,.65);Pr(p>.35)>.95; thenEVT>MM+.10 probability>.95.
- Checks/calculation: Exact incomplete-beta minima11,16,20,24,28,32,36,40,44 reproduce.
- Definitions/limits: Numerical integration of stated beta posterior; no normal approximation.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Every >100cc sICH trigger independently recomputed:11/16/20/24/28/32/36/40/44 atN20–100; predecessor tails≤.95 and minima tails>.95. Exact source rows match.

### S5089 — Bayesian sICH extracranialICA

- Location/role: [DOC-003 physical p60](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=60); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N20,30,40,50,60,70,80,90,100; lower limits11,16,20,24,28,32,36,40,44. Beta(.35,.65);Pr(p>.35)>.95; step2EVT>MM+.10 probability>.95.
- Checks/calculation: Same exact minima reproduce every printed row.
- Definitions/limits: Source-specific scope retained, not double counted as independent cause.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; ExtracranialICA sICH vector independently checked with same stated posterior and source pp.59–60; all nine minima match, with scope maintained separately. No executed event series.

### S5090 — Bayesian mortality ≤100cc

- Location/role: [DOC-003 physical p61](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=61); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N50,100,150,200,250; lower limits26,49,71,92,113. Beta(.4,.6);Pr(p>.4)>.95; step2EVT>MM+.10 probability>.95.
- Checks/calculation: Exact minima26,49,71,92,113 reproduce.
- Definitions/limits: No executed step2 comparison supplied.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; ≤100cc mortality vector independently recomputed under Beta(.4,.6):26/49/71/92/113 atN50/100/150/200/250; every minimum and predecessor verifies the>.95 rule.

### S5091 — Bayesian mortality >100cc

- Location/role: [DOC-003 physical p62](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=62); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N20,30,40,50,60,70,80,90,100; printed lower limits12,17,22,26,32,35,40,44,49. Beta(.4,.6);Pr(p>.4)>.95.
- Checks/calculation: Exact minima12,17,22,26,31,35,40,44,49. N60,s31 tail.9644096>.95;32vs31 differs3.125% and count half-unit intervals touch. Excluded display precision.
- Definitions/limits: Step2EVT>MM+.10 probability>.95; no executed data supplied.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; AtN60 the stated beta rule reaches>.95 with31events(tail.964409556), predecessor30=.938913247; source threshold32. Exact integer relative difference1/32=.03125≤.05 and half-unit intervals touch; display rule screens this apparent difference. Remaining eight rows reproduce.

### S5092 — Bayesian mortality extracranialICA

- Location/role: [DOC-003 physical p63](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=63); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: N20,30,40,50,60,70,80,90,100; printed lower limits12,17,22,26,32,35,40,44,49; Beta(.4,.6),Pr(p>.4)>.95.
- Checks/calculation: Same minima12,17,22,26,31,35,40,44,49; same N60 observation consolidated in excluded row, relative discrepancy≤5%.
- Definitions/limits: Step2 conditional comparison supplied without observed event data.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; ExtracranialICA mortality repeats the sameN60 threshold32/minimum31 pattern and is consolidated withS5091; all other eight rows reproduce. No interval-versus-ownP or same-display relative>.05 discrepancy; rounding exclusion retained.

### S5093 — Appendix direction and theta

- Location/role: [DOC-003 physical p81](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=81); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Y=MMmRS,X=EVTmRS;H0P(Y≤X)=.5;HAP(Y≤X)=.5+theta;theta=(z.975+z.9)/sqrt(3*560)=.0791. EfficacyZ≥2.604/final≥2.772;futilitytildeZ≤−1.897. DOC004pp39–40 repeats.
- Checks/calculation: Theta=.07908489 reproduces. Positive alternative favors lower MM score rather than EVT; F-ST1-504. Rank-sum orientation also needs clarification.
- Definitions/limits: Hypothesis orientation is explicit, independent of unknown ranking/tie convention; actual stoppingZ absent.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Exact protocol pp.80–81/SAP pp.39–40 confirm positiveP(MM≤EVT)=.5+.0791 despite lower-mRS benefit; C013 covers direction and missing coding/ranks/ties. Independenttheta=.0790848815 reproduces. No operational Z or alpha inferred.

### S5094 — SAP300 stopping review

- Location/role: [DOC-004 physical p12](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=12); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: DOC004p12 planned200/380, requested300 review, no alteration/additional interim analyses; apply prespecified boundaries to30090-day cases and stop for efficacy;family-wise.05.
- Checks/calculation: Boundary application at300 differs from stated200/380 schedule, while claiming no alteration. F-ST1-505 asks which calibrated rule applies.
- Definitions/limits: Review and stop explicitly disclosed; no broad critique; .05vsone-sided.025 alone excluded.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; SAP pp.9,11–12,40 directly retain200/380 schedule and describe300-outcome boundary rejection with no added analysis. C014 covers missing information-time/boundary mapping; count differences cannot be rounding, but no alpha-violation claim made.

### S5095 — SAP ordinal merge

- Location/role: [DOC-004 physical p14](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Primary mRS5/6 mergedp14/p16 to avoid6→5 counting as success; anticipated distributionp10 has sevenlevels.
- Checks/calculation: Analysis definition and planning distribution are separate objects; no contradictory executed calculation supplied.
- Definitions/limits: Tie handling not assumed beyond source merger.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; SAP pp.14–16 explicitly merges mRS5/6 for treatment-success analyses. Planningseven-level distribution and descriptive full-scale graphics are distinct quantities; no absent-rank reconstruction or raw data claim.

### S5096 — SAP WMW transformations

- Location/role: [DOC-004 physical p16](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: WMW superiority95%CI/P;ARD described as probability EVTbetter, formulaARD=2(WMW−.5);NNT=1/ARD;WMW generalized odds95%CI.
- Checks/calculation: Explicit transformation identifies net comparative quantity. Descriptive probability wording apparent issue excluded; no executedARD supplied.
- Definitions/limits: TERMINOLOGY_OR_WORDING; generalized-odds/tie/CI formula absent.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; DirectSAP p.16 suppliesARD=2(WMW−.5) andNNT=1/ARD, making net contrast explicit. Probability wording alone does not change a supplied executed ARD; no result or interval/P conflict established. Terminology exclusion retained.

### S5097 — SAP functional independence

- Location/role: [DOC-004 physical p17](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=17); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 90-daymRS0–2; derive indicator from imputedmRS, Rubin pooling; modifiedPoissonRR95%CI/P.
- Checks/calculation: Model/output and imputation linkage coherent.
- Definitions/limits: No executed estimate/test here.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; DirectSAP p.17 defines90-daymRS0–2, derived binary indicators from MIordinal scores, Rubin pooling and modifiedPoissonRR95%CI/P; coherent planned linkage. Hierarchy discrepancy belongsC010; imaging-specific population discrepancy belongsC002.

### S5098 — SAP independent ambulation

- Location/role: [DOC-004 physical p17](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=17); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 90-daymRS0–3; same MI/Rubin; modifiedPoissonRR95%CI/P.
- Checks/calculation: Model/output and population/threshold coherent.
- Definitions/limits: No executed estimate/test here.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; DirectSAP p.17 defines90-daymRS0–3 with sameMI/Rubin/modPoisson planned approach; threshold nested within ordinal outcome and not confused with independence. No executed number here.

### S5099 — SAP binary safety/early improvement

- Location/role: [DOC-004 physical p18](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=18); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: sICH24h, worsening≥4NIHSS24h, all-cause death90days, improvement≥8orNIHSS0–1 at24h. Binary logisticMI30, mortalityderivedmRS; modifiedPoissonRR95%CI/Ppp18–21.
- Checks/calculation: Common analysis rule checked separately against each endpoint definition and missingness link; all explicit. Missing early-improvement hypothesis predicate resolved by surrounding binary comparison.
- Definitions/limits: Covariate/pooled-test detail unreported; no numerical conflict.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; DirectSAP pp.18–21 separately verifies sICH/worsening24h,mortality90d and improvement≥8orNIHSS0–1; binarylogisticMI and modifiedPoissonRR output are distinct steps. C015 retains PLAN-only4h/24h comparison; no REPORTwindow fabricated.

### S5100 — SAP descriptive methods

- Location/role: [DOC-004 physical p19](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=19); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Complications cumulativecounts/proportions; reperfusionmTICI≥2bEVTonly; neither hypothesistest norimputation. Discharge sixcategory proportions/noimputationp20.
- Checks/calculation: Descriptive analysis intentionally distinguished from tested binary outcomes; unnamed discharge test has no executedP supplied.
- Definitions/limits: Generic absent discharge test excluded.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; DirectSAP pp.19–20 defines proceduralcomplications/reperfusion as descriptive with no hypothesis/imputation; discharge has hypothesis but no named test. No executed dischargeP establishes a missing-method contradiction.

### S5101 — SAP NeuroQoL

- Location/role: [DOC-004 physical p21](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=21); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 90-dayquality-of-life distribution; median(IQR); median-regression difference95%CI/P; noimputation.
- Checks/calculation: Median contrast compatible with quantile-regression output.
- Definitions/limits: No executed estimate/CI here.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; DirectSAP p.21 names median-regression difference95%CI/P forNeuroQoL90d, median(IQR) description/noMI. This is an internally stated coherent model; no preferred quantile/rank method proposed.

### S5102 — SAP sensitivities/subgroups

- Location/role: [DOC-004 physical p23](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=23); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: As-treatedreceived treatment; per-protocol allcriteria/core-lab imaging/assignedtreatment. RepeatWMW. Subgroupsage70,NIHSS20,ICA/M1,time12/6h,core70/100/150,ASPECTS6–10/3–5/0–2,mismatch1.8/15and1.2/10,restrictedsets,hemisphere,US/nonUSpp21–23.
- Checks/calculation: Populations clearly separate; nested thresholds are distinct analyses. Secondary multiplicity not adjustedp14;95%CI. Illustrative forest entries1.00(.50,2.00) are placeholders.
- Definitions/limits: No comparison of illustrative values with trial estimates.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; SAP pp.21–23 defines all subgroup thresholds and distinctas-treated/per-protocol sensitivities. Illustrative1.00(.50,2.00) entries are templates, not zero-event reported RRs; no RouteA1 false pairing. Secondary multiplicity explicitly unadjusted.

### S5103 — SAP exploratory imaging

- Location/role: [DOC-004 physical p23](../../../../joi240006supp3_prod_1708623114.99733.pdf#page=23); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Section12 exploratory/tertiary may defer; core/ASPECTS ceilings,joint modification,mismatch, compositeunion or larger when union infeasible, age/severity/time/hemisphere/transferetc.
- Checks/calculation: Context identifies same optional tertiary scope; no executed result here. DOC005 secondary-specific SAP separately assigned.
- Definitions/limits: No raw-data/model-preference audit.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; SAP pp.23–24 expressly permits tertiary analyses beyondprimarymanuscript; compositeunion with larger-volume fallback is specified. Later analysis-specific max-core hierarchy is coveredC003 in itsassignedlane; no generic omittedtertiary candidate.

### S5104 — Historical SELECT functional independence

- Location/role: [DOC-003 physical p13](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=13); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT30%vsMM13%; adjustedOR2.92,95%CI1.00–7.91,P=.041
- Checks/calculation: Estimate contained, endpoints ordered; printedCIcontainsnull1 whileP<.05; F-ST1-501. No Wald method assumed.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.13 confirmshistoricalOR2.92CI1.00–7.91/P.041; estimatecontained,endpointsordered,butprintednullboundary/significantP remainsC011RouteA1. Hiddenprecision/CItestalternatives retained, no modelvariance inferred.

### S5105 — Historical SELECT ordinal effect

- Location/role: [DOC-003 physical p13](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=13); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: AdjustedOR2.01,95%CI1.00–4.03,P=.049
- Checks/calculation: Estimate contained, endpoints ordered; printedCIcontainsnull1 whileP<.05; F-ST1-501.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.13 confirmshistoricalOR2.01CI1.00–4.03/P.049 andsignificantshift; sameC011pattern. PLAN historicalclassificationambiguity explicit, not currenttrial effect.

### S5106 — Historical SELECT sICH

- Location/role: [DOC-003 physical p14](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT7%vsMM13%,P=.26
- Checks/calculation: Nonsignificant conclusion agrees withP. No matched effectCI; exact test unstated.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.14 historical7%/13%,P.26 accompaniesnostatisticaldifference; direction/test conclusionreconcile. No matchedCI/testformula supplied for exactnumericP reproduction.

### S5107 — Historical SELECT mortality

- Location/role: [DOC-003 physical p14](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT29%vsMM42%,P=.17
- Checks/calculation: Nonsignificant conclusion agrees withP. Exact test unstated.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.14 historical29%/42%,P.17 agreesnonsignificantmortalitystatement. Roundedpercentages and absentmodel/armNs cannot establish contradictory estimate.

### S5108 — Historical retrospective good outcome

- Location/role: [DOC-003 physical p14](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: ASPECTS<7:37%vs≥7:47%,P=.8
- Checks/calculation: Printed nonsignificant conclusion agrees withP; sample size/test absent; no assumed reproduction.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.14 historical37%/47%,P.8 agreesnonsignificantgood-outcomestatement; noCI/rawNs/test supplied, no imputed testmethod.

### S5109 — Historical retrospective sICH

- Location/role: [DOC-003 physical p14](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 9%vs9%,P=1.0
- Checks/calculation: Identical rounded percentages and nonsignificantP; no contradiction.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.14 historical9%/9%,P1.0 agreesno sICHdifference. Equalroundedpercentages do not requireequal exactrisks; noconflict.

### S5110 — Historical retrospective mortality

- Location/role: [DOC-003 physical p14](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 20%vs22%,P=.8
- Checks/calculation: Small displayed difference with nonsignificantP; no supplied contradictoryCI.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.14 historical20%/22%,P.8 agreesnomortalitydifference. No interval/test conflict or unique sourcedefinedreproduction.

### S5111 — Historical matched-cohort ordinal effect

- Location/role: [DOC-003 physical p14](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=14); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: OR2.56,95%CI2.50–8.47,P=.04
- Checks/calculation: Point contained; endpoints ordered; interval excludesnull1/P<.05 agree. Log-Wald symmetry diagnostic alone does not establish conflicting stated test.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.14 printsOR2.56(2.50–8.47),P.04; pointcontained, orderedlimits, null-exclusion/significanceagree. Log-Waldasymmetrydiagnostic lacks stated sharedCI algorithm; differenthistoricalstudies do not form a reproducing common-model display.

### S5112 — Historical matched-cohort independence

- Location/role: [DOC-003 physical p15](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT25%vsMM0%,P=.04
- Checks/calculation: Reported significance matchesP; sample sizes/test absent; no CI supplied.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.15 historical25%/0%,P.04 agreesstatisticalindependenceclaim. MissingmatchedNs/model/CI prevent independentown-test numericreproduction; zero percentage not zeroP.

### S5113 — Historical matched-cohort infarct volume

- Location/role: [DOC-003 physical p15](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: Mean(SD)EVT87(77)vsMM242(120)mL,P<.001
- Checks/calculation: Direction and significantP consistent; sample size missing, no fabricated t-test.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.15 infarctmean(SD)87(77)/242(120)mL,P<.001:lowerEVTvolumeandclaimed significanceagree. No armNs/statedtest for tdiagnostic orSE reconstruction.

### S5114 — Historical matched-cohort PH2

- Location/role: [DOC-003 physical p15](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: P>.99; stated no significant difference
- Checks/calculation: Conclusion/P agree; no point/interval supplied.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.15 PH2P>.99 agreesnostatisticaldifference; noestimateCI or Pzero slip. No additional inference supported.

### S5115 — Historical matched-cohort hemicraniectomy

- Location/role: [DOC-003 physical p15](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: P=.10; stated no significant difference
- Checks/calculation: Conclusion/P agree.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.15 hemicraniectomyP.10 agreesnostatisticaldifference; nointerval/point supplied. No unsupported allocation/test assumed.

### S5116 — Historical matched-cohort mortality

- Location/role: [DOC-003 physical p15](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=15); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: P=.75; stated no significant difference
- Checks/calculation: Conclusion/P agree.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.15 mortalityP.75 agreesnostatisticaldifference; absentcounts/test do not createcandidate.

### S5117 — Historical meta-analysis sICH

- Location/role: [DOC-003 physical p16](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: EVT0%vsMM12%,P=.24
- Checks/calculation: Stated no significant difference agrees; no sample/test inputs supplied.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.16 historicalmeta-analysis sICH0%/12%,P.24 agreesnonsignificant claim. No sampledenominators/model orCI to contradict ownP.

### S5118 — Historical SELECT early-window sICH

- Location/role: [DOC-003 physical p16](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 8/173(5%)vs3/18(17%),P=.072; narrative safety outcomes significantly increased
- Checks/calculation: The sICH P=.072 is not significant at.05 while paragraph explicitly includes it among safety outcomes that significantly increased. Exact test unspecified; see F-ST1-506.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.16 confirms8/173=4.624%→5%,3/18=16.667%→17%,P.072 withcollectivesignificantstatement. C012 coversRouteA1, withhistoricalPLAN/collectivewordingambiguity; noadjusted/crude substitution.

### S5119 — Historical SELECT early-window worsening

- Location/role: [DOC-003 physical p16](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 14/173(8%)vs5/18(28%),P=.023
- Checks/calculation: Direction and significance agree; percentages reconcile with integer rounding.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.16 confirms14/173=8.092%→8%,5/18=27.778%→28%,P.023:direction/significanceandcountpercentages agree. Qualitative doubledwording separatelyexcluded.

### S5120 — Historical SELECT early-window mortality

- Location/role: [DOC-003 physical p16](../../../../joi240006supp2_prod_1708623114.99233.pdf#page=16); PLAN. Context and any paired locations are stated below.
- Printed values, model, contrast and population: 15/173(9%)vs7/18(39%),P=.001
- Checks/calculation: Direction and significance agree; percentages reconcile with integer rounding.
- Definitions/limits: PLAN historical rationale, not observed SELECT2 result. No external source consulted; absent sidedness/model/test inputs not inferred.
- Pass 1: PASS_1_COMPLETE.
- Pass 2: PASS_2_COMPLETE. Fresh independent runtime root/stat2_plan_methods; Directprotocol p.16 confirms15/173=8.671%→9%,7/18=38.889%→39%,P.001:direction/significanceandcountpercentages agree. No fabricatedSE/test calculation.

## Complete Bayesian calculation facts

Posterior given s events/N is Beta(a+s,b+N−s). Tail=1−I_t(a+s,b+N−s), evaluated with Lanczos log-gamma and a convergent incomplete-beta continued fraction in JavaScript. This is deterministic integration of source-specified priors and event counts. No Python, external package or normal approximation used. At each N the minimalinteger s is the first with tail>.95; every predecessor checked.

| Prior/threshold | N | Minimum s | Tail at s | Tail at s−1 |
|---|---:|---:|---:|---:|
| Beta(0.35,0.65);t=0.35 | 20 | 11 | 0.961767775 | 0.907160210 |
| Beta(0.35,0.65);t=0.35 | 30 | 16 | 0.977665716 | 0.949620772 |
| Beta(0.35,0.65);t=0.35 | 40 | 20 | 0.971728919 | 0.943879068 |
| Beta(0.35,0.65);t=0.35 | 50 | 24 | 0.968187856 | 0.941671152 |
| Beta(0.35,0.65);t=0.35 | 60 | 28 | 0.966289545 | 0.941479639 |
| Beta(0.35,0.65);t=0.35 | 70 | 32 | 0.965500009 | 0.942468950 |
| Beta(0.35,0.65);t=0.35 | 80 | 36 | 0.965458559 | 0.944154658 |
| Beta(0.35,0.65);t=0.35 | 90 | 40 | 0.965921547 | 0.946243703 |
| Beta(0.35,0.65);t=0.35 | 100 | 44 | 0.966722456 | 0.948552978 |
| Beta(0.35,0.65);t=0.35 | 150 | 63 | 0.960473449 | 0.943979008 |
| Beta(0.35,0.65);t=0.35 | 200 | 82 | 0.959361444 | 0.945000174 |
| Beta(0.35,0.65);t=0.35 | 250 | 101 | 0.960602998 | 0.948205346 |
| Beta(0.4,0.60);t=0.4 | 20 | 12 | 0.961099626 | 0.906027079 |
| Beta(0.4,0.60);t=0.4 | 30 | 17 | 0.964812378 | 0.925698692 |
| Beta(0.4,0.60);t=0.4 | 40 | 22 | 0.970415675 | 0.941869624 |
| Beta(0.4,0.60);t=0.4 | 50 | 26 | 0.954554044 | 0.920363713 |
| Beta(0.4,0.60);t=0.4 | 60 | 31 | 0.964409556 | 0.938913247 |
| Beta(0.4,0.60);t=0.4 | 70 | 35 | 0.952790714 | 0.924044283 |
| Beta(0.4,0.60);t=0.4 | 80 | 40 | 0.963305404 | 0.941342910 |
| Beta(0.4,0.60);t=0.4 | 90 | 44 | 0.954441732 | 0.930280177 |
| Beta(0.4,0.60);t=0.4 | 100 | 49 | 0.964452433 | 0.945653062 |
| Beta(0.4,0.60);t=0.4 | 150 | 71 | 0.964576872 | 0.949726349 |
| Beta(0.4,0.60);t=0.4 | 200 | 92 | 0.956349011 | 0.941476112 |
| Beta(0.4,0.60);t=0.4 | 250 | 113 | 0.951428952 | 0.937144130 |

No scientific scope gaps. Exact P/CI reproductions unavailable where named sidedness/test/variance/covariance or raw ranks are absent; these are recorded per relationship. Every assigned statistical statement was checked, with candidate inclusion independently pending screen.


