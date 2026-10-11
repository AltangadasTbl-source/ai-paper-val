# Numeric consistency review

- Runtime agent: 01a12955-73e0-70e1-8995-af54c921c97a
- Model / reasoning: gpt-6.1-sol / medium
- Start mode: FRESH_SPAWN
- Scope: all91 numeric relationships N001–N071 and N201–N220, every constituent row and cell, participant flow, treatment/analysis/available-data totals, events, rates, safety and concealment counts, effect-measure identity and linked denominators.
- Completed relationships:91. Findings:2. Excluded observations:8.
- Complete per-ID calculations and NUMERIC_CHECK_COMPLETE records: relationships/numeric_relationship_inventory.md.

Read QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md completely. Reconstructed checks independently from current supplied sources and the current evidence maps. Findings below were visually confirmed on new CPU Poppler26.01.0 renders of the exact supplied PDF pages. No previous candidate/report conclusions were inputs. No stable candidate IDs or dispositions are assigned here.

### F-NUM-001

**Title:** Sample-size paragraph total does not reconcile with four stated cell sizes.

**Relationships:** N024; linked S005. **Focus area:** A and C. **Proposed review domain:** statistical_results. **Proposed relationship type:** S_W.

**Exact compared locations and roles:** REPORT [main article PDF p4, printed p861, Sample Size paragraph, upper right column](../../../jama_bot_2019_oi_190007.pdf#page=4): total392 participants, parenthetical196 in each of4 possible intervention combinations, subsequent22% attrition and250 participants per combination. The conflicting counts are within the same paragraph. Direct visual confirmation: preprocessing/numeric_review/main-p4.png, rendered from this supplied page.

**Printed inputs:** “392 participants (196 in each of the 4 possible intervention combinations)” for evaluating main effects of each of two interventions. Active20%, control30%, two-sided alpha.05 and power.90;22% attrition and250 per intervention combination. The four-combination count is the stated factorial structure, not a rounded continuous input.

**Rule and calculation:** Four cells of196 require4×196=784 participants, not392. With displayed count196 allowed its half-unit interval[195.5,196.5], recomputed total[782,786]; total392 has interval[391.5,392.5]. Gap389.5 participants; relative discrepancy389.5/392=0.993622>0.05. Exact-integer arithmetic produces784 versus392. This is independent of selecting a statistical sample-size formula. The attrition sentence corroborates a per-cell interpretation:196/(1−.22)=251.282, close to250/cell, and four250 cells require1000 planned participants.

**Qualifying route:** Route A, category3 (counts within one paragraph/display); also a printed count changes the reading under category2.

**Affected result or extracted value:** Required pre-attrition sample size and the implied per-cell versus factor-level size underlying power for the primary MDD main-effect comparisons. Extracting392 as the full required sample yields half the total implied by four196 cells.

**Why context does not resolve it:** Route A count conflict. Although factorial pooling suggests392 might refer to one factor level, the paragraph explicitly calls392 participants the required size and puts196 in each of four combinations. Reconstructability of a plausible intended reading does not remove the observable printed count discrepancy.

**Alternatives and missing definition:**392 may designate each pooled factor level (two cells196+196), rather than the total across four combinations; alternatively196 may designate each of two pooled conditions rather than each factorial cell. The paragraph does not identify which unit392 counts. No preferred analysis or final replacement value is proposed.

**Exact human question:** Does392 denote the entire pre-attrition trial or one pooled factor level, and how should the statement196 in each of four intervention combinations be reconciled with that quantity and the subsequent250-per-combination target?

### F-NUM-002

**Title:** Planned and reported daily EPA+DHA quantities differ beyond display precision and stated manufacturing tolerance.

**Relationships:** N006,N203,N208. **Focus area:** D. **Proposed review domain:** protocol_report. **Proposed relationship type:** P_R; all relationships P_R. The matching two REPORT statements corroborate the same reported side and do not independently conflict.

**Exact compared locations and roles:** PLAN [protocol PDF p23, Omega-3 PUFA fish oils paragraph](../../../joi190007supp1_prod.pdf#page=23): intended EPA+DHA1.0g/day. PLAN [protocol PDF p18, intervention1a content](../../../joi190007supp1_prod.pdf#page=18):1000mg omega-3 fatty acids, and PLAN [protocol PDF p20, composition box](../../../joi190007supp1_prod.pdf#page=20): acceptable deviation90%–125%. REPORT [results supplement PDF p4, eAppendix2 first paragraph](../../../joi190007supp3_prod.pdf#page=4): daily two pills for one year,1412mg EPA+DHA. REPORT [main article PDF p1 abstract intervention](../../../jama_bot_2019_oi_190007.pdf#page=1) and [p2 Multinutrient Supplements](../../../jama_bot_2019_oi_190007.pdf#page=2):1412mg omega-3, EPA:DHA3:1. Exact matching chemical quantity is established most directly by protocol p23 and results supplement p4. Visual confirmation on protocol-p23.png and support-p4.png.

**Printed inputs:** Planned EPA+DHA=1.0g/day (=1000mg/day); reported EPA+DHA1412mg/day. Protocol composition allows90%–125% manufacturing deviation. Both define a daily one-year randomized supplementation intervention; no change of dose is disclosed in the cited passages.

**Rule and calculation:** Compare matched daily EPA+DHA amounts in common mg units. Widest displayed PLAN interval from1.0g is[950,1050]mg; REPORT1412mg interval[1411.5,1412.5]mg. Gap361.5mg; relative discrepancy361.5/1412=0.256020>0.05. Even allowing manufacturing tolerance generously, treating125% as[124.5%,125.5%] and applying its highest end to the largest planned amount gives maximum1050×1.255=1317.75mg. Remaining gap1411.5−1317.75=93.75mg; relative discrepancy93.75/1412=0.066395>0.05. The protocol1000mg integer display supplies a narrower interval, so the conservative calculation uses the broader1.0g statement.

**Qualifying route:** Route B.

**Affected result or extracted value:** The EPA+DHA dose of the randomized multinutrient intervention whose primary12-month MDD and secondary symptom effects are reported; extraction could record1000mg/day from the supplied protocol or1412mg/day from the results descriptions.

**Why context does not resolve it:** The two matched chemical quantities differ by41.2% at their printed centers. Both refer to EPA+DHA per day; differences between total fish-oil mass and active fatty-acid mass cannot reconcile these exact statements. Display precision and the protocol manufacturing allowance still leave a relative residual above0.05. This is an intervention-dose element explicitly in focus, affects exposure extraction, and lacks an immediate source-grounded dose amendment.

**Alternatives and missing definition:** There may have been an amended formulation or a difference between intended and produced dose; the protocol names a separate composition document C1.2 that is not supplied as an independent direct source. The actual final formulation release specification and whether1412mg describes the daily combined EPA+DHA rather than another manufacturing basis are human questions. Laboratory FAME composition fractions in the results supplement p5 do not supply capsule mass and do not establish an amended daily target. No production mechanism is inferred.

**Exact human question:** Which supplied specification governs the final daily EPA+DHA dose, and what documented formulation amendment or dose basis reconciles the protocol1.0g/day with the reported1412mg/day?

## Excluded observations

Only apparent issues screened out by this checker are listed. Checks that reconcile are recorded in the relationship inventory.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main PDF p3 Figure1 versus p2 eligibility; N008/N010 | Online BMI exclusion prints<15 rather than eligibility lower bound25. Telephone screening separately excludes18 withBMI<25. This is a screening-procedure threshold, with coherent flow totals and no changed printed analysis-population size or primary/key-secondary statistical decision rule established. | OUT_OF_FOCUS |
| REPORT main PDF p4/p6 and PLAN SAP p4; N023 | ≥70% adherence versus narrative more than70% is a threshold wording difference with no displayed exact-boundary participants or changed numeric result; the a priori definition is unambiguous. | TERMINOLOGY_OR_WORDING |
| REPORT main PDF p4; N024 |196/(1−22%)=251.282 versus250 per cell. Allowing196±.5,22%±.5pp gives[249.045,253.548]; printed250 interval[249.5,250.5] overlaps. Separate from total392 conflict. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main PDF p6 Table2 footnote d versus footnote f and p1/p7; N058 | Repeated supplements without therapy label beside22 events resolves immediately to with therapy from same-display footnote f and the four-arm counts; the numeric value22/256(8.6%) itself is consistent and no numeric direction is reversed. | TERMINOLOGY_OR_WORDING |
| REPORT main PDF p8/Table3 versus crude descriptive means/events; N066/N067,N056 | Crude PHQ/GAD differences and event-derived ratios differ from adjusted multiply imputed coefficients/ORs/HRs; the source explicitly defines adjusted models and effect coding. No crude computation is claimed. | MODEL_VERSUS_CRUDE |
| REPORT supplement PDF p12; N212 |211/1025=20.585% versus printed22%; conservative recomputed half-unit interval[20.5266,20.6442]%, printed[21.5,22.5]%, residual0.8558/22≈0.03890≤0.05. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT supplement PDF p12/p16; N212/N218 |Single-time biomarker subset range211–331 and paired-changeN335/334 differ slightly across descriptions. This peripheral available-data comparison does not change primary/key-secondary result or analyzed trial population; visit/subset bases are not identical. | PERIPHERAL_COMPARISON |
| PLAN protocol PDF p35 versus REPORT supplement PDF p12 and main p4; N205/N212 |FFQ264 versus250 items and TFEQ label18 with21-item table differ across instrument descriptions; no displayed primary/key-secondary result or analysis-population denominator relies on these counts. | PERIPHERAL_COMPARISON |

## Completion and limitations

All91 assigned N relationships have explicit NUMERIC_CHECK_COMPLETE rows. Every baseline count/percentage pair, country and education column total, screening and follow-up category, primary-event/factor count, person-month rate, safety total, support adherence row, and concealment count was checked. Table1 percentages and all four event-percent pairs reconcile after half-unit display intervals. The1025 randomized analysis population agrees in all report displays; available-data missingness matches each Figure2 panel. The239 dropout total is distinct from246 no-month12 measurements by source definition.

No scientific-coverage limitation. Arm-specific available-data adherence denominators are not printed; each reconstructed integer denominator set exactly sums to the printed row N and reproduces all16 percentages. These reconstructions are checks, not assertions of unavailable raw observations. Graphical means are not numerically labeled and were not digitized. Group summary percent-weight changes cannot be reproduced without individual baseline weights. Model-based estimates cannot be equated to crude event ratios. Full statistical inference and planned-analysis contrasts are independently reviewed in the statistical and cross-source lanes; the present numeric findings are not conditional on their conclusions.
