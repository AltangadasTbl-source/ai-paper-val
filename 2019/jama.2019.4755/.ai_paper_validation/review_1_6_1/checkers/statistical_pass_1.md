# Statistical pass 1 — complete self-screened review

- **Stage:** statistics_pass_1.
- **Runtime agent ID:** /root/statistics_pass_1 (manifest spelling root/statistics_pass_1).
- **Routing:** newly spawned gpt-6.1-sol, high effort; this agent may not perform pass 2.
- **Exact scope:** DOC-001 REPORT physical pp1-7; DOC-002 PLAN pp1-62; DOC-003 PLAN pp1-10; DOC-004 REPORT pp1-8; DOC-005 REPORT p1. Complete mapped union88pages. [Complete inventory](../statistics/relationship_inventory.md): S001-S116, all116 PASS_1_COMPLETE.
- **Counts:**116 stable relationships;108 explicitly retained inferential result/test endpoints;44 method/design records (main13 plus remaining31);90 effect-difference CIs;18 site SD/P endpoints;0 findings;22 excluded observations;0 scientific coverage gaps.

## Inputs and source authority

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md completely; also current settings, inventories, tooling record, coverage manifest and both complete main/support evidence maps. Mapper keys were crossed into fresh global S IDs; none were old checker/candidate conclusions. Source-linked reusable text and direct Poppler pdftotext26.01.0 readings locate the values. Direct confirmation covered main pp3-6, protocol pp28-29 and SAP pp1-10. For result supplement p7, mapper/direct-render evidence explicitly distinguishes native hidden numbers and visible cells rather than treating native extraction as a rendered reading. No external sources, historical scientific dispositions, raw data or preferred-analysis recommendations were used. All work is English; supplied sources and reused assets are preserved.

## Completed checks and results

All90 effect-difference intervals have ascending endpoints, contain the point estimate and agree with the aspirin-minus-placebo direction. Source-defined sensitivity, specificity, PPV and NPV denominators were evaluated separately for each matched count matrix. Main Table2/3, eTable3 combined-sample, eTables4/5 actual-day2 per-protocol and eTable6 intention-to-screen site results were kept distinct. All90 endpoints reproduce to half-unit display precision under the named95% Agresti-Caffo interval construction, with the adjusted interval centered on adjusted proportions rather than necessarily the printed raw difference. Per-result counts and reconstructed endpoints are retained in the inventory; no row or sex/cutoff endpoint was sampled.

Main primary quantitative sensitivity is9.8points[−3.1,22.2],P=.14 at10.2µgHb/g and6.0[−5.7,17.5],P=.32 at17.0. Both95%CIs include0, both P>.05 and all primary conclusion occurrences describe no significant increase. Qualitative sensitivity12.7[0.1,24.7],P=.048 and pooled specificity−6.4[−9.6,−3.2],P<.001;−3.1[−5.4,−0.8],P=.008;−8.0[−11.0,−4.9],P<.001 agree in significance and direction. The method does not expressly name the algorithm producing these individual P values. Consequently a CI-inversion P calculation could only be a diagnostic approximation, never a source-established identity test. No unsupported sidedness, degrees of freedom, test statistic, covariance or variance estimator was assigned.

Sex interaction P=.08-.49 addresses effect modification, rather than each subgroup's within-stratum aspirin comparison. Several male sensitivity/women PPV intervals excluding0 do not contradict nonsignificant interaction tests. The narrative 'Overall, no significant differences' for predictive values is immediately resolved by the pooled All rows: their PPV/NPV CIs all include0 in both intention-to-screen and per-protocol analyses.

Every eTable6 site sensitivity/specificity SD is nonnegative, all18 P values lie between.16 and.50 and none crosses the stated.05 criterion. The decision to retain the model without site random intercept follows that reported test decision. The source supplies nullSD=0 versusSD>0 and likelihood-ratio testing, but not the likelihood statistic or its reference law; P=.50 at zero/tiny fitted SD is not treated as a discrepancy. The separate SAP participant random-intercept model for replicate measurements is a different data structure, not interchangeable with the site analysis.

Planned2400 randomized/2000 analyzed with10%disease implies200 affected=100/arm as printed. The report's36%→60%,24-point design effect,90% power and two-sidedα.05 agree with the protocol. A **diagnostic normal two-proportion sample-size approximation**, using the printed inputs, gives88.97 affected/arm without correction and97.12 with a common continuity correction;100 is compatible with nominal90% power. The exact planned test and correction implementation are not stated, so this is not a claim of exact sample-size reproduction. A second diagnostic for36%→70% gives48.87 affected/arm with that correction; the protocol does not give sex-specific disease counts, so no balanced-sex assumption supports a finding. For specificity90%,900 nondiseased/arm gives a diagnostic normal95% interval88.04%-91.96%, compatible with the printed expected88%-92%. No model/covariate or preferred power method is proposed.

Protocol day3 after drugday1 equals report/SAP day2 after drugday0 by the SAP's explicit renumbering footnote. SAP§7 explicitly changes the primary population from per-protocol to intention-to-screen and includes missing collection dates; these later rules resolve earlier SAP sections. Available-result analysis descriptions and matched denominator matrices identify the printed primary numbers. Fisher missingness evaluation outputs, its numerical decision threshold, complete missing-outcome treatment rule and individual duplicate handling are not supplied; no unsupported imputation mechanism was inferred.

Primary confirmatory versus exploratory secondary inference and no multiple-testing adjustment are expressly reported. The package supplies no further multiplicity algorithm, efficacy/futility interim rule, noninferiority/equivalence margin or claim. Recruitment and unexpected-reaction stopping provisions were reviewed, with absent interim counts/numerical adverse-reaction boundary recorded precisely. Neither continued recruitment nor unrelated serious events establishes a failed stopping rule.

Prespecified exploratory ROC/LR/screening-burden, longitudinal/baseline-change and non-sex subgroup outputs are not supplied; the paper expressly identifies LR/AUC as not reported. These absent outputs do not by themselves establish a changed primary/key-secondary numerical result, identify a replacement analysis or make any supplied table number unassignable. The protocol's broad sample-size paragraph describes more quantities under 'primary endpoint' than its repeated dedicated definitions; immediate hierarchy and sensitivity-focused power context resolve the intended primary quantitative FIT sensitivity.

## Findings

No observation met all four inclusion criteria after exact matching, half-unit arithmetic and immediate-context review. No F-ST1 ID is emitted. The proposed review domain and affected-result/human-question fields required for findings therefore have no applicable finding unit. No severity, adjudication, evidence state, acceptance or correction is assigned by this checker.

## Excluded observations

Each observation or repeated pattern appears once with exactly one normative reason code. Coherent relationships yielding no observation remain explicitly completed in the inventory; their absence here is not missing coverage.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p5 Tables2/3; REPORT DOC-004 pp5-7 eTables3-5 | A printed group subtraction can differ by0.1point from the printed difference (e.g.82.2−88.7 versus−6.4); exact count ratios/half-unit intervals reconcile all rows. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p3 method/p5 Tables2-3; PLAN DOC-003 p8; REPORT DOC-004 pp5-7 | Raw point differences need not equal the95%CI midpoint; adjusted-Wald Agresti-Caffo construction explains all90 intervals. | CONTEXT_RESOLVES |
| REPORT DOC-001 pp3-5 outcome P values; PLAN DOC-003 p8 | The exact individual outcome P algorithm, test statistics and standard errors are not supplied; a particular test inversion cannot be asserted. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p5; REPORT DOC-004 pp5-7 | Group-specific Agresti-Coull intervals are described but not displayed; they cannot be mechanically compared with a supplied group CI. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 pp3-5; PLAN DOC-003 p9 | Subgroup difference CIs may exclude0 while sex-interaction P=.08-.49 remains nonsignificant; these are distinct hypotheses. | CONTEXT_RESOLVES |
| REPORT DOC-001 p4 predictive-value narrative/p5 Table3; REPORT DOC-004 p7 eTable5 | 'Overall' no significant PPV/NPV difference refers pooled All rows and does not negate several negative women PPV intervals. | CONTEXT_RESOLVES |
| REPORT DOC-004 p7 eTable5 women PPV cells | Visible presentation shows minus signs without numerical portions; source-native−18.2,−25.7,−21.6 and adjacent group values/intervals identify intended differences immediately. Native/render distinction preserved. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-001 p5 Table3 men's third10.2 row | Test-name cell blank; the row position and matching Table2 count results identify qualitative FIT immediately. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-004 p5 eTable3 men quantitative10.2 sensitivityCI | Printed endpoint separator '−5.5.27.8' has evident intended lower/upper limits−5.5 and27.8. | NOTATION_OR_TYPOGRAPHY |
| PLAN DOC-003 p8§5.4/p9§7; REPORT DOC-001 p3 | Earlier primary PP versus later ITS is an expressly disclosed change to the plan and matches the report. | CONTEXT_RESOLVES |
| PLAN DOC-003 p7§4/p9§7; REPORT DOC-004 p4 | Earlier missing collection-date exclusion versus later inclusion is an expressly disclosed change; dated/undated valid samples distinguish analysis sets. | CONTEXT_RESOLVES |
| PLAN DOC-002 pp18-21,28; PLAN DOC-003 p4footnote; REPORT DOC-001 pp2-3 | Protocol day3 versus SAP/report day2 uses explicit medicationday1→day0 renumbering, preserving the two-day interval. | CONTEXT_RESOLVES |
| PLAN DOC-002 pp11,22,28; PLAN DOC-003 pp6-8; REPORT DOC-001 p3 | Sample-size paragraph broadly names sensitivity/specificity/AUC/two assays under primary endpoint; repeated dedicated hierarchy and sensitivity power define the quantitative-sensitivity primary analysis. | CONTEXT_RESOLVES |
| PLAN DOC-002 pp19,27-28; PLAN DOC-003 pp3,6,8-9; REPORT DOC-001 p3 and all result displays | ROC/LR/screening-burden, baseline/day-change mixed model, non-sex subgroup and delayed-colonoscopy outputs are absent. No supplied result demonstrates changed primary/key-secondary inference or an unidentified number-producing analysis. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp28-29; REPORT DOC-001 pp3,6 | Exact sample-size test/continuity algorithm and sex-specific affected counts are absent; labeled normal diagnostics are compatible with printed totals and nominal power. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 p27 recruitment rule; REPORT DOC-001 pp1-4 | No recruitment count at half planned time is supplied, so inadequate-recruitment stop rule cannot be evaluated retrospectively. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 p27 safety rule; REPORT DOC-001 p4 | No numeric unexpected-serious-reaction rate boundary is supplied; unrelated serious events do not establish a stopping-rule contradiction. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp27-29; PLAN DOC-003 pp8-9; REPORT DOC-001 pp3,6 | No efficacy interim, NI/equivalence margin or multiplicity-adjusted decision rule supplied; no associated decision claim requires an invented rule. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp27,34 | General dropout reinclusion prohibition and later-colonoscopy reinclusion allowance are prospective operational statements; no affected primary/key-secondary value or analysis-population change established. | PERIPHERAL_COMPARISON |
| REPORT DOC-001 pp3-5; REPORT DOC-004 p8 | SiteSD=0/tinySD withP=.50 is coherent with reported zero-boundary hypothesis; likelihood statistic/reference law/df are unreported, so an alternative conventional P calculation is conditional. | CONDITIONAL_OR_UNREPORTED |
| PLAN DOC-002 pp10,15-17,30-32,42-43,59-62; REPORT DOC-001 pp2,7; REPORT DOC-005 p1 | Historical diagnostic/P/ROC, pharmacology, calendar, budget, bibliography and availability quantities are not current trial inferential results or decision rules. | OUT_OF_FOCUS |
| REPORT DOC-001 p5 Table3 women qualitative10.2 NPV | Provisional handoff upper limit3.8 is not the direct-source reading: source prints5.8; Agresti-Caffo gives5.791. Current main mapper and inventory use5.8. This is a transcription handoff matter. | NOT_REPRODUCED |

## Remaining limits and handoff

Scientific coverage is complete for all88supplied pages and116Srelationships. Mechanical limits are exact individual outcome P construction; group-specific unprinted CIs; individual interaction coefficients/P mappings; site likelihood statistics/reference distribution/df/fixed effects; exact planned continuity-correction implementation/sex-specific disease allocation; missingness evaluation/decision and duplicate participant-level data; exploratory outputs absent from package; interim recruitment data/numerical safety boundary; hidden-versus-visible eTable5 women differences. None supports a pass1 finding by itself.

Pass2 requires a different fresh gpt-6.1-sol/high agent. It must revisit S001-S116 against the complete candidate ledger, independent screening and mechanical recheck, then add PASS_2_COMPLETE to every record. This agent owns only statistics/relationship_inventory.md and checkers/statistical_pass_1.md; shared manifest/coverage edits belong to the coordinator.

## Explicit relationship completion records

This table enumerates every stable relationship; evidence, calculations and named unavailable inputs are recorded in the corresponding inventory row. Both endpoints of every paired supplemental record were completed.

| S ID | Pass 1 record |
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


