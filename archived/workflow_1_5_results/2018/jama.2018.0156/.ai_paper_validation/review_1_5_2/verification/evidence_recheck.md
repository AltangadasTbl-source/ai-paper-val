# Evidence Recheck

## Scope and method

This recheck covers every stable candidate in [`candidate_ledger.md`](../candidate_ledger.md):
`C001` through `C008`. Each ID was checked separately against the cited location in the three
supplied PDFs. Fresh native/layout text and fresh page renderings were used only as locators and
transcription aids; the supplied PDFs were the final authority. No source or candidate ID was
changed. Every candidate remains **Pending Human Adjudication**.

The cited targets resolve within the supplied PDFs: DOC-001 has 9 pages, DOC-002 has 134 pages,
and DOC-003 has 3 pages. All links below use the PDF page number, not a printed internal page
number.

## C001 — Noninferiority narrative reverses the displayed bound direction

- **Cited location found:** Yes. DOC-001, [main article Methods, PDF p. 3](../../../jama_jabre_2018_oi_180004.pdf#page=3), Statistical Analysis, and [main article Results, PDF p. 4](../../../jama_jabre_2018_oi_180004.pdf#page=4), Primary Outcome.
- **Source printed value/text matched:** Yes. The Methods state that noninferiority would be accepted if the lower limit of the BMV-minus-ETI CI was higher than `−1%`. The Results print difference `0.11%`, one-sided 97.5% CI `−1.64% to infinity`, and `P for noninferiority = .11`.
- **Comparator matched:** Yes. The next Results sentence says the lower limit was “greater than the threshold of noninferiority, thus noninferiority was not demonstrated.” The printed conclusion is also consistent with the abstract and Key Points, which say the difference did not meet the 1% margin.
- **Consistency rule applicable:** Yes. On the printed signed percentage-point scale, the lower endpoint must be numerically greater than `−1.00%` to meet the stated rule. A narrative direction word can be compared directly with the displayed endpoint and threshold.
- **Calculation or logical comparison reproduced:** `−1.64% < −1.00%`; equivalently, `−1.64 − (−1.00) = −0.64` percentage points. Therefore, the displayed endpoint is not greater than the threshold. The printed noninferiority conclusion follows the displayed rule and values, while the word “greater” does not.
- **Necessary inputs available:** The effect direction, margin, decision rule, lower endpoint, P value, and narrative conclusion are all printed. No additional numeric input is needed for this direction check.
- **Exact missing inputs or definitions:** The source does not provide editorial history or intended replacement wording, and it does not state whether “greater” was meant to read “not greater,” “lower,” or another phrase.
- **Source-grounded alternative interpretation:** The conclusion may have been intended to follow the correct comparison while one direction word was omitted or reversed. That explanation is compatible with the abstract, Key Points, P value, and stated rule, but the intended wording is not supplied.
- **Direct observation versus inferred explanation:** The rule, endpoint, threshold, direction word, and conclusion are direct observations. Calling the word a production or wording error, or proposing “not greater,” is an inference.
- **Exact remaining human question:** What wording was intended for the comparison between `−1.64%` and `−1.00%`, while preserving or reconsidering the separately printed noninferiority conclusion?
- **Status:** Pending Human Adjudication.

## C002 — Centre-5 pause contrast mixes a count outcome with seconds

- **Cited location found:** Yes. DOC-001, [main article Results, PDF p. 4](../../../jama_jabre_2018_oi_180004.pdf#page=4), Post-Hoc Analyses. The outcome definition is also in [Methods, PDF p. 3](../../../jama_jabre_2018_oi_180004.pdf#page=3).
- **Source printed value/text matched:** Yes. The Results describe “the number of pauses greater than 2 seconds,” give BMV `27` and ETI `16`, and print “difference, `11 seconds` [95% CI, `7 to 15`]; `P < .001`.” The Methods likewise call the measure the “number of pauses lasting more than 2 seconds.”
- **Comparator matched:** Yes. The named outcome is a number of qualifying pauses, while the unit attached to the difference is seconds. The adjacent CCF result is separately and consistently expressed as percentages.
- **Consistency rule applicable:** Yes. A difference between two event counts has a count unit. The 2-second duration is the threshold defining which pauses are counted; it does not by itself convert the number of qualifying events into elapsed time.
- **Calculation or logical comparison reproduced:** `27 − 16 = 11`. The point arithmetic reproduces the printed difference. Under the repeated “number of pauses” wording, that result is 11 pauses, whereas the article prints 11 seconds.
- **Necessary inputs available:** The outcome wording, duration threshold, group values, point difference, printed unit, CI, P value, and subgroup sizes (BMV `56`, ETI `59`) are available. These are sufficient for the arithmetic and unit comparison.
- **Exact missing inputs or definitions:** The source does not say whether `27` and `16` are totals, means, medians, or another summary; it does not assign units to those group values or the CI; it does not state the CI method; and it does not supply patient-level monitor data or total pause durations.
- **Source-grounded alternative interpretation:** The values might be duration summaries, which could make seconds appropriate, but that interpretation conflicts with the repeated “number of pauses” wording. Conversely, the values may be pause counts and the threshold’s time unit may have been carried onto the difference.
- **Direct observation versus inferred explanation:** The outcome phrases, threshold, values, difference, seconds label, interval, P value, and subgroup sizes are direct observations. Treating either the outcome wording or the seconds label as unintended is an inference.
- **Exact remaining human question:** Are `27` and `16` counts of qualifying pauses or time summaries, what summary statistic was used, and what unit applies to the difference and its 95% CI?
- **Status:** Pending Human Adjudication.

## C003 — PP day-28 survival point difference does not round from the printed inputs

- **Cited location found:** Yes. DOC-001, [main article Table 2, PDF p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), Per-Protocol Analysis, “Survival at 28 d”; and DOC-002, [Statistical Analysis Plan, PDF p. 123](../../../joi180004supp1_prod.pdf#page=123), section 8.1.2.
- **Source printed value/text matched:** Yes. Table 2 prints PP denominators BMV `n = 995` and ETI `n = 943`, group results `54 (5.4)` and `51 (5.4)`, BMV-minus-ETI difference `0.1`, 95% CI `−10 to 9.7`, and `P = .99`. The SAP says categorical percentages are based on nonmissing values and rounded to one decimal place.
- **Comparator matched:** Yes. The point difference `0.1` appears in the proportion-difference column beside the two printed count/percentage pairs and denominators.
- **Consistency rule applicable:** Yes, conditionally on the printed counts and denominators defining the table’s unadjusted point estimator. A percentage-point difference calculated from those rates can be rounded to the table’s one-decimal point-difference display. The SAP explicitly sets one-decimal rounding for categorical percentages, although it does not separately state a rounding rule for the difference column.
- **Calculation or logical comparison reproduced:** `100 × 54/995 = 5.427136%`; `100 × 51/943 = 5.408271%`; and `100 × (54/995 − 51/943) = 0.018864` percentage points. Ordinary rounding to one decimal gives `0.0`, not the printed `0.1`. Subtracting the two displayed group percentages also gives `5.4 − 5.4 = 0.0`.
- **Necessary inputs available:** The counts, PP denominators, displayed percentages, signed effect label, point difference, CI, P value, and categorical percentage-rounding statement are available. They are sufficient for the direct count-derived check.
- **Exact missing inputs or definitions:** The exact point-estimate procedure, any adjustment or weighting, row-specific denominators, retained internal rates, and a specific rounding rule for percentage-point differences are not supplied.
- **Source-grounded alternative interpretation:** A separately retained estimator, adjustment, weighting, or unprinted denominator could yield a value that rounds to `0.1`; none is identified for this row. The SAP’s one-decimal statement directly governs percentages and may not have been intended to govern differences.
- **Direct observation versus inferred explanation:** The table cells and SAP text are direct observations. The `0.0` display is the arithmetic result conditional on using the printed counts and denominators as the estimator. Any alternate estimator or denominator is inferred.
- **Exact remaining human question:** Which exact estimator, denominator, retained rates, and rounding convention generated the printed PP survival difference of `0.1` percentage points?
- **Status:** Pending Human Adjudication.

## C004 — PP day-28 survival confidence interval has an unresolved scale/precision inconsistency

- **Cited location found:** Yes. DOC-001, [main article Methods, PDF p. 3](../../../jama_jabre_2018_oi_180004.pdf#page=3), secondary-outcome analysis rule, and [Table 2, PDF p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), PP “Survival at 28 d”; DOC-002, [Statistical Analysis Plan, PDF p. 124](../../../joi180004supp1_prod.pdf#page=124), section 8.2.3.
- **Source printed value/text matched:** Yes. Table 2 prints BMV `54/995 (5.4%)`, ETI `51/943 (5.4%)`, difference `0.1`, 95% CI `−10 to 9.7`, and `P = .99` in a column labelled `BMV(%) − ETI(%) (95% CI)`. The main Methods and SAP say secondary rates use a chi-square test on proportions and that corresponding CIs on differences are presented.
- **Comparator matched:** Yes. The interval is paired with two approximately 5.4% rates from roughly 1,000 participants per group, a near-zero point difference, and `P = .99`. Visual inspection of the rendered PDF confirms that the lower endpoint is printed as `−10`, not `−1.0`.
- **Consistency rule applicable:** Yes as a scale and precision diagnostic. A CI in the labelled proportion-difference column should use the percentage-point scale. A standard binomial risk-difference interval can test whether the printed span is numerically plausible, but it is not a replacement for the unreported source-specific construction.
- **Calculation or logical comparison reproduced:** The count-derived rates are `5.427136%` and `5.408271%`, with difference `0.018864` points. A diagnostic unpooled binomial SE is `1.028756` percentage points, producing an ordinary Wald 95% interval of approximately `−1.9975 to 2.0352` points. The printed interval spans `19.7` points (`9.7 − (−10)`), versus approximately `4.03` points in this diagnostic. The near-unit `P = .99` is directionally compatible with the nearly equal rates but does not reproduce the printed CI.
- **Necessary inputs available:** Counts, denominators, effect scale, point and interval displays, P value, and general analysis rule are available for the diagnostic comparison.
- **Exact missing inputs or definitions:** The exact CI formula, SAS procedure and options, pooled versus unpooled variance, continuity correction, exact/asymptotic choice, adjustment or weighting, row-level retained data, and whether either endpoint lost a decimal are not supplied.
- **Source-grounded alternative interpretation:** A nonstandard or adjusted method could produce a wider interval, although no such method is named for this row. A production or decimal-transcription issue could also explain the display, but the intended endpoints are not in the supplied sources.
- **Direct observation versus inferred explanation:** The table cells, heading, P value, and methods statements are direct observations. The diagnostic interval is an explicitly labelled independent calculation, not a proposed replacement. Decimal loss, transcription, or a nonstandard method are inferred explanations.
- **Exact remaining human question:** What exact retained inputs, CI method, software settings, scale, and generated endpoints produced the printed `−10 to 9.7` interval?
- **Status:** Pending Human Adjudication.

## C005 — PP ROSC ETI percentage conflicts with its count, denominator, and signed difference

- **Cited location found:** Yes. DOC-001, [main article Table 2, PDF p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6), Per-Protocol Analysis, “Return of spontaneous circulation.”
- **Source printed value/text matched:** Yes. The PP denominators are BMV `n = 995` and ETI `n = 943`. The row prints BMV `342 (34.4)`, ETI `377 (30.0)`, BMV-minus-ETI difference `−5.6` with 95% CI `−9.9 to −1.3`, and `P = .01`.
- **Comparator matched:** Yes. The ETI count, denominator, displayed percentage, and signed difference all appear in the same table block, whose heading identifies the direction as BMV minus ETI.
- **Consistency rule applicable:** Yes. In a “No. of Patients (%)” table, a parenthetical rate can be compared with `100 × count/analysis denominator`; the signed point difference can be compared with the two count-derived rates.
- **Calculation or logical comparison reproduced:** `100 × 342/995 = 34.371859%`, which rounds to the printed BMV `34.4%`. `100 × 377/943 = 39.978791%`, which rounds to `40.0%`, not `30.0%`. The count-derived signed difference is `100 × (342/995 − 377/943) = −5.606932` points, which rounds to the printed `−5.6`. The two displayed percentages instead imply `34.4 − 30.0 = +4.4` points.
- **Necessary inputs available:** Counts, PP denominators, displayed rates, effect direction, difference, CI, and P value are complete for the arithmetic check.
- **Exact missing inputs or definitions:** The source gives no alternate ETI denominator, weighted or adjusted rate, row-specific population, retained internal value, or indication of which printed element was intended.
- **Source-grounded alternative interpretation:** An alternate denominator of about 1,257 would make `377` approximately 30.0%, but the printed PP ETI denominator is 943, and using 943 reproduces the signed difference. A production issue could affect one of the printed elements, but the source does not identify it.
- **Direct observation versus inferred explanation:** The table values and labels are direct observations. `40.0%` is the arithmetic result from the printed count and denominator, not an adjudicated replacement. Any alternate denominator or production explanation is inferred.
- **Exact remaining human question:** Which of `377`, `n = 943`, `30.0%`, and `−5.6` represents the intended PP ETI ROSC analysis, and was any denominator or estimator omitted?
- **Status:** Pending Human Adjudication.

## C006 — Main article and eTable report different contributing-centre counts

- **Cited location found:** Yes. DOC-001, [main article Methods, PDF p. 2](../../../jama_jabre_2018_oi_180004.pdf#page=2), Study Design; and DOC-003, [Supplement 2 eTable 1, PDF p. 2](../../../joi180004supp2_prod.pdf#page=2).
- **Source printed value/text matched:** Yes. The main article says the study involved `20` prehospital EMS centers: `15` in France and `5` in Belgium. eTable 1 is titled “Number of Cases That Each Investigator Centre Contributed” and prints 21 distinct row labels: 1, 24, 5, 9, 12, 17, 13, 8, 3, 14, 22, 11, 15, 23, 16, 18, 20, 25, 7, 6, and 2.
- **Comparator matched:** Yes. Every eTable row has at least one participant across its two arms; centre 2 has BMV `0` and ETI `3`. The eTable column totals are labelled BMV `N = 1018` and ETI `N = 1022`.
- **Consistency rule applicable:** Yes, conditionally on “investigator centre” rows and “prehospital EMS centers” representing the same counting unit. Distinct contributing rows can be counted and compared with the article’s centre total.
- **Calculation or logical comparison reproduced:** Counting the eTable labels gives 21 rows. Summing their counts gives BMV `1018` and ETI `1022`, exactly matching the eTable headers and totaling `2040`. The main article’s country counts give `15 + 5 = 20`. Thus, the displayed counts are 21 investigator-centre rows versus 20 EMS centers.
- **Necessary inputs available:** The main centre statement, all eTable row labels and arm counts, and the eTable totals are available. They are sufficient to establish the two displayed counts and the reconciliation of participant totals.
- **Exact missing inputs or definitions:** No crosswalk links investigator-centre identifiers to EMS centers; no source identifies each row’s country, administrative unit, mobile unit, or whether two investigator records belong to one EMS center.
- **Source-grounded alternative interpretation:** One EMS center may be represented by multiple investigator-centre rows, or the two documents may use different administrative units. The main article notes that an EMS center can have one or more mobile intensive care units, but it does not map those units to eTable rows.
- **Direct observation versus inferred explanation:** The 20-centre statement, 21 row labels, arm counts, and reconciled totals are direct observations. A many-to-one mapping or different administrative definition is inferred.
- **Exact remaining human question:** What is the explicit mapping of the 21 investigator-centre rows to the 20 EMS centers, including any rows that share one EMS center?
- **Status:** Pending Human Adjudication.

## C007 — Published primary-endpoint description omits the amended baseline-disability qualification

- **Cited location found:** Yes. DOC-001, [main article abstract, PDF p. 1](../../../jama_jabre_2018_oi_180004.pdf#page=1), Main Outcomes and Measures, and [Methods, PDF p. 3](../../../jama_jabre_2018_oi_180004.pdf#page=3), Outcomes; DOC-002, [protocol amendment comparison, PDF p. 110](../../../joi180004supp1_prod.pdf#page=110), section 4.1.1.
- **Source printed value/text matched:** Yes. The article defines favorable neurological outcome as CPC 1 or 2 / CPC 2 or less. The amended protocol column retains CPC 2 or less and adds that, for neurological disability before randomization, survival with the same degree of disability is considered favorable. Table 2 on [PDF p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6) further says CPCs 1 and 2 were counted as success when coding the primary outcome.
- **Comparator matched:** Yes. The amended baseline-disability qualification is present in Supplement 1 but absent from the article’s abstract, Methods outcome definition, and Table 2 coding footnote.
- **Consistency rule applicable:** Yes as an endpoint-definition comparison. If the amended qualification was part of the algorithm used for the published counts, a CPC-1-or-2-only description is not logically exhaustive because a survivor retaining a worse pre-randomization disability could qualify under the amendment.
- **Calculation or logical comparison reproduced:** No participant-level recalculation is possible. The logical scenario is reproducible: a participant with CPC greater than 2 before randomization who survives with the same disability would be favorable under the amended qualification but not under a literal CPC-1-or-2-only rule.
- **Necessary inputs available:** Both endpoint wordings, the amendment date/context, the published success counts, and the Table 2 coding footnote are available for the definition comparison.
- **Exact missing inputs or definitions:** The supplied sources do not identify the final participant-level coding algorithm, baseline CPC/disability values, day-28 CPC paired with baseline status, how “same degree” was operationalized, or whether any participant relied on the qualification.
- **Source-grounded alternative interpretation:** The article may use an abbreviated general description while the full algorithm retained the qualification, or no enrolled participant may have required it. Alternatively, the published coding may have used only CPC 1 or 2. The supplied aggregate sources do not distinguish these possibilities.
- **Direct observation versus inferred explanation:** The article wording, amended wording, Table 2 footnote, and aggregate counts are direct observations. Any effect on classification or counts is inferred because participant-level coding evidence is absent.
- **Exact remaining human question:** What exact algorithm generated the primary counts, and did any participant qualify as favorable solely because survival preserved the same pre-randomization disability?
- **Status:** Pending Human Adjudication.

## C008 — Protocol composite technique-failure definition cannot reconcile with the article’s smaller ETI failure count if they are the same endpoint

- **Cited location found:** Yes. DOC-002, [protocol amendment comparison, PDF p. 110](../../../joi180004supp1_prod.pdf#page=110), Secondary Endpoints; DOC-001, [abstract, PDF p. 1](../../../jama_jabre_2018_oi_180004.pdf#page=1), [flow and Results, PDF p. 4](../../../jama_jabre_2018_oi_180004.pdf#page=4), and [Table 3, PDF p. 6](../../../jama_jabre_2018_oi_180004.pdf#page=6).
- **Source printed value/text matched:** Yes. The amended protocol defines technique failure as 28-day mortality, regurgitation during the procedure, or procedural failure, clarified as failure to ventilate for BMV or failure to intubate for ETI. The article prints ETI failure `21/996 (2.1%)`. The ETI ITT population has `54/1022` deaths by day 28.
- **Comparator matched:** Yes. The flow prints 1023 randomized to ETI, 1022 in ETI ITT, 999 in the ETI-side safety analysis display, and 24 excluded in that display. Table 3 labels its analysis “Safety Population” but uses `996` as the ETI denominator for the failure row, three fewer than the `999` shown for ETI complications.
- **Consistency rule applicable:** Conditionally. For the same endpoint in the same aligned source population, a union containing all 28-day deaths cannot have fewer events than its mortality component. The rule cannot be applied unconditionally across ITT and actual-treatment/safety displays without a participant crosswalk.
- **Calculation or logical comparison reproduced:** The ledger’s conservative displayed-flow calculation is `54 − 24 = 30`, and `30 > 21`. If the three additional participants absent from the Table 3 failure denominator were also all deaths, the corresponding conservative bound would be `54 − 24 − 3 = 27`, still greater than 21. However, these bounds assume the ETI-side flow exclusions identify every ETI-randomized participant outside the exact 996-person failure population; the article defines safety by treatment actually received and shows crossover, so that assumption is not mechanically established from aggregate displays alone.
- **Necessary inputs available:** The amended composite definition, ETI ITT deaths, randomized and flow counts, safety-population concept, Table 3 failure count/denominator, and regurgitation count are available. They are sufficient to reproduce the conditional comparison but not to prove participant-set alignment.
- **Exact missing inputs or definitions:** The article does not define the Table 3 “failure” row; does not state whether it is the amended composite; does not explain why its ETI denominator is 996 rather than 999; does not give 28-day deaths within the exact 996-person population; and does not provide participant-level mappings among randomization arm, actual treatment, crossover, mortality, regurgitation, procedural failure, and Table 3 inclusion.
- **Source-grounded alternative interpretation:** The article’s failure row may be a narrower procedural endpoint, which is consistent with its separate reporting of mortality and regurgitation. It may also use an actual-treatment population not directly comparable with ETI ITT mortality. Either interpretation would make the aggregate counts non-nested, but the row’s exact definition is not supplied.
- **Direct observation versus inferred explanation:** The protocol definition, flow counts, ITT deaths, Table 3 values, and safety-population label are direct observations. Treating Table 3 failure as the same composite, assigning the 24 and 3 omitted participants to death status, or treating the row as a narrower endpoint are inferences.
- **Exact remaining human question:** What exact event definition and participant set produced ETI `21/996`, how do those 996 participants map to the ETI ITT and actual-treatment populations, and is this row intentionally distinct from the amended composite technique-failure endpoint?
- **Status:** Pending Human Adjudication.

## Coverage and limitations

- Stable IDs assigned: 8 (`C001`–`C008`).
- Stable IDs separately rechecked: 8 of 8.
- Cited PDF location sets found: 8 of 8.
- Source printed value/text blocks matched: 8 of 8.
- Comparator blocks matched: 8 of 8.
- Arithmetic or logical comparisons reproduced: 8 of 8.
- IDs with all inputs needed for the narrow displayed-value comparison: C001, C002, C003, C005, and C006.
- IDs whose exact estimator, classification, or population alignment remains unavailable: C004, C007, and C008; C002 and C003 also lack the underlying summary/estimator definitions needed to identify intended reporting.
- No new OCR was run. No legacy audit derivative was read as evidence. No candidate rests on a display-zero P value.

All eight candidates remain **Pending Human Adjudication**. This recheck records observations,
conditional calculations, source limitations, and human questions; it does not assign severity,
validity, acceptance, rejection, exclusion, or a final correction.
