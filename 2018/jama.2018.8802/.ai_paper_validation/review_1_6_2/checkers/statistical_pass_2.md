# Statistical pass 2 — Workflow 1.6.2

Runtime agent: /root/stat2. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. This runtime differs from /root/stat1. PASS_2_COMPLETE.

Scope: every stable statistical relationship S001 through S120, the complete current ledger C001, C002, C003, C004, all ten initial screening rows, every mechanical recheck fact, and all 36 prior checker exclusion rows: numeric 9, numeric-tail 8, cross-source 10, statistical pass 1 9. The complete scope and review contract were read. Current main/support quantitative maps supplied matching locations; no legacy scientific conclusions or external source was used. Main article and results supplement are REPORT; prospective protocol is PLAN.

Direct source text was reread with CPU `pdftotext -layout`, Poppler 25.03.0: results supplement PDF pp.5–9 and protocol p.17, to stdout without new derivatives. Existing exact-source recheck text and visual-confirmation facts cover main pp.1,3–8, protocol pp.16,18–19 and results supplement p.2. The source-linked reusable image DOC-003-p06.png was viewed to confirm all eTable 3 signs, columns and P values. Historical image renderer/version is unrecorded; direct current-PDF text independently confirms its values. Numerical diagnostic arithmetic used JavaScript; no Python, OCR, new rendering, source mutation, asset mutation or nested agent was used. Existing recheck extraction/rendering provenance remains in preprocessing/recheck_derivative_record.md.

Results: 120 of 120 S records revisited and marked PASS_2_COMPLETE while retaining PASS_1_COMPLETE; one fresh finding, F-ST2-001; one newly excluded apparent observation. All 36 prior exclusions remain screened out after the row-specific checks below. No already-screened finding is re-emitted. Exact model variance, test construction, rank, event-time and patient-opportunity reconstruction remain limited by named unavailable inputs. Every candidate remains Pending Human Adjudication.

## Findings

### F-ST2-001

**Title:** Three-month vascular-death adjusted difference, interval and P value do not reconcile under the two-sided normal-Wald relationship supported by the other eTable 3 difference rows.

**Relationships:** S059, S117. Proposed primary relationship type S_W; all relationships S_W.

**Compared locations and document roles:** REPORT [results supplement PDF p.6, eTable 3, 3-month vascular-death row, absolute-difference and its adjacent P columns](../../../joi180070supp2_prod.pdf#page=6); REPORT [p.7, adjustment footnote](../../../joi180070supp2_prod.pdf#page=7); REPORT [main PDF p.4, Data Analysis confidence level and two-sided test rule](../../../jama_wang_2018_oi_180070.pdf#page=4). All twelve rows in the same p.6 absolute-difference display supply the empirical comparison pattern; their separate HR columns are not substituted. Only the p.6 estimate/CI/P tuple conflicts, making the proposed issue S_W, rather than S_C merely because the main report supplies its inferential rule.

**Printed values:** Intervention 46/2400 (1.9%) and control 67/2400 (2.8%); adjusted absolute difference −1.43 percentage points, 95% CI −2.33 to −0.54, adjacent P=0.001. Separate HR .62 (95% CI .42–.92), P=.02. The source states adjustment for listed patient/hospital characteristics, 95% confidence intervals, and two-sided testing. Both the printed difference CI and P support significance; the issue concerns quantitative estimate/interval/P compatibility rather than a null-crossing reversal.

**Rule and calculation:** The two-sided normal-Wald relationship uses q=1.95996398454, SE=(U−L)/(2q), z=|b|/SE, and P=2Φ(−|z|). Here SE=.45664104, z≈3.13156257, and P≈.00173892. This is explicitly a diagnostic reconstruction of an unreported CI/test construction, not a claim to recreate patient-level model estimation. The source does not name a difference-specific test or CI formula. The same relationship nevertheless reproduces every other absolute-difference P in this same display within that row's printed-input intervals, as documented individually below; therefore it is empirically supported by this display rather than selected from convention alone.

**Printed-input interval calculation:** b∈[−1.435,−1.425], L∈[−2.335,−2.325], U∈[−.545,−.535]. Allowing these inputs independently is conservative: width∈[1.780,1.800], so SE∈[.45408998,.45919212] and |z|∈[3.10328,3.16017]. The attainable diagnostic P interval is approximately [.00157692,.00191404]. Printed P=.001 has half-unit interval [.0005,.0015]. The minimum gap is .00007692 and relative gap against .001 is .07692, above .05. Imposing exact symmetric-Wald centering can only narrow the conservative envelope, not bridge the gap. Numerical normal-tail evaluation approximation is below 2×10⁻⁷ here, much smaller than the gap. Route A category 1 interval/test compatibility is not screened out by display precision; the complete half-unit calculation is supplied to show that the numerical discrepancy persists even when the source's rounding allowances are applied.

**Empirical support from all comparison rows:** Every other difference row has overlapping recomputed and printed P intervals under the same two-sided normal-Wald relationship. All estimates and interval endpoints in this table are allowed ±.005; printed P values get ±.005 at two decimal places or ±.0005 at three decimal places. These independently varying input envelopes are conservative and are not adjusted-model/raw-count comparisons.

| S record; eTable 3 difference row | Central diagnostic P | P envelope from printed-input half units | Printed P interval | Comparison |
|---|---:|---|---|---|
| S053; ischemic stroke 3 months | .402683 | [.396798,.408576] | [.395,.405] | Overlap |
| S055; hemorrhagic stroke 3 months | .228788 | [.218143,.239604] | [.225,.235] | Overlap |
| S057; myocardial infarction 3 months | .459537 | [.428638,.490435] | [.475,.485] | Overlap |
| S059; vascular death 3 months | .001739 | [.001577,.001914] | [.0005,.0015] | Gap .00007692 |
| S061; ischemic stroke 6 months | .053315 | [.051641,.055022] | [.045,.055] | Overlap |
| S063; hemorrhagic stroke 6 months | .372987 | [.359118,.386924] | [.375,.385] | Overlap |
| S065; myocardial infarction 6 months | .854212 | [.827605,.880160] | [.855,.865] | Overlap |
| S067; vascular death 6 months | .041667 | [.039733,.043661] | [.035,.045] | Overlap |
| S069; ischemic stroke 12 months | .025094 | [.024256,.025950] | [.025,.035] | Overlap |
| S071; hemorrhagic stroke 12 months | .803450 | [.789812,.816933] | [.795,.805] | Overlap |
| S073; myocardial infarction 12 months | .446906 | [.422667,.471171] | [.445,.455] | Overlap |
| S075; vascular death 12 months | .003970 | [.003744,.004206] | [.0035,.0045] | Overlap |

**Focus area:** B, estimate and test logic. **Proposed review domain:** statistical_results.

**Qualifying route:** Route A, category 1 — a P value that does not belong to the printed estimate and interval under a same-display supported inferential reconstruction. This is not the small-P display-zero exclusion, and no P=0 is printed.

**Affected result or extracted value:** The three-month vascular-death adjusted absolute-difference P=.001 and its relationship to the paired 95% CI; downstream extraction of the numerical P and inferential precision. This finding does not claim a change in the printed significance conclusion.

**Why context does not resolve it:** Route A category 1 covers reproduced interval/test conflicts. The same display's other eleven difference rows support the named relationship after their input rounding, while this row remains outside its printed P interval. Neither the separate HR/P nor the adjustment footnote identifies a different difference-specific CI/test construction for this row. The normal-Wald diagnostic is not asserted as the actual undisclosed method; the supported numerical incompatibility and missing construction are the human question.

**Source-grounded alternatives and missing definition:** The P value may come from a different test, variance estimator, confidence construction, dataset or estimand than the displayed difference interval. A non-Wald interval or a separately adjusted test could supply an explanation. None is specified for this row or distinguished from the other rows. Difference-specific CI/test construction, covariance output and patient/event data are absent. No intended P, interval endpoint, production mechanism or preferred analysis is proposed.

**Exact human question:** Which confidence-interval and testing procedures produced the three-month vascular-death adjusted difference −1.43 (−2.33 to −0.54) and P=.001, and how does that pairing reconcile with the two-sided normal-Wald relationship that reproduces the other eleven absolute-difference rows in the same display?

## Registered-candidate implications after recheck

| Stable ID | S records directly involved | Pass-2 review of mechanical facts and implications |
|---|---|---|
| C001 | S100,S104,S105 | The source-confirmed total-over-total versus patient-average composite definitions remain algebraically distinct: their difference is Cov(k,p)/mean(k). No individual k or p is supplied, so no actual trial-value difference is claimed. Opportunity-level ORPA does not identify weighting of the descriptive mean or adjusted difference. PLAN versus main REPORT gives P_R; results-supplement REPORT versus main REPORT gives S_C; P_R has precedence and protocol_report agrees. No re-emission. |
| C002 | S106,S108,S116 | Figure counts sum 3980, text primary-analysis total is4800, and Table 2 all-or-none denominators are2400 each. The conservative total gap818.5/4800=.17052 exceeds .05. Follow-up arithmetic reconciles; the primary-analysis labels do not. Available mRS3949 versus generic follow-up3980 is a distinct assessment-set definition, not another implied primary-count conflict. S_W/statistical_results agrees with the count-domain rule. No computational exclusion is inferred. No re-emission. |
| C003 | S109,S112,S120 | Exact sources attach the same Table 3 results to discharge and symptom onset. Report outcome definitions, Cox methods, disability footnote and both figure axes use onset. Median hospital stays do not convert the individual origins. PLAN corroborates onset but does not add a conflicting P_R relationship. S_W/report_internal_inconsistency agrees. No event-date reanalysis or extra issue is inferred. No re-emission. |
| C004 | S035,S036,S117 | Direct source confirms positive .2 upper endpoint and adjacent P=.009; 95% CI includes0 and P remains below.05 for every displayed half-unit bound. The separate HR(.90–1.02), P=.14 is internally compatible and may explain the narrative. Route A1 remains; difference-interval midpoint and normal-width diagnostics are the same issue, not a second candidate. S_W/statistical_results agrees. No re-emission. |

All four recheck evidence states are reproduced; source classifications were confirmed without transcription correction. This table records pass-2 scientific implications, not an inclusion audit or a human disposition. New finding F-ST2-001 awaits a fresh independent pass-2 inclusion screen before any registration.

## Explicit completion for every S relationship

Locations and exact tuples remain in the canonical relationship inventory; the table below documents the separate pass-2 reasoning record without duplicating the main full-text locator appendix. In each tuple check, interval order, containment, direction, null crossing and paired test are assessed independently. Unavailable exact model construction never means that a relationship was skipped. Count/percentage, matched copy and eligible-population implications were reviewed against the complete numeric inventory and current maps. References to a reconciled tuple mean the supplied checks reconcile, not that raw model output was recreated.

| S ID | Pass-2 check and implication | Completion |
|---|---|---|
| S001 | Composite difference contains point/excludes0, P=.02; precision copies overlap; C001 weighting remains separate. | PASS_2_COMPLETE |
| S002 | Composite ORPA contains point/excludes1, P=.003; opportunity-level GEE does not equal a crude ratio. | PASS_2_COMPLETE |
| S003 | All-or-none difference contains point/includes0, P=.06; copies overlap and no success claimed for this endpoint. | PASS_2_COMPLETE |
| S004 | All-or-none ORPA contains point/includes1, P=.31; full2400 denominators identify C002 comparator. | PASS_2_COMPLETE |
| S005 | IV rtPA difference ordered/contained/includes0, P=.26;212/204 eligible denominators match. | PASS_2_COMPLETE |
| S006 | IV rtPA ORPA ordered/contained/includes1, P=.06; separate test from S005. | PASS_2_COMPLETE |
| S007 | Early antithrombotic difference ordered/contained/includes0, P=.10; count fractions reconcile. | PASS_2_COMPLETE |
| S008 | Early antithrombotic ORPA ordered/contained/includes1, P=.07; adjusted GEE quantity retained. | PASS_2_COMPLETE |
| S009 | Dysphagia difference ordered/contained/includes0, P=.41; eligibility differs legitimately by arm. | PASS_2_COMPLETE |
| S010 | Dysphagia ORPA ordered/contained/includes1, P=.10; no count-ratio substitution. | PASS_2_COMPLETE |
| S011 | DVT difference ordered/contained/excludes0, P=.01; favorable effect supports narrative. | PASS_2_COMPLETE |
| S012 | DVT ORPA ordered/contained/excludes1, P=.04; both primary DVT tests significant. | PASS_2_COMPLETE |
| S013 | Discharge-antithrombotic difference ordered/contained/includes0, P=.09. | PASS_2_COMPLETE |
| S014 | Discharge-antithrombotic ORPA ordered/contained/includes1, P=.10. | PASS_2_COMPLETE |
| S015 | AF-anticoagulation difference ordered/contained/includes0, P=.18;155/137 eligible populations retained. | PASS_2_COMPLETE |
| S016 | AF-anticoagulation ORPA ordered/contained/includes1, P=.23. | PASS_2_COMPLETE |
| S017 | Lipid-lowering difference ordered/contained/includes0, P=.25; detailed eligibility resolves brief label. | PASS_2_COMPLETE |
| S018 | Lipid-lowering ORPA ordered/contained/includes1, P=.40. | PASS_2_COMPLETE |
| S019 | Antihypertensive difference ordered/contained/includes0, P=.07. | PASS_2_COMPLETE |
| S020 | Antihypertensive ORPA ordered/contained/includes1, P=.10; adjusted estimand retained. | PASS_2_COMPLETE |
| S021 | Antidiabetic difference ordered/contained/excludes0, P=.02; narrative significant measure matches. | PASS_2_COMPLETE |
| S022 | Antidiabetic ORPA ordered/contained/excludes1, P=.02. | PASS_2_COMPLETE |
| S023 | Vascular3mo difference ordered/contained/excludes0, P=.007; abstract precision overlaps, C003 time origin retained. | PASS_2_COMPLETE |
| S024 | Vascular3mo HR ordered/contained/excludes1, P=.002; Cox effect not crude event ratio. | PASS_2_COMPLETE |
| S025 | Vascular6mo difference ordered/contained/excludes0, P=.02; more precise abstract values overlap. | PASS_2_COMPLETE |
| S026 | Vascular6mo HR ordered/contained/excludes1, P=.004. | PASS_2_COMPLETE |
| S027 | Vascular12mo difference ordered/contained/excludes0, P=.005; precision copies overlap. | PASS_2_COMPLETE |
| S028 | Vascular12mo HR ordered/contained/excludes1, P<.001; Figure2A duplicate matches. | PASS_2_COMPLETE |
| S029 | Disability3mo difference ordered/contained/excludes0, P=.01;2180/2105 alive/available denominators retained. | PASS_2_COMPLETE |
| S030 | Disability3mo OR ordered/contained/excludes1, P=.002; binary mRS3–5 model retained. | PASS_2_COMPLETE |
| S031 | Disability6mo difference ordered/contained/excludes0, P=.006;2058/2009 denominators retained. | PASS_2_COMPLETE |
| S032 | Disability6mo OR ordered/contained/excludes1, P=.002. | PASS_2_COMPLETE |
| S033 | Disability12mo difference ordered/contained/excludes0, P=.02;1852/1798 denominators are not enrolled populations. | PASS_2_COMPLETE |
| S034 | Disability12mo OR ordered/contained/excludes1, P=.01. | PASS_2_COMPLETE |
| S035 | CI[−1.1,+.2] contains0 and paired P=.009; exact-source C004 retained, no duplicate finding. | PASS_2_COMPLETE |
| S036 | In-hospital HR(.90–1.02) includes1, P=.14; separate effect reconciles and may support narrative. | PASS_2_COMPLETE |
| S037 | Death3mo difference ordered/contained/includes0, P=.08. | PASS_2_COMPLETE |
| S038 | Death3mo HR ordered/contained/includes1, P=.23. | PASS_2_COMPLETE |
| S039 | Death6mo difference ordered/contained/includes0, P=.38; model direction may differ from crude counts. | PASS_2_COMPLETE |
| S040 | Death6mo HR ordered/contained/includes1, P=.81;103 versus101 crude counts do not contradict adjusted HR. | PASS_2_COMPLETE |
| S041 | Death12mo upper endpoint−0.0 is displayed zero; P=.05 is nonsignificant under strictP<.05; no hidden sign inferred. | PASS_2_COMPLETE |
| S042 | Death12mo HR ordered/contained/includes1, P=.21; Figure2B matches. | PASS_2_COMPLETE |
| S043 | Age availability comparison P=.81; medians/IQR do not supply ranks for exact Wilcoxon recreation. | PASS_2_COMPLETE |
| S044 | Male2497/3949 vs546/851; prior Pearson diagnostic≈.610 matches .61; no CI/test conflict. | PASS_2_COMPLETE |
| S045 | Prior stroke1137/3949 vs251/851; Pearson diagnostic≈.682 matches .68. | PASS_2_COMPLETE |
| S046 | Diabetes890/3949 vs196/851; Pearson diagnostic≈.755 compatible with .75 at display precision. | PASS_2_COMPLETE |
| S047 | Hypertension2552/3949 vs538/851; Pearson diagnostic≈.438 matches .44. | PASS_2_COMPLETE |
| S048 | Dyslipidemia285/3949 vs62/851; Pearson diagnostic≈.944 matches .94; baseline cross-copy is peripheral. | PASS_2_COMPLETE |
| S049 | CAD/MI512/3949 vs97/851; Pearson diagnostic≈.213 matches .21. | PASS_2_COMPLETE |
| S050 | AF200/3949 vs45/851; Pearson diagnostic≈.788 matches .79. | PASS_2_COMPLETE |
| S051 | Smoking1736/3949 vs380/851; Pearson diagnostic≈.712 matches .71. | PASS_2_COMPLETE |
| S052 | NIHSS3(2–6) each and P=.99; medians do not imply equal rank distributions; raw ranks unavailable. | PASS_2_COMPLETE |
| S053 | Ischemic3mo difference CI contains0/P=.40; same-display normal diagnostic envelope overlaps printed P. | PASS_2_COMPLETE |
| S054 | Ischemic3mo HR CI contains1/P=.59; adjusted Cox model retained. | PASS_2_COMPLETE |
| S055 | Hemorrhagic3mo difference CI contains0/P=.23; normal envelope overlaps. | PASS_2_COMPLETE |
| S056 | Hemorrhagic3mo HR CI contains1/P=.68. | PASS_2_COMPLETE |
| S057 | MI3mo difference CI contains0/P=.48; point rounding broadens normal envelope to include printed P. | PASS_2_COMPLETE |
| S058 | MI3mo HR CI contains1/P=.48;3 versus5 events do not recreate adjusted Cox inference. | PASS_2_COMPLETE |
| S059 | Vascular-death3mo CI excludes0/P=.001 but quantitative Wald compatibility fails after all half units: F-ST2-001. | PASS_2_COMPLETE |
| S060 | Vascular-death3mo HR CI excludes1/P=.02; separate HR does not replace S059 paired difference test. | PASS_2_COMPLETE |
| S061 | Ischemic6mo difference CI includes0/P=.05; strict threshold reconciles and normal P envelope overlaps. | PASS_2_COMPLETE |
| S062 | Ischemic6mo HR CI excludes1/P=.04; different estimand/test from S061. | PASS_2_COMPLETE |
| S063 | Hemorrhagic6mo difference CI contains0/P=.38; normal envelope overlaps after half units. | PASS_2_COMPLETE |
| S064 | Hemorrhagic6mo HR CI contains1/P=.80. | PASS_2_COMPLETE |
| S065 | MI6mo difference CI contains0/P=.86; normal envelope overlaps, equal raw8/8 does not force adjusted difference0. | PASS_2_COMPLETE |
| S066 | MI6mo HR CI contains1/P=.64; no crude substitution. | PASS_2_COMPLETE |
| S067 | Vascular-death6mo difference CI excludes0/P=.04; normal envelope overlaps. | PASS_2_COMPLETE |
| S068 | Vascular-death6mo HR CI contains1/P=.16; separate difference/ratio significance is not paired CI/P conflict. | PASS_2_COMPLETE |
| S069 | Ischemic12mo difference CI excludes0/P=.03; normal envelope overlaps. | PASS_2_COMPLETE |
| S070 | Ischemic12mo HR CI excludes1/P=.01. | PASS_2_COMPLETE |
| S071 | Hemorrhagic12mo difference CI contains0/P=.80; normal envelope overlaps. | PASS_2_COMPLETE |
| S072 | Hemorrhagic12mo HR CI contains1/P=.96; adjusted point1.02 does not require equality to raw23/24 ratio. | PASS_2_COMPLETE |
| S073 | MI12mo difference CI contains0/P=.45; normal envelope overlaps. | PASS_2_COMPLETE |
| S074 | MI12mo HR CI contains1/P=.43. | PASS_2_COMPLETE |
| S075 | Vascular-death12mo difference CI excludes0/P=.004; normal envelope overlaps. | PASS_2_COMPLETE |
| S076 | Vascular-death12mo HR CI excludes1/P=.02; event components allowed to overlap patients. | PASS_2_COMPLETE |
| S077 | Sensitivity composite difference CI excludes0/P<.001; contraindication-inclusive definition matches strategy. | PASS_2_COMPLETE |
| S078 | Sensitivity composite ORPA CI excludes1/P=.003; narrative's P refers to this ratio. | PASS_2_COMPLETE |
| S079 | Sensitivity rtPA difference CI contains0/P=.27;254/238 denominators include contraindications. | PASS_2_COMPLETE |
| S080 | Sensitivity rtPA ORPA CI contains1/P=.13. | PASS_2_COMPLETE |
| S081 | Sensitivity early-antithrombotic difference CI excludes0/P=.02;2400 each denominators retained. | PASS_2_COMPLETE |
| S082 | Sensitivity early-antithrombotic ORPA CI excludes1/P=.03. | PASS_2_COMPLETE |
| S083 | Sensitivity dysphagia difference CI contains0/P=.36; unchanged denominator alone supplies no contradiction. | PASS_2_COMPLETE |
| S084 | Sensitivity dysphagia ORPA CI contains1/P=.17. | PASS_2_COMPLETE |
| S085 | Sensitivity DVT difference CI excludes0/P=.01;672/606 denominators match expanded eligibility. | PASS_2_COMPLETE |
| S086 | Sensitivity DVT ORPA CI contains1/P=.07; separate estimand/test from S085. | PASS_2_COMPLETE |
| S087 | Sensitivity discharge-antithrombotic difference CI excludes0/P=.03; percentage discrepancy is within .05 rule. | PASS_2_COMPLETE |
| S088 | Sensitivity discharge-antithrombotic ORPA CI includes1/P=.05; strict threshold reconciles. | PASS_2_COMPLETE |
| S089 | Sensitivity AF difference CI contains0/P=.12; endpoint29.3 has its printed one-decimal precision. | PASS_2_COMPLETE |
| S090 | Sensitivity AF ORPA CI contains1/P=.29; count/percentage is within display precision. | PASS_2_COMPLETE |
| S091 | Sensitivity lipid difference CI contains0/P=.28; count/percentage within display precision. | PASS_2_COMPLETE |
| S092 | Sensitivity lipid ORPA CI contains1/P=.63. | PASS_2_COMPLETE |
| S093 | Sensitivity antihypertensive difference CI contains0/P=.07. | PASS_2_COMPLETE |
| S094 | Sensitivity antihypertensive ORPA CI contains1/P=.07. | PASS_2_COMPLETE |
| S095 | Sensitivity antidiabetic difference CI excludes0/P=.007; count/percentage within .05 display rule. | PASS_2_COMPLETE |
| S096 | Sensitivity antidiabetic ORPA1.59 CI1.11–2.23 excludes1/P=.01; geometric-centering gap relative.00402≤.05. | PASS_2_COMPLETE |
| S097 | Hemorrhage1/46 versus2/23 percentages match; Fisher diagnostic≈.25593 reproduces .26, generic χ² text lacks implementation; no same-display supporting χ² rows. | PASS_2_COMPLETE |
| S098 | Figure2A HR/CI/P copies Table3; curves and decreasing risk sets agree; event times prevent exact log-rank reconstruction. | PASS_2_COMPLETE |
| S099 | Figure2B HR/CI/P copies Table3; CI includes1/P=.21; censoring/risk sets do not equal enrollment or crude events. | PASS_2_COMPLETE |
| S100 | Power inputs agree plan/report;40×120=4800; composite variance/equation/cluster-size assumptions absent, no supported binary formula imposed. | PASS_2_COMPLETE |
| S101 | Hospital randomization and GEE within-hospital dependence agree; no independent/paired design conflict supplied. | PASS_2_COMPLETE |
| S102 | Nine measures and composite/all-or-none remain primary adherence definitions; detailed eligibility resolves brief wording; C001 weights separate. | PASS_2_COMPLETE |
| S103 | Either-co-primary positive rule met by composite only; no adjustment explicitly stated; no conflicting planned multiplicity rule. | PASS_2_COMPLETE |
| S104 | Aggregate and patient-average primary definitions remain distinct; C001 source facts/recheck confirmed; no actual data-value gap claimed. | PASS_2_COMPLETE |
| S105 | Opportunity5/7 example gives3 ones+2 zeros=5; not trial nine-measure replacement; ORPA not crude average. | PASS_2_COMPLETE |
| S106 | C002 labels/counts retained:3980 versus4800 exceeds .05; underlying follow-up arithmetic coherent. | PASS_2_COMPLETE |
| S107 | Plan allows identified adjustment variables; report supplies full patient/hospital list, no conflicting fixed planned list. | PASS_2_COMPLETE |
| S108 | Imputation examples concern baseline covariates;3949 available=3650 alive-mRS+299 deaths; not3980 generic completion. | PASS_2_COMPLETE |
| S109 | C003 discharge versus onset origin confirmed; no individual-date conversion possible. | PASS_2_COMPLETE |
| S110 | Binary mRS3–5, OR, logistic and mixed-model binary descriptions can coexist; no supplied incompatible model output. | PASS_2_COMPLETE |
| S111 | Four vascular components and patient-overlap footnote explain sum greater than composite; no disjoint-count assumption. | PASS_2_COMPLETE |
| S112 | Planned secondary outcome status and reported outcome definitions match; exploratory interpretation does not itself replace status. | PASS_2_COMPLETE |
| S113 | Contraindication-inclusive sensitivity implemented; plan does not explicitly name a distinct all-or-none sensitivity contrast. | PASS_2_COMPLETE |
| S114 | Sensitivity narrativeP=.003 matches ORPA; differenceP<.001 belongs separate effect;80.91 versus80.9 precision overlaps. | PASS_2_COMPLETE |
| S115 | Mann–Whitney and Wilcoxon rank-sum consistent; descriptive medians do not assert a conflicting normality rule. | PASS_2_COMPLETE |
| S116 | Availability totals3949+851=4800; baseline NIHSS/dyslipidemia copy discrepancies are peripheral and within-display percentages reconcile. | PASS_2_COMPLETE |
| S117 | All86 tuples revisited; C004 null-crossing mismatch retained; F-ST2-001 quantitative P/CI reconstruction additionally identified; separate tests respected. | PASS_2_COMPLETE |
| S118 | Four30-patient batches and three intervening feedback cycles explain120; report weekly monitoring compatible. | PASS_2_COMPLETE |
| S119 | Enrollment cap2400/group met; administrative termination remit is not a printed efficacy interim rule; no NI/equivalence margin or conclusion supplied. | PASS_2_COMPLETE |
| S120 | Planned/reported Cox and KM compatible; log-rank caption is separate test mapping with matching significance; missing event times limit exact recreation. | PASS_2_COMPLETE |

## Reassessment of every prior checker exclusion

The row keys below identify each prior table row by checker and position, not a new finding or candidate ID. Each was reread against route A categories 1–5, the .05 display-precision rule and route B. Retain means the apparent issue remains screened out under the one named scope code. No excluded row conceals a reproduced route A observation requiring a fresh finding. The new S059 observation was absent from these exclusion tables and from the initial screening log.

| Prior row | Exact source scope / apparent issue | Pass-2 disposition | Reason code |
|---|---|---|---|
| Numeric row1 | MAIN p.6, CAD311/2400 printed13.05% | Retain: recomputed[12.9348,12.9819]% versus[13.045,13.055]%, gap ratio.004837≤.05; category3 threshold not met. | ROUNDING_OR_DISPLAY_PRECISION |
| Numeric row2 | SUPP p.8 control antithrombotic/AF/lipid/diabetes fractions | Retain: antithrombotic remaining relative gap≈.000025; others' half-unit intervals overlap. No category3 discrepancy above.05. | ROUNDING_OR_DISPLAY_PRECISION |
| Numeric row3 | MAIN p.6 vs SUPP p.5 dyslipidemia596 vs347 | Retain: baseline copies across displays, full population unchanged; each display's counts/percentages reconcile. | PERIPHERAL_COMPARISON |
| Numeric row4 | MAIN p.6 vs SUPP p.5 NIHSS4 vs3 | Retain: descriptive baseline medians across different stratifications; no primary/key-secondary result or population size changed. | PERIPHERAL_COMPARISON |
| Numeric row5 | MAIN p.6 baseline801 vs SUPP p.2 nominal20×40 | Retain: product half-unit interval[770.25,830.25] overlaps[800.5,801.5]; fixed nominal discrepancy1/801 also below.05. | ROUNDING_OR_DISPLAY_PRECISION |
| Numeric row6 | MAIN Tables2/3 and SUPP eTables3/4 adjusted vs crude effects | Retain: source explicitly adjusted; no crude/unadjusted label or same-display method reproducing these adjusted quantities from crude counts. | MODEL_VERSUS_CRUDE |
| Numeric row7 | PLAN p.17 three cycles versus p.13 four batches | Retain: Figure4 distinguishes four30-patient collections from three feedback loops;120 count reconciles. | CONTEXT_RESOLVES |
| Numeric row8 | MAIN p.4/PLAN p.19 illustrative5of7 versus nine measures | Retain: expressly hypothetical eligible patient;3+2=5; not a realized trial denominator or outcome-status change. | CONTEXT_RESOLVES |
| Numeric row9 | MAIN p.4/PLAN p.17 missing power inputs | Retain: composite SD/equation/size imbalance absent; no same-display supported power method or conflicting supplied inputs. | CONDITIONAL_OR_UNREPORTED |
| Numeric-tail row1 | SUPP p.2 vs MAIN p.6 nominal800 versus801 | Retain: displayed-input interval overlap and exact nominal relative difference below.05. | ROUNDING_OR_DISPLAY_PRECISION |
| Numeric-tail row2 | SUPP p.5 vs MAIN p.6 dyslipidemia/NIHSS | Retain: baseline-copy tier; within-display arithmetic and full4800 totals reconcile. | PERIPHERAL_COMPARISON |
| Numeric-tail row3 | PLAN p.6 vs MAIN p.2 older than18 versus≥18 | Retain: eligibility wording does not identify a differing actual analysis-population size or primary/key-secondary definition. | PERIPHERAL_COMPARISON |
| Numeric-tail row4 | PLAN pp.13–16 vs SUPP p.3 DVT48h/day2 | Retain: matched detailed specification is end hospital day2; abbreviated wording supplies no conflicting classified count or outcome rule. | CONTEXT_RESOLVES |
| Numeric-tail row5 | PLAN Tables2/3, MAIN p.3/p.7, SUPP p.3 LDL brief/detailed criteria | Retain: report points to detailed≥100/prior therapy/undocumented LDL specification matching plan; no boundary-specific count supplied. | CONTEXT_RESOLVES |
| Numeric-tail row6 | PLAN Figure4 p.13 vs p.17 cycles120 | Retain: initial30-patient batch plus three subsequent batches are explicit; no planned sample-size contradiction. | CONTEXT_RESOLVES |
| Numeric-tail row7 | PLAN p.19/MAIN p.4 illustrative5of7 | Retain: example not trial measure total; binary outcome coding reproduces. | CONTEXT_RESOLVES |
| Numeric-tail row8 | PLAN p.17/MAIN p.4 power reconstruction | Retain: absent composite variance/equation; no reproduced supported-method result conflict. | CONDITIONAL_OR_UNREPORTED |
| Cross row1 | MAIN p.6/SUPP p.2 survey801 vs800 nominal | Retain: baseline survey administrative recruitment copy, full randomized4800 unchanged; .05 rule also screens nominal gap. | PERIPHERAL_COMPARISON |
| Cross row2 | MAIN p.6/SUPP p.5 baseline dyslipidemia/NIHSS | Retain: baseline-copy tier; no change in primary/key-secondary result or total analysis population. | PERIPHERAL_COMPARISON |
| Cross row3 | PLAN pp.10,13–15/SUPP p.3 rtPA last-normal/onset brief descriptions | Retain: detailed timed eligibility matches report and supplies intended operational measure; no competing numerical denominator or outcome definition reproduced. | TERMINOLOGY_OR_WORDING |
| Cross row4 | PLAN pp.13–15/SUPP pp.3,9 48h/two days | Retain: detailed hospital-day measures match; brief phrasing has no competing classified result or status. | TERMINOLOGY_OR_WORDING |
| Cross row5 | PLAN p.6/MAIN p.2 adult age boundary | Retain: peripheral eligibility wording, no supplied counted boundary subgroup or changed analyzed size. | PERIPHERAL_COMPARISON |
| Cross row6 | MAIN p.4/PLAN pp.16–19 mode/median imputation | Retain: plan has no incompatible replacement rule and report does not call this additional step prespecified. | CONDITIONAL_OR_UNREPORTED |
| Cross row7 | MAIN pp.3–4/PLAN pp.13,16–19 either-co-primary/no multiplicity adjustment | Retain: explicit report rule, no competing planned rule, no unsupported claim that this decision rule was prespecified. | CONDITIONAL_OR_UNREPORTED |
| Cross row8 | MAIN p.4/PLAN pp.16,18–19 secondary analyses interpreted exploratory | Retain: outcomes remain labelled secondary in report; qualification of inference alone is not changed endpoint status under category5. | TERMINOLOGY_OR_WORDING |
| Cross row9 | MAIN p.4/PLAN p.17 composite power inputs | Retain: plan/report input lists agree; composite SD/full equation absent; no supported exact power conflict. | CONDITIONAL_OR_UNREPORTED |
| Cross row10 | MAIN p.4/PLAN pp.18–20 disability/GEE/interim/margin omissions | Retain: no fixed competing disability rule or printed interim/margin calculation; additions/omissions alone do not show replaced planned key analysis. | CONDITIONAL_OR_UNREPORTED |
| Statistical1 row1 | PLAN p.17/MAIN p.4 binary-proportion power illustration | Retain: continuous patient-composite variance cannot be inferred from baseline80%; binary illustration is conditional, not a reproducing source method. | CONDITIONAL_OR_UNREPORTED |
| Statistical1 row2 | MAIN/SUPP adjusted differences and ratios vs crude values | Retain: adjusted/model-based labels explicit; no claimed crude identity. | MODEL_VERSUS_CRUDE |
| Statistical1 row3 | MAIN p.6/SUPP p.5 baseline NIHSS/dyslipidemia | Retain: peripheral copies, not changed outcome or analysis-population total; counts within each display reconcile. | PERIPHERAL_COMPARISON |
| Statistical1 row4 | MAIN p.3/PLAN p.15/SUPP p.3 brief LDL>100 | Retain: detailed cited eligibility identifies≥100/prior therapy/undocumented LDL; no numerical endpoint boundary conflict reproduced. | TERMINOLOGY_OR_WORDING |
| Statistical1 row5 | PLAN p.19/MAIN p.4 illustrative5of7 | Retain: explicit hypothetical example; not a changed trial nine-measure definition. | CONTEXT_RESOLVES |
| Statistical1 row6 | MAIN p.4/p.8 binary disability logistic/mixed wording | Retain: binary logistic mixed-model labels can coexist; no supplied incompatible covariance/test result or replaced fixed planned disability model. | CONDITIONAL_OR_UNREPORTED |
| Statistical1 row7 | PLAN p.19/MAIN p.5/SUPP p.8 absent all-or-none sensitivity | Retain: supplied plan general denominator strategy does not explicitly prescribe a separate all-or-none sensitivity contrast; implemented composite/nine-measure sensitivity matches. | CONDITIONAL_OR_UNREPORTED |
| Statistical1 row8 | PLAN p.17/p.13 three loops versus120 patients | Retain: four30-patient batches shown; no count conflict after graph context. | CONTEXT_RESOLVES |
| Statistical1 row9 | MAIN pp.4–5 hemorrhageχ²/Fisher comparison | Retain: one sparse narrative comparison has no same-display χ² comparison rows; Fisher diagnostic reproduces .26, exact unadjusted χ² implementation/cluster variance unstated. Unlike new S059, no same-display method establishes a conflicting paired inference. | CONDITIONAL_OR_UNREPORTED |

Prior retained-exclusion reason counts: ROUNDING_OR_DISPLAY_PRECISION4; PERIPHERAL_COMPARISON8; MODEL_VERSUS_CRUDE2; CONTEXT_RESOLVES8; TERMINOLOGY_OR_WORDING4; CONDITIONAL_OR_UNREPORTED10. Total36. No prior exclusion is re-emitted or assigned a new finding ID.

## Excluded observations

Only a newly considered apparent issue is listed here. The preceding36-row reassessment table preserves prior exclusions separately; reconciled tuple checks are not new exclusions.

| Location | Observation | Reason code |
|---|---|---|
| REPORT results supplement PDF p.8, eTable4 antidiabetic ORPA, S096 | OR1.59 versus geometric midpoint√(1.11×2.23)=1.573309. Allowing endpoint±.005 gives midpoint[1.568000,1.578615], while point interval is[1.585,1.595]. Gap.006385/1.59=.004016≤.05, so the apparent log-centering discrepancy is within the display-precision rule; no null/P conflict is present. | ROUNDING_OR_DISPLAY_PRECISION |

## Completion and limits

Every S001–S120 has explicit pass-2 completion in both this artifact and the canonical inventory. All86 paired estimate/CI/P tuples, ten availability tests, the hemorrhage comparison, both curve panels and21 design/method relationships were revisited without limiting findings to the initial ledger. All four registered candidates and ten screened finding records retain their provenance, source facts and stable IDs. No model data reconstruction, broad methodology audit or preferred analysis is proposed.

Unavailable inputs: raw event/censoring times and risk histories for exact Cox/log-rank recreation; continuous ranks for Wilcoxon; individual eligibility/fulfilled-opportunity records and composite weights; difference-specific confidence/test constructions, model covariance/output and variance estimator; composite SD, exact power equation and cluster-size imbalance assumptions. These constrain exact calculation, not source-location or relationship coverage. F-ST2-001 explicitly tests the same-display supported relationship despite the unreported construction, and awaits independent screening. Zero prior exclusions require reopening; one fresh finding and one new exclusion complete this pass.
