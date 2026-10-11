# Statistical pass 2 — support shard B

- Runtime agent ID: /root/statistics_pass2_support_b.
- Model / reasoning effort: gpt-6.1-sol / high.
- Start mode: FRESH_SPAWN; this runtime is different from every pass-1 runtime.
- Exact scope: DOC-004 REPORT, joi180108supp3_prod.pdf physical pages 7–9; S321–S438, all 72 eTable 3 mode/variable/occasion tuples, all 30 eTable 4 rows, and all 16 eTable 5 subgroup effect/95% CI rows with all eight shared interaction tests.
- Pass-2 closure: 118/118 relationships, each explicitly PASS_2_COMPLETE below and in statistics/parts/pass2_support_b_closure.md.
- New findings: 1, F-ST2-501. Excluded observations: 4 consolidated rows. Scientific coverage gaps: 0.

QUALITY_CONTROL_SCOPE.md and workflow_1_6_2/review_contract.md were read completely. Pass 2 reread the complete current C001–C009 ledger, initial screening log, mechanical recheck, all assigned pass-1 relationship records, and all 35 Excluded observations rows across the numeric, cross-source and three statistical-pass-1 artifacts. Earlier review conclusions and the web were not scientific inputs.

Exact supplied pp7–9 were reread using direct Poppler 25.03.0 `pdftotext -layout -f 7 -l 9 joi180108supp3_prod.pdf -`; exact main REPORT pp4 and 6 and PLAN SAP p14 were likewise reread with selected-page direct layout stdout. Current source-matched recheck/screening extracts were used for searching relevant definitions. Visual reading used the current independently source-confirmed p9 recheck rendering and curator-matched reusable pp7–8 images. Existing render provenance is Poppler 25.03.0 CPU for preprocessing/recheck-results-p9.png and UNKNOWN_LEGACY_RENDERER for reused review_1_5_2/preprocessing/rendered_pages/joi180108supp3_prod-p7.png and -p8.png. No fresh derivative was necessary; supplied sources, reused assets, pass-1 parts and canonical inventory were preserved.

## Rules applied to every assigned record

**T3-CONT:** All 48 eTable 3 continuous tuples were source-matched for arm, mode and occasion. Each median is contained in its ordered IQR. These are marginal medians/IQRs, not effect CIs; overlap, equal rounded medians or separate marginal-summary arithmetic cannot determine the between-arm P value. Row-specific continuous tests, raw ranks, test statistics and SEs are absent. No unavailable model or normal/rank test was assumed.

**T3-COUNT:** All 24 eTable 3 binary tuples were reread for numerator, denominator, percentage, P attribution and endpoint definition. Each count is at most its denominator and each ABG denominator is at most the printed mode contributor count for that arm/occasion. Every percentage reconciles under the displayed-input/output half-unit allowances and 0.05 relative-gap cutoff, including the 74/264 versus 27.9% cell and 6/161 versus 3.8% cell. The table explicitly says that smaller ABG denominators reflect missing measurements. Arterial pH<7.25 and respiratory acidosis (pH<7.35 AND PaCO2>45) are distinct endpoints. Both-zero rows show a dash, not a positive-count contradiction. Exact binary test variants are not supplied for this display.

**T4-IQR:** Every eTable 4 median is contained in its ordered IQR. Equal rounded medians/IQRs do not imply equal raw distributions, including lowest RASS day 3 P=.01 and colloid-volume P=.97. P is not an IQR-null test. Row-specific tests, SEs, test statistics and raw distributions are absent. S415 additionally has the newly emitted duration-window finding.

**T4-COUNT:** Explicit fractions and the seven rescue-therapy count/header-denominator pairs reconcile under the half-unit rule. The four implicit-denominator use rows have the arithmetic gaps listed below, all screened by relative discrepancy at most 0.05. No available-data denominator was invented to reconcile them. Counts and percentages were checked within the display, rather than dismissed as peripheral descriptive results.

**T5:** All 16 subgroup estimates remain in ordered 95% CIs. Low-minus-intermediate direction agrees with the half-unit allowances of the displayed means and estimate. Only the ICU subgroup CI excludes zero. The eight P values test interaction between subgroup and randomized arm, not each subgroup's treatment effect. Main REPORT p4 establishes Gaussian GLMs, two-sided reported P, alpha .05, no multiplicity adjustment and exploratory secondary analyses. It does not give subgroup n, CI-producing estimator, link, covariates, covariance, variance estimator, degrees of freedom or the CI-to-interaction estimator mapping. Missing details alone are not findings. No noninferiority/equivalence margin, efficacy interim boundary or numerical stopping conclusion applies to these displays.

## Recheck and cross-lane implications

The full ledger/recheck was considered without re-emitting any already screened issue. C006 has P_R only: the matrix's in-paper annotation is not an opposing prospective PLAN. C006's absent respiratory-rate primary-VFD subgroup is not supplied by any eTable 3 respiratory measurement or by eTable 5's eight pairs. C007's prospective zero-inflated versus reported Gaussian subgroup model applies to all S423–S438 and remains a planned-versus-reported issue, with the disclosed change retained. C003's eligibility question contextualizes S427–S428 without claiming a changed subgroup count. C009's exact visual row-attribution question is preserved for S435–S436, with no inferred category assignment or subgroup n. C001's binary-RR identity does not transfer to these mean-difference or percentage rows. C004/C005's primary endpoint/model comparisons and C002/C008's separate source tuples yield no further conflict in the assigned displays.

The main p6 and eTable 5 ICU/outside-ICU effects, limits and interaction P agree numerically. Calling the matching limits IQR in narrative is already considered by the screening/recheck and does not create another interval-versus-test finding. The visual C009 reading remains exactly as rechecked. No complete-case, randomization denominator, subgroup sample size, covariance or variance estimator was inferred from clinical convention.

## Recalculated display-precision check for the eight implicit percentages

For count a, header n and percentage p, recomputed percentage interval is [100(a−.5)/(n+.5), 100(a+.5)/(n−.5)]; p has ±.05 percentage-point allowance. Values below are independently recalculated.

| eTable 4 arm/row | Printed count/header and % | Recomputed interval (%) | Remaining gap / printed % |
|---|---|---|---:|
| Low sedative | 320/477; 70.6 | [66.910995,67.261280] | .046582 |
| Intermediate sedative | 333/484; 72.1 | [68.627451,68.976215] | .042632 |
| Low analgesic | 277/477; 61.1 | [57.905759,58.237146] | .046037 |
| Intermediate analgesic | 273/484; 59.1 | [56.243550,56.566701] | .042019 |
| Low neuromuscular blockade | 53/477; 11.7 | [10.994764,11.227702] | .036094 |
| Intermediate neuromuscular blockade | 60/484; 13.0 | [12.280702,12.512927] | .033621 |
| Low vasopressor | 363/477; 80.0 | [75.916230,76.285414] | .045807 |
| Intermediate vasopressor | 353/484; 76.4 | [72.755418,73.112720] | .042373 |

These are at most .05, so no reproduced route-A category-3 observation remains. This conclusion follows the numerical precision rule, not an assumption that these rows use smaller denominators.

## Shared interaction-test diagnostic review

The following is a **diagnostic approximation only**: derive SE from each CI width/3.92 and assume independent normal subgroup contrasts, giving z=|MD1−MD2|/sqrt(SE1²+SE2²), then a two-sided normal P. The half-unit ranges allow each printed MD and endpoint ±.005; 3.92 is held fixed as part of the diagnostic. No diagnostic is substituted for the reported Gaussian GLM.

| Shared S pair / subgroup | Printed interaction P | Diagnostic P | Diagnostic range from displayed MD/CI inputs |
|---|---:|---:|---|
| S423/S424 pneumonia | .16 | .473232 | [.469184,.477284] |
| S425/S426 sepsis | .17 | .187943 | [.185337,.190567] |
| S427/S428 oxygenation | .32 | .318242 | [.314467,.322031] |
| S429/S430 LIPS | .96 | .958165 | [.952831,.963477] |
| S431/S432 admission | .23 | .203439 | [.200747,.206147] |
| S433/S434 SAPS II | .26 | .254384 | [.250286,.258508] |
| S435/S436 prior ventilation | .98 | .981895 | [.979615,.984172] |
| S437/S438 intubation location | .01 | .007769 | [.007469,.008079] |

For pneumonia, the diagnostic SEs are 6.68/3.92=1.704082 and 3.26/3.92=.831633; contrast 1.36 gives z=.717231 and P≈.473232. Source P=.16 remains a different printed interaction test, and its two constituent subgroup CIs both include zero. Comparing that interaction P with either subgroup CI would compare different null hypotheses. The source does not establish that the pairwise-independent CI-width contrast is the interaction estimator. Numerical agreement for several other pairs is not evidence of the missing covariance/estimator mapping; sepsis and admission also differ under this diagnostic. Route A category 4 concerns a printed estimate or interval that a reproducing method does not reproduce; this diagnostic instead calculates a P under additional assumptions and does not reproduce a source-supported estimate/interval construction. Category 1 would apply to a reproduced interval/test conflict, but the two separate subgroup-effect CIs are not a CI for their interaction, and no source-supported compatibility conflict is established. The exclusion is therefore based on an assumed additional analysis relationship, not on dismissing a reproduced conflict because its production mechanism is unavailable.

## Prior checker exclusion reread

All 35 rows were independently reread against route A categories 1–5 and the display-precision rule: numeric 6; cross-source 14; statistical pass 1 main/plan 10; support A 1; support B 4. Source tuples outside S321–S438 remain owned by the other fresh pass-2 shards; their source-level closure is not claimed here. This shard independently revisited the eTable 4 count/percentage rows, eTable 5 pneumonia diagnostic and interval terminology, clinical/medical category wording, three-day display versus longer descriptive plan, the “35.” percentage, and empty dispersion parenthesis. None of those prior excluded rows establishes an additional reproduced always-register observation in this assigned scope. The newly found S415 numerical duration/window question was not a prior exclusion and is emitted below.

## Findings

### F-ST2-501

**Title:** The reported vasopressor-duration quartile leaves its time window unclear.

**Relationships:** S415.

**Exact locations and document roles:** REPORT [DOC-004 results supplement, physical p8, eTable 4 title, “Days of vasopressor use” row in both treatment arms, and median/interquartile-range footer](../../../../joi180108supp3_prod.pdf#page=8). The same REPORT's [physical p7, eTable 3 title and four occasion headings](../../../../joi180108supp3_prod.pdf#page=7) supplies a source-grounded alternative counting convention, not a second conflicting document. Both compared title and numerical row are REPORT within the results supplement.

**Printed values:** The eTable 4 title says “during the first three days.” “Days of vasopressor use” is 2 (1–4) in the low arm and 2 (1–4) in the intermediate arm, with P=.87. Its footer defines the summaries as median (interquartile range). The vasopressor footnote defines the qualifying drugs/dose but supplies no duration-counting rule or separate window for this row.

**Rule and calculation:** An accumulated duration confined to three elapsed days is bounded by 3 days, so its upper quartile cannot exceed 3. The upper-quartile reading 4 permits [3.5,4.5] under half-unit display allowances. The admissible upper-quartile interval for a duration bounded by 3 is [0,3], leaving gap 3.5−3=0.5 days, and relative discrepancy 0.5/4=0.125, above 0.05. The title describes a specified observation window, not a rounded numerical estimate; its three-day window is not enlarged by rounding. This calculation establishes the consequence of the printed elapsed-duration reading; it does not assert that the authors counted elapsed days rather than calendar days. The median and quartile endpoints are ordered and contain the median, and no conflict with P=.87 is asserted.

**Focus area:** C, an analysis description unclear about the time window/counting unit producing a printed duration; B, time-window attribution of a quantitative result.

**Proposed review domain:** report_internal_inconsistency.

**Proposed relationship type / all relationships:** S_W / S_W.

**Qualifying route:** Route B.

**Affected result or extracted value:** The low- and intermediate-arm vasopressor-duration distributions 2 (1–4) days, particularly whether the extracted 4-day upper quartile describes a three-day truncated elapsed duration, a count of calendar days touched, or a longer treatment course.

**Why context does not resolve it:** The title supplies a three-day horizon, while the printed upper quartile is four days. The nearby sedative, analgesic and neuromuscular-blockade duration rows do not identify an alternative rule for vasopressors. eTable 3, under a similar first-three-days title, lists the randomization-day occasion separately from days 1–3; that makes calendar-day counting or an additional partial day a plausible alternative, but does not define how eTable 4's duration was calculated. The footer gives the summary type only, and the vasopressor footnote gives the drug/dose definition only. This quantity-to-window assignment affects the duration a reader extracts, rather than merely varying the wording of the same unambiguous quantity. The quantity-changing-label comparison is in scope.

**Alternatives and missing definition:** Counting every calendar date with vasopressor exposure, including the randomization date plus days 1–3, could yield four counted dates without exceeding three elapsed days. The row could instead summarize a longer treatment course despite the table-wide title, or the intended quartile/title could differ. No alternative is chosen. Needed definitions are the row's exposure-window start/end and whether “days” means elapsed time or calendar dates touched. This is separate from screened F-XS-007: it compares a supplied numerical vasopressor quartile with its own table's horizon, not a planned full-course sedative/blocker endpoint with a reported partial-period summary.

**Exact human question:** What exposure window and counting rule produced the “Days of vasopressor use” summaries 2 (1–4) in both arms of eTable 4, and how does the 4-day upper quartile relate to the table's stated first-three-day horizon?

## Excluded observations

Only apparent issues decided not to emit appear here; checks that reconcile and already screened findings are in their relationship records.

| Location | Observation | Reason code |
|---|---|---|
| REPORT DOC-004 p8 eTable 4, four use rows, both arms | All eight count/header/percentage gaps independently recomputed above remain at most .05 after half-unit allowances. They therefore do not meet reproduced route A category 3. Consolidates the numeric and support-B pass-1 occurrences. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT DOC-004 p9 eTable 5, eight pairs, particularly S423/S424; REPORT main p4 method | Independent normal CI-width interaction diagnostic ≈.473 versus pneumonia P=.16 is not a source-supported estimator linkage. No interaction CI is printed; individual subgroup CIs and the shared interaction P test different nulls. The diagnostic table and named missing mappings above explain why no category-1 or category-4 conflict is reproduced. | CONDITIONAL_OR_UNREPORTED |
| REPORT DOC-004 p7 eTable 3 Other mode, after-titration respiratory acidosis | Printed “35.” for 7/20 has unambiguous numerical reading 35%, with no changed number or magnitude. | NOTATION_OR_TYPOGRAPHY |
| REPORT DOC-004 p9 eTable 5 footer | Empty parentheses in “Data are mean ()” do not alter the mean, ± dispersion entries or separately defined mean-difference 95% CIs. No numerical conflict follows from the missing dispersion abbreviation. | NOTATION_OR_TYPOGRAPHY |

## Explicit relationship closure

Every row records completion even where a producing-analysis definition is absent. The rules and precise missing definitions are given above; absent inputs were not supplied by convention.

| S ID | Exact REPORT source / row | Occasion | Pass 2 record |
|---|---|---|---|
| S321 | [DOC-004 p7 eTable 3 VCV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S322 | [DOC-004 p7 eTable 3 VCV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S323 | [DOC-004 p7 eTable 3 VCV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S324 | [DOC-004 p7 eTable 3 VCV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S325 | [DOC-004 p7 eTable 3 VCV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S326 | [DOC-004 p7 eTable 3 VCV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S327 | [DOC-004 p7 eTable 3 VCV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S328 | [DOC-004 p7 eTable 3 VCV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S329 | [DOC-004 p7 eTable 3 VCV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S330 | [DOC-004 p7 eTable 3 VCV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S331 | [DOC-004 p7 eTable 3 VCV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S332 | [DOC-004 p7 eTable 3 VCV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S333 | [DOC-004 p7 eTable 3 VCV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S334 | [DOC-004 p7 eTable 3 VCV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S335 | [DOC-004 p7 eTable 3 VCV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S336 | [DOC-004 p7 eTable 3 VCV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S337 | [DOC-004 p7 eTable 3 VCV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S338 | [DOC-004 p7 eTable 3 VCV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S339 | [DOC-004 p7 eTable 3 VCV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S340 | [DOC-004 p7 eTable 3 VCV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S341 | [DOC-004 p7 eTable 3 VCV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S342 | [DOC-004 p7 eTable 3 VCV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S343 | [DOC-004 p7 eTable 3 VCV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S344 | [DOC-004 p7 eTable 3 VCV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S345 | [DOC-004 p7 eTable 3 PSV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S346 | [DOC-004 p7 eTable 3 PSV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S347 | [DOC-004 p7 eTable 3 PSV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S348 | [DOC-004 p7 eTable 3 PSV, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S349 | [DOC-004 p7 eTable 3 PSV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S350 | [DOC-004 p7 eTable 3 PSV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S351 | [DOC-004 p7 eTable 3 PSV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S352 | [DOC-004 p7 eTable 3 PSV, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S353 | [DOC-004 p7 eTable 3 PSV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S354 | [DOC-004 p7 eTable 3 PSV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S355 | [DOC-004 p7 eTable 3 PSV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S356 | [DOC-004 p7 eTable 3 PSV, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S357 | [DOC-004 p7 eTable 3 PSV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S358 | [DOC-004 p7 eTable 3 PSV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S359 | [DOC-004 p7 eTable 3 PSV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S360 | [DOC-004 p7 eTable 3 PSV, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S361 | [DOC-004 p7 eTable 3 PSV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S362 | [DOC-004 p7 eTable 3 PSV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S363 | [DOC-004 p7 eTable 3 PSV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S364 | [DOC-004 p7 eTable 3 PSV, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S365 | [DOC-004 p7 eTable 3 PSV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S366 | [DOC-004 p7 eTable 3 PSV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S367 | [DOC-004 p7 eTable 3 PSV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S368 | [DOC-004 p7 eTable 3 PSV, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S369 | [DOC-004 p7 eTable 3 Other, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S370 | [DOC-004 p7 eTable 3 Other, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S371 | [DOC-004 p7 eTable 3 Other, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S372 | [DOC-004 p7 eTable 3 Other, FiO2](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S373 | [DOC-004 p7 eTable 3 Other, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S374 | [DOC-004 p7 eTable 3 Other, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S375 | [DOC-004 p7 eTable 3 Other, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S376 | [DOC-004 p7 eTable 3 Other, PaO2/FiO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S377 | [DOC-004 p7 eTable 3 Other, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S378 | [DOC-004 p7 eTable 3 Other, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S379 | [DOC-004 p7 eTable 3 Other, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S380 | [DOC-004 p7 eTable 3 Other, PaCO2 mmHg](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S381 | [DOC-004 p7 eTable 3 Other, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S382 | [DOC-004 p7 eTable 3 Other, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S383 | [DOC-004 p7 eTable 3 Other, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S384 | [DOC-004 p7 eTable 3 Other, Arterial pH](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-CONT; median/order/direction reread; row test/ranks/SE absent |
| S385 | [DOC-004 p7 eTable 3 Other, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S386 | [DOC-004 p7 eTable 3 Other, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S387 | [DOC-004 p7 eTable 3 Other, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S388 | [DOC-004 p7 eTable 3 Other, Arterial pH <7.25](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S389 | [DOC-004 p7 eTable 3 Other, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | After titration on randomization day | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S390 | [DOC-004 p7 eTable 3 Other, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 1 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S391 | [DOC-004 p7 eTable 3 Other, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 2 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S392 | [DOC-004 p7 eTable 3 Other, Respiratory acidosis](../../../../joi180108supp3_prod.pdf#page=7) | Day 3 | PASS_2_COMPLETE; T3-COUNT; count/denominator/% and endpoint/P mapping reread; sparse-test choice absent |
| S393 | [DOC-004 p8 eTable 4 Sedative infusion](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; recalculated implicit count/header gap≤.05; no new finding |
| S394 | [DOC-004 p8 eTable 4 Days sedative administration](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S395 | [DOC-004 p8 eTable 4 Analgesic infusion](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; recalculated implicit count/header gap≤.05; no new finding |
| S396 | [DOC-004 p8 eTable 4 Days analgesic administration](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S397 | [DOC-004 p8 eTable 4 Lowest RASS day 1](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S398 | [DOC-004 p8 eTable 4 Lowest RASS day 2](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S399 | [DOC-004 p8 eTable 4 Lowest RASS day 3](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S400 | [DOC-004 p8 eTable 4 Neuromuscular blockade](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; recalculated implicit count/header gap≤.05; no new finding |
| S401 | [DOC-004 p8 eTable 4 Days neuromuscular blockade](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S402 | [DOC-004 p8 eTable 4 Fluid balance 24h day 1 mL](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S403 | [DOC-004 p8 eTable 4 Fluid balance 24h day 2 mL](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S404 | [DOC-004 p8 eTable 4 Fluid balance 24h day 3 mL](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S405 | [DOC-004 p8 eTable 4 Use colloids](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S406 | [DOC-004 p8 eTable 4 Volume colloids](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S407 | [DOC-004 p8 eTable 4 Volume crystalloids](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S408 | [DOC-004 p8 eTable 4 Transfusion red blood cells](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S409 | [DOC-004 p8 eTable 4 Units red blood cells](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S410 | [DOC-004 p8 eTable 4 Transfusion fresh frozen plasma](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S411 | [DOC-004 p8 eTable 4 Units fresh frozen plasma](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S412 | [DOC-004 p8 eTable 4 Transfusion platelets](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S413 | [DOC-004 p8 eTable 4 Units platelets](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; median/order/P attribution reread; row test/raw distribution absent |
| S414 | [DOC-004 p8 eTable 4 Use vasopressors](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; recalculated implicit count/header gap≤.05; no new finding |
| S415 | [DOC-004 p8 eTable 4 Days vasopressors](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-IQR; ordered IQR; F-ST2-501 time-window question |
| S416 | [DOC-004 p8 eTable 4 Decreasing instrumental dead space](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S417 | [DOC-004 p8 eTable 4 Recruitment maneuvers](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S418 | [DOC-004 p8 eTable 4 Prone positioning](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S419 | [DOC-004 p8 eTable 4 Inhaled nitric oxide](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S420 | [DOC-004 p8 eTable 4 High frequency oscillatory ventilation](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S421 | [DOC-004 p8 eTable 4 Extracorporeal membrane oxygenation](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S422 | [DOC-004 p8 eTable 4 Extracorporeal CO2 removal](../../../../joi180108supp3_prod.pdf#page=8) | First 3 days; row-defined time | PASS_2_COMPLETE; T4-COUNT; explicit/header percentage and zero states reread; no new finding |
| S423 | [DOC-004 p9 eTable 5 Pneumonia](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S424 | [DOC-004 p9 eTable 5 Non-Pneumonia](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S425 | [DOC-004 p9 eTable 5 Sepsis yes](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S426 | [DOC-004 p9 eTable 5 Sepsis no](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S427 | [DOC-004 p9 eTable 5 PaO2/FiO2 ≤200](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context; C003 eligibility context |
| S428 | [DOC-004 p9 eTable 5 PaO2/FiO2 >200](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context; C003 eligibility context |
| S429 | [DOC-004 p9 eTable 5 LIPS ≥4](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S430 | [DOC-004 p9 eTable 5 LIPS <4](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S431 | [DOC-004 p9 eTable 5 Admission clinical](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S432 | [DOC-004 p9 eTable 5 Admission surgical](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S433 | [DOC-004 p9 eTable 5 SAPS II ≥50](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S434 | [DOC-004 p9 eTable 5 SAPS II <50](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S435 | [DOC-004 p9 eTable 5 Pre-randomization ventilation numerical line 1; duration label displaced](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context; C009 retained attribution question; no category assignment |
| S436 | [DOC-004 p9 eTable 5 Pre-randomization ventilation numerical line 2; printed beside >6 h](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context; C009 retained attribution question; no category assignment |
| S437 | [DOC-004 p9 eTable 5 Start ventilation ICU](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |
| S438 | [DOC-004 p9 eTable 5 Start ventilation outside ICU](../../../../joi180108supp3_prod.pdf#page=9) | VFD day 28 | PASS_2_COMPLETE; T5; MD direction/containment/order and shared interaction-null mapping reread; estimator/covariance/n absent; C007 context |

## Limitations and completion

118/118 S records and all eight shared interaction tests revisited. One new source-grounded finding, four excluded-observation rows, zero scientific coverage gaps. Intrinsic missing definitions remain row-specific continuous/sparse tests, subgroup n, CI-producing methods, interaction estimator mapping/link/covariance/variance/df, and S415 duration window/counting rule. No source or historical asset was modified, no web/legacy scientific conclusion was used, and canonical inventory updates are left to the coordinator.

