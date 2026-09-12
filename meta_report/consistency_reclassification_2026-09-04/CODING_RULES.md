# Post-hoc document-role reclassification

Scope: current highest-version package-level final_report MD, 45 packages in year folders 2018/2019/2024/2025. Preserve source candidate IDs and statuses; this is categorization of recorded candidate issues, not final error adjudication or a new source-first audit. User explicitly requests reuse of detailed validation records. All output outside paper packages.

Read every full candidate card. Consult current-version candidate ledger / verification / checker / source inventory for ambiguous roles, comparisons, mixed cards, plan amendments, potential duplicate issues. Record exact consulted paths. Do not classify from category or protocol keywords alone: a plan merely corroborating an internal mismatch is not a plan discrepancy.

Produce one JSON row per input key with fields:
- key, primary, relations (array), rationale (concrete English summary of discrepancy and role assignment), evidence_paths (array of consulted file paths beyond final report), ambiguity (string, empty if none), duplicate_of (key or empty), subtype (short issue mechanism).
Primary mutually exclusive values:
- P_R: actual candidate discrepancy between reported article/results supplement and protocol/SAP. Includes framing/prespecification mismatch; does NOT imply proven protocol violation.
- P_P: discrepancy solely inside protocol/SAP or between plan documents/versions.
- S_C: main vs non-plan supplement, or two different non-plan supplements.
- S_W: within one main article or one non-plan supplement, including arithmetic, statistical, labels, definition mismatch.
- OTHER: cannot assign to above; explain.
relations includes every substantive discrepancy relationship from [P_R,P_P,S_C,S_W,OTHER]. Use primary precedence P_R > P_P > S_C > S_W > OTHER for genuinely mixed candidates; do not include corroborating sources as discrepancy relations. Mark ambiguity for mixed cases.
Protocol/SAP document role follows content, not file named supp1/supp2. Internal inconsistencies inside one bound protocol bundle remain P_P even if distinct historical plan versions appear in that file. Submission means main + non-plan supplements operationally; protocol/SAP are separated analytically though physically submitted too.
subtype describes mechanism; preserve original category in input/merged ledger independently.
Uncertain alternatives and possible disclosed amendments must be noted in ambiguity; preserve candidate count regardless. Only mark duplicate_of when clearly identical underlying issue; near-related issues are not automatically duplicates. Do not silently split/merge source IDs.

Save year output as coded_YEAR.json and review_YEAR.md, with full coverage, counts, consulted evidence, boundary cases and likely duplicates. Source final report is always implicitly consulted; evidence_paths should document deeper reads. Counts must reconcile to input. Do not regenerate scientific validation workflow.

Clarification: use P_O for a substantive protocol/SAP vs another prospective operational document (e.g. manual of procedures) discrepancy when neither side is a main article/results report. This is protocol/SAP involvement, but not reported-results-vs-plan. P_P remains protocol/SAP-only. Precedence P_R > P_O > P_P > S_C > S_W > OTHER. Add evidence_state='not_reproduced' only if the final record explicitly says source mismatch was not reproduced; otherwise 'recorded_candidate'. Preserve the historical intended relationship for not_reproduced IDs, distinguish them in sensitivity results.

Additional category P_B: inconsistencies of historical/background empirical results presented inside protocol/SAP material. Separate these from current-study planning definitions/calculations (P_P) and current main/non-plan supplements (S_W). They contribute to broad protocol/SAP-material involvement, but never establish a current report-versus-plan discrepancy. Examples are PROVIDE background results inside ImmunoSep protocol and historical Ontario PICU figures used as planning background. Physical bundle and content-level role are both retained; stored direct page renders settle ambiguous boundaries.

Recheck status refinement: 'repaired_residual' when an original transcription was explicitly disproven but the corrected source values leave a different, conditional question. These stay in residual-candidate sensitivity counts; do not exclude by searching 'not reproduced' alone. For example 2025.24175 C005 (117 per arm, approximate attrition), C009 (24/31/33 sites). 'not_reproduced' removes only fully unsupported mismatch registrations from sensitivity numerator and denominator. This is an evidence-record distinction, not a final scientific validity adjudication.
