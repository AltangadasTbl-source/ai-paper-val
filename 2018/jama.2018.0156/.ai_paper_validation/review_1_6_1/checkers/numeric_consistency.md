# Numeric consistency review — main report

Runtime agent ID: 01a128e7-cc36-7d53-98bd-05dedeb36905. Stage: fresh numeric_consistency_reviewer main shard, gpt-6.1-sol / medium. Scope: DOC-001, REPORT, jama_jabre_2018_oi_180004.pdf physical pages 1-9, stable main groups N001-N098 and all numeric implications of main statistical groups S001-S021. The separate support checker owns DOC-002/DOC-003. No legacy scientific conclusions or web evidence used. Contracts QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md read completely.

Current source-linked main evidence map, inventories and tooling record were read. Direct source layout text was checked with pdftotext 25.03.0 over all nine pages; source-linked existing renders for physical pages 4 and 6 visually checked for flow/table alignment. Derived text/images are aids; the supplied PDF is authority. No supplied source or pre-existing asset was changed.

## Completed coverage and calculations

All 98 main N groups have an explicit completed check in relationships/numeric_relationship_inventory.md. Its table-group enrichment covers 11 binary outcome tuples (ITT primary and three secondary outcomes; PP primary and three secondary outcomes; safety difficulty, failure, regurgitation), two compression-subset comparisons, CPC sums/complements, all baseline percentage rows and subgroup partitions, and every ETI-only complication. Main S003 sample-size recruitment inputs and S018 adjusted-estimate identity were considered without replacing their statistical analyses. Statistical interval/test derivation is owned by the independent statistical reviewers.

Each real-valued input/output retains its half-unit rounding interval. Participant/event count intervals are intersected with nonnegative integers and retain exact printed counts. Ratios and differences from those counts are compared with output display intervals. Where explicit fractions immediately resolve small display differences, the observation remains excluded under CONTEXT_RESOLVES; administrative contributor-cell differences use PERIPHERAL_COMPARISON. Fractional-count relaxation is not used.

Main numeric checks: randomized1020+1023=2043; ITT1018+1022=2040 after2+1 ineligibility exclusions; PP995+943=1938; printed safety1028+999=2027; BMV safety1014+14=1028; printed randomized-ETI safety1023−14−9−1=999. Rescue55+100=155 reason occurrences for146 patients can overlap under figure footnote. PP reason occurrences28 and85 need not equal exclusions because the footnote permits overlap. Activity, etiology, rhythm and CPC category counts sum to their own subgroup/population denominators. Favorable CPC1+2 and any-CPC survival1-4 reconcile all ITT and PP primary/survival counts.

## Findings

### F-NUM-001

The ETI safety population does not account for the directly intubated participant randomized to BMV under the stated actual-treatment rule.

- **Exact source locations and document roles:** REPORT [DOC-001 PDF p3, Statistical Analysis, safety-population definition](../../../jama_jabre_2018_oi_180004.pdf#page=3); REPORT [DOC-001 PDF p4, Figure, upper BMV branch and both safety-analysis boxes; Baseline Characteristics](../../../jama_jabre_2018_oi_180004.pdf#page=4); REPORT [DOC-001 PDF p6, Table 3, safety denominators](../../../jama_jabre_2018_oi_180004.pdf#page=6). Relationship inventory N010, N011, N017-N019 and N090.
- **Printed inputs:** p3 defines safety as “all treated patients according to the treatment actually received” and attributes unsuccessfully attempted ETI adverse events to ETI. p4 BMV branch:1020 randomized,1014 received BMV,6 did not receive BMV, comprising2 not in cardiac arrest,1 directly intubated because massive regurgitation did not allow BMV, and3 no resuscitation. ETI branch:1023 randomized;979 received ETI;21 attempted but impossible and received BMV;14 allocated ETI but received BMV without that attempted-ETI description;9 no resuscitation. ETI safety box:999 included and24 excluded, comprising14 crossover to BMV,9 no resuscitation and1 aged<18. BMV safety:1028=1014 allocated BMV/received BMV+14 allocated ETI/received BMV. Narrative safety total2027=1028+999. Table3 complication denominatorETI999, BMV1027; difficulty/failure ETI996.
- **Rule and calculation:** preserve the figure’s actual initial-treatment attribution and its explicit ETI age exclusion. The allocated-ETI safety contribution is1023−14−9−1=999, equivalently979+21−1=999. The allocated-BMV participant explicitly receiving direct ETI is not in the BMV safety constituent sum1014+14=1028 and is additional to those999 allocated-ETI contributors. Applying the stated all-treated actual-treatment rule therefore gives1000 ETI safety contributors and2028 total safety contributors, unless that one directly intubated participant has an additional eligibility/analysis exclusion that is not stated. No rescue-BMV participant is reclassified in this calculation: the figure retains them in BMV, and this observation concerns only the explicitly never-BMV crossover.
- **Display-precision interval check:** each integer participant count n retains[n−0.5,n+0.5); because a participant count is integer, the only admissible integer is n. Thus the unique direct-ETI crossover contributes1, cannot contribute0 within[0.5,1.5), and the ETI box’s existing999 contributors cannot simultaneously denote1000 within[998.5,999.5). This is participant membership accounting rather than a recomputed rounded percentage; the discrepancy remains under the source-defined integer constraint.
- **Focus area:** A, counts and denominators; C, population-definition logic.
- **Proposed review domain:** statistical_results. Proposed relationship: S_W; all compared content is one REPORT document.
- **Affected result or extracted value:** size and treatment attribution of the ETI safety analysis population and its adverse-event denominators; consequently extraction of ETI safety event proportions in Table3, especially regurgitation75/999, could depend on whether the directly intubated crossover was counted or additionally excluded.
- **Why context does not resolve it:** the figure explicitly exhausts the BMV safety membership with1014+14, while the ETI999 is exhausted by the allocated-ETI branch after its own24 exclusions. The direct-ETI crossover is in neither accounting. The safety definition says all treated according to actual treatment, and neither safety box supplies an exclusion for this person. The source identifies an outcome-specific denominator996 or1027 where relevant, but that does not identify whether this participant belongs to the overall ETI safety set or why they would be omitted.
- **Source-grounded alternatives and missing definition:** the999/2027 safety totals could be the intended populations with an additional unstated exclusion for the directly intubated crossover; alternatively the stated all-treated actual-treatment definition could include that participant in ETI, requiring different population membership/counts. Massive regurgitation is described as the reason BMV was impossible; the source does not say that this participant was excluded from safety or that it constituted a pre-resuscitation ineligibility exclusion. Without individual outcome membership, no event numerator adjustment is asserted.
- **Exact human question:** Was the participant randomized to BMV but directly intubated without receiving BMV included in the ETI safety analysis, and, if excluded, what safety-population rule accounts for that exclusion and the reported999 ETI/2027 total safety participants?

## Excluded observations

Every observation below has one reason code; repeated manifestations of the same observation are consolidated.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-001 p1/p4, N001 | Exact2040/2043×100=99.853157% versus printed99.8% lies just beyond display precision; explicit counts identify the intended completion value immediately. Integer counts remain exact. | CONTEXT_RESOLVES |
| REPORT DOC-001 p1/p5, N002/N028 |665 women in randomized2043 versus664 women in ITT2040 is compatible with the three excluded patients; the populations are explicitly distinct. | CONTEXT_RESOLVES |
| REPORT DOC-001 p1, N002 |665/2043=32.550% versus displayed32%; numerator and population are directly stated, so intended count/proportion is identifiable at once. | CONTEXT_RESOLVES |
| REPORT DOC-001 p1/p5, N002/N027 |Overall mean64.7 versus weighted ITT displayed means64.748; ±0.05-year group-mean intervals and distinct randomized population reconcile. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p1-p3, N003 |Follow-up-end date precedes a strict28-day interval from the final enrollment date; calendar comparison does not establish any missing primary result. | PERIPHERAL_COMPARISON |
| REPORT DOC-001 p4, N014-N016 |Rescue reasons55+100 exceed146, and PP reason occurrences exceed exclusion totals; figure footnote explicitly permits several reasons for the same participant and BMV PP23 is the difference from ITT1018. | CONTEXT_RESOLVES |
| REPORT DOC-001 p5, N030-N043 |Coexisting-condition prevalence rows do not form a mutually exclusive partition; summing them to100% is not source-grounded. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p5, N044-N048/N050-N053/N062-N066 |Rounded categorical percentages can sum slightly below/above100%; exact category counts sum to their printed subgroup totals. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-001 p5-p6, N026-N085/N090-N094 | Ordinary percentage cells round from exact counts. Amiodarone200/1018=19.646365% vs19.7%; ITTROSC397/1022=38.845401% vs38.9%; PPadmission289/995=29.045226% vs29.1%; difficulty134/996=13.453815% vs13.4% lie outside their output intervals, but explicit fractions immediately resolve their intended values. | CONTEXT_RESOLVES |
| REPORT DOC-001 p5, N068 |Epinephrine-dose contributor denominator is not reported; dose population cannot be inferred from all-group totals or drug-prevalence count alone. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p6, N081 |PP ETI CPC1 count34/943 is3.606%, printed3.5%; the explicit34 and943 and complete CPC distribution identify the intended reading at once. | CONTEXT_RESOLVES |
| REPORT DOC-001 p6, N080/S017 survival | Exact100×(54/995−51/943)=0.0188642pp versus printed0.1pp does not reconcile by rounding exact counts; printed fractions identify the near-zero contrast and intended extraction immediately. | CONTEXT_RESOLVES |
| REPORT DOC-001 p6, N080/S017 ROSC |PP ETI377/943=39.979%, printed30.0%; row342/995=34.372% and difference−5.6 jointly establish the intended approximately40.0% at once. This is an exploratory PP secondary display. | CONTEXT_RESOLVES |
| REPORT DOC-001 p1/p4/p6, N090/S010-S012 |Safety event denominators1027/1028/996/999 vary by outcome; explicit per-row fractions identify each extracted rate, without establishing which missing observations account for the differences. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p4, N022/S014 |Number of pauses27 versus16 yields11 count; printed difference “11 seconds” is a unit slip resolved by the same sentence’s explicit count outcome and monitoring threshold>2 seconds. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-001 p4/p6, N023/N072-N073 |ECMO and donation occurrence counts35+23+12+21=91 match post-hoc exclusion91; overlap is not established, so no contrary unique-person total is inferred. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p4/p6, N024/S020 |Post-hoc155 pre-ROSC intubations need not equal rescue146 plus directETI1 because exhaustive identical timing/population membership is not asserted. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-001 p3-p4, N074/S001/S018 |Hierarchical adjusted risk difference0.05 versus crude0.114 does not imply an effect-identity inconsistency. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 p3, S003 |956 per arm gives1912; recruitment target2000 is an increased target rather than an asserted exact product. | CONTEXT_RESOLVES |
| REPORT DOC-001 p3/p7, N009/N096 |Historical registry650000 versus649359 and BMV3% versus2.9% are rounded background descriptions, separate from this trial’s primary outcomes. | PERIPHERAL_COMPARISON |
| REPORT DOC-001 p3/p7, N009 |Historical OR0.38 “in favor of BMV” cannot be equated to a crude RR3/1.1; model/reference orientation and cited historical design are distinct. | MODEL_VERSUS_CRUDE |
| REPORT DOC-001 p7, N097 |Historical success91.8% and difficult-intubation9.2% do not sum100%; this cited background comparison does not change the present trial’s primary/key secondary results or population. | PERIPHERAL_COMPARISON |
| REPORT DOC-001 p4, S001 |Sentence says lower limit “greater” despite−1.64% below−1%; numbers, same-sentence noninferiority-not-demonstrated conclusion and repeated abstract/Key Points interpretation resolve intended relation immediately. | TERMINOLOGY_OR_WORDING |

Main shard summary:9/9 source pages reviewed;98 stable N groups complete, including all numeric implications of21 main S groups;1 finding;23 excluded-observation rows. No scientific coverage gaps. Limitations: individual participant records and reasons for outcome-specific missing observations unavailable; unreported modeled-analysis parameters and simulation state not inferred. Statistical CI/test questions are independently assigned, not claimed resolved here. Durable artifacts: relationships/numeric_relationship_inventory.md and checkers/numeric_consistency.md.

# Numeric consistency review: support shard

Runtime CODEX_THREAD_ID: 01a128e7-f3a0-7770-a947-d62dbe760872. Assigned scope: DOC-002 PDF pages 1-134, PLAN by content, and DOC-003 PDF pages 1-3, REPORT by content. Current mapper page coverage is 137/137. All 71 support numeric groups are checked and consolidated as N099-N155 (57 relationships); all 38 support inferential tuples/specifications receive numeric-implication checks. Main-article joins are assigned to the separate cross-source checker.

The complete QUALITY_CONTROL_SCOPE.md and Workflow 1.6.1 review contract were read. No previous candidate, checker, screening or report conclusions were used. Direct supplied PDFs govern source readings. Poppler 25.03.0 direct layout extraction confirmed the results supplement, original/final protocol statistical passages, final primary definition, accrual table, amendment center arithmetic and native SAP. Supplied-source renders confirmed DOC-003 p3 and scanned DOC-002 p130. No additional OCR was needed.

## Completed checks

Both eTable 1 column totals reconcile exactly: BMV sum 1018, ETI sum 1022, grand total 2040. All 21 row counts and their percentage denominators were checked separately in the inventory. No row exceeds its denominator. Column percentages sum 100.1% and 100.3%; 21 rounded one-decimal rows permit a cumulative deviation up to 1.05 percentage points in either direction.

The eTable 2 fractions reconcile with their percentages and expressly labeled absolute differences in percentages:
- First row: 43/971 = 4.428424% and 39/978 = 3.987730%; BMV−ETI = 0.440694 percentage points, inside printed 0.4 ± 0.05.
- Second row: 41/863 = 4.750869% and 45/1174 = 3.833049%; BMV−ETI = 0.917820 percentage points, inside printed 0.9 ± 0.05.

Both rows satisfy event count ≤ denominator and point containment within ordered printed intervals. The first row has total 1949 and favorable-event sum 82; the second has total 2037 and event sum 86. Their captions expressly identify different exclusion/reassignment analyses. Their differences are risk differences in percentage points, rather than ratios or odds ratios. No inference about the selected row-specific test or CI algorithm is supplied by this numeric check.

Across original protocol, final protocol and SAP, 956 per group implies 1912 required participants, while the separately stated recruitment target is 2000. The target adds 88 above the modeled requirement. Expected 3% versus 2%, absolute margin 1%, power 0.8, type-I 0.025 and 5000 Newcomb–Wilson simulations are consistently repeated. The stated simulation cannot be exactly reproduced without its algorithm or executable inputs; no substitute normal approximation is treated as authoritative. Planned center arithmetic is 15 + 5 = 20 and 20 × 100 = 2000, with the disclosed amendment 20 − 1 + 6 = 25.

All day-28/day-35 ascertainment windows, age ≥18 population definitions, missing-primary-as-no-success and secondary-nonmissing denominators, ITT/PP/AT definitions, 0-6 mRS, 1-5 CPC, 0-100 VAS, 0-4 Han scales and seven-component IDS rules were checked for their numeric meaning. Source-linked repetition and amendments remain in the inventory; prospective definitions and empty forms contain no observed flow/event totals to reconstruct.

One-decimal percentages retain[x−0.05,x+0.05), while integer participant counts remain exact. Center9 ETI71/1022×100=6.947162% is just below printed7.0% interval. Center18 BMV29/1018×100=2.848723% and ETI24/1022×100=2.348337% are just below printed2.9%/2.4% intervals. These administrative cells do not change any result, population size or decision rule: PERIPHERAL_COMPARISON. All remaining center percentages round from their explicit counts, and integer column sums reconcile.

## Findings

No numeric-support observation satisfies all four inclusion criteria after self-screening. No finding ID is assigned.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| REPORT [DOC-003 p2](../../../joi180004supp2_prod.pdf#page=2), eTable 1 centers 9 and 18; N135, N147 | Exact integer-count percentages6.947162%,2.848723%,2.348337% lie just outside displayed7.0%,2.9%,2.4% intervals. These administrative contributor cells do not change a reported result, analysis population or decision rule; other center cells round ordinarily. | PERIPHERAL_COMPARISON |
| REPORT [DOC-003 p2](../../../joi180004supp2_prod.pdf#page=2), eTable 1 whole columns; N155 | Rounded percentage columns sum 100.1% and 100.3%; both remain inside the 21-row display-precision envelope and counts sum to both N labels exactly. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN [DOC-002 p24](../../../joi180004supp1_prod.pdf#page=24), [p79](../../../joi180004supp1_prod.pdf#page=79), recruitment rows; N116 | Five patients per center per month over 24 months implies 120 rather than the planned 100 per center. Monthly administrative accrual projections do not define a different analysis-population size or planned statistical decision. | PERIPHERAL_COMPARISON |
| PLAN [DOC-002 p11](../../../joi180004supp1_prod.pdf#page=11), [p37](../../../joi180004supp1_prod.pdf#page=37), [p66](../../../joi180004supp1_prod.pdf#page=66), [p92](../../../joi180004supp1_prod.pdf#page=92), [p120](../../../joi180004supp1_prod.pdf#page=120), [p129](../../../joi180004supp1_prod.pdf#page=129); N113-N114 | 956 × 2 = 1912 differs from recruitment target 2000; the source explicitly distinguishes required per-group sample from total recruitment target. | CONTEXT_RESOLVES |
| PLAN [DOC-002 p12-p14](../../../joi180004supp1_prod.pdf#page=12), [p67-p69](../../../joi180004supp1_prod.pdf#page=67); N118 | Historical airway subgroup counts are not declared an exhaustive partition of the external cohort; 8487 + 1968 = 10455 and the supplied 40/120 and 69/573 percentages reconcile. These are background figures rather than CAAM analysis denominators. | PERIPHERAL_COMPARISON |
| PLAN [DOC-002 p55-p56](../../../joi180004supp1_prod.pdf#page=55), [p106-p107](../../../joi180004supp1_prod.pdf#page=106); N128, N127 | Unfilled forms define dates, units, dose and seriousness fields; no observed event total, denominator or patient value is printed. A flow/event discrepancy would require unreported entries. | CONDITIONAL_OR_UNREPORTED |
| PLAN [DOC-002 p52](../../../joi180004supp1_prod.pdf#page=52), [p103](../../../joi180004supp1_prod.pdf#page=103); N125 | IDS infinity denotes an impossible procedure, while the calculation instruction retains the attained finite score before abandonment; these are readily distinguished procedure-status and scoring conventions, with no numerical trial result here. | CONTEXT_RESOLVES |
| PLAN [DOC-002 p121](../../../joi180004supp1_prod.pdf#page=121), [p130](../../../joi180004supp1_prod.pdf#page=130), [p133](../../../joi180004supp1_prod.pdf#page=133); SF-S001 numeric implication | Scanned alternative prints +0.01 where native alternative and explicit lower-CI rule use −0.01; the same paragraph labels noninferiority and supplies null −0.01. The missing minus is immediately resolved by that local context and explicit decision rule. | NOTATION_OR_TYPOGRAPHY |
| PLAN [DOC-002 p22](../../../joi180004supp1_prod.pdf#page=22), [p36](../../../joi180004supp1_prod.pdf#page=36), [p77](../../../joi180004supp1_prod.pdf#page=77), [p91](../../../joi180004supp1_prod.pdf#page=91), [p121](../../../joi180004supp1_prod.pdf#page=121); N122 and OP-S002/SF-S016 | Broad ITT language and explicit data-use withdrawal rules alone do not supply a numerical randomized-versus-analyzed discrepancy; participant-specific withdrawals and actual denominator joins require report evidence assigned elsewhere. | CONDITIONAL_OR_UNREPORTED |
| REPORT [DOC-003 p3](../../../joi180004supp2_prod.pdf#page=3), both eTable 2 rows; N153-N154 | Exact reproduction of each CI and P tuple would require a selected test per row and a CI algorithm that this table does not state. The fractions, displayed risk differences, interval ordering and point containment reconcile; statistical diagnostic assessment is retained for the separate statistical reviewer. | CONDITIONAL_OR_UNREPORTED |

## Completion and limitations

Scope: 137 physical source pages; 71 numeric mapper groups; 57 stable N relationships; 38 support inferential numeric-implication checks; 0 findings; 10 excluded-observation groups. No count or denominator scientific-coverage gap. Exact simulation code and row-specific CI algorithms are unavailable; PLAN pages supply definitions and projections rather than realized trial-flow counts. Main-article joins, endpoint-amendment interpretation and inferential compatibility are assigned to the corresponding independent specialists.

Artifacts: relationships/parts/numeric_support_inventory.md and checkers/parts/numeric_support.md. Sources and reused assets preserved.


## Canonical numeric-stage closure

The coordinator losslessly appended the disjoint support checker part after both fresh agents completed, adjusting its source links from four to three parent levels. All three sources are covered. Stable N001-N155: main98 and support57 relationships; main statistical-tuple enrichment and support38 inferential numeric-implication groups preserve quantities without duplicate N IDs. Total findings1; excluded observations33 (23main+10support). Original complete support parts remain separately preserved.

Coordinator audit repair: precision explanations/reason codes were updated from the fresh quality auditor's exact-count calculations. Stable IDs, finding set, exclusion count, source facts and candidate registrations are retained. No source or legacy evidence asset was modified.
