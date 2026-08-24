# Cross-Source Consistency Review

## Scope, evidence boundary, and method

This checker reviewed the complete fresh direct-source evidence set: DOC-001 (`jama_wang_2018_oi_180070.pdf`, pp. 1-10), DOC-002 (`joi180070supp1_prod.pdf`, pp. 1-25), and DOC-003 (`joi180070supp2_prod.pdf`, pp. 1-9). It used only the current native-text and coordinate-layout assets, current main/support extraction records, canonical relationship inventories, and the supplied PDFs. No legacy audit derivative or external source was used.

For every possible match, the comparison first required the same population, time point, contrast, model/analysis set, measure, scale/unit, reference condition, and displayed precision. Planned quantities were not treated as observed results, and sensitivity-analysis denominators were not compared as though they were primary-analysis denominators. A displayed small P value was not treated as a candidate solely by its formatting; no mapped display-zero P value occurred.

## Complete relationship coverage

### Numeric/reporting inventory

| Source/relationship scope | Cross-source matching completed | Result |
|---|---|---|
| DOC-001 abstract, Key Points, narrative, Figure 1, Tables 1-3, captions, and footnotes: N001, N002, N003, N004, N005, N006, N007, N008, N009, N010, N011, N012, N013, N014, N015, N016, N017, N018, N019, N020, N021, N022, N023, N024, N025, N026, N027, N028, N029, N030 | Matched repeated enrolment, allocation, follow-up, co-primary, event, disability, death, performance-measure, and baseline displays to their eligible abstract/narrative/table/figure/support occurrences after denominator and precision matching. | COMPLETE; qualifying observations XC001-XC003 below. |
| DOC-002 protocol: N031, N032, N033, N034, N035, N036, N037, N038, N039, N040, N041, N042, N043, N044, N045, N046, N047, N048 | Matched trial design, eligibility, intervention timing, measure definitions, composite/all-or-none definitions, planned sample-size quantities, analysis plan, and sensitivity-analysis definition to corresponding DOC-001/DOC-003 occurrences. | COMPLETE; qualifying observations XC001-XC003 below. |
| DOC-003 eAppendix/eTables: N049, N050, N051, N052, N053, N054, N055, N056, N057, N058, N059, N060, N061 | Matched baseline survey, eTable definitions, mRS-availability table, individual vascular-event tables, and sensitivity-analysis displays to their same-population/time/analysis-set occurrences. | COMPLETE; qualifying observations XC001-XC003 below. |

### Inferential/statistical inventory

| Relationship IDs reviewed for cross-document identity | Result |
|---|---|
| S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, S025, S026, S027 | COMPLETE. Abstract, narrative, Table 2/Table 3, Figure 2, and sensitivity-analysis occurrences were matched only within their stated model and analysis set. No additional cross-document numeric mismatch was identified in this lane. |
| S028, S029, S030, S031, S032, S033, S034, S035, S036, S037, S038, S039, S040, S041, S042, S043, S044, S045, S046, S047, S048, S049, S050, S051, S052, S053, S054, S055, S056, S057, S058, S059, S060, S061, S062, S063, S064, S065, S066, S067 | COMPLETE. Protocol analysis definitions and support eTable estimates were matched to the corresponding main-source definitions/results where population, time, and denominator agreed. No additional cross-document numeric mismatch was identified in this lane. |

## Provisional cross-source candidates

The `XC` identifiers are provisional discovery identifiers only. They are not stable candidate IDs and convey no adjudication, severity, or disposition.

## XC001 — LDL eligibility threshold differs between the reported performance-measure row and protocol/eTable definition

**Category:** Measure, label, or scale inconsistency.

**Exact linked locations:** [DOC-001, PDF p. 3](../../../jama_wang_2018_oi_180070.pdf#page=3), Outcomes definition; [DOC-001, PDF p. 7](../../../jama_wang_2018_oi_180070.pdf#page=7), Table 2 lipid-lowering row; [DOC-002, PDF p. 14](../../../joi180070supp1_prod.pdf#page=14), Table 2/3 discharge measure; [DOC-002, PDF p. 15](../../../joi180070supp1_prod.pdf#page=15), Table 3 definition; [DOC-003, PDF p. 3](../../../joi180070supp2_prod.pdf#page=3), eTable 1 definition.

**Direct observation:** DOC-001 describes the discharge performance measure as lipid-lowering treatment for LDL **more than 100 mg/dL** (also printed in Table 2 as “LDL >100 mg/dL”; 1,415/1,481 and 1,439/1,547). DOC-002 Table 2 says statin treatment for LDL **≥100 mg/dL**; DOC-002 Table 3 and DOC-003 eTable 1 likewise specify lipid-lowering treatment if LDL **≥100 mg/dL**, with additional stated eligibility conditions (prior lipid-lowering treatment or undocumented LDL).

**Comparison logic:** The displayed comparator is the same discharge performance measure, in the same acute-ischemic-stroke trial population. `>100 mg/dL` excludes a patient whose LDL is exactly 100 mg/dL, whereas `≥100 mg/dL` includes that patient. The two rules therefore define different eligibility sets at the threshold; the main Table 2 row omits the supplied supplement’s additional “or not documented/prior treatment” wording as well.

**Supported alternatives:** The main article may abbreviate the full specification, or the `>100` symbol may be a reporting-label simplification rather than the rule used to derive the shown denominators. The supplied documents do not state which threshold was used to construct the Table 2 denominators.

**Human verification steps:** Open the cited PDF pages, confirm the comparator symbols and the full eTable/protocol definition, then inspect the analysis dataset/codebook or prespecified measure form to determine whether LDL exactly 100 mg/dL, undocumented LDL, and prior lipid-lowering treatment were eligible in the reported Table 2 row.

## XC002 — Composite adherence is described as a patient-averaged quantity in the article but as care-opportunity-level analysis in the protocol and eAppendix

**Category:** Measure, label, or scale inconsistency.

**Exact linked locations:** [DOC-001, PDF p. 3](../../../jama_wang_2018_oi_180070.pdf#page=3), Outcomes—composite definition; [DOC-001, PDF p. 7](../../../jama_wang_2018_oi_180070.pdf#page=7), Table 2 composite row; [DOC-002, PDF p. 18](../../../joi180070supp1_prod.pdf#page=18) and [DOC-002, PDF p. 19](../../../joi180070supp1_prod.pdf#page=19), Statistical analysis plan; [DOC-003, PDF p. 2](../../../joi180070supp2_prod.pdf#page=2), eAppendix baseline-survey endpoint definition.

**Direct observation:** DOC-001 states that the composite measure is the total eligible measures performed divided by the total eligible measures for **a given patient**, and that it “was calculated for each patient and then averaged.” Table 2 reports the corresponding composite means as 88.2 (SD 15.1) versus 84.8 (SD 18.2). DOC-002 instead states that, for composite analysis, **each care opportunity contributed an observation**, coded 1 for met and 0 for not met; its 5-of-7 example contributes five observations. DOC-003 says its prerandomization survey used the “same endpoint definition” as the randomized phase, then defines the composite as total interventions performed among eligible patients divided by total possible interventions among eligible patients.

**Comparison logic:** A mean of per-patient percentages gives each patient equal weight. A pooled care-opportunity proportion gives patients with more eligible measures more weight. These are distinct analysis units and can yield different percentages, differences, and models even with the same underlying care events. The sources present both as the composite endpoint for the trial/randomized phase rather than labelling one as a separate estimand.

**Supported alternatives:** The prose may describe a descriptive patient-level composite while the GEE/OR analysis uses care opportunities, or the sources may use “composite” for related but intentionally distinct descriptive and inferential summaries. The supplied sources do not explicitly reconcile the unit used for the printed Table 2 mean/difference with the unit used in the care-opportunity analysis.

**Human verification steps:** Verify the cited wording in the direct PDFs; then obtain the statistical analysis specification or analysis code that generated the Table 2 composite mean, absolute difference, and ORPA. Establish whether the reported 88.2% and 84.8% are means of patient-level proportions, pooled opportunity proportions, or different summaries reported under one endpoint label.

## XC003 — DVT-prophylaxis timing is printed as “within 48 hours” in the protocol table but “by end of hospital day 2” in the specifications and reported-table footnote

**Category:** Measure, label, or scale inconsistency.

**Exact linked locations:** [DOC-002, PDF p. 13](../../../joi180070supp1_prod.pdf#page=13), protocol Table 2; [DOC-002, PDF p. 14](../../../joi180070supp1_prod.pdf#page=14) and [DOC-002, PDF p. 15](../../../joi180070supp1_prod.pdf#page=15), protocol Table 3 specification; [DOC-003, PDF p. 3](../../../joi180070supp2_prod.pdf#page=3), eTable 1 specification; [DOC-001, PDF p. 7](../../../jama_wang_2018_oi_180070.pdf#page=7), Table 2 DVT-prophylaxis row/footnote.

**Direct observation:** DOC-002 protocol Table 2 calls the acute DVT measure “DVT prophylaxis **within 48 hours of admission** in patients at risk.” The same protocol’s Table 3 says nonambulatory patients received DVT prophylaxis **by end of hospital day two**. DOC-003 eTable 1 and DOC-001 Table 2 footnote use the latter “by end of hospital day 2” wording for the displayed 178/645 (27.6%) versus 66/592 (11.1%) result.

**Comparison logic:** “Within 48 hours of admission” is an elapsed-time rule; “by end of hospital day 2” is a calendar-day boundary unless a study convention equates it to 48 hours. The stated windows can include different patients/events for admissions late in a day. They are presented as the same DVT performance measure.

**Supported alternatives:** The protocol may have defined hospital day two operationally as 48 hours after admission, or its Table 2 may have used informal shorthand. The direct sources provide no operational definition that makes the two boundaries demonstrably identical.

**Human verification steps:** Confirm the labels in the cited PDFs and inspect the protocol’s case-report-form/time-stamp rules or data dictionary. Determine whether hospital day two was operationalized as 48 elapsed hours, midnight-based calendar days, or another convention, and which rule produced the reported DVT denominators and percentages.

## Matched observations not emitted as provisional candidates

- Main and support planned sample-size descriptions both state approximately/precisely 4,800 patients across 40 clusters at a median 120 patients per cluster. The protocol’s three 30-patient monitoring cycles describe a feedback-cycle cadence, not an explicitly stated alternative total enrollment target; it was therefore not compared as a conflicting observed count.
- The reported primary Table 2 denominators and eTable 4 sensitivity denominators differ where the supplement explicitly defines the sensitivity analysis as including contraindicated patients in the overall-population denominator. They were not treated as competing analysis sets.
- The 3,980 completed 12-month follow-ups and the 3,949 patients with one-year mRS data describe different outcome-availability variables; the eTable explicitly partitions all 4,800 patients into mRS available/lost groups. No same-variable contradiction was identified.
- The individual-event totals in eTable 3 are not required to equal the number of patients with any new vascular event because DOC-003 explicitly states that a patient may have different new vascular events.
- DOC-001’s “18 years or older” and DOC-002’s “Older than 18” differ at the age-18 boundary, but the supplied package contains no reported count, denominator, or result that identifies an enrolled 18-year-old or connects that boundary to a displayed quantitative result. This was documented as an unmatched eligibility-definition ambiguity, not emitted as a candidate under the fixed scope.

## Limitations

Fresh native and coordinate-layout extraction was readable for all assigned result-relevant text. DOC-002 figures 1-4 had unavailable internal visual-only material in the fresh assets, but their captions and associated narrative/definitions were checked; no printed result comparator was omitted from the source mappings. This review does not replace source-image confirmation of the cited symbols or access to the analysis dataset, case-report form, or code needed to resolve the three provisional observations.
