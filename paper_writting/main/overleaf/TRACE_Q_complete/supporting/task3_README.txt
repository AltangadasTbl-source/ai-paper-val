TASK 3 — CONFIRMED STATISTICAL NOTES ANALYSIS

Start with task3_report.pdf, a concise article-style report (within 10 pages,
including tables and figures). The complete taxonomy and all 139 raw Notes,
exact excerpts, coding reasons, audit flags and source cells are retained in
the accompanying XLSX/CSV/JSON rather than repeated as a long PDF appendix.
The 20-slide presentation and Chinese speaker notes are under ../../slides/.
The previous full 49-page report and its sources are archived separately.

QUICK DATA ACCESS
statistical_issue_recategorization.xlsx: 139 confirmed statistical candidates,
the overlapping 37 substantive cases, taxonomy, overall and period summaries.
confirmed_statistical_notes_year_paper_candidate.csv: requested four-column
structure (year, paper, candidate, Notes) for the 139-case analytical corpus.
notes_year_paper_candidate.csv: complete 440-case source index, same structure.
all_notes.csv/json: complete source index with final/raw fields and provenance.
semantic_coding_final.csv/json: final audited 139-case coding; use this version.
taxonomy_final.json: final operational category rules and boundaries.
category_summary.csv: all/substantive counts, shares and paper denominators.
category_period_summary.csv: before (2018–2019) vs after (2024–2025).
category_year_summary.csv: individual-year descriptive profiles.
paper_category_counts.csv: all 44 papers by all seven categories, including zero.
category_primary_assignment_sensitivity.csv: sensitivity excluding the three
primary-ambiguous cases (136 confirmed, 34 substantive).

SCOPE AND PROVENANCE
Only retained, final-domain statistical_results, confirmed_issue candidates
with original S_C/S_W relationships enter text mining/coding: 139, of which 37
are substantive. Other domains are never lexically mined or recategorized.
The 440-record extraction is a provenance index; 301 cases are out of scope.

The user confirmed subsequent human review of the copied workbooks. Final
copied labels determine eligibility and substantive status. Raw Notes come from
earlier Claude Opus 5.5 high-effort review runs and are not human-written Notes.
All 413 retained Notes are blank in the copies. All raw Notes are nonempty.
Decision codes match across raw/copied workbooks; human-review provenance
depends on the user's confirmation, not this label agreement.
New mechanism categories are LLM-assisted and not separately human validated.
Neither coding nor audit independently re-verifies the trial calculations.

METHOD AND AUDIT FILES
text_mining_specification.json: normalization, tokens, stopwords and frequencies.
text_normalized_notes.json: only 139 eligible Notes, separate from verbatim text.
text_note_statistics.csv / text_word_bigram_frequencies.csv: only confirmed
statistical and nested substantive subsets. Frequencies are not mechanism rates;
stopwords remove no/not, OR case-folds to or, and single-letter P is excluded.
Semantic coding always uses full Notes with numbers, negation and qualifications.
semantic_coding_v1.*: provisional coding retained for the audit history only.
coding_audit_all.*: complete second-agent audit of all 139 Notes.
coding_audit_reconciliation.* / coding_audit_metadata.json: four boundary
disagreements, three provisional-label revisions, and three remaining primary
ambiguities. Shared taxonomy; no human or blinded reliability claim.
Source workbook/text hashes, exact XML values, independent R extraction checks
and deterministic-rerun results are saved in the extraction and validation files.

REPRODUCE FROM PROJECT ROOT (RUN EACH LINE IN ORDER)
python3 analysis/review_notes/extract_review_notes.py
python3 analysis/review_notes/build_semantic_coding_v1.py
python3 analysis/review_notes/coding_audit_reconcile.py
python3 analysis/review_notes/aggregate_semantic_categories.py
python3 slides/prepare_notes_outputs.py
python3 analysis/review_notes/build_task3_report.py

Semantic scripts materialize saved full-note judgments and reconciliation;
rerunning them is not a fresh model review or an automated keyword classifier.
Original workbooks, analysis tables and the manuscript are unchanged.
The full source-data environment is required to rerun extraction. The generated
task3_report.tex is self-contained and can be compiled separately using XeLaTeX.

SEPARATE TASKS
Task 1: ../domain_comparisons/ (the three other review domains, no text mining).
Task 2: ../workflow_detail/ (Workflow 1.6.2 roles, decisions and source locators).
