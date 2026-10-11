# Cross-source consistency review — Workflow 1.6.1

Scope completed: DOC-001 physical PDF pp. 1-11; DOC-002 pp. 1-25; DOC-003 pp. 1-13, using all 122 main reconstruction records M001-M110 and M073a-M073l and all 45 support reconstruction groups U01-U45. The comparisons are grouped into 23 coherent relationship families below, below the 120-relationship shard bound. This is a fresh cross-source review, not a recovery of earlier conclusions. No candidate IDs or adjudications are assigned.

Read completely: START_PROMPT.md, QUALITY_CONTROL_SCOPE.md, workflow_1_6_1/review_contract.md; current source inventory, evidence-asset inventory, source coverage and tooling record; both new mapper reconstruction sections. The combined annexes were not read as one block. Targeted exact-source native/layout extraction used Poppler pdftotext 25.03.0, with visual confirmation using curator source-matched 200-dpi renders for DOC-002 p.9, DOC-001 p.3 and DOC-003 pp.6,10. Source-linked mapper transcriptions and mapping of non-result pages provide the remaining coverage context. Reused artifacts remained unchanged; no new derivatives, Python extraction, OCR, GPU, web or old review conclusions were used.

Roles by content: DOC-001 is REPORT; DOC-002 is PLAN; DOC-003 pp.1-5 and p.6 interim application are REPORT; its p.6 quoted protocol rule and pp.7-13 prospective form are PLAN. Links below resolve relative to this checker artifact.

## Completed comparison families

| Family | Reconstruction scope | Matching and completion |
|---|---|---|
| 1 | M001; U04,U18 | Randomized/enrolled/completed counts and eligibility matched abstract, narrative and flow; all757 randomized included, no follow-up loss. |
| 2 | M002; U13,U14 | Allocation ratio, block sizes, strata and envelope rules compared; primary analysis model unchanged; isolated stratum-name scope considered below. |
| 3 | M003; U05,U17,U42-U44 | First-device success vs laryngoscope insertion distinguished; switches within one insertion are first-device failures, explaining rescue table. Primary difficult subset198+182=380; overall381+376=757. |
| 4 | M003,M075,M078,M101; U06,U09,U11,U30,U33,U35 | Composite/hypoxemia definitions, thresholds, ascertainment and available-waveform denominators matched. No raw waveform inference. |
| 5 | M003,M076,M079,M090; U07,U12,U31,U34,U35,U42 | Prespecified duration clock vs reported clock compared; F-XS-001. Main and supplemental arm medians/IQRs match exactly. |
| 6 | M004; U03,U21-U23 |374/187,95%/86%,9% effect,80% power and two-sided.05 agree. Objective wording interpreted with power section. No noninferiority/equivalence margin specified. |
| 7 | M005; U02,U15,U37,U44 | Randomized first-device intervention and rescue discretion compared; historical bougie sizes are background; no discrepant randomized dose/duration identified. |
| 8 | M006; U20,U21,U25 | Primary chi-square, secondary subgroup/all-patient analyses,95% intervals and two-sided.05 matched. Summaries not all displayed are not replacement analyses. |
| 9 | M007; U21,U25 | Exploratory subgroups identified as unplanned; no prespecified multiplicity correction replaced; no significance-threshold conflict identified. |
| 10 | M008,M091,M092,M110; U20,U36 | Difficult380 and overall757 survival populations kept distinct; HR1.29(1.04-1.60),P.02 vs overallHR1.12(.97-1.30),P.12 matched captions/narrative. PH limitation disclosed consistently. |
| 11 | M009; U26 | Missing-primary video review and available-case secondary denominators compared. No demonstrated primary missingness or exclusion conflict. |
| 12 | M009; U19,U27,U28,U38 | Futility-only interim,DSMB discretion,safety stopping and continuation compared; primary-subgroup specification vs all507 interim inputs is F-XS-002. |
| 13 | M010-M019; U04,U13,U15,U18,U24 | Flow counts, deviations, no-device failures, actual-device analysis and nonrandomized refusals distinguished. No randomized population-size conflict identified. |
| 14 | M020-M049; U10,U17,U39-U41 | Baseline measurements/subjective difficulty and clinical labels aligned; descriptive values separated from inferential endpoints. |
| 15 | M050-M073,M073a-M073l; U39-U44 | Process fields, operator definitions, screen-use categories and laryngeal grades matched form; secondary/exploratory process comparisons treated under peripheral tier. |
| 16 | M074; U29,U35 | Primary191/198 vs150/182,96%vs82%,14-point difference matches abstract,Key Points,narrative,Table3 and cluster supplement. CI8-20 vs7-21 and interaction.36vs.35 belong to disclosed distinct models. |
| 17 | M075,M076; U30,U31,U35 | Difficult composite156/191 vs123/177 and duration39vs40 match; recalculated cluster effects/tests distinguished. |
| 18 | M077-M079; U32-U35 | Overall373/381 vs328/376,98%vs87%,11-point difference and composite317/371 vs282/366 match; duration38vs36 matches abstract. CI-order observation excluded below. |
| 19 | M080-M090; U17,U25,U42,U43 | Unplanned success subgroups matched narrative andTable3, including pooled grades2-4=101/104 vs54/90,97%vs60%; successful-attempt-only38vs34 separated from overall38vs36. |
| 20 | M093-M098; U05,U15,U42-U44 | Rescue8+48=56 first-device failures, same-insertion rescue and later insertion distinguished; no attribution conflict. |
| 21 | M099; U37,U44 | Bougie procedural clicks404/444,hold-up283/444,resistance31/444 and rotation maneuver matched; isolated discussion group wording considered below. |
| 22 | M100-M109; U08,U09,U15,U19,U45 | Hypoxemia13%vs14%,esophageal0vs3 matched abstract/narrative/tables; additional safety/form windows do not establish omitted key-secondary event counts. |
| 23 | M110; U01,U02,U10,U16,U23,U28 | Disclosures, protocol identity, background, timing and administrative context reviewed; no separate SAP, amendment text, structured Office/CSV source or additional primary/key-secondary result supplied. |

## Findings

### F-XS-001

**Title:** Prespecified time-to-intubation endpoint ends at cuff inflation, while reported first-attempt duration ends at blade removal.

**Compared locations and roles:**

- PLAN: [DOC-002 p.9, section2.2, lines315-317](../../../joi180054supp1_prod.pdf#page=9): time to intubation is the interval from beginning of the intubation attempt to inflation of the ETT cuff with the tube in the trachea. [PLAN p.10, lines346-347](../../../joi180054supp1_prod.pdf#page=10) specifies stopwatch measurement using that definition.
- REPORT: [DOC-001 p.3, Trial Outcomes](../../../jama_driver_2018_oi_180054.pdf#page=3) defines duration as insertion to removal of the laryngoscope blade. [REPORT p.7, Table3 footnotec and duration rows](../../../jama_driver_2018_oi_180054.pdf#page=7) repeats this clock and prints difficult-airway medians39vs40 seconds, difference−1(−6to3), and overall medians38vs36 seconds, difference1 with printed interval4to−1. [REPORT p.1 abstract](../../../jama_driver_2018_oi_180054.pdf#page=1) repeats overall38vs36 seconds.
- REPORT: [DOC-003 p.3, eTable1 duration footnote](../../../joi180054supp2_prod.pdf#page=3) also defines blade entry to blade removal; [REPORT p.2 duration rows](../../../joi180054supp2_prod.pdf#page=2) repeats39vs40 and38vs36 seconds.
- PLAN corroborating operational context: [DOC-003 p.10, Attempt1 instructions](../../../joi180054supp2_prod.pdf#page=10) defines an attempt from blade insertion to blade removal; [PLAN p.11, Attempt2 instructions](../../../joi180054supp2_prod.pdf#page=11) repeats that boundary. These instructions establish procedural attempt boundaries, not a separate explicit duration-outcome clock, and are not counted as an independent PLAN–PLAN relationship.

**Printed statements and comparison logic:** The clock starts with the attempt in both specifications. Its stop is expressly cuff inflation in the protocol and blade removal in both results documents. These are different procedural events, not an abbreviation, scale conversion or rounding difference. The source does not equate their timestamps or disclose an endpoint amendment. The observation concerns the defined endpoint, not a conjecture that a specific numerical median would change by a particular number of seconds.

**Focus area:** D, planned versus reported endpoint definition.

**Proposed review domain:** protocol_report.

**Proposed relationship type / all relationships:** P_R / P_R. The two REPORT sources agree with each other. The prospective form is corroborating operational context, not an additional duration result in conflict.

**Affected result or extracted value:** The first-attempt duration medians39vs40 seconds in difficult airways and38vs36 seconds overall, reported as a planned secondary outcome and included in the abstract. Extraction as the protocol's time until cuff inflation would treat blade-removal duration as a different endpoint.

**Why context does not resolve it:** The report's local footnote makes the reported endpoint clear, but does not reconcile it with the explicit prespecified cuff-inflation endpoint. The supplied package does not state that cuff inflation and blade removal coincide or that one endpoint replaced the other. A reader can identify the two clocks but cannot decide that the same timing outcome was measured under both specifications.

**Supported alternatives / missing definition:** The duration endpoint may have been changed to laryngoscope-in-mouth time; alternatively, cuff inflation may have been used during collection despite the repeated reported blade-removal definition. The supplied form supports the reported procedural boundary but contains no patient-level timestamps or duration-outcome amendment that selects between these alternatives.

**Human verification steps:** Compare protocol section2.2 and measurement section3.2 with report Table3 footnotec and eTable1 footnote. Establish which event stopped the stopwatch and whether a dated endpoint amendment exists. Determine whether the reported medians should be interpreted as attempt duration or as the prespecified time to cuff inflation. No replacement analysis or correction is proposed.

### F-XS-002

**Title:** The futility-only interim report uses all-enrolled success rates, while the plan restricts the interim to the primary outcome in the difficult-airway analysis population.

**Compared locations and roles:**

- PLAN: [DOC-002 p.13, lines427-431](../../../joi180054supp1_prod.pdf#page=13) identifies patients with any difficult-airway characteristic as the primary analysis population. [PLAN p.20, lines693-706](../../../joi180054supp1_prod.pdf#page=20) calls this the main analysis and distinguishes all enrolled patients as secondary.
- PLAN: [DOC-002 p.21, section8.6.2, lines730-742](../../../joi180054supp1_prod.pdf#page=21) specifies interim after500 enrolled, analysis “for the primary outcome only,” projection to1000 equally allocated with control success unchanged and bougie second-half success15percentagepoints higher,capped100%, stopping for futility if no difference is found. [DOC-003 p.6 quoted protocol block, PLAN by content](../../../joi180054supp2_prod.pdf#page=6) reproduces that restriction and decision rule.
- REPORT: [DOC-003 p.6, paragraphs below the quotation](../../../joi180054supp2_prod.pdf#page=6) reports after507 enrolled: bougie250/257(97%) and tube/stylet213/250(85%); using the stated assumptions the trial was not stopped for futility.
- REPORT contextual population confirmation: [DOC-001 p.4, Figure1 and Trial Patients](../../../jama_driver_2018_oi_180054.pdf#page=4) gives final overall757 and final difficult-airway380; [REPORT p.1 abstract](../../../jama_driver_2018_oi_180054.pdf#page=1) distinguishes primary380 from secondary all757. The [REPORT p.4 interim-method paragraph](../../../jama_driver_2018_oi_180054.pdf#page=4) defers details to Supplement2.

**Printed statements and comparison logic:**257+250=507, exactly the reported total enrolled at interim. This interim analysis set cannot be the primary difficult-airway subset: its507 exceeds even the final difficult-airway total380. Thus the printed input proportions are all-enrolled rates. The plan's main outcome analysis is the difficult-airway subset, whereas all-patient success is designated secondary. The interim report explicitly links the all-enrolled rates to applying the quoted futility assumptions; it provides no difficult-subset interim rates or separate application to that subset. Rounding of97% and85% does not affect this population comparison.

**Focus area:** D, planned interim analysis population and decision rule.

**Proposed review domain:** protocol_report.

**Proposed relationship type / all relationships:** P_R / P_R. The quoted PLAN rule and protocol agree; the REPORT input rates are the other side of the comparison.

**Affected result or extracted value:** The reported continuation decision following the futility-only interim, and which analysis population's success rates supplied the planned primary-outcome futility projection. This is a planned decision-rule comparison, not a peripheral per-time-point observation count.

**Why context does not resolve it:** The primary outcome's difficult-airway analysis population is stated explicitly and distinguished from the all-patient secondary analysis. The interim appendix nevertheless applies the quotation to denominators covering all507 enrollees. It does not label this as an additional DSMB analysis or explain why the primary-population restriction has a different meaning for futility. DSMB discretion permits additional analyses but does not identify the printed one as such or supply the planned primary-population calculation.

**Supported alternatives / missing definition:** The DSMB may have used all-patient first-attempt success as the operative futility population; alternatively, a difficult-airway futility calculation may have been performed in addition to the presented overall rates. Neither is established by the supplied appendix. This finding does not assert that the continuation decision would differ if the difficult-airway rates were used.

**Human verification steps:** Establish whether section8.6.2's primary-only restriction included the primary analysis population; check which participants supplied the actual projected contingency table and whether a difficult-subset calculation or amendment was documented. Distinguish any additional discretionary DSMB analysis from the planned primary-outcome interim. No preferred interim method is proposed.

## Excluded observations

Each observation appears once and has exactly one scope reason code. Fully matching relationships are documented in the completed-family table rather than inventing discrepant observations.

| Location | Observation | Reason code |
|---|---|---|
| REPORT [mainp.7](../../../jama_driver_2018_oi_180054.pdf#page=7), [supplementp.2](../../../joi180054supp2_prod.pdf#page=2) and [supplementp.3](../../../joi180054supp2_prod.pdf#page=3) | Primary/composite/overall CIs and P values differ in the clustering analysis, but its heading and footnote expressly state that difference,P and interactionP are recalculated for physician clustering while arm columns are unchanged. This repeated model contrast is resolved. | CONTEXT_RESOLVES |
| REPORT [mainp.7](../../../jama_driver_2018_oi_180054.pdf#page=7) and [supplementp.2](../../../joi180054supp2_prod.pdf#page=2) | Overall duration CI printed4to−1 in main and−1to4 in supplement; point1 is inside the same pair of limits and the intended interval is immediately identifiable. | NOTATION_OR_TYPOGRAPHY |
| REPORT [mainpp.1,5](../../../jama_driver_2018_oi_180054.pdf#page=5) and [mainp.7](../../../jama_driver_2018_oi_180054.pdf#page=7) | Overall duration38vs36 and successful-attempt-only38vs34 have different analysis sets explicitly labeled; difficult-only39vs40 also separate. | CONTEXT_RESOLVES |
| REPORT [mainp.5](../../../jama_driver_2018_oi_180054.pdf#page=5), [mainp.8](../../../jama_driver_2018_oi_180054.pdf#page=8) and [supplementp.4](../../../joi180054supp2_prod.pdf#page=4) | Difficult-only HR1.29/P.02 and overallHR1.12/P.12 are different explicitly identified populations, not conflicting matched results. | NOT_REPRODUCED |
| REPORT [mainp.7](../../../jama_driver_2018_oi_180054.pdf#page=7) and PLAN [protocolp.9](../../../joi180054supp1_prod.pdf#page=9) | First-pass/first-attempt success wording and switches on the same blade insertion distinguish first-device failure from successful later rescue; no success definition conflict remains. | TERMINOLOGY_OR_WORDING |
| PLAN [protocolp.13](../../../joi180054supp1_prod.pdf#page=13), [formp.9](../../../joi180054supp2_prod.pdf#page=9) and REPORT [mainp.2](../../../jama_driver_2018_oi_180054.pdf#page=2) | Cervical immobility/immobilization,facial or neck trauma/facial trauma,airway edema/obstruction and blood/vomit/body fluids are field-resolvable descriptions of difficulty; no primary-subset membership discrepancy is demonstrated. | TERMINOLOGY_OR_WORDING |
| PLAN [protocolp.11](../../../joi180054supp1_prod.pdf#page=11) and REPORT [mainp.3](../../../jama_driver_2018_oi_180054.pdf#page=3) | Planned randomization stratum also lists apparent facial/neck trauma; report lists obesity or cervical immobilization. No actual alternative primary analysis set, primary-model covariate, or changed endpoint result is established by this isolated allocation-description comparison. | CONDITIONAL_OR_UNREPORTED |
| PLAN [protocolpp.20-21](../../../joi180054supp1_prod.pdf#page=20) and REPORT [mainp.4](../../../jama_driver_2018_oi_180054.pdf#page=4) | Missing-primary paragraph refers to first-pass success without hypoxemia, but primary is repeatedly defined as first-pass success; no missing primary forms or primary exclusions are demonstrated. The isolated outcome-name wording does not make the reported191/198 and150/182 unclear. | TERMINOLOGY_OR_WORDING |
| PLAN [protocolpp.20-21](../../../joi180054supp1_prod.pdf#page=21) and REPORT [mainp.4](../../../jama_driver_2018_oi_180054.pdf#page=4) | Planned video recovery/exclusion vs “missing data were left as such” does not establish that available video was unused; absent waveform explains relevant available-case denominators. | CONDITIONAL_OR_UNREPORTED |
| PLAN [protocolp.20](../../../joi180054supp1_prod.pdf#page=20) and REPORT [mainp.4](../../../jama_driver_2018_oi_180054.pdf#page=4) | Planned ITT excludes no intubation attempt and non-Macintosh patients, whereas all randomized participants appear in report; flow shows all randomized patients had blade insertion and all used Macintosh blades. | NOT_REPRODUCED |
| PLAN [protocolp.19](../../../joi180054supp1_prod.pdf#page=19) and REPORT [mainp.3](../../../jama_driver_2018_oi_180054.pdf#page=3) | Planned1yearor1000 with possible extension vs stopping above374difficult; actual report spansSeptember2016-August2017, one year. It does not establish that the reported threshold caused completion before the planned calendar stopping criterion. | CONDITIONAL_OR_UNREPORTED |
| PLAN [protocolp.11](../../../joi180054supp1_prod.pdf#page=11), [protocolp.19](../../../joi180054supp1_prod.pdf#page=19) and REPORT [mainp.3](../../../jama_driver_2018_oi_180054.pdf#page=3) | Aim “differs by more than9%” is accompanied by a detectable9% power difference and standard chi-square plan; no9% noninferiority or superiority margin test is specified. | CONTEXT_RESOLVES |
| PLAN [protocolp.19](../../../joi180054supp1_prod.pdf#page=19) and REPORT [mainpp.3-4](../../../jama_driver_2018_oi_180054.pdf#page=3) | Some planned summaries including mean/min/max and Kaplan-Meier percentiles are not printed; this alone does not establish replacement of the primary/key-secondary analysis. Stata12.1vs15.1 is software-version wording, not a shown statistical-result conflict. | CONDITIONAL_OR_UNREPORTED |
| PLAN [protocolp.19](../../../joi180054supp1_prod.pdf#page=19) and REPORT [mainp.4](../../../jama_driver_2018_oi_180054.pdf#page=4) | No multiplicity adjustment was planned in the supplied section; report explicitly uses.05 and no correction for exploratory subgroups. No conflicting multiplicity decision rule. | NOT_REPRODUCED |
| PLAN [protocolp.21](../../../joi180054supp1_prod.pdf#page=21) and REPORT [supplementp.6](../../../joi180054supp2_prod.pdf#page=6) |500planned vs507actual interim enrollment by itself is a timing/contributor-count difference; no precise500-only boundary or distinct statistical decision caused by the additional7 is established. | PERIPHERAL_COMPARISON |
| PLAN [protocolp.9](../../../joi180054supp1_prod.pdf#page=9), REPORT [mainp.7](../../../jama_driver_2018_oi_180054.pdf#page=7) and [mainp.9](../../../jama_driver_2018_oi_180054.pdf#page=9) | Hypoxemia window cuff inflation+1minute vs completion of attempt+1minute is adjacent-procedure wording; no waveform/timestamp evidence establishes differently classified primary/key-secondary events. The independently explicit duration endpoint is retained in F-XS-001. | CONDITIONAL_OR_UNREPORTED |
| REPORT [mainp.5](../../../jama_driver_2018_oi_180054.pdf#page=5) and [mainp.9](../../../jama_driver_2018_oi_180054.pdf#page=9) | Resistance7% described as bougie-group intubations vs31/444 across actual bougie uses. This procedural outcome is not primary/key-secondary and supplies no conflicted primary denominator. | PERIPHERAL_COMPARISON |
| REPORT [mainp.8](../../../jama_driver_2018_oi_180054.pdf#page=8) and [mainp.7](../../../jama_driver_2018_oi_180054.pdf#page=7) | Rescue table counts same-insertion success after first-device failure; primary success excludes switching. Definitions and caption immediately explain8+48failures. | CONTEXT_RESOLVES |
| REPORT [mainp.7](../../../jama_driver_2018_oi_180054.pdf#page=7) and PLAN [formp.10](../../../joi180054supp2_prod.pdf#page=10) | Actual-first-device result assigns11no-device patients their randomized device; footnote explicitly provides the rule, so categories402/355 are not contradictory randomized denominators381/376. | CONTEXT_RESOLVES |
| REPORT [mainp.9](../../../jama_driver_2018_oi_180054.pdf#page=9) and PLAN [protocolpp.12,18](../../../joi180054supp1_prod.pdf#page=18), [formp.13](../../../joi180054supp2_prod.pdf#page=13) | Patient-participation1minute and safety monitoring throughoutED/5minute arrest windows are different procedures; unprinted arrest categories do not establish a replaced primary/key-secondary outcome or missing event count. | CONDITIONAL_OR_UNREPORTED |
| REPORT [mainp.9](../../../jama_driver_2018_oi_180054.pdf#page=9) and [mainp.8](../../../jama_driver_2018_oi_180054.pdf#page=8) | Discussion points to FigureS1 for rotation while supplement's maneuver diagram is eFigure2; intended clinical maneuver is obvious. | PERIPHERAL_COMPARISON |
| REPORT [mainpp.5,8,10](../../../jama_driver_2018_oi_180054.pdf#page=10) and [supplementp.4](../../../joi180054supp2_prod.pdf#page=4) | Proportional hazards not upheld is disclosed in results,limitations and both captions; this is not an undisclosed cross-source assumption conflict. | CONTEXT_RESOLVES |

## Completion and limitations

Two findings and22 excluded observations. All23 assigned comparison families completed; no scientific coverage gap and no unreviewed matched-result occurrence identified. No Office/CSV sources or separate SAP supplied. Individual timestamps,waveforms,interim difficult-subset records and dated endpoint amendments are not supplied; this limits mechanical recalculation and causal interpretation, not source-unit review. F-XS-001 concerns an explicit endpoint definition; F-XS-002 concerns the demonstrated interim analysis population. Neither asserts a changed trial conclusion or recommends an analysis. Sources and all reusable assets were preserved.
