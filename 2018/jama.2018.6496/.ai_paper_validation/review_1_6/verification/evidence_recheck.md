# Workflow 1.6 Mechanical Evidence Recheck

Exact assigned stable-ID scope: C001, C002, C003, C004, C005, C006, C007, C008, C009, C010. All ten IDs are covered individually and remain **Pending Human Adjudication**. This record supplies evidence facts, not scientific adjudication. It does not remove, merge, or renumber any assigned ID.

## Direct-source authority and tooling

Read the complete `QUALITY_CONTROL_SCOPE.md`, `workflow_1_6/review_contract.md`, current ledger, and tooling record. Current checker provenance was consulted as a locator where needed. Earlier-run candidate or decision artifacts were not used. Reused OCR/text/images are not the final authority for any card below.

Freshly rendered every unique cited source page from the three supplied PDFs, and visually inspected all 16 renders through `view_image`. Engine: direct CPU-only Poppler `pdftoppm` and `pdftotext`, version 25.03.0, as recorded in `tooling_record.md`. For each page the exact command pattern was:

```bash
pdftoppm -f N -l N -r 125 -singlefile -png "SOURCE.pdf" ".ai_paper_validation/review_1_6/preprocessing/recheck-NAME-N"
pdftotext -layout -f N -l N "SOURCE.pdf" ".ai_paper_validation/review_1_6/preprocessing/recheck-NAME-N.txt"
```

The complete substitutions and derivatives are listed below. Both commands succeeded for every row. Fresh layout text is a transcription aid; visual inspection of the exact freshly rendered source page confirmed the cited content. No OCR, package installation, fallback interpreter, or GPU was needed. No supplied source or reused derivative was edited. Arithmetic below was reproduced with JavaScript and direct logical comparison; no scientific-review Python was used.

| Source PDF | N | NAME | Fresh render | Fresh layout text | Visual inspection |
|---|---:|---|---|---|---|
| jama_driver_2018_oi_180054.pdf | 3 | main | ../preprocessing/recheck-main-3.png | ../preprocessing/recheck-main-3.txt | Complete |
| jama_driver_2018_oi_180054.pdf | 4 | main | ../preprocessing/recheck-main-4.png | ../preprocessing/recheck-main-4.txt | Complete |
| jama_driver_2018_oi_180054.pdf | 5 | main | ../preprocessing/recheck-main-5.png | ../preprocessing/recheck-main-5.txt | Complete |
| jama_driver_2018_oi_180054.pdf | 6 | main | ../preprocessing/recheck-main-6.png | ../preprocessing/recheck-main-6.txt | Complete |
| jama_driver_2018_oi_180054.pdf | 7 | main | ../preprocessing/recheck-main-7.png | ../preprocessing/recheck-main-7.txt | Complete |
| jama_driver_2018_oi_180054.pdf | 9 | main | ../preprocessing/recheck-main-9.png | ../preprocessing/recheck-main-9.txt | Complete |
| joi180054supp1_prod.pdf | 7 | protocol | ../preprocessing/recheck-protocol-7.png | ../preprocessing/recheck-protocol-7.txt | Complete |
| joi180054supp1_prod.pdf | 8 | protocol | ../preprocessing/recheck-protocol-8.png | ../preprocessing/recheck-protocol-8.txt | Complete |
| joi180054supp1_prod.pdf | 9 | protocol | ../preprocessing/recheck-protocol-9.png | ../preprocessing/recheck-protocol-9.txt | Complete |
| joi180054supp1_prod.pdf | 10 | protocol | ../preprocessing/recheck-protocol-10.png | ../preprocessing/recheck-protocol-10.txt | Complete |
| joi180054supp1_prod.pdf | 20 | protocol | ../preprocessing/recheck-protocol-20.png | ../preprocessing/recheck-protocol-20.txt | Complete |
| joi180054supp1_prod.pdf | 21 | protocol | ../preprocessing/recheck-protocol-21.png | ../preprocessing/recheck-protocol-21.txt | Complete |
| joi180054supp2_prod.pdf | 2 | support | ../preprocessing/recheck-support-2.png | ../preprocessing/recheck-support-2.txt | Complete |
| joi180054supp2_prod.pdf | 3 | support | ../preprocessing/recheck-support-3.png | ../preprocessing/recheck-support-3.txt | Complete |
| joi180054supp2_prod.pdf | 7 | support | ../preprocessing/recheck-support-7.png | ../preprocessing/recheck-support-7.txt | Complete |
| joi180054supp2_prod.pdf | 10 | support | ../preprocessing/recheck-support-10.png | ../preprocessing/recheck-support-10.txt | Complete |

## Recheck summary

| ID | Primary category | Relationship type | All relationships | Review domain | Evidence state | Classification result |
|---|---|---|---|---|---|---|
| C001 | Denominator, proportion, or total inconsistency | S_W | S_W | statistical_results | recorded_candidate | Confirmed |
| C002 | Denominator, proportion, or total inconsistency | S_W | S_W | statistical_results | recorded_candidate | Confirmed |
| C003 | Denominator, proportion, or total inconsistency | S_W | S_W | statistical_results | recorded_candidate | Confirmed |
| C004 | Statistical reporting inconsistency | S_W | S_W | statistical_results | recorded_candidate | Confirmed |
| C005 | Denominator, proportion, or total inconsistency | P_P | P_P | plan_material | recorded_candidate | Confirmed |
| C006 | Measure, label, or scale inconsistency | P_R | P_R | protocol_report | recorded_candidate | Confirmed; operational-form locator clarified |
| C007 | Measure, label, or scale inconsistency | P_P | P_P | plan_material | recorded_candidate | Confirmed |
| C008 | Measure, label, or scale inconsistency | S_W | S_W | report_internal_inconsistency | record_input_error | Relationship retained; matched-result identity unestablished |
| C009 | Measure, label, or scale inconsistency | P_R | P_R | protocol_report | recorded_candidate | Confirmed |
| C010 | Denominator, proportion, or total inconsistency | S_W | S_W | statistical_results | recorded_candidate | Confirmed |

No relationship-type or primary-category correction is required. C008 requires an evidence-state change from provisional `recorded_candidate` to `record_input_error`. C006's corroborating form location is the attempt-definition heading before Q13, not the Q13 device field. All classifications use content roles and the required precedence; corroborating documents do not add discrepancy relationships.

## C001 — Respiratory-indication percentages

- **Location found:** Yes. [Main PDF p.5, Table 1](../../../jama_driver_2018_oi_180054.pdf#page=5), asthma/COPD/heart failure/pneumonia row; column headers; medical parent row; altered-mental-status sibling row.
- **Source value/text matched:** Yes. Respiratory row is `16 (5)` and `23 (7)` under columns headed No. (%) with n=381 and n=376.
- **Comparator matched:** Yes. Arm totals 381/376 and medical parent counts `318 (83)`/`315 (84)` are printed. Altered mental status is `185 (49)`/`173 (46)`, consistent with arm totals rather than the medical subset.
- **Consistency rule applicable:** Yes, conditionally on the displayed column bases. Numerator/denominator percentages rounded to whole percent should lie within 0.5 percentage point of the exact fraction. A different row-specific base needs identification if the same header otherwise governs the rows.
- **Calculation reproduced:** Yes. 100×16/381=4.199475%→4%; 100×23/376=6.117021%→6%. The printed 5%/7% lie beyond whole-percent rounding tolerance. The alternative bases reproduce the display: 100×16/318=5.031447%→5%; 100×23/315=7.301587%→7%.
- **Necessary inputs available:** All printed inputs for the header-based check and medical-subset diagnostic are available. **Missing definition:** an explicit respiratory-row denominator or documented exception to the common column basis.
- **Source-grounded alternative interpretation:** The medical parent immediately precedes the subrows, so medical-subset percentages could be intended. The sibling altered-mental-status percentages instead use whole-arm bases, leaving the table's basis inconsistent or insufficiently distinguished.
- **Direct observation versus inferred explanation:** The counts, percentages, arm totals, and medical totals are direct observations. The candidate's denominator interpretation and possible use of medical-subset arithmetic are inferences, not reconstructed raw data. No incorrect count is established.
- **Document roles:** Every compared location is REPORT: baseline results inside the main article. No PLAN comparison is involved.
- **Classification:** Primary category `Denominator, proportion, or total inconsistency`; primary relationship `S_W`; all relationships `S_W`; review domain `statistical_results`. Confirmed without correction. **Classification ambiguity:** none about the roles or relationship; the intended denominator remains the scientific question.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** the directly printed header-based percentages do not reproduce the row values, while the unlabelled medical-subset bases do; no source statement settles the row exception.
- **Exact remaining human question:** Should the respiratory row's percentages use all randomized patients or only medical-indication patients, and which denominator/label was intended for these two displayed proportions?

## C002 — Other-medical percentages

- **Location found:** Yes. [Main PDF p.5, Table 1](../../../jama_driver_2018_oi_180054.pdf#page=5), Other subrow within Medical, column headers, medical parent row, and medical sibling rows.
- **Source value/text matched:** Yes. The medical Other row is `44 (14)` and `41 (13)`.
- **Comparator matched:** Yes. Headers give n=381/376; Medical gives 318/315; medical subrow counts are 185,32,21,20,16,44 and 173,23,27,28,23,41. Their sums are 318 and 315.
- **Consistency rule applicable:** Yes, under the column bases. The proportion must reproduce the printed whole percentage within 0.5 percentage point; subrow counts themselves need not be changed to evaluate this rule.
- **Calculation reproduced:** Yes. 100×44/381=11.548556%→12%; 100×41/376=10.904255%→11%. These differ from 14%/13%. Medical-subset arithmetic gives 100×44/318=13.836478%→14%; 100×41/315=13.015873%→13%. Parent totals reconcile, and sibling altered-mental-status percentages use arm denominators.
- **Necessary inputs available:** Counts and both possible denominator pairs are available. **Missing definition:** the intended denominator of the medical Other percentages and any permitted row-specific percentage convention.
- **Source-grounded alternative interpretation:** The two percentages can be interpreted as percentages of the Medical subgroup, but that convention is not applied consistently to all medical subrows.
- **Direct observation versus inferred explanation:** Direct observations are the printed rows/headers and the internally additive counts. Use of a different denominator is inferred from arithmetic. No count error is inferred.
- **Document roles:** All conflicting locations are REPORT within main Table 1.
- **Classification:** Primary category `Denominator, proportion, or total inconsistency`; primary relationship `S_W`; all relationships `S_W`; review domain `statistical_results`. Confirmed without correction. **Classification ambiguity:** none about roles or relationship; row base is unresolved.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** header-denominator arithmetic does not reproduce either Other percentage, but medical-subset arithmetic does.
- **Exact remaining human question:** Were 14% and 13% intended as medical-subset percentages, and how should their basis be made consistent with the headers and adjacent subrows?

## C003 — Final-operator total

- **Location found:** Yes. [Main PDF p.6, Table 2](../../../jama_driver_2018_oi_180054.pdf#page=6), Operator rows, arm headers, and footnote f. [Operational form PDF p.7, question 2](../../../joi180054supp2_prod.pdf#page=7) was also found as a corroborating category locator.
- **Source value/text matched:** Yes. Bougie counts are senior resident/fellow 318, junior resident 57, faculty 8; comparator counts are 334,37,5.
- **Comparator matched:** Yes. Header n=381/376. Footnote f explicitly says the table lists the final intubating physician and reports 8 physician changes total, 4 per group. Form Q2 says to circle one training level.
- **Consistency rule applicable:** Yes. If rows list one final physician per patient, mutually exclusive final-physician categories cannot total above the arm patient count. An episode-count interpretation would require a different definition from the printed footnote.
- **Calculation reproduced:** Yes. Bougie 318+57+8=383, two above 381. Comparator 334+37+5=376. The four physician changes per group do not explain the excess under a final-only count. Rounded percentages cannot change this integer sum.
- **Necessary inputs available:** Printed counts, arm totals, and final-physician label are available. **Missing inputs/definitions:** the case-level final-physician counts and any actual rule allowing categories to overlap or operator episodes to be counted.
- **Source-grounded alternative interpretation:** The table may have inadvertently mixed initial/final operators or operator episodes, or one count may be a transcription issue. These are explanations to investigate, not observations established by this package.
- **Direct observation versus inferred explanation:** The sum 383 and final-physician wording are direct/reproducible facts. The production mechanism is unknown. No particular row is identified as the one to change.
- **Document roles:** Main Table 2 header, operator rows, and footnote f are REPORT. The blank prospective form Q2 is PLAN and only corroborates the one-category concept; it does not provide an independently conflicting value.
- **Classification:** Primary category `Denominator, proportion, or total inconsistency`; primary relationship `S_W`; all relationships `S_W`; review domain `statistical_results`. Confirmed without correction. The corroborating PLAN form adds no `P_R`. **Classification ambiguity:** none about role/type; the counted unit requires clarification.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** freshly inspected integer rows exceed the printed bougie arm n under the explicitly stated final-physician rule.
- **Exact remaining human question:** Which patients/operators contribute to the three bougie rows, and how should 383 listed final operators reconcile with 381 patients under footnote f?

## C004 — Duration interval endpoint order

- **Location found:** Yes. [Main PDF p.7, Table 3](../../../jama_driver_2018_oi_180054.pdf#page=7), all-patient first-attempt-duration row and Difference (95% CI) header; [main PDF p.4, statistical analysis](../../../jama_driver_2018_oi_180054.pdf#page=4); [results supplement PDF p.2, eTable 1](../../../joi180054supp2_prod.pdf#page=2) and [p.3, analysis note](../../../joi180054supp2_prod.pdf#page=3) as corroboration/context.
- **Source value/text matched:** Yes. Main all-patient row prints medians 38/36 seconds, difference `1 (4 to −1)`, and P=.24.
- **Comparator matched:** Yes. Column heading specifies a 95% CI. Main methods specify Hodges–Lehmann differences and confidence intervals for continuous variables. Supplement prints difference `1 s (−1 s to 4 s)` and P=.95 and explicitly states that Difference/P/interaction columns were recalculated for physician clustering.
- **Consistency rule applicable:** Yes. A confidence interval written as an endpoint range conventionally lists lower then upper bound. The main table's other ranges follow that convention. This is an endpoint-order check, independent of P-value reconstruction.
- **Calculation/logical comparison reproduced:** Yes. 4>−1: the main printed range descends. Reordering diagnostically gives [−1,4], containing estimate 1. This diagnostic does not assign the intended interval. A Hodges–Lehmann difference of 1 need not equal the marginal median subtraction 38−36=2. Different clustered P=.95 and unclustered P=.24 are not treated as a matched-analysis contradiction.
- **Necessary inputs available:** Printed point estimate, endpoints, CI header, and methods suffice for ordering. **Missing inputs/definitions:** original unclustered interval output is needed to identify the intended endpoints; model output is unnecessary for observing the printed order.
- **Source-grounded alternative interpretation:** The two endpoints may have been transposed. The independently clustered supplement's ordered range supports this possibility without establishing a final change to the main analysis.
- **Direct observation versus inferred explanation:** Descending endpoints are directly visible. Endpoint transposition is an inferred mechanism. P-value compatibility and paper-level consequences are not established by this check.
- **Document roles:** All main locations and results eTable/analysis note are REPORT. The discrepancy is internal to the main REPORT interval and its header/range convention; the second REPORT corroborates the plausible ordering rather than supplying a distinct conflicting inferential estimate.
- **Classification:** Primary category `Statistical reporting inconsistency`; primary relationship `S_W`; all relationships `S_W`; review domain `statistical_results`. Confirmed; no `S_C` added for corroboration. **Classification ambiguity:** none.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** direct source prints `4 to −1` in its 95% CI column, reproducing the descending-order observation.
- **Exact remaining human question:** What are the original lower and upper bounds for the main unclustered all-patient Hodges–Lehmann duration difference, and was the displayed endpoint sequence intended?

## C005 — Historical rescue percentage

- **Location found:** Yes. [Protocol PDF p.7, lines 196–203, especially 198–199](../../../joi180054supp1_prod.pdf#page=7).
- **Source value/text matched:** Yes. Historical observational-trial background states 20 out of 26 (76.9%) and 70 out of 88 (79.6%) attempts.
- **Comparator matched:** Yes. The numerator 70 and denominator 88 are in the same sentence as 79.6% and refer to that described historical success rate.
- **Consistency rule applicable:** Yes, for direct rounding of the printed ratio to one decimal place. This rule does not establish whether a historical quoted value intentionally underwent another rounding procedure.
- **Calculation reproduced:** Yes. 100×70/88=79.5454545%, which directly rounds to 79.5%. The printed 79.6% interval [79.55,79.65) excludes that exact fraction by 0.0045455 percentage point. Printed minus exact is 0.0545455 percentage point, above the 0.05 direct-rounding allowance. The preceding 100×20/26=76.9230769% rounds to printed 76.9%.
- **Necessary inputs available:** Printed historical numerator, denominator, percentage, and precision suffice. **Missing definition:** whether 79.6% preserves an external quoted value or intermediate double rounding. External articles were neither sought nor used.
- **Source-grounded alternative interpretation:** The protocol cites prior studies, so retaining their quoted percentage is possible. Intermediate 79.545...→79.55→79.6 is another arithmetic explanation; the supplied protocol does not identify either convention.
- **Direct observation versus inferred explanation:** Printed 70/88 (79.6%) and direct-rounding mismatch are direct/reproducible. Citation preservation and double rounding are inferred explanations. This comparison concerns historical background, not this trial's patient results.
- **Document roles:** Entire compared sentence is PLAN by content: historical data inside the prospective clinical-trial protocol.
- **Classification:** Primary category `Denominator, proportion, or total inconsistency`; primary relationship `P_P`; all relationships `P_P`; review domain `plan_material`. Confirmed; background source citations do not convert the sentence into a REPORT. **Classification ambiguity:** none about role/type; rounding convention is unresolved.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** the exact direct fraction fails the one-decimal rounding interval printed in the supplied PLAN; no stated alternative rounding convention settles it.
- **Exact remaining human question:** Was 79.6% intended as the directly rounded fraction 70/88, a preserved quoted historical value, or the result of intermediate rounding?

## C006 — Duration stop event

- **Location found:** Yes. [Protocol PDF p.9, lines 315–317](../../../joi180054supp1_prod.pdf#page=9) and [p.10, lines 346–347](../../../joi180054supp1_prod.pdf#page=10); [main PDF p.3, Trial Outcomes and Measurements](../../../jama_driver_2018_oi_180054.pdf#page=3), [main p.7, Table 3 rows/footnote c](../../../jama_driver_2018_oi_180054.pdf#page=7); [results supplement p.2, duration rows](../../../joi180054supp2_prod.pdf#page=2), [p.3, dagger note](../../../joi180054supp2_prod.pdf#page=3). The [operational form p.10](../../../joi180054supp2_prod.pdf#page=10) attempt-definition heading before Q13 was also found. Locator clarification: Q13 itself records device used; the attempted-end definition is in the heading above Q13.
- **Source value/text matched:** Yes. Protocol secondary outcome 2 is time to intubation (first attempt only), beginning of attempt to inflation of the ETT cuff when the tube is in the trachea; a research assistant records it with a stopwatch.
- **Comparator matched:** Yes. Main defines duration as blade insertion to blade removal; Table 3 footnote c and supplement dagger define the same stop. Table 3 labels duration a planned secondary outcome and prints difficult-airway medians 39/40 seconds and all-patient medians 38/36 seconds. The form defines an attempt as blade insertion→blade removal, but does not identify the secondary stopwatch endpoint.
- **Consistency rule applicable:** Yes, for alignment of the named planned continuous endpoint with its reported definition. Cuff inflation and blade removal are different named stop events unless an equivalence or change is supplied.
- **Logical comparison reproduced:** Yes. Planned duration = t(cuff inflation)−t(beginning of attempt); reported duration = t(blade removal)−t(blade insertion). Even if start events coincide, the stop-event labels differ. Their numeric difference cannot be calculated without paired timestamps, and no specific bias or difference is asserted.
- **Necessary inputs available:** Both explicit definitions, secondary labels, and reported summaries are available. **Missing inputs/definitions:** paired stop timestamps; any endpoint amendment or explicit mapping; the stopwatch stop instruction actually used to produce reported summaries/time models, including unsuccessful attempts.
- **Source-grounded alternative interpretation:** The report could intentionally describe a distinct or amended duration measure. Events may have been operationally near each other or coincident. The form's attempt definition may describe an operational boundary distinct from the protocol's successful-intubation stopwatch outcome.
- **Direct observation versus inferred explanation:** The two named endpoint definitions and planned-secondary report label are direct observations. Amendment, coincidence, and actual clock consequences are possible explanations, not supplied facts.
- **Document roles:** Protocol §§2.2/3.2 are PLAN. Main outcomes and reported Table 3 are REPORT; results eTable/notes are REPORT. Blank prospective form p.10 is PLAN by content.
- **Classification:** Primary category `Measure, label, or scale inconsistency`; primary relationship `P_R`; all relationships `P_R`; review domain `protocol_report`. Confirmed. No `P_P` is added: form attempt boundaries alone do not constitute a conflicting instruction for the same stopwatch measure. Main and results supplement agree, so they add no `S_C`. **Classification ambiguity:** potentially distinct/amended duration measure; the package does not resolve that alignment.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** both explicit duration definitions are present and have different stop labels, while a supplied equivalence/amendment for the planned-secondary report label is absent. The corrected form locator does not disprove the registered PLAN–REPORT comparison.
- **Exact remaining human question:** Which stop event generated the reported 39/40- and 38/36-second summaries and time analyses, and was the change from cuff inflation to blade removal an intended endpoint amendment or a separately labelled measure?

## C007 — Primary missing-data endpoint wording

- **Location found:** Yes. [Protocol PDF p.8, §2.1 lines 280–282](../../../joi180054supp1_prod.pdf#page=8); [p.9, lines 284–295 and 304–312](../../../joi180054supp1_prod.pdf#page=9); [p.20, §8.6.1 lines 719–720](../../../joi180054supp1_prod.pdf#page=20) continued at [p.21, lines 721–722](../../../joi180054supp1_prod.pdf#page=21). Main p.3 primary definition was inspected as corroboration.
- **Source value/text matched:** Yes. Primary outcome is first-pass success, satisfied by successful first-attempt intubation. Secondary outcome 1 is first-pass success without hypoxemia, requiring both successful first attempt and absence of hypoxemia.
- **Comparator matched:** Yes. Missing-data paragraph begins “For the primary outcome” on p.20 and continues on p.21 with video review to determine whether first-pass success without hypoxemia was achieved.
- **Consistency rule applicable:** Yes. Endpoint identity: first-pass success A differs from first-pass success without hypoxemia A∩B. Naming a primary endpoint cannot be treated as naming the secondary composite without an explanation.
- **Logical comparison reproduced:** Yes. A patient with successful first-pass intubation and hypoxemia belongs to A but not A∩B. This logical counterexample reproduces the endpoint-label distinction; it does not establish that any such missing case occurred or affected analysis.
- **Necessary inputs available:** Primary/secondary definitions and missing-data instruction suffice. **Missing inputs/definitions:** the actual retrieval instruction, whether A and B were recovered independently, case counts using this branch, and the endpoint coding applied in those cases.
- **Source-grounded alternative interpretation:** The secondary endpoint name may have been copied into the primary clause; video review may have obtained both components without replacing primary success; the branch may have been unused. None is established from supplied results.
- **Direct observation versus inferred explanation:** The inconsistent endpoint names are direct. Affected outcomes and branch usage are unknown; any copying explanation is inferred.
- **Document roles:** All conflicting definitions/instructions are PLAN within the clinical-trial protocol. Main REPORT primary wording only corroborates the ordinary primary definition.
- **Classification:** Primary category `Measure, label, or scale inconsistency`; primary relationship `P_P`; all relationships `P_P`; review domain `plan_material`. Confirmed; main corroboration adds no `P_R`. **Classification ambiguity:** none about role/type; operational handling of missing data is unresolved.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** the printed primary missing-data clause names the separately defined secondary composite rather than the primary outcome.
- **Exact remaining human question:** Did the primary missing-data clause intend to recover first-pass success alone or the no-hypoxemia composite, and what endpoint was actually coded if this branch was used?

## C008 — Resistance-result population identity

- **Location found:** Yes. [Main PDF p.5, Other Outcomes](../../../jama_driver_2018_oi_180054.pdf#page=5), continuation at [p.7 below Table 3](../../../jama_driver_2018_oi_180054.pdf#page=7), [p.9 discussion](../../../jama_driver_2018_oi_180054.pdf#page=9), and [p.4 randomized group sizes](../../../jama_driver_2018_oi_180054.pdf#page=4).
- **Source value/text matched:** Yes. Bougie was used in 444 patients; resistance was reported in 31 patients (7%), remedied by rotation/readvancement in all but one. Discussion says the resistance was observed in 7% of intubations in the bougie group and remedied in all cases except one.
- **Comparator matched:** The printed text is matched, but **matched-result identity is not established**. Randomized bougie arm n=381 is found. No randomized-arm resistance numerator is printed in these locations, and “bougie group” could informally denote all actual bougie use in this paragraph.
- **Consistency rule applicable:** Conditional only. A percentage for the same event numerator must use the same defined population, but the package does not establish that the discussion reused pooled numerator 31 with denominator 381. That unsupported assignment cannot be an actual numeric comparison.
- **Calculation/logical comparison reproduced:** Pooled arithmetic reproduces 100×31/444=6.981982%→7%. Conditional 100×31/381=8.136483%→8% is correct arithmetic but **does not reproduce a registered actual arm-specific mismatch**, because input 31 is not established for that arm. Separate arm-specific counts 25,26,27,28 among 381 would each round to 7%; these are diagnostic possible values, not inferred actual counts. Repetition of 7% and the all-but-one remedy wording suggests a shared result but does not prove one.
- **Necessary inputs available:** Pooled count/denominator and printed discussion label are available. **Missing inputs/definitions:** the discussion's intended denominator, its resistance numerator, and an explicit statement that both passages summarize the same event set. Without these, whether there is a residual population-label discrepancy cannot be settled.
- **Source-grounded alternative interpretation:** “Bougie group” may informally refer to all 444 patients in whom a bougie was used; alternatively, the discussion may report a separately calculated rounded randomized-arm proportion. The two possibilities are compatible with the supplied wording and printed 7%, and the package does not choose between them.
- **Direct observation versus inferred explanation:** Different population wording is directly observed. Reusing pooled 31 in randomized 381 is an inferred alignment assumption, not a direct input. The equal rounded percentages and remedy phrase are evidence suggesting identity, not proof. No arm-specific count or 8% result is attributed to the source.
- **Document roles:** All compared locations are REPORT within the main article.
- **Classification:** Primary category `Measure, label, or scale inconsistency`; primary relationship `S_W`; all relationships `S_W`; review domain `report_internal_inconsistency`. Retained as the best-supported classification of the registered comparison, without changing the stable ID. **Classification ambiguity:** the intended group label and identity of the repeated result remain unresolved.
- **Evidence state:** `record_input_error`, correcting the ledger's provisional state. **Determining recheck fact:** the registered mismatch would require an unsupported alignment of pooled numerator 31 with randomized-arm denominator 381; no arm numerator or explicit matched-result identity is supplied. Source text is faithfully transcribed, but an actual discrepancy cannot be established or explicitly disproved. This is not `not_reproduced`, because the package does not demonstrate reconciliation; it is not `repaired_residual`, because no source transcription was disproven and replaced.
- **Exact remaining human question:** Does the discussion's “bougie group” mean all actual bougie-use patients, or the randomized bougie arm, and does its 7% reuse the pooled 31/444 result or a separate arm-specific numerator/denominator?

## C009 — Hypoxemia observation-window anchor

- **Location found:** Yes. [Protocol PDF p.9, lines 304–312](../../../joi180054supp1_prod.pdf#page=9) and [p.10, lines 340–344 and 353–354](../../../joi180054supp1_prod.pdf#page=10); [main PDF p.3, Measurements and Trial Outcomes](../../../jama_driver_2018_oi_180054.pdf#page=3); [main p.7, Table 3 footnotes b/c](../../../jama_driver_2018_oi_180054.pdf#page=7); [main p.9, Table 5 hypoxemia row/footnote b](../../../jama_driver_2018_oi_180054.pdf#page=9); [results supplement p.3, asterisk/dagger notes](../../../joi180054supp2_prod.pdf#page=3).
- **Source value/text matched:** Yes. Protocol hypoxemia is saturation <90%, or a >10% drop if starting below 90%, observed from first-attempt beginning to one minute after ETT cuff inflation; measurements are every 20 seconds with lowest value also recorded. Protocol hypoxemia secondary outcome 4 invokes the same definition.
- **Comparator matched:** Yes. Report hypoxemia threshold agrees, but Table 3/5 and supplement say during or within one minute after completion of the attempt. Reported attempt duration is blade insertion→blade removal. Main Measurements describes collection until one minute following the end of the first attempt. Printed event fractions are 47/371 and 50/364; composite fractions are 156/191 versus 123/177 and 317/371 versus 282/366.
- **Consistency rule applicable:** Yes. The same event definition requires the same observation-window anchor unless an equivalence/change is specified. Equal saturation thresholds do not establish equal observation intervals.
- **Logical comparison reproduced:** Yes. Protocol window end is t(cuff inflation)+60 seconds; report end is t(attempt completion)+60 seconds, with blade removal defining report duration. Different anchor names are directly reproduced. They could coincide operationally, but that equivalence is not supplied. No event-count change can be calculated from aggregate fractions.
- **Necessary inputs available:** Threshold definitions, named time anchors, and reported fractions are available. **Missing inputs/definitions:** paired cuff-inflation/blade-removal timestamps, event saturation trajectories, rule for failed first attempts followed by rescue, any explicit amendment/equivalence, and actual window used to code fractions.
- **Source-grounded alternative interpretation:** Cuff inflation and blade removal may have coincided or nearly coincided; observation could have been deliberately amended to the first-attempt end; completion may have been defined operationally in a way not fully stated. These alternatives prevent reconstructing numerical consequences but do not erase the different printed definitions.
- **Direct observation versus inferred explanation:** Direct observation is the named-anchor difference with agreed thresholds. A changed event classification, altered percentage, or actual endpoint amendment is not demonstrated.
- **Document roles:** Protocol definitions and operational measurement plan are PLAN. Main and results-supplement definitions/fractions are REPORT.
- **Classification:** Primary category `Measure, label, or scale inconsistency`; primary relationship `P_R`; all relationships `P_R`; review domain `protocol_report`. Confirmed. Agreeing REPORT statements create no `S_C`; the supplied PLAN definitions agree and create no `P_P`. **Classification ambiguity:** actual operational equivalence or endpoint amendment is not resolved by supplied timestamps or clarification.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** explicit PLAN and REPORT observation windows have different named end anchors, with no supplied equivalence or amendment resolving the alignment.
- **Exact remaining human question:** Was hypoxemia for the reported fractions measured through one minute after cuff inflation or after first-attempt completion/blade removal, especially for failed attempts and rescues, and what supplied definition explains any change?

## C010 — Initial oxygen available-case denominators

- **Location found:** Yes. [Main PDF p.5, Table 1](../../../jama_driver_2018_oi_180054.pdf#page=5), oxygen saturation median and two threshold rows, arm headers, and footnote b.
- **Source value/text matched:** Yes. Initial oxygen rows print <90%: `44/352 (13)` and `40/344 (12)`; <80%: `21/352 (6)` and `11/344 (3)`.
- **Comparator matched:** Yes. Headers n=381/376. Footnote b lists missing initial heart rate, systolic blood pressure, and oxygen saturation respectively as 61 (29/32), 185 (94/91), and 43 (19/24). The word “respectively” assigns 43 and 19/24 specifically to oxygen saturation, not heart rate. Initial vital signs are the first after enrollment before intubation.
- **Consistency rule applicable:** Yes, conditionally on one initial oxygen-saturation measure supplying the median and thresholds. Available cases = arm n minus missing cases. Additional threshold exclusions need an explicit rule.
- **Calculation reproduced:** Yes. Oxygen-footnote available n: 381−19=362 and 376−24=352. Threshold denominators instead are 352/344, implying missing 29/32, total 61 rather than 43. Difference is 10 and 8 available cases, total 18. Footnote 19+24=43 is internally additive. Printed percentages themselves round correctly using their displayed denominators; the inconsistency concerns available-case totals, not those fractions.
- **Necessary inputs available:** Arm totals, printed threshold denominators, missingness counts, and initial-timepoint definition suffice. **Missing inputs/definitions:** any threshold-only exclusion or different availability definition; number of median-contributing saturation observations; whether the threshold denominators came from the same initial reading.
- **Source-grounded alternative interpretation:** Median and thresholds might use different availability rules, with extra excluded readings for thresholds. The threshold implied missingness also equals the separately printed heart-rate missingness, which is a transcription possibility rather than evidence of its cause. The footnote does not identify extra threshold exclusions. Table 2 start-of-attempt oxygen values concern another time point and are not a matched comparator.
- **Direct observation versus inferred explanation:** The 362/352 versus 352/344 arithmetic and footnote's assignment of missingness are direct/reproducible. Transcription from another vital-sign denominator or additional exclusion is inferred. No corrected denominator is adjudicated.
- **Document roles:** All compared rows, headers, and footnote are REPORT within main Table 1.
- **Classification:** Primary category `Denominator, proportion, or total inconsistency`; primary relationship `S_W`; all relationships `S_W`; review domain `statistical_results`. Confirmed. **Classification ambiguity:** none about role/type; availability rules remain unresolved.
- **Evidence state:** `recorded_candidate`. **Determining recheck fact:** directly observed saturation missingness 19/24 does not reproduce the threshold denominators under the same initial-measure rule, and no additional exclusion definition resolves it.
- **Exact remaining human question:** Do the initial saturation median and threshold rows use the same eligible readings, and which missingness or threshold-exclusion rule reconciles n=381/376, missing 19/24, and available denominators 352/344?

## Coverage and limitations

All ten assigned stable IDs have direct-source confirmation of cited printed inputs, separate comparator and applicability checks, reproduced arithmetic/logical comparison or an explicit alignment failure, named missing inputs, content-role classification, and one evidence state. No location was inaccessible. No OCR/source disagreement was encountered in the candidate values visually checked. Scientific questions requiring unprovided event-level data, timing data, rounding provenance, or endpoint/population definitions are enumerated per ID and remain human questions, rather than omissions of assigned recheck coverage.
