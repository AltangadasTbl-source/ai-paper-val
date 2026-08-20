# Mechanical Evidence Recheck

This artifact mechanically rechecks every stable candidate in `candidate_ledger.md` against the exact supplied-source PDF locations. Fresh layout text and rendered pages were used only as locators and visual aids; the supplied PDFs remained the authority. No candidate is adjudicated here. Every candidate remains **Pending Human Adjudication**.

## C001 — Spontaneous-delivery hazard ratio conflicts across narrative and Figure 2B

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Primary Outcome narrative below Table 2, and DOC-001 `jama_saccone_2017_oi_170144.pdf#page=6`, Figure 2 panel B, “Spontaneous delivery only.”
- **Source printed value/text matched:** Yes. The p. 5 narrative prints “hazard ratio, 0.36; 95% CI, 0.54-0.87” for the survival analysis to 34 weeks.
- **Comparator printed value/text matched:** Yes. Figure 2B prints “Hazard ratio, 0.68; 95% CI, 0.54-0.87” and labels the panel “Spontaneous delivery only.”
- **Consistency rule applicable:** Yes. A hazard-ratio point estimate must lie within its ordered CI on the same scale. Matched occurrences of the same outcome, analysis context, and CI should also report the same point estimate unless the source identifies a different model or contrast.
- **Calculation or logical comparison reproduced:** Yes. `0.36 != 0.68`; `0.36 < 0.54`, so the narrative point estimate is not contained in `[0.54, 0.87]`; `0.54 <= 0.68 <= 0.87`, so the Figure 2B estimate is contained. The CI endpoints are identical at both locations.
- **Necessary inputs available:** The two point estimates, both CI endpoints, outcome label, survival-analysis context, and Figure 2 panel identity are available and sufficient for mismatch and containment checks.
- **Exact missing inputs or definitions:** The fitted Cox coefficient, standard error, model output, event-level analysis data, and a source statement identifying which HR is authoritative are not supplied.
- **Alternative source-grounded interpretation:** Figure 2A is explicitly a different “All delivery types” analysis and reports HR 0.70 (95% CI, 0.55-0.88), but that distinction does not reconcile the p. 5 spontaneous-delivery narrative with panel B. It remains possible that the narrative and panel B unexpectedly use different Cox specifications, although the package does not name such a distinction and both print the same CI.
- **Direct observation versus inferred explanation:** Direct observation: the narrative prints 0.36 with 0.54-0.87, while spontaneous-delivery panel B prints 0.68 with 0.54-0.87. Inferred, not established: a transcription error, swapped model result, or unreported model difference caused the conflict.
- **Exact remaining human question:** What HR and 95% CI were produced by the intended spontaneous-delivery Cox analysis through 34 weeks, and which printed occurrence corresponds to that output?

## C002 — SPTB under 32 weeks difference does not round from printed counts

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, “Spontaneous preterm birth, No. (%), <32 wk.”
- **Source printed value/text matched:** Yes. The row prints pessary `10 (6.7)` and control `14 (9.3)` under arm headers `n = 150`.
- **Comparator printed value/text matched:** Yes. The between-group difference is printed as `-2.6` percent with 95% CI `-4.1 to 9.4`.
- **Consistency rule applicable:** Yes. Using the exact printed counts and denominators, the crude percentage-point difference is `100*(x_p/n_p - x_c/n_c)`; standard nearest one-decimal rounding has a 0.05-point half-unit tolerance.
- **Calculation or logical comparison reproduced:** Yes. `100*(10/150 - 14/150) = -2.666666...`, which rounds to `-2.7%`. The printed `-2.6%` instead equals subtraction of the already rounded percentages, `6.7 - 9.3 = -2.6`.
- **Necessary inputs available:** Counts, arm denominators, displayed percentages, contrast order, and printed difference are available and sufficient for the exact-fraction diagnostic.
- **Exact missing inputs or definitions:** The table-production code and an explicit rule stating whether point differences were calculated from exact risks, unrounded internal risks, rounded displayed percentages, or another analysis denominator are not supplied.
- **Alternative source-grounded interpretation:** The printed value is reproducible if the displayed one-decimal percentages were subtracted. The methods on DOC-001 p. 4 state that effects were quantified as differences in cumulative incidence and that 95% CIs used bootstrap methods, but they do not state that rounded percentages generated the point estimate.
- **Direct observation versus inferred explanation:** Direct observation: the counts, denominators, percentages, and `-2.6%` difference coexist in the row. Inferred, not established: rounded displayed percentages rather than exact fractions generated the point estimate.
- **Exact remaining human question:** Was the intended point difference computed from exact risks as `-2.7%`, from displayed rounded percentages as `-2.6%`, or from another explicitly defined denominator or calculation?

## C003 — Operative-vaginal-delivery difference does not round from printed counts

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, “Operative vaginal delivery, No. (%).”
- **Source printed value/text matched:** Yes. The row prints pessary `5 (3.3)` and control `10 (6.7)` under arm headers `n = 150`.
- **Comparator printed value/text matched:** Yes. The between-group difference is `-3.4` percent with 95% CI `-2.1 to 9.1`.
- **Consistency rule applicable:** Yes. Exact printed fractions define the crude percentage-point difference, and standard one-decimal rounding has a 0.05-point half-unit tolerance.
- **Calculation or logical comparison reproduced:** Yes. `100*(5/150 - 10/150) = -3.333333...`, which rounds to `-3.3%`; subtraction of displayed percentages gives `3.3 - 6.7 = -3.4%`.
- **Necessary inputs available:** The two counts, both arm denominators, displayed percentages, contrast order, and printed difference are available for the diagnostic calculation.
- **Exact missing inputs or definitions:** The point-estimate production code and an explicit convention governing exact-fraction versus rounded-display subtraction are absent. No alternative analysis denominator is printed.
- **Alternative source-grounded interpretation:** The `-3.4%` value is exactly reproducible from the displayed rounded percentages. DOC-001 p. 4 describes a between-group difference in cumulative incidence but does not define rounded-display subtraction.
- **Direct observation versus inferred explanation:** Direct observation: the row prints all compared values. Inferred, not established: the point difference was produced by subtracting rounded table percentages or by an unreported alternative computation.
- **Exact remaining human question:** Is `-3.4%` the intended operative-vaginal-delivery point difference, and what explicit denominator and rounding convention generated it?

## C004 — Chorioamnionitis difference does not round from printed counts

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, “Chorioamnionitis, No. (%).”
- **Source printed value/text matched:** Yes. The row prints pessary `5 (3.3)` and control `7 (4.7)` under arm headers `n = 150`.
- **Comparator printed value/text matched:** Yes. The between-group difference is `-1.4` percent with 95% CI `-3.7 to 6.6`.
- **Consistency rule applicable:** Yes. Exact printed fractions define the crude percentage-point difference under the stated arm sizes; the one-decimal rounding half-unit is 0.05 percentage points.
- **Calculation or logical comparison reproduced:** Yes. `100*(5/150 - 7/150) = -1.333333...`, which rounds to `-1.3%`; displayed-percentage subtraction gives `3.3 - 4.7 = -1.4%`.
- **Necessary inputs available:** The event counts, arm denominators, displayed percentages, contrast order, and point difference are available for exact-fraction comparison.
- **Exact missing inputs or definitions:** The production rule for the point difference, internal unrounded values or code, and any intended denominator different from 150 are not supplied.
- **Alternative source-grounded interpretation:** The printed `-1.4%` is reproducible by subtracting the displayed rounded percentages. The source methods describe cumulative-incidence differences but do not specify that display-rounded values are the computational inputs.
- **Direct observation versus inferred explanation:** Direct observation: the complete printed row and arm headers match the ledger. Inferred, not established: rounded display values or another unstated convention explain the difference.
- **Exact remaining human question:** Should the exact-fraction result be displayed as `-1.3%`, or was `-1.4%` intentionally produced under a documented rounded-percentage or alternative-denominator convention?

## C005 — Perinatal-death difference does not round from printed counts

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, “Perinatal death, No. (%).”
- **Source printed value/text matched:** Yes. The row prints pessary `2 (1.3)` and control `4 (2.7)` under arm headers `n = 150`.
- **Comparator printed value/text matched:** Yes. The between-group difference is `-1.4` percent with 95% CI `-2.5 to 5.6`.
- **Consistency rule applicable:** Yes. Exact printed counts and denominators define the crude percentage-point contrast; the standard one-decimal half-unit is 0.05 percentage points.
- **Calculation or logical comparison reproduced:** Yes. `100*(2/150 - 4/150) = -1.333333...`, which rounds to `-1.3%`; displayed-percentage subtraction gives `1.3 - 2.7 = -1.4%`.
- **Necessary inputs available:** Counts, denominators, displayed percentages, contrast direction, and point difference are available for the arithmetic check.
- **Exact missing inputs or definitions:** The production code, explicit point-estimate rounding convention, and any denominator other than the printed 150 per arm are unavailable.
- **Alternative source-grounded interpretation:** The table value is reproducible from subtraction of the displayed one-decimal percentages, while DOC-001 p. 4 describes differences in cumulative incidence without specifying this rounded-display convention.
- **Direct observation versus inferred explanation:** Direct observation: all compared values are printed in the cited row. Inferred, not established: table formatting values were reused as calculation inputs or an alternate computation was used.
- **Exact remaining human question:** Is the intended perinatal-death difference the exact-fraction result rounded to `-1.3%`, the displayed-percentage subtraction `-1.4%`, or a value from another documented calculation?

## C006 — Birth weight under 2500 g difference lies outside its printed CI

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-003 `joi170144supp2_prod.pdf#page=3`, eTable 2, “Birth weight <2,500 grams.”
- **Source printed value/text matched:** Yes. The row prints pessary `28 (18.7%)`, control `45 (30.0%)`, and between-group difference `-11.3` percent.
- **Comparator printed value/text matched:** Yes. The same difference cell prints 95% CI `-1.1 to +21.2`; the row also prints RR `0.62 (0.41 to 0.94)` and `p-value 0.03`.
- **Consistency rule applicable:** Yes. A point estimate and its labeled CI must use the same contrast and scale, with the point lying between ordered endpoints.
- **Calculation or logical comparison reproduced:** Yes. `100*(28/150 - 45/150) = -11.333333...`, consistent with `-11.3%`, but `-11.3 < -1.1`, so `-11.3` is outside `[-1.1, 21.2]`. The sign-reversed point `+11.3` would lie inside that printed interval.
- **Necessary inputs available:** Both counts, denominators, the risk-difference point estimate, CI endpoints, RR, and P value are available and sufficient for direction and containment checks.
- **Exact missing inputs or definitions:** Bootstrap replicates, complete risk-difference CI procedure/output, resampling details, and the intended contrast direction for the printed CI are not supplied; therefore an intended replacement interval cannot be mechanically reconstructed.
- **Alternative source-grounded interpretation:** The CI may have been calculated or printed for the reverse contrast (control minus pessary), because `+11.3` is contained in `[-1.1, +21.2]`, while the point estimate and RR use the pessary-versus-control direction. This would still leave a within-row contrast-label mismatch and is an inferred explanation, not an authoritative resolution.
- **Direct observation versus inferred explanation:** Direct observation: the negative point estimate is outside its printed CI, and arm risks and RR both favor the same negative/lower-risk direction. Inferred, not established: CI endpoints/signs were transcribed incorrectly or the CI used the reverse group contrast.
- **Exact remaining human question:** What signed 95% CI was produced for the pessary-minus-control `-11.3%` risk difference, and did the displayed CI use the opposite contrast or contain an endpoint/sign transcription?

## C007 — Respiratory-distress-syndrome difference does not round from printed counts

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-003 `joi170144supp2_prod.pdf#page=3`, eTable 2, “Respiratory distress syndrome.”
- **Source printed value/text matched:** Yes. The row prints pessary `14 (9.3%)` and control `31 (20.7%)` under headers `N=150` for each arm.
- **Comparator printed value/text matched:** Yes. The between-group difference is `-11.4` percent with 95% CI `-19.9 to -2.9`.
- **Consistency rule applicable:** Yes. The exact printed fractions determine the crude percentage-point contrast under standard nearest one-decimal rounding.
- **Calculation or logical comparison reproduced:** Yes. `100*(14/150 - 31/150) = -11.333333...`, which rounds to `-11.3%`; subtraction of displayed percentages gives `9.3 - 20.7 = -11.4%`.
- **Necessary inputs available:** Event counts, both denominators, displayed percentages, contrast order, and printed difference are all available for the arithmetic comparison.
- **Exact missing inputs or definitions:** The table-production code and explicit rule for calculating point differences from exact versus display-rounded risks are absent; no alternative denominator is stated.
- **Alternative source-grounded interpretation:** The printed `-11.4%` exactly matches subtraction of the displayed rounded percentages. eTable 2 states that data are numbers and percentages but does not define this as the point-estimate calculation rule.
- **Direct observation versus inferred explanation:** Direct observation: the full row and arm headers match the ledger. Inferred, not established: display-rounded percentages were subtracted rather than exact risks.
- **Exact remaining human question:** Was `-11.4%` intentionally calculated from the displayed percentages, or should the exact-fraction result be displayed as `-11.3%` under the intended convention?

## C008 — Cervical-length subgroup difference is on the opposite side of the rounding boundary

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-003 `joi170144supp2_prod.pdf#page=4`, eTable 3, “TVU CL <=10mm” subgroup for spontaneous preterm birth at less than 34 weeks.
- **Source printed value/text matched:** Yes. The row prints pessary `3/56 (5.4%)` and control `10/42 (23.8%)`.
- **Comparator printed value/text matched:** Yes. The between-group difference is `-18.4` percent with 95% CI `-34.6 to -3.3`.
- **Consistency rule applicable:** Yes. The source supplies exact subgroup fractions, so the crude percentage-point difference can be computed and rounded to one decimal; the rounding boundary is material here.
- **Calculation or logical comparison reproduced:** Yes. `100*(3/56 - 10/42) = -18.452380...`, whose nearest one-decimal value is `-18.5%`. Subtracting displayed percentages gives `5.4 - 23.8 = -18.4%`. The exact value is approximately 0.00238 percentage points beyond the `-18.45` midpoint toward `-18.5`.
- **Necessary inputs available:** Exact numerators and denominators, displayed percentages, contrast order, and printed point difference are available for the diagnostic calculation.
- **Exact missing inputs or definitions:** The point-estimate production code and explicit convention for exact-fraction versus displayed-percentage subtraction are missing. No record states how values at or near a one-decimal rounding boundary were handled.
- **Alternative source-grounded interpretation:** The reported `-18.4%` is reproducible from the displayed percentages. eTable 3 expressly presents number/total number and percentage but does not state that rounded percentages, rather than the fractions, define the between-group point difference.
- **Direct observation versus inferred explanation:** Direct observation: all fractions, percentages, and `-18.4%` are printed in the cited subgroup row. Inferred, not established: a rounded-display subtraction convention caused the boundary-side difference.
- **Exact remaining human question:** Was the intended subgroup difference computed from exact fractions and rounded to `-18.5%`, or from displayed percentages to obtain `-18.4%`, and which convention governs the table?

## C009 — Cesarean-delivery difference lies outside its printed CI

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, “Cesarean delivery, No. (%).”
- **Source printed value/text matched:** Yes. The row prints pessary `45 (30.0)`, control `57 (38.0)`, and between-group difference `-8.0` percent.
- **Comparator printed value/text matched:** Yes. The same difference cell prints 95% CI `-3.2 to 19.0`; the row also prints RR `0.79 (0.57-1.09)` and `P=.18`.
- **Consistency rule applicable:** Yes. A point estimate must lie within its own ordered interval when both are labeled as the same between-group difference.
- **Calculation or logical comparison reproduced:** Yes. `30.0 - 38.0 = -8.0`, but `-8.0 < -3.2`, so `-8.0` is outside `[-3.2, 19.0]`. The sign-reversed point `+8.0` is inside the printed interval.
- **Necessary inputs available:** Arm risks/counts, point difference, CI endpoints, contrast display, RR, and P value are available and sufficient for containment and direction checks.
- **Exact missing inputs or definitions:** The bootstrap draws and complete CI analysis output are absent. The package does not state that this row's CI intentionally uses a contrast opposite to its point estimate, and it supplies no authoritative alternate endpoints.
- **Alternative source-grounded interpretation:** The CI could reflect control minus pessary while the point estimate reflects pessary minus control, because `+8.0` lies within `[-3.2, 19.0]`. The common Table 2 “Between-Group Difference” column does not label mixed directions, so this remains a possible explanation for, not a resolution of, the observed mismatch.
- **Direct observation versus inferred explanation:** Direct observation: the printed `-8.0` point lies outside the printed CI, while the arm percentages reproduce `-8.0`. Inferred, not established: the CI used the reverse contrast or suffered a sign/endpoint production error.
- **Exact remaining human question:** What signed bootstrap 95% CI belongs to the pessary-minus-control cesarean-delivery difference, and was the displayed interval computed in the reverse direction?

## C010 — Operative-vaginal-delivery difference lies outside its printed CI

- **Status:** Pending Human Adjudication.
- **Cited location found:** Yes. DOC-001 `jama_saccone_2017_oi_170144.pdf#page=5`, Table 2, “Operative vaginal delivery, No. (%).”
- **Source printed value/text matched:** Yes. The row prints pessary `5 (3.3)`, control `10 (6.7)`, and between-group difference `-3.4` percent.
- **Comparator printed value/text matched:** Yes. The same difference cell prints 95% CI `-2.1 to 9.1`; the row also prints RR `0.50 (0.18-1.43)` and `P=.29`.
- **Consistency rule applicable:** Yes. A point estimate must be contained in its own ordered CI when the source labels both as the same between-group difference.
- **Calculation or logical comparison reproduced:** Yes. `-3.4 < -2.1`, so the printed point is outside `[-2.1, 9.1]`. The displayed percentages reproduce `3.3 - 6.7 = -3.4`, while the sign-reversed point `+3.4` lies inside the printed interval.
- **Necessary inputs available:** Counts, arm denominators, displayed risks, point estimate, interval endpoints, RR, and P value are available for containment and direction checks.
- **Exact missing inputs or definitions:** Bootstrap replicates, complete CI construction output, and an explicit intended CI contrast direction are unavailable, so no replacement CI can be derived from supplied evidence.
- **Alternative source-grounded interpretation:** The interval may have been generated for control minus pessary while the point estimate is displayed as pessary minus control, since `+3.4` is contained. The table header does not identify opposite directions within one cell, so this is an inferred production explanation and not an authoritative resolution.
- **Direct observation versus inferred explanation:** Direct observation: `-3.4` is not contained in its printed CI, and the arm percentages support the negative point direction. Inferred, not established: reversed-contrast CI computation or a sign/endpoint transcription caused the display.
- **Exact remaining human question:** What signed bootstrap 95% CI belongs to the intended operative-vaginal-delivery point difference, and is the printed point estimate paired with a reverse-contrast interval?

## Recheck Summary

- **Stable IDs mechanically checked:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010.
- **Cited source locations found:** 10 of 10 candidates; 11 candidate-location occurrences because C001 has two cited PDF pages.
- **Unresolved evidence inputs:** Authoritative Cox output for C001; explicit point-difference rounding/production rules for C002-C005, C007, and C008; bootstrap draws or authoritative signed risk-difference CI outputs for C006, C009, and C010.
- **Adjudication status:** Every candidate remains Pending Human Adjudication.
