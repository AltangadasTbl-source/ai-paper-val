# Human adjudication v.2.1.5 — Design

This version updates v.2.1.4 with two vocabulary changes. Disposition now offers only retain, exclude, and discuss; out_of_scope is removed. The domain internal_nonstatistical is replaced by report_internal_inconsistency, defined by the report materials: inconsistencies within the main paper, within the updated supplement, or between those two documents. Its name does not restrict the domain to nonstatistical content. Use statistical_results when specifically assessing a statistical reporting error.

The new domain uses the existing Internal or plan assessment field (internalStatus). A retained candidate requires that assessment. Substantive report-internal inconsistencies in S_C/S_W keep the existing secondary_temporal outcome. Statistical-error criteria and the descriptive treatment of P_R/P_P are unchanged. Plan-material inconsistency remains a separate domain, despite sharing the assessment field.

All four annual workbooks and both 2019 examples use the new vocabulary in Codebook, dropdowns, cell comments, conditional formatting, default formulas, source suggestions, primary snapshots, summaries, and exported decisions. Pasted retired option codes are invalid in both primary and checker stages. Schema is xlsx-adjudication-7; version and revision are v.2.1.5.

The source catalog derives directly from v.2.1.4. Only the AI-suggested domain label changes on 130 records. All 412 candidate identities, evidence, descriptions, source links, and relationship codes are preserved. The catalog records the parent version, parent source signature, rename count, and new source signature. This is a terminology migration, not a re-adjudication of sources or imported human answers.

There are four annual templates with 45 C_<paper> sheets and the same 19-column layout as v.2.1.4. Primary review starts in each template; prepare-checker still creates the next working copy with a frozen primary snapshot, visible summaries, and empty checker inputs. The ready 2019 example provides 71 synthetic completed primary records and 71 pending checks. Original versions and completed inputs are not overwritten.

Regression checks cover the inherited two-stage workflow, exact layout preservation, the limited catalog rename, removal of old option codes from all six review files, rejection of pasted retired codes, and the new domain through completion, inheritance, and export. See [VALIDATION.md](VALIDATION.md) for measured results and desktop limitations.
