# Statistical consistency review — pass 2

Runtime agent ID: `/root/statistics_pass_2`; fresh `qc161_statistical_consistency_reviewer`, `gpt-6.1-sol`/`high`, distinct from `/root/statistics_pass_1`. Pass: 2. Assigned scope: all 103 parent relationships S001–S092 and S101–S111, including every retained main-table row, graphical marker, simulation cell, and all 27 subordinate individual tuples under S107. Represented source scope: DOC-001 REPORT pp1–10, DOC-002 PLAN pp1–55, DOC-003 REPORT pp1–17, DOC-004 REPORT p1. There is no applicable inferential relationship on the administrative-only data-sharing page. Parent grouping does not reduce subordinate coverage.

Read completely `QUALITY_CONTROL_SCOPE.md`, `workflow_1_6_1/review_contract.md`, the 606-line statistical inventory including its complete main and support evidence, the complete C001–C004 ledger, the single initial inclusion screen and all seven decisions, all mechanical recheck facts, and the complete pass-1 checker. The pass-1 exclusions were reconsidered under the same conservative context threshold. Only the current-run ledger/screen/recheck supplied the mandated pass-2 context; no earlier-run scientific conclusions, external literature, web, raw-data audit or Python scientific calculation was used.

Direct-source rereading used available Poppler `pdftotext` 25.03.0, `-layout -f FIRST -l LAST SOURCE -`, streamed without creating derivatives: DOC-001 pp3–4 and7–8; DOC-002 pp19–21,35,38–43; DOC-003 p5 andpp10–17. Current-run direct source renders `preprocessing/recheck-main-page5.png` and `preprocessing/screen-main-page6.png` were visually inspected for all Figure2/3 markers, axes, captions and table context. These images were made by direct Poppler and are visual aids to the supplied PDFs. No source, reusable artifact or other agent's output was changed. Canonical inventory changes are limited to the Pass2 statuses and a completion record; all pass-1 evidence and subordinate tuples are preserved.

## New findings

None. No `F-ST2` finding is emitted. The seven observations already given finding IDs and screened in the initial log were revisited through the complete ledger and recheck; none is re-emitted. Their source-grounded implications are recorded below without assigning a disposition or numerical replacement.

## Existing screening and recheck implications

| Existing candidate or screened finding | Pass-2 reconciliation |
|---|---|
| C001, F-NUM-001; S022/S063 | The source repeatedly defines INQoL as 0–100, while upper quartiles 110.3/120.0 remain above100 after half-unit allowances. Independently, the mean96.89(SD38.49) exceeds the bounded-score SD maximum even for every n≥2: sqrt(2×96.885×3.115)=24.5681<38.485. The unit needed for extracting the−14.22 effect remains unspecified; no alternative scale is supplied. This is the existing within-REPORT scale issue. |
| C002, F-XS-002; F-ST1-002 screened as duplicate | PLAN inverse-gamma variation priors and REPORT uniform SD(.01,10) priors give different variance families: v=SD² has bounded support(.0001,100) and density proportional to v^(−1/2), whereas inverse-gamma variance support is unbounded above. All eight SD-prior statements across three models are retained. The unreported clinical-prior counterpart is not an independent basis; the plan expressly permits a noninformative robustness branch. No posterior influence or executed amendment is inferred. |
| C003, F-ST1-001; S005/S006/S062/S088 | The stated common two-sided dependent-t effect/95%CI/test rule applies without assigning df. Precision-compatible maximum ratios6.785/5.135=1.3213 and.675/.435=1.5517 remain below conservative necessary normal-limit quantile ratios1.6198 for roundedP=.001 and1.6789 forP<.001. Finite positive Student-t df cannot supply the required smaller ratio. The normal-limit comparisons are necessary bounds, not reconstructed P values. Missing contributing pairs/df/output prevent selecting exact replacement quantities; the secondary exploratory label does not map different test and interval outputs. |
| C004, F-XS-001; F-ST1-003 screened as duplicate | Source visual rereading matches the dark-blue CLCN1 n16 group marker, primary stiffness reduction and95%CrI labels. Conservative graphical point3.45–3.65 and upper-end4.65–4.90 do not overlap narrative rounding intervals3.835–3.845 and5.155–5.165. Exact graphical coordinates remain absent. Figure3A corroborates the narrative magnitude and is not itself a reconstructed mean. No separate finding is emitted. |
| F-XS-003 screened CONTEXT_RESOLVES; S104 | Protocol p38 general related-SAE trigger and p39 detailed cardiac-event guidance can apply cumulatively: neither list is exclusive, and the paragraph refers to more detailed guidance. Both parenthetical boundaries identify three patients;3/30=10%. No new safety-rule observation is emitted and no actual DSMB consequence is inferred. |

Document-role implications remain content-grounded: main/results supplement are REPORT; prospective protocol is PLAN. C001/C003/C004 concern quantities/methods within one REPORT; C002 compares PLAN and REPORT. Corroboration creates no additional conflicting relationship. These statements revisit existing evidence and classification facts; every assigned candidate remains Pending Human Adjudication.

## Complete relationship revisitation

Each row is a separate parent record. All applicable estimates/intervals were checked for containment, endpoint order, direction and matched contrast; counts and contributor definitions were reconciled before comparisons. Exact test/CI compatibility was checked only where the source supplies a common method, two-sidedness and confidence level. Unreported df, covariance, variance estimator, denominator, posterior shape and estimand mapping were not inferred. The clinical substantial-effect threshold is>.75 IVR points, not a noninferiority/equivalence margin. No such design or margin is supplied. Secondary multiplicity is expressly unadjusted/exploratory. Individual stopping is advisory; no aggregate efficacy interim/stopping claim is inferred.

| S ID | Pass-2 fact, screening/recheck implication, or named reconstruction limit | Pass 2 |
|---|---|---|
| S001 | Normal hierarchy, all available completed-period data and placebo−mexiletine direction match explicit arm likelihoods. Primary-prior implication is existing C002; no covariance assigned. | PASS_2_COMPLETE |
| S002 | >.75 probability and >80%/<20% advice revisited against27 rows;24 continue/3 stop. Patient11 exception disclosed,80% values rounded. | PASS_2_COMPLETE |
| S003 | Post hoc fixed-effect simulation distinct from prospective expected-posterior task;685/1000=68.5%→69%,1.29−1.75=−.46. | PASS_2_COMPLETE |
| S004 | Mixed model/variance components/covariate selection coherent with repeated crossover description; order.85 and period.22 exceed.10. df/SE absent. | PASS_2_COMPLETE |
| S005 | Common dependent-t analysis explicitly produces total-group effects/CIs/tests. Paired design coherent; existing C003 covers two incompatible tuples. Subgroup interaction output kept distinct. | PASS_2_COMPLETE |
| S006 | Two-sided P<.05 rule and exploratory unadjusted secondary interpretation retained; no additional multiplicity rule or margin invented. | PASS_2_COMPLETE |
| S007 | All three group effects contained in orderedCrIs, positive reductions. CLCN1 plot discrepancy already C004; posterior probabilities are not P values. | PASS_2_COMPLETE |
| S008 | .85/.22 agree with no significant order/period effect and selection exclusion. No test statistic supplied. | PASS_2_COMPLETE |
| S009 | Current3.12(2.46,3.78) and quoted prior2.69(2.12,3.26) ordered/contained; descriptive consistency claims no equivalence test. | PASS_2_COMPLETE |
| S010 | Pain.68(−.52,1.89),weakness1.48(.18,2.77),tiredness1.23(−.23,2.67) ordered/contained;45/87/74 refer>.75, not zero-null tests. | PASS_2_COMPLETE |
| S011 | Age50(24–65)/38(19–64),P=.09: ranges contain means; Mann–Whitney ranks/ties absent, so no summary-based P inversion. | PASS_2_COMPLETE |
| S012 | Men13/16=81.25% and7/11=63.64% round to81/64;P=.39 not inverted without stated rank/test implementation. | PASS_2_COMPLETE |
| S013 | Pretrial mexiletine2/16=12.5%→13 and0/11;P=.50. No different binary test substituted. | PASS_2_COMPLETE |
| S014 | Other medication7/16=43.75%→44 and5/11=45.45% versus46 displayed; baseline precision/context does not alter an inferential result. Rank implementation absent. | PASS_2_COMPLETE |
| S015 | Stiffness6.7(6–7)/4.7(3.3–5.1),P=.002: medians in orderedIQRs; CLCN1 higher matches narrative. | PASS_2_COMPLETE |
| S016 | Pain0(0–1.1)/3.4(2.3–5.5),P=.002: orderedIQRs/median containment; SCN4A higher matches narrative. | PASS_2_COMPLETE |
| S017 | Weakness3.8(1.1–5)/.5(0–6.1),P=.06: orderedIQRs/containment; ranks absent, descriptive spread cannot determine P. | PASS_2_COMPLETE |
| S018 | Tiredness3.4(1.4–6)/5.1(3.9–6.1),P=.16: orderedIQRs/containment; rank P not reconstructed. | PASS_2_COMPLETE |
| S019 | Handgrip1.1(.9–2)/1.5(1–6.4),P=.40: orderedIQRs/containment, seconds identified. | PASS_2_COMPLETE |
| S020 | Eyelid1.2(.6–2.9)/4(1.3–11.2),P=.01: higher SCN4A direction matches narrative; orderedIQRs. | PASS_2_COMPLETE |
| S021 | TimedUp&Go9.7(8.8–11)/9.5(8.3–10.3),P=.49: orderedIQRs/containment; rank inputs absent. | PASS_2_COMPLETE |
| S022 | INQoL84(74.5–110.3)/98(56–120),P=.82: medians within orderedIQRs; scale bound already C001, not a new rank-test issue. | PASS_2_COMPLETE |
| S023 | SF36physical40.8(37.7–46.6)/38.7(33.6–40),P=.11: orderedIQRs/containment and scale direction checked. | PASS_2_COMPLETE |
| S024 | SF36mental52.1(44.7–57.1)/55(37.2–59.1),P=.88: orderedIQRs/containment; rank P not inferred. | PASS_2_COMPLETE |
| S025 | Figure2 patient13 SCN4A near0,interval−.4 to.1: graphical containment/order; interim−.05(−.56,.45) is a separately defined analysis. | PASS_2_COMPLETE |
| S026 | Patient11 near0,interval−.5 to.1 ordered/contained; eTable3 wide interimCrI and38% exception are disclosed, no assumed model equality. | PASS_2_COMPLETE |
| S027 | Patient22 near0,interval−.6 to.5 ordered/contained; interim.01(−.56,.57),1%/stop agrees. | PASS_2_COMPLETE |
| S028 | Patient4 open SCN4A1.1(.2,1.9) ordered/contained; two sets and81%/continue match eTable3. | PASS_2_COMPLETE |
| S029 | Patient20 SCN4A1.1(.1,2.1) ordered/contained; interim1.13 and rounded80%/continue coherent. | PASS_2_COMPLETE |
| S030 | Patient8 SCN4A1.2(0,2.3) ordered/contained; interim1.2 and rounded80%/continue coherent. | PASS_2_COMPLETE |
| S031 | Patient25 CLCN1 near1.6(1.2,2) ordered/contained; interim1.65(1.27,2.03),100%/continue agrees at graphical precision. | PASS_2_COMPLETE |
| S032 | Patient18 CLCN1 near2.6(1.8,3.4) ordered/contained; interim2.55(1.77,3.32),100%/continue. | PASS_2_COMPLETE |
| S033 | Patient19 SCN4A near2.6(1.2,4) ordered/contained; interim2.63(1.18,4.01),99%/continue. | PASS_2_COMPLETE |
| S034 | Patient24 CLCN1 near2.6(2.2,3.1) ordered/contained; interim2.64(2.16,3.12),100%/continue. | PASS_2_COMPLETE |
| S035 | Patient12 SCN4A near2.7(1.8,3.6) ordered/contained; interim2.66(1.76,3.56),100%/continue. | PASS_2_COMPLETE |
| S036 | Patient15 CLCN1 near2.7(2.2,3.2) ordered/contained; interim2.7(2.16,3.24),100%/continue. | PASS_2_COMPLETE |
| S037 | Patient2 open CLCN1 near3.1(2.8,3.5) ordered/contained; two sets,interim3.1(2.63,3.49),100%/continue; no exact graphical equality assumed. | PASS_2_COMPLETE |
| S038 | Patient27 CLCN1 near3.1(2.4,3.8) ordered/contained; interim3.14(2.46,3.83),100%/continue. | PASS_2_COMPLETE |
| S039 | Patient9 SCN4A near3.2(2.8,3.6) ordered/contained; interim3.2(2.78,3.56),100%/continue. | PASS_2_COMPLETE |
| S040 | Patient17 CLCN1 near3.2(2.9,3.5) ordered/contained; interim3.22(2.94,3.50),100%/continue. | PASS_2_COMPLETE |
| S041 | Patient14 CLCN1 near3.5(2.8,4.2) ordered/contained; interim3.5(2.81,4.19),100%/continue. | PASS_2_COMPLETE |
| S042 | Patient30 CLCN1 near3.6(2.9,4.2) ordered/contained; interim3.57(2.91,4.23),100%/continue. | PASS_2_COMPLETE |
| S043 | Patient10 SCN4A near3.7(2.4,5) ordered/contained; interim3.7(2.28,5.04),100%/continue; graphical bounds approximate. | PASS_2_COMPLETE |
| S044 | Patient1 open CLCN1 near4.4(4,4.9) ordered/contained; two sets,interim4.4(4.03,4.85),100%/continue. | PASS_2_COMPLETE |
| S045 | Patient21 SCN4A near4.4(3.8,5) ordered/contained; interim4.41(3.80,5),100%/continue. | PASS_2_COMPLETE |
| S046 | Patient16 CLCN1 near4.5(3.9,5.1) ordered/contained; interim4.49(3.96,5.03),100%/continue. | PASS_2_COMPLETE |
| S047 | Patient28 CLCN1 near4.5(4,5) ordered/contained; interim4.50(4,4.99),100%/continue. | PASS_2_COMPLETE |
| S048 | Patient26 CLCN1 near4.7(4.2,5.2) ordered/contained; interim4.65(4.07,5.21),100%/continue; no exact model equality assumed. | PASS_2_COMPLETE |
| S049 | Patient5 open CLCN1 near4.7(4.5,4.9) ordered/contained; two sets,interim4.7(4.50,4.87),100%/continue. | PASS_2_COMPLETE |
| S050 | Patient23 CLCN1 near5.6(5.1,6.1) ordered/contained; interim5.49(4.98,6.04),100%/continue; graphical precision/model mapping limits equality. | PASS_2_COMPLETE |
| S051 | Patient29 CLCN1 near7(6.6,7.5) ordered/contained; interim6.99(6.59,7.41),100%/continue; distinct from group marker. | PASS_2_COMPLETE |
| S052 | Every density/threshold/group reviewed; CLCN1 density near3.8 corroborates C004 narrative, not an exact mean reconstructed from mode. | PASS_2_COMPLETE |
| S053 | All survival curves decrease with threshold;>.75 readouts100/100/93 coherent;20%/52% and.43/1.14 historical translations admit rounding. | PASS_2_COMPLETE |
| S054 | All sequential markers revisited; first11 recruited IDs and completed-analysis sequence are not assumed identical. Terminal SCN4A uses an unspecified aggregation mapping. | PASS_2_COMPLETE |
| S055 | Primary frequentist3.12(2.46,3.78),P<.001 ordered/contained/beneficial; adjusted mixed-model effect need not equal3.13 crude difference. | PASS_2_COMPLETE |
| S056 | CLCN1 frequentist3.82(3.10,4.54),P<.001 ordered/contained/beneficial; not Bayesian3.84, different identified method. | PASS_2_COMPLETE |
| S057 | SCN4A1.89(1.01,2.76),P=.002 ordered/contained/beneficial; df/SE unspecified, no crude2.06 substitution. | PASS_2_COMPLETE |
| S058 | Pain.70(.18,1.23),P=.01 ordered/contained/beneficial; frequentist result distinct from Bayesian.68 and45%>.75. | PASS_2_COMPLETE |
| S059 | Weakness1.56(1.05,2.06),P<.001 ordered/contained/beneficial; modeled effect versus crude1.47 excluded. | PASS_2_COMPLETE |
| S060 | Tiredness1.27(.58,1.95),P=.001 ordered/contained/beneficial; mixed-model tuple not inverted with unreported df. | PASS_2_COMPLETE |
| S061 | SF36physical7.81(4.72,10.88),P<.001 contained/ordered; tiny midpoint offset permits half-unit boundary, positive improvement. Arm-change CI construction/pairs absent. | PASS_2_COMPLETE |
| S062 | SF36mental6.78(1.64,11.92),P=.001 contained/ordered/positive improvement; existing C003 covers same-test incompatibility. | PASS_2_COMPLETE |
| S063 | INQoL−14.22(−24.71,−3.74),P=.01 contained/ordered; negative improvement coherent, unknown scale already C001. | PASS_2_COMPLETE |
| S064 | Handgripfirst−2.85(−5.28,−.42),P=.02 contained/ordered/beneficial; isolated placebo upper minus is contextual typography. | PASS_2_COMPLETE |
| S065 | Handgripfifth−.97(−2.03,.09),P=.07 contains0, nonsignificant direction coherent; no paired-count inference. | PASS_2_COMPLETE |
| S066 | CLCN1handgripfifth.04(−1.11,1.19),P=.95 contains0; subgroup result distinguished from interactionP=.04. | PASS_2_COMPLETE |
| S067 | SCN4Ahandgripfifth−1.96(−3.41,.51),P=.009: immediate symmetric-summary direction identifies upper-end sign slip; no new finding. | PASS_2_COMPLETE |
| S068 | Handgripmean−1.44(−2.66,−.22),P=.02 contained/ordered/beneficial; marginal arm summaries not assumed identical paired inputs. | PASS_2_COMPLETE |
| S069 | Eyelidfirst−4.25(−8.45,−.05),P=.05: roundedP admits<.05; CI/point direction beneficial. | PASS_2_COMPLETE |
| S070 | Eyelidfifth−.95(−2.25,.35),P=.14 contains0, nonsignificance agrees; paired df absent. | PASS_2_COMPLETE |
| S071 | Eyelidmean−2.11(−3.94,−.28),P=.03 excludes0,beneficial; same-test necessary bound supplies no additional contradiction. | PASS_2_COMPLETE |
| S072 | TimedUp&Gofirst−1.25(−2.23,−.28),P=.01 contained/ordered/beneficial; display midpoint allowance applied. | PASS_2_COMPLETE |
| S073 | TimedUp&Gofifth−1(−2.01,.03),P=.06 contains0; midpoint discrepancy admits half-unit boundary, no exact output supplied. | PASS_2_COMPLETE |
| S074 | TimedUp&Gomean−1.12(−2.07,−.18),P=.02 contained/ordered/beneficial; placebo upper-end character is readily contextual. | PASS_2_COMPLETE |
| S075 | Relaxationfirst−.02(−.86,.82),P=.96 contains0; precision-compatible ratio allows stated near-null test. | PASS_2_COMPLETE |
| S076 | Relaxationfifth−.01(−.16,.14),P=.87 contains0; half-unit allowance material for tiny effect, no unrounded t inferred. | PASS_2_COMPLETE |
| S077 | Relaxationmean−.02(−.28,.25),P=.91 contains0; half-unit allowance resolves near-zero ratio comparison. | PASS_2_COMPLETE |
| S078 | Peakforcefirst32.92(−5.10,70.94),P=.09 contained/ordered/nonsignificant; positive change improvement. | PASS_2_COMPLETE |
| S079 | Peakforcefifth24.08(−5.22,53.39),P=.10 contained/ordered/nonsignificant; paired df/SE not supplied. | PASS_2_COMPLETE |
| S080 | Peakforcemean37.23(10.19,64.28),P=.009 contained/ordered/beneficial; no additional necessary-bound contradiction. | PASS_2_COMPLETE |
| S081 | Transientparesisfirst−3.7(−15.10,7.68),P=.51 contained/ordered/nonsignificant; lower is better. | PASS_2_COMPLETE |
| S082 | Transientparesisfifth−12.25(−22.04,−2.47),P=.02 contained/ordered/beneficial; subgroup effects and interaction distinct. | PASS_2_COMPLETE |
| S083 | CLCN1paresisfifth−23.85(−32.45,−15.24),P<.001 contained/ordered/beneficial; source-reported subgroup effect retained. | PASS_2_COMPLETE |
| S084 | SCN4Aparesisfifth13.71(−1.96,25.47),P=.02: isolated lower-minus sign context immediately resolved; positive worsening visible, generalized footnote pertains total result. | PASS_2_COMPLETE |
| S085 | Paresismean−7.34(−13.45,−1.24),P=.02 contained/ordered/beneficial; no crude−6.30 substitution with absent matched pairs. | PASS_2_COMPLETE |
| S086 | CLCN1paresismean−12.37(−18.35,−6.38),P<.001 contained/ordered/beneficial; no subgroup covariance/df supplied. | PASS_2_COMPLETE |
| S087 | SCN4Aparesismean4.46(−3.85,12.76),P=.28 contains0,positive worsening not significant; treatment interaction distinct. | PASS_2_COMPLETE |
| S088 | EMG.67(.23,1.11),P<.001 contained/ordered/beneficial; common dependent-t compatibility already C003, no new output inferred. | PASS_2_COMPLETE |
| S089 | StiffnessinteractionP=.004 matches stronger CLCN1 reduction; subgroupP and interactionP not equated, interactionSE/covariance absent. | PASS_2_COMPLETE |
| S090 | HandgripfifthinteractionP=.04 matches relative SCN4A response; upper-endpoint slip contextual, not an independent method issue. | PASS_2_COMPLETE |
| S091 | ParesisfifthinteractionP<.001 matches CLCN1 relative benefit/SCN4A worsening; no interaction test inversion from subgroupCIs. | PASS_2_COMPLETE |
| S092 | ParesismeaninteractionP=.002 matches CLCN1 relative benefit; same subgroup numbers repeat narrative; covariance/interactionstatistic absent. | PASS_2_COMPLETE |
| S101 | Prospective methodological primary objective and reported clinical primary endpoint coexist with shared IVR stiffness definition; no new quantity attribution issue. | PASS_2_COMPLETE |
| S102 | All four prospective prior/pair cells and two6×8 simulation tables revisited; expected probabilities≠power. Nullmax.66<.8→0/1000;685+315=1000;bias−.46. Simulation seeds/draws not supplied. | PASS_2_COMPLETE |
| S103 | PLAN intent-to-treat/all pretermination data compared with REPORT completed-period inclusion27/30; usable periods/consent for three dropouts absent, no unconditional exclusion asserted. | PASS_2_COMPLETE |
| S104 | Every safety trigger/threshold andp38/p39 context revisited;3/30=10%,samecardiacevents≥2. Initial screen already resolves nonexclusive guidance; no unpublished DSMB choice inferred. | PASS_2_COMPLETE |
| S105 | PLAN random-intercept/slope hierarchy and REPORT separate-arm hierarchy traced without assigning covariance. Single report center explains absent center variability. Variance-family change already C002; no independent clinical-prior counterpart basis. | PASS_2_COMPLETE |
| S106 | Individual≥80%/≤20% PLAN advice and strict REPORT boundaries compared with rounded80% rows; advisory nature/exception resolves decisions, no aggregate stopping inferred. | PASS_2_COMPLETE |
| S107 | All27 rows individually revisited below: orderedCrIs contain means;24continue/3stop,16CLCN1/11SCN4A,4secondsets/23firstsets. Patient11 exception disclosed. | PASS_2_COMPLETE |
| S108 | All four posterior curves and exact100/45/87/74 probabilities match primary/secondary Bayesian narrative; no exact normal tail/mean inferred from curves. | PASS_2_COMPLETE |
| S109 | Individual normal arm likelihoods, means,precisions,tau=1/sigma² andstep(diff−threshold) coherent. Fixed30 loops require unsupplied data padding/indexing; priors already C002. | PASS_2_COMPLETE |
| S110 | Complete hierarchical likelihood, observed-count loops,commonSD,arm mean anddiff formulas coherent; arm glossary reversals resolve from code/data. Covariance not supplied; priors already C002. | PASS_2_COMPLETE |
| S111 | Gen_Pat1/0,a+b/c+d arm means,commonSD and both contrasts/thresholds coherent; duplicatedSCN4A glossary besideCLCN1 resolves from explicit code. Priors already C002. | PASS_2_COMPLETE |

## S107 — individual pass-2 records

Direct source: [REPORT results supplement p5, eTable3](../../../joi180136supp2_prod.pdf#page=5), compared with [REPORT main p3, Bayesian Analysis](../../../jama_stunnenberg_2018_oi_180136.pdf#page=3) and [PLAN protocol p42, advisory stopping](../../../joi180136supp1_prod.pdf#page=42). All means are contained and every pair of endpoints ordered. Each mean/CrI/probability tuple remains in the canonical inventory. No normal approximation is used to replace any reported posterior probability.

| Patient row key | Gene | Mean and95%CrI | Posterior / post-trial implication | Pass 2 |
|---|---|---|---|---|
| 1 | CLCN1 | 4.4(4.03,4.85) | 100%/continued;secondset | PASS_2_COMPLETE |
| 2 | CLCN1 | 3.1(2.63,3.49) | 100%/continued;secondset | PASS_2_COMPLETE |
| 4 | SCN4A | 1.1(.27,1.90) | 81%/continued;secondset | PASS_2_COMPLETE |
| 5 | CLCN1 | 4.7(4.50,4.87) | 100%/continued;secondset | PASS_2_COMPLETE |
| 8 | SCN4A | 1.2(−.03,2.41) | 80%/continued;display permits>80% | PASS_2_COMPLETE |
| 9 | SCN4A | 3.2(2.78,3.56) | 100%/continued | PASS_2_COMPLETE |
| 10 | SCN4A | 3.7(2.28,5.04) | 100%/continued | PASS_2_COMPLETE |
| 11 | SCN4A | 0(−12.24,12.16) | 38%/stopped;zero-symptom/prior-driven exception explicitly disclosed | PASS_2_COMPLETE |
| 12 | SCN4A | 2.66(1.76,3.56) | 100%/continued | PASS_2_COMPLETE |
| 13 | SCN4A | −.05(−.56,.45) | 2%/stopped | PASS_2_COMPLETE |
| 14 | CLCN1 | 3.5(2.81,4.19) | 100%/continued | PASS_2_COMPLETE |
| 15 | CLCN1 | 2.7(2.16,3.24) | 100%/continued | PASS_2_COMPLETE |
| 16 | CLCN1 | 4.49(3.96,5.03) | 100%/continued | PASS_2_COMPLETE |
| 17 | CLCN1 | 3.22(2.94,3.50) | 100%/continued | PASS_2_COMPLETE |
| 18 | CLCN1 | 2.55(1.77,3.32) | 100%/continued | PASS_2_COMPLETE |
| 19 | SCN4A | 2.63(1.18,4.01) | 99%/continued | PASS_2_COMPLETE |
| 20 | SCN4A | 1.13(.14,2.13) | 80%/continued;display permits>80% | PASS_2_COMPLETE |
| 21 | SCN4A | 4.41(3.80,5.0) | 100%/continued | PASS_2_COMPLETE |
| 22 | SCN4A | .01(−.56,.57) | 1%/stopped | PASS_2_COMPLETE |
| 23 | CLCN1 | 5.49(4.98,6.04) | 100%/continued | PASS_2_COMPLETE |
| 24 | CLCN1 | 2.64(2.16,3.12) | 100%/continued | PASS_2_COMPLETE |
| 25 | CLCN1 | 1.65(1.27,2.03) | 100%/continued | PASS_2_COMPLETE |
| 26 | CLCN1 | 4.65(4.07,5.21) | 100%/continued | PASS_2_COMPLETE |
| 27 | CLCN1 | 3.14(2.46,3.83) | 100%/continued | PASS_2_COMPLETE |
| 28 | CLCN1 | 4.50(4.0,4.99) | 100%/continued | PASS_2_COMPLETE |
| 29 | CLCN1 | 6.99(6.59,7.41) | 100%/continued | PASS_2_COMPLETE |
| 30 | CLCN1 | 3.57(2.91,4.23) | 100%/continued | PASS_2_COMPLETE |

Counts reconcile:16+11=27;24+3=27;23+4=27;23×1+4×2=31sets. All16CLCN1 continue and8of11SCN4A continue. The clinical exception prevents treating three discontinuations as three numerically below20% posteriors; the source explains that distinction locally.

## Excluded observations

Each reconsidered observation or repeated pattern appears once, with exactly one reason code. Existing screened findings are handled only in the preceding reconciliation table and are not re-emitted here.

| Location | Observation | Reason code |
|---|---|---|
| DOC-001 REPORT p7;S004,S055–S060 | Model-based IVR effects differ from crude arm differences; identified mixed model supplies the comparison context. | MODEL_VERSUS_CRUDE |
| DOC-001 REPORT pp7–8;S061–S087 | Marginal change summaries do not uniquely reproduce paired effect means without row-specific matched contributors/repeated-set aggregation; those inputs are absent. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 REPORT pp7–8;S061–S087 | Change-block placebo−mexiletine heading versus displayed change signs: arm changes and scale directions immediately identify beneficial/worsening direction. | CONTEXT_RESOLVES |
| DOC-001 REPORT pp6–8;S064,S067,S074,S084 | Isolated endpoint sign/character slips in firsthandgrip placebo,SCN4Afifthhandgrip,meanTimedUp&Go placebo andSCN4Afifthparesis are resolved by immediate symmetric summaries/point and direction. One typography pattern. | NOTATION_OR_TYPOGRAPHY |
| DOC-001 REPORT p7;S061–S063 | Asymmetric marginal arm-changeCIs do not establish a treatment-test contradiction: their distinct CI construction is not stated. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 REPORT p7;S061,S073,S076,S077 | Tiny midpoint or near-zero CI/P differences permit precision-compatible values when each input receives its half-unit interval. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 REPORT p7;S069 | P=.05 andCI excluding0 permit an underlyingP<.05 within two-decimal display precision. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 REPORT pp7–8;S084 | General significant-results-favor-mexiletine footnote is read as total-group summary; SCN4A worsening is explicitly visible locally. | CONTEXT_RESOLVES |
| DOC-001 REPORT p5 Table1;S011–S024 | P values cannot be reconstructed from summaries without ranks/ties/execution detail; no alternate test for count rows inferred. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 REPORT p5 Table1;S014 | Other-pretrial-medication5/11 versus displayed46% is a descriptive baseline display difference and does not change a primary/key result or analysis-population size. | PERIPHERAL_COMPARISON |
| DOC-001 REPORT pp4–6;DOC-003 REPORT pp5,8;S007,S010,S052,S107,S108 | Exact normal-tail inversion of credible intervals/probabilities assumes an unstated posterior distribution; diagnostic shapes cannot replace supplied Bayesian analyses. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 REPORT p5;S002,S107 patient11 | 38% posterior versus discontinuation/nonresponder terminology is explained by explicit zero-symptom and wide-prior exception. | CONTEXT_RESOLVES |
| DOC-002 PLAN p42;DOC-003 REPORT p5;S106,S107 patients8/20 | Strict versus inclusive80% boundary cannot establish different decisions from integer-rounded80% posteriors. | ROUNDING_OR_DISPLAY_PRECISION |
| DOC-001 REPORT p5;DOC-003 REPORT p5;S025–S051,S107 | Figure2individual and eTable3interim intervals are not established as the same hierarchical/standalone analysis, especially patient11; no exact equivalence inferred. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 REPORT p6 Figure3C;S054 | Sequential terminalSCN4A≈88% versus93% narrative lacks a common aggregation-set/model mapping; recruited IDs and plotted-analysis counts also differ by disclosed dropout context. | CONDITIONAL_OR_UNREPORTED |
| DOC-001 REPORT p6;DOC-002 PLAN p43;DOC-003 REPORT pp11–14;S053,S106,S110,S111 | Cumulative/survival wording,LR label and arm/genotype glossary reversals resolve directly from probability axis,likelihood context and explicit code. | TERMINOLOGY_OR_WORDING |
| DOC-002 PLAN p35;DOC-001 REPORT pp3–4;S103 | A population discrepancy requires absent usable-period/consent details for dropouts; no assumed primary eligibility exclusion. | CONDITIONAL_OR_UNREPORTED |
| DOC-002 PLAN pp40–41;DOC-003 REPORT pp11–14;S105,S110,S111 | Random-intercept/slope versus arm-mean hierarchy cannot yield a covariance contradiction without its planned covariance; the single report center resolves center variability. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 REPORT p10;S109 | Fixed30 loops versus maximum30/missingobservations requires absent data vectors/padding/indexing to establish an implementation contradiction. | CONDITIONAL_OR_UNREPORTED |
| DOC-003 REPORT p15;S102 | eMethods-number pointers are immediately identified from individual/group model titles; they do not identify a different executed analysis. | NOTATION_OR_TYPOGRAPHY |
| DOC-002 PLAN pp19–21;DOC-003 REPORT pp15–17;S102 | Expected posterior probability and fixed-effect power are explicitly different simulation criteria; seeds/draws absent, so no formula-based sample-size reconstruction asserted. | CONDITIONAL_OR_UNREPORTED |
| DOC-002 PLAN pp40–42;DOC-003 REPORT pp10–14;S105 | Missing clinical-prior counterpart/result mapping alone does not establish replacement: protocol permits noninformative robustness substitution. This supplies no independent candidate beyond the already screened variance-family contrast. | CONDITIONAL_OR_UNREPORTED |
| DOC-002 PLAN p40;DOC-001 REPORT pp3–6;S105 | General unreported Bayesian physiologic-secondary output is not a prespecified key-secondary replacement; absence alone supplies no result-specific contradiction. | CONDITIONAL_OR_UNREPORTED |

## Completion and limitations

Pass2 completed for103/103 parent S IDs and27/27 subordinate S107 rows. New findings0; excluded observation patterns23. Every parent and individual row has explicit PASS_2_COMPLETE in this artifact and the canonical inventory. No fresh pass-2 inclusion screen is required because there is no new finding. No source-unit or inferential-relationship coverage gap remains.

Named reconstruction limits remain: exact unlabelled graphical coordinates and sequential aggregation/model identifiers; mixed-model df,SE,covariance/variance estimator; row-specific paired contributors/df/SE/test outputs and repeated-set aggregation; marginal-changeCI construction; posterior samples/distribution shapes; executed Bayesian-prior files/amendment mapping; usable dropout periods/consent; simulation seeds/draws and fixed-loop data padding. These restrict exact reconstruction and explanation, not coverage. No preferred method, numerical replacement, severity, acceptance or human disposition is assigned.

Artifacts: `checkers/statistical_pass_2.md`; canonical status update `statistics/relationship_inventory.md`. Runtime identity for the execution manifest: `/root/statistics_pass_2`.
