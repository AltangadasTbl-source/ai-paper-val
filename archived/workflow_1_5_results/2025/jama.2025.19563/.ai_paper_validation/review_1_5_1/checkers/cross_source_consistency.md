# Cross-Source and Cross-Location Consistency Review

## Scope and method

This review covers the canonical 1.5.1 inventories `N001` through `N117` and
`S001` through `S034`, using the current main/support mapping artifacts and
direct-PDF confirmation of every potential discrepancy reported below. It
compares occurrences only after matching population, time, intervention
contrast, outcome/component definition, model, measure/scale, unit, reference
direction, and displayed precision. Protocol values labelled planned or
projected were not treated as observed-result comparators. No old candidate,
checker, verification, quality, or report artifact was used as a scientific
input.

The direct sources are:

- DOC-001: `jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf` (PDF pp. 1-11).
- DOC-002: `joi250084supp1_prod_1765403089.61351.pdf` (PDF pp. 1-90; protocol/SAP).
- DOC-003: `joi250084supp2_prod_1765403089.61751.pdf` (PDF pp. 1-69; Supplement 2).

`CROSS-CAND` keys below are provisional checker keys only. They are not stable
candidate IDs, dispositions, severity assessments, validity judgments, or
adjudications.

## Complete inventory and matched-cluster coverage

| Inventory IDs reviewed | Matched cluster(s) and identity controls applied | Result |
|---|---|---|
| N001-N002; N036-N039; N066-N067; S001, S008-S010 | Study frame; primary endpoint; ITT/randomized population; 12-month timing; AI/dDPP minus human/hDPP contrast; noninferiority rule | One planned-versus-reported endpoint-definition discrepancy is recorded as CROSS-CAND-001. Planned N=368/184 per arm versus observed N=368/183 and 185 is a planned-versus-observed distinction, not a conflict. |
| N003-N007; N091-N092 | Recruitment, allocation, retention, primary-analysis and restricted-analysis populations | PASS. Figure 1 allocation 183+185=368; missed 12-month visit counts 26+29=55; restricted populations 151+149=300. eTables 1-2 use their stated start/exposure/site populations. |
| N008-N018; N093-N101; S022-S026 | Overall and arm-specific baseline characteristics, site, A1C-status, completion-status and per-protocol tables; counts, denominators, units, summary type and displayed precision | Main-table age P=.01 and eTable 3 P=.014 concern the same randomized-arm comparison and are compatible with differing displayed precision. Two table-footnote inconsistencies are recorded as CROSS-CAND-003 and CROSS-CAND-004. |
| N019-N024; N102-N111; S004-S007, S014-S021, S027-S034 | Primary/component outcomes, incident diabetes-range A1C, engagement, completion, per-protocol and sensitivity results; 12-month time, population, AI-minus-human direction, percentage-point RD, adjusted/unadjusted model and one-sided bound | PASS except CROSS-CAND-002. Main Figure 2/unadjusted eFigure 4 overall RD (-0.2) and age-adjusted eFigure 3 RD (-2.0) are distinct models, so they are not conflicting values. Incident A1C 4.4%/3.8% matches 8/183 and 7/185 in eTable 13 when defined as occurring during the study (6 and/or 12 months). |
| N025-N030; N112-N117 | Figures 3-4; figure labels, units, engagement matrices; sensitivity and adverse-event tables | CROSS-CAND-005 records the Figure 3 baseline measure label. Figure 4 counts/percentages reconcile under the stated within-engagement and among-achiever denominators. eTables 18-19 differ only by stated sensitivity/model; eTable 20 participant counts and event counts retain their explicitly different denominators. |
| N031-N035; N040-N065; N068-N090; S011-S013 | Narrative cross-references; protocol definitions, schedules, instruments, missingness, activity, medication, safety and economic-plan records | PASS / not directly matchable where source is a definition, external context, planned operation, or has no reported comparator. Rate, count, proportion, and unit distinctions were retained: protocol health-use fields are 6-month counts, not rates; adverse-event category cells are event-level, while the participant row is participant-level. |

All 117 numeric/reporting IDs and all 34 statistical IDs are represented by the
six coverage rows above. No display-zero P value was mapped; the display-zero
exclusion is therefore not applicable.

## Matched results that agree after identity matching

- **Primary randomized result:** DOC-001 PDF pp. 1, 4, and 7 reports 58/183
  (31.7%) versus 59/185 (31.9%), unadjusted RD -0.2 percentage points with a
  one-sided lower bound -8.2. DOC-003 PDF p. 35 (eFigure 4 overall) reports
  the same population/counts/percentages and unadjusted result. DOC-003 p. 34
  (eFigure 3) instead expressly reports an *age-adjusted* RD -2.0 (-9.8), so
  its different estimate is model-specific rather than a cross-source conflict.
- **Component results:** DOC-001 PDF p. 7 Figure 2 and DOC-003 PDF p. 34
  eFigure 3 agree on all randomized-arm component numerators, denominators and
  one-decimal percentages. The RDs differ only where eFigure 3 explicitly uses
  age adjustment. The baseline-prediabetes A1C component is n=130 per arm in
  both sources.
- **Program initiation/completion and engagement:** DOC-001 PDF pp. 4 and 9
  agrees with the Figure 4 matrices: AI 171/183 initiated and 117/183
  completed; human 153/185 initiated and 93/185 completed. The 25/22/37% and
  28/28/35% figures use engagement-level denominators; the 5/21/74% and
  15/29/56% figures use outcome-achiever denominators, so they are not
  competing rates.
- **Participant populations and missingness:** DOC-001 PDF pp. 4-5 and
  DOC-003 PDF pp. 48-50 agree on 26 AI and 29 human participants without a
  12-month visit and on treatment-failure primary handling. The A1C-method
  count issue below is an exception.
- **Per-protocol results:** DOC-001 PDF p. 4 defines the restricted analysis;
  DOC-003 PDF pp. 53-58 uses AI N=151/human N=149 and reports its results as
  supportive per-protocol data. These are not directly interchangeable with
  primary ITT results.
- **A1C and activity definitions:** DOC-001 PDF pp. 3-4 and DOC-003 PDF pp.
  7-30 consistently distinguish A1C percentage points, ActiGraph MVPA in
  minutes/week, the 150-minutes/week benchmark, and the primary zero assignment
  for nonwear. eTables 18a-18b are explicitly alternative PA assumptions.
- **Adverse events:** DOC-001 PDF pp. 6 and 9 says more events occurred in AI
  and none were study-related. DOC-003 PDF pp. 63-68 gives 66/183 versus
  21/185 participants with an event, 100 versus 25 events, and 0 related events
  in each arm. These descriptions agree after distinguishing people from events.

## Provisional qualifying observations

## CROSS-CAND-001 — Protocol and final-report primary endpoint use different A1C failure conditions

**Category:** Cross-document numeric inconsistency / measure, label, or scale inconsistency.

**Exact linked locations:**

- [DOC-002 protocol — PDF p. 15](<../../../joi250084supp1_prod_1765403089.61351.pdf#page=15>), section 3.2 Primary Endpoint.
- [DOC-001 main article — PDF p. 4](<../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4>), Primary Analysis.
- [DOC-003 Supplement 2 — PDF p. 56](<../../../joi250084supp2_prod_1765403089.61751.pdf#page=56>), eTable 13 methods/result context.

**Printed values/statements:** The protocol defines the binary 12-month success as one or more of: at least 5% weight loss; at least 4% weight loss plus at least 150 minutes/week PA; or at least a 0.2% A1C reduction. It states success is 1 if at least one measure is achieved and 0 otherwise. The main article instead defines its primary endpoint as those three components **in participants who maintained HbA1c less than 6.5% throughout the study**. Supplement eTable 13 states that participants with diabetes-range A1C at 6 and/or 12 months fail the endpoint regardless of weight/PA.

**Comparison logic:** Population (randomized participants), intervention contrast, 12-month endpoint, component thresholds, units, and endpoint role match. The added throughout-study A1C <6.5% condition changes who can be classified as a primary-endpoint success; it is not a difference in rounding, model, or a planned sample-size quantity.

**Supported alternatives:** A protocol amendment, SAP update, or prespecified final analysis rule may have added this failure condition. The supplied protocol page may not be the final amended version. Those possibilities explain the difference but do not identify its source in the supplied files.

**Human verification steps:** Determine the protocol version/amendment history governing the final analysis; verify whether the A1C <6.5% throughout rule was prospectively added and whether the main text should identify it as an amendment or revised endpoint definition; verify endpoint coding for participants with diabetes-range A1C.

## CROSS-CAND-002 — 313 stated complete A1C outcomes versus 312 listed 12-month A1C measurements

**Category:** Denominator, proportion, or total inconsistency / cross-document numeric inconsistency.

**Exact linked locations:**

- [DOC-001 main article — PDF p. 4](<../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=4>), Results: “313 participants completed the 12-month study and had complete outcomes data.”
- [DOC-003 Supplement 2 — PDF p. 8](<../../../joi250084supp2_prod_1765403089.61751.pdf#page=8>), A1C Measurement table: 12-month Afinion 2 Analyzer n=282, A1CNow+ n=30, serum n=0.
- [DOC-003 Supplement 2 — PDF p. 50](<../../../joi250084supp2_prod_1765403089.61751.pdf#page=50>), eTable 8c: 26/183 and 29/185 A1C measurements missing and “There was no missing A1C ... data among study completers.”

**Printed values:** The listed 12-month A1C method counts sum to 312 (282 + 30 + 0). The main article gives 313 participants with complete 12-month outcomes; eTable 8c gives 55 missing A1C observations (26 + 29), also implying 368 - 55 = 313 with an A1C result, and explicitly says none is missing among completers.

**Comparison logic:** All three occurrences concern the study's 12-month participant-level A1C availability, not different intervention arms, rates, or analysis models. Under the table title, the three method rows are presented as the devices/methods used for A1C measurements. Their total is one lower than both independently printed complete-A1C quantities.

**Supported alternatives:** One 12-month A1C measurement may have used an unlisted method, may have been omitted from the device-method table, or “complete outcomes” may have a denominator not fully captured by that table despite eTable 8c's no-missing-A1C statement.

**Human verification steps:** Reconcile the 313 participant IDs with A1C device logs; confirm whether any 12-month result used Siemens DCA Vantage or another unlisted method; correct either the device-method table total or the completeness/missingness statement if reconciliation does not yield 313.

## CROSS-CAND-003 — Figure 3 calls BMI values “weight” while the matched baseline table identifies them as BMI

**Category:** Measure, label, or scale inconsistency.

**Exact linked locations:**

- [DOC-001 main article — PDF p. 8](<../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=8>), Figure 3 footnote a.
- [DOC-001 main article — PDF p. 6](<../../../jama_mathioudakis_2025_oi_250084_1765403089.60451.pdf#page=6>), baseline Table BMI row.
- [DOC-003 Supplement 2 — PDF pp. 53-54](<../../../joi250084supp2_prod_1765403089.61751.pdf#page=53>), eTable 11 BMI row for the restricted-analysis population (supporting unit distinction).

**Printed values/statements:** Figure 3 footnote a says “Baseline median (IQR) weight: 32.2 (28.2-35.9) kg/m2” in AI and “32.5 (29.3-37.7) kg/m2” in human. The main baseline Table prints those same values under “BMI, median (IQR).” Weight is a mass quantity (e.g., kg), whereas kg/m2 is the printed BMI unit.

**Comparison logic:** The identical arm-specific values and IQRs make this a matched occurrence; population is randomized baseline in both. The scale/unit rules identify the Figure 3 values as BMI, not weight. This is not merely a difference between baseline and 12-month weight change plots.

**Supported alternatives:** “Weight” may be a figure-footnote label error, with the values/unit correctly describing BMI. No source supports interpreting 32.2 kg/m2 as body mass.

**Human verification steps:** Check the figure production source and baseline dataset; replace the label with BMI if confirmed, or report actual baseline weight in kg if weight was intended.

## CROSS-CAND-004 — eTables 5-7 repeat an age P value for “study groups” beneath tables with different comparison groups

**Category:** Cross-document numeric inconsistency / measure, label, or scale inconsistency.

**Exact linked locations:**

- [DOC-003 Supplement 2 — PDF pp. 42-43](<../../../joi250084supp2_prod_1765403089.61751.pdf#page=42>), eTable 5 “Baseline Characteristics by Site,” age footnote 2.
- [DOC-003 Supplement 2 — PDF pp. 44-45](<../../../joi250084supp2_prod_1765403089.61751.pdf#page=44>), eTable 6 “Baseline Characteristics by Baseline A1C Status,” age footnote 2.
- [DOC-003 Supplement 2 — PDF pp. 46-47](<../../../joi250084supp2_prod_1765403089.61751.pdf#page=46>), eTable 7 “Baseline Characteristics by Trial Completion Status,” age footnote 2.
- [DOC-003 Supplement 2 — PDF pp. 39-40](<../../../joi250084supp2_prod_1765403089.61751.pdf#page=39>), eTable 3, where the same randomized treatment-arm comparison is actually displayed.

**Printed values/statements:** Each of eTables 5, 6, and 7 attaches to Age the statement: “Age differed between study groups (p = 0.014); all other baseline characteristics were similar (p > 0.05).” Their column comparisons are, respectively, site (JHU vs Reading), baseline A1C status (<5.7% vs 5.7%-6.4%), and trial completion status (completer vs dropped out/lost). In contrast, eTable 3 is the randomized-population/treatment-arm table that also uses the p=.014 statement.

**Comparison logic:** A P value has meaning only with its comparison population/contrast. The exact duplicated statement identifies “study groups,” but the three tables display different contrasts and in eTables 5-6 print their own different comparison statements (site differences and A1C-status differences). Thus p=.014 cannot simultaneously be the displayed table-specific age test for all three table contrasts.

**Supported alternatives:** The repeated footnote can be an intentionally retained global randomized-treatment-arm note rather than a table-specific P value; however, its attachment to the Age rows of three other stratification tables makes that scope unclear. It may also be a copied footnote that should have been removed or relabelled.

**Human verification steps:** Confirm the intended comparator for each p=.014 footnote; if it is the treatment-arm result, relocate or label it as a global note; if table-specific, provide/recalculate the appropriate P values for the site, A1C-status, and completion contrasts.

## CROSS-CAND-005 — eTable 7 says no characteristic was significant but supplies the significance threshold in the opposite direction

**Category:** Statistical reporting inconsistency / cross-location label inconsistency.

**Exact linked location:** [DOC-003 Supplement 2 — PDF pp. 46-47](<../../../joi250084supp2_prod_1765403089.61751.pdf#page=46>), eTable 7 footnote 1.

**Printed statement:** “No baseline characteristics were statistically significant different between groups (p<0.05).”

**Comparison logic:** Under the ordinary stated threshold convention used elsewhere in the same supplement (for example, eTable 3 says an age difference has p=.014 and calls it different; the accompanying other-characteristics wording is p>0.05), `p<0.05` denotes statistical significance, whereas the text says none was statistically significant. The wording is internally opposite and does not report individual table-specific P values that could resolve it.

**Supported alternatives:** The inequality may be a typographic sign error and intended to read `p>0.05`; alternatively, the sentence may have omitted a qualifier or refers to a different test family. The supplied table does not state the exact tests/P values for the completion-status comparisons.

**Human verification steps:** Verify the completion-status analysis output and intended significance convention; correct the inequality or sentence; provide a table note that names the comparison/test if the result is retained.

## Limitations

- DOC-002 native/layout text is glyph-encoded, so its endpoint language was
  confirmed on the direct rendered protocol page. This is an extraction-method
  limitation, not a source-coverage gap.
- The package supplies no raw participant data or final protocol-amendment
  history. These sources can explain, but cannot resolve, CROSS-CAND-001 and
  CROSS-CAND-002.
- No candidate is based solely on an absent value, external literature, general
  study-design concern, or P-value display convention.

## Completion statement

Reviewed matched clusters: 6 inventory coverage clusters. Provisional qualifying
observations: 5 (`CROSS-CAND-001` through `CROSS-CAND-005`). All inventory IDs
were covered; remaining unmatched definition-only, contextual, planned, and
no-applicable records are documented above rather than treated as omissions.
