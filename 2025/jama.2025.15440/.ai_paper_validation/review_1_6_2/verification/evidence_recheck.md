# Mechanical evidence recheck — Workflow 1.6.2

Fresh evidence-rechecker stage: /root/evidence_rechecker, gpt-6.1-sol, high. Assigned stable set: C001; finding provenance F-ST1-001. The complete current-run ledger, initial screen, normative scope and review contract were read. Source-matched page visuals were authoritative; OCR/text were locators only. No old selection, external material, new OCR or source modification was used.

**Status:** Pending Human Adjudication

## C001 — Age-under-75 planned subgroup power

**Evidence state:** reproduced

**Review domain:** plan_material

**Relationship type:** P_P

**All relationships:** P_P

**Compared document roles:** PLAN protocol Table 4 affected power cell versus PLAN protocol Table 4 assumptions and all 23 other power cells.

**Classification ambiguity:** None for role, relationship or domain. The exact power implementation and underlying unrounded inputs are not named.

**Classification confirmation:** The table is prospective statistical-design content in the protocol's statistical-power appendix. Interim-informed inputs do not change this content's PLAN role. Every affected and compared location is inside one PLAN document; P_P is the sole and primary relationship under P_R > P_P > S_C > S_W and entails plan_material. Report context is not in conflict and creates no P_R relationship. No role, relationship, domain or transcription correction is required.

### Every location found and source/comparator matched

The protocol source is joi250068supp1_prod_1760999665.28862.pdf. Independently recomputed SHA-256: 3f599193f39b562d392dc919161fd3afa8c728d8652738f9c971ca327c01047a, matching the recorded unchanged source.

| Exact supplied location | Role | Location found / source matched | Comparator matched and purpose |
|---|---|---|---|
| [Protocol PDF p. 22, Table 4](../../../joi250068supp1_prod_1760999665.28862.pdf#page=22), Age <75 row, rightmost “Power for total of 5000, 2p<0.01” cell | PLAN | Yes; 34% is clearly printed in the specified column | Same-row 25% population, 2.52% patch, 2.96% active, ratio 2.5, 1.18% control, sample sizes 2924/4048 and other powers 41%/20%/52% all match |
| [Protocol PDF p. 22, Table 4](../../../joi250068supp1_prod_1760999665.28862.pdf#page=22), all six assumption rows, four power columns and two sample-size columns | PLAN | Yes; every cell transcribed below visually matched | All 23 other power cells and 12 sample-size cells inspected and independently recalculated; comparators, not further affected cells |
| [Protocol PDF p. 20, Table 2](../../../joi250068supp1_prod_1760999665.28862.pdf#page=20), sample-size heading and 2.5-year row | PLAN | Yes; heading says total sample size “continuity corrected”; row prints control 1.75%, active 4.41%, alpha .05, power 90%, total 1914 | Supports correction context; does not establish the exact Table 4 function |
| [Protocol PDF p. 21, Table 3](../../../joi250068supp1_prod_1760999665.28862.pdf#page=21), whole-trial assumptions and power headings | PLAN | Yes; original row: population 100%, patch 3.75%, active 4.41%, ratio 2.52, control 1.75%, n 1914/2649; revised ratio-2.5 rows: active/control 4.41%/1.77% and 4.82%/1.93% | Confirms total-trial-size and two-sided .05/.01 context; not another affected cell |
| [Protocol PDF p. 19, Appendix 2, “Sample size calculation”](../../../joi250068supp1_prod_1760999665.28862.pdf#page=19) | PLAN | Yes; explicitly assumes 1:1 allocation to equal control/active numbers | Additional direct source support: Table 3 covers whole-cohort sizes up to 5000 and Table 4 gives the same calculations for age/sex subgroups; supports m=Tf/2 |

Only one affected location is registered: Age <75 / total 5000 / 2p<.01. There is no repeated affected pattern. Every comparator was nevertheless inspected.

The direct Table 4 transcription is:

| Group | Population | Patch AF | Active AF at 2.5 years | Active/control ratio | Control AF | 90%-power subgroup n, .05 / .01 | Powers: 4000/.05, 4000/.01, 5000/.05, 5000/.01 |
|---|---:|---:|---:|---:|---:|---|---|
| Age <80 | 64% | 2.78% | 3.27% | 2.5 | 1.31% | 2642 / 3658 | 89% / 73% / 95% / 85% |
| Age ≥80 | 36% | 6.28% | 7.39% | 2.5 | 2.95% | 1135 / 1571 | 96% / 87% / 99% / 95% |
| Age <75 | 25% | 2.52% | 2.96% | 2.5 | 1.18% | 2924 / 4048 | 41% / 20% / 52% / 34% |
| Age ≥75 | 75% | 4.62% | 5.44% | 2.5 | 2.18% | 1563 / 2164 | 100% / 98% / 100% / 100% |
| Males | 54% | 4.94% | 5.82% | 2.5 | 2.33% | 1458 / 2018 | 98% / 92% / 99% / 98% |
| Female | 46% | 3.09% | 3.64% | 2.5 | 1.46% | 2367 / 3276 | 80% / 60% / 89% / 75% |

The active-rate column definition is patch rate × 1.177; the footnote identifies interim AF detection by patch. All age-under-75 values match the ledger exactly.

### Applicable rule and independent reproduction

The applicable rule is the registered same-display reproducing-method comparison and the scope's display-precision interval check. The registered Route A category 4 concerns a printed power not reproduced by a method that tracks the other display cells. This is a diagnostic reconstruction, not an assertion that the source used a named function or that a preferred method is required.

With control rate p0, active rate p1, subgroup fraction f and total trial T, define m=Tf/2, d=p1−p0, A=√[(p0+p1)(1−(p0+p1)/2)], B=√[p0(1−p0)+p1(1−p1)], z=Φ⁻¹(1−α/2).

Power (%) = 100{Φ[(√m d−zA−1/√m)/B] + Φ[(−√m d−zA−1/√m)/B]}.

The term 1/√m supplies the diagnostic continuity correction. Exact two-sided thresholds .05 and .01 use z=1.959963984540054 and 2.5758293035489004. Independent JavaScript V8 arithmetic used an erf-based CDF approximation, with an explicit outward ±0.00002 percentage-point numerical guard for the summed CDF/floating-point evaluation.

At p0=.0118, p1=.0296, f=.25, T=5000 and m=625, independent power is 28.585281%, agreeing with the recorded 28.585280% to less than .000001 percentage point. This approximation difference is not a source-transcription correction.

All 24 cells were recalculated; values below are reconstructed (printed):

| Group | 4000/.05 % | 4000/.01 % | 5000/.05 % | 5000/.01 % |
|---|---|---|---|---|
| Age <80 | 88.977874 (89) | 72.845977 (73) | 94.860067 (95) | 84.476660 (85) |
| Age ≥80 | 95.857850 (96) | 86.766867 (87) | 98.603992 (99) | 94.288019 (95) |
| Age <75 | 41.851153 (41) | 20.530754 (20) | 52.055448 (52) | 28.585281 (34) |
| Age ≥75 | 99.557460 (100) | 97.723140 (98) | 99.926443 (100) | 99.479987 (100) |
| Males | 97.938182 (98) | 92.261244 (92) | 99.443747 (99) | 97.260074 (98) |
| Female | 80.516912 (80) | 59.595357 (60) | 89.005329 (89) | 72.889320 (75) |

All 23 comparator cells satisfy the workflow precision rule. Even using the central input combination alone, each comparator's distance from its printed half-unit interval, divided by its printed value, is at most .021476 (Female / 5000/.01), below .05. Those central inputs lie inside every displayed-input rounding box, so allowing the full box cannot increase the minimum gap. Independent evaluation of all 16 corners per cell also agrees with the current-run computation record. Corner envelopes are preserved in the derivative; the affected-cell proof below uses full interval arithmetic and does not assume corners locate the global extrema.

Additional same-method support is supplied by the 12 sample-size outputs. At 90% power let K=zA+Φ⁻¹(.90)B, x=(K+√[K²+4d])/(2d), total subgroup n=2x². The independent outputs all differ by less than 1% at central inputs:

| Group | Reconstructed / printed n at .05 | Reconstructed / printed n at .01 |
|---|---|---|
| Age <80 | 2644.027 / 2642 | 3662.921 / 3658 |
| Age ≥80 | 1129.398 / 1135 | 1564.024 / 1571 |
| Age <75 | 2905.288 / 2924 | 4024.585 / 4048 |
| Age ≥75 | 1565.495 / 1563 | 2168.427 / 2164 |
| Males | 1457.054 / 1458 | 2018.125 / 2018 |
| Female | 2373.467 / 2367 | 3288.083 / 3276 |

These comparisons support the method reconstruction and assign no replacement number.

### Full display-precision interval check

Allow p0∈[.01175,.01185], p1∈[.02955,.02965], f∈[.245,.255], and conservatively T∈[4999.5,5000.5]. The .01 threshold is an exact decision rule, not a rounded observation. The printed 34% allows [33.5,34.5]%. Treating T as the exact design count would narrow the enclosure.

Allowing active/control rates to vary independently is conservative. Any inputs also obeying the displayed ratio, patch-rate and multiplier relationships lie inside this wider box; those constraints can only narrow it.

| Quantity | Conservative interval |
|---|---|
| m | [612.43875,637.56375] |
| d | [.0177,.0179] |
| A | [.201114780660,.201590860408] |
| B | [.200720539557,.201197552172] |
| First CDF argument | [−.606021786852,−.525184440686] |
| Second CDF argument | [−5.040078175893,−4.948728272239] |
| Power before numerical guard | [27.225033,29.972785]% |
| Power after outward numerical guard | [27.225013,29.972805]% |
| Printed interval | [33.5,34.5]% |

Both rates are below .5, so each Bernoulli variance in B increases over its box; p0+p1 is below 1, so the transformed variance in A increases over its box. Sums, products, positive square roots and division by positive B were propagated conservatively; Φ is increasing. The resulting enclosure does not rely on grid sampling or joint endpoint monotonicity. Numerical margins are outward.

The guarded minimum gap is 33.5−29.972805=3.527195 percentage points; relative discrepancy is 3.527195/34=.103741 > .05. The registered inconsistency is reproduced. The ledger's prior unguarded enclosure 27.225032–29.972784% and .103742 relative discrepancy are corroborated to numerical approximation precision. This record adds an explicit numerical guard without changing any source input.

### Inputs, alternatives and remaining human question

**Necessary inputs available:** Yes for the diagnostic and interval test. Total trial size, subgroup fraction, active/control proportions, sidedness, thresholds and 1:1 allocation are source grounded; every comparison output is visible. No cited-location or source-reading gap remains.

**Exact missing inputs or definitions:** The source does not name the software, version, function, exact/normal implementation, Table 4 continuity-correction convention, cell-specific method variation, or underlying unrounded subgroup/rate inputs. The previous table explicitly mentions continuity-corrected sample sizes, but the exact Table 4 implementation cannot be uniquely attributed from approximate same-display tracking. These missing definitions do not prevent reproducing the registered comparison.

**Source-grounded alternative interpretation:** A distinct calculation/correction convention or underlying input specific to the affected cell could account for 34%. Removing the correction from the same diagnostic gives 35.699810% at 5000/.01, within the workflow threshold of 34%, but 27.416397% at 4000/.01, versus that row's printed 20%. It therefore does not provide one consistent same-row explanation. The protocol says Table 4 gives the same calculations for subgroups and discloses no separate rightmost age-under-75 convention. These possibilities are human questions rather than established production explanations.

**Direct observation versus inferred explanation:** Direct source observations are the 34% cell, all displayed inputs/comparators, two-sided thresholds, prospective context, explicit 1:1 allocation and preceding continuity-corrected heading. The formula, same-display tracking and enclosure are independently reproduced calculations. Attribution of that exact software/algorithm to the authors and an explanation of how 34% arose remain inferred and are not established.

**Affected result or extracted value:** Planned age-under-75 subgroup power at total trial 5000 and two-sided .01. No discrepancy in an observed treatment-effect result is established by this record.

**Exact remaining human question:** Which power algorithm/correction convention and underlying inputs produced 34% for Age <75 at total trial size 5000 and two-sided .01, and can the same rules account for the row's 20% at 4000/.01 and all other Table 4 cells?

**Recheck fact determining evidence state:** The exact source prints 34%; all registered inputs and comparators match; the independently reconstructed conservative full-input enclosure remains separated from the printed interval by a relative gap above .05 under the same-display method. The sole evidence state is reproduced. C001 remains Pending Human Adjudication. No disposition or replacement value is assigned.

### Provenance, counts and limitations

Authoritative visuals inspected: current-run preprocessing/doc002-page-019.png, doc002-page-020.png, doc002-page-021.png and doc002-page-022.png; source-matched PyMuPDF 1.26.4 CPU renders at 200 dpi. tooling_record.md records GPU_USER_REQUESTED for approved RapidOCR/ONNX Runtime CUDA OCR. Existing GPU OCR served only as a locator. This agent performed no new rendering, OCR or installation.

Independent derivative: [recheck-initial-power-computation.json](../preprocessing/recheck-initial-power-computation.json), JavaScript V8 arithmetic.

Counts: 1 stable ID assigned; 1 completed recheck; reproduced=1; factual/transcription/classification corrections=0. All cited/affected locations and 23 power comparators were inspected. Exact undisclosed implementation and unrounded inputs remain the only limitation; no source-location coverage gap remains.
