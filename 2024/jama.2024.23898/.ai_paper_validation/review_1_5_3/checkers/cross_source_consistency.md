# Cross-Source Consistency Review

## Scope, method, and result

This review checked every mapped matched result and definition across the five supplied direct sources: the main article (DOC-001, pp. 1-10), protocol (DOC-002, pp. 1-66), SAP (DOC-003, pp. 1-40), results supplement (DOC-004, pp. 1-2), and data-sharing statement (DOC-005, p. 1). It used the two current quantitative evidence maps as relationship locators and verified the candidate comparators in the supplied PDFs or their direct-source page extraction. It did not use old checker, candidate, verification, quality, or report conclusions, and it did not use web sources.

Before calling a difference, each comparison was matched for population, intervention contrast, analysis set, outcome/measure, time window, model, scale, unit, reference group, and displayed precision. Four distinct candidate consistency issues met the threshold. They have no stable candidate IDs and remain **Pending Human Adjudication**. The remaining matched relationships reconciled, were intentionally different analysis sets/windows, or had no populated cross-document comparator.

## Candidate consistency issues

### 1. Primary-outcome time-origin label differs between the article and SAP

**Primary category:** Cross-document numeric inconsistency; Measure, label, or scale inconsistency.

**Matched relationship:** Primary binary GI-3 recovery, IV lidocaine versus placebo, primary analysis population, 72-hour window, adjusted relative-risk analysis.

**Exact printed evidence:**

- Main article abstract: “return of gut function at **72 hours after surgery**,” with GI-3 defined as diet tolerance for three consecutive meals and passage of flatus or stool; it reports 160/279 (57.3%) versus 164/278 (59.0%), adjusted difference −1.9% (95% CI, −8.0% to 4.2%), RR 0.97 (95% CI, 0.88 to 1.07). [DOC-001 p. 1](jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=1)
- Main article Results and Table 2 label the same result as GI-3 “at **72 hours after operation**” / “by 72 h after operation,” with 160 (57.3%) versus 164 (59.0%) and RR 0.97 (0.88 to 1.07). [DOC-001 p. 5](jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=5); [DOC-001 p. 6](jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6)
- SAP definition: GI-3 is the same binary composite “at **72 hours after the start of operation**.” [DOC-003 p. 9](joi240139supp2_prod_1741633738.17362.pdf#page=9)

**Comparison logic:** “After the start of operation” specifies a clock origin. “After surgery” and “after operation,” as printed in the article, do not say that the clock begins at operation start and can be read as an interval following completion of surgery. The numerical result is otherwise exactly matched; the candidate is the unmatched time-origin label for that result, not a numerical disagreement.

**Supported alternatives:** The article’s shorter wording may use “after surgery/operation” as a conventional shorthand for the SAP’s start-of-operation clock. Conversely, it may describe a different clock origin. The supplied package does not contain the analysis dataset or timestamp derivation needed to distinguish these alternatives.

**Human verification steps:**

1. Inspect the final case-report-form/data dictionary and analysis derivation for the GI-3 72-hour cutoff.
2. Confirm whether the cutoff was calculated from incision/operation start, start of anaesthesia, operation completion, or another recorded time.
3. If it was operation start, decide whether each article occurrence should state that origin; if not, confirm whether the SAP definition or article label is the applicable one.

### 2. Postoperative opioid-consumption window is 24 hours in the article and 72 hours in the protocol/SAP

**Primary category:** Cross-document numeric inconsistency; Measure, label, or scale inconsistency.

**Matched relationship:** Postoperative morphine-equivalent opioid consumption, IV lidocaine versus placebo, postoperative analgesia quantity, reported as a secondary outcome.

**Exact printed evidence:**

- Main article outcome definition calls the secondary outcome “postoperative opioid consumption (**up to 24 hours**).” [DOC-001 p. 4](jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4)
- Main article Table 2 reports “postoperative oral morphine equivalent analgesia **up to 24 h**,” 70.6 mg (IQR, 30.0-150.0; n=210) for lidocaine and 45.0 mg (IQR, 17.1-98.6; n=210) for placebo. [DOC-001 p. 6](jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=6)
- Protocol definition: total postoperative opioid consumption is morphine-equivalent dose, “cumulative total until **72 hours after start of operation**.” [DOC-002 p. 17](joi240139supp1_prod_1741633738.16362.pdf#page=17)
- SAP assessment schedule likewise specifies “Total opioid consumption in-hospital up to **72 hours**.” [DOC-003 p. 11](joi240139supp2_prod_1741633738.17362.pdf#page=11)

**Comparison logic:** The measure and units match, but the printed endpoint window differs by 48 hours. A 24-hour cumulative amount cannot be assumed numerically interchangeable with a 72-hour cumulative amount. No 72-hour observed opioid total is printed in the main article, so this is a time-window/measure-label inconsistency rather than a recalculation of the displayed medians.

**Supported alternatives:** The final analysis may have intentionally changed the secondary-outcome window from 72 to 24 hours; alternatively, 72-hour data may have been collected but the article reported a distinct 24-hour endpoint. The supplied sources do not provide an amendment, final outcome-definition table, or source data that resolves which interpretation applies.

**Human verification steps:**

1. Locate the final approved outcome-definition/amendment record and statistical output for opioid consumption.
2. Confirm the time window used to generate the displayed 70.6-mg and 45.0-mg medians.
3. Confirm whether 72-hour opioid totals were analysed and, if so, whether their omission or a 24-hour relabeling was intended.

### 3. Unplanned-readmission ascertainment window is 90 days in Table 3 but 30 days in the article methods, protocol, and SAP layout

**Primary category:** Cross-document numeric inconsistency; Measure, label, or scale inconsistency.

**Matched relationship:** Unplanned readmission after the operation, participant count/proportion, IV lidocaine versus placebo, tertiary/safety outcome.

**Exact printed evidence:**

- Main article Methods defines the tertiary outcome as “unplanned readmission within **30 days** of surgery.” [DOC-001 p. 4](jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=4)
- Main article Table 3 instead labels the displayed result “Unplanned readmission after discharge and within **90 d of operation**”: 31/279 (11.1%) for lidocaine and 34/278 (12.2%) for placebo. [DOC-001 p. 8](jama_paterson_2024_oi_240139_1741633738.12862.pdf#page=8)
- Protocol definition: “Unplanned re-admissions within **30 days** of date of operation,” measured as number of patients readmitted, with a 30-day specific time point. [DOC-002 p. 18](joi240139supp1_prod_1741633738.16362.pdf#page=18)
- SAP dummy-table heading specifies “unplanned re-admissions within **30 days** of date of operation.” [DOC-003 p. 27](joi240139supp2_prod_1741633738.17362.pdf#page=27)

**Comparison logic:** These are the same population, contrast, count/proportion scale, and readmission concept, but the article supplies two incompatible time windows: 30 days in Methods and 90 days in Table 3. The protocol and SAP independently support the 30-day definition. Counts for a 90-day window cannot be interpreted as the planned 30-day endpoint without an explicit change or relabeling explanation.

**Supported alternatives:** Table 3 may correctly report a post-protocol 90-day outcome, with the Methods text and planning documents unrevised. Alternatively, the 31 and 34 counts may be 30-day counts whose Table 3 label is incorrect. The supplied package has no patient-level readmission dates or final amendment that selects between these alternatives.

**Human verification steps:**

1. Check the final analysis dataset/output and the statistical-analysis amendment history for the readmission endpoint and cutoff date.
2. Reproduce the 31 and 34 participant counts under both 30- and 90-day windows.
3. Align the Methods, Table 3 label, and any final protocol/SAP amendment to the confirmed analysis window.

### 4. ERAS-adherence subgroup cut points do not align with the protocol’s stated compliance bands

**Primary category:** Measure, label, or scale inconsistency; Cross-document numeric inconsistency.

**Matched relationship:** Enhanced Recovery After Surgery (ERAS) protocol-compliance subgroup for the primary GI-3 outcome, subgroup category scale, and interaction analysis.

**Exact printed evidence:**

- Protocol: ERAS compliance is measured from listed care variables and is graded as “0-30% compliant; 30-60% compliant; >60% compliant.” [DOC-002 pp. 17-18](joi240139supp1_prod_1741633738.16362.pdf#page=17)
- SAP names the primary-outcome subgroup as “ERAS protocol compliance (High, moderate, low)” and gives 99% CIs for exploratory subgroup analyses, but does not print numerical cut points. [DOC-003 p. 15](joi240139supp2_prod_1741633738.17362.pdf#page=15)
- Results-supplement eFigure presents “enhanced recovery protocol adherence” subgroups and defines high as at least 7 of 10 criteria and low as fewer than 5 of 10 criteria; it reports high n=191, moderate n=274, and low n=92 with their subgroup RRs. [DOC-004 p. 2](joi240139supp3_prod_1741633738.18862.pdf#page=2)

**Comparison logic:** For a 10-criterion score, the protocol’s stated 0-30%, 30-60%, and >60% bands place scores 0-3, 3-6, and 7-10 in the respective bands, subject to treatment of the shared 30% boundary. The eFigure’s “low <5” places a score of 4/10 (40%) in low, whereas 40% is within the protocol’s stated 30-60% band. The eFigure does not print the moderate definition, so its three displayed RRs cannot be unambiguously connected to the protocol’s graded compliance scale.

**Supported alternatives:** The protocol’s “e.g.” before its bands may denote an illustrative, rather than final, categorization; the final 10-criterion algorithm may deliberately define low as 0-4, moderate as 5-6, and high as 7-10. Alternatively, the protocol bands may be the applicable definition and the eFigure’s low threshold may be mislabeled. No final data dictionary or derivation is supplied to resolve this.

**Human verification steps:**

1. Obtain the final ERAS variable list, denominator rule, and categorization code used for the eFigure.
2. Tabulate the number of criteria met for all 557 primary-analysis participants and reproduce n=191, 274, and 92 under the eFigure thresholds and the protocol bands.
3. Confirm the intended definition for “moderate,” the allocation of a 4/10 score, and whether the protocol wording was superseded.

## Completed matched-result coverage with no candidate

| Match group and mapped relationships | Locations checked | Comparison result |
|---|---|---|
| Trial population, 1:1 contrast, dose, minimisation variables, post-randomisation exclusions, and primary/per-protocol/safety analysis sets (N001-N005, N011-N013, N045; N-SUP-012) | DOC-001 pp. 1, 3-5; DOC-002 pp. 19-29; DOC-003 pp. 7-10, 13-17 | No unmatched printed value after distinguishing randomised, primary, per-protocol, and safety sets. |
| GI-3 composition, primary counts/percentages, adjusted difference/RR/CI, P value, and abstract/narrative/Table 2/eFigure overall result (N003, N007-N010, N020, N037; S001-S005, S012; N-SUP-001) | DOC-001 pp. 1, 4-6; DOC-004 p. 2; DOC-002 pp. 15-18; DOC-003 pp. 9, 14, 20, 34 | The printed primary values reconcile at displayed precision. The time-origin label difference is recorded separately as issue 1. |
| Power and sample-size quantities (N019; N-SUP-013) | DOC-001 p. 5; DOC-002 pp. 19-20, 40; DOC-003 pp. 13-15 | 60% to 73.2% GI-3 is the complement of 40% to 26.8% non-return; both give the printed 13.2-point difference and N=562. |
| GI-2/GI-3 time-to-event and PPOI definitions/labels (N003, N020-N021; N-SUP-002-003) | DOC-001 pp. 4, 6; DOC-002 pp. 15-18; DOC-003 pp. 9-10, 20-21, 34-35 | Definitions, event direction, analysis labels, and 120-hour PPOI window reconcile. |
| PONV, OBAS, QoR-15, EQ-5D-5L, and their scale/collection/model definitions (N021-N025; S006-S009; N-SUP-004-008) | DOC-001 pp. 4, 6; DOC-002 pp. 15-18, 31-37, 60-61; DOC-003 pp. 10-12, 19, 21-25, 32, 35-36 | No matched-result value or scale contradiction. The sources provide planned definitions but no populated support result tables. |
| Intraoperative opioid quantities and postoperative opioid endpoint (N023; N-SUP-006) | DOC-001 pp. 4, 6-7; DOC-002 pp. 17, 33-36; DOC-003 pp. 11, 19, 24 | Units and OME label are consistent; the postoperative time-window conflict is recorded separately as issue 2. |
| Enhanced-recovery process measures and fluid/catheter/mobilisation timing (N026-N027, N043; N-SUP-009) | DOC-001 p. 7; DOC-002 pp. 17-18, 31-37; DOC-003 pp. 14-15, 26, 36; DOC-004 p. 2 | Individual process-measure labels and timing reconcile. The subgroup-category scale conflict is recorded separately as issue 4. |
| Medical and patient discharge readiness definitions, time scale, and HRs (N028; S010; N-SUP-010) | DOC-001 p. 7; DOC-002 p. 18; DOC-003 pp. 26, 36 | No conflict after matching distinct clinician-assessed and patient-assessed endpoints. |
| Total length of stay, mortality, serious/adverse events, and major complications (N033-N036; S011; N-SUP-011, N-SUP-018) | DOC-001 pp. 4, 8-9; DOC-002 pp. 18-19, 30-37, 43-48; DOC-003 pp. 10-13, 27-29, 36 | Length-of-stay definition/30-day window, mortality windows, safety counting units, and complication definition reconcile. The readmission-window conflict is recorded separately as issue 3. |
| Subgroup contrast, subgroup N totals, interaction P values, 99% CIs, and infusion/operation/sex/age categories (N006, N038-N042; S013-S017; S-SUP-015) | DOC-001 pp. 4-5, 7, 9; DOC-004 p. 2; DOC-002 pp. 40-42; DOC-003 pp. 14-15, 37-38 | No other mismatched subgroup result was found. ERAS categorization is recorded separately as issue 4. |
| Figure 1 flow, Figure 2 at-risk/event display, abstract/narrative/conclusion summaries, and contextual literature figures (N010-N014, N030-N032, N044-N046) | DOC-001 pp. 1-3, 5, 8-10 | No matched cross-document comparator gives a qualifying quantitative conflict. Figure 2’s at-risk and event values are correctly distinguished from cumulative event counts. |
| Protocol/SAP templates, schedule, dummy tables, projected recruitment graphics, formula appendices, and DOC-005 data-sharing statement (N-SUP-016-019) | DOC-002 pp. 36-37, 49-52, 59-66; DOC-003 pp. 17-30, 31-40; DOC-005 p. 1 | No populated result values were available to match. Blank template fields and projections were not treated as result values. |

## Counts and limitations

- Direct-source scope completed: DOC-001 10/10 pages, DOC-002 66/66 pages, DOC-003 40/40 pages, DOC-004 2/2 pages, and DOC-005 1/1 page; 119/119 total units are mapped in `source_coverage.md`.
- Matched relationship groups completed: 12. Qualifying distinct candidates: 4. No candidate IDs or AI adjudications were assigned.
- Limitations: DOC-002 and DOC-003 are planning documents and supply definitions, planned output structures, and code, not populated final result tables. The package contains no patient-level data, final outcome-derivation dataset, amendment log resolving all endpoint changes, or structured-data file. These limitations prevent choosing among the supported alternatives but do not prevent identifying the printed cross-source differences above.
