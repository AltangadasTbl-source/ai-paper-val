# Final Evidence-Quality Audit

## Audit status

- **Status:** COMPLETE.
- **Stable candidate set:** C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, C011.
- **Stable candidates audited:** 11 of 11.
- **Direct-source coverage audited:** 3 of 3 sources and 39 of 39 PDF pages.
- **Relationship coverage audited:** 38 of 38 numeric relationships and 25 of 25 statistical relationships.
- **Statistical passes audited:** pass 1 and pass 2 each contain an explicit completion record for S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, and S025.
- **Disposition boundary:** Every stable candidate remains Pending Human Adjudication. This audit supplies evidence-quality checks and bounded repair instructions only.

The current-run artifacts document uncapped discovery from complete source and relationship assignments. They do not use a legacy candidate set, review queue, desired count, or top-N boundary as a discovery scope. The reusable coverage and fresh-required coverage partition all 39 source pages, and the mapped-unit count closes every direct-source row. The two source-grounded omissions identified during the initial audit were appended without renumbering as C010 and C011, preserved in the numeric inventory and checker provenance, and mechanically rechecked against the direct PDFs. The ledger, recheck, and quality ID sets are now identical at 11 IDs.

## C001 — Protocol matching direction conflicts with the final matched cohort

- **Status:** Pending Human Adjudication.
- **Evidence-card fields:** The current ledger and recheck supply exact locations, both printed statements, the identity rule, reproduced arithmetic, necessary missing inputs, a conditional alternative, separation of observation from explanation, and an exact human question. No material candidate-specific evidence field is missing.
- **Direct support and pagination:** Main article PDF pp. 1, 3, and 4 and protocol PDF p. 3 were found at the cited package-relative links. All cited page numbers are within the direct PDFs and the links resolve to the named files.
- **Reproduced calculation:** `2,287 × 5 = 11,435`. The reported cohort therefore contains five nonsurgical controls per surgical patient, while the protocol sentence grammatically states five surgical patients per nonsurgical patient.
- **Assumptions and alternatives:** The record does not assume which wording reflects the implemented code. Drafting inversion and an unstated ratio convention remain clearly conditional alternatives; the missing matching code and version history are named.
- **Duplicate assessment:** NUM-P001 and CROSS-P001 concern the same statements, comparator, and direction rule and are correctly preserved as provenance for one stable record. No other stable candidate duplicates this relationship.
- **Impact wording:** The record does not claim that any effect estimate or paper-level conclusion changes. Any final downstream statement must be limited to possible copying of the matching direction into a methods extraction if the candidate is confirmed.
- **Required repair:** None specific to this record.

## C002 — Heart-failure ARD does not reconcile with displayed 8-year incidences

- **Status:** Pending Human Adjudication.
- **Evidence-card fields:** The printed incidences, printed ARD, contrast direction, arithmetic rule, rounding analysis, missing unrounded inputs, alternative point-estimator interpretation, and exact human question are present.
- **Direct support and pagination:** Main article PDF p. 7 and Supplement 1 PDF p. 7 contain the cited values. Main article PDF p. 4 contains the calculation and bootstrap-interval method cited by the recheck.
- **Reproduced calculation:** `18.9% - 6.8% = 12.1%`, not the printed 12.9%; the discrepancy is 0.8 percentage point. The possible difference from independently rounded one-decimal incidence inputs is at most approximately 0.10 percentage point, so displayed rounding does not reconcile the values.
- **Assumptions and alternatives:** A separately generated ARD point estimate is a conditional explanation, not a supplied fact. The source expressly describes percentile bootstrap generation for the interval but does not define a distinct ARD point estimator.
- **Duplicate assessment:** This record is not a duplicate of C003, C004, C005, or C006 because it concerns a different outcome row and different printed values, although the consistency rule is shared.
- **Impact wording:** The record supports only the bounded possibility that an extractor could copy either the ARD or the displayed incidence difference if the candidate is confirmed. It does not support a conclusion-impact claim.
- **Required repair:** Completed. Main article PDF p. 4 is now included in the ledger's exact source locations. No further record-specific repair remains.

## C003 — Coronary-disease ARD does not reconcile with displayed 8-year incidences

- **Status:** Pending Human Adjudication.
- **Evidence-card fields:** The compared values, contrast, arithmetic, rounding bound, missing inputs, conditional alternative, and exact human question are present.
- **Direct support and pagination:** Main article PDF p. 7 and Supplement 1 PDF p. 7 contain the reported values; main article PDF p. 4 contains the method statement used for the alternative interpretation.
- **Reproduced calculation:** `11.6% - 7.9% = 3.7%`, not 4.2%; the discrepancy is 0.5 percentage point and is not explained by two independently rounded one-decimal inputs.
- **Assumptions and alternatives:** A separate estimator remains possible but is not defined in the supplied package. It must remain an unresolved alternative rather than an asserted explanation.
- **Duplicate assessment:** The relationship is outcome-specific and distinct from the other ARD records.
- **Impact wording:** Any final downstream statement must be limited to possible extraction of the coronary-disease absolute effect if the candidate is confirmed. No paper-level conclusion claim is supported.
- **Required repair:** Completed. Main article PDF p. 4 is now included in the ledger's exact source locations. No further record-specific repair remains.

## C004 — Cerebrovascular-disease ARD does not reconcile with displayed 8-year incidences

- **Status:** Pending Human Adjudication.
- **Evidence-card fields:** The source values, comparator, calculation, rounding bound, missing inputs, alternative, and exact human question are present.
- **Direct support and pagination:** Main article PDF p. 7 and Supplement 1 PDF p. 7 contain the reported values; main article PDF p. 4 contains the relevant calculation and bootstrap-interval description.
- **Reproduced calculation:** `5.6% - 4.1% = 1.5%`, not 1.8%; the discrepancy is 0.3 percentage point, beyond the approximate 0.10-point displayed-rounding bound.
- **Assumptions and alternatives:** The negative lower confidence endpoint is an interval value and does not establish the point-estimation rule. A distinct point estimator is possible but is not supplied.
- **Duplicate assessment:** The different endpoint and values make this a distinct relationship, not a duplicate of another ARD candidate.
- **Impact wording:** The supported downstream statement is limited to potential copying of the displayed cerebrovascular absolute effect if confirmed. No broader effect is established.
- **Required repair:** Completed. Main article PDF p. 4 is now included in the ledger's exact source locations. No further record-specific repair remains.

## C005 — Nephropathy ARD does not reconcile with displayed 8-year incidences

- **Status:** Pending Human Adjudication.
- **Evidence-card fields:** The record contains the exact values, direction, arithmetic, rounding analysis, missing inputs, conditional alternative, observation-versus-inference distinction, and exact human question.
- **Direct support and pagination:** Main article PDF p. 7 and Supplement 1 PDF p. 7 contain the reported values; main article PDF p. 4 contains the cited method context.
- **Reproduced calculation:** `16.3% - 6.1% = 10.2%`, not 11.1%; the discrepancy is 0.9 percentage point and exceeds the rounding bound.
- **Assumptions and alternatives:** A separate point estimate is not ruled out, but neither its formula nor its unrounded inputs are provided. The record correctly treats this as an unresolved alternative.
- **Duplicate assessment:** The endpoint and printed values are distinct from all other stable relationships.
- **Impact wording:** A final card may identify only the possible copying of the nephropathy ARD or displayed incidence difference if confirmed; it must not infer conclusion change.
- **Required repair:** Completed. Main article PDF p. 4 is now included in the ledger's exact source locations. No further record-specific repair remains.

## C006 — Atrial-fibrillation ARD does not reconcile with displayed 8-year incidences

- **Status:** Pending Human Adjudication.
- **Evidence-card fields:** Exact values, comparator, rule, arithmetic, rounding bound, missing estimator inputs, alternative, and human question are present.
- **Direct support and pagination:** Main article PDF p. 7 and Supplement 1 PDF p. 7 contain the reported values; main article PDF p. 4 contains the method context.
- **Reproduced calculation:** `13.6% - 7.9% = 5.7%`, not 6.5%; the discrepancy is 0.8 percentage point, beyond ordinary displayed rounding.
- **Assumptions and alternatives:** The supplied source does not define a separate ARD point estimator. That possibility must remain conditional.
- **Duplicate assessment:** This is an endpoint-specific printed relationship and is not duplicative of the other ARD records.
- **Impact wording:** The only supported downstream statement concerns possible extraction of the atrial-fibrillation absolute effect if confirmed. No conclusion-impact claim is supported.
- **Required repair:** Completed. Main article PDF p. 4 is now included in the ledger's exact source locations. No further record-specific repair remains.

## C007 — Supplement tables use different nonsurgical medication denominators at baseline

- **Status:** Pending Human Adjudication.
- **Evidence-card fields:** Both denominators, their table/time labels, the integer comparison, the missing inclusion or availability rule, a complete-case alternative, and the exact human question are present.
- **Direct support and pagination:** Supplement 1 PDF p. 5 prints matched nonsurgical `N=11435` for index-date medication classes; Supplement 1 PDF p. 14 prints a nonsurgical year-0 medication-proportion sample size of `11433`. Both links resolve and the pages are truthful.
- **Reproduced calculation:** `11,435 - 11,433 = 2` participants. The supplied pages do not print a missingness, timing, or inclusion rule that accounts for the difference.
- **Assumptions and alternatives:** The record does not assert that the analysis sets must be identical. A complete-case or availability rule is retained as an unresolved source-grounded possibility.
- **Duplicate assessment:** This is the single N029 denominator relationship and does not duplicate a statistical-test or medication-percentage relationship.
- **Impact wording:** Any downstream statement must be limited to possible denominator selection by an extractor if the candidate is confirmed.
- **Required repair:** None specific to this record.

## C008 — Medication comparison is labeled with two different procedure names

- **Status:** Pending Human Adjudication.
- **Evidence-card fields:** The matched time, outcomes, P-value family, both procedure labels, identity rule, unavailable contingency cells and software settings, alternative label interpretations, and exact human question are present.
- **Direct support and pagination:** Main article PDF p. 4 names a two-sample proportions test, main article PDF p. 10 names Fisher exact tests for the six year-8 comparisons, and Supplement 1 PDF p. 12 repeats the year-8 P-value family and the two-sample-proportions label. Supplement 1 PDF p. 14 contains only the overall year-8 availability denominators used in the recheck limitation.
- **Reproduced comparison:** Five matched categories display `P<.001` and insulin displays `P=.008` in both the figure and eTable 8, while the attached procedure names differ. The supplied aggregate displays do not permit either test to be rerun.
- **Assumptions and alternatives:** The record must remain a procedure-label ambiguity. It must not assert that different computations were necessarily performed because “two-sample proportions test” may have been used generically or Fisher testing may have been the specific year-8 implementation.
- **Duplicate assessment:** S013 and S025 track overlapping aspects of the same six year-8 comparisons and are properly cross-referenced in one stable record.
- **Impact wording:** The supported downstream risk is limited to copying a test-method label if the candidate is confirmed; no numerical effect or conclusion change is established.
- **Required repair:** If the final card mentions the overall year-8 denominators, cite Supplement 1 PDF p. 14. Keep the candidate statement focused on conflicting printed labels, not an unproven difference in calculations.

## C009 — Time-varying-HR narrative names eTable 4 while the matching display is eTable 7

- **Status:** Pending Human Adjudication.
- **Evidence-card fields:** The narrative label, adjacent and repeated table labels, actual eTable 4 content, content-identity rule, version-history alternative, and exact human question are present.
- **Direct support and pagination:** Supplement 1 PDF p. 19 prints the narrative reference to eTable 4 immediately above eTable 7; PDF p. 10 contains the identical eTable 7; PDF p. 6 contains actual eTable 4 with event rates rather than time-varying HRs. All three links resolve and the page labels are truthful.
- **Reproduced comparison:** The narrative's measure and time points match eTable 7 at years 2, 5, and 8, while actual eTable 4 reports rates per 100 patient-years. This is a label-and-content identity comparison, not an arithmetic calculation.
- **Assumptions and alternatives:** Earlier numbering remains possible because no version history is supplied. The current package does not establish which wording the authors would choose as a correction.
- **Duplicate assessment:** NUM-P008, CROSS-P003, and STAT1-P001 concern the same narrative, table labels, and identity rule and are correctly preserved as provenance for one stable record.
- **Impact wording:** A bounded downstream statement may say that a reader or extractor could follow the cited table number to a different measure if the candidate is confirmed. It must not claim an effect-estimate or paper-level conclusion change.
- **Required repair:** Completed. The ledger and recheck headings now state the printed eTable 4/eTable 7 contrast neutrally and do not prescribe a correction.

## C010 — Biguanide count and percentage do not reconcile in eTable 3

- **Status:** Pending Human Adjudication.
- **Evidence-card fields:** The ledger and recheck provide the printed numerator, printed denominator, printed percentage, exact arithmetic rule, reproduced calculation, display precision, missing patient-level inputs, an alternate-denominator possibility, separation of observation from explanation, and an exact human question. No material candidate-specific evidence field is missing.
- **Direct support and pagination:** Supplement 1 PDF p. 5 contains eTable 3, the metabolic-surgery column denominator `N=2287`, and the biguanide entry `1530 (67.9%)`. The package-relative link resolves to the direct PDF and the cited page is truthful.
- **Reproduced calculation:** `1,530 / 2,287 × 100 = 66.8999...%`, which rounds to 66.9% at one decimal rather than the printed 67.9%. The discrepancy is 1.0 percentage point. Conversely, 67.9% of 2,287 is approximately 1,552.6, not 1,530.
- **Assumptions and alternatives:** The record does not select the count, percentage, or denominator as the source of the mismatch. A different unprinted row denominator is retained only as an unresolved possibility; the cited table supplies no such denominator.
- **Duplicate assessment:** C010 concerns the internal arithmetic of one surgery-group count-and-percentage entry. It is distinct from C007, which compares two nonsurgical denominators across separate tables, and from C008, which concerns test-procedure labels.
- **Impact wording:** A bounded downstream statement may identify possible copying of the biguanide count or percentage by a data extractor if the candidate is confirmed. No broader effect or paper-level conclusion change is established.
- **Required repair:** Completed. N022 now names the printed relationship, the numeric checker preserves AUDIT-OMISSION-001, the stable ledger contains C010, and the direct-source recheck is complete.

## C011 — Standardized-difference footnote says absolute value while columns contain negative values

- **Status:** Pending Human Adjudication.
- **Evidence-card fields:** The ledger and recheck provide the exact footnote definition, signed comparator values, applicable sign rule, reproducible logical comparison, readily checked group-direction examples, missing table-generation convention, a signed-value alternative, observation-versus-inference separation, and an exact human question. No material candidate-specific evidence field is missing.
- **Direct support and pagination:** Main article PDF p. 5 contains Table 1 and multiple negative standardized-difference entries; PDF p. 6 contains the continuation and footnote b defining the values as an “absolute value.” Both package-relative links resolve to the direct PDF and the pagination is truthful.
- **Reproduced comparison:** For every real value `x`, `|x| >= 0`; therefore negative entries cannot simultaneously be absolute values under the footnote definition. The signs also follow the printed surgery-minus-control direction in checkable examples: men are 34.5% versus 48.2% before matching and the table prints `-28.0`, while women are 65.5% versus 51.9% and the table prints `28.0`.
- **Assumptions and alternatives:** The record does not assume that the displayed signs or the footnote should govern. It retains the source-grounded possibility that the columns intentionally use signed standardized differences while the absolute-value phrase does not describe that convention.
- **Duplicate assessment:** C011 is the single N005 definition-versus-signed-display relationship. It is not a duplicate of any arithmetic, denominator, statistical-test, or table-cross-reference candidate.
- **Impact wording:** A bounded downstream statement may identify possible copying or interpretation of the balance-measure convention if the candidate is confirmed. It must not infer an effect-estimate or paper-level conclusion change.
- **Required repair:** Completed. N005 now includes the relationship, the numeric checker preserves AUDIT-OMISSION-002, the stable ledger contains C011, and the direct-source recheck is complete.

## Coverage and execution audit

### Direct sources and reusable evidence

The source-coverage rows reconcile as follows:

| Source | Total | Reusable | Fresh-required | Mapped | Audit result |
|---|---:|---:|---:|---:|---|
| DOC-001 | 12 | 12 | 0 | 12 | Count partition and mapping closure reproduced. |
| DOC-002 | 20 | 15 | 5 | 20 | Count partition and mapping closure reproduced. |
| DOC-003 | 7 | 0 | 7 | 7 | Count partition and mapping closure reproduced. |

The total is 39 pages, with `27 + 12 = 39` and 39 mapped pages. Fresh native and layout extraction artifacts exist for DOC-002 pp. 1-5 and DOC-003 pp. 1-7. All 59 actively reused artifact paths exist and all 59 before-hashes reproduce. The maps explicitly document no-applicable-result pages, so reusable evidence did not become a scientific scope boundary.

The direct-source before-hash manifest was repaired from the contemporaneous source inventory. `sha256sum -c` now passes DOC-001, DOC-002, and DOC-003. The corrected DOC-002 digest is `ec4e0375222279bcc2137db1be3649d22fd86997f308c1c8f0cba85cfba4c322`. This closes the earlier run-manifest transcription defect; no direct source or reused artifact was modified.

### Coverage manifest

At audit closure, the pre-report coverage manifest has 20 data rows. Each row contains one undecorated relative artifact path, each existing row has a disjoint or explicitly complete scope, and every listed artifact exists. All assigned N IDs and S IDs are explicitly enumerated without a range shortcut. Candidate registration, evidence recheck, and evidence quality each enumerate C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, and C011 individually. Evidence recheck is marked COMPLETE for 11 of 11 IDs.

This audit closes the evidence-quality scope. The coordinator must mark its manifest row COMPLETE after this response. The mandatory `report_generation` row is intentionally pending until the report agent is assigned; that later row must enumerate C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, and C011 individually and contain one plain relative artifact path. These are downstream orchestration controls, not an unresolved scientific-coverage gap.

### Statistical passes and display-zero rule

Statistical pass 1 uses runtime ID `/root/statistics_pass_1`; statistical pass 2 uses `/root/statistics_pass_2`. They are distinct, non-placeholder runtime IDs. Both manifest rows specify `gpt-5.6-terra`, `high`, and `FRESH_SPAWN`. Each pass explicitly covers S001, S002, S003, S004, S005, S006, S007, S008, S009, S010, S011, S012, S013, S014, S015, S016, S017, S018, S019, S020, S021, S022, S023, S024, and S025. Pass 2 also revisits every stable candidate and recheck fact that existed at its start.

No stable candidate mentions or depends on `P = 0`, `p = 0.000`, or an equivalent display zero. The source relationships use threshold forms such as `P<.001`, which the statistical inventories and both passes correctly distinguish from display zero. Therefore the independent-contradiction conditional field is not applicable to C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, or C011.

### Agent execution manifest

The manifest snapshot contains 10 unique agent IDs and no duplicate row. It includes the coordinator once and includes the reuse curator, both mappers, numeric reviewer, cross-source reviewer, both statistical reviewers, mechanical rechecker, and this auditor once each. Model, effort, start mode, and primary artifact agree with the role contract. The appended-ID recheck was completed by the already manifested evidence-rechecker, so it does not create a second agent row. The coordinator must append every later report-generation or other model agent exactly once; the final token ledger must use the same final agent set.

## Closure controls for downstream report generation

All evidence-quality repairs are complete. The remaining controls belong to the subsequent report-generation and final-validation stages:

1. Mark the `evidence_quality` coverage row COMPLETE and add the mandatory `report_generation` row after the report agent is assigned. Enumerate C001, C002, C003, C004, C005, C006, C007, C008, C009, C010, and C011 individually, with one plain relative artifact path in each row.
2. Keep the ledger, recheck, quality, and final-report ID sets identical at 11 unless a later genuinely new candidate is appended without renumbering and then rechecked and audited.
3. Add every later model agent exactly once to the execution manifest and token ledger.
4. Every final report card must contain the complete required evidence-card fields. Its human adjudication section must use exactly these blank subfields and no substitute values:

   ```markdown
   **Human adjudication fields:**
   - **Validity:** __
   - **Importance:** __
   - **Action:** __
   - **Initials:** __
   - **Notes:** __
   ```

## Limitations

The supplied package does not include matching code, analysis code, unrounded cumulative-incidence or ARD inputs, bootstrap replicates, medication contingency cells, exact test-function settings, a reconciliation rule for the two year-0 medication denominators, table-generation code, or document version history. These limits are named in the applicable candidate records and do not prevent the direct observations or calculations recorded here. The final report and human-adjudication subfields do not yet exist, so their exact 11-ID set, evidence-card labels, bounded downstream wording, and `__` placeholders require final mechanical confirmation after report generation.
