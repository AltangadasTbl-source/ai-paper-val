# Cross-Source Consistency Review

## Scope, evidence boundary, and method

This is a complete fresh-evidence cross-source review of DOC-001 through DOC-004: the main article (`jama_parshuram_2018_oi_180015.pdf`, pp. 1-11), protocol (`joi180015supp1_prod.pdf`, pp. 1-37), analysis plan (`joi180015supp2_prod.pdf`, pp. 1-7), and Supplement 3 (`joi180015supp3_prod.pdf`, pp. 1-14). Native and layout PDF text, current rendered-page confirmations where needed, and the fresh mapper/relationship inventories were used. No legacy audit output, web material, or external source was used. There are no supplied Office, workbook, CSV, or other structured-data sources.

Before comparing values, this checker aligned population, period, contrast, model, measure, scale, unit, reference group, analysis set, and displayed precision. Planned protocol quantities were not treated as conflicting with completed-trial quantities solely because the trial changed through enrollment, attrition, implementation, or the finalized analysis plan.

All relationships in `relationships/numeric_relationship_inventory.md` (N001-N088) and `statistics/relationship_inventory.md` (S001-S045) were considered. The coverage record below names the matching route or reason an exact cross-source match is not applicable.

## Complete relationship coverage and matched-result record

| Relationship IDs | Evidence surfaces compared | Alignment and outcome |
|---|---|---|
| N001-N004; S001-S003 | DOC-001 abstract/methods/analysis versus DOC-002 trial frame and DOC-003 analysis specifications | Same cluster trial, intended population, outcome families, rate units, and hospital-level framework. DOC-002's 22 planned sites versus DOC-001's 21 completed sites is explained by planned allowance for 1-2 attritions; it is not a same-analysis-set value. No qualifying difference. |
| N005-N012; S004-S007 | DOC-001 Table 2/narrative/abstract versus DOC-004 eFigure 2 and DOC-003 continuous-outcome model definitions | Documentation sample totals (1,270, 2,588, 1,419, 2,832; total 8,109/8,190) and seven-item measurement construct align. The five recited Table 2 effects and the >=5-item result (38.1%, 95% CI 20.8%-55.4%) match the narrative; the figure is a distribution display and has no competing estimate. No qualifying difference. |
| N013-N017 | DOC-001 Figure 1, Table 1, Results, and DOC-004 eTables 2-3 | Baseline/intervention hospital counts, discharges, and patient-days agree after separating the two nonimplementing BedsidePEWS sites from the 21-hospital completed analysis set. All displayed group totals agree with Supplement 3. No qualifying difference. |
| N018-N023; S004-S007 | DOC-001 Table 2, narrative, caption/footnotes, DOC-003 model plan, DOC-004 eFigure 2 | Mean-difference direction, confidence intervals, population, 24-hour measurement window, and item scale are aligned. Raw displayed means are not substituted for GEE adjusted difference-in-change values. No qualifying difference. |
| N024-N037; S008-S018 | DOC-001 abstract, Results, Tables 3/footnotes, Figure 2/caption, narrative and DOC-004 eTables 1-5 | Main primary mortality (1.93 vs 1.56 per 1,000 discharges; adjusted difference 0.01, OR 1.01), SCD (0.50 vs 0.84 per 1,000 patient-days; RR 0.77), event counts/rates, urgent-ICU analysis, and post-trial assumptions reproduce in their matched supplement locations. ICU-discharge, hospital-discharge, patient-day, and patient-level measures were kept distinct. No numeric conflict. One definition conflict is recorded below. |
| N038-N076; S019-S035 | DOC-002 repeated protocol narrative, tables, appendices, and DOC-001/DOC-003/DOC-004 completed-trial descriptions | Most protocol statements are planned definitions, assumptions, or background evidence and are not same-result comparators to final results. The final protocol, SAP, and main report identify distinct final model families. Three internally repeated protocol definition/unit discrepancies are qualifying candidates below; remaining planned-versus-final differences are not candidates. |
| N077-N080; S036-S044 | DOC-003 SAP versus DOC-001 analysis and DOC-004 table notes | Binary/count/continuous model families, clustering, offsets, analysis units, and ICU per-patient construction are comparable at the stated level. The SAP's displayed code is not used to recalculate adjusted values. Its apparent offset-expression formatting issue cannot establish a different executed model from supplied evidence and is not a candidate. |
| N081-N088; S045 | DOC-004 definitions, figures, eTables 2-5 versus DOC-001 results/tables and DOC-002 protocol | Mortality and SCD matrices, hospital labels, counts, denominators, rates, adjusted ICU estimates, and anticipated/actual summary values agree with corresponding main-paper values at printed precision. Supplement 3's SCD definition instead matches DOC-002's `>60 mL/kg` threshold, not DOC-001's `60 mL/kg or greater`; this is Candidate CS-01. |

### Explicit no-match/not-comparable scopes

- DOC-002 pp. 2-6, 18-23, 25-27, and 31-37 include background performance evidence, search material, implementation detail, forms, or references. They have no same-population completed-trial-result counterpart.
- DOC-003 pp. 1-7 provides models, transformations, sensitivity-analysis options, and code. It has no additional observed result table, so it cannot supply a second printed estimate for most S001-S018 or S045 relationships.
- Figure 2/eFigure 1 circle coordinates and eFigure 2 histogram bins are visual descriptive displays; they do not give alternative adjusted estimates for Table 3/Table 2 outcomes.
- No displayed `P = 0`, `p = 0.000`, or equivalent was found. Protocol Table 2's `<.0001` is a threshold display, not a display-zero issue and not a candidate basis.

## Qualifying candidate consistency issues

The records below are provisional quality-control candidates only. They have no stable C IDs and require human adjudication.

### CS-01 — SCD fluid-volume threshold differs between the main report and supporting definitions

- **Category:** Measure, label, or scale inconsistency.
- **Exact locations:** DOC-001 [main Methods, PDF p. 4](jama_parshuram_2018_oi_180015.pdf#page=4); DOC-004 [eTable 1, PDF p. 7](joi180015supp3_prod.pdf#page=7); DOC-002 [Table 5, PDF p. 24](joi180015supp1_prod.pdf#page=24).
- **Direct observations:** DOC-001 defines a significant clinical deterioration event using “fluid boluses of **60 mL/kg or greater** within the 12 hours before ICU admission.” DOC-004 eTable 1 defines the same Late ICU Admission/SCD component as “**>60 ml/kg**” in the preceding 12 hours. DOC-002 Table 5 also prints `>60ml/kg` for its circulatory category and `<60ml/kg` for early transfer.
- **Comparator and rule:** These documents describe the same SCD/Late ICU Admission measure, population without preceding DNR, 12-hour pre-transfer window, and fluid-resuscitation component. `>=60` includes an exactly 60 mL/kg exposure; `>60` excludes it.
- **Derived inference:** If any reviewed event had exactly 60 mL/kg fluid exposure and no other qualifying component, SCD classification could depend on which printed definition was used. The package does not report boundary-case counts, so no numerical outcome impact is inferred.
- **Supported alternatives:** DOC-001 could intend `>60 mL/kg`, as in both support documents; alternatively DOC-002/DOC-004 could omit the inclusive boundary used in the main report.
- **Human verification question:** Which threshold was implemented for SCD adjudication, and should all three documents state the same inclusive/exclusive rule?

### CS-02 — Protocol appendix states a mortality absolute reduction on an incompatible percent scale

- **Category:** Cross-document numeric inconsistency.
- **Exact locations:** DOC-002 [protocol p. 1](joi180015supp1_prod.pdf#page=1), [protocol p. 14](joi180015supp1_prod.pdf#page=14), and [Power & Sample Size Appendix p. 29](joi180015supp1_prod.pdf#page=29); corroborating final planned-value description: DOC-001 [Methods, PDF p. 4](jama_parshuram_2018_oi_180015.pdf#page=4).
- **Direct observations:** DOC-002 p. 1 states that 22 hospitals permit an absolute reduction of “**0.9 deaths/1000 hospital admissions**,” equal to an 18% relative risk reduction at baseline `5.1/1000`. DOC-002 p. 14 states the corresponding absolute difference as `0.09%` (and `0.9/1000`). DOC-002 p. 29 states that the same 18% relative risk reduction “corresponds to an absolute risk reduction of **0.9%**.” DOC-001 prints `0.9 per 1,000 hospital discharges` in its sample-size description.
- **Comparator and rule:** `0.9 per 1,000 = 0.0009 = 0.09%`; it is not `0.9%`. Also, `5.1/1,000 × 0.18 = 0.918/1,000`, consistent with the p. 1/p. 14/DOC-001 rounded quantity, not with 0.9%.
- **Derived inference:** Under the explicitly repeated baseline and relative reduction, the p. 29 percent sign represents a ten-fold scale difference from the other printed versions. This is a planning-quantity reporting-unit inconsistency, not an observed mortality-result discrepancy.
- **Supported alternatives:** The p. 29 text may have intended `0.09%` or `0.9 per 1,000`; a different baseline/quantity is not supplied on that page.
- **Human verification question:** Was p. 29 intended to say `0.09%` (equivalently 0.9 per 1,000), and should the appendix use the same unit as the protocol and final paper?

### CS-03 — Protocol uses incompatible Children’s Resuscitation Intensity Scale labels for cardiac-arrest documentation

- **Category:** Measure, label, or scale inconsistency.
- **Exact locations:** DOC-002 [protocol p. 11](joi180015supp1_prod.pdf#page=11), [Table 5, protocol p. 24](joi180015supp1_prod.pdf#page=24), and [Table 6 legend, protocol p. 27](joi180015supp1_prod.pdf#page=27).
- **Direct observations:** DOC-002 p. 11 says cardiac arrest without preceding DNR is “rated as **6 or 7** on the Children’s Resuscitation Intensity Scale.” Table 5 assigns cardiopulmonary resuscitation to category 6 and death to category 7. The Table 6 legend instead calls clinical-deterioration events that include a cardiac arrest “**scale rating 4 or 5**.”
- **Comparator and rule:** All statements identify the same named seven-point scale and cardiac-arrest event documentation. On supplied Table 5, ratings 4-5 describe circulatory/late-transfer categories, whereas cardiac arrest/death is 6-7. No alternate 4-5 scale is identified.
- **Derived inference:** The p. 27 legend's `4 or 5` labels do not reconcile with the protocol's cardiac-arrest scale definition. This could select or describe a different case subset if used operationally.
- **Supported alternatives:** The legend may contain a scale-number transcription error; it could refer to an unstated, different abstraction scale, although no such scale is supplied.
- **Human verification question:** Does the Table 6 legend intend `scale rating 6 or 7`, or was it referring to a separately defined scale that should be named?

### CS-04 — Protocol preventability threshold says `>4` but includes rating 4 and is contradicted by its table legend

- **Category:** Measure, label, or scale inconsistency.
- **Exact locations:** DOC-002 [protocol p. 11](joi180015supp1_prod.pdf#page=11) and [Table 7, protocol p. 28](joi180015supp1_prod.pdf#page=28); final implementation comparison: DOC-004 [eTable 1, PDF p. 8](joi180015supp3_prod.pdf#page=8) and DOC-001 [Table 3 footnote, PDF p. 7](jama_parshuram_2018_oi_180015.pdf#page=7).
- **Direct observations:** DOC-002 p. 11 says events with consensus rating “**at >4**” will be potentially preventable, then immediately says ratings **4, 5, and 6** will be deemed potentially preventable. DOC-002 Table 7 says a rating of “**4 or more**” is high preventability. DOC-004 defines ratings 4, 5, and 6 as potentially preventable; DOC-001 says rating 4 indicates more than likely preventable and reports the resulting outcome.
- **Comparator and rule:** On a six-point ordinal scale, `>4` means 5 or 6, while `4 or more` means 4, 5, or 6. The p. 11 text cannot use `>4` and include 4 under ordinary inequality notation.
- **Derived inference:** The protocol threshold wording conflicts with both its listed qualifying ratings and the final main/supplement definition. The sources do not identify how many events had rating 4, so effect on reported counts is not inferred.
- **Supported alternatives:** `>4` may be typographic notation intended to mean `>=4`; alternatively the listed rating 4 and Table 7/final definition could be incorrect.
- **Human verification question:** What threshold was applied to adjudication data, and should the protocol specify `rating 4 or more` if it was the rule reported in the final article and supplement?

## Non-candidate cross-source observations

- The protocol's 22-site plan, 23 randomized sites, and 21 completed sites describe different trial stages and are explicitly compatible with planned attrition; they are not competing population totals.
- Planned weighted logit/Poisson/linear analyses and finalized GEE analyses differ in implementation details, but no two estimates are presented as from the same model. No model-label candidate is emitted.
- DOC-003's apparent placement of terms inside an offset expression is a code/prose formatting ambiguity. Without executed code or a conflicting reported final model, it does not establish a reproducible cross-source inconsistency.
- DOC-002's 1,052 urgent-ICU-admission reference data are described as annual in planning context and as two-year aggregate source data in the appendix. The supplied denominators/period do not identify whether this is annualization shorthand or an error; no same-result numerical comparison can be made.

## Completion summary

- Direct-source scope reviewed: DOC-001 pp. 1-11, DOC-002 pp. 1-37, DOC-003 pp. 1-7, and DOC-004 pp. 1-14 (69/69 PDF pages).
- Relationship coverage: N001-N088 (88/88) and S001-S045 (45/45), with matchability/no-match status recorded above.
- Qualifying provisional cross-source candidates: 4 (CS-01 through CS-04).
- No stable candidate IDs, severity, verification status, disposition, or final correction is assigned.
- Limitation: No event-level data or adjudication manual is supplied to resolve boundary cases or confirm implemented protocol wording. Every candidate remains pending human adjudication.
