# Statistical pass 2 — supplementary nutritional count-test relationships

Runtime agent: /root/statistical_pass2_extra_a. Model: gpt-6.1-sol. Reasoning effort: high. Start mode: FRESH_SPAWN. Exact disjoint scope: S121, S122, S123, S124, S125, S126, S127, S128, S129, S130, S131, S132, S133, S134, S135, S136, S137, S138, S139, S140, S141, S142, S143, S144, S145, S146. This additional bounded shard does not replace the mandatory statistical pass-2 agent.

The complete QUALITY_CONTROL_SCOPE.md and review contract, assigned complete packet_03.md, complete current pass2_shared_context.md, current source-derived methods text, and the source-matched eTable 3 rendering were read. The shared context includes the full initial ledger, all screening decisions, all mechanical recheck facts, and all 53 original checker exclusions. No prior-run conclusions or external evidence were used. Both owned output artifacts are complete; canonical merges belong to the coordinator.

## Source authority and applicable checks

All 26 relationships concern [DOC-003 REPORT eTable 3, physical PDF p17](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=17), nutritional abnormalities through 12 years. The exact current rendering preprocessing/stat_extra_source17.png was visually reread: all assigned counts, N values, percentages, P values, abnormality definitions, group labels and footnotes match the preserved pass-1 transcription. Footnote a compares each SURG/procedure group with MED; footnote b defines N as participants with observed data. Anemia has its own observed-data denominators, 87 and 147; other assigned abnormalities use MED 88 and SURG 151, with procedure denominators 81, 37 and 33. These observed-data denominators are not substituted for randomized cohort totals or longitudinal model denominators.

The supplied [REPORT p6](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=6) states chi-squared or Fisher's exact tests for categorical adverse events/study outcomes. [REPORT p5](../../../../joi240004supp2_prod_1721756962.82552.pdf#page=5) describes secondary results as hypothesis generating without multiple-testing adjustment; p4's adjusted four-group primary-model comparisons do not establish that these separate nutritional tests use adjusted P values. No confidence interval, fitted effect estimate, standard error, or test statistic is printed in eTable 3. Thus point containment, CI order/null exclusion and estimate/CI/test compatibility are not applicable here. Frequencies establish observed direction without implying a fitted effect magnitude. No noninferiority, equivalence, interim or stopping conclusion is attached to these cells; no sample-size calculation is printed here.

The source-linked deterministic pass-1 Pearson and Fisher diagnostic calculations were reused after exact-source input confirmation. Pearson uses the reconstructed 2×2 table; one reference-distribution degree of freedom follows mathematically from that table and is not imported from an unspecified fitted model. Fisher probability ordering, sidedness, continuity-correction convention and exact per-row author software selection are not stated and are not inferred. The Fisher reconstruction is explicitly diagnostic; compatibility with the supplied test family suffices to avoid a fabricated method contradiction. All 24 numeric P values in this shard agree with the Pearson diagnostic within their own printed half-unit intervals, with zero interval gap and zero relative discrepancy. The two all-zero rows print NA, consistent with a degenerate Pearson event margin; a diagnostic Fisher value of one does not require the source to print a numeric test.

## Relationship-by-relationship pass-2 checks

Each row below was checked against its preserved full pass-1 record and the exact source display. All percentages are 100×events/N within their printed half-unit intervals; all counts are nonnegative integers not exceeding their denominators. Every assigned S record in statistics/parts/pass2_03_inventory.md separately retains PASS_1_COMPLETE and records PASS_2_COMPLETE with the applicable logic and limitations.

| S ID | Exact eTable 3 contrast; printed counts, percentages and P | Pass-2 test/precision fact | Count, direction and method implications |
|---|---|---|---|
| S121 | Anemia SURG vs MED: 35/147 (23.8%) vs 11/87 (12.6%); P .04 | Pearson diagnostic .037791055 lies in [.035,.045]; gap 0 | Higher SURG frequency; anemia-specific observed N; source inputs and allowed test family reconcile. |
| S122 | Anemia RYGB vs MED: 25/78 (32.1%) vs 11/87 (12.6%); P .003 | .002582461 lies in [.0025,.0035]; gap 0 | Higher RYGB frequency; observed N 78, not full surgical N; no CI conflict can be asserted. |
| S123 | Anemia SG vs MED: 8/36 (22.2%) vs 11/87 (12.6%); P .18 | .181084051 lies in [.175,.185]; gap 0 | Higher SG frequency; observed N 36; nonsignificance is compatible with the supplied count-test pair. |
| S124 | Anemia AGB vs MED: 2/33 (6.1%) vs 11/87 (12.6%); P .30 | .300188266 lies in [.295,.305]; gap 0 | Lower AGB frequency; 25+8+2=35 events and 78+36+33=147 observed surgical participants. |
| S125 | Low iron SURG vs MED: 48/151 (31.8%) vs 15/88 (17.0%); P .01 | .012594432 lies in [.005,.015]; gap 0 | Higher SURG frequency; source N and percentage reconcile; no adjusted-model estimate supplied. |
| S126 | Low iron RYGB vs MED: 30/81 (37.0%) vs 15/88 (17.0%); P .003 | .003310326 lies in [.0025,.0035]; gap 0 | Higher RYGB frequency; reference is MED, not the pooled surgical group. |
| S127 | Low iron SG vs MED: 10/37 (27.0%) vs 15/88 (17.0%); P .20 | .202812509 lies in [.195,.205]; gap 0 | Higher SG frequency; observed percentage direction and nonsignificant test do not conflict. |
| S128 | Low iron AGB vs MED: 8/33 (24.2%) vs 15/88 (17.0%); P .37 | .368868681 lies in [.365,.375]; gap 0 | Higher AGB frequency; 30+10+8=48 and 81+37+33=151 reconcile to SURG. |
| S129 | B12 deficiency SURG vs MED: 20/151 (13.2%) vs 8/88 (9.1%); P .34 | .335478869 lies in [.335,.345]; gap 0 | Higher SURG frequency; the exact printed B12 threshold is retained without clinical reinterpretation. |
| S130 | B12 deficiency RYGB vs MED: 15/81 (18.5%) vs 8/88 (9.1%); P .07 | .074161112 lies in [.065,.075]; gap 0 | Higher RYGB frequency; printed nonsignificance agrees with the reconstructed test. |
| S131 | B12 deficiency SG vs MED: 4/37 (10.8%) vs 8/88 (9.1%); P .77 | .765727009 lies in [.765,.775]; gap 0 | Higher SG frequency; counts/denominators/percentage and test are compatible. |
| S132 | B12 deficiency AGB vs MED: 1/33 (3.0%) vs 8/88 (9.1%); P .26 | .257820453 lies in [.255,.265]; gap 0 | Lower AGB frequency; 15+4+1=20 reconciles to SURG; diagnostic test selection does not assert the author option. |
| S133 | Vitamin D deficiency SURG vs MED: 35/151 (23.2%) vs 23/88 (26.1%); P .61 | .606966175 lies in [.605,.615]; gap 0 | Lower SURG frequency; no contradictory directional claim accompanies the row. |
| S134 | Vitamin D deficiency RYGB vs MED: 22/81 (27.2%) vs 23/88 (26.1%); P .88 | .880389589 lies in [.875,.885]; gap 0 | Higher RYGB frequency; observed frequency differs from pooled SURG direction without a contradiction. |
| S135 | Vitamin D deficiency SG vs MED: 2/37 (5.4%) vs 23/88 (26.1%); P .008 | .008166102 lies in [.0075,.0085]; gap 0 | Lower SG frequency; printed significant P reproduces; no interval is supplied. |
| S136 | Vitamin D deficiency AGB vs MED: 11/33 (33.3%) vs 23/88 (26.1%); P .43 | .432801079 lies in [.425,.435]; gap 0 | Higher AGB frequency; 22+2+11=35 and procedure N sum 151 reconcile to SURG. |
| S137 | Hypocalcemia SURG vs MED: 1/151 (0.7%) vs 0/88 (0); P .44 | .444269420 lies in [.435,.445]; gap 0 | Higher SURG frequency; sparse data do not justify imposing a preferred test instead of the stated test family. |
| S138 | Hypocalcemia RYGB vs MED: 1/81 (1.2%) vs 0/88 (0); P .30 | .295832583 lies in [.295,.305]; gap 0 | Higher RYGB frequency; observed percentages and reported-family test reconcile. |
| S139 | Hypocalcemia SG vs MED: 0/37 (0) vs 0/88 (0); P NA | Both event counts zero; Pearson event margin degenerate; diagnostic Fisher P=1 | Equal frequencies; NA is explicit, with no supplied numerical test or inferential claim to contradict. |
| S140 | Hypocalcemia AGB vs MED: 0/33 (0) vs 0/88 (0); P NA | Both event counts zero; Pearson event margin degenerate; diagnostic Fisher P=1 | Equal frequencies; 1+0+0=1 surgical event and N 151 reconcile; NA does not denote a display-zero P. |
| S141 | Elevated PTH SURG vs MED: 66/151 (43.7%) vs 29/88 (33.0%); P .10 | .101308072 lies in [.095,.105]; gap 0 | Higher SURG frequency; PTH threshold and observed N preserved; no CI or fitted coefficient supplied. |
| S142 | Elevated PTH RYGB vs MED: 41/81 (50.6%) vs 29/88 (33.0%); P .02 | .019873476 lies in [.015,.025]; gap 0 | Higher RYGB frequency; printed P and counts compatible; no multiplicity claim is manufactured. |
| S143 | Elevated PTH SG vs MED: 12/37 (32.4%) vs 29/88 (33.0%); P .95 | .954737513 lies in [.945,.955]; gap 0 | Lower SG frequency; near-equal rates and large P reconcile. |
| S144 | Elevated PTH AGB vs MED: 13/33 (39.4%) vs 29/88 (33.0%); P .51 | .507541324 lies in [.505,.515]; gap 0 | Higher AGB frequency; 41+12+13=66 and procedure N sum 151 reconcile to SURG. |
| S145 | Hypoalbuminemia SURG vs MED: 23/151 (15.2%) vs 9/88 (10.2%); P .27 | .273167137 lies in [.265,.275]; gap 0 | Higher SURG frequency; neighboring SG/AGB counts 5/4 corroborate 14+5+4=23, without expanding owned S scope. |
| S146 | Hypoalbuminemia RYGB vs MED: 14/81 (17.3%) vs 9/88 (10.2%); P .18 | .181367753 lies in [.175,.185]; gap 0 | Higher RYGB frequency; exact percentage, MED reference and supplied test family reconcile. |

## Screening, recheck and cross-source implications

The current screen already registers the prospective vascular/safety CMH versus retrospective chi-squared/Fisher mapping issue through F-XS-010, with F-ST1-008 recorded as its duplicate. Its exact-source recheck preserves unspecified CMH strata, broad chi-squared wording, sparse-outcome Fisher substitution and composite-versus-individual-row alternatives. This shard's successful reconstructed count tests do not supply the missing prospective test mapping and do not justify removing or re-emitting the existing issue. No stratified CMH calculation is inferred from aggregate eTable 3 counts.

The other current ledger and recheck facts concern distinct primary/binary model quantities, primary/key outcome specifications, mortality, baseline race accounting or plan enrollment/power. Their denominators, fitted methods and CIs are not imported into eTable 3. No current screening decision establishes a new inconsistency in these 26 count-test relationships.

All 53 original checker exclusion rows were read against the five route-A categories and the full display-precision rule. None identifies a newly qualifying inconsistency within S121–S146. The extra-statistical last-digit exclusion names S147/S152/S165/S180/S181 outside this shard, gives relative residual gaps far below .05, and contains no interval/test conflict. No new global route-A concern was identified from the supplied context; global exact-source exclusion review and any resulting findings remain the mandatory pass-2 agent's responsibility. The coordinator and primary pass-2 agent were informed, preventing duplicate registration.

## New findings

No newly qualifying finding in the assigned scope. No new finding identifier was assigned. Existing screened observations were not re-emitted.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|

Zero new apparent observations were excluded. Reconciled checks and named limitations remain in the relationship records rather than being counted as excluded observations.

## Provenance, limitations and closure

Compute device: CPU. Reused current-run direct engine: Poppler 26.01.0 for stat_extra_source17.png and stat_extra_methods4-6-layout.txt. No rendering, OCR, fresh extraction, numerical re-execution, custom Python or source modification was needed. Preserved diagnostic calculations are deterministic JavaScript arithmetic from exact-source confirmed inputs; they are not author-software identifications. Missing row-specific test selection, Fisher sidedness/probability ordering and any CMH stratum counts remain limitations. Absence of CI/SE/test-statistic/fitted-effect cells makes those checks not applicable rather than a scientific coverage gap.

Closure: 26 assigned relationships receive PASS_2_COMPLETE; 24 numeric count-test comparisons reconcile with zero precision gap; two explicit NA rows are checked; zero new findings; zero new excluded observations; no source-coverage gap in this shard. Durable inventory: statistics/parts/pass2_03_inventory.md. All current stable candidates remain Pending Human Adjudication.
