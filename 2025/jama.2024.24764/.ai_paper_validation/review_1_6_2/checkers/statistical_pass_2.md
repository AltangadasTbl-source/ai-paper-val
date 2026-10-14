# Statistical pass 2 — complete independent review

- Runtime agent: `task:/root/statistics_pass2`; newly spawned `gpt-6.1-sol` / `high`, distinct from `task:/root/statistics_pass1`.
- Exact scope: S001–S137, all C001–C005, all ten initial screening decisions, all mechanical recheck facts, and every excluded-observation row from numeric (7), cross-source (10), and statistical pass 1 (12) checkers: 29 rows.
- Completed bounded batches: S001–S120 (120 records) and S121–S137 (17 records). Every relationship has its own result and `PASS_2_COMPLETE` below and in the canonical inventory and its two bounded parts. All 42 tipping bars are individually revisited.
- Findings: zero new F-ST2 findings. Already-screened observations are not re-emitted. Five stable IDs remain Pending Human Adjudication; this stage assigns no adjudication.
- Controls: QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md read completely. Scientific inputs are current-run maps, inventory, checker findings, screening, ledger and exact-source recheck, plus eligible source-linked text/page images. No web, legacy scientific decisions, custom Python, new extraction, OCR or rendering was used.

## Evidence and rules applied

REPORT sources are [main article](../../../jama_atherton_2025_oi_240145_1741627844.85412.pdf#page=1) and [results supplement](../../../joi240145supp3_prod_1741627844.89412.pdf#page=1). PLAN sources are [SAP](../../../joi240145supp1_prod_1741627844.87412.pdf#page=1) and [protocol](../../../joi240145supp4_prod_1741627844.90412.pdf#page=1). Content roles, not supplement numbers, determine relationships. Existing evidence state and classification facts were checked against the source declarations, rather than adopted as dispositions.

Exact-page current-run native text was read for main pp1,2,4,6,8,10, SAP pp12,15,25,26,42 and protocol pp2,17,39; the source-matched results p4 image was visually inspected. Eligible geometric layout supplied main pp3,5,7; results pp3–8; SAP pp9,11–15,17–18,22–23,27–29,44–46; protocol pp17,25–30,38–40. Source-matched main p9 and results p9 images were independently viewed for all subgroup estimates/interaction labels and every tipping bar. The supplemental text header and page footer were used to match exact source pages, including eTable1/eTable2 sharing PDF p3. Main p6 supplies skin-preparation continuation, pain instrument discussion and no-difference narrative. The current source recheck supplies its complete exact-page confirmation of all five candidates and bounded whole-report/whole-protocol searches; those absence checks remain bounded to the supplied package.

Reading aids reside in preprocessing/recheck/ for current-run exact text/images, and the curator's eligible review_1_5_3/preprocessing/numeric_direct/ and support_mapper/ layout files plus document_outputs/ page images. Reused extracts/images are unchanged. Native/render engine for current-run recheck aids is PyMuPDF 1.26.4; rendering device CPU, 200 dpi. Legacy derivative versions are absent as inventoried upstream. This stage produced only review artifacts, so no OCR/GPU inference or derivative engine is claimed.

Two-sided 95% intervals and .05 tests are explicitly supplied by SAP p12 and protocol p38; no multiplicity correction is prescribed. Null is 1 for RR/geometric ratio and 0 for additive differences. For each reported row the check covers ordered endpoints, point containment, null/significance agreement, effect direction/reference, population/time/model matching and relevant count/denominator implications. Interaction tests are kept distinct from individual effects. Exact finite-sample/model P reconstruction is unavailable where test statistic, df, fitted covariance and variance estimator are absent; normal/log-Wald arithmetic is diagnostic only. No conventional df, common variance, omnibus test or denominator is invented. No noninferiority/equivalence margin or claim occurs. Interim guidance is approximate P<.001 with an additional management-impact condition; no realized interim statistic/stopping assertion is supplied to contradict it.

## Per-relationship pass-2 results

Each row is an independent completion record. Its exact location and original printed evidence are retained in statistics/relationship_inventory.md. A reference to a C ID preserves its existing human question and does not duplicate registration.

| S ID | Pass 2 calculation or logical check | Pass 2 status |
|---|---|---|
| S001 | SSI 112/394 and108/394 reconcile; RR1.03 lies in [.83,1.28] containing1, P.78 nonsignificant; copies/reference match. No crude-versus-adjusted substitution. | PASS_2_COMPLETE |
| S002 | RD.010 contained in [−.050,.071], containing0; separate identity-link fit, RR P.78 not assigned to RD. | PASS_2_COMPLETE |
| S003 | UK ratio.91 inside [.82,1.02], includes1 and P.12>.05; lower ratio/medians direction agrees. Planned difference replacement remains C002. | PASS_2_COMPLETE |
| S004 | Pooled ratio.96 inside [.88,1.06], includes1 and P.21>.05; copies match. Diagnostic normal log-Wald P≈.39 requires an unreported test/df to assess exact P; C002 is separate. | PASS_2_COMPLETE |
| S005 | PCS30 −.86 and−.861 half-unit intervals overlap; both ordered CIs contain estimate/0, P.39 nonsignificant. Covariance specification implication retained under C004. | PASS_2_COMPLETE |
| S006 | MCS30 −1.90 and−1.904 half-unit intervals overlap; both CIs contain estimate/0, P.12 nonsignificant; C004 covers covariance. | PASS_2_COMPLETE |
| S007 | Pain7 −.41 lies in [−.70,−.12] excluding0; P.01<.05, lower pain direction/narrative agree. Diagnostic normal P≈.0056 can display.01. | PASS_2_COMPLETE |
| S008 | Pain30 −.06 lies in [−.28,.16] containing0; P.61>.05. Mean1.8 copies do not replace adjusted MD; unrounded output/df absent. | PASS_2_COMPLETE |
| S009 | Readmission11/399 vs11/398 percentages reconcile; RR1.02 within [.45,2.31] includes1, P.96>.05; same-model log diagnostic agrees. | PASS_2_COMPLETE |
| S010 | Readmission RD.010 within [−.014,.034] includes0. SAP expressly reports RR P; normal RD diagnostic.41 is a different link/fit and cannot contradict RR P.96. | PASS_2_COMPLETE |
| S011 | Wound73/392 vs71/397 reconciles; RR1.04 within [.78,1.39] includes1 with P.79>.05. Adjusted label resolves crude comparison. | PASS_2_COMPLETE |
| S012 | Wound RD.007 within [−.046,.060] includes0; no independently attributed RD P. Participant73/71 differs from multiple-type counts84/83 by definition. | PASS_2_COMPLETE |
| S013 | Clean RR.75 in [.43,1.28], includes1; favorable axis agrees;18/24 are event counts, not risk denominators. Interaction.28 is not row P. | PASS_2_COMPLETE |
| S014 | Clean-contaminated RR1.28 in [.87,1.89], includes1;44/35 event counts; reference/axis direction agrees and interaction.28 remains distinct. | PASS_2_COMPLETE |
| S015 | Contaminated RR1.20 in [.77,1.87], includes1;29/23 events, positive unfavorable direction; no row test inferred. | PASS_2_COMPLETE |
| S016 | Dirty RR.84 in [.55,1.29], includes1;21/26 events; four contamination rows sum112/108, not unprinted subgroup denominators. | PASS_2_COMPLETE |
| S017 | No-stoma RR1.19 in [.89,1.60], includes1;70/59 events; unfavorable axis agrees; interaction.14 separate. | PASS_2_COMPLETE |
| S018 | Stoma RR.86 in [.62,1.19], includes1;42/49 events; stoma partitions112/108 and favorable axis agrees. | PASS_2_COMPLETE |
| S019 | Colonic RR.96 in [.72,1.28], includes1;60/60 events; adjusted RR need not equal equal-count crude ratio. | PASS_2_COMPLETE |
| S020 | Noncolonic RR1.09 in [.71,1.66], includes1;29/28 events; direction/axis coherent, no row P derived. | PASS_2_COMPLETE |
| S021 | Nonbowel RR1.14 in [.67,1.94], includes1;23/20 events; operative rows sum112/108, interaction.81 remains distinct. | PASS_2_COMPLETE |
| S022 | BMI<18.5 RR.93 in [.30,2.89], includes1;5/4 events; missing subgroup denominators preclude crude-risk calculation. | PASS_2_COMPLETE |
| S023 | BMI18.5–24.9 RR.94 in [.62,1.41], includes1;33/37 events; reference/direction coherent. | PASS_2_COMPLETE |
| S024 | BMI25–29.9 RR.94 in [.62,1.42], includes1;30/30 events; adjusted effect does not require exactly1. | PASS_2_COMPLETE |
| S025 | BMI≥30 RR1.18 in [.82,1.70], includes1;41/32 events. BMI subtotal109/103 lacks a complete-partition claim; no contradiction with112/108. | PASS_2_COMPLETE |
| S026 | Incision<15 RR1.28 in [.76,2.16], includes1;21/22 events. Report follows SAP substantive<15 rule; screened shell boundary retained for audit. | PASS_2_COMPLETE |
| S027 | Incision≥15 RR1.01 in [.79,1.29], includes1;90/81 events. Subtotal111/103 has no complete-case subgroup denominator statement. | PASS_2_COMPLETE |
| S028 | Chlorhexidine RR1.10 in [.79,1.55], includes1;51/44 events, direction/axis agree; interaction.68 separate. | PASS_2_COMPLETE |
| S029 | Aqueous povidone RR1.15 in [.69,1.94], includes1;19/16 events; no mismatched measure label or row P. | PASS_2_COMPLETE |
| S030 | Other-preparation RR.92 in [.65,1.30], includes1;42/48 events; preparation partition112/108 matches primary. | PASS_2_COMPLETE |
| S031 | UK RR1.08 in [.83,1.40], includes1;79/73 events; primary country comparison distinct from pooled LOS population. | PASS_2_COMPLETE |
| S032 | Australia RR.92 in [.61,1.39], includes1;33/35 events; country totals112/108; interaction.52 separate. | PASS_2_COMPLETE |
| S033 | In-person RR.96 in [.75,1.23], includes1;77/78 events match narrative denominators214/209 and percentages36/37. | PASS_2_COMPLETE |
| S034 | Remote visual RR1.02 in [.54,1.91], includes1;15/16 events match72/76 narrative denominators and21% rounding. | PASS_2_COMPLETE |
| S035 | Remote nonvisual RR.67 in [.31,1.48], includes1;9/13 events match76/76 narrative denominators and12/17% rounding; assessment subtotal not all primary cases. | PASS_2_COMPLETE |
| S036 | UK prepandemic RR1.11 in [.83,1.50], includes1;60/55 events; date contrast/reference/axis match. | PASS_2_COMPLETE |
| S037 | UK on/after11Mar2020 RR.98 in [.58,1.65], includes1;19/18 events; UK event totals79/73, not full international totals. | PASS_2_COMPLETE |
| S038 | PCS7 .130 in [−1.755,2.014] includes0, P.89>.05;248+232=480, adjusted MD distinct from raw means. C004 covariance applies. | PASS_2_COMPLETE |
| S039 | MCS7 −2.190 in [−4.470,.088] includes0, P.06>.05;248+232=480; no threshold reversal. C004 applies. | PASS_2_COMPLETE |
| S040 | Exact `(-0.104 -0.010)` context reads [−.104,−.010], midpoint−.057, P.02<.05, lower QoL direction. Screening notation decision revisited without re-emission; narrative issue remains C001. | PASS_2_COMPLETE |
| S041 | EQ index14 −.023 in [−.072,.027], null included/P.37>.05;233+238=471. C004 applies; normal diagnostic is not exact model output. | PASS_2_COMPLETE |
| S042 | EQ index21 −.017 in [−.067,.032], null included/P.49>.05;229+231=460; direction consistent with control reference. | PASS_2_COMPLETE |
| S043 | EQ index30 −.007 in [−.054,.040], null included/P.78>.05;289+264=553; no final-time test conflict. | PASS_2_COMPLETE |
| S044 | Exact `(-2.389 -4.557)` context reads [−2.389,+4.557], midpoint1.084, contains0/P.54>.05;289+278=567. Notation decision retained. | PASS_2_COMPLETE |
| S045 | EQ health14 −.668 in [−4.379,3.042], null included/P.72>.05;231+226=457; adjusted label preserved. | PASS_2_COMPLETE |
| S046 | Exact `(-5.926 -1.597)` context reads [−5.926,+1.597], midpoint−2.1645 consistent with estimate rounding, null included/P.26>.05;222+215=437. Notation decision retained. | PASS_2_COMPLETE |
| S047 | EQ health30 −2.010 in [−5.559,1.540], null included/P.27>.05;281+250=531; C004 applies. | PASS_2_COMPLETE |
| S048 | PCS interaction.44 nonsignificant; distinct time-variation hypothesis, no covariance/df to reconstruct from two row CIs. C004 method scope applies. | PASS_2_COMPLETE |
| S049 | MCS interaction.84 nonsignificant; no contradiction with individual nonsignificant contrasts, no unreported joint covariance inferred. | PASS_2_COMPLETE |
| S050 | EQ-index interaction.10 nonsignificant; does not negate day7 P.02. C001 retains this distinct-null alternative without claiming an overall effect. | PASS_2_COMPLETE |
| S051 | EQ-health interaction.22 nonsignificant; day-specific CIs all include0, no exact joint test reconstruction supplied. | PASS_2_COMPLETE |
| S052 | PP RR1.00 in [.80,1.25] includes1; main P.98 can accompany rounded1.00. Duration definition differs from receipt98%, not a denominator conflict. | PASS_2_COMPLETE |
| S053 | Exclude-early RR.95 in [.76,1.19] includes1; stated form-window sensitivity is planned and robustness narrative matches. | PASS_2_COMPLETE |
| S054 | 30–44-day RR.99 in [.79,1.23] includes1; ascertainment window distinct from30-day event horizon; no endpoint substitution. | PASS_2_COMPLETE |
| S055 | Diary-only exclusion RR1.01 in [.81,1.26] includes1; planned ascertainment sensitivity, primary original estimate retained. | PASS_2_COMPLETE |
| S056 | Theatre-without-prior-SSI exclusion RR1.02 in [.82,1.27] includes1; exact planned definition and reported label match. | PASS_2_COMPLETE |
| S057 | Worst intervention/best control assignment RR1.19 in [.96,1.46] includes1; unfavorable direction, endpoint consistent with graphA100%. | PASS_2_COMPLETE |
| S058 | Best intervention/worst control assignment RR.89 in [.72,1.10] includes1; favorable direction, endpoint consistent with graphB100%. | PASS_2_COMPLETE |
| S059 | GraphA0% bar ordered, point contained, spans1; start near primaryRR consistent with missing-event axis; no numeric limit invented. | PASS_2_COMPLETE |
| S060 | GraphA5% bar ordered, point contained, spans1; increasing intervention-event assignment raises point. | PASS_2_COMPLETE |
| S061 | GraphA10% bar ordered, point contained, spans1; direction and nonsignificance caption agree. | PASS_2_COMPLETE |
| S062 | GraphA15% bar ordered, point contained, spans1; no threshold crossing of complete interval. | PASS_2_COMPLETE |
| S063 | GraphA20% bar ordered, point contained, spans1; directional progression agrees with intervention assignment. | PASS_2_COMPLETE |
| S064 | GraphA25% bar ordered, point contained, spans1; no plotted point outside its interval. | PASS_2_COMPLETE |
| S065 | GraphA30% bar ordered, point contained, spans1; caption's absence of significant control benefit agrees. | PASS_2_COMPLETE |
| S066 | GraphA35% bar ordered, point contained, spans1; no numerical CI/P cells claimed. | PASS_2_COMPLETE |
| S067 | GraphA40% bar ordered, point contained, spans1; direction rises and null remains inside. | PASS_2_COMPLETE |
| S068 | GraphA45% bar ordered, point contained, spans1; no new threshold or reference conflict. | PASS_2_COMPLETE |
| S069 | GraphA50% bar ordered, point contained, spans1; intervention missing-event increase has expected stated direction. | PASS_2_COMPLETE |
| S070 | GraphA55% bar ordered, point contained, spans1; caption and favorable<1 axis convention consistent. | PASS_2_COMPLETE |
| S071 | GraphA60% bar ordered, point contained, spans1; lower limit remains visibly below1. | PASS_2_COMPLETE |
| S072 | GraphA65% bar ordered, point contained, spans1; no claimed significant unfavorable treatment contrast. | PASS_2_COMPLETE |
| S073 | GraphA70% bar ordered, point contained, spans1; no estimate/interval direction conflict. | PASS_2_COMPLETE |
| S074 | GraphA75% bar ordered, point contained, spans1; null-line and caption agree. | PASS_2_COMPLETE |
| S075 | GraphA80% bar ordered, point contained, spans1; no numeric P or denominator inferred. | PASS_2_COMPLETE |
| S076 | GraphA85% bar ordered, point contained, spans1; increasing point does not establish significance while CI crosses1. | PASS_2_COMPLETE |
| S077 | GraphA90% bar ordered, point contained, spans1; unfavorable direction/reference convention agrees. | PASS_2_COMPLETE |
| S078 | GraphA95% bar ordered, point contained, spans1; lower end remains below null despite maximal assignments approached. | PASS_2_COMPLETE |
| S079 | GraphA100% bar ordered, point contained, spans1; endpoint matches extreme RR1.19 [.96,1.46] at visual precision, caption agrees. | PASS_2_COMPLETE |
| S080 | GraphB0% bar ordered, point contained, spans1; start near primaryRR consistent with control missing-event axis. | PASS_2_COMPLETE |
| S081 | GraphB5% bar ordered, point contained, spans1; increasing control-event assignment lowers point. | PASS_2_COMPLETE |
| S082 | GraphB10% bar ordered, point contained, spans1; direction and nonsignificance caption agree. | PASS_2_COMPLETE |
| S083 | GraphB15% bar ordered, point contained, spans1; no complete-interval crossing of null. | PASS_2_COMPLETE |
| S084 | GraphB20% bar ordered, point contained, spans1; point descends with stated assignment. | PASS_2_COMPLETE |
| S085 | GraphB25% bar ordered, point contained, spans1; no point outside its interval. | PASS_2_COMPLETE |
| S086 | GraphB30% bar ordered, point contained, spans1; favorable point does not imply significant effect. | PASS_2_COMPLETE |
| S087 | GraphB35% bar ordered, point contained, spans1; reference/axis convention agrees. | PASS_2_COMPLETE |
| S088 | GraphB40% bar ordered, point contained, spans1; no exact intermediate estimate/P invented. | PASS_2_COMPLETE |
| S089 | GraphB45% bar ordered, point contained, spans1; caption agrees with null containment. | PASS_2_COMPLETE |
| S090 | GraphB50% bar ordered, point contained, spans1; control missing-event increase reduces ratio as labeled. | PASS_2_COMPLETE |
| S091 | GraphB55% bar ordered, point contained, spans1; upper end visibly above1. | PASS_2_COMPLETE |
| S092 | GraphB60% bar ordered, point contained, spans1; no significant intervention benefit asserted by this bar. | PASS_2_COMPLETE |
| S093 | GraphB65% bar ordered, point contained, spans1; all direction conventions agree. | PASS_2_COMPLETE |
| S094 | GraphB70% bar ordered, point contained, spans1; no numeric CI/denominator inference. | PASS_2_COMPLETE |
| S095 | GraphB75% bar ordered, point contained, spans1; no threshold conflict with caption. | PASS_2_COMPLETE |
| S096 | GraphB80% bar ordered, point contained, spans1; progression remains below1 in point only. | PASS_2_COMPLETE |
| S097 | GraphB85% bar ordered, point contained, spans1; upper end remains above null. | PASS_2_COMPLETE |
| S098 | GraphB90% bar ordered, point contained, spans1; favorable direction and nonsignificance coexist. | PASS_2_COMPLETE |
| S099 | GraphB95% bar ordered, point contained, spans1; no stopping or superiority declaration contradicts bar. | PASS_2_COMPLETE |
| S100 | GraphB100% bar ordered, point contained, spans1; endpoint matches extreme RR.89 [.72,1.10] at visual precision, caption agrees. | PASS_2_COMPLETE |
| S101 | Contamination interaction.28>.05 matches no-heterogeneity narrative; four row intervals are distinct effect tests, df/covariance absent. | PASS_2_COMPLETE |
| S102 | Stoma interaction.14>.05 matches no-heterogeneity narrative; opposite-sided point estimates do not independently establish interaction. | PASS_2_COMPLETE |
| S103 | Procedure interaction.81>.05; all three row CIs include1, joint test not reconstructed from unreported covariance. | PASS_2_COMPLETE |
| S104 | BMI interaction.81>.05; incomplete BMI event subtotal does not identify a contradictory analysis denominator. | PASS_2_COMPLETE |
| S105 | Incision interaction.42>.05; shell exact15 boundary remains screened peripheral issue, no primary/key-result/decision-rule change demonstrated. | PASS_2_COMPLETE |
| S106 | Preparation interaction.68>.05; complete event subtotal112/108, no heterogeneity conclusion consistent. | PASS_2_COMPLETE |
| S107 | Country interaction.52>.05; UK and Australia events sum primary totals, no population attribution conflict. | PASS_2_COMPLETE |
| S108 | Assessment interaction.67>.05; raw ascertainment-rate differences compare methods, not treatment-by-method interaction. | PASS_2_COMPLETE |
| S109 | Pandemic interaction.68>.05; UK-only subgroup scope and79/73 subtotal match; no international denominator imposed. | PASS_2_COMPLETE |
| S110 | Individual1:1 allocation, minimisation covariates and random center match planned/reported level; center effect does not imply cluster randomization. | PASS_2_COMPLETE |
| S111 | SAP unstructured versus REPORT independent repeated covariance is the reproduced C004 specification comparison; working/other model level and robust-SE alternatives retained. | PASS_2_COMPLETE |
| S112 | Planned UK additive LOS contrast absent while REPORT geometric ratios present; C002 persists, including SAP transformation permission as alternative. No raw-median arithmetic claim. | PASS_2_COMPLETE |
| S113 | Literal participant indicators imply T=ΣT_iI_i and B=ΣB_iI_i; separate coefficients dependent. C005 is narrow parameterization/adjustment ambiguity; some fitted marginal contrasts remain estimable. | PASS_2_COMPLETE |
| S114 | .25×.60=.15, difference.10;2×336=672;336/.80=420. Diagnostic334.156 discrepancy below5% even holding probabilities fixed; source Stata implementation absent. | PASS_2_COMPLETE |
| S115 | Stated superiority/two-sided95%/.05 agrees with reported no evidence of reduction; no equivalence or noninferiority conclusion/margin inferred. | PASS_2_COMPLETE |
| S116 | 840 randomized−19 removed=821;399+398=797;797−9=788. Allocation-based complete cases and retained priorSSI after death/dropout explicitly stated; no census/imputation contradiction. | PASS_2_COMPLETE |
| S117 | Exclusive ascertainment additions109+0+3=112 and107+1+0=108; overlapping earlier sources are not summed. CDC/diary definitions and30-day horizon stated. | PASS_2_COMPLETE |
| S118 | SF12 scoring transforms/PCS-MCS aggregates read; P/BP and GHP/GH labels resolve in adjacent domain definitions. No raw item records; no reproduced numeric scoring conflict. | PASS_2_COMPLETE |
| S119 | Planned crosswalk/postdeath index0 and complete-item scoring distinguished from primary no-imputation wording; actual secondary coding absent, not contradicted. | PASS_2_COMPLETE |
| S120 | PP≥3days/early-discharge is planned, receipt98% is distinct; optional≥5days not affirmatively promised as mandatory. Reported PP RR/P/CI coherent. | PASS_2_COMPLETE |
| S121 | All six mandatory primary sensitivities plusPP displayed and include1; posthoc tipping supplement does not supplant original primary result. | PASS_2_COMPLETE |
| S122 | Nine reported subgroup families all in detailed SAP; protocol expressly delegates comprehensive analysis toSAP, so no absent prespecification finding. | PASS_2_COMPLETE |
| S123 | Substantive<15/≥15 versus shell≤15/>15 changes exactly15 allocation; REPORT follows substantive labels. Already-screened peripheral decision revisited; no demonstrated primary/key-result or formal rule change. | PASS_2_COMPLETE |
| S124 | Secondary safety heading still retains secondary status; wound/readmission definitions and same analyses persist. No promotion/demotion or changed composite reproduced for RouteA5. | PASS_2_COMPLETE |
| S125 | Planned SAE RR output absent, but SAE is nonkey secondary;158/411 and165/410 patients vs237/259 events explicitly distinguished and counts reconcile. | PASS_2_COMPLETE |
| S126 | Acceptability planned MD output/professional survey absent, but no abstract or designated-key outcome; no printed test or scale conflict beyond recoverable terminology. | PASS_2_COMPLETE |
| S127 | UK LOS analysis is present plus pooled extension; no claim of omitted UK population. Planned missing additive contrast and pooled presentation retained within C002. | PASS_2_COMPLETE |
| S128 | No multiplicity adjustment, final.05 and approximate interim.001 are source-stated; no realized stopping/interim output contradicts them. C001 cannot assume a hidden adjusted threshold. | PASS_2_COMPLETE |
| S129 | Feasibility70/6months/≥5sites and traffic-light ranges read; adherence24h differs from PP3days by definition. No realized threshold statistic supplied; no boundary-gap claim with a reported result. | PASS_2_COMPLETE |
| S130 | Primary RR CI/P and subgroup/sensitivity/tipping robustness agree; absence of reduction is not equivalence. QoL unqualified summary exception remains C001, not blanket reconciliation. | PASS_2_COMPLETE |
| S131 | Pain1–10 quantity/timepoints/−.41 contrast remain identifiable despite VAS/Likert names; lower pain/acceptability and higher QoL direction definitions coherent. | PASS_2_COMPLETE |
| S132 | UK economic analysis expressly separate; no economic estimate/conclusion in REPORT to contradict plan. Nonkey absent output alone outside mandatory primary/key analysis omission. | PASS_2_COMPLETE |
| S133 | SAP robust sandwich SE positive declaration, REPORT estimator not specified; absence alone no contrary estimator. Exact test/df/covariance limitation remains distinct from C004 positive covariance conflict. | PASS_2_COMPLETE |
| S134 | Prospective20% attrition versus actual52/840 missing primary is not one copied quantity; deaths with knownSSI remain available. No power-input inconsistency. | PASS_2_COMPLETE |
| S135 | Allowed assessment dates5–10/30–44 versus target day7/day30 and fixed30-day infection horizon distinguished; amended window/sensitivity language reconciles definitions. | PASS_2_COMPLETE |
| S136 | Plan permits LOS0 but no actual zero observations printed; REPORT log transformation does not establish log0 was evaluated. Cannot infer changed zero handling. | PASS_2_COMPLETE |
| S137 | Main no-difference QoL narrative vsday7P.02 remains C001; interaction.10/omnibus/final-time/clinical interpretation alternatives retained, no global longitudinal effect inferred. | PASS_2_COMPLETE |

## Stable candidate and mechanical-recheck reconciliation

All facts in verification/evidence_recheck.md were reviewed, including each cited location, source/comparator match, rule, calculation, input availability, alternative, observation/inference distinction, question, content roles and classification. Its 39 derivatives cover 18 exact pages plus three complete-document native checks. No transcription correction or additional conflicting location is established by pass 2.

| Stable ID | Pass-2 assessment of evidence and remaining question | Role/type/domain reconciliation |
|---|---|---|
| C001 | Main abstract/body broad QoL summaries and eTable3 day7P.02 confirmed; [.015,.025] stays below.05. Contextual negative endpoints reconcile the row itself. Nonsignificant interaction.10 tests time variation; an unprinted omnibus treatment test, final-time focus or clinical-importance summary remains a distinct alternative. No isolated-time result is claimed to prove global QoL efficacy. Ask the narrative's actual hypothesis/component/time. | REPORT versus REPORT; S_C; statistical_results; reproduced. SAP significance convention corroborates only, no P_R. |
| C002 | Both UK/pool geometric ratios confirmed; UK planned arithmetic/median differences absent in supplied results. SAP p15 permission through sensitivity is an alternative, not a supplied additive output. No absent UK population assertion. Ask replacement decision/amendment and planned difference result. | PLAN versus REPORT; P_R; protocol_report; reproduced. No independent P_P inferred from skewness contingencies or S_W from agreeing report copies. |
| C003 | Main affirmative predicted-survival exclusion confirmed against protocol's complete two-exclusion list and amendment context. Willing/able follow-up is not explicit predicted survival. No realized exclusion count/clinical effect inferred; ASA example does not create a separate quantitative finding. | PLAN versus REPORT; P_R; protocol_report; reproduced. Primary SSI population descriptor makes this in-focus, not calendar/administrative comparison. |
| C004 | Positive unstructured/independent declarations confirmed; every SF12/EQ contrast and interaction is affected method scope. Different model level, working covariance with sandwich inference or an amendment remains possible; no resulting numeric fitting change claimed. | PLAN versus REPORT; P_R; protocol_report; reproduced. Supplementary outputs corroborate affected values, add no S_C. |
| C005 | Literal fixed-indicator dependence reproduced conditionally, separate treatment/baseline coefficients need defined coding/constraints. Some fitted marginal contrasts can remain estimable; no universal absolute-contrast inestimability or actual fitted-report claim. Ask participant meaning and intended baseline-adjusted contrast. | PLAN-only same SAP; P_P; plan_material; reproduced. REPORT covariance/outputs do not introduce a conflicting party. |

## Rereview of every checker excluded-observation row

This table individually records all 29 source rows, in checker order, with exactly one present reason code. It is the complete pass-2 `Excluded observations` table; repeated observations across upstream checkers are revisited separately here because the contract requires every upstream row. No new F-ST2 observation is emitted. Checks that reconcile without an apparent issue are recorded in the per-S table, rather than added to this table. Route A1 is never treated as display rounding; A2–A4 require a reproduced numeric mismatch under the specified evidence and A5 requires the scoped planned/report status or analysis conflict.

| Location | Observation and pass-2 source/rule reassessment | Reason code |
|---|---|---|
| Numeric row1: REPORT mainp8; resultsp3–4 | Model-adjusted MD/RR/RD versus raw descriptive subtraction/ratio: mainp4 names adjustment and separate links; supplement names longitudinal interaction/randomcenter. No source says crude. A1–A4 printed contradiction is not demonstrated by this raw comparison; C004 separately covers method declaration. | MODEL_VERSUS_CRUDE |
| Numeric row2: REPORT mainp7 Table2 | Staffing totals446/429,445/433,425/416 exceed headers411/410; e.g.319/411=77.62% fits77.6%. Individual counts/percentages reconcile. Categories do not claim a mutually exclusive staffing partition; multiple grades can contribute. A3 cannot be reproduced without adding exclusivity. | CONDITIONAL_OR_UNREPORTED |
| Numeric row3: REPORT mainp8 and resultsp5 |73/71 participants versus84/83 complication types. Exact footnote counts multiple types separately; grade totals64+16+4=84 and59+17+7=83 reconcile. No A3 contradictory denominator for one quantity. | CONTEXT_RESOLVES |
| Numeric row4: REPORT resultsp6 eTable6 |Earlier37/43,4/7,38/25 overlap109/107 day30; explicit footnote and exclusive italic0/1 and3/0 give112/108. No A3 total contradiction after respecting source overlap. | CONTEXT_RESOLVES |
| Numeric row5: REPORT mainp3/p8 |All recorded deaths25(10/15) versus within30day24(10/14) are not explicitly identical horizons. p3 gives no30day restriction. Main values transcribed correctly but same-endpoint mismatch not reproduced; adjacent integer half-unit intervals alone do not substitute for endpoint matching. | NOT_REPRODUCED |
| Numeric row6: REPORT mainp9 |BMI109/103, incision111/103, assessment101/107 event subtotals versus112/108: figure labels events, not a claim every primary participant has each classificatory measure. No complete partition or subgroup denominator printed; A3 cannot be established by assuming it. | CONDITIONAL_OR_UNREPORTED |
| Numeric row7: REPORT mainpp5–7 |Smoking405/402, skin411/409, blood407/406 available totals differ from411/410 header denominators. Example220/411=53.527% matches53.5 and274/411=66.667% matches66.7. Header-based percentages and available counts are distinguishable; no A3 reproduced mismatch. | CONTEXT_RESOLVES |
| Cross row1: PLAN SAPp23; REPORT mainp4/resultsp4 |Postdeath EQindex0 is prescribed; primary complete-case sentence is not an EQ-specific statement that zero coding was omitted. Actual implementation missing, no changed outcome status or printed numeric contradiction; cannot create A5 by inference. | CONDITIONAL_OR_UNREPORTED |
| Cross row2: PLAN protocolpp24–25/SAPpp7,27; REPORT mainp8 |Wound/readmission heading changes to Secondary safety outcomes, retaining secondary status, definitions and contrasts. No reproduced promotion/demotion among primary/secondary/tertiary/exploratory/safety is established merely by a subdivision retaining Secondary. | TERMINOLOGY_OR_WORDING |
| Cross row3: PLAN SAPpp26–27,44/protocolpp25,27; REPORT mainp8 |Patient planned MD and professional survey absent; no abstract/designated-key status. Planned secondary status remains, so A5 status change is not reproduced and mandatory primary/key omission rule does not capture these missing contrasts. | CONDITIONAL_OR_UNREPORTED |
| Cross row4: PLAN protocolpp39–40/SAPp29; REPORT main |Economic details expressly documented separately in SAPp29; no economic REPORT value/conclusion conflicts. A5 does not mandate this nonkey separate output in clinical report. | CONTEXT_RESOLVES |
| Cross row5: REPORT mainpp4,6,8; PLAN protocolp2/SAPpp7,26 |VAS/Likert/10-point pain naming; explicit1–10 limits, day7/day30 and MD−.41 remain the same quantity. Amendment records collection-tool terminology correction. No number/sign/reference or outcome hierarchy changes for A2/A5. | TERMINOLOGY_OR_WORDING |
| Cross row6: REPORT mainp8/resultsp3 |PCS−.86 vs−.861, MCS−1.90 vs−1.904 and CI copies: half-unit intervals overlap, gap0 and relative gap0. No A1 null/P classification difference; display precision screens copied values. | ROUNDING_OR_DISPLAY_PRECISION |
| Cross row7: REPORT mainp4; PLAN protocolpp2,25–29/SAPp13,p32 |Target7–10 versus allowed5–10 assessment window; amendment expands window, schedule agrees. Distinct target versus allowable date does not change30-day infection horizon or establish A5 endpoint substitution. | CONTEXT_RESOLVES |
| Cross row8: PLAN protocolp17 |At-least5cm inclusion vs converted-open greater-than5cm procedural wording. Plan-internal procedural boundary does not demonstrate changed primary/key result, analysis-set size or formal statistical decision rule. A5 report-status/analysis conflict absent. | PERIPHERAL_COMPARISON |
| Cross row9: PLAN protocolp39/SAPp28; REPORT mainpp4,9 |Short protocol subgroup list vs detailed nine-family SAP: protocolp38 expressly delegates comprehensive methods; SAP contains reported skin/BMI/incision/assessment/pandemic families. A5 unsupported prespecification is not reproduced. | CONTEXT_RESOLVES |
| Cross row10: REPORT mainp8/resultsp5 |Participant grades53+16+4=73,47+17+7=71 vs complication-type grades64+16+4=84,59+17+7=83; supplement expressly counts multiple types. Same as numeric row3, still not an A3 contradictory quantity. | CONTEXT_RESOLVES |
| Statistical row1: PLAN SAPp9/protocolp38; REPORT mainp4 (S114) |Normal diagnostic334.156/arm vs336: allowing n[335.5,336.5] gives central diagnostic gap1.344/336=.004, below.05 before expanding displayed probability inputs.336/.8=420, target840 reproduces. A4 requires greater-than5% remaining discrepancy; no new finding. | ROUNDING_OR_DISPLAY_PRECISION |
| Statistical row2: REPORT mainp8 pooledLOS (S004) |Normal log-Wald P≈.39 vs.21 revisited. Interval includes1 and both P>.05, so no null classification conflict. Exact mixed-linear test, df, variance and CI construction absent. Other LOS row/continuous outcomes do not establish one common fitted df/test; diagnostic cannot prove A1 numerical incompatibility or A4 reproducing method. Ask missing output only if available, no new candidate solely from it. | CONDITIONAL_OR_UNREPORTED |
| Statistical row3: REPORT mainp8; PLAN SAPp25 (S009/S010) |RD normal diagnostic≈.41 vsrowP.96: SAP expressly assigns P to adjustedRR and separate identity/log models. RR1.02/.45–2.31 has diagnostic≈.96. No A1 interval/P conflict because mismatched estimands were being compared. | NOT_REPRODUCED |
| Statistical row4: PLAN SAPpp22–23 (S118) |PainP/BP and general-healthGHP/GH label changes resolve using immediately adjacent definitions/rescale formulas. No printed numeric score conflict is demonstrated from missing raw items; not A2 numeric slip. | TERMINOLOGY_OR_WORDING |
| Statistical row5: PLAN SAPpp17,28,46; REPORT mainp9 (S123) |Exactly15cm changes between shell≤15/>15 and substantive<15/≥15, while REPORT follows substantive labels. Already-screened F-XS-004 not re-emitted. Hypothesis-generating subgroup shell comparison remains peripheral absent changed primary/key overall result, analysis-population size or statistical decision rule. | PERIPHERAL_COMPARISON |
| Statistical row6: PLAN SAPpp27,45; REPORT mainp8 (S125) |SAE RR/CI/P planned but absent; SAE not abstract-reported/key. Patient/event distinctions reconcile. No status change or absent primary/key analysis under A5, and no printed inferential value conflict. | OUT_OF_FOCUS |
| Statistical row7: PLAN SAPpp27,44; REPORT mainp8 (S126) |Patient acceptability MD/CI/P planned but absent; nonkey secondary, same outcome status. Missing nonkey contrast is outside A5 mandatory primary/key-analysis omission, not evidence of numerical incompatibility. | OUT_OF_FOCUS |
| Statistical row8: REPORT mainpp4,6,8; PLAN SAPp26 (S131) |PainVAS/Likert wording resolves to same1–10 quantity/timepoints and declared favorable direction; exact MD/P do not change. No A2 printed numeric sign/digit issue. | TERMINOLOGY_OR_WORDING |
| Statistical row9: PLAN protocolpp39–40/SAPp29; REPORT main (S132) |Economic result absent from clinical REPORT but SAP documents it separately, not primary/key omission or a conflicting printed conclusion. No outcome status change reproduced. | OUT_OF_FOCUS |
| Statistical row10: PLAN SAPp26; REPORT mainp4 (S133) |Robust sandwich SE prescribed but not restated: report does not affirm a contrary estimator. Positive covariance comparison alreadyC004 is distinct. A1 needs actual incompatible quantities; no printed SE/statistic or contrary estimator supplied. | CONDITIONAL_OR_UNREPORTED |
| Statistical row11: PLAN SAPpp18,25; REPORT mainp4 (S136) |LOS0 possible versus actual log transformation: actual zero observations/handling absent. Cannot show a logarithm applied to0 or conflicting fitted number without assuming cases occurred; not A4 reproducing method. | CONDITIONAL_OR_UNREPORTED |
| Statistical row12: REPORT mainp8/resultsp3–4 (S005/S006/S038–S047) |Raw armmeans do not reproduce adjusted longitudinal differences; sources explicitly declare baseline/minimisation adjustment and treatment×time. No crude label; does not screen any independent interval/P conflict, including C001. | MODEL_VERSUS_CRUDE |

## Previously screened findings: independent revisit for the auditor

F-ST1-001 is already recorded SCREENED_OUT as NOTATION_OR_TYPOGRAPHY, so it is not re-emitted. The exact p4 image confirms the three strings rather than an OCR-only issue. Taking index day7 endpoints as−.104 and−.010 gives midpoint−.057 and significantP.02. Taking health day7 upper limit as+4.557 gives midpoint1.084 and nonsignificantP.54; health day21 upper+1.597 gives midpoint−2.1645 (rounding to the printed−2.164 is possible) and nonsignificantP.26. The immediate rows identify the sign/separator meanings; no digit needs changing. A forced uniform separator parse creates a conflict, but does not establish a substantive printed numeric reading at the inclusion threshold. These exact strings and contextual alternatives are preserved for the auditor; an independently reproduced sign/interval conflict would invoke RouteA1 and could not be screened as rounding.

F-XS-004 is already recorded SCREENED_OUT as PERIPHERAL_COMPARISON, so it is not re-emitted. SAP substantive pp17/28 assigns exactly15 to≥15; shellp46 assigns it to≤15; REPORTp9 uses<15/≥15. The discrepancy is real and quantity-changing at that boundary. However it is PLAN-internal secondary hypothesis-generating subgroup-shell detail, not a supplied change to primary/key overall outcome, total analysis-set size, or formal statistical decision rule. No exact15 participant count or implementation is inferred. Auditor should retain both exact operators while applying the comparison tier and avoid calling it merely a typographic sign issue. The other eight screening INCLUDE rows retain all source locations and consolidate into the existing five stable issues; no suppressed additional pattern is identified.

## Limitations and completion

All137S records, all5C IDs, all10 screening decisions, all29 upstream excluded rows and all recheck facts have explicit pass-2 coverage. No scientific unit assigned to this stage remains unread. Source values and reused derivatives were preserved. Exact-P/variance reconstruction is limited by missing model test statistics, df, fitted covariance/variance output and unrounded coefficients; graphical intermediate tipping limits are not numeric cells. Candidate questions preserve the unsupplied model syntax, coding/constraints and analysis amendment definitions. No actual GPU OCR was needed by this stage. No new finding requires a pass-2 screener. Inclusion audit and every disposition remain the responsibility of subsequent audit/human adjudication, respectively.
