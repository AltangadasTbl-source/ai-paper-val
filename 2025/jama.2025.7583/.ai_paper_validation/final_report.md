# Human Adjudication Report — jama.2025.7583

Source PDFs were preserved unchanged. This report is limited to supplied materials and is not a legal opinion.

## Package Manifest

| ID | Source / pages | Classification and scientific processing status | Record path |
|---|---|---|---|
| DOC-001-MAIN | `jama_shotar_2025_oi_250033_1750956987.75881.pdf` / 9 | Main article; audited pp. 1-9; preprocessing and scientific checks completed. | [document output](document_outputs/DOC-001-MAIN/) |
| DOC-002-PROTOCOL | `joi250033supp1_prod_1750956987.76581.pdf` / 63 | Protocol; Not Audited by Design; rights screen and inventory completed. | [document output](document_outputs/DOC-002-PROTOCOL/) |
| DOC-003-ADMIN | `joi250033supp3_prod_1750956987.77681.pdf` / 23 | Administrative material; Not Audited by Design; rights screen and inventory completed. | [document output](document_outputs/DOC-003-ADMIN/) |
| DOC-004-RESULTS-SUPP | `joi250033supp4_prod_1750956987.77981.pdf` / 15 | Results supplement; audited pp. 1-15 (results priority pp. 8-13); preprocessing and scientific checks completed. | [document output](document_outputs/DOC-004-RESULTS-SUPP/) |
| DOC-005-SAP | `joi250033supp5_prod_1750956987.78281.pdf` / 9 | Statistical analysis plan; Not Audited by Design; rights screen and inventory completed. | [document output](document_outputs/DOC-005-SAP/) |

Package limitation: the main article cites Supplement 2, but no corresponding PDF was supplied. This is not a scientific finding.

## AI Training Restriction Summary

This is a separate compliance screen, not part of the scientific findings. Permissions were assumed given under the package instruction for continued processing. No permission is inferred from documents with no located restriction.

| Document ID | Status | Exact evidence location | Human Compliance Review |
|---|---|---|---|
| DOC-001-MAIN | Explicit AI Training Restriction | PDF p. 1 footer (repeated pp. 1-9): “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes — assumed permission given for this workflow. |
| DOC-002-PROTOCOL | No AI Training Restriction Located in Provided Materials | PDF p. 1 footer (repeated pp. 1-63): “This document is the property of DRCI / APHP. Any reproduction is strictly forbidden.” The statement concerns reproduction, not AI training; metadata and all-page keyword screen found no AI-training language. | No |
| DOC-003-ADMIN | No AI Training Restriction Located in Provided Materials | Metadata; focused PDF pp. 1-2 and 22-23 inspection; all-page native-text keyword screen: no qualifying rights or AI-use language located. | No |
| DOC-004-RESULTS-SUPP | Explicit AI Training Restriction | PDF p. 1 footer (repeated pp. 1-15): “© 2025 American Medical Association. All rights reserved, including those for text and data mining, AI training, and similar technologies.” | Yes — assumed permission given for this workflow. |
| DOC-005-SAP | No AI Training Restriction Located in Provided Materials | Metadata; focused PDF pp. 1-2 and 8-9 inspection; all-page native-text keyword screen: no qualifying rights or AI-use language located. | No |

Detailed records: [DOC-001](document_outputs/DOC-001-MAIN/ai_training_restriction_record.md), [DOC-002](document_outputs/DOC-002-PROTOCOL/ai_training_restriction_record.md), [DOC-003](document_outputs/DOC-003-ADMIN/ai_training_restriction_record.md), [DOC-004](document_outputs/DOC-004-RESULTS-SUPP/ai_training_restriction_record.md), [DOC-005](document_outputs/DOC-005-SAP/ai_training_restriction_record.md).

## Scientific Findings

### 1. Inclusion label applied to excluded patients

- **Category / severity:** Presentation inconsistency / Minor.
- **Exact location:** DOC-001-MAIN, `jama_shotar_2025_oi_250033_1750956987.75881.pdf`, PDF p. 4, Figure 1 footnote a; DOC-004-RESULTS-SUPP, `joi250033supp4_prod_1750956987.77981.pdf`, PDF p. 8, eFigure 1 title and exclusion box.
- **Compared statements:** Figure 1 directs readers to reasons for excluding patients “with an inclusion criterion.” eFigure 1 repeats “reasons for excluding patients with an inclusion criterion,” while its `Excluded (n=317)` box includes `Other pre-specified non-inclusion criteria (n=164)`, `Patient refusal (n=101)`, `Other reasons (n=18)`, and `Unknown reasons (n=34)`.
- **Logical basis:** The label lacks a `not meeting` or `non-` qualifier despite the displayed non-inclusion and other exclusion categories. This is a localized labeling defect only; it does not establish incorrect counts, allocation, analyses, or conclusions.
- **Verification instruction:** Read the complete p. 4 footnote and p. 8 eFigure 1 title and four top-level categories; confirm that no `not meeting` or `non-` qualifier precedes `inclusion criterion`.

### 2. MAGIC-MT usual-care event count omitted

- **Category / severity:** Presentation inconsistency / Minor.
- **Exact location:** DOC-004-RESULTS-SUPP, `joi250033supp4_prod_1750956987.77981.pdf`, PDF p. 14, eTable 4, MAGIC-MT row, `Primary outcome` column.
- **Compared values/statements:** The cell states: `24 patients (6.7%) reached the primary outcome in the intervention group as compared to (9.9%) in the usual-care group (between-group difference, -3.3 percentage points; 95% confidence interval, -7.4 to 0.8; P = 0.10)`. No usual-care numerator appears before `(9.9%)`. The adjacent EMBOLISE and STEM rows display counts for both groups.
- **Logical basis:** One arm’s event count is absent, leaving the comparative sentence incomplete and preventing direct verification of the usual-care count from this table cell. The percentage and treatment-effect statistics remain displayed; no numerical contradiction or impact on conclusions is established.
- **Verification instruction:** Inspect the MAGIC-MT cell at native magnification; confirm no control numerator precedes `(9.9%)` and compare the two-arm count formatting in EMBOLISE and STEM immediately above.

## Rejected and Uncertain Candidates

**Rejected by evidence verification; not scientific findings.**

- **Treatment-type rows exceed the shared denominator** — DOC-001-MAIN PDF p. 5, Table 1. Although `146/163` plus `18/163` equals 164, mutual exclusivity at the patient level was not established; bilateral surgery could involve more than one procedure/opening.
- **Full-analysis-set/imputation labels beside observed denominators** — DOC-004-RESULTS-SUPP PDF pp. 9 and 15; resolved by DOC-001-MAIN PDF p. 6, Table 2 footnotes a-c. `24/162` and `33/157` are observed descriptors; the reported effect estimate is the multiply imputed ITT/full-analysis-set result.

**Uncertain model-dependent checks; not candidates or findings.**

- Exact adjusted/multiple-imputation regression calculations (DOC-001-MAIN pp. 3, 5-6; DOC-004-RESULTS-SUPP pp. 6, 9) require patient-level data and the imputation/model specification.
- Confidence-interval symmetry (DOC-001-MAIN p. 3 and p. 6 Table 2 footnotes b, g) is not an applicable error screen for bootstrap and GEE intervals.
- Exact interaction, GEE, and Wilcoxon P values (DOC-001-MAIN p. 6, Figure 2 and Table 2) cannot be reconstructed from the displayed aggregates alone.
- Observed fractions next to multiple-imputation labels (DOC-004-RESULTS-SUPP p. 9) can appear ambiguous alone but are resolved by DOC-001-MAIN p. 6, Table 2 footnotes a-c.

No verifier-stage or critic-stage candidate remained uncertain. Detailed dispositions are retained in [evidence verifier output](evidence_verifier_output.md), [critic output](critic_output.md), and [statistical checker output](statistical_consistency_checker_output.md).

## Human Adjudication Checklist

- [ ] Confirm each issue against the cited source PDF page, figure, table, and quoted text.
- [ ] Decide whether either Minor presentation inconsistency warrants correction; do not recast either as a participant-flow, numerical, methodological, or clinical error on this record.
- [ ] Retain rejected and uncertain items as non-findings unless new source evidence resolves their stated limitation.
- [ ] Review DOC-001-MAIN and DOC-004-RESULTS-SUPP under the applicable institutional permissions process; permissions were assumed for this workflow.
- [ ] Record the missing cited Supplement 2 as a package-completeness limitation if relevant to downstream review.
