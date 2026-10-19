# C007 focused source recheck

Scope: C007 only; all registered affected locations, plus the primary Table 2 comparison and the detailed non-response-weighting explanation. Prior artifacts and sources preserved. Status remains Pending Human Adjudication.

## Finding and bounded interpretation

C007 concerns the hierarchy assigned to missing-data analyses. The SAP retains an initial primary-analysis statement based on observed follow-up and a missing-at-random (MAR) assumption, while the report presents pattern-mixture imputation plus inverse-probability/non-response weighting as primary and complete-case analysis as sensitivity. However, the same final SAP contains a conditional pattern-mixture/IPW first approach and a dated amendment explicitly adding IPW. These provisions substantially support the reported implementation. The remaining question is how the retained primary/MAR statement and the conditional amended approach were intended to determine the primary-versus-sensitivity hierarchy. This is not evidence of an undisclosed or unauthorized change, and the follow-up-only analysis is not absent from the report.

## Exact supplied-source locations and key text

Links below are relative to this artifact, with PDF page numbers.

| Location | Role by content | Matched key text or displayed content | Recheck significance |
|---|---|---|---|
| [SAP PDF p.19, section 11](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19) | PLAN | “For the primary analyses, we will analyze those patients who have follow-up data.” The next sentence states that missing data will be assumed MAR given baseline adjustment. | The retained primary-analysis/MAR wording is present. |
| [SAP PDF p.19, same section](../../../joi250046supp2_prod_1755300121.15087.pdf#page=19) | PLAN | Sensitivity analyses are contemplated for “>15% missing outcome follow-up at 3 months or differential missingness by group.” It then states: “Our first approach will apply a pattern mixture imputation missing data approach that relaxes the MAR assumption”, with IPW for those missing every follow-up. | The final SAP also explicitly contains the approach used in the report. This is a substantive alternative interpretation to a simple primary-analysis replacement claim. |
| [SAP PDF p.4, amendment dated 07/17/24](../../../joi250046supp2_prod_1755300121.15087.pdf#page=4) | PLAN | “Added inverse probability of missing weights (IPW) to address missing data for those missing all time points.” It explains that adding IPW permits interpretation among all randomized participants rather than only those with some follow-up. | An explicit amendment supports IPW. Its rationale refers to 12.1% missing all outcomes; this historical proportion must not automatically be equated to the final report's 12.7%. |
| [SAP PDF p.4, amendment rationale](../../../joi250046supp2_prod_1755300121.15087.pdf#page=4) | PLAN | The amendment says the addition was proposed by the masked biostatistician, who had no access to outcome data or treatment-arm data summaries at the time. | The supplied material itself documents masking. It does not support an explanation based on selecting a favorable treatment result. |
| [Main article PDF p.4, journal p.595](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=4) | REPORT | “Missing outcome data for the primary analysis were addressed in 3 ways”: prespecified adjustment, nonignorable pattern-mixture imputation among those with some follow-up, and inverse-probability weighting for those with no follow-up. | Confirms the reported primary specification. |
| [Results supplement PDF p.4, Missing Data](../../../joi250046supp4_prod_1755300121.15587.pdf#page=4) | REPORT | The opening says the study met the SAP's prespecified criteria for the primary analysis to use MNAR imputation with non-response weighting and regression adjustment. It reports primary-outcome completeness at 3 months of 77.1% overall (UC 79.9%, PT 69.8%, HC 81.6%). | Both the >15% missingness condition and differential missingness are supported by the displayed values. |
| [Results supplement PDF p.5, Non-Response Weighting](../../../joi250046supp4_prod_1755300121.15587.pdf#page=5) | REPORT | “we added non-response weighting which we formally incorporated into the SAP”; the next paragraph calls this the “primary weighted analysis”. | Corroborates an acknowledged SAP incorporation rather than an undisclosed addition. |
| [Results supplement PDF p.9, eTable 4](../../../joi250046supp4_prod_1755300121.15587.pdf#page=9) | REPORT | Heading: “Summary of primary estimation model fit to imputed data with weighting.” Three-month RRs are PT/UC 1.28 (1.06, 1.55), HC/UC 1.54 (1.30, 1.82), HC/PT 1.20 (1.03, 1.40). | Confirms which model generated the primary estimates. |
| [Results supplement PDF p.11, eTable 7 and preceding paragraph](../../../joi250046supp4_prod_1755300121.15587.pdf#page=11) | REPORT | The sensitivity introduction lists complete-case analysis. Its first block is labeled “Complete-case analysis: Adjusted GEE without imputation or weighting”, with n=1,798 at 3 months (UC 621, PT 542, HC 635). | Confirms observed-follow-up/complete-case results are supplied as sensitivity, rather than missing. |
| [Main article PDF p.9, journal p.600, Table 2 primary row](../../../jama_debar_2025_oi_250046_1755300121.13587.pdf#page=9) | REPORT | The three-month pain-severity RRs match eTable 4: 1.28 (1.06–1.55), 1.54 (1.30–1.82), 1.20 (1.03–1.40). | Corroborates the primary-result identity; no report-versus-supplement numeric discrepancy is asserted. |

## Mechanical recheck record

| Required field | C007-specific fact |
|---|---|
| Location found | All six registered locations found: main p.4; SAP pp.4 and 19; results supplement pp.4, 9 and 11. Results p.5 and main p.9 additionally inspected. |
| Source text matched | Primary follow-up/MAR wording, amended conditional pattern-mixture/IPW wording, reported primary MNAR/IPW specification, and complete-case sensitivity labeling all matched. |
| Comparator matched | The registered comparator is the retained primary/MAR statement, not an assumed absence of IPW from the SAP. |
| Consistency rule applicable | Focus D: planned-versus-reported primary analysis and missing-data hierarchy. The ambiguity also spans retained versus amended PLAN statements. |
| Logical comparison reproduced | Different primary/sensitivity labels remain visible, while explicit amendment and conditional implementation language support the reported approach. Evidence supports a hierarchy-clarification question; it does not establish that IPW was unplanned. |
| Display-precision interval check | Not applicable to the registered textual hierarchy comparison. The different model estimates below are not copies of one quantity under an identical analysis and are not tested as an arithmetic inconsistency. For CI interpretation, two-decimal half-unit intervals cannot move the primary HC/PT lower limit 1.03 to 1 (1.025–1.035), or the complete-case limits 0.94 and 1.29 to a wholly one-sided interval (0.935–0.945 and 1.285–1.295). |
| Necessary inputs available | Enough source text is available to establish the hierarchy ambiguity and amendment alternative. Primary and complete-case RRs/CIs are available for a bounded downstream comparison. |
| Exact missing inputs or definitions | A definitive statement of which primary/sensitivity clause takes precedence after the SAP amendment, and the original implementation decision record. Individual data and analysis code, matched covariate/model specifications, and intermediate results would be needed to isolate effects of weighting versus imputation or other model differences. |
| Source-grounded alternative | The final conditional pattern-mixture/IPW first approach, triggered by the observed missingness, governed the primary analysis; the earlier primary/MAR sentence was retained without a revised hierarchy label. |
| Direct observation versus inference | Direct: all labels, amendment, masking explanation, estimates and intervals cited above. Inference: the residual issue is a hierarchy ambiguity. Neither a result-driven switch nor its absence can be established from these texts alone. |
| Exact remaining human question | After the July 17, 2024 amendment and the missingness trigger, was pattern-mixture/IPW intended to replace the initial follow-up/MAR analysis as primary, with complete-case retained as sensitivity, and where is that hierarchy explicitly documented? |
| Evidence state | reproduced. The determining fact is that the retained primary/MAR statement and report's primary MNAR/IPW versus complete-case sensitivity designation remain differently labeled, while the amendment is recorded as a substantial explanatory alternative. |

## Classification confirmation

- SAP pp.4 and 19 are PLAN by their prospective analysis/amendment content. Main article and results supplement are REPORT by their actual-analysis and results content.
- Primary relationship: P_R. All relationships: P_R, P_P. Review domain: protocol_report. P_R takes precedence because reported hierarchy is compared with the retained plan hierarchy. P_P concerns the retained primary/MAR wording versus the same plan's conditional first approach and amendment; it does not arise merely because a plan corroborates a report.
- Classification ambiguity: the final amendment/conditional branch may substantively reconcile the implementation; the residual wording/hierarchy question does not imply noncompliance. No classification field is changed in the preserved ledger.

## Downstream impact supported by the supplied results

| Three-month comparison | Primary weighted/imputed model, main Table 2 and eTable 4 | Complete-case model, eTable 7 |
|---|---|---|
| PT vs UC | 1.28 (1.06–1.55) | 1.34 (1.12–1.61) |
| HC vs UC | 1.54 (1.30–1.82) | 1.48 (1.24–1.75) |
| HC vs PT | 1.20 (1.03–1.40) | 1.10 (0.94–1.29) |

For both active treatments versus UC, the RR direction and a 95% CI wholly above 1 persist in these two reported approaches. The active-treatment comparison is more sensitive: HC/PT has a 95% CI excluding 1 in the primary model, but including 1 in complete-case analysis. Thus choosing the analysis for extraction can affect both a treatment-comparison estimate and whether its displayed interval includes the null. It does not establish which analysis should be preferred, or imply a formal test that the two model estimates differ.

The primary and complete-case analyses differ in observations, imputation, weighting, and covariate adjustment. eTable 4 lists 2,036 persons with at least one follow-up contributing to the weighted/imputed model, whose stated target is all 2,331 randomized participants; eTable 7 lists 1,798 complete cases at three months. These estimates cannot isolate IPW's effect, and are not themselves a numeric inconsistency. A meta-analysis could obtain different estimates and weights depending on which it extracts; the size or significance of a pooled change cannot be determined without that downstream dataset and analysis. Code analysis type explicitly, preserve the designated primary and sensitivity identities, and avoid combining them as independent trial results. The amendment's masking explanation is the source's statement, not an independently established historical fact.

Tooling: visual confirmation used the supplied-source page renders identified in the assigned scope, including full original-page layout. No new OCR or rendering, source mutation, or setup was performed. Direct pdftotext was unavailable, consistent with tooling_record.md; no text extraction was substituted as final visual authority. No compute-device change was made.
