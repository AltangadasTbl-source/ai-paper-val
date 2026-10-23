TRACE-Q presentation — 17 slides, 3 sections

DELIVERABLES
trace_q_slides.tex: self-contained Beamer presentation for XeLaTeX on Overleaf. Tables, the TikZ chart and hidden Chinese Beamer notes are embedded
in this single TeX file; no project fonts, figures or tables are required.
Workflow slides have moved to workflow_1_6_2_EN.md and workflow_1_6_2_CN.md.
The former page 6 (44 trial packages) is preserved unchanged as page 2.
speech_notes_cn.tex / .txt / .json: Chinese spoken script, one notes
section per slide. Thumbnails are optional when a deck PDF is available.
../overleaf/TRACE_Q_complete/documents/task3_report.tex: concise Task 3 report source,
within 10 pages including tables and figures. Complete category boundaries
and all 139 Notes/coding decisions remain in the accompanying XLSX/CSV/JSON.
../analysis/review_notes/statistical_issue_recategorization.xlsx: reviewable
139-case coding, overlapping 37-case substantive subset, taxonomy and results.

SECTIONS
1. Paper and study design (slides 1–2)
2. Review codebook and Notes mining (slides 3–9)
3. Before/after publication-cohort comparisons (slides 10–17)

INTERPRETATION
Before = papers published in 2018–2019 (19 papers).
After = papers published in 2024–2025 (25 papers).
These labels do not identify a pandemic effect or classify recruitment dates.

Confirmed all: retained statistical_results, confirmed_issue, original S_C/S_W
relationship, regardless of substantiveness (139 candidates).
Confirmed substantive: same filter plus substantive (37).
The paper's principal endpoint also includes probable substantive issues (41).
The broader original report-material total of 149 includes 10 report-internal
issues and must not replace 139.

New domain comparisons use final domain labels and explicitly include original
P_R/P_P relations, unlike the original report-only endpoint. Report-internal
and plan-material broad outcomes count established substantive/minor findings;
protocol-report outcomes describe retained differences, not confirmed errors.
Sparse and indeterminate states are reported separately in the analysis files.

PROVENANCE AND TEXT-MINING SCOPE
The user confirmed later human review of copied R_Bulun workbooks. Their final
labels determine inclusion and substantiveness. Earlier raw Notes are authored
by Claude Opus 5.5 high-effort review runs. New mechanism coding is LLM-assisted,
with a complete second-agent audit; it is not newly human-validated coding.
Raw and copied decision codes match. All 413 retained Notes were cleared in the
copies, requiring recovery from the raw workbooks.

All 440 raw Notes are extracted as a provenance index. Only the 139 confirmed
statistical_results candidates and their nested 37 substantive cases enter
lexical mining or semantic recategorization. No other domain is text-mined.
The 139 cases receive seven primary categories; three retain explicit primary
ambiguity flags. Every human decision remains unchanged.

SOURCES AND CHECKS
Manuscript: ../manuscript/trace_q_draft.tex and supplement.tex.
Final labels: ../review_results_2_4_1_Rbulun_copy/*.xlsx.
Raw Notes: ../reviewer_runs_raw/20xx/R_Bulun/*.xlsx.
Frozen analysis: ../analysis/candidate_results.csv and candidate_provenance.csv.
Workflow source locators and role matrix: ../analysis/workflow_detail/.
Additional domain analyses: ../analysis/domain_comparisons/.
Extraction, taxonomy, reconciled coding and audit: ../analysis/review_notes/.

Current checks inspect the 17-frame/3-section source and all 17 Chinese note
mappings without rendering. Earlier analytical checks verified exact Notes
transfer, unchanged final labels and counts.
All 8 original comparisons reproduce; 32 exact permutation probabilities are
independently checked. Confidence intervals use 20,000 within-period paper
bootstrap resamples, seed 20261022. Text mechanism comparisons are descriptive.

UPDATE SOURCES WITHOUT RENDERING
python3 slides/prepare_extended_speech_notes_cn.py
python3 slides/make_standalone.py
python3 slides/build_speech_notes_cn.py

Local PDFs, previews and build files have been removed. The current font and
layout revision has only been checked statically; compile it on Overleaf.
The notes generator writes source only by default; --render is an explicit opt-in.

The slide build only compiles the delivered TeX. The verification script reads
the four final XLSX files directly and checks the paper counts and 32 exact
tests against the packaged analyses. Original relationship codes come from
overleaf/TRACE_Q_complete/data/candidate_provenance.csv. Bootstrap intervals
are preserved because their complete paper-level inputs match exactly.
review_results_verification.json records the workbook hashes and audit.
Legacy analysis-generation scripts require their original analysis inputs.

The full analysis reproduction order is in analysis/review_notes/README.txt.
Source manuscript, source workbooks and frozen analysis inputs are unchanged.
The earlier 15-slide version is preserved in archive/.

COMPILE ON OVERLEAF
Upload trace_q_slides.tex alone or use ../overleaf/TRACE_Q_Overleaf_ready.zip.
Select XeLaTeX and recompile from scratch after replacing an older source.
The source-only project also includes speech_notes_cn_main.tex and the reports.
Chinese notes compile without thumbnails. To add thumbnails, compile the deck
on Overleaf, download its PDF and upload it as trace_q_slides.pdf.

FONT AND LAYOUT REVISION
fix-cm enables the requested small math sizes. Explicit Latin Modern Mono bold,
italic and bold-italic faces avoid missing shapes. The workflow checker table is now in the Markdown guides. These changes are also applied
by make_standalone.py, so regenerating the source preserves them.

SPEECH REVISION
The spoken results now explicitly use review_results_2_4_1_Rbulun_copy.
All 440 final judgments match the existing analysis: 413 retained, 27 excluded,
139 confirmed statistical findings and 37 confirmed substantive findings.
The 413 retained Notes cells are blank. Seven-category mechanism coding and
historical explanatory examples are labelled supplementary prior Notes-based
analysis; they are not attributed to the final workbook Notes columns.
