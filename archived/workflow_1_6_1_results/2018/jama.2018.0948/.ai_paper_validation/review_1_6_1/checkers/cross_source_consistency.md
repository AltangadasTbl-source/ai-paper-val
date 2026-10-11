# Cross-source consistency review

Scope COMPLETE: DOC-001 REPORT, all 11 physical pages; DOC-002 PLAN, all 37 pages; DOC-003 PLAN, all 7 pages; DOC-004 REPORT, all 14 pages. Reviewed both complete evidence maps and all 110 numeric relationship groups (N001–N065 and N101–N145). No Office or structured-data source is supplied. Source roles were confirmed by content. Primary/key secondary comparisons were aligned on eligible ward population, baseline versus 52-week intervention period, intervention minus usual-care contrast, discharge versus patient-day denominators, model and displayed precision. Protocol and SAP analyses, endpoint hierarchy, covariates, strata, weights, populations, repeated admissions, missingness, power, interim/stopping rules, multiplicity and intervention timing were compared with report materials and each other. QUALITY_CONTROL_SCOPE.md and the review contract were read completely. No prior conclusions or web evidence were read.

Final authority for cited statements: direct Poppler 25.03.0 `pdftotext -layout` reads of the supplied PDFs. Complete source-matched maps were used as locators. This checker has one self-screened finding and 21 excluded observations; no C IDs or adjudications are assigned.

## Coverage and matched results

| Relationship scope | Completed comparison |
|---|---|
| N001–N026 | Entire hospital/patient flow, period sizes, sample/assessment counts and Table 1; randomized versus completed hospitals distinguished; descriptive cross-location differences screened by peripheral tier. |
| N027–N035, N062, N118 | Every Table 2 descriptive/inferential cell, matching narrative, documentation revision and supplementary histogram; frequency over 24 hours distinguished from completeness of the latest simultaneous set. |
| N036–N042, N058–N061, N103, N106–N108, N119–N124, N143–N144 | All occurrences of primary mortality and key secondary SCDE in abstract, Key Points, narrative, Table 3, hospital tables/figures and sample assumptions. Mortality 97/50173 versus 147/94366; SCDE 127/251859 versus 259/307584 reconcile across matched report locations. OR 1.01 (0.61–1.69), difference 0.01 (−0.80–0.81), P=.96 and SCDE RR 0.77 (0.61–0.97), difference −0.34 (−0.73–0.05), P=.03 match. Endpoint eligibility comparison yields F-XS-001. |
| N043–N057, N125–N142 | All remaining Table 3 and eTable 4 outcomes, captions/footnotes and matching main narrative; discharge-rate analyses separated from urgent-ICU patient analyses and modeled effects separated from crude summaries. Main urgent-ICU mortality 42/686 versus 67/967, difference −1.55 (−4.90–1.80) percentage points/P=.36 and predicted mortality 5.5% versus 4.6%, difference 0.69 (−0.54–1.92)/P=.27 match supplement. |
| N005, N060–N065, N101–N117, N119, N142–N145 | All mapped protocol/SAP specifications compared with report: population, intervention dose/duration, definitions/windows, hospital models versus individual ICU models, baseline/strata/weights, zero-event correction, sensitivities/subgroups, power/attrition, repeated admissions, discharge conventions, missingness and decision rules. No noninferiority/equivalence margin is specified; superiority/two-sided alpha .05, no interim efficacy analysis. Background/reference/administrative units inspected and distinguished from trial results. |

## Findings

### F-XS-001

**Title:** Planned and reported circulatory eligibility rules for the key secondary deterioration composite differ.

**Compared exact locations and roles:**

- PLAN [protocol p.24, Table 5, circulatory category 4](../../../joi180015supp1_prod.pdf#page=24), supported by PLAN [protocol p.10, main secondary outcome referring to Table 5](../../../joi180015supp1_prod.pdf#page=10).
- REPORT [main article p.4, Study Outcomes](../../../jama_parshuram_2018_oi_180015.pdf#page=4).
- REPORT [results supplement p.6, eTable 1, significant clinical deterioration event component b](../../../joi180015supp3_prod.pdf#page=6).
- Affected result occurrences: REPORT [abstract p.1](../../../jama_parshuram_2018_oi_180015.pdf#page=1), [secondary result narrative p.6](../../../jama_parshuram_2018_oi_180015.pdf#page=6), [Table 3 p.7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), [discussion p.9](../../../jama_parshuram_2018_oi_180015.pdf#page=9), and REPORT [eTable 3 p.11](../../../joi180015supp3_prod.pdf#page=11).

**Printed specifications:** Protocol Table 5 defines circulatory support as >60 mL/kg intravenous/intraosseous fluids in the preceding 12 hours **and** administration of an intravenous/intraosseous inotrope or vasopressor at transfer or in those 12 hours. Its SCDE column marks category 4 “Yes”; category 5 is respiratory plus that circulatory category. Report eTable 1 component b uses the same fluid amount/window and drug window but joins them with **and/or**. The main article describes one or more qualifying components and separately lists vasoactive medication **or** fluid boluses of 60 mL/kg or greater. Both report definitions therefore permit a circulatory-only event with one of the two therapies; the protocol category requires both.

**Comparison logic:** Let F denote the specified fluid criterion and V the specified vasoactive criterion, holding the eligible population, transfer and 12-hour window fixed. The protocol circulatory criterion is F AND V; the reported criterion is F OR V. For F=true,V=false or F=false,V=true, the rules differ. These are logical demonstrations, not claims that a supplied individual patient had those characteristics. No amount of display rounding changes the conjunction. This finding rests on the conjunction difference, not on whether exactly 60 mL/kg meets a greater-than threshold. The total effect cannot be recalculated from supplied aggregate data.

**Focus area:** D, planned versus reported key secondary endpoint definition.

**Proposed review domain:** protocol_report.

**Proposed primary relationship:** P_R. **All relationships:** P_R. The two REPORT definitions agree on permitting either therapy and do not independently conflict over the conjunction.

**Affected result or extracted value:** The significant clinical deterioration composite: 127 events at BedsidePEWS hospitals versus 259 at usual-care hospitals, rates 0.50 versus 0.84 per 1000 patient-days, adjusted rate ratio 0.77 (95% CI 0.61–0.97), P=.03. An extractor evaluating prespecified late-ICU-admission outcomes needs to know whether this is the Table 5 intersection composite or the reported union composite.

**Why context does not resolve it:** The operational prospective table explicitly uses a conjunction and labels that category eligible; both report definitions use a union. The broader protocol narrative says significant respiratory or circulatory therapies but directs the reader to Table 5 for the operational definition, so it does not identify which circulatory rule generated the reported 386 events. The SAP supplies count models without redefining this endpoint. The report discloses documentation/stratification changes but supplies no corresponding reconciliation of this eligibility change. Immediate context cannot establish whether the protocol conjunction was intended, whether eligibility was amended, or whether the reported definition alone describes the implemented rule.

**Supported alternatives and missing definition:** The report may describe the applied composite accurately after an endpoint-definition amendment, or the prospective table may have used a narrower conjunction than intended. Another possibility is that all counted circulatory-only events met both criteria, so counts happened to coincide; individual eligibility data establishing that are absent. These alternatives do not select a correction or predict the direction of effect.

**Human verification steps:** Check the operational case-report/adjudication definition used at sites and any dated endpoint amendment. Determine whether fluid-only and vasoactive-only deterioration qualified, and whether any reported SCDE events depended on the union rather than the intersection. Confirm which composite should be extracted as the prespecified key secondary outcome.

## Excluded observations

Each observation is listed once with exactly one scope reason code. Reconciled matching results are documented above rather than assigned findings.

| Location | Observation | Reason code |
|---|---|---|
| REPORT main pp.1–3,5–6 | Abstract 21 randomized/completed hospitals versus Figure 1 initial 23 randomized; two intervention withdrawals are explicitly shown before active implementation. The completed 21-center result population is identifiable. | CONTEXT_RESOLVES |
| REPORT main p.3 versus results supplement pp.9,11 | Individual hospital minimum/maximum discharge or patient-day ranges in flow boxes differ from some supplementary rows; aggregate primary/key secondary analysis sizes agree. | PERIPHERAL_COMPARISON |
| REPORT main p.5 Table 1 hospital staffing | Printed ICU physician categories do not exhaust every hospital, but no unreported category is established and no result-specific analysis population changes. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol pp.9–10 versus REPORT main pp.1–2 | Age/gestation endpoint wording uses <18/>37 versus ≤18/≥37. Boundary language does not establish different actual enrollment; the common pediatric/term population is immediately recognizable. | TERMINOLOGY_OR_WORDING |
| PLAN protocol pp.7–9,22–23 versus REPORT main pp.2–3,9 | Education start 3 months before run-in versus locally delivered 1–2 months before implementation; five-week run-in and 52-week exposure agree, and locally tailored preparation/extensions are explicitly described. No result quantity is unresolved. | CONTEXT_RESOLVES |
| PLAN protocol p.16/SAP pp.1–4 versus REPORT main pp.4–5 | Primary and ICU model descriptions evolved from hospital-weighted models to GEE models. Report/SAP explicitly identify GEE, baseline covariates and analysis units; absence of a separate hospital-size weight statement does not establish how weights were applied. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol p.16 versus REPORT main p.5 | Hospital-size stratification removed because only three large hospitals were available; report directly discloses the changed covariate set, so intended primary analysis is identifiable. | CONTEXT_RESOLVES |
| PLAN protocol p.16/SAP p.6 versus REPORT main p.5 | Four protocol subgroups versus two SAP subgroup specifications; report explicitly says planned subgroups are not reported. No conflicting subgroup estimate or primary-result attribution is supplied. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol p.16/SAP pp.4–5 versus REPORT main pp.4–9 and results supplement | Some planned sensitivity/model-choice results are not separately tabulated. Nonreporting alone does not reproduce a conflicting primary estimate. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol p.16 versus REPORT main pp.6–7,9/results supplement pp.6,9 | Protocol specifies mortality following DNR; report numerical analysis is clearly without DNR (42/47, OR2.05), while discussion calls a sensitivity “after DNR.” The table and result narrative identify the extractable no-DNR estimate at once; no competing after-DNR adjusted estimate is attributed to those numbers. | CONTEXT_RESOLVES |
| REPORT abstract p.1/main p.6 versus main p.7 footnote a; PLAN protocol p.16 | Broad baseline-adjustment statement versus omitted baseline for certain identity-link differences. Main p.5 describes convergence fallback and Table 3 names every exception; SCDE rate ratio still adjusts baseline. Distinct models explain the stated difference and ratio. | CONTEXT_RESOLVES |
| PLAN protocol p.16/SAP p.7 versus REPORT results supplement p.13 | ICU patients in both study periods excluded; supplement explicitly identifies 55 exclusions and per-patient aggregation consistent with SAP. No divergent matched ICU population is established. | NOT_REPRODUCED |
| PLAN protocol p.15 versus REPORT results supplement pp.6–7,12–13 | Early discharge assumption for ventilator-free days is detailed in protocol but not repeated in results footnotes; no contrary implemented rule is supplied. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol pp.1,14,29 versus REPORT main p.4/results supplement p.14 | Mortality power appendix prints absolute reduction 0.9% while summary/body imply 0.9 per1000/0.09%; baseline5.1/1000 and relative reduction18% immediately identify the intended scale. Anticipated bed totals differ but stated common power inputs identify assumptions. | CONTEXT_RESOLVES |
| PLAN SAP p.3, lines108–131 | Illustrative count-model code has syntax/variable inconsistencies; prose specifies intervention+baseline, log offset and identity time products. Treating the literal illustrative code as the executed analysis would require an unsupported assumption. | NOTATION_OR_TYPOGRAPHY |
| PLAN SAP p.5 versus PLAN protocol p.16/REPORT main p.7 | SAP shell labels readmissions Poisson while text distinguishes binary outcomes and report explicitly gives logistic odds ratios. Shell-table naming alone does not obscure which reported analysis produced the values. | CONTEXT_RESOLVES |
| REPORT main pp.4,7 versus PLAN protocol p.12/REPORT supplement p.6 | “48 hours” readmission label versus before third midnight; protocol and detailed report share the operational calendar definition, and this exploratory outcome does not change a primary/key secondary result. | PERIPHERAL_COMPARISON |
| REPORT main pp.4–5,7 versus PLAN protocol pp.10–16 | Previously specified endpoint names also appear under post hoc/exploratory analysis heading; main report distinguishes added outcomes, post hoc multiplicity adjustment and exploratory inference. No contradictory key secondary decision rule is established. | CONTEXT_RESOLVES |
| REPORT main p.8 Figure 2/results supplement pp.2–3 | Colors/line-style descriptions differ between caption and legend; supplementary hospital letters and tables identify arm and rates, and reported primary effect/direction agrees. | NOTATION_OR_TYPOGRAPHY |
| REPORT main p.4/results supplement p.6 versus PLAN protocol pp.10–11,24 | Greater-than versus at-least60mL/kg and early-ICU death wording differ. The exact boundary and whether those deaths already meet resuscitation components are not established by patient-level data; do not infer an additional numerical effect beyond the independently reproduced conjunction issue. | CONDITIONAL_OR_UNREPORTED |
| PLAN protocol pp.19–20,29–30; REPORT results supplement p.14 | Historical validation/background counts, administrative totals and rounded anticipated versus actual summaries are contextual; no conflicting matched primary/key secondary quantity remains. | PERIPHERAL_COMPARISON |

## Limitations

No scientific coverage gap. Supplied aggregates do not identify counts of fluid-only versus vasoactive-only SCDE events, individual endpoint component overlaps, exact hospital model weights/covariances, or dated endpoint amendments. The endpoint-rule discrepancy is directly reproduced; any numerical change to the event totals or treatment effect remains unquantified. Exact graphic coordinates derive from hospital tables; histogram heights are approximate visual evidence and do not substitute for unreported exact bin data. No external literature or raw-data audit was performed.
