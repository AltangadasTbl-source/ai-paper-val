# Numeric consistency checker

Fresh main numeric stage: DOC-001, jama_wang_2018_oi_180070.pdf, physical pages 1–10; N001–N070 and every mapped scalar relationship checked. All compared locations below are REPORT by content within the same main article. Seven distinct candidates; no stable C IDs, severity, validity, or disposition assigned. Every candidate remains Pending Human Adjudication. Support review is disjoint and may be appended by the coordinator.

Evidence: complete current main map, reusable source-linked layout text, current direct Poppler 25.03.0 `pdftotext -layout` reads of main p.3–8, with exact table/figure labels retained. No old candidate, old conclusion, web, GPU, custom Python or installation used. Existing rendered p.6/p.8 are available for mandatory final direct visual recheck; text is a locator and transcription aid. All findings below require that recheck stage. Numerical calculations use displayed counts and ordinary arithmetic; missing scientific definitions remain explicit.

## NUM-MAIN-01 — Primary-analysis totals differ between Results and flow diagram

- Relationships: N001, N003, N014, N067. Primary category: Denominator, proportion, or total inconsistency.
- Locations and roles: [Results p.4](../../../jama_wang_2018_oi_180070.pdf#page=4), REPORT; [Figure1 bottom patient-analysis boxes p.5](../../../jama_wang_2018_oi_180070.pdf#page=5), REPORT; [Table2 all-or-none denominators p.7](../../../jama_wang_2018_oi_180070.pdf#page=7), REPORT.
- Printed inputs: Results says “4800 patients were enrolled prospectively and included in the primary analysis”; Methods says intention-to-treat for all outcomes. Figure1 says “2003 Patients included in primary analysis” intervention and “1977 Patients included in primary analysis” control. Earlier diagram boxes have2400 per arm; lost to follow-up397/423. Table2 all-or-none uses1290/2400 and1147/2400.
- Rule/calculation/tolerance: same primary-analysis population total should agree exactly;2003+1977=3980,4800−3980=820;397+423=820. Table2 denominators total4800. Integer tolerance zero.
- Direct observation: the same primary-analysis label accompanies3980 in Figure1 and4800 in text/table. Derived inference: Figure1 bottom counts apparently describe12-month follow-up completion, since they equal enrolled minus losses.
- Alternatives: diagram might mean a follow-up-specific subset or different analysis, but no such qualification appears in the boxes. This does not establish that any analysis excluded820 patients.
- Quality-control relevance: a population label may cause downstream extraction of the wrong primary denominator.
- Exact human question: Do Figure1’s2003/1977 refer to12-month completion, and which population does “included in primary analysis” intend at each location?

## NUM-MAIN-02 — Intervention CAD percentage does not reconcile with count and arm total

- Relationship: N031. Primary category: Denominator, proportion, or total inconsistency.
- Locations and roles: [Table1 p.6 intervention CAD/previous myocardial infarction row and Patients total](../../../jama_wang_2018_oi_180070.pdf#page=6), REPORT for both cells.
- Printed inputs: intervention Patients No.2400; CAD/previous myocardial infarction311(13.05); baseline126(15.7) among801 and control298(12.4) among2400 corroborate the count(percent) format.
- Rule/calculation/tolerance:100*311/2400=12.958333…%; two-decimal rounding12.96%, one-decimal13.0%; printed13.05 differs by0.091667 percentage point, exceeding its0.005-point display tolerance. A denominator producing13.05 exactly would be311/.1305=2383.1418 rather than2400.
- Direct observation: numerator, denominator and percentage printed in same table do not reconcile under its standard count/arm-total convention. Inference: a different row denominator could explain the percentage but is not given.
- Alternatives: unreported missing-data denominator approximately2383; typo in311,13.05,or denominator. General imputation is described onp.4; no row denominator footnote explains the difference.
- Quality-control relevance: the displayed baseline prevalence may be reused independently of its count.
- Exact human question: Which count and denominator generated13.05%, and is the printed intervention CAD count or percentage intended to use2400 patients?

## NUM-MAIN-03 — Control EMS percentage differs from its printed count and total

- Relationship: N035. Primary category: Denominator, proportion, or total inconsistency.
- Locations and roles: [Table1 p.6 control Transported to ED by EMS row and Patients total](../../../jama_wang_2018_oi_180070.pdf#page=6), REPORT for both cells.
- Printed inputs:236(9.9) control patients transported by EMS;control total2400. Adjacent control onset-to-ED within2h row238(9.9) is a separate variable, not replacement input.
- Rule/calculation/tolerance:100*236/2400=9.833333…%; nearest one decimal9.8%, discrepancy0.066667 percentage point from9.9 exceeds0.05-point display tolerance. A percentage rounding to9.9 requires denominator greater than2371.86 and no greater than2395.94, rather than2400.
- Direct observation: same-table count/percentage/total mismatch. Derived inference: a smaller row-specific denominator could explain it; not reported.
- Alternatives: row-specific missingness denominator, count typo or percentage typo. No table note identifies a different denominator; p.4 describes imputation.
- Quality-control relevance: count and percentage lead to different extracted EMS prevalences.
- Exact human question: Does236 use a row-specific denominator, and what denominator/count/percentage should be read for the control EMS characteristic?

## NUM-MAIN-04 — Key Points labels the all-or-none outcome as adherence to all nine measures

- Relationships: N008, N009, N040, N041. Primary category: Measure, label, or scale inconsistency.
- Locations and roles: [Key Points Findings p.2](../../../jama_wang_2018_oi_180070.pdf#page=2), REPORT; [Outcomes all-or-none definition p.3](../../../jama_wang_2018_oi_180070.pdf#page=3), REPORT; [Table2 all-or-none/rtPA rows p.7](../../../jama_wang_2018_oi_180070.pdf#page=7), REPORT.
- Printed inputs: Key Points says “co-primary outcome of adherence to all9 performance measures”; Methods defines proportion receiving all performance measures “for which the patient was eligible.” Table2 all-or-none1290/2400 intervention and1147/2400 control;rtPA receipt46/212 and23/204.
- Rule/calculation/tolerance: literal receipt of all nine includes rtPA, so all-nine recipients cannot exceed rtPA recipients46/23. Printed all-or-none1290/1147 exceeds those bounds by1244/1124; even all-nine eligibility cannot exceed212/204 rtPA eligible patients. Exact count tolerance zero. Eligible all-or-none can exceed these counts because ineligible measures are exempt.
- Direct observation: Key Points omits the eligibility qualification that makes the reported outcome counts possible. Derived inference: a literal all-nine interpretation yields impossible counts; this is a labeling issue, not an allegation that Table2 was calculated literally that way.
- Alternatives: “all9” may be shorthand for the9-measure eligible bundle; its intended colloquial reading may already be clear to specialists.
- Quality-control relevance: an unqualified label can change which outcome definition is extracted.
- Exact human question: Should the Key Points all-nine phrase explicitly indicate all eligible measures to agree with the Methods definition and Table2 counts?

## NUM-MAIN-05 — Same clinical follow-up results labeled from discharge and from onset

- Relationships: N010, N050–N059, N062, N064. Primary category: Measure, label, or scale inconsistency.
- Locations and roles: [Clinical Events opening paragraph p.5](../../../jama_wang_2018_oi_180070.pdf#page=5), REPORT; [Outcomes time definition p.3](../../../jama_wang_2018_oi_180070.pdf#page=3), REPORT; [Table3 footnoteb and Figure2 x-axes p.8](../../../jama_wang_2018_oi_180070.pdf#page=8), REPORT; [Table1 length of stay p.6](../../../jama_wang_2018_oi_180070.pdf#page=6), REPORT.
- Printed inputs: Clinical Events says outcomes at3,6,12months “after discharge,” then reports the same vascular/disability results appearing in Table3. Methods says3,6,12months “after initial symptom onset”; Table3 disability footnote says after stroke onset;Figure2 says Days After Stroke Symptom Onset. Table1 median stay13 intervention/12 control days confirms onset and discharge are distinct times.
- Rule/calculation/tolerance: identical matched follow-up outcomes should have a consistent time origin. Time since discharge equals time since onset minus onset-to-discharge interval; these origins are not interchangeable. No arithmetic correction inferable from median stay because onset-to-admission is separate; tolerance is exact label identity, not an assumed fixed12–13day shift.
- Direct observation: reference-time labels differ for the same Table3-linked results. Derived inference: discharge indexing generally shifts the observation window; no raw dates available to determine which was used.
- Alternatives: a narrative typo, or genuinely different event ascertainment origin disclosed elsewhere. The figure explicitly uses onset.
- Quality-control relevance: follow-up-time coding can differ in downstream evidence extraction.
- Exact human question: Were these3/6/12month outcomes measured from stroke onset or hospital discharge, and how should the p.5 label align with the Methods/table/figure?

## NUM-MAIN-06 — Cumulative-incidence curves called HR curves

- Relationships: N062, N064, N066. Primary category: Measure, label, or scale inconsistency.
- Locations and roles: [Discussion p.7 final right-column paragraph](../../../jama_wang_2018_oi_180070.pdf#page=7), REPORT; [Figure2A/B p.8 y-axes and annotations](../../../jama_wang_2018_oi_180070.pdf#page=8), REPORT.
- Printed inputs: discussion “The HR curves of these new clinical vascular events were almost completely separated in the first30days.” Figure2A plots two group-specific curves with y-axis Cumulative Incidence and ticks0,.05,.10,.15;annotationHR0.72(95%CI0.60–0.87). Figure2B has same y-axis and a different scalar HR0.86.
- Rule/calculation/tolerance: cumulative incidence is a time-indexed event probability for each group; an HR compares hazards between groups and is not the plotted y quantity. Two probability curves and a scalarHR.72 are different quantitative objects; tolerance exact measure identity. No calculation of an HR from curve height is justified.
- Direct observation: curve measure namedHR in prose conflicts with displayed cumulative-incidence axes. Derived inference: the adjective may lead readers to misread what separation represents; it does not negate the displayed HR estimate.
- Alternatives: informal abbreviation for curves accompanied by an HR; no separate HR-function plot is supplied.
- Quality-control relevance: incorrect measure naming can propagate confusion between event probabilities and hazard ratios.
- Exact human question: Does the discussion intend cumulative-incidence curves, and should its HR-curve label match Figure2’s plotted quantity?

## NUM-MAIN-07 — Stated NIHSS median used for imputation differs from Table1 medians

- Relationships: N013, N034. Primary category: Numeric or arithmetic inconsistency (conditional on the imputation reference population).
- Locations and roles: [Data Analysis p.4 missing-values paragraph](../../../jama_wang_2018_oi_180070.pdf#page=4), REPORT; [Table1 p.6 NIHSS admission row and patient totals](../../../jama_wang_2018_oi_180070.pdf#page=6), REPORT.
- Printed inputs: “Only one patient had a missing…NIHSS score, which was replaced by the median value of3”; Table1 NIHSS median4 in baseline survey801 patients, intervention2400 and control2400;IQRs2–8,2–6,2–6. General rule says medians imputed for missing continuous variables.
- Rule/calculation/tolerance: if3 is the median of observed trialNIHSS scores, appending one observation equal to that median preserves pooled median3. If both equal-sized arms have median4, their pooled trial median must be4 for exact displayed integer medians (or at least3.5 if integer medians were rounded from half-integer3.5). These cannot equal3. Baseline median4 also does not supply3. Integer-valuedNIHSS supports half-integer sample medians; even a±.5 display tolerance around4 excludes exact3.
- Direct observation: the value identified as “median” is3, while every displayed patient-group NIHSS median is4. Derived diagnostic inference: these summaries are incompatible if they use the same trial reference population and the stated one-value median imputation; the package does not explicitly name the median reference population.
- Alternatives: hospital-specific median3; subgroup/different data stage median;imputation under an external reference distribution;typo in3 or Table1. No individualNIHSS values or imputation implementation are supplied, so no replacement value is prescribed. This is a conditional question, not a general criticism of imputation.
- Quality-control relevance: the numeric imputation input and summary statistic may be reused as contradictory descriptions of the same baseline distribution.
- Exact human question: Which population/data stage supplied theNIHSS median3, and how does it relate to Table1’s median4 and the stated single missing value?

## Complete checks and boundaries

All70 main relationship groups checked. Table1 all hospital percentages, subgroup sums,30 patient count/percentage cells, all median/IQR/range/unit cells;Table2 all20 count/denominator/percentage cells and composite mean/SD;Table3 all20 count/denominator/percentage cells;both figures’ complete flow/risk arrays;all mapped time/population/measure/narrative repetitions inspected. Every Table2/Table3 effect label retained; adjusted versus crude differences not treated as arithmetic discrepancies. All cumulative vascular/death counts are monotonic. Disability prevalence need not be monotonic and its survivor/mRS denominator differs legitimately from trial denominator. Current eligibility need not equal baseline medical-history prevalence. Calendar3months need not coincide exactly with figure day90, so small risk-set/event boundary differences alone do not establish a candidate. Censored Kaplan–Meier incidence can exceed rawcount/2400;visual endpoints are not precise printed counts. Median versus mean and descriptive composite versus adjusted opportunity-levelOR are distinct estimands.

The in-hospital death AD confidence interval/P/significance comparison is recorded N056 and sent to the statistical lane, without a duplicate numeric card. There is no displayed-zeroP candidate. Context estimates lacking a supplied independent comparator are not externally verified. No assigned source or relationship omitted. Seven candidate cards emitted without count-based suppression; no severity, final correction, or adjudication.

# Disjoint support numeric shard — canonical merged copy

The following section preserves every support finding. Source links have been rebased from the part directory to this canonical checkers directory; scientific content and stable relationship IDs are unchanged.
# Support numeric consistency review

Status: COMPLETE. Exact scope: DOC-002 PLAN PDF pages1–25 and DOC-003 REPORT PDF pages1–9, all68 SUP-Ngroups represented by stable N501–N568 in the companion inventory. Every supplied numeric table cell, percentage, total, definition, figure and background value was considered. There is no finding limit. Main-only numeric scope is handled by the mandatory numeric reviewer. Six distinct candidate observations are emitted; none has a stable C ID, evidence state, severity or disposition.

The counted cells are58 integer numerator/denominator percentages:16 in eTable2,24 in eTable3,18 in eTable4. All58 were recalculated;54 reconcile within their printed precision and4 do not. The two rtPA eTable4 percentages use2 decimal places and reconcile. Each numerator is nonnegative and no larger than its denominator. eTable2 availability denominators sum3949+851=4800. Repeated comorbidities and overlapping vascular events are not mutually exclusive. All eTable3 event counts are nondecreasing across3/6/12months for the same event and arm. Event counts per arm/time sum107/147,169/213 and242/323; these cannot be treated as participant totals because p7 explicitly allows multiple events.

The eTable4 composite is mean(SD), so it cannot be reconstructed by unweighted averaging of component percentages. Both adjusted effect columns explicitly carry covariate footnote a; differences such as raw85.3−80.9=4.4 versus adjusted4.20 are not numeric inconsistencies. HR is not a crude risk ratio; ORPA is not a percentage ratio. Every printed interval is ordered and contains its corresponding point estimate. Statistical compatibility beyond those structural facts belongs to the independent statistical passes. Equal6-month MI event counts8/8 may coexist with adjusted nonzero difference−0.03 and HR0.78; no contradiction follows.

PLAN Figure4 shows four batches of30=120 and three intermediate feedback loops. This reconciles the planned40×120=4800 patients and three feedback cycles. The teaching example gives5=3+2 binary care opportunities, although its named total of7 measures differs from the nine-measure specification (candidate below). The network563 hospitals across27+4=31 regions gives18.16 per region and is compatible with expressly approximate “about20.” Background cost5.76billion and cited trial sizes19435/20000/one million lack a matched supplied conflicting quantity. Bibliographic identifiers and illustrative figure list numerals are not treated as patient counts.

All68 relationships receive COMPLETE entries in [the inventory](../relationships/parts/numeric_support_inventory.md). No unresolved scientific page or table-cell coverage gap remains. Supplied information does not include per-measure baseline survey denominators, a sample-size formula, or table-specific inferential variance conventions; these are named boundaries rather than candidates by themselves. Abbreviated rtPA labels (“<2hours”) versus arrival-within2/treatment-within3 definitions do not establish a separately counted treatment/eligibility discrepancy without a timestamp boundary convention. No display-zero P value candidate is emitted.

Direct-source confirmation used pdftotext25.03.0 for PLAN pp13–19 and REPORT pp3–4, and direct rendering of REPORT p8 with pdftoppm25.03.0 at1800px followed by image inspection. The source visible p8 table confirms all four percentage inputs and the LDL>100 header. Fresh derivative: .ai_paper_validation/review_1_6/preprocessing/numeric-support-page8.png, engine Poppler25.03.0. No Python extraction, package environment, web, GPU, old checker/report conclusions or source changes were used.

## NUMSUP-01 — Discharge antithrombotic control percentage

Relationship: N564. Proposed category: Denominator, proportion, or total inconsistency.

Compared locations and roles: REPORT [DOC-003 physical PDFp8,eTable4](../../../joi180070supp2_prod.pdf#page=8), row “Antithrombotics” under “Performance measures at discharge,” Control “No./Total(%)” cell. Both the printed integer fraction and its accompanying percentage are REPORT content in the same cell. The adjusted difference and ORPA columns are separate quantities and are not comparators for this candidate.

Printed inputs: 2141/2400 (89.3%). Direct source image confirms these values.

Reproducible rule and calculation: an unadjusted percentage accompanying exact integer No./Total is100×2141/2400=89.20833333333333%. Rounded to one decimal, the value is89.2%. The printed89.3% differs by0.09166667 percentage points. One-decimal tolerance is±0.05percentage points, inclusive at ties. The value lies outside that interval.

Direct observation versus inference: the fraction and percentage coexist in the source; their mathematical incompatibility under the column’s stated No./Total interpretation is observed and reproduced. Which input produced the mismatch is unknown.

Alternatives: a different denominator, a different numerator, a weighted/adjusted percentage or a transcription problem could explain the display. The table supplies no alternative percentage definition, and footnote a is attached to the adjusted difference/ORPA columns. Do not infer a correction.

Quality-control relevance: the cell supplies inconsistent raw count/proportion inputs for downstream extraction. The absolute difference is small and does not establish an effect on the trial conclusion.

Exact human question: “Does the control discharge antithrombotic entry refer to2141 of2400 patients, and if so what explains its reported89.3% rather than the proportion implied by those printed integers?”

No classification adjudication or stable C ID is assigned.

## NUMSUP-02 — AF anticoagulation control percentage

Relationship: N565. Proposed category: Denominator, proportion, or total inconsistency.

Compared locations and roles: REPORT [DOC-003 physical PDFp8,eTable4](../../../joi180070supp2_prod.pdf#page=8), row “Anticoagulation for Atrial Fibrillation,” Control “No./Total(%)” cell. Both the printed integer fraction and its accompanying percentage are REPORT content in the same cell. The adjusted difference and ORPA columns are separate quantities and are not comparators for this candidate.

Printed inputs: 39/174 (22.5%). Direct source image confirms these values.

Reproducible rule and calculation: an unadjusted percentage accompanying exact integer No./Total is100×39/174=22.413793103448278%. Rounded to one decimal, the value is22.4%. The printed22.5% differs by0.08620690 percentage points. One-decimal tolerance is±0.05percentage points, inclusive at ties. The value lies outside that interval.

Direct observation versus inference: the fraction and percentage coexist in the source; their mathematical incompatibility under the column’s stated No./Total interpretation is observed and reproduced. Which input produced the mismatch is unknown.

Alternatives: a different denominator, a different numerator, a weighted/adjusted percentage or a transcription problem could explain the display. The table supplies no alternative percentage definition, and footnote a is attached to the adjusted difference/ORPA columns. Do not infer a correction.

Quality-control relevance: the cell supplies inconsistent raw count/proportion inputs for downstream extraction. The absolute difference is small and does not establish an effect on the trial conclusion.

Exact human question: “Does the control af anticoagulation entry refer to39 of174 patients, and if so what explains its reported22.5% rather than the proportion implied by those printed integers?”

No classification adjudication or stable C ID is assigned.

## NUMSUP-03 — Lipid-lowering control percentage

Relationship: N566. Proposed category: Denominator, proportion, or total inconsistency.

Compared locations and roles: REPORT [DOC-003 physical PDFp8,eTable4](../../../joi180070supp2_prod.pdf#page=8), row “Lipid-lowering for LDL>100mg/dL,” Control “No./Total(%)” cell. Both the printed integer fraction and its accompanying percentage are REPORT content in the same cell. The adjusted difference and ORPA columns are separate quantities and are not comparators for this candidate.

Printed inputs: 1439/1586 (90.8%). Direct source image confirms these values.

Reproducible rule and calculation: an unadjusted percentage accompanying exact integer No./Total is100×1439/1586=90.73139974779319%. Rounded to one decimal, the value is90.7%. The printed90.8% differs by0.06860025 percentage points. One-decimal tolerance is±0.05percentage points, inclusive at ties. The value lies outside that interval.

Direct observation versus inference: the fraction and percentage coexist in the source; their mathematical incompatibility under the column’s stated No./Total interpretation is observed and reproduced. Which input produced the mismatch is unknown.

Alternatives: a different denominator, a different numerator, a weighted/adjusted percentage or a transcription problem could explain the display. The table supplies no alternative percentage definition, and footnote a is attached to the adjusted difference/ORPA columns. Do not infer a correction.

Quality-control relevance: the cell supplies inconsistent raw count/proportion inputs for downstream extraction. The absolute difference is small and does not establish an effect on the trial conclusion.

Exact human question: “Does the control lipid-lowering entry refer to1439 of1586 patients, and if so what explains its reported90.8% rather than the proportion implied by those printed integers?”

No classification adjudication or stable C ID is assigned.

## NUMSUP-04 — Antidiabetic medication control percentage

Relationship: N568. Proposed category: Denominator, proportion, or total inconsistency.

Compared locations and roles: REPORT [DOC-003 physical PDFp8,eTable4](../../../joi180070supp2_prod.pdf#page=8), row “Antidiabetic Medication,” Control “No./Total(%)” cell. Both the printed integer fraction and its accompanying percentage are REPORT content in the same cell. The adjusted difference and ORPA columns are separate quantities and are not comparators for this candidate.

Printed inputs: 557/688 (81.1%). Direct source image confirms these values.

Reproducible rule and calculation: an unadjusted percentage accompanying exact integer No./Total is100×557/688=80.95930232558139%. Rounded to one decimal, the value is81.0%. The printed81.1% differs by0.14069767 percentage points. One-decimal tolerance is±0.05percentage points, inclusive at ties. The value lies outside that interval.

Direct observation versus inference: the fraction and percentage coexist in the source; their mathematical incompatibility under the column’s stated No./Total interpretation is observed and reproduced. Which input produced the mismatch is unknown.

Alternatives: a different denominator, a different numerator, a weighted/adjusted percentage or a transcription problem could explain the display. The table supplies no alternative percentage definition, and footnote a is attached to the adjusted difference/ORPA columns. Do not infer a correction.

Quality-control relevance: the cell supplies inconsistent raw count/proportion inputs for downstream extraction. The absolute difference is small and does not establish an effect on the trial conclusion.

Exact human question: “Does the control antidiabetic medication entry refer to557 of688 patients, and if so what explains its reported81.1% rather than the proportion implied by those printed integers?”

No classification adjudication or stable C ID is assigned.

## NUMSUP-05 — Seven-measure example versus nine listed measures in PLAN

Relationship: N520, corroborating count N512. Proposed category: Numeric or arithmetic inconsistency.

Compared locations and roles: PLAN [DOC-002 PDFp19,lines276–279](../../../joi180070supp1_prod.pdf#page=19) says “eligible for5 of the7 performance measures,” followed by3 outcome1 and2 outcome0 observations. PLAN [PDFp13,Table2](../../../joi180070supp1_prod.pdf#page=13) and [PDFp14,Table2 continuation](../../../joi180070supp1_prod.pdf#page=14) list four acute and five discharge performance measures. PLAN Table3 pp14–15 specifies the same nine measures. All compared content belongs to the bound prospective protocol.

Printed inputs and reproducible rule: example total7; enumerated actual list4+5=9. The stated total differs by2 measures, with zero tolerance for an integer inventory. Separately5=3+2 is coherent, and neither five observations nor3/5 compliance is itself inconsistent.

Direct observation versus inference: the two total measure counts7 and9 are directly printed/enumerated. Treating “the7 performance measures” as the specified trial measure universe is an interpretation of definite wording; it is not proof that any actual analysis used7 measures.

Alternatives: the passage may intentionally illustrate a hypothetical seven-measure setting, may refer to an undocumented seven-measure subset, or may retain earlier example wording. An illustration of the opportunity-level model does not necessarily determine the actual trial denominator.

Quality-control relevance: the wording may mislead reconstruction of the specified composite opportunity universe even though the binary arithmetic is correct. This observation is restricted to the PLAN text and does not assert any effect on reported trial estimates.

Exact human question: “Does the p19 seven-measure example intentionally describe a hypothetical or particular subset, or should its named total be reconciled with the nine predefined measures listed in Tables2–3?”

No classification adjudication or stable C ID is assigned.

## NUMSUP-06 — Sensitivity lipid-lowering label differs from supplied eligibility definition

Relationship: N566 with N536 specification. Proposed category: Measure, label, or scale inconsistency.

Compared locations and roles: REPORT [DOC-003 PDFp8,eTable4](../../../joi180070supp2_prod.pdf#page=8), row “Lipid-lowering for LDL>100mg/dL” with1415/1517(93.3%) versus1439/1586(90.8%). REPORT [PDFp3,eTable1](../../../joi180070supp2_prod.pdf#page=3), row “LDL100 or Not Documented,” defines the measure for LDL≥100mg/dL, prior lipid-lowering treatment, or LDL not documented. Both locations are within the same non-plan results supplement.

Printed inputs and reproducible rule: >100 and≥100 are unequal eligibility sets because exactly100 satisfies only the latter. Prior treatment and undocumented LDL also broaden the specified set beyond a simple measured LDL>100 threshold. No rounding tolerance applies to this label comparison. The printed denominators1517/1586 are not reproducible from supplied patient-level LDL/prior-treatment/missingness data.

Direct observation versus inference: the inequality and omitted eligibility alternatives are directly observable differences in the supplied label/definition. It is not known whether the sensitivity calculation actually used a narrower set or whether the row title is an abbreviated label for the defined measure.

Alternatives: the shortened title may name the broader prespecified measure, or sensitivity analysis may use a specific variant not separately documented in the footnote. The overall-population sensitivity includes contraindicated patients; that fact alone does not resolve the exactly100/prior-treatment/undocumented eligibility set.

Quality-control relevance: the printed label could lead extraction of a different eligible subgroup or threshold. This is distinct from NUMSUP-03, which concerns only the control count/percentage arithmetic. Do not infer that any particular patient was excluded or included incorrectly.

Exact human question: “Does the eTable4 lipid-lowering denominator include LDL exactly100mg/dL, prior lipid-lowering therapy and undocumented LDL as eTable1 specifies, and what eligibility scope is intended by the >100mg/dL row label?”

No classification adjudication or stable C ID is assigned.

## Completion record

All68 support relationships N501–N568 complete;58 percentage cells explicitly recalculated, including all18 sensitivity cells. Six distinct document-grounded candidates are emitted above. Four are same-cell reported percentages, one is PLAN measure-universe wording, one is REPORT measure eligibility labeling. All source roles are assigned by content. Interpretation alternatives are preserved for human review. No supplied or reusable asset was modified.

