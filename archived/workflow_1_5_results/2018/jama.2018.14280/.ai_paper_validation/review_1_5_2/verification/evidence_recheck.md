# Fresh Evidence Recheck

Scope: stable candidates C001-C023 in `candidate_ledger.md`. Each candidate was rechecked separately against the supplied PDF at the stated page, using fresh native/layout text and fresh page renders only as locators. All candidates remain **Pending Human Adjudication**. No candidate was deleted, merged, renumbered, ranked, or assigned a disposition.

## C001 — Reversed endpoint in the eTable 2 PEEP interquartile range

- **Cited location found:** Yes. [Supplement 3, eTable 2, Other Mode of Ventilation, after titration on day of randomization, intermediate arm, PEEP](../../../joi180108supp3_prod.pdf#page=6).
- **Source printed value/text matched:** Yes: `8 (5–1)` cm H2O.
- **Comparator printed value/text matched:** Yes. The table note says data are `N (%) and median (interquartile range)`, and the adjacent low-arm entry is `5 (5–10)`.
- **Consistency rule applicable:** For a median and IQR written as `median (lower–upper)`, the ordered relation is lower quartile <= median <= upper quartile.
- **Calculation or logical comparison reproduced:** `5 <= 8` is true, but `8 <= 1` is false.
- **Necessary inputs available / missing:** The printed median, both printed endpoints, unit, and IQR definition are available. The intended upper endpoint or any underlying patient-level values are not supplied.
- **Source-grounded alternative interpretation:** The last digit may be truncated or mistyped, but no supplied source gives a replacement endpoint.
- **Direct observation versus inferred explanation:** Direct observation: the PDF prints `8 (5–1)` and identifies the parenthetical values as an IQR. Inferred explanation: a typesetting error caused the reversed endpoint.
- **Exact remaining human question:** What are the intended lower and upper quartiles for this cell?
- **Status:** Pending Human Adjudication.

## C002 — At-risk-for-ARDS percentages use undisclosed denominators

- **Cited location found:** Yes. [Main article, Table 1, Patients at risk for ARDS](../../../jama_simonis_2018_oi_180108.pdf#page=5).
- **Source printed value/text matched:** Yes: low `292 (61.6)` and intermediate `290 (60.3)`.
- **Comparator printed value/text matched:** Yes: column headers are low `n = 477` and intermediate `n = 484`.
- **Consistency rule applicable:** A displayed count and percentage should reproduce from the stated denominator, subject to one-decimal rounding, or a different denominator should be identified.
- **Calculation or logical comparison reproduced:** `292/477 = 61.2159%` -> 61.2%, and `290/484 = 59.9174%` -> 59.9%. In contrast, `292/474 = 61.6034%` -> 61.6%, and `290/481 = 60.2911%` -> 60.3%.
- **Necessary inputs available / missing:** Counts, percentages, and arm totals are available. Row-specific denominators and missing counts are not printed.
- **Source-grounded alternative interpretation:** Table 1 may use available-case denominators of 474 and 481 for this row, consistent with the displayed percentages, while retaining randomized arm totals in the headers.
- **Direct observation versus inferred explanation:** Direct observation: the displayed percentages do not round from the header totals, while 474 and 481 reproduce them. Inferred explanation: three observations per arm were unavailable for this variable.
- **Exact remaining human question:** What denominators and missing counts were used for the at-risk-for-ARDS row?
- **Status:** Pending Human Adjudication.

## C003 — Septic-shock percentages use undisclosed denominators

- **Cited location found:** Yes. [Main article, Table 1, Septic shock](../../../jama_simonis_2018_oi_180108.pdf#page=5).
- **Source printed value/text matched:** Yes: low `82 (17.6)` and intermediate `74 (15.5)`.
- **Comparator printed value/text matched:** Yes: column headers are low `n = 477` and intermediate `n = 484`.
- **Consistency rule applicable:** A displayed count and percentage should reproduce from the stated denominator, subject to one-decimal rounding, or a different denominator should be identified.
- **Calculation or logical comparison reproduced:** `82/477 = 17.1908%` -> 17.2%, and `74/484 = 15.2893%` -> 15.3%, rather than 17.6% and 15.5%. Example alternative denominators reproduce the display: `82/466 = 17.5966%` -> 17.6%, and `74/477 = 15.5136%` -> 15.5%; rounding alone does not identify a unique low-arm denominator.
- **Necessary inputs available / missing:** Counts, percentages, and arm totals are available. Exact row-specific denominators, missing counts, and the missingness rule are not supplied.
- **Source-grounded alternative interpretation:** Available-case denominators smaller than the randomized arm totals may have been used.
- **Direct observation versus inferred explanation:** Direct observation: header-total calculations do not match the printed percentages. Inferred explanation: missing baseline values caused use of row-specific denominators.
- **Exact remaining human question:** What exact denominators and missingness rule generated 17.6% and 15.5%?
- **Status:** Pending Human Adjudication.

## C004 — Tobacco-use categories use undisclosed denominators

- **Cited location found:** Yes. [Main article, Table 1, Patient tobacco use](../../../jama_simonis_2018_oi_180108.pdf#page=5).
- **Source printed value/text matched:** Yes. Low: never `106 (22.3)`, current `97 (20.4)`, previous `75 (15.8)`, unknown `197 (41.5)`. Intermediate: `111 (23.0)`, `97 (20.1)`, `80 (16.6)`, `194 (40.2)`.
- **Comparator printed value/text matched:** Yes: arm headers are 477 and 484; the four category counts total 475 and 482.
- **Consistency rule applicable:** Mutually listed categorical counts should reconcile to the disclosed denominator, and each percentage should use that denominator or the table should identify a different base.
- **Calculation or logical comparison reproduced:** Low total `106+97+75+197 = 475`; intermediate total `111+97+80+194 = 482`. The percentages reproduce these totals, for example `106/475 = 22.3158%` -> 22.3% and `111/482 = 23.0290%` -> 23.0%, rather than the header totals.
- **Necessary inputs available / missing:** All listed category counts and percentages are available. The status of the two patients per arm not represented by the listed categories and the variable-specific denominator policy are not supplied.
- **Source-grounded alternative interpretation:** The percentages may intentionally use 475 and 482 available tobacco-use records even though `Unknown` is also a printed category.
- **Direct observation versus inferred explanation:** Direct observation: listed counts stop two short of each arm total and percentages are based on the smaller sums. Inferred explanation: two further records per arm were missing outside the `Unknown` category.
- **Exact remaining human question:** Were 475 and 482 the intended denominators, and how were the two unrepresented patients per arm classified?
- **Status:** Pending Human Adjudication.

## C005 — Alcohol-use categories use undisclosed denominators

- **Cited location found:** Yes. [Main article, Table 1, Patient alcohol use](../../../jama_simonis_2018_oi_180108.pdf#page=5).
- **Source printed value/text matched:** Yes. Low counts/percentages are `121 (25.5)`, `47 (9.9)`, `26 (5.5)`, `59 (12.4)`, and `222 (46.7)`; intermediate values are `92 (19.1)`, `61 (12.7)`, `30 (6.2)`, `56 (11.6)`, and `243 (50.4)`.
- **Comparator printed value/text matched:** Yes: arm headers are 477 and 484; listed alcohol categories total 475 and 482.
- **Consistency rule applicable:** Listed category counts and percentages should reconcile to a disclosed denominator.
- **Calculation or logical comparison reproduced:** Low total `121+47+26+59+222 = 475`; intermediate total `92+61+30+56+243 = 482`. Examples: `121/475 = 25.4737%` -> 25.5% and `92/482 = 19.0871%` -> 19.1%.
- **Necessary inputs available / missing:** Category counts and percentages are available. The denominator policy and the classification of two patients per arm outside the listed categories are missing.
- **Source-grounded alternative interpretation:** Variable-specific available-case denominators of 475 and 482 may have been intended.
- **Direct observation versus inferred explanation:** Direct observation: percentages reproduce 475/482 and the counts are two short of each arm header. Inferred explanation: two additional records per arm were missing despite the listed `Unknown` category.
- **Exact remaining human question:** Should denominators 475 and 482 and two missing observations per arm be disclosed for alcohol use?
- **Status:** Pending Human Adjudication.

## C006 — ICU-admission categories use undisclosed denominators

- **Cited location found:** Yes. [Main article, Table 1, Reason for ICU admission](../../../jama_simonis_2018_oi_180108.pdf#page=5).
- **Source printed value/text matched:** Yes: low surgical `82 (17.3)` and medical `393 (82.7)`; intermediate surgical `79 (16.4)` and medical `403 (83.6)`.
- **Comparator printed value/text matched:** Yes: arm headers are 477 and 484; the two categories total 475 and 482.
- **Consistency rule applicable:** An apparently exhaustive binary categorization should sum to its stated denominator, and the displayed percentages should use a disclosed base.
- **Calculation or logical comparison reproduced:** `82+393 = 475` and `79+403 = 482`; `82/475 = 17.2632%` -> 17.3%, and `79/482 = 16.3900%` -> 16.4%.
- **Necessary inputs available / missing:** Both category counts and percentages are available. No reason, missing category, or variable-specific denominator is printed for the two patients per arm not included.
- **Source-grounded alternative interpretation:** Surgical/medical status may have been available for only 475 and 482 patients.
- **Direct observation versus inferred explanation:** Direct observation: the two rows total 475/482 and their percentages reproduce those totals. Inferred explanation: two patients per arm lacked a classifiable ICU-admission reason.
- **Exact remaining human question:** What denominators and missing categories were used for reason for ICU admission?
- **Status:** Pending Human Adjudication.

## C007 — Sedative-infusion percentages omit effective denominators

- **Cited location found:** Yes. [Supplement 3, eTable 4, Sedative infusion](../../../joi180108supp3_prod.pdf#page=8).
- **Source printed value/text matched:** Yes: low `320 (70.6)` and intermediate `333 (72.1)`.
- **Comparator printed value/text matched:** Yes: column headers are 477 and 484; the table note says data are `number / total (%) or median (interquartile range)` but these cells omit totals.
- **Consistency rule applicable:** Count/percentage pairs should reproduce from a disclosed denominator.
- **Calculation or logical comparison reproduced:** `320/477 = 67.0859%` -> 67.1% and `333/484 = 68.8017%` -> 68.8%. The displayed values instead reproduce with `320/453 = 70.6402%` -> 70.6% and `333/462 = 72.0779%` -> 72.1%.
- **Necessary inputs available / missing:** Counts, percentages, arm totals, and the row definition are available. Row totals 453 and 462 are only arithmetically recoverable; missing counts and the analysis population are not printed.
- **Source-grounded alternative interpretation:** This row may use a complete-case subset, as other eTable 4 rows explicitly display denominators below the arm totals.
- **Direct observation versus inferred explanation:** Direct observation: header-total percentages disagree and 453/462 reproduce the display. Inferred explanation: missing co-intervention records defined the smaller population.
- **Exact remaining human question:** Were 453 and 462 the row denominators, and what records were excluded or missing?
- **Status:** Pending Human Adjudication.

## C008 — Analgesic-infusion percentages omit effective denominators

- **Cited location found:** Yes. [Supplement 3, eTable 4, Analgesic infusion](../../../joi180108supp3_prod.pdf#page=8).
- **Source printed value/text matched:** Yes: low `277 (61.1)` and intermediate `273 (59.1)`.
- **Comparator printed value/text matched:** Yes: headers are 477 and 484; the data note calls for number/total (%) while these cells omit totals.
- **Consistency rule applicable:** Count/percentage pairs should reproduce from a disclosed denominator.
- **Calculation or logical comparison reproduced:** `277/477 = 58.0713%` -> 58.1% and `273/484 = 56.4050%` -> 56.4%. `277/453 = 61.1479%` -> 61.1% and `273/462 = 59.0909%` -> 59.1% reproduce the display.
- **Necessary inputs available / missing:** Counts, percentages, arm totals, and definition are available. Exact printed row totals, missing counts, and population rules are absent.
- **Source-grounded alternative interpretation:** A 453/462 complete-case population may underlie this row, consistent with the table's use of explicit reduced denominators elsewhere.
- **Direct observation versus inferred explanation:** Direct observation: 477/484 do not generate the printed percentages and 453/462 do. Inferred explanation: incomplete analgesic-infusion records caused the denominator reduction.
- **Exact remaining human question:** What exact row totals and missing-data rule generated the analgesic-infusion percentages?
- **Status:** Pending Human Adjudication.

## C009 — Neuromuscular-blockade percentages omit effective denominators

- **Cited location found:** Yes. [Supplement 3, eTable 4, Neuromuscular blockade](../../../joi180108supp3_prod.pdf#page=8).
- **Source printed value/text matched:** Yes: low `53 (11.7)` and intermediate `60 (13.0)`.
- **Comparator printed value/text matched:** Yes: headers are 477 and 484; totals are omitted from these number/percentage cells.
- **Consistency rule applicable:** Count/percentage pairs should reproduce from a disclosed denominator.
- **Calculation or logical comparison reproduced:** `53/477 = 11.1111%` -> 11.1% and `60/484 = 12.3967%` -> 12.4%. `53/453 = 11.6998%` -> 11.7% and `60/462 = 12.9870%` -> 13.0% reproduce the display.
- **Necessary inputs available / missing:** Printed counts, percentages, arm totals, and exposure definition are available. Row totals, missing counts, and population definition are not printed.
- **Source-grounded alternative interpretation:** A 453/462 available-case subset may have been used, as with adjacent infusion rows.
- **Direct observation versus inferred explanation:** Direct observation: arm-total calculations fail and 453/462 calculations match. Inferred explanation: missing co-intervention data explain the smaller denominators.
- **Exact remaining human question:** What row denominators and exclusions or missing observations underlie this row?
- **Status:** Pending Human Adjudication.

## C010 — Vasopressor-use percentages omit effective denominators

- **Cited location found:** Yes. [Supplement 3, eTable 4, Use of vasopressors](../../../joi180108supp3_prod.pdf#page=8).
- **Source printed value/text matched:** Yes: low `363 (80.0)` and intermediate `353 (76.4)`.
- **Comparator printed value/text matched:** Yes: headers are 477 and 484; the cells omit row totals even though the table note defines number/total (%).
- **Consistency rule applicable:** Count/percentage pairs should reproduce from a disclosed denominator.
- **Calculation or logical comparison reproduced:** `363/477 = 76.1006%` -> 76.1% and `353/484 = 72.9339%` -> 72.9%. `363/454 = 79.9559%` -> 80.0% and `353/462 = 76.4069%` -> 76.4% reproduce the display.
- **Necessary inputs available / missing:** Counts, percentages, arm totals, and vasopressor definition are available. Row totals 454/462 are not printed; missing counts and population rules are absent.
- **Source-grounded alternative interpretation:** The low-arm denominator may match the 454 explicitly printed in several nearby transfusion/colloid rows, while the intermediate vasopressor denominator is a different 462-person subset; the source does not state whether these populations are shared.
- **Direct observation versus inferred explanation:** Direct observation: 454/462 reproduce the display and 477/484 do not. Inferred explanation: missing vasopressor-use data created different effective denominators.
- **Exact remaining human question:** Were 454 and 462 the vasopressor denominators, and why do they differ from the arm totals and nearby intermediate denominator 464?
- **Status:** Pending Human Adjudication.

## C011 — Mortality effect-measure wording conflicts with Table 2 and the SAP

- **Cited location found:** Yes. [Main article, Statistical Analysis](../../../jama_simonis_2018_oi_180108.pdf#page=4), [main article, Table 2 and footnotes c/d](../../../jama_simonis_2018_oi_180108.pdf#page=6), and [SAP, secondary outcomes](../../../joi180108supp2_prod.pdf#page=13).
- **Source printed value/text matched:** Yes. The main Methods says `ICU and hospital length of stay and mortality rates were compared using Kaplan-Meier survival curves and reported as hazard ratios calculated from a Cox proportional hazard model.`
- **Comparator printed value/text matched:** Yes. Table 2 labels ICU and hospital mortality `RR` under footnote c, while 28- and 90-day mortality are `HR` under footnote d. The SAP assigns RR to ICU/hospital mortality and Kaplan-Meier/Cox HR to 28-/90-day mortality.
- **Consistency rule applicable:** The described estimator/effect measure should align across Methods, prespecified plan, table label, and footnotes for the same outcomes.
- **Calculation or logical comparison reproduced:** The semantic mapping is discordant for ICU/hospital mortality: main Methods -> HR/Cox if read to include those mortality rates; Table 2 and SAP -> RR/Wald. The 28-/90-day HR mapping is aligned between Table 2 and SAP.
- **Necessary inputs available / missing:** All relevant labels and method descriptions are present. The main sentence's intended outcome scope and any analysis code or model output are absent.
- **Source-grounded alternative interpretation:** The Methods sentence may have intended Kaplan-Meier/Cox only for time-indexed 28-/90-day mortality, with the adjacent sentence on `other secondary binary outcomes` covering ICU/hospital mortality, but that restriction is not stated in the sentence.
- **Direct observation versus inferred explanation:** Direct observation: the sources print different method/measure descriptions for ICU/hospital mortality. Inferred explanation: the Methods sentence is overbroad rather than Table 2 and the SAP using a different analysis.
- **Exact remaining human question:** Which model and effect measure were actually used for ICU and hospital mortality, and what outcome scope was intended by the main Methods sentence?
- **Status:** Pending Human Adjudication.

## C012 — ICU-mortality RR does not reproduce from printed risks

- **Cited location found:** Yes. [Main article, Table 2, ICU mortality and footnote c](../../../jama_simonis_2018_oi_180108.pdf#page=6).
- **Source printed value/text matched:** Yes: low `132/450 (29.3)`, intermediate `115/458 (25.1)`, and `RR, 1.11 (0.96–1.27)`.
- **Comparator printed value/text matched:** Yes: both printed count/total risks and the RR label were located; footnote c identifies a risk ratio with Wald likelihood-ratio approximation confidence intervals and chi-square P values.
- **Consistency rule applicable:** If the RR is the unadjusted low-arm risk divided by the intermediate-arm risk, it should reproduce from the printed counts and totals subject to rounding.
- **Calculation or logical comparison reproduced:** `(132/450)/(115/458) = 1.168231884`, which rounds to 1.17, not 1.11.
- **Necessary inputs available / missing:** All inputs for the crude displayed-risk ratio are available. The exact estimator, any weighting/stratification, analysis-set membership, and model output needed to generate 1.11 are not supplied.
- **Source-grounded alternative interpretation:** Footnote c specifies an inferential procedure but not the RR computation itself; a non-crude or differently defined analysis population could yield an estimate not equal to the displayed-risk ratio.
- **Direct observation versus inferred explanation:** Direct observation: the printed crude risks yield 1.1682 and the table prints 1.11. Inferred explanation: an unreported estimator or population produced 1.11.
- **Exact remaining human question:** What estimator, direction, analysis population, and any weights or strata generated RR 1.11?
- **Status:** Pending Human Adjudication.

## C013 — Hospital-mortality RR does not reproduce from printed risks

- **Cited location found:** Yes. [Main article, Table 2, hospital mortality and footnote c](../../../jama_simonis_2018_oi_180108.pdf#page=6).
- **Source printed value/text matched:** Yes: low `151/477 (31.7)`, intermediate `140/484 (28.9)`, and `RR, 1.06 (0.93–1.22)`.
- **Comparator printed value/text matched:** Yes: both count/total risks and the RR/footnote were found.
- **Consistency rule applicable:** An unadjusted low/intermediate RR should equal the ratio of the two printed risks.
- **Calculation or logical comparison reproduced:** `(151/477)/(140/484) = 1.094399521`, which rounds to 1.09, not 1.06.
- **Necessary inputs available / missing:** Printed-risk inputs are complete. The estimator specification, alternative population, weighting/stratification, and model output that could generate 1.06 are absent.
- **Source-grounded alternative interpretation:** The Wald likelihood-ratio wording may refer to an estimate produced by an implementation not recoverable from the displayed 2-by-2 margins.
- **Direct observation versus inferred explanation:** Direct observation: the crude printed-risk ratio is 1.0944 and the printed RR is 1.06. Inferred explanation: a non-crude estimator or different population was used.
- **Exact remaining human question:** What exact analysis generated hospital-mortality RR 1.06?
- **Status:** Pending Human Adjudication.

## C014 — ARDS RR does not reproduce from printed risks

- **Cited location found:** Yes. [Main article, Table 2, Development of ARDS and footnote c](../../../jama_simonis_2018_oi_180108.pdf#page=6).
- **Source printed value/text matched:** Yes: low `17/448 (3.8)`, intermediate `23/462 (5.0)`, and `RR, 0.86 (0.59–1.24)`.
- **Comparator printed value/text matched:** Yes: both risks, RR, and footnote c were located.
- **Consistency rule applicable:** The unadjusted low/intermediate RR should reproduce from printed counts/totals.
- **Calculation or logical comparison reproduced:** `(17/448)/(23/462) = 0.762228261`, which rounds to 0.76, not 0.86.
- **Necessary inputs available / missing:** Inputs for the crude ratio are complete. Exact estimator, analysis population, weights/strata, and model output for 0.86 are missing.
- **Source-grounded alternative interpretation:** The source may report a model- or test-derived RR not defined by the displayed margins, although it does not state such a derivation.
- **Direct observation versus inferred explanation:** Direct observation: the displayed risks yield 0.7622 while the RR is 0.86. Inferred explanation: an unreported estimator/population produced 0.86.
- **Exact remaining human question:** What estimator and denominator population produced ARDS RR 0.86?
- **Status:** Pending Human Adjudication.

## C015 — Pneumonia RR does not reproduce from printed risks

- **Cited location found:** Yes. [Main article, Table 2, Development of pneumonia and footnote c](../../../jama_simonis_2018_oi_180108.pdf#page=6).
- **Source printed value/text matched:** Yes: low `19/450 (4.2)`, intermediate `17/462 (3.7)`, and `RR, 1.07 (0.78–1.47)`.
- **Comparator printed value/text matched:** Yes: counts/totals, percentages, RR, and footnote c were found.
- **Consistency rule applicable:** An unadjusted low/intermediate RR should equal the ratio of the printed risks.
- **Calculation or logical comparison reproduced:** `(19/450)/(17/462) = 1.147450980`, which rounds to 1.15, not 1.07.
- **Necessary inputs available / missing:** Printed-risk inputs are complete. Estimator details, alternative population, weights/strata, and model output are absent.
- **Source-grounded alternative interpretation:** A risk-ratio procedure based on information beyond the displayed margins is possible under the broad Methods wording, but is not described.
- **Direct observation versus inferred explanation:** Direct observation: the crude ratio is 1.1475 and the printed RR is 1.07. Inferred explanation: a non-crude estimator/population produced 1.07.
- **Exact remaining human question:** What exact computation and population generated pneumonia RR 1.07?
- **Status:** Pending Human Adjudication.

## C016 — Pneumothorax RR does not reproduce from printed risks

- **Cited location found:** Yes. [Main article, Table 2, Pneumothorax and footnote c](../../../jama_simonis_2018_oi_180108.pdf#page=6).
- **Source printed value/text matched:** Yes: low `8/448 (1.8)`, intermediate `6/462 (1.3)`, and `RR, 1.16 (0.73–1.84)`.
- **Comparator printed value/text matched:** Yes: counts/totals, percentages, RR, and footnote were found.
- **Consistency rule applicable:** The unadjusted low/intermediate risk ratio should reproduce from the printed risks.
- **Calculation or logical comparison reproduced:** `(8/448)/(6/462) = 1.375`, which rounds to 1.38, not 1.16.
- **Necessary inputs available / missing:** Crude-risk inputs are complete. Estimator definition, alternative population, weights/strata, and model output needed for 1.16 are missing.
- **Source-grounded alternative interpretation:** A model- or test-derived effect using information not printed in the table could differ from the crude margins.
- **Direct observation versus inferred explanation:** Direct observation: the printed margins yield 1.375 and the RR cell prints 1.16. Inferred explanation: an undisclosed estimator or population produced 1.16.
- **Exact remaining human question:** What computation and analysis set generated pneumothorax RR 1.16?
- **Status:** Pending Human Adjudication.

## C017 — Atelectasis RR does not reproduce from printed risks

- **Cited location found:** Yes. [Main article, Table 2, Atelectasis and footnote c](../../../jama_simonis_2018_oi_180108.pdf#page=6).
- **Source printed value/text matched:** Yes: low `51/449 (11.4)`, intermediate `52/464 (11.2)`, and `RR, 1.00 (0.81–1.23)`.
- **Comparator printed value/text matched:** Yes: both displayed risks, RR, and footnote c were located.
- **Consistency rule applicable:** The unadjusted low/intermediate RR should equal the ratio of the printed count/total risks.
- **Calculation or logical comparison reproduced:** `(51/449)/(52/464) = 1.013534350`, which rounds to 1.01, not 1.00.
- **Necessary inputs available / missing:** Crude ratio inputs are complete. The precise estimator, any non-crude analysis, and model output needed to obtain 1.00 are absent.
- **Source-grounded alternative interpretation:** A separately estimated or more heavily rounded effect could print as 1.00, but the source does not disclose the computation.
- **Direct observation versus inferred explanation:** Direct observation: the exact printed margins yield 1.0135. Inferred explanation: model derivation or a reporting convention yielded 1.00.
- **Exact remaining human question:** What estimator and rounding rule produced atelectasis RR 1.00?
- **Status:** Pending Human Adjudication.

## C018 — Extrapulmonary-infection RR does not reproduce from printed risks

- **Cited location found:** Yes. [Main article, Table 2, Extrapulmonary infection and footnote c](../../../jama_simonis_2018_oi_180108.pdf#page=6).
- **Source printed value/text matched:** Yes: low `20/448 (4.5)`, intermediate `28/463 (6.0)`, and `RR, 0.84 (0.60–1.18)`.
- **Comparator printed value/text matched:** Yes: risks, RR, and footnote were found.
- **Consistency rule applicable:** The unadjusted low/intermediate RR should reproduce from the printed count/total risks.
- **Calculation or logical comparison reproduced:** `(20/448)/(28/463) = 0.738201531`, which rounds to 0.74, not 0.84.
- **Necessary inputs available / missing:** Crude-risk inputs are complete. Exact estimator, alternative population, weighting/stratification, and model output are missing.
- **Source-grounded alternative interpretation:** The printed RR may have been generated by an unspecified procedure beyond the displayed margins.
- **Direct observation versus inferred explanation:** Direct observation: the margins yield 0.7382 while the RR is 0.84. Inferred explanation: an unreported estimator or analysis set explains the difference.
- **Exact remaining human question:** What procedure and population produced extrapulmonary-infection RR 0.84?
- **Status:** Pending Human Adjudication.

## C019 — Extrapulmonary-sepsis RR does not reproduce from printed risks

- **Cited location found:** Yes. [Main article, Table 2, Extrapulmonary sepsis and footnote c](../../../jama_simonis_2018_oi_180108.pdf#page=6).
- **Source printed value/text matched:** Yes: low `12/448 (2.7)`, intermediate `16/463 (3.5)`, and `RR, 0.87 (0.56–1.33)`.
- **Comparator printed value/text matched:** Yes: both risks, RR, and footnote were found.
- **Consistency rule applicable:** The unadjusted low/intermediate RR should equal the ratio of the printed risks.
- **Calculation or logical comparison reproduced:** `(12/448)/(16/463) = 0.775111607`, which rounds to 0.78, not 0.87.
- **Necessary inputs available / missing:** Printed-risk inputs are complete. Estimator details, alternative population, weights/strata, and model output are absent.
- **Source-grounded alternative interpretation:** A non-crude RR consistent with a broader inferential implementation could differ from the displayed margins, but no such implementation is identified.
- **Direct observation versus inferred explanation:** Direct observation: the crude ratio is 0.7751 and the RR is 0.87. Inferred explanation: an unreported estimator/population produced 0.87.
- **Exact remaining human question:** What estimator and analysis set generated extrapulmonary-sepsis RR 0.87?
- **Status:** Pending Human Adjudication.

## C020 — Delirium RR does not reproduce from printed risks

- **Cited location found:** Yes. [Main article, Table 2, Delirium and footnote c](../../../jama_simonis_2018_oi_180108.pdf#page=6).
- **Source printed value/text matched:** Yes: low `149/343 (43.4)`, intermediate `132/361 (36.6)`, and `RR, 1.15 (0.99–1.34)`.
- **Comparator printed value/text matched:** Yes: both risks, RR, and footnote were found.
- **Consistency rule applicable:** The unadjusted low/intermediate RR should reproduce from the printed count/total risks.
- **Calculation or logical comparison reproduced:** `(149/343)/(132/361) = 1.188024560`, which rounds to 1.19, not 1.15.
- **Necessary inputs available / missing:** Crude ratio inputs are complete. Exact estimator, analysis-set definition beyond the shown totals, weights/strata, and model output are missing.
- **Source-grounded alternative interpretation:** A non-crude analysis or a population not fully represented by the displayed margins could produce another RR.
- **Direct observation versus inferred explanation:** Direct observation: printed margins yield 1.1880 while the RR is 1.15. Inferred explanation: an unreported estimator/population generated 1.15.
- **Exact remaining human question:** What computation and analysis population produced delirium RR 1.15?
- **Status:** Pending Human Adjudication.

## C021 — Tracheostomy RR does not reproduce from printed risks

- **Cited location found:** Yes. [Main article, Table 2, Need for tracheostomy and footnote c](../../../jama_simonis_2018_oi_180108.pdf#page=6).
- **Source printed value/text matched:** Yes: low `54/477 (11.3)`, intermediate `52/484 (10.7)`, and `RR, 1.03 (0.84–1.26)`.
- **Comparator printed value/text matched:** Yes: both risks, RR, and footnote were found.
- **Consistency rule applicable:** The unadjusted low/intermediate RR should equal the ratio of the printed risks.
- **Calculation or logical comparison reproduced:** `(54/477)/(52/484) = 1.053701016`, which rounds to 1.05, not 1.03.
- **Necessary inputs available / missing:** Crude ratio inputs are complete. Estimator specification, alternative population, weighting/stratification, and model output for 1.03 are absent.
- **Source-grounded alternative interpretation:** An effect computed by a procedure not reducible to the displayed margins may differ from the crude ratio, although the source does not specify one.
- **Direct observation versus inferred explanation:** Direct observation: the margins yield 1.0537 and the RR cell prints 1.03. Inferred explanation: a non-crude estimator or population produced 1.03.
- **Exact remaining human question:** What exact analysis generated tracheostomy RR 1.03?
- **Status:** Pending Human Adjudication.

## C022 — The same subgroup intervals are labelled IQR and 95% CI

- **Cited location found:** Yes. [Main article, Subgroups and Exploratory Analyses](../../../jama_simonis_2018_oi_180108.pdf#page=6) and [Supplement 3, eTable 5](../../../joi180108supp3_prod.pdf#page=9).
- **Source printed value/text matched:** Yes. Main text prints inside-ICU mean difference `-2.50 [IQR, -4.63 to -0.36]` and outside-ICU `1.45 [IQR, -0.52 to 3.43]`.
- **Comparator printed value/text matched:** Yes. eTable 5 has the header `Mean Difference (95% CI)` and prints ICU `-2.50 (-4.63–-0.36)` and Outside ICU `1.45 (-0.52–3.43)`.
- **Consistency rule applicable:** Identical interval endpoints attached to the same point estimates should have the same interval type unless a documented reason distinguishes them.
- **Calculation or logical comparison reproduced:** Both sources match exactly on the two point estimates and all four endpoints; only the interval labels differ (`IQR` versus `95% CI`).
- **Necessary inputs available / missing:** Both printed labels and values are available. The analysis output and editorial provenance needed to establish the intended label are not supplied.
- **Source-grounded alternative interpretation:** Because eTable 5 is explicitly a mean-difference subgroup analysis and labels its interval column 95% CI, the narrative's `IQR` may be a label transcription error; this interpretation does not establish the intended wording.
- **Direct observation versus inferred explanation:** Direct observation: identical numeric intervals carry two different labels. Inferred explanation: the narrative label was transcribed incorrectly.
- **Exact remaining human question:** Are both intervals 95% CIs, and which source wording should be clarified?
- **Status:** Pending Human Adjudication.

## C023 — Enrollment completion dates differ by two days

- **Cited location found:** Yes. The main article prints August 20, 2017 in the [abstract](../../../jama_simonis_2018_oi_180108.pdf#page=1) and [Results/Patients](../../../jama_simonis_2018_oi_180108.pdf#page=5). The SAP prints August 22, 2017 in the [abstract](../../../joi180108supp2_prod.pdf#page=3) and again in its introduction on [PDF page 5](../../../joi180108supp2_prod.pdf#page=5). The corrected ledger identifies both SAP pages.
- **Source printed value/text matched:** Yes. Main: trial `conducted from September 1, 2014, through August 20, 2017` and patients screened `through August 20, 2017`.
- **Comparator printed value/text matched:** Yes. SAP: `Enrollment of patients was complete on August 22, 2017` and `Enrollment of patients in PReVENT was complete on August 22, 2017`.
- **Consistency rule applicable:** Dates presented as the end of trial enrollment for the same trial should agree, or their distinct operational meanings should be defined.
- **Calculation or logical comparison reproduced:** August 22, 2017 is two calendar days after August 20, 2017.
- **Necessary inputs available / missing:** Both dates, trial identity, and surrounding descriptions are available. Definitions of `through` and `enrollment ... complete`, the last randomization timestamp, and administrative closure records are not supplied.
- **Source-grounded alternative interpretation:** August 20 may refer to the last screened/enrolled or randomized patient and August 22 to administrative completion, but the supplied sources do not define such separate events.
- **Direct observation versus inferred explanation:** Direct observation: the main article uses August 20 and the SAP uses August 22 for enrollment-period completion language. Inferred explanation: clinical enrollment and administrative completion occurred on different dates.
- **Exact remaining human question:** What operational event does each date represent, and what was the actual last patient enrollment/randomization date?
- **Status:** Pending Human Adjudication.

## Recheck completion

- Stable IDs assigned: 23.
- Stable IDs covered: C001-C023 (23/23).
- Source locations found: all 23 candidates; C023 includes a refined locator for the SAP's second printed occurrence (PDF page 5 rather than page 6).
- Items with missing information requiring human clarification: 23/23, as stated in each candidate's exact remaining question.
- Final state for every candidate: **Pending Human Adjudication**.
