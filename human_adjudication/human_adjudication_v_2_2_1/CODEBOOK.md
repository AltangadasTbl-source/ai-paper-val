# Codebook — v.2.2.1

Methodological option meanings are carried forward from the v.2.1.5.3 annual workbook Codebook. The original field label `Statistcal_or_numerical issue` is retained for continuity. Readiness, copying, completion, and counts are manual in Markdown.

## Applicable judgments

| Retained domain | Required | Optional |
| --- | --- | --- |
| statistical\_results | Statistcal\_or\_numerical issue; Substantiveness | Downstream impact |
| report\_internal\_inconsistency | Report-internal or planning-material inconsistency |  |
| plan\_material | Report-internal or planning-material inconsistency |  |
| protocol\_report | No additional judgment | Protocol interpretation |

Disposition and Review domain are required for every candidate, including exclude and discuss. For inactive judgment fields, leave blank or enter `not_applicable`; their effective value for comparison is `not_applicable`. An active required field cannot be blank or `not_applicable`. Active optional fields may be blank. Clear obsolete answers after changing disposition or domain. Notes are optional and remain part of the assessment comparison. Blank means unanswered or not assessed; it is distinct from an explicit uncertainty code.

## Disposition

Keep, exclude, or defer for discussion. Blank means untouched. No AI disposition is preselected. Preserve Primary at handoff; edit Checker / final during checking.

Scope: Required; all domains.

- `retain`: Retain candidate. After human review, keep this finding in the applicable review results; retaining a protocol discrepancy does not automatically confirm an issue.

- `exclude`: Do not retain. The candidate has been assessed and should not remain as a finding, for example because the apparent mismatch has a satisfactory explanation.

- `discuss`: Needs discussion. The reviewer has considered the candidate but cannot settle the disposition without further discussion. This is a decision to defer, not an untouched blank.

## Review domain

Choose the assessment branch. All four choices are available. This does not change the frozen source relationship. Confirm the AI suggestion explicitly in Primary.

Scope: Required; all domains.

- `statistical_results`: Statistical results (S\_C / S\_W). Assess reported numbers, estimates, intervals, denominators or statistical claims in the current report materials.

- `report_internal_inconsistency`: Report internal inconsistency (S\_C / S\_W). Assess inconsistencies within the main paper, within the updated supplement, or between the main paper and updated supplement. The name describes the report materials being compared; it is not restricted to nonstatistical content. Use statistical\_results when specifically judging a statistical or numerical reporting issue.

- `protocol_report`: Protocol-report (P\_R). Assess whether planned and reported conduct or analyses meaningfully differ, using the compared materials. No search for acknowledgment or reasons for changes is required.

- `plan_material`: Plan material (P\_P). Assess an inconsistency involving planning materials themselves rather than a planned-versus-reported result. The original relationship code remains unchanged.

## Complete

Use no while drafting. Primary uses primary\_done; Checker / final uses checker\_done. Reset the affected completion marker to no after edits, recheck, and mark complete again.

Scope: Required; each stage.

- `no`: Draft. This review stage is not yet confirmed complete; AI suggestions or partially filled fields do not count as completed human review.

- `primary_done`: Human reviewed; initial stage complete. This never counts as checker completion.

- `checker_done`: Second person reviewed; checker stage complete. Required discussion must also be resolved.

## Validation hint

Use the manual readiness rules in USAGE.md. Markdown does not calculate validation hints or block invalid entries.

Scope: Manual.

## Notes (optional)

Optional English context. Blank final notes do not inherit Primary notes. Use a Markdown line break or a separate labeled paragraph for long notes.

Scope: Optional.

## Statistcal_or_numerical issue

Does a statistical or numerical reporting issue exist? Example: a reported percentage conflicts with its stated numerator and denominator after checking definitions. Certainty is separate from importance.

Scope: Required; retained statistical\_results.

- `confirmed_issue`: Confirmed statistical or numerical reporting issue. The available evidence establishes a reporting issue or contradiction, even if the correct replacement value is not known.

- `probable_issue`: Probable statistical or numerical reporting issue. The evidence favors a reporting issue, but an unresolved limitation or plausible alternative prevents confirmation.

- `not_issue`: Not a statistical or numerical issue. The apparent discrepancy is consistent with a valid calculation, definition, analysis method or reporting context.

- `indeterminate`: Indeterminate. The available evidence does not support deciding whether a statistical or numerical reporting issue exists; neither confirmation nor dismissal is justified.

- `not_applicable`: Use only for an inactive judgment field or a non-retained candidate. It is not an issue verdict, missing evidence, or an unanswered applicable question. Blank inactive fields have the same effective value.

## Substantiveness

Could the issue meaningfully affect interpretation or data use? A harmless spacing typo is minor\_presentation; an ambiguous extractable effect estimate may be substantive. An issue can be confirmed yet minor.

Scope: Required; retained statistical\_results.

- `substantive`: Substantive. The issue could meaningfully change interpretation, data extraction or downstream analysis, rather than only the presentation of the result.

- `minor_presentation`: Minor or presentation only. The intended result remains clear and the issue is a small formatting, labeling or typographic problem without a meaningful change in interpretation.

- `indeterminate`: Indeterminate. There is not enough information to decide whether the issue is substantive or limited to presentation.

- `not_applicable`: Use only for an inactive judgment field or a non-retained candidate. It is not an issue verdict, missing evidence, or an unanswered applicable question. Blank inactive fields have the same effective value.

## Downstream impact

Add only useful information about later extraction or analysis. direct means the affected value itself may be extracted, not that harm has occurred. Blank is allowed and means not assessed; it is not unlikely or not\_applicable. This field does not determine temporal eligibility.

Scope: Optional; retained statistical\_results.

- `direct`: Direct extraction or analysis impact. The affected value or definition is itself an input to data extraction or subsequent analysis; this describes potential impact, not proven downstream harm.

- `possible`: Possible downstream impact. A plausible route to affecting later interpretation, extraction or analysis exists, but the connection is indirect or uncertain.

- `unlikely`: Unlikely downstream impact. The issue is unlikely to change extracted information or later analysis because the relevant result remains clear and usable.

- `unknown`: Unable to assess. The materials do not establish enough about the affected information or its likely use to judge downstream impact.

- `not_applicable`: Use only for an inactive judgment field or a non-retained candidate. It is not an issue verdict, missing evidence, or an unanswered applicable question. Blank inactive fields have the same effective value.

## Report-internal or planning-material inconsistency

Judge whether the compared materials are inconsistent and how much that matters. For report\_internal\_inconsistency, compare content within the main paper, within the updated supplement, or between those two report materials. For plan\_material, compare planning materials such as protocol versus protocol or SAP. Plan versus final report belongs to protocol\_report. Use statistical\_results when specifically judging a statistical or numerical reporting issue.

Scope: Required; retained report\_internal\_inconsistency or plan\_material.

- `substantive_inconsistency`: Substantive inconsistency. Conflicting statements, values, labels, or descriptions in the compared report or planning materials could materially change how the study, population, procedures or results are understood.

- `minor_presentation`: Minor presentation inconsistency. A real discrepancy exists, but it mainly affects presentation, including minor wording or labeling problems, and the intended meaning remains clear. Example: an imprecise label whose intended meaning is clear from context.

- `non_inconsistency`: Not an inconsistency. The statements are compatible once their definitions, populations, time points or other context are taken into account. This includes different wording with the same substantive meaning. Example: participants and study participants refer to the same group.

- `indeterminate`: Indeterminate. The available material is insufficient to establish whether the statements conflict or how important any conflict is.

- `not_applicable`: Use only for an inactive judgment field or a non-retained candidate. It is not an issue verdict, missing evidence, or an unanswered applicable question. Blank inactive fields have the same effective value.

## Protocol interpretation

Describe the compared plan and report only when useful: meaningful difference, minor presentation issue, version/timing ambiguity, no inconsistency, or indeterminate. Use minor\_presentation for a small wording problem and non\_inconsistency for equivalent wording with no actual conflict. Use the available comparison evidence; no additional search for change records or reasons is required. Blank is allowed and never blocks completion. Retained protocol differences are descriptive and excluded from temporal analysis.

Scope: Optional; retained protocol\_report.

- `substantive_difference`: Substantive difference. The compared plan and report meaningfully differ in an outcome, population, procedure, or analysis. This describes the difference; it does not establish an issue or an unjustified change. Example: the planned primary time point is 12 months but the report uses 6 months.

- `minor_presentation`: Minor presentation difference. A minor wording, labeling or presentation problem exists, but the intended planned and reported meaning or conduct remains clear. Example: an imprecise outcome label clarified by the same definition in both documents.

- `version_timing`: Version or timing ambiguity. The difference may reflect which protocol version or date is being compared; the sequence cannot be resolved from the available material.

- `non_inconsistency`: No inconsistency. The compared statements are compatible after checking the population, definitions, time points, or context, including equivalent wording with no change in meaning or conduct. Example: week 12 and 12 weeks after baseline describe the same time point. Normally consider Disposition=exclude for this candidate.

- `indeterminate`: Indeterminate. The available evidence cannot support a more specific interpretation of the planned-versus-reported difference.

- `not_applicable`: Use only for an inactive judgment field or a non-retained candidate. It is not an issue verdict, missing evidence, or an unanswered applicable question. Blank inactive fields have the same effective value.

## Checker result

Required in checker stage. Keep answers unchanged for agree. Every other result needs a comment; disagreements or uncertainty also require resolved discussion before final delivery.

Scope: Required; completed Checker.

- `agree`: Accept the unchanged primary assessment. All eight effective final answers, including notes, must equal Primary. Mark Checker / final Complete as checker\_done. No comment is required.

- `agree_clarification`: Accept the main assessment with clarification. Edit relevant answers directly and explain in Checker comment.

- `disagree`: Disagree, proposal pending discussion. Recommend a different assessment, explain why in a comment, and enter proposed changes. The proposal is not final consensus until discussion is resolved.

- `unable`: Unable to resolve. The checker cannot settle the issue from the available information. State what remains uncertain in a comment and refer it for discussion.

## Checker comment

Explain the clarification, disagreement, or uncertainty in English. An unchanged agreement does not require a comment.

Scope: Required unless Checker result is agree.

## Discussion resolution

For disagree, unable, or any primary discuss, discuss together and select resolved. Record participants and the conclusion in Resolution note; update the final assessment.

Scope: Conditional; discussion.

- `pending`: Discussion not resolved. A required discussion is not yet settled. For an unchanged agreement this default can be left as-is because no separate resolution is required.

- `resolved`: Joint discussion resolved. Record the participants and agreed conclusion in Resolution note, update the proposed assessment, and do not leave disposition as discuss.

## Resolution note

Record participants and the agreed conclusion in English. Update proposed judgments and do not leave Disposition=discuss. Checker completion alone does not settle disagreement.

Scope: Required when resolved.

## Candidate key

Unique candidate identity used for matching, even after complete rows are reordered. Never edit this value.

Scope: Reference.

## Candidate title

Short candidate title. A candidate is an AI flag for human assessment, not a confirmed issue.

Scope: Reference.

## Source location

Where to check the source claim. Candidate sections include full catalog evidence and links to the original paper files.

Scope: Source reference; both roles.

## Primary assessment

Primary contains the original assessment. Preserve its eight answers and primary\_done at handoff. Copy the answers into Checker / final before editing final answers.

Scope: Reference.

## Relationships and final outcomes

The frozen primary relationship is never changed by a human domain selection. `S_W` describes within-document report comparisons, `S_C` cross-document report comparisons, `P_R` plan-versus-report comparisons, and `P_P` planning-material comparisons. Retain all secondary relationship records for context; use the frozen primary relationship for the outcome.

Assign exactly one outcome only after final readiness, using this order:

1. If final Disposition is not `retain`, use `not_eligible`. Final `discuss` is not allowed.
2. For retained `P_R`, use `protocol_descriptive`.
3. For retained `P_P`, use `plan_descriptive`.
4. For retained `S_C` or `S_W`, domain `statistical_results`, issue `confirmed_issue` or `probable_issue`, and substantiveness `substantive`, use `primary_temporal`.
5. For retained `S_C` or `S_W`, domain `report_internal_inconsistency` and inconsistency `substantive_inconsistency`, use `secondary_temporal`.
6. Otherwise use `not_eligible`.

P_R and P_P remain descriptive and never enter the temporal comparison. Downstream impact does not determine eligibility. AI suggestions are not human findings. Visible-answer checking is not blinded inter-rater reliability.
