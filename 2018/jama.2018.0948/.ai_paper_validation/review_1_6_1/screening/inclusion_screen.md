# Independent initial inclusion screen

Scope complete: every finding in checkers/numeric_consistency.md, checkers/cross_source_consistency.md and checkers/statistical_pass_1.md. The numeric checker supplied no finding; the cross-source checker supplied F-XS-001 and statistical pass 1 supplied F-ST1-001. Two findings were independently screened and consolidated into one included SCDE endpoint-definition issue. No finding was screened out. Coordinator registered the consolidated issue as C001.

Read completely: START_PROMPT.md, QUALITY_CONTROL_SCOPE.md, workflow_1_6_1/review_contract.md and all three assigned checker artifacts. Direct source confirmation used Poppler pdftotext 25.03.0 native/layout output from the supplied PDFs; source-matched reusable rendered images of protocol p.24 and results supplement p.6 provided additional visual confirmation of conjunctions and component boundaries. The tooling follows tooling_record.md. No old scientific conclusions, external evidence, Python scientific orchestration or source modifications were used.

| Finding ID | Source checker | Screening stage | Decision | Reason code | Candidate ID |
|---|---|---|---|---|---|
| F-XS-001 | cross_source_consistency_reviewer | initial | INCLUDE | MEETS_THRESHOLD | C001 |
| F-ST1-001 | statistics_pass_1 | initial | INCLUDE | MEETS_THRESHOLD | C001 |

F-XS-001: The directly reproduced protocol conjunction versus reported disjunction changes the operational eligibility definition of the named key secondary composite and its extraction, while neither the same-page protocol context nor the report reconciles those predicates.

F-ST1-001: The same circulatory discrepancy and the independently reproduced addition of first-hour ICU deaths form a broader reported SCDE eligibility definition whose relationship to the protocol-defined composite is not reconciled by immediate context, so this finding is included in the same endpoint-definition issue while retaining both components.

## Consolidation group and retained evidence

Consolidation group: **SCDE endpoint eligibility, protocol versus report**. F-XS-001 and F-ST1-001 share the same protocol Table 5, reported definition, key secondary event totals and extraction question; registering another issue for their shared circulatory comparison would duplicate the evidence. The included issue retains two explicitly distinguished eligibility components below, rather than treating the added death window as a numerical increase in observed events. No independent numerical rule failure or separate affected result has been demonstrated.

Proposed review domain: protocol_report. Primary relationship type: P_R. All relationships: P_R. The prospective protocol is PLAN by content; the published article and non-plan results supplement are REPORT by content. The two REPORT documents agree on permitting either circulatory therapy and on the first-hour ICU death component, so their corroboration does not add S_C. The SAP is PLAN but supplies no competing SCDE eligibility definition; it is contextual support and is not another conflicting relationship. Focus area: D, planned versus reported key secondary endpoint definition. Classification ambiguity: whether a dated endpoint amendment or an operational definition reconciles the supplied protocol with the report is not established in the package.

### Circulatory component assessed independently

- PLAN [protocol physical p.24, Table 5 category 4](../../../joi180015supp1_prod.pdf#page=24) requires greater than 60 mL/kg intravenous/intraosseous fluid in the preceding 12 hours **and** an intravenous/intraosseous inotrope or vasopressor at transfer or in the preceding 12 hours; the SCDE column marks category 4 Yes and category 5 combines respiratory and circulatory support.
- PLAN [protocol physical p.10, main secondary outcome](../../../joi180015supp1_prod.pdf#page=10) identifies SCDE as the main secondary composite and directs the reader to Table 5; its general reference to significant respiratory or circulatory therapies does not replace category 4's explicit internal conjunction.
- REPORT [results supplement physical p.6, eTable 1 component b](../../../joi180015supp3_prod.pdf#page=6) uses the same fluid/drug windows but prints **and/or**.
- REPORT [main article physical p.4, Study Outcomes](../../../jama_parshuram_2018_oi_180015.pdf#page=4) defines a composite of one or more components and separately lists administration of vasoactive medication **or** provision of qualifying fluid boluses.

Holding the fluid threshold away from its boundary, let F denote qualifying fluid and V qualifying vasoactive medication. Protocol circulatory eligibility is F AND V; reported circulatory eligibility is F OR V. A fluid-only or vasoactive-only event satisfies one predicate and not the other. Other composite components can overlap, so the comparison does not establish an observed event-count change. It does reproduce a substantive eligibility-rule discrepancy; rounding, typography, a model-versus-crude comparison and a field-resolvable synonym do not explain the different conjunctions.

All four inclusion criteria hold: the predicates are directly reproduced; the key secondary endpoint definition is within focus D and an eligible comparison tier; no cited immediate context selects a reconciled protocol-to-report rule; and an extractor's component definition attached to the SCDE estimate can change. The issue is the endpoint specification, not the absence of patient-level component data. Any claim that a fluid-only or drug-only event actually contributed to the printed counts would be conditional and is not retained.

### Death location/window component assessed independently

- PLAN [protocol physical p.10, main secondary outcome](../../../joi180015supp1_prod.pdf#page=10) specifies death without DNR on an inpatient ward.
- PLAN [protocol physical p.24, Table 5 category 7](../../../joi180015supp1_prod.pdf#page=24) specifies death on an inpatient ward without DNR and explicitly says no transfer from the ward area; category 6 separately permits chest compressions or ECMO within one hour of PICU admission.
- PLAN [protocol physical p.11, clinical deterioration scale context](../../../joi180015supp1_prod.pdf#page=11) lists intubation, cardiopulmonary resuscitation and mechanical circulatory support in the first hour after ICU admission, while describing death prior to transfer; it does not explicitly add post-transfer death to category 7.
- REPORT [results supplement physical p.6, eTable 1 component d](../../../joi180015supp3_prod.pdf#page=6) explicitly adds death within one hour of urgent ICU admission to ward death without DNR; it also permits pronouncement without cardiopulmonary resuscitation when there was intent to perform it.
- REPORT [main article physical p.4, Study Outcomes](../../../jama_parshuram_2018_oi_180015.pdf#page=4) separately includes death within the first hour of ICU admission.

Let W denote qualifying ward death and I qualifying first-hour post-urgent-ICU-admission death. The printed death component changes from W to W OR I. This is a directly observed location/window change, irrespective of whether observed I events also met another component. Complete overlap cannot be selected from immediate context: protocol category 6 requires chest compressions or ECMO, and the report's death component expressly allows pronouncement without CPR; the package does not state that every early ICU death received intubation or another qualifying treatment. No assumed patient's existence or unreported numerical increase is needed to compare the supplied endpoint definitions.

All four inclusion criteria hold at definition level: ward-only versus ward-or-first-hour-ICU is reproduced; this is a key secondary endpoint window in focus D; immediate context neither removes the added explicit component nor reconciles it with protocol category 7; and it changes the component definition an extractor records with the reported SCDE result. The cross-source checker's exclusion of a proposed numerical consequence as conditional is compatible with retaining no numerical consequence, but does not resolve the directly reproduced eligibility-definition comparison itself.

### Affected result and all matching report locations

The retained extraction question concerns the endpoint definition attached to 386 intervention-period significant clinical deterioration events: 127 events/251,859 patient-days at BedsidePEWS hospitals versus 259/307,584 at usual-care hospitals, rates 0.50 versus 0.84 per 1000 patient-days, adjusted rate ratio 0.77 (95% CI 0.61–0.97), P=.03. The separately fitted absolute difference is −0.34 (95% CI −0.73 to 0.05) per 1000 patient-days; Table 3 explicitly identifies its baseline-adjustment exception, so that ratio/difference distinction is not part of the retained issue.

All checker-cited affected locations were reread directly and retained: REPORT [abstract physical p.1](../../../jama_parshuram_2018_oi_180015.pdf#page=1), REPORT [secondary-result narrative physical p.6](../../../jama_parshuram_2018_oi_180015.pdf#page=6), REPORT [Table 3 SCDE row and estimator footnotes physical p.7](../../../jama_parshuram_2018_oi_180015.pdf#page=7), REPORT [discussion physical p.9](../../../jama_parshuram_2018_oi_180015.pdf#page=9), and REPORT [eTable 3 SCDE column and aggregate rows physical p.11](../../../joi180015supp3_prod.pdf#page=11). These results agree numerically across matched locations; the candidate concerns their endpoint definition, not their repeated counts or estimates.

Source-grounded alternatives remain: a prospective amendment may have reconciled both reported components; the report may state the consistently applied operational definition; or overlapping components may have left observed event totals unchanged. The supplied package does not identify an amendment date or component-level mapping that selects among those alternatives. The question for human review is which circulatory predicate and death location/window classified the reported SCDE events and how that operational definition relates to the supplied protocol. No preferred endpoint, revised event count or revised effect estimate is proposed.

The greater-than versus at-least 60 mL/kg boundary wording is outside the retained candidate scope: it is an isolated threshold wording difference readily interpreted in the field and remains screened out under TERMINOLOGY_OR_WORDING, consistent with the checker catalogue. This ancillary observation is not an additional finding and does not add a row to the screening table.

## Counts and limits

Finding rows: 2. INCLUDE rows: 2. Consolidated included issues: 1. SCREENED_OUT finding rows: 0; every permitted screened-out reason code therefore has count 0. The numeric checker supplied 0 findings, so it has no screening row. Every supplied finding has exactly one initial decision; candidate ID assignment belongs to the coordinator.

No cited-source access or transcription gap remains. Component counts, overlaps, operational classification records and a dated endpoint amendment are not supplied; numerical consequences cannot be determined. These limits are retained explicitly and do not become additional candidates. Proposed domain/relationship fields are screening recommendations for subsequent source recheck and audit, not human adjudications.
