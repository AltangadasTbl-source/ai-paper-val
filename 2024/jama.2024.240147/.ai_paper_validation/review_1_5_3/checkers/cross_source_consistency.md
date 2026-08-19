# Cross-Source Consistency Review

## Scope and method

- **Assigned sources checked:** main article DOC-001; protocol and SAP in DOC-002; results supplement DOC-003; administrative DOC-004 and DOC-005.
- **Evidence authority:** supplied PDFs. The current quantitative maps were used only to locate and enumerate relationships; every observation below was checked against the direct PDF page named in its link.
- **Matching rule:** a value was compared only where population, time window, contrast, analysis set, model/adjustment, measure, scale, unit, reference group, and displayed precision were the same or where a printed numerator/denominator/percentage identity itself was being tested. Planned protocol/SAP quantities were not treated as comparators for observed trial results.
- **Relationships checked:** 29 matched quantitative relationships (primary/key-secondary outcomes, Figure 2 exploratory outcomes, Figure 4/eTable 7 subgroups, intervention/exposure measures, baseline and adverse-event rows, participant flow, and sample-size/model/definition occurrences); 11 protocol/SAP definition or planning relationships were checked for non-applicability to observed results.
- **Qualifying candidate observations:** 7. These are not stable candidate IDs and are all **Pending Human Adjudication**.

## Qualifying candidate observations

### 1. Liberal walk-in transport percentage does not reconcile with its displayed count and denominator

- **Category:** Rate-versus-count inconsistency.
- **Exact source location:** [DOC-003, eTable 2, PDF p. 15](../../../joi240147supp2_prod_1738701765.29201.pdf#page=15), “Type of transport to the trauma center,” liberal oxygen group, “Walk-in.”
- **Printed value:** `4/743 (5.3)`.
- **Comparison logic:** This row explicitly labels the quantity `no./total no. (%)`; thus its percentage must be the percentage represented by the displayed numerator and denominator, to the shown one decimal place.
- **Calculation:** 4 / 743 x 100 = 0.538...%, which rounds to **0.5%**, not 5.3%.
- **Supported alternatives:** The displayed count or denominator could be wrong; alternatively, the percentage may have been intended as 0.5%. The supplied source does not identify which field is authoritative.
- **Human verification steps:** Inspect the analytic transport variable for liberal-group walk-ins; confirm the count and denominator; then verify the one-decimal percentage in the source table and downstream extraction dataset.

### 2. Liberal vascular-surgery percentage is nonzero despite a displayed zero numerator

- **Category:** Rate-versus-count inconsistency.
- **Exact source location:** [DOC-003, eTable 2, PDF p. 15](../../../joi240147supp2_prod_1738701765.29201.pdf#page=15), “Surgery performed in the trauma resuscitation room,” liberal oxygen group, “Vascular surgery.”
- **Printed value:** `0/747 (1.1)`.
- **Comparison logic:** The row is labelled `no./total no. (%)`; a zero numerator with a positive denominator has a percentage of zero on any nonnegative percentage scale.
- **Calculation:** 0 / 747 x 100 = **0.0%**, whereas the displayed percentage is **1.1%**.
- **Supported alternatives:** The numerator may have been intended to be a nonzero value (approximately 8/747 would round to 1.1%), or the displayed percentage may have been intended as 0.0%. The supplied documents do not resolve this.
- **Human verification steps:** Check the liberal-group resuscitation-room surgery records and table-program output; establish the intended numerator and replace/reconfirm the percentage accordingly.

### 3. The all-patient further-adjusted primary-outcome confidence-interval upper limit differs across two Supplement 2 tables

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-003, eTable 4, PDF p. 17](../../../joi240147supp2_prod_1738701765.29201.pdf#page=17), primary outcome, “Adjusted odds ratio (95% CI)”; [DOC-003, eTable 7, PDF p. 20](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20), “All patients,” “Adjusted odds ratio (95% CI).”
- **Population/time/contrast/measure matched:** 733 restrictive versus 724 liberal primary-analysis patients; death and/or major respiratory complications within 30 days; restrictive-versus-liberal odds ratio; displayed as an adjusted odds ratio with 95% CI.
- **Printed values:** eTable 4: **0.98 (0.68 to 1.41)**. eTable 7: **0.98 (0.68 to 1.39)**.
- **Comparison logic:** These table rows name the same all-patient population, outcome, contrast, effect scale, and adjusted-estimate label. The point estimate and lower confidence limit agree, while the displayed upper confidence limit differs at the reported two-decimal precision.
- **Supported alternatives:** The two “Adjusted odds ratio” columns could use nonidentical covariate specifications that are not stated in the table footnotes; if so, the labels insufficiently distinguish the models. If the model is the same, one printed upper limit is inconsistent.
- **Human verification steps:** Obtain the table specifications/code for eTables 4 and 7; compare the covariate and missing-data handling for the all-patient adjusted model; confirm the unrounded interval and the intended displayed upper limit.

### 4. The liberal AIS-less-than-3 subgroup percentage conflicts between Figure 4 and eTable 7 and with its count/denominator

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001, Figure 4, PDF p. 8](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8), moderate/severe TBI, `AIS score <3`; [DOC-003, eTable 7, PDF p. 20](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20), moderate/severe traumatic brain injury, `AIS <3`.
- **Population/time/contrast/measure matched:** Liberal oxygen group; primary composite within 30 days; subgroup with AIS score below 3; displayed event count, denominator, and percentage.
- **Printed values:** Figure 4 prints **48/473 (10.1)**. eTable 7 prints **48/473 (9.2)**.
- **Comparison logic:** The numerator and denominator are identical across locations, so the percentage is directly comparable. 48 / 473 x 100 = 10.148...%, which rounds to **10.1%**, agreeing with Figure 4 and not eTable 7.
- **Supported alternatives:** eTable 7’s percentage is likely a transcription/display error; the supplied source alone cannot establish whether a distinct undisclosed denominator was used, because the printed denominator is 473 in both locations.
- **Human verification steps:** Verify the subgroup dataset and the eTable 7 rendering; confirm that 48 events among 473 liberal participants was the intended display and correct/reconfirm the percentage.

### 5. The liberal known-lung-disease subgroup percentage conflicts between Figure 4 and eTable 7 and with its count/denominator

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-001, Figure 4, PDF p. 8](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=8), known lung disease, `Yes`; [DOC-003, eTable 7, PDF p. 20](../../../joi240147supp2_prod_1738701765.29201.pdf#page=20), known lung disease, `Yes`.
- **Population/time/contrast/measure matched:** Liberal oxygen group; primary composite within 30 days; known-lung-disease subgroup; displayed event count, denominator, and percentage.
- **Printed values:** Figure 4 prints **14/69 (20.3)**. eTable 7 prints **14/69 (20.2)**.
- **Comparison logic:** The same count and denominator are displayed. 14 / 69 x 100 = 20.289...%, which rounds to **20.3%** at one decimal place, matching Figure 4 rather than eTable 7.
- **Supported alternatives:** eTable 7 may contain a rounding/transcription error, or one table may have used a different unreported rounding rule. The latter is not specified in the supplied sources.
- **Human verification steps:** Check the unrounded subgroup percentage and the two table production files; confirm the required rounding convention and reconcile the displayed percentage.

### 6. eTable 10’s post-randomization-exclusion total and group cells do not reconcile with each other or with Figure 1

- **Category:** Cross-document numeric inconsistency.
- **Exact source locations:** [DOC-003, eTable 10, PDF p. 24](../../../joi240147supp2_prod_1738701765.29201.pdf#page=24), “Exclusion after randomization”; [DOC-001, Figure 1, PDF p. 3](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3), “Excluded after randomization.”
- **Population/time/contrast/measure matched:** Participants excluded after randomization, reported by assigned oxygen group, before the secondary-exclusion line in the trial flow.
- **Printed values:** eTable 10 header: **N=130**; restrictive **55/750 (45)**; liberal **67/758 (55)**. Figure 1: restrictive **59 excluded after randomization**; liberal **71 excluded after randomization** (total **130**).
- **Comparison logic:** The eTable’s displayed group counts total 55 + 67 = **122**, not its stated N=130. Figure 1 supplies 59 + 71 = **130**. Each Figure 1 group count exceeds the corresponding eTable 10 count by four. eTable 10’s 45%/55% partition matches 55/122 and 67/122, not a partition of the printed N=130 or the group denominators 750/758.
- **Supported alternatives:** The table may intentionally omit the four restrictive and four liberal participants “omitted according to Swiss law due to withdrawn consent” listed in Figure 1, while retaining Figure 1’s total N=130. However, eTable 10 does not state that exclusion or define its N=130/denominator basis; its footnote only explains two missing randomized-oxygen data for the separate secondary-exclusion row.
- **Human verification steps:** Determine whether the eight Swiss-law omissions were deliberately excluded from eTable 10; if yes, revise the row’s total, denominators, and footnote to identify its population; if no, reconcile the group counts and percentages to Figure 1.

### 7. eTable 10 labels secondary-exclusion group fractions with incompatible denominators

- **Category:** Denominator, proportion, or total inconsistency.
- **Exact source location:** [DOC-003, eTable 10, PDF p. 24](../../../joi240147supp2_prod_1738701765.29201.pdf#page=24), “Secondary exclusion.” Comparator for count identity: [DOC-001, Figure 1, PDF p. 3](../../../jama_arleth_2024_oi_240147_1738701765.27201.pdf#page=3).
- **Population/time/contrast/measure matched:** Secondary exclusions after randomization, restrictive and liberal groups.
- **Printed values:** eTable 10: header **N=341**; restrictive **174/750 (51)**; liberal **165/758 (49)**. Figure 1 prints **174** restrictive and **165** liberal secondary exclusions. The eTable footnote says two patients had missing randomized-oxygen data, explaining the discrepancy between N=341 and the displayed cell counts.
- **Comparison logic:** The counts are concordant with Figure 1 and total 339. The percentages 51 and 49 are the partition of 339 (174/339 = 51.3%; 165/339 = 48.7%), not percentages of the displayed within-group denominators (174/750 = 23.2%; 165/758 = 21.8%). Therefore the printed `no./total no. (%)` format pairs a within-group denominator with a cross-row partition percentage. The N=341 header is also not the sum of the two displayed counts, although the footnote identifies two unassigned patients.
- **Supported alternatives:** The intended presentation may be a distribution of the 339 classified secondary exclusions (51% restrictive, 49% liberal), in which case `/750` and `/758` are inappropriate denominators for those percentages. Alternatively, the intended presentation may be within-group exclusion proportions, in which case 23.2% and 21.8% would be the relevant rounded values. The source does not specify which estimand was intended.
- **Human verification steps:** Confirm whether eTable 10 is meant to show allocation distribution or within-group exclusion incidence; use one denominator consistently; describe the two missing randomized-oxygen assignments separately and reconcile the stated N=341 with the classified counts.

## Checked matched relationships without a qualifying cross-source difference

- **Primary outcome:** Abstract, Key Points, Results, Figure 2, Figure 4, and eTable 4 consistently display 118/733 (16.1%) versus 121/724 (16.7%) and OR 1.01 (0.75 to 1.37), where the same stratification-adjusted model is named. eTable 4’s further-adjusted estimate was considered separately in observation 3.
- **Key secondary outcomes:** Figure 2 and eTable 4 agree for death (63/733 versus 53/724; OR 1.28 [0.85 to 1.92]) and major respiratory complications (65/733 versus 78/724; OR 0.84 [0.59 to 1.19]).
- **Exploratory outcomes:** Figure 2 and eTable 5 agree for hypoxemic episodes, ICU readmission, sepsis, surgical-site infection, and postdischarge pneumonia after matching each outcome’s stated population and time window. The source’s statement that no exploratory outcome remained significant after FDR adjustment is compatible with eTable 5’s unadjusted-model P values and does not supply a conflicting adjusted P value.
- **Intervention/exposure:** Main-text medians for nonintubated oxygen flow, intubated FiO2, and major protocol violations agree with eFigure/eTable 3 after matching units, time (eight-hour intervention), and denominators where printed.
- **Adverse events:** Main-text atelectasis percentages (27.6% restrictive; 34.7% liberal) agree with eTable 9’s 207/750 and 263/758. eTable 9’s death denominator differs from the primary outcome because its footnote defines adverse-event observation through possible consent withdrawal; it was not treated as a same-analysis-set comparator.
- **Flow:** Figure 1 and eTable 10 agree on the classified secondary-exclusion counts (174 restrictive; 165 liberal), while the denominator/percentage presentation remains a candidate in observation 7. Figure 3’s cause-specific event rows were not compared directly with Figure 2’s binary 30-day outcome totals because their cumulative-incidence/display population and event classification are not defined as the same measure.
- **Protocol/SAP versus report:** Sample-size values (710 per arm/1420 total, assumed 10% versus 15%, 80% power, 5% significance) and the final SAP’s outcome/model definitions are planning/specification material and do not conflict with the observed analyses after accounting for planned versus actual time and analysis population. Earlier protocol-version thresholds and interim targets were treated as superseded planning material, not matched observed results.
- **Administrative supplements:** DOC-004 contains collaborator-roster pagination only; DOC-005 is a data-sharing statement. Neither provides a matched analyzed result.
- **Display/formatting checked but not a candidate:** [DOC-003, eTable 11, PDF p. 25](../../../joi240147supp2_prod_1738701765.29201.pdf#page=25) prints `135//750 (18.0)`. The double slash is a presentation defect, but 135/750 = 18.0% and no conflicting matched quantitative value was found; it is therefore not registered as a quantitative-consistency candidate in this checker.

## Limitations

- No raw dataset, statistical code, or table-production files were supplied; the supported alternatives and human questions above cannot be resolved from the PDFs alone.
- The protocol contains multiple versions and planning quantities. These were compared only after version and planning-versus-observed status were made explicit; they cannot establish an observed-result conflict by themselves.
- This artifact assigns neither stable C IDs nor an AI judgment. Candidate registration, source recheck, and human adjudication remain separate stages.
