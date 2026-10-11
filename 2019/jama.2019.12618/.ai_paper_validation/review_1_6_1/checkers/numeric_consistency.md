# Numeric consistency review

Fresh primary numeric checker: 94 relationship bundles N001–N094. Complete scope is the article pp1–10, results-supplement pp1–9 and13, all protocol pp1–153, all SAP pp1–83 and data-sharing p1. Disjoint supplementary adverse-event-table review is appended below, with N095–N195. Combined inventory: 195 relationships; both bounded assignments remain below120. Complete source maps and every page-coverage record were read. Source-linked reusable text supplied all table cells; direct Poppler26.01.0 extraction confirmed the final SAP population definitions and relevant rescue tables. No prior scientific conclusions were consulted.

Checks include every flow branch, every baseline row, every efficacy result and sensitivity row, every main safety row, all supplement counts/doses/definitions outside the disjoint shard, all plan numeric design relationships and administrative no-applicable units. Exact patient counts are integers. Rounding intervals are half the last displayed unit; categorical totals permit reported overlap; model-based estimates are distinguished from crude recomputation. All94 primary relationships are CHECK_COMPLETE. Normal-approximation power calculations are diagnostics except where the plan prints that exact formula; unreported quantile conventions and model details cannot establish findings.

## Findings

### F-NUM-001

The reported per-protocol sensitivity population uses a different numeric adherence threshold from the final SAP.

- **Locations and roles:** REPORT [main article PDF p6, adherence sensitivity narrative](../../../jama_rathinam_2019_oi_190092.pdf#page=6) and [PDF p7, Figure2 model4 and footnote e](../../../jama_rathinam_2019_oi_190092.pdf#page=7); PLAN [final SAP PDF p71, §4.1](../../../joi190092supp3_prod.pdf#page=71), corroborated by PLAN [original SAP PDF p31, §4.1](../../../joi190092supp3_prod.pdf#page=31).
- **Printed inputs:** Final SAP per-protocol efficacy population includes ITT participants excluding major deviations or medication noncompliance, explicitly “less than 50% of the study drug received by self report or pill counts at study visits.” The article p6 sensitivity includes only participants missing less than20% of doses; Figure2 calls model4 “Per protocol”, with90/94 participants,61/54 successes,n184,OR1.56(95%CI0.84–2.96),P=.17.
- **Rule and calculation:** Let a be the fraction of expected doses received and m=1−a the fraction missed. The SAP adherence component retains a≥0.50 (m≤0.50); the report retains m<0.20 (a>0.80). The interval0.50≤a≤0.80 is retained under the SAP adherence component but excluded under the report rule. The30 percentage-point threshold separation exceeds any whole-percent half-unit rounding intervals. This is a definition comparison, not an assertion that a particular participant occupies that interval. The participant total90+94=184 itself reconciles.
- **Relationship IDs:** N040,N078.
- **Focus area:** D, planned versus reported analysis population.
- **Proposed review domain:** protocol_report. Primary relationship P_R; all relationships P_R.
- **Affected result or extracted value:** The definition of the n184 per-protocol six-month sensitivity analysis and itsOR1.56(0.84–2.96),P=.17.
- **Why context does not resolve it:** The report explicitly labels this analysis per protocol, while the final SAP gives a materially different adherence component for that named population. The report does not explain replacement of the50% receipt threshold, distinguish an additional adherence-only sensitivity from the SAP per-protocol set, or state how major deviations were handled for this displayed set. Both definitions are explicit; a reader cannot know whether the named planned population or a newly defined sensitivity produced the displayed result.
- **Source-grounded alternatives:** The displayed result may be an additional stricter adherence sensitivity; or the planned per-protocol definition may have been amended beyond the supplied final SAP; or the report's label may refer to a differently constructed population. The supplied text does not select among these possibilities. No alternative participant count is inferred.
- **Human question:** Was Figure2 model4 the prespecified SAP per-protocol efficacy analysis or a separate adherence sensitivity, and which adherence/deviation definition produced its184 participants?

## Excluded observations

Each apparent observation is listed once. Ordinary reconciled arithmetic appears in the inventory rather than being inflated into excluded-observation counts.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main p3–4,p7;N006 | Narrative “lost to follow-up”22 includes19lost and3missed visits in flow. Both forms lead to11missing perarm and194 analyzed; counts and population are immediately identifiable. | TERMINOLOGY_OR_WORDING |
| REPORT main p5;N012 | Race categories sum111/112 rather than107/109. Footnote identifies seven participants with more than one racial heritage; excess4+3=7. | CONTEXT_RESOLVES |
| REPORT main p5;N020,N022,N024 | Rounded grade percentages sum99.9 or100.1 in some columns. Each individual percentage lies within its half-unit interval using its evaluable-eye denominator. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p5;N026 | MMF edema55(27.3) with201eye header gives27.3632%, outside27.3±.05. The explicit count/header make55/201 clear; this isolated tenth-point display does not obscure the intended descriptive proportion. | CONTEXT_RESOLVES |
| REPORT main p6;N031 | MTX failure-category percents81+9+9=99 while26+3+3=32. Individual whole-percent rounding intervals reconcile. | ROUNDING_OR_DISPLAY_PRECISION |
| REPORT main p6–7;N036 | Switching columns20/29 versus7/20 are opposite original allocation. Immediate footnote/narrative identifies current medication, resolving reference population. Superscript associations are similarly resolved by full footnote text. | CONTEXT_RESOLVES |
| REPORT main p7;N035 | 68eligible switch failures is not reproduced by74failures minus5lab safety failures alone, which gives69. Eligibility is not stated to be determined solely by those five failures; absence of another exclusion cannot be assumed. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p7;N037 | Steroid discontinuation50.0%/55.0% has no printed numerator/denominator; inferring them from all continuation patients or continued successes creates an unstated assumption. | CONDITIONAL_OR_UNREPORTED |
| REPORT main p6–7;N046 | Reported site-adjusted ORs/RDs differ slightly from crude odds/differences; the stated logistic random-site model resolves that comparison. | MODEL_VERSUS_CRUDE |
| REPORT main p6;N041–N042 | Modelled visual/thickness differences are not the differences of printed medians. Model and descriptive summaries are different quantities. | MODEL_VERSUS_CRUDE |
| REPORT main p8;N047 | MMF header109 differs from the108 denominator of percentages. Footnote identifies the one randomized patient never treated; exposure population is identifiable immediately and supplement explicitly prints108. | CONTEXT_RESOLVES |
| REPORT main p7–8;N050 | MTX ALT/AST14(13.0) with107 participants yields13.0841%, outside13.0±.05. Explicit count and exposure denominator identify14/107; other MTX cells establish107. Isolated tenth-point display is immediately resolvable. | CONTEXT_RESOLVES |
| REPORT main p7–8;N058 | Fourteen serious events cannot be reconstructed by summing20patient-category counts; overlapping categories are permitted, and the package does not establish a disjoint event-to-category map. | CONDITIONAL_OR_UNREPORTED |
| PLAN SAP pp23,63–64;N066 | Conventional unadjusted normal diagnostic gives196.22complete participants or218.03 allowing10%loss versus approximate216. Source calls power/sample size approximate and simulation-based; formula quantile convention and interim-adjusted implementation are not supplied. A diagnostic cannot establish a different fitted-design sample size. | CONDITIONAL_OR_UNREPORTED |
| PLAN SAP pp24,65;N069 | Parenthetical hazardC=log2/3.5 follows a sentence attributing3.5months toMMF, whileC denotesMTX. Within this secondary power illustration, the3.5-month assumed median is explicit and swappingC/I is a label matter rather than a different actual trial result. | CONTEXT_RESOLVES |
| PLAN SAP pp26–27,67–68;N074–N075 | Enrollment table says B→A58.3,A→B38.9; power-table headings display A→B58,B→A38. Surrounding explicit j0/j1 definitions, n1=58/n0=38 and named p0/p1 identify which sample size enters each term immediately. Transposed A/B headings do not obscure the printed power calculation. | NOTATION_OR_TYPOGRAPHY |
| PLAN SAP pp27,68;N076 | Narrative says17%difference withMMF.42; table80% row uses.42 versus.17 and summary says25%difference. The adjacent table/summary resolve17 as the comparator probability rather than the difference; .42−.17=.25. | CONTEXT_RESOLVES |
| PLAN SAP pp27,68;N075 | Seven-row explicit normal-power formula yields87.4165,80.2453,82.8952,94.0835,95.5020,80.0441,82.3322%. First six round to printed87,80,83,94,96,80. Last80% row can reconcile when .40 and.15 each keep±.005 input intervals: .396 versus.154 yields79.52%, inside80±.5. | ROUNDING_OR_DISPLAY_PRECISION |
| PLAN protocol pp43–44,124–125;N088 | “10 or more letters of the first line” versus five-letter rows is an obvious wording slip: nearby total-correct-letter score and+30 rule identify the intended total. No trial value is assigned differently. | TERMINOLOGY_OR_WORDING |
| PLAN protocol/SAP definitions and revisions;REPORT main p3,8;supp1 pp5–7;N063,N089,N091 | Exact laboratory cutoffs vary at boundary values or between disclosed original/final revisions. No actual patient at an implicated boundary is supplied; extrapolating changed success/event classification is conditional. Operational or historical version comparisons alone do not establish an affected result. | CONDITIONAL_OR_UNREPORTED |
| PLAN recruitment/refraction/instrument/administrative pages;REPORT sharingp1;N079,N088,N090,N094 | Accrual39 versus40months at25%lower rate; scanner512×218 wording; chart/refraction/certification/admin numerals and historical background do not alter a supplied result, analysis-population size or planned statistical decision. | PERIPHERAL_COMPARISON |

## Limitations

No source-unit coverage gap. Raw individual adherence, category overlap, exact steroid-discontinuation numerators and intermediate model outputs are not supplied; no alternative numeric result is inferred. Statistical power and test findings are also independently reviewed in the mandatory statistical lanes. Primary checker:94 relationships,1 finding,21 excluded-observation rows. The supplement shard contributes101 relationships,0 findings,3 excluded observations. Combined195 relationships,1 finding,24 excluded observations.

# Numeric consistency checker: supplementary table shard

Assigned scope: DOC-002 REPORT joi190092supp1_prod.pdf, eTables4,5,6,8,9, PDF pages10,11,12,14,15,16. The assigned scope includes every printed table row and its count/percentage/denominator relation. eTable7 at PDF p13 and all matched counts outside these tables belong to the main numeric checker. Source location links below are relative to this part artifact.

Required QUALITY_CONTROL_SCOPE.md and workflow_1_6_1/review_contract.md were read completely. Tooling record reports direct Poppler tools available. Source-native authority used: Poppler26.01.0 pdftotext layout streamed directly from joi190092supp1_prod.pdf for PDF pages10–16. Relevant support extraction supplied locators, without importing checker conclusions. No old candidate or report artifact, external evidence, or extra Python was used.

## Complete scope and rules

All93 assigned rows,186 group-specific count/percentage cells,5 population-header relations and3 any-event union relations were checked. Complete provisional mapping is relationships/parts/numeric_supplement_inventory.md (N095–N195); the main numeric checker assigns global N identifiers losslessly.

Every count is an integer number of patients reporting at least one event. The percentage calculation is100n/D. One-decimal percentages retain half-unit display intervals, ±0.05 percentage point. Count and denominator half-unit intervals are intersected with the integer patient-count scale, leaving the printed integer. All counts satisfy0≤n≤D. The percentages are proportions of patients, not event rates, risk ratios or other between-arm effect measures. Tables supply no modeled estimate to compare with crude percentages.

The91 ordinary row relationships reconcile within one-decimal percentage intervals in both arms. Two row-level percentage observations are addressed below. The first three tables use107 MTX recipients and108 MMF recipients; their common footnote accounts for one randomized MMF patient who did not receive medication. eTable8 uses the continuation-after-success cohort62/56; eTable9 uses the switching cohort29/20. These interval-specific cohorts were not compared with randomized baseline denominators.

The any-event rows are compatible with person-level unions, with repeated category membership allowed:
- eTable4: category sums49/46, category maxima9/19, any-event30/33, population107/108.
- eTable5: category sums47/34, category maxima12/9, any-event22/19, population107/108.
- eTable6: category sums 168/131, category maxima 16/17, any-event 59/55, population 107/108.

In each arm and table, maximum category count≤any-event count≤min(population,category sum). No individual-level overlap data are supplied, so exact union arithmetic cannot be reconstructed. That is not a source contradiction.

## Findings

None. No F-NUM identifier assigned.

## Excluded observations

| Location | Observation | Reason code |
|---|---|---|
| [DOC-002 PDF p10](../../../joi190092supp1_prod.pdf#page=10), eTable4, REPORT, MMF eye-floaters cell; N098 | Printed5 (4.7), header N=108.100×5/108=4.6296296%, outside displayed4.7 interval[4.65,4.75); the expected one-decimal percentage is4.6. Both n=5 and N=108 are explicit, and neighboring MMF cells of5 are reported4.6 in the immediately adjacent tables. This isolated percentage display is resolved at once from the count and denominator, leaving the patient proportion identifiable. | CONTEXT_RESOLVES |
| [DOC-002 PDF p15](../../../joi190092supp1_prod.pdf#page=15), eTable9, REPORT, serious systemic diarrhea MMF cell and MMF header; [p16](../../../joi190092supp1_prod.pdf#page=16) footnote; N186 | Printed1 (3.4), header N=20.100×1/20=5.0%, outside displayed3.4 interval[3.35,3.45). The same table reports MMF1 (5.0) for low hemoglobin, allergy and fever; MTX N=29 with1 (3.4) is printed throughout. The displayed count and header identify1/20 at once. Footnote merely names diarrhea/fatigue as drug-related serious events and gives no separate denominator. This isolated percentage display does not obscure the count or intended denominator. | CONTEXT_RESOLVES |
| [DOC-002 PDF p10](../../../joi190092supp1_prod.pdf#page=10), [p11](../../../joi190092supp1_prod.pdf#page=11), [p12](../../../joi190092supp1_prod.pdf#page=12), REPORT, any-event rows versus categories; N193–N195 | Any-event count is not the sum of patient counts in individual categories. Patients may report more than one category; the table explicitly counts patients with at least one event and union bounds hold. | CONTEXT_RESOLVES |

## Limitations and handoff

No scientific coverage gap within the assigned scope. Patient overlap data are unavailable for exact any-event union reconstruction; displayed union bounds were fully checked. No inference was made about omitted adverse-event rows, unreported category exclusivity or unreported denominators.

Counts:101 provisional numeric relationships;93 table rows;186 count/percentage cells;0 findings;3 excluded-observation rows. Every assigned source page is covered; p16 supplies the eTable9 footnote. This checker emits no candidate ID, adjudication or proposed correction.

