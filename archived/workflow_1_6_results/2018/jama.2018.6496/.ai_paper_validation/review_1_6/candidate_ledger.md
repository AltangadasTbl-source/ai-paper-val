# Workflow 1.6 Candidate Ledger

Pending Human Adjudication. Discovery began with all 49 source pages and every mapped relationship. Only records comparing the same printed inputs, comparator, and consistency rule were merged before stable IDs. No assigned ID may be deleted or renumbered. Evidence states and classifications below reflect the complete direct-source mechanical recheck; final independent audit is complete with no further classification repair.

## Classification table

| ID | Primary category | Relationship type | All relationships | Compared document roles | Review domain | Evidence state | Suggested review disposition |
|---|---|---|---|---|---|---|---|
| C001 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main Table 1 respiratory-indication row vs REPORT main Table 1 headers and sibling rows | statistical_results | recorded_candidate | retain |
| C002 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main Table 1 other-medical row vs REPORT main Table 1 headers and sibling rows | statistical_results | recorded_candidate | retain |
| C003 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main Table 2 operator rows vs REPORT main Table 2 header and final-physician footnote | statistical_results | recorded_candidate | retain |
| C004 | Statistical reporting inconsistency | S_W | S_W | REPORT main Table 3 all-patient duration interval vs REPORT main interval header and methods | statistical_results | recorded_candidate | retain |
| C005 | Denominator, proportion, or total inconsistency | P_P | P_P | PLAN protocol historical rescue counts vs PLAN same sentence percentage | plan_material | recorded_candidate | retain |
| C006 | Measure, label, or scale inconsistency | P_R | P_R | PLAN protocol duration endpoint vs REPORT main and results-supplement duration endpoint | protocol_report | recorded_candidate | retain |
| C007 | Measure, label, or scale inconsistency | P_P | P_P | PLAN protocol primary definition vs PLAN protocol primary missing-data endpoint wording | plan_material | recorded_candidate | retain |
| C008 | Measure, label, or scale inconsistency | S_W | S_W | REPORT main pooled bougie-use resistance result vs REPORT main discussion population label | report_internal_inconsistency | record_input_error | discuss |
| C009 | Measure, label, or scale inconsistency | P_R | P_R | PLAN protocol hypoxemia observation window vs REPORT main and results-supplement observation window | protocol_report | recorded_candidate | retain |
| C010 | Denominator, proportion, or total inconsistency | S_W | S_W | REPORT main Table 1 initial oxygen denominators vs REPORT same table missingness footnote | statistical_results | recorded_candidate | retain |

## C001 — Respiratory-indication percentages use a different denominator

**Provenance:** NUM-A01; N044 with N039–N043 corroboration. Independent numeric-main checker.

**Exact source locations:** [Main PDF p.5, Table 1](../../jama_driver_2018_oi_180054.pdf#page=5), respiratory-indication row, headers and sibling rows; all REPORT.

**Printed inputs and rule:** Headers n=381 and 376, No.(%); row asthma/COPD/heart failure/pneumonia 16(5), 23(7). Under header denominators, 100×16/381=4.199% and 100×23/376=6.117%, rounding to 4% and 6%. Under medical denominators 318 and 315 they round to 5% and 7%. Sibling altered-mental-status rows use all-arm denominators. Whole percentages allow ±0.5 percentage point; both observed deviations exceed that allowance.

**Alternative and human question:** The row may intend medical-subset percentages, but that basis is not identified consistently. Determine the intended numerator, denominator and row/header label. Counts themselves are not shown to be wrong. Classification S_W: all conflicting printed content is within one REPORT; no plan discrepancy.

## C002 — Other-medical percentages change the denominator

**Provenance:** NUM-A02; N045 with N039/N040/N046–N048 corroboration. Distinct row/inputs from C001.

**Exact source locations:** [Main PDF p.5, Table 1](../../jama_driver_2018_oi_180054.pdf#page=5), Medical—Other row, headers and sibling rows; all REPORT.

**Printed inputs and rule:** 44(14), 41(13); headers 381/376. 100×44/381=11.549%→12%; 100×41/376=10.904%→11%. Medical-subset bases yield 44/318=13.836%→14% and 41/315=13.016%→13%. Medical count subrows sum exactly 318 and 315; the candidate concerns displayed proportion bases. Whole-percent tolerance ±0.5 percentage point.

**Alternative and human question:** Row-specific medical denominators could be intended. Which basis should accompany the percentages, and should the row or header distinguish it? Classification S_W; shared possible cause with C001 does not permit merging distinct printed comparisons.

## C003 — Final-operator counts exceed the bougie arm total

**Provenance:** NUM-A03 and CROSS07; N076/N077/N078/N029 and X053. Genuine duplicates merged before ID assignment.

**Exact source locations:** [Main PDF p.6, Table 2 operator rows, header and footnote f](../../jama_driver_2018_oi_180054.pdf#page=6); all conflicting locations REPORT. PLAN operational form p.7 only corroborates category meanings.

**Printed inputs and rule:** Bougie n=381, senior/fellow 318, junior 57, faculty 8. Footnote lists the final intubating physician and mentions four physician changes per arm. 318+57+8=383, exceeding 381 by two; comparator 334+37+5=376 reconciles. One final physician per patient gives a mutually exclusive count total no greater than n. Integer tolerance zero; rounded percentages do not reconcile excess counts.

**Alternative and human question:** Rows could count operator episodes rather than one final physician, or one printed input could differ from intended data. How do final-operator counts reconcile to 381 and what counted unit does footnote f define? S_W; corroborating PLAN form does not add P_R.

## C004 — Duration confidence limits are printed in descending order

**Provenance:** NUM-A04, CROSS01 and STAT-A01 (statistical pass-1 endpoint-order relationship S040); N097 and X005/X064. Same printed interval/order rule merged.

**Exact source locations:** [Main PDF p.7, Table 3 all-patient duration](../../jama_driver_2018_oi_180054.pdf#page=7), interval header; [main PDF p.4 methods](../../jama_driver_2018_oi_180054.pdf#page=4); REPORT. [Results supplement PDF p.2](../../joi180054supp2_prod.pdf#page=2) is corroboration, with a different clustered analysis.

**Printed inputs and rule:** Difference 1 (4 to −1) seconds, P=.24. Lower-to-upper interval order requires first endpoint≤second endpoint: 4>−1. Sorted endpoints contain 1, but sorting is only a diagnostic and no correction is adjudicated. Hodges–Lehmann difference 1 need not equal 38−36=2. Clustered supplement prints 1 (−1 to 4), P=.95; differing P values are not a contradiction under differing analyses.

**Alternative and human question:** Confirm original unclustered lower/upper limits and any intended notation. Classification S_W; the supplement corroborates ordering but does not create a separate cross-document inferential discrepancy.

## C005 — Historical rescue percentage differs from direct rounding

**Provenance:** NUM-B01; N134/U010.

**Exact source locations:** [Protocol PDF p.7, lines 198–199](../../joi180054supp1_prod.pdf#page=7); historical background inside PLAN.

**Printed inputs and rule:** 70 out of 88 (79.6%). 100×70/88=79.5454545%, directly rounding to 79.5% at one decimal. Printed 79.6 has rounding interval [79.55,79.65), excluding the exact fraction by 0.0045455 percentage point. Printed-minus-exact 0.0545455 percentage point exceeds 0.05 allowance. Preceding 20/26 (76.9%) reconciles.

**Alternative and human question:** Intermediate double rounding or preservation of an external quoted percentage could explain 79.6; external literature is outside supplied evidence. Does 79.6 intentionally preserve an intermediate/quoted value or represent the direct percentage of 70/88? P_P, not trial REPORT inconsistency; no claim of trial-conclusion effect.

## C006 — Planned duration and reported duration use different stop events

**Provenance:** NUM-B02, CROSS03 and STAT-A02; N140/N173/N184, X016, S087. The same duration definition comparison is merged.

**Exact source locations:** [Protocol PDF p.9, lines 315–317](../../joi180054supp1_prod.pdf#page=9), [p.10 lines 346–347](../../joi180054supp1_prod.pdf#page=10), PLAN; [main PDF p.3](../../jama_driver_2018_oi_180054.pdf#page=3), [Table 3 p.7](../../jama_driver_2018_oi_180054.pdf#page=7), REPORT; [results supplement p.3 dagger](../../joi180054supp2_prod.pdf#page=3), REPORT. [Operational form p.10 attempt instructions preceding Q13](../../joi180054supp2_prod.pdf#page=10), PLAN, corroborates attempt boundaries.

**Printed inputs and rule:** PLAN time to intubation, first attempt only, ends at tracheal cuff inflation. REPORT first-attempt duration ends at blade removal, with planned-secondary labels and summaries 39/40 seconds (difficult) and 38/36 seconds (all). Different named stop events define different measures unless equivalence is supplied. No paired timestamps permit calculating the clock difference.

**Alternative and human question:** An amendment or deliberately distinct endpoint could explain the definitions; actual stop events might coincide. Which stop event generated the summaries and models, and how should the planned-endpoint label be read? Primary P_R; form labels attempt boundaries rather than a time-to-intubation stopwatch outcome, so it does not independently establish P_P. Classification ambiguity: potentially distinct/amended secondary endpoint, without a supplied amendment resolving alignment.

## C007 — Primary missing-data instruction names a secondary composite

**Provenance:** NUM-B03, CROSS04 and STAT-A04; N136/N161, X024, S089.

**Exact source locations:** [Protocol PDF p.8 §2.1](../../joi180054supp1_prod.pdf#page=8), [p.9 primary and secondary definitions](../../joi180054supp1_prod.pdf#page=9), [p.20 lines 719–720](../../joi180054supp1_prod.pdf#page=20), [p.21 lines 721–722](../../joi180054supp1_prod.pdf#page=21); all PLAN. Main primary definition is corroboration only.

**Printed inputs and rule:** Primary first-pass success A versus missing-primary video instruction to determine first-pass success without hypoxemia A∩B. A successful hypoxemic patient satisfies A but not A∩B. The explicit endpoint labels differ; no number of affected missing cases is supplied or inferred.

**Alternative and human question:** Secondary wording may have been copied, both components may have been retrieved independently, or the branch may never have been used. Which endpoint was intended under the primary missing-data clause? P_P; the agreeing main primary definition does not add a REPORT-versus-PLAN discrepancy.

## C008 — Resistance percentage changes its named population

**Provenance:** CROSS02; X039, N020 corroborating numeric scan. Numeric checker did not emit a count candidate because the arm-specific numerator is absent.

**Exact source locations:** [Main PDF p.5 Other Outcomes](../../jama_driver_2018_oi_180054.pdf#page=5), [p.7 continuation](../../jama_driver_2018_oi_180054.pdf#page=7), [p.9 discussion](../../jama_driver_2018_oi_180054.pdf#page=9), [p.4 randomized group sizes](../../jama_driver_2018_oi_180054.pdf#page=4); REPORT.

**Printed inputs and conditional rule:** 444 patients used a bougie at any stage; resistance 31 (7%), remedied in all but one. Discussion repeats 7% and all-but-one remedy but says intubations in the bougie group, whose randomized n=381. 31/444=6.982%→7%; if the same 31 were meant, 31/381=8.136%→8%. This conditional reassignment is not established as an actual analysis input.

**Alternative and human question:** Bougie group might informally mean all bougie-use patients; a distinct arm-specific numerator 25–28 among 381 also rounds to 7%. Is the repeated discussion percentage the same pooled result or a separately calculated randomized-group estimate? S_W and report_internal_inconsistency. Classification ambiguity: identity of the repeated result and intended population label. Direct-source rechecker assigns record_input_error: the 31/381 comparison relies on an unsupported numerator/population alignment; whether a residual label discrepancy exists cannot be settled. Suggested review disposition discuss is mechanically derived and is not human adjudication. No exact arm event count is invented.

## C009 — Hypoxemia window has a different end anchor

**Provenance:** NUM-B04, CROSS05 and STAT-A03; N139/N143/N172, X017, S088. Same observation-window rule merged; distinct from C006 continuous duration measure.

**Exact source locations:** [Protocol PDF p.9 lines 304–312](../../joi180054supp1_prod.pdf#page=9), [p.10 lines 340–354](../../joi180054supp1_prod.pdf#page=10), PLAN; [main PDF p.3](../../jama_driver_2018_oi_180054.pdf#page=3), [Table 3 p.7 footnote b](../../jama_driver_2018_oi_180054.pdf#page=7), [Table 5 p.9 footnote b](../../jama_driver_2018_oi_180054.pdf#page=9), REPORT; [results supplement p.3 asterisk](../../joi180054supp2_prod.pdf#page=3), REPORT.

**Printed inputs and rule:** PLAN window ends one minute after ETT cuff inflation; REPORT window ends one minute after completion of the attempt, defined by blade removal. Both have the same saturation threshold, but different anchors do not establish the same observation window. Reported fractions include 47/371 and 50/364 hypoxemia; composites 156/191 versus 123/177 and 317/371 versus 282/366. No affected events or changed percentages can be reconstructed.

**Alternative and human question:** Stop events may have coincided, or the window may have been deliberately amended/distinguished. Which interval generated the reported event fractions, including failed-attempt/rescue cases? P_R; agreeing REPORT definitions do not add S_C. Classification ambiguity: possible operational equivalence or amendment without paired timestamps or explicit supplied clarification.

## C010 — Initial oxygen missingness does not reproduce its denominators

**Provenance:** CROSS06; X048, N028/N037/N038.

**Exact source locations:** [Main PDF p.5, Table 1 initial oxygen rows, headers and footnote b](../../jama_driver_2018_oi_180054.pdf#page=5); all REPORT.

**Printed inputs and rule:** n=381/376; <90% rows 44/352 and 40/344, <80% 21/352 and 11/344. Footnote missing initial saturation 43, split 19/24. Same-measure available denominators would be 381−19=362 and 376−24=352. Printed 352/344 imply missing 29/32=61, 18 more than the footnote. Footnote 19+24=43 itself adds correctly; later Table 2 oxygen measures are a different time point.

**Alternative and human question:** Threshold rows could have additional exclusions or differ from the saturation summary, but no extra rule is supplied. Does one initial saturation measure support both median and threshold rows, and how do the footnote and denominator counts reconcile? S_W; missing extra-exclusion definition remains explicit.
